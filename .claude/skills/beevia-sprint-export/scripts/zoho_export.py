#!/usr/bin/env python3
"""Export the Beevia sprint board from Zoho Sprints to CSV.

Reproduces the format Zoho's own UI export produces, so the output is a
drop-in replacement for a manual export and is consumed unchanged by the
`beevia-audit` skill.

Usage:
    python3 zoho_export.py --probe          # inspect the live API shape FIRST
    python3 zoho_export.py                  # write today's export
    python3 zoho_export.py --sprint 0702    # override the sprint filter
    python3 zoho_export.py --dry-run        # fetch + report, write nothing
    python3 zoho_export.py --date 2026-08-05  # backdate the filename

Exit codes:
    0  export written (or dry run succeeded)
    1  configuration or API error
    2  fetched successfully but zero items matched
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# --------------------------------------------------------------------------- #
# Output format — matched to Zoho's UI export, byte for byte.
# --------------------------------------------------------------------------- #

COLUMNS = [
    "Item Id", "Item Name", "Description", "Created On", "Sprint", "Created by",
    "Tags", "Completed On", "Assignee", "Status", "Epic", "Item Type",
    "Priority", "Start Date", "End Date", "Start After", "Duration",
    "Estimation Points", "Release", "Total Workhours", "Work hours per owner",
    "Work hours type", "Parent Id", "Sprint Type", "Sprint Start Date",
    "Sprint End Date", "Comments", "Created Time", "Last Modified",
    "Blocked by", "Blocked On",
]

# API keys per column, tried in order.
#
# VERIFIED against the live API (2026-08). Zoho item payloads carry *ids*, not
# labels — `statusId`, `projItemTypeId`, `projPriorityId`, `epicId`, and an
# `ownerId` ARRAY. `resolve_names()` folds the lookup tables in and writes the
# `*Name` keys listed first below, so the raw id is only ever a fallback.
FIELD_MAP: dict[str, list[str]] = {
    "Item Id":              ["itemId", "itemNo"],          # itemId = BVA-I72
    "Item Name":            ["itemName", "name", "title"],
    "Description":          ["description", "itemDescription", "desc"],
    "Created On":           ["createdTime", "createdDate", "createdOn"],
    "Sprint":               ["sprintName", "sprint", "sprintNo"],
    "Created by":           ["createdByName", "createdBy", "creator"],
    "Tags":                 ["tags", "tagNames", "labels"],
    "Completed On":         ["completedDate", "completedOn", "closedDate"],
    "Assignee":             ["assigneeName", "ownerName", "assignee", "owner"],
    "Status":               ["statusName", "status"],
    "Epic":                 ["epicName", "epic"],
    "Item Type":            ["itemTypeName", "itemType", "type"],
    "Priority":             ["priorityName", "priority"],
    "Start Date":           ["startDate", "plannedStartDate"],
    "End Date":             ["endDate", "plannedEndDate"],
    "Start After":          ["startAfter"],
    "Duration":             ["duration"],
    "Estimation Points":    ["points", "estimationPoints", "estimatePoints"],
    "Release":              ["releaseName", "release"],
    "Total Workhours":      ["totalWorkHours", "totalWorkhours"],
    "Work hours per owner": ["workHoursPerOwner", "workhoursPerOwner"],
    "Work hours type":      ["workHoursType", "workhoursType"],
    "Parent Id":            ["parentItemNo", "parentId", "parent"],
    "Sprint Type":          ["sprintTypeName", "sprintType"],
    "Sprint Start Date":    ["sprintStartDate"],
    "Sprint End Date":      ["sprintEndDate"],
    # The UI export writes comment BODIES as JSON here; the API returns only
    # `commentCount` on the item, so this stays blank rather than emitting a
    # number where a reader expects text.
    "Comments":             [],
    "Created Time":         ["createdTime", "createdDate"],
    "Last Modified":        ["lastModifiedTime", "lastModified", "modifiedTime"],
    "Blocked by":           ["blockedByObj", "blockedBy", "blockedByItems"],
    "Blocked On":           ["blockedOn"],
}

# Columns the API genuinely does not expose on these endpoints. Listing them
# here keeps the "unresolved column" warning honest — it should fire for
# mapping mistakes, not for data Zoho never sends.
KNOWN_UNAVAILABLE = {
    "Tags",                  # only `tagCount` is returned, never the names
    "Last Modified",         # absent from both list and detail payloads
    "Comments",              # only `commentCount`; bodies need a per-item call
    "Release",
}

# Project-level workhour settings. The UI export repeats them on every row but
# no API endpoint returns them, so they are emitted from config to keep the
# output diff-clean against a manual export. They are constants, not per-item
# data — if the project's workhour config changes, change them here.
CONSTANT_COLUMNS = {
    "Total Workhours":      ("EXPORT_TOTAL_WORKHOURS", "00:00/day"),
    "Work hours per owner": ("EXPORT_WORKHOURS_PER_OWNER", "00:00"),
    "Work hours type":      ("EXPORT_WORKHOURS_TYPE", "hrs/day"),
}

# Zoho renders sprint type as an int; the UI export writes the word.
SPRINT_TYPES = {1: "Upcoming", 2: "Start", 3: "Completed", 4: "Canceled"}

# Sprint listing defaults to UPCOMING ONLY. Every call must say otherwise.
ALL_SPRINT_TYPES = "[1,2,3,4]"

ZOHO_DATE = "%d/%b/%Y"
ZOHO_DATETIME = "%d/%b/%Y %I:%M %p"

# Columns rendered as date-time rather than date-only in the UI export.
DATETIME_COLUMNS = {"Created On", "Created Time", "Last Modified", "Completed On"}


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

def workspace_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, ".claude")) and os.path.basename(d) != ".claude":
            return d
        d = os.path.dirname(d)
    return os.getcwd()


ROOT = os.environ.get("BEEVIA_ROOT") or workspace_root()


def load_env() -> None:
    """Load ROOT/.env into os.environ without overwriting real env vars."""
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)


def need(key: str) -> str:
    v = os.environ.get(key, "").strip()
    if not v:
        die(f"missing required config: {key}\n"
            f"      Copy .env.example to .env and fill it in.")
    return v


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------------------------------- #
# Zoho API
# --------------------------------------------------------------------------- #

class Zoho:
    def __init__(self) -> None:
        self.dc = os.environ.get("ZOHO_DC", "com").strip().lstrip(".")
        self.accounts = f"https://accounts.zoho.{self.dc}"
        self.base = os.environ.get(
            "ZOHO_API_BASE", f"https://sprintsapi.zoho.{self.dc}/zsapi"
        ).rstrip("/")
        self.token: str | None = None
        # Zoho attaches a {userId: displayName} map to most responses rather
        # than a users endpoint. Accumulate it from every call so owner and
        # creator ids can be resolved without a dedicated lookup.
        self.seen_users: dict[str, str] = {}

    # -- auth -------------------------------------------------------------- #

    # Access tokens live ~1h. Cache to disk so repeated invocations (probing,
    # a failed run, an export retry) reuse one instead of refreshing each time
    # — Zoho rate-limits the REFRESH endpoint aggressively and will lock you
    # out for a while with "too many requests continuously".
    CACHE = ".zoho-token-cache.json"

    def _cache_path(self) -> str:
        return os.path.join(ROOT, self.CACHE)

    def _load_cached(self) -> str | None:
        try:
            with open(self._cache_path(), encoding="utf-8") as fh:
                blob = json.load(fh)
        except (OSError, json.JSONDecodeError):
            return None
        if blob.get("dc") != self.dc:
            return None
        # 5-minute safety margin against clock skew and in-flight requests.
        if blob.get("expires_at", 0) - 300 < dt.datetime.now().timestamp():
            return None
        return blob.get("access_token")

    def _store(self, token: str, expires_in: int) -> None:
        path = self._cache_path()
        try:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump({
                    "access_token": token,
                    "expires_at": dt.datetime.now().timestamp() + int(expires_in),
                    "dc": self.dc,
                }, fh)
            os.chmod(path, 0o600)     # it is a credential
        except OSError:
            pass                      # cache is an optimisation, not required

    def authenticate(self, force: bool = False) -> None:
        """Get an access token, from cache when possible."""
        if not force:
            cached = self._load_cached()
            if cached:
                self.token = cached
                return
        data = urllib.parse.urlencode({
            "refresh_token": need("ZOHO_REFRESH_TOKEN"),
            "client_id": need("ZOHO_CLIENT_ID"),
            "client_secret": need("ZOHO_CLIENT_SECRET"),
            "grant_type": "refresh_token",
        }).encode()
        req = urllib.request.Request(f"{self.accounts}/oauth/v2/token", data=data)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                payload = json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            if "too many requests" in body.lower():
                die("Zoho is rate-limiting token refresh.\n"
                    "      Wait ~10-30 minutes, then retry. The token cache "
                    f"({self.CACHE}) prevents this in normal use — it is only\n"
                    "      hit when many separate invocations each refresh.")
            die(f"token refresh failed ({e.code}): {body}")
        except urllib.error.URLError as e:
            die(f"cannot reach {self.accounts}: {e.reason}")

        if "access_token" not in payload:
            die(f"token refresh returned no access_token: {payload}\n"
                f"      Common causes: wrong ZOHO_DC for this account, "
                f"revoked refresh token, or scopes missing.")
        self.token = payload["access_token"]
        self._store(self.token, payload.get("expires_in", 3600))

    # -- requests ---------------------------------------------------------- #

    def try_get(self, path: str, **params) -> tuple[int, object]:
        """GET without dying. Returns (http_status, parsed_body_or_text).

        Status 0 means the request never completed (DNS, TLS, timeout).
        """
        url = f"{self.base}/{path.lstrip('/')}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={
            "Authorization": f"Zoho-oauthtoken {self.token}",
            "Accept": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode("utf-8", "replace")
                try:
                    payload = json.loads(body)
                except json.JSONDecodeError:
                    return r.status, body[:400]
                if isinstance(payload, dict):
                    names = payload.get("userDisplayName")
                    if isinstance(names, dict):
                        self.seen_users.update(names)
                return r.status, payload
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:400]
            try:
                return e.code, json.loads(body)
            except json.JSONDecodeError:
                return e.code, body
        except urllib.error.URLError as e:
            return 0, str(e.reason)

    def get(self, path: str, **params) -> dict:
        # VERIFIED: Zoho Sprints collection endpoints require `action=data`.
        # Without it every path returns `7404 Given URL is wrong`, which reads
        # like a bad path rather than a missing parameter.
        params.setdefault("action", "data")
        status, payload = self.try_get(path, **params)
        if status == 200:
            return payload if isinstance(payload, dict) else {"_": payload}
        if status in (401, 403):
            die(f"{status} on {path}\n      {payload}\n"
                f"      Check the OAuth scopes on the refresh token.")
        if status == 0:
            die(f"cannot reach {self.base}/{path}: {payload}")
        die(f"HTTP {status} on {self.base}/{path.lstrip('/')}: {payload}\n"
            f"      Run --discover to find the correct path shape.")

    def paginate(self, path: str, **params):
        """Yield rows across pages. Zoho uses 1-based `index` + `range`.

        Deduplicates on the row id: with `subitem=true` a page boundary can
        re-emit an item that also appears under its parent, which would
        otherwise produce duplicate CSV rows.
        """
        index, page_size, seen = 1, 100, 0
        emitted: set[str] = set()
        while True:
            payload = self.get(path, index=index, range=page_size, **params)
            rows = extract_rows(payload)
            if not rows:
                return
            for row in rows:
                rid = str(row.get("id") or "")
                if rid and rid in emitted:
                    continue
                if rid:
                    emitted.add(rid)
                yield row
            seen += len(rows)
            if len(rows) < page_size:
                return
            index += page_size
            if seen > 20000:            # runaway guard
                print("WARNING: stopped paginating at 20000 rows", file=sys.stderr)
                return


def decode_columnar(payload: dict) -> list[dict]:
    """Decode Zoho Sprints' columnar envelope into plain dicts.

    VERIFIED against the live API. Zoho does not return records as objects.
    It returns, for a resource `X`:

        "XJObj":  { "<id>": [v0, v1, v2, ...] }     records as positional arrays
        "X_prop": { "fieldName": <index>, ... }     the array's schema
        "XIds":   [ "<id>", ... ]                   ordering

    e.g. projects come back as
        projectJObj = {"1875...145": ["Beevia", "7", "2026-06-16T23:00:00.000Z", ...]}
        project_prop = {"projName": 0, "projNo": 1, "startDate": 2, ...}

    `userDisplayName` ({userId: name}) is folded in so owner/creator ids can be
    resolved to names for the CSV.
    """
    rows: list[dict] = []
    names = payload.get("userDisplayName") or {}

    for key in payload:
        if not key.endswith("JObj") or not isinstance(payload[key], dict):
            continue
        kind = key[:-4]                                   # projectJObj -> project
        prop = payload.get(f"{kind}_prop") or {}
        if not prop:
            continue
        order = payload.get(f"{kind}Ids") or list(payload[key])
        for rid in order:
            arr = payload[key].get(rid)
            if not isinstance(arr, list):
                continue
            row = {f: (arr[i] if i < len(arr) else None)
                   for f, i in prop.items() if isinstance(i, int)}
            row["id"] = rid
            for field in ("owner", "createdBy", "assignee", "ownerId"):
                val = row.get(field)
                if isinstance(val, str) and val in names:
                    row[f"{field}Name"] = names[val]
            rows.append(row)
    return rows


def extract_rows(payload) -> list:
    """Rows from a Zoho response, columnar or plain."""
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return []

    columnar = decode_columnar(payload)
    if columnar:
        return columnar

    best: list = []
    for value in payload.values():
        if isinstance(value, list) and value and isinstance(value[0], dict):
            if len(value) > len(best):
                best = value
        elif isinstance(value, dict):
            nested = extract_rows(value)
            if len(nested) > len(best):
                best = nested
    return best


# --------------------------------------------------------------------------- #
# Lookup tables
#
# Item payloads reference statuses, types, priorities and epics by id. These
# fetch the project's label tables once so every item can be resolved locally
# instead of per-item round trips.
# --------------------------------------------------------------------------- #

def _index_by(rows: list[dict], *id_keys: str) -> dict[str, dict]:
    """Index rows under every id key they expose.

    Zoho returns two different ids on these tables — a project-scoped row id
    (`id`) and a global type id (`itemTypeId`, `priorityId`) — and items may
    reference either. Indexing both avoids guessing which.
    """
    out: dict[str, dict] = {}
    for row in rows:
        for key in id_keys:
            val = row.get(key)
            if val:
                out[str(val)] = row
    return out


class Lookups:
    """Project label tables, fetched once per run."""

    def __init__(self) -> None:
        self.status: dict[str, dict] = {}
        self.item_type: dict[str, dict] = {}
        self.priority: dict[str, dict] = {}
        self.epic: dict[str, dict] = {}
        self.users: dict[str, str] = {}
        self.epic_scope_missing = False

    def load(self, z: "Zoho", team: str, project: str) -> None:
        base = f"team/{team}/projects/{project}"

        def fetch(path: str) -> list[dict]:
            status, payload = z.try_get(f"{base}/{path}",
                                        action="data", index=1, range=200)
            if status != 200:
                return []
            if isinstance(payload, dict):
                self.users.update(payload.get("userDisplayName") or {})
            return extract_rows(payload)

        self.status = _index_by(fetch("itemstatus/"), "id", "statusId")
        self.item_type = _index_by(fetch("itemtype/"), "id", "itemTypeId")
        self.priority = _index_by(fetch("priority/"), "id", "priorityId")

        # Epics need their own OAuth scope. Missing it is a config problem, not
        # a failure — degrade to a blank Epic column and say so once, loudly.
        status, payload = z.try_get(f"{base}/epic/",
                                    action="data", index=1, range=200)
        if status == 200:
            self.epic = _index_by(extract_rows(payload), "id", "epicId")
            if isinstance(payload, dict):
                self.users.update(payload.get("userDisplayName") or {})
        else:
            self.epic_scope_missing = True
            print("WARNING: cannot read epics "
                  f"(HTTP {status}) — the Epic column will be blank.\n"
                  "         The refresh token is missing ZohoSprints.epic.READ. "
                  "Re-authorise with\n"
                  "         that scope added to restore it.", file=sys.stderr)


def fetch_detail(z: "Zoho", team: str, project: str, sprint: str,
                 item_id: str, attempts: int = 4) -> dict | None:
    """One item's detail record, or None if it could not be fetched.

    Descriptions live only on this endpoint, so an export needs one call per
    item. Zoho throttles that burst — roughly half of a 120-item run came back
    empty without this retry — and it does so WITHOUT an error status, which is
    why the failure has to be detected by an empty result rather than a code.
    """
    import time
    delay = 0.6
    for attempt in range(attempts):
        status, payload = z.try_get(
            f"team/{team}/projects/{project}/sprints/{sprint}/item/{item_id}/",
            action="details")
        if status == 200:
            rows = extract_rows(payload)
            if rows:
                return rows[0]
        if attempt < attempts - 1:
            time.sleep(delay)
            delay *= 2          # 0.6s, 1.2s, 2.4s
    return None


def sweep_modified(z: "Zoho", team: str, project: str, sprint: str,
                   since: dt.date, until: dt.date, tz: str = "+01:00",
                   ) -> dict[str, str]:
    """Recover each item's last-modified DATE by filtering one day at a time.

    `Last Modified` is not a field on any endpoint, but `I-modifiedon` IS a
    supported filter — so the value can be recovered by asking "which items were
    modified on day D?" for each day and keeping the latest hit per item.

    The filter shape is easy to get wrong and fails with a bare 400:

        filter={"queryType":1,"jsontmpl":"item_default",
                "I-modifiedon":[["<start>","<end>"]]}      <- range is NESTED

    The outer array is a list of CONDITIONS, each of which may be a keyword
    ("today") or a [start, end] pair. Passing the pair at the top level — the
    obvious reading — is rejected.

    Costs one request per day in the window, not one per item.
    Returns {zohoItemId: "YYYY-MM-DD"}; day precision only, since narrowing to
    a time would take a bisection per item and bulk edits carry no audit record
    to borrow an exact stamp from.
    """
    found: dict[str, str] = {}
    day = since
    while day <= until:
        window = json.dumps({
            "queryType": 1,
            "jsontmpl": "item_default",
            "I-modifiedon": [[f"{day.isoformat()}T00:00:00{tz}",
                              f"{day.isoformat()}T23:59:59{tz}"]],
        })
        status, payload = z.try_get(
            f"team/{team}/projects/{project}/sprints/{sprint}/item/",
            action="data", index=1, range=500, subitem="true", filter=window)
        if status == 200 and isinstance(payload, dict):
            for item_id in (payload.get("itemIds") or []):
                found[str(item_id)] = day.isoformat()   # later days overwrite
        day += dt.timedelta(days=1)
    return found


def fetch_activity(z: "Zoho", team: str, project: str, sprint: str,
                   item_id: str) -> list[dict]:
    """An item's audit trail, newest last.

    `.../item/{id}/activity/` returns a per-day envelope:

        auditJObj: { "<day>": { auditObj: { "<auditId>": [ ...positional... ] } } }
        audit_prop: { "action": 0, "actiontime": 7, "actionby": 5, ... }

    NOTE this is NOT a substitute for the export's `Last Modified` column — see
    `write_activity()`. It records discrete audited actions, and bulk board
    operations do not produce one.
    """
    status, payload = z.try_get(
        f"team/{team}/projects/{project}/sprints/{sprint}/item/{item_id}"
        f"/activity/", index=1, range=200)
    if status != 200 or not isinstance(payload, dict):
        return []
    prop = payload.get("audit_prop") or {}
    if not prop:
        return []
    users = payload.get("userDisplayName") or {}
    out: list[dict] = []
    for block in (payload.get("auditJObj") or {}).values():
        for arr in (block.get("auditObj") or {}).values():
            if not isinstance(arr, list):
                continue
            rec = {f: (arr[i] if i < len(arr) else None)
                   for f, i in prop.items() if isinstance(i, int)}
            actor = rec.get("actionby")
            rec["actionByName"] = users.get(str(actor), actor)
            out.append(rec)
    out.sort(key=lambda r: str(r.get("actiontime") or ""))
    return out


def write_activity(path: str, activity: dict[str, list[dict]]) -> None:
    """Write the audit trails beside the CSV, as JSON.

    Kept out of the CSV on purpose: the export's 31 columns are fixed to match
    Zoho's UI output byte for byte, and this is strictly extra signal.

    It exists because `Last Modified` cannot be recovered (see SKILL.md) and
    this is the accurate replacement for what that column was being used for —
    a real, timestamped status-transition history per item, rather than a single
    stamp that bulk operations overwrite.
    """
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(activity, fh, indent=1, default=str)
    os.replace(tmp, path)


def link_parents(rows: list[dict]) -> None:
    """Fill `parentItemNo` with the parent's composed id (e.g. BVA-I72).

    Sub-items reference their parent by internal id; the UI export shows the
    human item id. Call AFTER `resolve_names`, which is what writes `itemId`.
    """
    by_id = {str(r.get("id")): r.get("itemId") for r in rows if r.get("id")}
    for r in rows:
        parent = r.get("immediateParentId") or r.get("parentItem")
        if parent and str(parent) not in ("-1", ""):
            label = by_id.get(str(parent))
            if label:
                r["parentItemNo"] = label


def strip_html(value: str) -> str:
    """Zoho stores descriptions as HTML; the UI export writes plain text.

    Tags are removed WITHOUT substituting whitespace, which is what Zoho's own
    exporter does. That glues words across a tag boundary — "an invite<br>link"
    becomes "an invitelink" — and it is reproduced deliberately: this file is
    meant to be a drop-in replacement for a manual export, and inserting the
    missing space would make every description differ on every future diff.
    """
    import html
    import re
    text = re.sub(r"<[^>]+>", "", value)
    text = html.unescape(text).replace("\xa0", " ")
    # Raw newlines inside the stored markup are dropped too, not turned into
    # spaces — same reasoning, and the source is Word-pasted HTML where the
    # line breaks are formatting artefacts rather than content.
    text = text.replace("\r", "").replace("\n", "")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def resolve_names(item: dict, lk: Lookups, prefix: str) -> None:
    """Fold lookup labels into an item, in place.

    Writes the `*Name` keys FIELD_MAP reads first, so the CSV shows labels
    rather than the opaque ids the API returns.
    """
    st = lk.status.get(str(item.get("statusId")))
    if st:
        item["statusName"] = st.get("statusName")

    it = lk.item_type.get(str(item.get("projItemTypeId")))
    if it:
        item["itemTypeName"] = it.get("itemTypeName")

    pr = lk.priority.get(str(item.get("projPriorityId")))
    if pr:
        item["priorityName"] = pr.get("priorityName")

    ep = lk.epic.get(str(item.get("epicId")))
    if ep:
        item["epicName"] = (ep.get("epicName") or ep.get("name")
                            or ep.get("itemName"))

    # `ownerId` is an array; the UI export shows a single assignee, or blank.
    owners = item.get("ownerId")
    if isinstance(owners, list):
        names = [lk.users.get(str(o)) for o in owners]
        names = [n for n in names if n]
        if names:
            item["assigneeName"] = ", ".join(names)
    elif isinstance(owners, str) and lk.users.get(owners):
        item["assigneeName"] = lk.users[owners]

    if item.get("createdBy") and not item.get("createdByName"):
        item["createdByName"] = lk.users.get(str(item["createdBy"]))

    # Item Id is composed, never returned: <projectPrefix>-<typePrefix><itemNo>
    # e.g. BVA + I + 72 -> BVA-I72. The type prefix comes from the item type;
    # the project prefix is not exposed by the API at all (see ZOHO_ITEM_PREFIX).
    if item.get("itemNo") is not None:
        type_prefix = (it or {}).get("prefix") or "I"
        item["itemId"] = f"{prefix}-{type_prefix}{item['itemNo']}" if prefix \
            else f"{type_prefix}{item['itemNo']}"

    if isinstance(item.get("description"), str):
        item["description"] = strip_html(item["description"])

    stype = item.get("sprintType")
    if isinstance(stype, int) or (isinstance(stype, str) and stype.isdigit()):
        item["sprintTypeName"] = SPRINT_TYPES.get(int(stype), str(stype))


# --------------------------------------------------------------------------- #
# Field extraction
# --------------------------------------------------------------------------- #

def pick(item: dict, column: str) -> str:
    """First non-empty candidate key for a column, normalised to a string."""
    if column in CONSTANT_COLUMNS:
        env_key, default = CONSTANT_COLUMNS[column]
        return os.environ.get(env_key, default)
    for key in FIELD_MAP.get(column, []):
        if key in item and item[key] not in (None, "", [], {}):
            return stringify(item[key], column)
    return ""


# Zoho writes "-1" for "no value" on date, duration and reference fields.
# Rendered literally it looks like real data.
#
# "None" is deliberately NOT here: it is a real priority label in this project,
# and treating it as null blanked the Priority column on every row.
NULL_SENTINELS = {"-1", "-1.0", "null"}

# Counts the UI export leaves blank when zero rather than printing "0".
BLANK_WHEN_ZERO = {"Comments"}


def export_tz() -> dt.tzinfo | None:
    """Timezone the timestamps are rendered in.

    Zoho's UI export renders in the exporting user's Zoho profile timezone, not
    UTC, so a run on a UTC box would otherwise be off by the offset. Set
    EXPORT_TZ (an IANA name) to pin it; falls back to the machine's local zone.
    """
    name = os.environ.get("EXPORT_TZ", "").strip()
    if not name:
        return None                      # local time
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(name)
    except Exception:
        print(f"WARNING: unknown EXPORT_TZ {name!r} — using local time",
              file=sys.stderr)
        return None


def format_iso(value: str, column: str) -> str | None:
    """Render an ISO-8601 instant the way the UI export does."""
    text = value.replace("Z", "+00:00")
    try:
        stamp = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if stamp.tzinfo is not None:
        stamp = stamp.astimezone(export_tz())
    # A date-only source (the --modified sweep resolves to a day, not a time)
    # must not gain a fabricated "12:00 AM".
    date_only = "T" not in text
    fmt = ZOHO_DATE if date_only or column not in DATETIME_COLUMNS \
        else ZOHO_DATETIME
    # Zoho prints "05/Aug/2026 05:23 PM" — no zero-padding oddities, but
    # %I gives a leading zero on Linux, matching the sample.
    return stamp.strftime(fmt)


def stringify(value, column: str) -> str:
    if isinstance(value, str) and value.strip() in NULL_SENTINELS:
        return ""
    if isinstance(value, (int, float)) and value == -1:
        return ""
    if column in BLANK_WHEN_ZERO and value in (0, "0"):
        return ""
    if isinstance(value, str) and re.match(r"^\d{4}-\d{2}-\d{2}", value):
        rendered = format_iso(value, column)
        if rendered is not None:
            return rendered
    if isinstance(value, list):
        parts = []
        for v in value:
            if isinstance(v, dict):
                parts.append(str(v.get("name") or v.get("itemNo") or
                                 v.get("id") or ""))
            else:
                parts.append(str(v))
        return ", ".join(p for p in parts if p)
    if isinstance(value, dict):
        return str(value.get("name") or value.get("itemNo") or
                   value.get("id") or "")
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        # Zoho returns epoch milliseconds for timestamps.
        if column in DATETIME_COLUMNS or "Date" in column:
            return format_epoch(value, column)
        return str(value)
    if isinstance(value, str) and value.isdigit() and len(value) == 13:
        if column in DATETIME_COLUMNS or "Date" in column:
            return format_epoch(int(value), column)
    return str(value)


def format_epoch(ms, column: str) -> str:
    try:
        stamp = dt.datetime.fromtimestamp(float(ms) / 1000.0)
    except (ValueError, OSError, OverflowError):
        return str(ms)
    fmt = ZOHO_DATETIME if column in DATETIME_COLUMNS else ZOHO_DATE
    return stamp.strftime(fmt)


# --------------------------------------------------------------------------- #
# CSV writing
# --------------------------------------------------------------------------- #

def write_csv(path: str, items: list[dict], meta: dict) -> None:
    """Write with a UTF-8 BOM, CRLF endings and Zoho's 5-row preamble.

    All three details matter: the audit script reads with utf-8-sig and locates
    the header by finding `Item Id`, and a diff against a manual export should
    show only data changes.
    """
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, lineterminator="\r\n", quoting=csv.QUOTE_MINIMAL)
        pad = len(COLUMNS) - 2
        for label, value in (
            ("Team Name", meta["team"]),
            ("Project Name", meta["project"]),
            ("Exported By", meta["exported_by"]),
            ("Date", meta["exported_at"]),
            ("Filter", meta["filter"]),
        ):
            w.writerow([label, value] + [""] * pad)
        w.writerow(COLUMNS)
        for item in items:
            w.writerow([pick(item, c) for c in COLUMNS])
    os.replace(tmp, path)


# --------------------------------------------------------------------------- #
# Probe
# --------------------------------------------------------------------------- #

def id_of(row: dict) -> str:
    """Best-effort identifier from a Zoho row, without assuming a key name."""
    for k in ("id", "teamId", "zsoid", "projectId", "sprintId", "itemId",
              "prefixId", "portalId"):
        if row.get(k):
            return str(row[k])
    # Fall back to any key that looks like an id and holds a long number.
    for k, v in row.items():
        if k.lower().endswith("id") and isinstance(v, (str, int)) and \
                str(v).isdigit() and len(str(v)) >= 6:
            return str(v)
    return ""


def name_of(row: dict) -> str:
    # `projName` / `sprintName` are the columnar field names Zoho actually uses.
    for k in ("name", "projName", "sprintName", "itemName", "teamName",
              "projectName", "displayName", "title", "portalName"):
        if row.get(k):
            return str(row[k])
    return ""


def dump_rows(label: str, payload, limit: int = 15) -> list:
    """Print a response's real structure — envelope keys, then rows."""
    rows = extract_rows(payload)
    if isinstance(payload, dict):
        print(f"   envelope keys: {list(payload)[:12]}")
    print(f"   rows found: {len(rows)}")
    if rows:
        print(f"   row keys    : {sorted(rows[0])[:18]}")
        for r in rows[:limit]:
            i, n = id_of(r), name_of(r)
            print(f"     - id={i or '?':<14} name={n or '?'}")
    else:
        preview = json.dumps(payload, default=str)[:400]
        print(f"   raw: {preview}")
    return rows


