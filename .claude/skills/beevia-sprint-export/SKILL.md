---
name: beevia-sprint-export
description: Pull the Beevia sprint board from the Zoho Sprints API and write it to sprint-board-exports/ in the same CSV format as a manual Zoho export. Use when asked to fetch, refresh, download or update the sprint board, or before running a project status report that needs current data.
---

# Beevia sprint board export

Replaces the manual "export CSV from Zoho Sprints" step. Output is a drop-in
replacement for a UI export and is consumed unchanged by `beevia-audit`.

```bash
S=.claude/skills/beevia-sprint-export/scripts/zoho_export.py

python3 $S --probe                    # FIRST RUN: inspect the live API
python3 $S                            # write today's export
python3 $S --dry-run                  # fetch + report, write nothing
python3 $S --sprint 0703              # override the sprint filter
python3 $S --date 2026-08-05          # backdate the filename
python3 $S --raw 'team/910540998/projects/'   # dump one endpoint verbatim
```

Writes `sprint-board-exports/beevia-sprint-board-YYYY-MM-DD.csv`.
Exit `0` = written · `1` = config/API error · `2` = fetched but zero items matched.

## Status — end-to-end working

Verified against the live account on 2026-08-06 by writing a full export and
diffing it against a same-day manual one.

| Part | State |
|---|---|
| **Full export** | ✅ **Working.** 120 items (54 Stories + 66 Tasks), 21 of 31 columns populated, the rest genuinely empty on this board. |
| **CSV output format** | ✅ **Verified** byte-for-byte — UTF-8 BOM, CRLF, 5-row preamble padded to 31 fields, header on line 6. |
| **OAuth refresh + token cache** | ✅ **Verified.** |
| **`teams/` / `projects/`** | ✅ **Verified.** Team `910540998` (`blomgram`), project `187554000000089145` (Beevia). |
| **`sprints/` endpoint** | ✅ **Resolved** — needed `type=[1,2,3,4]`. |
| **`item/` endpoint** | ✅ **Resolved** — needed `subitem=true`. |
| **Columnar decoding** | ✅ **Verified** against real payloads, with a unit test. |
| **`FIELD_MAP`** | ✅ **Verified** against real items, including id→label resolution. |
| **`Last Modified`** | ✅ **Recovered** via `--modified` (day precision). |
| **`Epic`** | ⚠️ **Blocked on an OAuth scope** — see Known output gaps. |

Remaining diffs vs a manual export: `Epic` (scope), `Comments` (bodies not
exposed), and `Last Modified` time-of-day (day precision only).

## The two things that cost the most time

**1. `action=data` is mandatory.** Every Zoho Sprints collection endpoint needs
it. Without it you get `{"code":7404,"message":"Given URL is wrong"}` — which
reads as a wrong *path* and sends you rewriting URLs, when the path was fine.
`Zoho.get()` now adds it automatically.

**2. Records are columnar, not objects.** Zoho returns, for a resource `X`:

```jsonc
"XJObj":  { "<id>": ["Beevia", "7", "2026-06-16T23:00:00.000Z", ...] },  // positional
"X_prop": { "projName": 0, "projNo": 1, "startDate": 2, ... },           // schema
"XIds":   ["<id>", ...]                                                  // ordering
```

`decode_columnar()` handles this and folds `userDisplayName` in so owner ids
resolve to names. Any code assuming a list of JSON objects will silently see
zero rows.

## The two parameters that silently return partial data

**RESOLVED 2026-08. Both were 200-with-missing-rows, not errors** — the most
dangerous failure mode, because the export looks complete.

### 1. `sprints/` needs `type` — else upcoming sprints only

Without it Zoho returns `{"sprintIds": [], "status": "success"}`, which reads
like an empty project. The docs state it plainly: *"If you don't pass 'type'
param, only the upcoming sprints would be listed."*

```
type=[1,2,3,4]      # 1 upcoming · 2 active · 3 completed · 4 canceled
```

Sprint 0702 is active, so it was invisible until this was added.

### 2. `item/` needs `subitem=true` — else root items only

Without it the sprint returned **54 of 120 items**: the 54 Stories at `depth=0`,
and none of the 66 child Tasks. 55% of the board, missing silently.

Note it is `subitem`, not `isSubItem`/`viewType`/`depth` — the endpoint rejects
unknown params with `400 Extra parameter found in URL`, so a typo fails loudly
while an omission fails quietly.

## Verified endpoint map

