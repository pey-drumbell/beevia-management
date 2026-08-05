#!/usr/bin/env python3
"""Beevia daily audit — deterministic checks across code, specs, docs and board.

Read-only. Never writes to the workspace or the service repos.

Usage:
    python3 .claude/skills/beevia-audit/scripts/audit.py            # full report
    python3 .claude/skills/beevia-audit/scripts/audit.py --json     # machine-readable
    python3 .claude/skills/beevia-audit/scripts/audit.py --quiet    # only problems

Exit codes:
    0  no drift, no errors
    1  drift or inconsistency found (detail in the report)
    2  the audit itself could not run (missing file, unparseable spec)
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.parse

try:
    import yaml
except ImportError:
    print("FATAL: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(2)

def _find_root() -> str:
    """Walk up from this script to the workspace root.

    Identified by containing `.claude/` — more robust than counting parent
    directories, which breaks if the skill is nested differently or invoked
    through a symlink. Falls back to $PWD.
    """
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, ".claude")) and \
           os.path.basename(d) != ".claude":
            return d
        d = os.path.dirname(d)
    return os.getcwd()


ROOT = os.environ.get("BEEVIA_ROOT") or _find_root()

METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}

# service dir -> (implemented spec, proposed spec)
SERVICES = {
    "beevia-api": ("openapi.yaml", "openapi.proposed.yaml"),
    "beevia-admin-api": ("openapi.admin.yaml", "openapi.admin.proposed.yaml"),
}

# (path, method) pairs allowed to appear in BOTH a spec and its proposed file.
# These are live endpoints whose request contract is designed to widen; the
# proposed file restates them in target state. Shrink this as they ship.
ALLOWED_OVERLAP = {
    "openapi.yaml": {
        ("/payments/send", "post"),
        ("/payments/request", "post"),
        ("/payments/{id}/pay", "post"),
    },
    "openapi.admin.yaml": set(),
}

# Schemas deliberately different between a spec and its proposed file
# (current form vs widened target form). Everything else must match.
ALLOWED_SCHEMA_DRIFT = {"SendMoneyRequest", "RequestMoneyRequest"}

problems: list[str] = []
notes: list[str] = []


def problem(msg: str) -> None:
    problems.append(msg)


# --------------------------------------------------------------------------- #
# 1. Route extraction from NestJS controllers
# --------------------------------------------------------------------------- #

CTRL_RE = re.compile(r"@Controller\(\s*'([^']*)'\s*\)|@Controller\(\s*\)")
ROUTE_RE = re.compile(
    r"@(Get|Post|Put|Patch|Delete|Head|Options)\(\s*'([^']*)'\s*\)"
    r"|@(Get|Post|Put|Patch|Delete|Head|Options)\(\s*\)"
)


def normalise(path: str) -> str:
    """`:id` -> `{id}`; collapse duplicate slashes; keep a leading slash."""
    path = re.sub(r":(\w+)", r"{\1}", path)
    path = re.sub(r"/+", "/", path)
    return path if path.startswith("/") else "/" + path


def extract_routes(service_dir: str) -> set[tuple[str, str]]:
    """Every (path, method) declared by controller decorators in a service."""
    src = os.path.join(ROOT, service_dir, "src")
    if not os.path.isdir(src):
        problem(f"service source not found: {src}")
        return set()

    found: set[tuple[str, str]] = set()
    for f in glob.glob(os.path.join(src, "**", "*.controller.ts"), recursive=True):
        prefix = None
        for line in open(f, encoding="utf-8", errors="replace"):
            m = CTRL_RE.search(line)
            if m:
                prefix = m.group(1) or ""
                continue
            m = ROUTE_RE.search(line)
            if m and prefix is not None:
                method = (m.group(1) or m.group(3)).lower()
                sub = m.group(2) or ""
                parts = [p for p in (prefix, sub) if p]
                found.add((normalise("/" + "/".join(parts)), method))
    return found


def spec_ops(path: str) -> set[tuple[str, str]]:
    doc = load_spec(path)
    return {(p, m) for p, item in (doc.get("paths") or {}).items()
            for m in item if m in METHODS}


_spec_cache: dict[str, dict] = {}


def load_spec(name: str) -> dict:
    if name in _spec_cache:
        return _spec_cache[name]
    p = os.path.join(ROOT, name)
    if not os.path.exists(p):
        problem(f"spec missing: {name}")
        _spec_cache[name] = {"paths": {}}
        return _spec_cache[name]
    try:
        _spec_cache[name] = yaml.safe_load(open(p, encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"FATAL: {name} does not parse: {e}", file=sys.stderr)
        sys.exit(2)
    return _spec_cache[name]


def param_agnostic(pairs: set[tuple[str, str]]) -> set[tuple[str, str]]:
    """Compare paths ignoring parameter NAMES (`{id}` vs `{walletId}`)."""
    return {(re.sub(r"\{\w+\}", "{}", p), m) for p, m in pairs}


# --------------------------------------------------------------------------- #
# 2. Drift: code vs implemented spec, and shipped proposals
# --------------------------------------------------------------------------- #

def check_drift() -> dict:
    out = {}
    for service, (impl, proposed) in SERVICES.items():
        code = extract_routes(service)
        spec = spec_ops(impl)
        prop = spec_ops(proposed)

        code_n, spec_n = param_agnostic(code), param_agnostic(spec)
        missing = sorted(code_n - spec_n)        # in code, not documented
        extra = sorted(spec_n - code_n)          # documented, not in code
        shipped = sorted(param_agnostic(prop) & code_n)  # proposal now live

        allowed = param_agnostic(ALLOWED_OVERLAP.get(impl, set()))
        shipped = [s for s in shipped if s not in allowed]

        if missing:
            problem(f"{service}: {len(missing)} route(s) in code but NOT in {impl}")
        if extra:
            problem(f"{service}: {len(extra)} route(s) in {impl} but NOT in code")
        if shipped:
            problem(f"{service}: {len(shipped)} PROPOSED route(s) now implemented "
                    f"— move them from {proposed} to {impl}")

        out[service] = {
            "code_routes": len(code), "spec_routes": len(spec),
            "proposed_routes": len(prop),
            "missing_from_spec": missing, "extra_in_spec": extra,
            "shipped_proposals": shipped,
        }
    return out


# --------------------------------------------------------------------------- #
# 3. Spec health
# --------------------------------------------------------------------------- #

def check_specs() -> dict:
    out = {}
    for impl, proposed in SERVICES.values():
        for name in (impl, proposed):
            p = os.path.join(ROOT, name)
            if not os.path.exists(p):
                continue
            txt = open(p, encoding="utf-8").read()
            doc = load_spec(name)

            have = {(s, n) for s, items in (doc.get("components") or {}).items()
                    for n in items}
            need = set(re.findall(r"#/components/(\w+)/([A-Za-z0-9_]+)", txt))
            broken = sorted(need - have)
            # securitySchemes are referenced from `security:`, not via $ref
            unused = sorted(n for n in have - need if n[0] != "securitySchemes")

            ids = [doc["paths"][p_][m].get("operationId")
                   for p_ in doc.get("paths", {}) for m in doc["paths"][p_]
                   if m in METHODS]
            dupes = sorted({i for i in ids if i and ids.count(i) > 1})
            missing_ids = ids.count(None)
            markers = txt.count("x-beevia-")

            if broken:
                problem(f"{name}: {len(broken)} broken $ref(s): {broken[:3]}")
            if unused:
                problem(f"{name}: {len(unused)} unused component(s): {unused[:3]}")
            if dupes:
                problem(f"{name}: duplicate operationId(s): {dupes[:3]}")
            if missing_ids:
                problem(f"{name}: {missing_ids} operation(s) without an operationId")
            if markers:
                problem(f"{name}: {markers} legacy `x-beevia-*` marker(s) — "
                        f"status is expressed by FILE, not by marker")

            out[name] = {"ops": len(spec_ops(name)), "broken_refs": broken,
                         "unused": unused, "dupe_ids": dupes,
                         "missing_ids": missing_ids, "markers": markers}

        # overlap + shared-schema drift between the pair
        a, b = spec_ops(impl), spec_ops(proposed)
        overlap = sorted((a & b) - ALLOWED_OVERLAP.get(impl, set()))
        if overlap:
            problem(f"{impl} / {proposed}: unexpected overlap {overlap}")

        sa = (load_spec(impl).get("components") or {}).get("schemas") or {}
        sb = (load_spec(proposed).get("components") or {}).get("schemas") or {}
        drift = sorted(n for n in set(sa) & set(sb)
                       if sa[n] != sb[n] and n not in ALLOWED_SCHEMA_DRIFT)
        if drift:
            problem(f"{impl} / {proposed}: shared schema(s) diverged: {drift}")
        out.setdefault("_pairs", {})[impl] = {
            "overlap": overlap, "schema_drift": drift}
    return out


# --------------------------------------------------------------------------- #
# 4. Document consistency
# --------------------------------------------------------------------------- #

def check_docs() -> dict:
    out: dict = {"broken_links": [], "inventory": None}

    for f in glob.glob(os.path.join(ROOT, "*.md")):
        for m in re.findall(r"\]\((\./[^)]+)\)", open(f, encoding="utf-8").read()):
            target = urllib.parse.unquote(m[2:])
            if not os.path.exists(os.path.join(ROOT, target)):
                rel = os.path.basename(f)
                out["broken_links"].append(f"{rel} -> {target}")
                problem(f"broken link in {rel}: {target}")

    # api-rfc.md §3 domain inventory must sum to the real spec totals
    rfc = os.path.join(ROOT, "api-rfc.md")
    if os.path.exists(rfc):
        t = open(rfc, encoding="utf-8").read()
        m = re.search(r"## 3\. Domain inventory.*?\n\n(\|.*?)\n\n---", t, re.S)
        if m:
            ti = tp = 0
            for row in m.group(1).split("\n"):
                if not row.startswith("|") or "---" in row:
                    continue
                cells = [c.strip() for c in row.strip("|").split("|")]
                if len(cells) < 3 or cells[0].lower().startswith(("domain", "**total")):
                    continue
                ti += int(re.sub(r"\D", "", cells[1]) or 0)
                tp += int(re.sub(r"\D", "", cells[2]) or 0)
            impl_n = len(spec_ops("openapi.yaml"))
            prop_n = len(spec_ops("openapi.proposed.yaml")) - len(
                ALLOWED_OVERLAP["openapi.yaml"])
            out["inventory"] = {"rows_implemented": ti, "rows_proposed": tp,
                                "spec_implemented": impl_n, "spec_proposed": prop_n}
            if ti != impl_n:
                problem(f"api-rfc.md §3 implemented column sums to {ti}, "
                        f"openapi.yaml has {impl_n}")
            if tp != prop_n:
                problem(f"api-rfc.md §3 proposed column sums to {tp}, "
                        f"expected {prop_n} net-new")
        else:
            notes.append("api-rfc.md §3 domain inventory table not found — skipped")
    return out


# --------------------------------------------------------------------------- #
# 5. Sprint board
# --------------------------------------------------------------------------- #

def latest_board() -> str | None:
    files = sorted(glob.glob(os.path.join(ROOT, "sprint-board-exports", "*.csv")))
    return files[-1] if files else None


def check_board() -> dict | None:
    path = latest_board()
    if not path:
        notes.append("no sprint board export found — board section skipped")
        return None

    lines = open(path, encoding="utf-8-sig").readlines()
    # Preamble: Team/Project/Exported By/Date/Filter, then the header row.
    hdr = next((i for i, l in enumerate(lines)
                if l.split(",")[0].strip() == "Item Id"), 5)
    rows = list(csv.DictReader(lines[hdr:]))
    if not rows:
        problem(f"{os.path.basename(path)}: no rows parsed — check the preamble offset")
        return None

    g = lambda r, k: (r.get(k) or "").strip()

    # A parent is any item referenced as someone's Parent Id. Parents are
    # umbrella rows whose status rolls up — counting them double-counts work.
    parents = {g(r, "Parent Id") for r in rows if g(r, "Parent Id")}
    leaves = [r for r in rows if g(r, "Item Id") not in parents]

    status = collections.Counter(g(r, "Status") for r in leaves)
    by_assignee = collections.defaultdict(collections.Counter)
    for r in leaves:
        by_assignee[g(r, "Assignee") or "(blank)"][g(r, "Status")] += 1

    # NOTE: 'Unassigned' is a LITERAL value in this export, not an empty cell.
    unassigned = {g(r, "Item Id") for r in rows if g(r, "Assignee") == "Unassigned"}
    unassigned_leaves = sorted(unassigned - parents)

    def parse(d: str):
        try:
            return dt.datetime.strptime(d.split(" ")[0], "%d/%b/%Y").date()
        except (ValueError, IndexError):
            return None

    export_date = None
    for l in lines[:hdr]:
        if l.startswith("Date,"):
            export_date = parse(l.split(",")[1])
    today = export_date or dt.date.today()

    review = [r for r in leaves if g(r, "Status") == "REVIEW/QA"]
    inflow = collections.Counter(
        g(r, "Last Modified").split(" ")[0] for r in review)
    ages = [(today - d).days for d in
            (parse(g(r, "Last Modified")) for r in review) if d]
    recent = sum(1 for a in ages if a <= 2)

    sprint_end = parse(g(rows[0], "Sprint End Date"))
    days_left = (sprint_end - today).days if sprint_end else None

    unestimated = sum(1 for r in rows if g(r, "Estimation Points") in ("", "0"))
    no_epic = sum(1 for r in leaves if not g(r, "Epic"))

    if days_left is not None and days_left <= 3 and len(review) > len(leaves) * 0.5:
        problem(f"sprint ends in {days_left}d with {len(review)}/{len(leaves)} "
                f"leaf items still in REVIEW/QA")
    if unestimated == len(rows):
        notes.append("no estimation points on any item — velocity is not derivable")
    if unassigned_leaves:
        problem(f"{len(unassigned_leaves)} LEAF item(s) unassigned "
                f"(parents excluded): {unassigned_leaves[:5]}")

    return {
        "file": os.path.basename(path),
        "export_date": str(today),
        "sprint_end": str(sprint_end) if sprint_end else None,
        "days_left": days_left,
        "rows": len(rows), "parents": len(parents), "leaves": len(leaves),
        "status": dict(status),
        "by_assignee": {k: dict(v) for k, v in by_assignee.items()},
        "review_queue": len(review),
        "review_arrived_last_2d": recent,
        "review_inflow_by_date": dict(sorted(inflow.items())),
        "unestimated": unestimated, "leaves_without_epic": no_epic,
        "unassigned_leaves": unassigned_leaves,
    }


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="only print problems")
    args = ap.parse_args()

    result = {
        "root": ROOT,
        "drift": check_drift(),
        "specs": check_specs(),
        "docs": check_docs(),
        "board": check_board(),
    }
    result["problems"] = problems
    result["notes"] = notes

    if args.json:
        print(json.dumps(result, indent=2, default=str))
        return 1 if problems else 0

    if not args.quiet:
        print("=" * 68)
        print("BEEVIA DAILY AUDIT")
        print("=" * 68)

        print("\n-- CODE vs SPEC --")
        for svc, d in result["drift"].items():
            flag = "OK" if not (d["missing_from_spec"] or d["extra_in_spec"]) else "DRIFT"
            print(f"  {svc:18} code={d['code_routes']:3}  "
                  f"spec={d['spec_routes']:3}  proposed={d['proposed_routes']:3}  [{flag}]")
            for p, m in d["missing_from_spec"]:
                print(f"      + in code, undocumented : {m.upper():6} {p}")
            for p, m in d["extra_in_spec"]:
                print(f"      - documented, not in code: {m.upper():6} {p}")
            for p, m in d["shipped_proposals"]:
                print(f"      * PROPOSAL SHIPPED       : {m.upper():6} {p}")

        print("\n-- SPEC HEALTH --")
        for name, s in result["specs"].items():
            if name == "_pairs":
                continue
            ok = not (s["broken_refs"] or s["unused"] or s["dupe_ids"]
                      or s["missing_ids"] or s["markers"])
            print(f"  {name:30} ops={s['ops']:3}  [{'OK' if ok else 'ISSUES'}]")

        if result["board"]:
            b = result["board"]
            print(f"\n-- SPRINT BOARD ({b['file']}) --")
            print(f"  export {b['export_date']}  sprint ends {b['sprint_end']}"
                  f"  ({b['days_left']}d left)")
            print(f"  {b['leaves']} leaf items (+{b['parents']} parent stories)")
            print(f"  status: {b['status']}")
            print(f"  review queue: {b['review_queue']} "
                  f"({b['review_arrived_last_2d']} arrived in last 2d)")

        print("\n" + "=" * 68)

    if problems:
        print(f"PROBLEMS ({len(problems)}):")
        for p in problems:
            print(f"  ! {p}")
    else:
        print("No drift or inconsistency found.")
    for n in notes:
        print(f"  . {n}")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