def probe(z: Zoho) -> int:
    """Dump the live API shape so endpoints and FIELD_MAP can be verified.

    Prints the ACTUAL keys returned rather than guessing at them — Zoho's
    field naming is not fully documented and varies by plan and API version.
    """
    print(f"API base : {z.base}")
    print(f"Accounts : {z.accounts}\n")

    team = os.environ.get("ZOHO_TEAM_ID", "").strip()
    project = os.environ.get("ZOHO_PROJECT_ID", "").strip()

    if team:
        print(f"== teams (using configured ZOHO_TEAM_ID={team}) ==")
    else:
        print("== teams ==")
        # Zoho has used several spellings for this collection over time.
        for path in ("teams/", "team/", "portals/", "myteams/"):
            print(f"\n   -- GET {path}")
            try:
                rows = dump_rows(path, z.get(path))
            except SystemExit:
                print("   (request failed — trying next)")
                continue
            if rows:
                team = id_of(rows[0])
                if team:
                    print(f"   -> first team id: {team}")
                    break
        if not team:
            print("\n   Could not resolve a team id automatically.")
            print("   In Zoho Sprints the WORKSPACE id is the team id. Find it in")
            print("   the browser URL while viewing the board, then set:")
            print("       ZOHO_TEAM_ID=<workspace id>")
            return 1

    print(f"\n== projects (team {team}) ==")
    projects = dump_rows("projects", z.get(f"team/{team}/projects/"))
    if not project and projects:
        project = id_of(projects[0])
        print(f"   -> first project id: {project}")
    if not project:
        print("   (none — set ZOHO_PROJECT_ID)")
        return 1

    print(f"\n== lookups (project {project}) ==")
    lookups = Lookups()
    lookups.load(z, team, project)
    print(f"   statuses={len(set(map(id, lookups.status.values())))} "
          f"itemTypes={len(set(map(id, lookups.item_type.values())))} "
          f"priorities={len(set(map(id, lookups.priority.values())))} "
          f"epics={len(set(map(id, lookups.epic.values())))} "
          f"users={len(lookups.users)}")

    print(f"\n== sprints (project {project}) ==")
    sprints = dump_rows("sprints",
                        z.get(f"team/{team}/projects/{project}/sprints/",
                              type=ALL_SPRINT_TYPES))
    if not sprints:
        print("   NOTE: an empty list here usually means the `type` filter was "
              "omitted —\n         Zoho then returns upcoming sprints only.")
        return 1

    sid = sprints[0].get("sprintId") or id_of(sprints[0])
    print(f"\n== item keys (sprint {sid}) ==")
    items = extract_rows(
        z.get(f"team/{team}/projects/{project}/sprints/{sid}/item/",
              index=1, range=1))
    if not items:
        print("   (no items returned)")
        return 1

    item = items[0]
    status, payload = z.try_get(
        f"team/{team}/projects/{project}/sprints/{sid}/item/{item.get('id')}/",
        action="details")
    if status == 200:
        detail = extract_rows(payload)
        if detail:
            for k, v in detail[0].items():
                if v not in (None, "", [], {}):
                    item[k] = v
    # Mirror what main() does, or the report blames the mapping for context
    # the export supplies separately.
    sprint = sprints[0]
    item.setdefault("sprintName", sprint.get("sprintName"))
    item.setdefault("sprintStartDate", sprint.get("startDate"))
    item.setdefault("sprintEndDate", sprint.get("endDate"))
    item.setdefault("sprintType", sprint.get("sprintType"))
    lookups.users.update(z.seen_users)
    resolve_names(item, lookups, os.environ.get("ZOHO_ITEM_PREFIX", "").strip())

    for k, v in sorted(item.items()):
        print(f"   {k:30} {str(v)[:54].replace(chr(10), ' ')}")

    # A column is only a MAPPING problem when none of its candidate keys exist
    # on the item at all. A key that is present but holds "" or Zoho's "-1"
    # sentinel is real data, and reporting it as unresolved sends you hunting
    # for a bug that is not there.
    print("\n== FIELD_MAP coverage ==")
    unmapped, empty = [], []
    for c in COLUMNS:
        if c in CONSTANT_COLUMNS or pick(item, c):
            continue
        keys = FIELD_MAP.get(c, [])
        (empty if any(k in item for k in keys) else unmapped).append(c)

    filled = len(COLUMNS) - len(unmapped) - len(empty)
    print(f"   populated {filled}/{len(COLUMNS)} on this item")
    if empty:
        print(f"   mapped, empty on this item: {empty}")
    known = [c for c in unmapped if c in KNOWN_UNAVAILABLE]
    real = [c for c in unmapped if c not in KNOWN_UNAVAILABLE]
    if known:
        print(f"   not exposed by the API (expected blank): {known}")
    if real:
        print(f"   UNRESOLVED — likely a real mapping gap: {real}")
        print("   -> add each real key to the FRONT of that column's FIELD_MAP list")
    return 0