Base is `https://sprintsapi.zoho.com/zsapi` (the OAuth API). `sprints.zoho.com/zsapi`
seen in browser DevTools is the **web UI's** internal host, session-authenticated —
useful for reading path shapes, not a substitute for the API host.

| Purpose | Path (under `team/{team}/projects/{project}/`) | Params |
|---|---|---|
| Sprints | `sprints/` | `action=data index range type=[1,2,3,4]` |
| Items | `sprints/{sprintId}/item/` | `action=data index range subitem=true` |
| Item detail | `sprints/{sprintId}/item/{itemId}/` | `action=details` |
| Statuses | `itemstatus/` | `action=data index range` |
| Item types | `itemtype/` | `action=data index range` |
| Priorities | `priority/` | `action=data index range` |
| Epics | `epic/` | `action=data index range` |

Items carry **ids, not labels** (`statusId`, `projItemTypeId`, `projPriorityId`,
`epicId`, and `ownerId` as an ARRAY). `Lookups` + `resolve_names()` fold the
label tables in. `userDisplayName` arrives on the item payload itself, not from
any users endpoint, so `Zoho.try_get` accumulates it from every response.

`--discover` tries a bounded candidate matrix and reports which shapes answer.

## Known output gaps

Verified by diffing a generated export against a manual one for the same day:
**28 of 31 columns match exactly.** The three that do not:

| Column | Why | Fix |
|---|---|---|
| **Epic** | `epic/` returns `401 Invalid oauthscope` | Re-authorise the refresh token with **`ZohoSprints.epic.READ`** added. The script warns once and leaves the column blank. |
| **Last Modified** | Not a *field* on any endpoint — searched all 43 list and 34 detail fields for `mod\|updat\|chang\|revis\|edit\|last`: zero matches. | **Recoverable** with `--modified`, to day precision. See below. |

### Recovering `Last Modified` — `--modified`

Although no endpoint *returns* it, `I-modifiedon` is a supported **filter**, so
the value can be recovered by asking "which items changed on day D?" once per
day and keeping the latest hit per item. One request per day in the window
(~28), not per item. Verified: 120/120 items resolved.

The filter shape is the whole trick, and a wrong guess returns a bare `400`:

```jsonc
filter={"queryType":1,
        "jsontmpl":"item_default",
        "I-modifiedon":[["2026-08-05T00:00:00+01:00",
                         "2026-08-05T23:59:59+01:00"]]}   // range is NESTED
```

The outer array is a list of **conditions**, each either a keyword (`"today"`,
`"lastweek"`) or a `[start, end]` pair. Passing the pair at the top level — the
obvious reading, and what the doc example looks like at a glance — is rejected.
`I-modifiedon` as a plain URL parameter is also rejected; it only works nested
inside `filter`.

**Day precision only.** Narrowing to a time would need a bisection per item, and
bulk edits carry no audit record to borrow an exact stamp from, so the column is
written as `06/Aug/2026` rather than `06/Aug/2026 05:23 PM`.

### Recovered ≠ meaningful: do not use `Last Modified` as an activity signal

`--activity` writes `beevia-activity-<date>.json`, a per-item audit trail from
`.../item/{id}/activity/` with exact timestamps for every audited action.

The newest audit entry **is not** the export's `Last Modified`, and the gap is
instructive. Comparing them across items:

| item | export `Last Modified` | newest audited action |
|---|---|---|
| BVA-I40 | 05/Aug 05:23 PM | 05/Aug 05:23 PM ✓ |
| BVA-I72 | 05/Aug 05:23 PM | **22/Jul** 02:08 PM |
| BVA-I47 | 03/Aug 05:11 PM | **21/Jul** 04:53 PM |

Dozens of items share the identical stamp `05/Aug 05:23 PM` with no audit entry
that day: a **bulk board operation updates the row's modified time without
producing a per-item audit record**.

That makes `Last Modified` actively misleading for "when did work move".
Bucketing by it suggested 97 items entered review in the final three days of the
sprint — a cliff. The audit trail shows last-status-change spread across the
whole sprint (5 on 10 Jul … 16 on 31 Jul, 29 on 04 Aug, 9 on 05 Aug): steady
flow with one real spike, not a pile-up.

**Any staleness or throughput analysis should read the activity sidecar, not the
`Last Modified` column.**

### Comments

The API returns `commentCount` only; the UI export writes comment *bodies* as
JSON. Left blank rather than emitting a number where a reader expects text.
Affected 3/120 items.

Two deliberate fidelity choices, both to keep future diffs clean:

