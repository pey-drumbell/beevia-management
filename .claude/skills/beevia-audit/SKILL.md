---
name: beevia-audit
description: Daily audit of the Beevia project — detect drift between the API code and the OpenAPI specs, catch proposed endpoints that have shipped, validate spec health, and refresh the sprint status report. Use when asked for a daily/periodic Beevia review, an API drift check, a spec update, or a project status refresh.
---

# Beevia daily audit

Keeps four spec files, three RFC/analysis documents and one status report in sync with two evolving codebases and a sprint board.

**Run the script first. Do not re-derive by hand.** The mechanical parts — route extraction, drift diffing, spec validation, board statistics — are deterministic and already encoded. Hand-derivation is slower, burns context, and gets different answers on different days.

```bash
python3 .claude/skills/beevia-audit/scripts/audit.py          # human-readable
python3 .claude/skills/beevia-audit/scripts/audit.py --json   # for programmatic follow-up
python3 .claude/skills/beevia-audit/scripts/audit.py --quiet  # problems only
```

Exit `0` = clean, `1` = drift or inconsistency found, `2` = the audit could not run.

## Period-over-period

The script compares the two most recent board exports and prints a
`SINCE <previous export>` section (`delta` in `--json`): status movement, items
that **left** review, items newly Done, items that entered, and scope changes.

This exists because **throughput cannot be derived from one export.** A review
queue of 74 looks the same whether it is frozen or turning over completely, and
only the delta distinguishes them. "Nothing left REVIEW/QA since the last
export" is raised as a problem, not a note — it is the difference between a
busy team and a blocked one.

Two exports are required. With only one, the section is skipped and a note says
so; never present a first snapshot as though it showed a trend.

Queue **age** comes from the activity sidecar
(`beevia-activity-<date>.json`), never from the `Last Modified` column — bulk
board operations rewrite that column on dozens of items at once with no
per-item audit entry, and using it once overstated recent inflow ~5×. If the
sidecar is missing, age is reported as unknown rather than falling back.

## Hard constraint

`.claude/rules.md` forbids modifying the sub-repositories. **`beevia-api/`, `beevia-admin-api/`, `beevia-db-schema/`, `beevia-admin/` and `beevia-mobile/` are read-only.** Every deliverable is written at the workspace root. Never edit a service repo, even to fix something the audit finds — report it instead.

## The artifacts

| File | Contents |
|---|---|
| `openapi.yaml` | `beevia-api` — **implemented only**, no status markers |
| `openapi.proposed.yaml` | `beevia-api` — designed, not built |
| `openapi.admin.yaml` | `beevia-admin-api` — implemented only |
| `openapi.admin.proposed.yaml` | `beevia-admin-api` — designed, not built |
| `api-rfc.md` | Consumer API: conventions, gaps vs PRD, sequencing |
| `admin-api-rfc.md` | Admin API: RBAC model, module coverage vs dashboard spec |
| `suggestions.md` | Code/process observations |
| `project-status.md` | Sprint status, glanceable overview on top |

**Implemented vs proposed is expressed by FILE, never by a marker.** An earlier design used `x-beevia-status` extensions; that was dropped because `x-` is indistinguishable from an HTTP header and a merged file produced SDKs full of dead methods. The script fails if any `x-beevia-*` reappears. Proposed operations cite their source via `externalDocs`.

## What to do with the output

### Clean run (exit 0)
Say so and stop. Do not rewrite documents that are already correct.

### Route in code, undocumented
Add it to the implemented spec. Read the controller and its DTO for the real contract — summary, description, request schema, status codes, auth. Match the existing house style: `$ref` shared components, snake_case response fields, camelCase request bodies. Then update the `api-rfc.md` §3 inventory and the relevant §6 table.

### Proposal shipped
1. Delete the operation from the proposed file.
2. Add it to the implemented file **as actually built** — not as it was proposed. These usually differ; last time the shipped `DELETE /messages/{id}` used `?forEveryone=true` where the proposal had `?scope=`.
3. Remove any component that is now orphaned (the script will flag it next run).
4. Note it in the RFC's "what changed" section and strike it from the proposed inventory.

### Documented, not in code
A route was removed or renamed. Confirm which before editing — a rename shows up as one removal plus one addition.

### Spec health issues
Broken `$ref`s, unused components, duplicate `operationId`s, missing `operationId`s. All mechanical; fix directly.

### Shared schema diverged
The proposed files duplicate components rather than `$ref`ing across files, so both open in Swagger UI without bundling. The cost is drift. Realign, unless the divergence is intentional — `SendMoneyRequest` and `RequestMoneyRequest` are deliberately different (current vs widened target form) and are whitelisted in the script.

### Board findings
Refresh `project-status.md`. Keep the **quick overview at the top** — it is the part that gets read. Detail below.

## Traps that have already cost time

These are the specific things that produced wrong answers on the first pass. The script handles all of them; read this section before overriding it or analysing the board by hand.

**Parent stories inflate every board count.** The export mixes umbrella stories with real work items. A parent is any item referenced as another item's `Parent Id`. Report **leaf** items; state both numbers so the reader can reconstruct.

**`Unassigned` is a literal value, not an empty cell.** Filtering on empty strings returns zero and looks like "everything is staffed". All such items have historically been parent stories, i.e. a hierarchy artifact rather than a resourcing gap — check before reporting it as a problem.

**A large REVIEW/QA queue is not necessarily stale.** Check `Last Modified` distribution. Items arriving in the last 2–3 days are an end-of-sprint pile-up; items untouched for weeks are a rotting queue. Different diagnoses, different recommendations.

**Webhook routes are tagged `Webhooks`, not by domain.** `POST /kyc/entrust/webhook` sits under `/kyc` but is tagged `Webhooks`. Counting it in both places breaks the inventory total by one.

**Section headings in `api-rfc.md` §7 carry counts** that must sum to net-new proposed operations (total minus the whitelisted live-endpoint modifications). Update the heading when adding or removing a row.

**The CSV has a five-line preamble** before the header row. The script locates the header by finding `Item Id` rather than assuming an offset.

## Judgment, not mechanics

The script cannot decide these. Re-examine when the relevant code changes:

- **Does new work close a PRD gap or move sideways?** The four MVP gaps — multi-currency/FX, virtual cards, international KYC tier, consent management — are the spine of `api-rfc.md`. Check `PaymentService.activeNgn()`: while it exists, FX is not started regardless of what shipped.
- **Does a new admin capability conflict with E2EE?** The server cannot read message content. Any spec asking for "reported messages" or content moderation is unbuildable as written — see `admin-api-rfc.md` §5.1 for the three options.
- **Did a new endpoint introduce a security default worth flagging?** Particularly: is a new admin controller missing `@UseGuards`, which leaves it fully unauthenticated.

## Cadence

Daily works for drift detection — it is cheap and catches problems while the change is fresh. The narrative documents need editing only when the audit finds something; on a clean day the run is a few seconds and produces no diff.

The sprint board export is produced manually, so it will often be unchanged between runs. The script skips that section rather than failing when no export is present.