def raw(z: Zoho, path: str) -> int:
    """Dump one endpoint verbatim. For exploring undocumented shapes."""
    status, payload = z.try_get(path)
    print(f"HTTP {status}")
    print(json.dumps(payload, indent=2, default=str)[:8000]
          if not isinstance(payload, str) else payload[:8000])
    return 0 if status == 200 else 1


def discover(z: Zoho) -> int:
    """Find which endpoint shapes this account actually serves.

    Zoho Sprints' path layout differs by plan and API generation, and a wrong
    guess returns `7404 Given URL is wrong` rather than anything diagnostic.
    This tries a bounded set of candidates and reports what answers, turning
    the question into evidence instead of guesswork.
    """
    team = os.environ.get("ZOHO_TEAM_ID", "").strip()
    print(f"base: {z.base}")
    print(f"team: {team or '(unset)'}\n")

    # Ordered cheapest-first. `action=data` is a Zoho convention some
    # collection endpoints require.
    candidates: list[tuple[str, dict]] = [
        ("teams/", {}),
        ("teams/", {"action": "data"}),
        ("team/", {}),
        ("myteams/", {}),
        ("portals/", {}),
        ("zsapi/teams/", {}),
    ]
    if team:
        candidates += [
            (f"team/{team}/projects/", {}),
            (f"team/{team}/projects/", {"action": "data"}),
            (f"team/{team}/project/", {}),
            (f"teams/{team}/projects/", {}),
            (f"team/{team}/projects/", {"index": 1, "range": 10}),
            (f"portal/{team}/projects/", {}),
            (f"team/{team}/", {}),
            (f"team/{team}/myprojects/", {}),
        ]

    ok: list[str] = []
    for path, params in candidates:
        status, payload = z.try_get(path, **params)
        label = path + (f"?{urllib.parse.urlencode(params)}" if params else "")
        if status == 200:
            rows = extract_rows(payload)
            keys = list(payload)[:8] if isinstance(payload, dict) else "list"
            print(f"  200  {label}\n       envelope={keys} rows={len(rows)}")
            if rows:
                print(f"       row keys={sorted(rows[0])[:14]}")
            ok.append(label)
        else:
            msg = payload.get("message") if isinstance(payload, dict) else payload
            print(f"  {status:<4} {label}   {str(msg)[:60]}")

    print()
    if ok:
        print(f"WORKING: {ok}")
        print("-> update the paths in probe()/main() to the shape that answered.")
        return 0
    print("Nothing answered 200. Next steps:")
    print("  1. Confirm ZOHO_DC matches the account (tokens are per data centre).")
    print("  2. Confirm the refresh token carries the ZohoSprints.*.READ scopes.")
    print("  3. Open a board in the browser and copy the id from the URL.")
    print("  4. Try a path directly:  --raw 'teams/'")
    return 1


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true",
                    help="dump live API structure and exit")
    ap.add_argument("--discover", action="store_true",
                    help="try candidate endpoint shapes and report which answer")
    ap.add_argument("--raw", metavar="PATH",
                    help="GET one API path and dump the raw JSON, e.g. "
                         "--raw 'team/910540998/projects/'")
    ap.add_argument("--sprint", help="sprint name filter (default ZOHO_SPRINT_FILTER)")
    ap.add_argument("--date", help="date for the filename, YYYY-MM-DD (default today)")
    ap.add_argument("--out", help="output directory (default sprint-board-exports/)")
    ap.add_argument("--dry-run", action="store_true", help="fetch but do not write")
    ap.add_argument("--no-descriptions", action="store_true",
                    help="skip the per-item detail fetch (faster, blank Description)")
    ap.add_argument("--activity", action="store_true",
                    help="also write per-item audit trails to a sidecar JSON "
                         "(accurate status-transition timestamps; adds ~1 call/item)")
    ap.add_argument("--modified", action="store_true",
                    help="recover the Last Modified column by date-sweeping "
                         "I-modifiedon (day precision; ~1 call per day in sprint)")
    args = ap.parse_args()

    load_env()
    z = Zoho()
    z.authenticate()

    if args.discover:
        return discover(z)
    if args.raw:
        return raw(z, args.raw)
    if args.probe:
        return probe(z)

    team = need("ZOHO_TEAM_ID")
    project = need("ZOHO_PROJECT_ID")
    prefix = os.environ.get("ZOHO_ITEM_PREFIX", "").strip()
    sprint_filter = (args.sprint or os.environ.get("ZOHO_SPRINT_FILTER", "")).strip()

    lookups = Lookups()
    lookups.load(z, team, project)

    # VERIFIED: without `type`, Zoho lists ONLY UPCOMING sprints and returns
    # `{"sprintIds": []}` — a 200 with no rows, which reads like an empty
    # project rather than a filtered view. Ask for all four states explicitly.
    sprints = extract_rows(z.get(f"team/{team}/projects/{project}/sprints/",
                                 type=ALL_SPRINT_TYPES))
    if not sprints:
        die("no sprints returned — run --probe to check ids and endpoints")

    if sprint_filter:
        selected = [s for s in sprints
                    if sprint_filter.lower() in
                    str(s.get("name") or s.get("sprintName") or "").lower()]
        if not selected:
            names = [str(s.get("name") or s.get("sprintName")) for s in sprints]
            die(f"no sprint matches {sprint_filter!r}. Available: {names}")
    else:
        selected = sprints

    items: list[dict] = []
    activity: dict[str, list[dict]] = {}
    for s in selected:
        sid = s.get("sprintId") or s.get("id")
        name = s.get("sprintName") or s.get("name") or str(sid)
        # VERIFIED: without `subitem=true` the API returns ROOT ITEMS ONLY.
        # For sprint 0702 that is 54 Stories; the 66 child Tasks are silently
        # omitted, so the export would look complete while missing 55% of the
        # board. The UI export includes both.
        rows = list(z.paginate(
            f"team/{team}/projects/{project}/sprints/{sid}/item/",
            subitem="true"))
        # Carry sprint context onto each item; item payloads omit all of it.
        for r in rows:
            r.setdefault("sprintName", name)
            r.setdefault("sprintStartDate", s.get("startDate"))
            r.setdefault("sprintEndDate", s.get("endDate"))
            r.setdefault("sprintType", s.get("sprintType") or s.get("type"))

        # Descriptions live only on the per-item detail endpoint, so this is an
        # unavoidable N+1. It roughly doubles runtime; --no-descriptions skips
        # it when only the board state is wanted.
        if not args.no_descriptions:
            failed: list[str] = []
            for n, r in enumerate(rows, 1):
                detail = fetch_detail(z, team, project, sid, str(r.get("id")))
                if detail is None:
                    failed.append(r.get("itemNo") or str(r.get("id")))
                else:
                    # Detail is authoritative but sparser; never let it blank a
                    # field the list payload already filled.
                    for k, v in detail.items():
                        if v not in (None, "", [], {}):
                            r[k] = v
                if n % 25 == 0:
                    print(f"    …{n}/{len(rows)} descriptions", flush=True)
            if failed:
                # Silence here would ship a half-empty Description column that
                # reads as "these items have no description".
                print(f"WARNING: {len(failed)}/{len(rows)} detail fetches failed "
                      f"after retries — those descriptions are BLANK, not empty.",
                      file=sys.stderr)
                print(f"         items: {', '.join(map(str, failed[:15]))}"
                      f"{' …' if len(failed) > 15 else ''}", file=sys.stderr)
                print("         Re-run to fill them, or use --no-descriptions "
                      "to skip the column entirely.", file=sys.stderr)

        # Owner names arrive on the item payload itself, not the lookup tables.
        lookups.users.update(z.seen_users)
        for r in rows:
            resolve_names(r, lookups, prefix)
        link_parents(rows)

        if args.modified:
            # Sweep from the sprint's start (items can be modified before it
            # begins, so back off a fortnight) to today.
            began = str(s.get("startDate") or "")[:10]
            try:
                first = dt.date.fromisoformat(began) - dt.timedelta(days=14)
            except ValueError:
                first = dt.date.today() - dt.timedelta(days=60)
            stamps = sweep_modified(z, team, project, sid,
                                    first, dt.date.today())
            for r in rows:
                got = stamps.get(str(r.get("id")))
                if got:
                    r["lastModifiedTime"] = got
            print(f"    modified dates recovered for "
                  f"{sum(1 for r in rows if r.get('lastModifiedTime'))}/{len(rows)}",
                  flush=True)

        if args.activity:
            for n, r in enumerate(rows, 1):
                trail = fetch_activity(z, team, project, sid, str(r.get("id")))
                if trail:
                    activity[r.get("itemId") or str(r.get("id"))] = trail
                if n % 25 == 0:
                    print(f"    …{n}/{len(rows)} audit trails", flush=True)

        print(f"  sprint {name}: {len(rows)} items")
        items.extend(rows)

    if not items:
        print("No items matched — nothing written.", file=sys.stderr)
        return 2

    stamp = (dt.datetime.strptime(args.date, "%Y-%m-%d").date()
             if args.date else dt.date.today())
    out_dir = args.out or os.path.join(ROOT, "sprint-board-exports")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"beevia-sprint-board-{stamp:%Y-%m-%d}.csv")

    meta = {
        "team": os.environ.get("EXPORT_TEAM_NAME", ""),
        "project": os.environ.get("EXPORT_PROJECT_NAME", ""),
        "exported_by": os.environ.get("EXPORT_EXPORTED_BY", ""),
        "exported_at": dt.datetime.now().strftime(ZOHO_DATETIME),
        "filter": (f"Sprints Contains {sprint_filter}" if sprint_filter
                   else "All Sprints"),
    }

    # Report unresolved columns loudly — a silently blank column looks like
    # real data ("no estimates set") rather than a mapping gap.
    # Only a column whose candidate keys are ABSENT from every item is a
    # mapping gap. A key that is present but holds "" or Zoho's "-1" sentinel
    # is real data — most of this board genuinely has no dates or blockers, and
    # warning about those trained the reader to ignore the warning entirely.
    sample = items[:50]
    blank = []
    for c in COLUMNS:
        if c in KNOWN_UNAVAILABLE or c in CONSTANT_COLUMNS:
            continue
        if c == "Epic" and lookups.epic_scope_missing:
            continue
        if c == "Description" and args.no_descriptions:
            continue        # deliberately skipped, not a mapping gap
        if any(pick(i, c) for i in sample):
            continue
        if not any(k in i for i in sample for k in FIELD_MAP.get(c, [])):
            blank.append(c)
    if blank:
        print(f"WARNING: {len(blank)} column(s) have no source key on any of the "
              f"first {len(sample)} items:", file=sys.stderr)
        print(f"         {blank}", file=sys.stderr)
        print("         This is a FIELD_MAP gap, not empty data. "
              "Run --probe to see the real keys.", file=sys.stderr)

    if args.dry_run:
        print(f"[dry run] {len(items)} items -> {out}")
        return 0

    existed = os.path.exists(out)
    write_csv(out, items, meta)
    print(f"{'Overwrote' if existed else 'Wrote'} {out} ({len(items)} items)")

    if activity:
        side = os.path.join(out_dir, f"beevia-activity-{stamp:%Y-%m-%d}.json")
        write_activity(side, activity)
        print(f"Wrote {side} ({len(activity)} items with audit trails)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