- **Descriptions reproduce a Zoho bug.** Its exporter strips HTML tags and raw
  newlines without substituting a space, gluing words across the boundary
  (`an invite<br>link` → `an invitelink`). `strip_html()` matches this. Adding
  the missing space would be *better* text but would make all 120 descriptions
  differ on every future diff.
- **Three workhour columns are emitted from config** (`CONSTANT_COLUMNS`). They
  are project-level settings the UI repeats on every row and no endpoint returns.

`ZOHO_ITEM_PREFIX` is likewise not derivable — the API returns `itemNo` (72) and
the item type contributes `I`, but the `BVA` project code appears nowhere in any
payload. Set it from any item id on the board.

## Rate limits — important

**Zoho rate-limits the token-refresh endpoint hard**, and will lock you out for
tens of minutes with `"You have made too many requests continuously"`. Each
process invocation used to refresh, so a probing loop tripped it quickly.

Access tokens are now cached in `.zoho-token-cache.json` (gitignored, mode 600,
5-minute expiry margin) and reused for the ~1h lifetime. Normal use will not hit
the limit. If you do trip it, wait 10–30 minutes — retrying makes it worse.

### The *data* endpoints throttle too — and do it silently

Descriptions require one detail call per item (~120 per run). Zoho throttles
that burst, but **returns HTTP 200 with an empty body rather than 429**, so a
naive loop produced 62/120 blank descriptions that looked like items genuinely
having none.

`fetch_detail()` retries 4× with exponential backoff (0.6s → 2.4s) and detects
failure by an empty result, not a status code. Any item that still fails is
listed by name in a warning — never silently blank. A full run takes ~2 minutes;
`--no-descriptions` skips the whole pass when only board state is needed.

## Other API facts

- **`ZOHO_TEAM_ID` is the workspace id.** UI says "workspace", the API path says
  `team/{id}/`. Verified: `910540998`.
- Auth header is `Zoho-oauthtoken {token}`, not `Bearer`.
- Refresh tokens are per data centre; a `.com` token fails against `.eu`. Wrong
  `ZOHO_DC` is the usual cause of "invalid refresh token".
- The `teams/` envelope carries `baseURL` (`https://sprints.zoho.com`) — useful
  if the API host ever moves.
- Timestamps: the writer renders epoch ms as `05/Aug/2026 06:59 PM` for datetime
  columns, `05/Aug/2026` for date-only, matching the UI export.

## First-run workflow

1. `cp .env.example .env` and fill in the OAuth values. `.env` is gitignored.
   Team and project ids are already filled in and verified.
2. `python3 $S --probe` — prints real envelope keys, row keys and ids at each
   level, then one item's full key/value list, then a **FIELD_MAP coverage** line.
3. If coverage is not 31/31, add each real key to the **front** of that column's
   list in `FIELD_MAP`. Re-probe.
4. `python3 $S --dry-run`, then `python3 $S`.
5. Confirm the shape against the last manual export — only `Date` should differ:

   ```bash
   diff <(head -6 sprint-board-exports/beevia-sprint-board-2026-08-05.csv) \
        <(head -6 sprint-board-exports/beevia-sprint-board-$(date +%F).csv)
   ```

## Troubleshooting

**`id=None name=None` in probe output** — the row keys differ from what
`id_of()`/`name_of()` look for. Use `--raw 'team/'` to see the verbatim JSON and
add the real key to those helpers.

**Endpoint 404s** — the path shape is wrong for this plan. Explore with `--raw`,
starting from `team/{workspace}/projects/`, and correct the paths in `probe()`
and `main()`.

**A column is silently empty** — the script warns when a column is blank across
the first 50 items, because a blank column reads as real data ("no estimates
set") rather than a mapping gap. Take that warning seriously; check the probe
dump before accepting it.

**Zero items (exit 2)** — usually `ZOHO_SPRINT_FILTER` not matching. The error
lists the sprint names actually available.

## Guardrails

- Read-only against Zoho. Never call a mutating endpoint from this skill.
- Writes only to `sprint-board-exports/`. `.claude/rules.md` makes the service
  sub-repos off-limits.
- Never print or commit `.env` contents; the refresh token is a long-lived
  credential equivalent to a password.
- Same-day re-runs overwrite that day's file, via a temp file and atomic
  rename, so an API failure part-way through cannot truncate a good export.

## Chaining

The natural daily sequence is export then audit:

```bash
python3 .claude/skills/beevia-sprint-export/scripts/zoho_export.py \
  && python3 .claude/skills/beevia-audit/scripts/audit.py
```

`beevia-audit` picks up the newest CSV in the folder automatically, so a fresh
export feeds straight into the status report.
