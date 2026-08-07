---
name: beevia-refresh
description: Full Beevia refresh — pull the latest sprint board from Zoho, fast-forward every sub-repo to origin/main, re-audit the API surface, update the four OpenAPI specs, and write a dated project status report. Use when asked to refresh/update the project, do a full review, sync the repos and regenerate the status report, or produce this week's status.
---

# Beevia full refresh

One command chain that takes the workspace from "stale" to "current": fresh
board, fresh code, specs reconciled, status report written.

```bash
E=.claude/skills/beevia-sprint-export/scripts/zoho_export.py
S=.claude/skills/beevia-refresh/scripts/sync_repos.py
A=.claude/skills/beevia-audit/scripts/audit.py

python3 $E --modified --activity   # 1. board  (~4 min)
python3 $S                         # 2. code
python3 $A                         # 3. drift
                                   # 4. update specs   (judgement — see below)
                                   # 5. write report    (judgement — see below)
```

Steps 1–3 are mechanical and already encoded. **Run them; do not re-derive
their output by hand** — it is slower, burns context, and gives different
answers on different days. Steps 4–5 are the parts that need reading and
judgement, and they are where the time should go.

## MVP progress estimate

Every report carries an MVP-readiness estimate: one number at the top of the
web report (rendered as the segmented strip — see below) and a capability
table in the Markdown. It answers the question the board cannot: *how far is
the product from the PRD's MVP*, independent of sprint mechanics.

**Target date: 2026-09-01.** Provisional — set by the project owner on
2026-08-07 as a working anchor, not a commitment. Replace it here when a real
date is decided, and always print it with the word "provisional" until then.

### The rubric

Fixed capability list derived from PRD §1.2 and §11 (Phases 1–4). **Weights are
frozen** so the number is comparable across reports; changing a weight is a
methodology change and must be called out in the report that does it.

| # | Capability | Weight | Score from |
|---|---|---:|---|
| 1 | E2EE messaging | 15 | `/conversations` `/messages` `/keys` `/attachments` surface; chat screen inventory + crypto/socket layers in `beevia-mobile/lib` |
| 2 | Voice & video calling | 8 | `/calls` surface; `audio_call_screen` / `video_call_screen` present and wired |
| 3 | Message translation | 7 | `/translate` implemented vs proposed (`batch`, `languages`); `translate_chat_screen` in the client |
| 4 | Local KYC tier (BVN) | 8 | `/kyc/*` + `/upgrade/*` implemented; provider webhook; the client's full onboarding/wallet flow (BVN, facial verification) |
| 5 | International KYC tier | 6 | `/kyc/international/*` — proposed-only until it ships |
| 6 | Multi-currency wallets | 12 | `/wallets` surface; whether non-NGN wallets exist (`activeNgn()` is the tell); whether the client has a wallet home/balance/transactions screen beyond onboarding setup |
| 7 | Send / request / receive in chat | 12 | `/payments/*` implemented (send, request, accept, decline, pay, cancel) vs the missing read path; whether the client's money UI actually calls the payments API (see wired-vs-stub below) |
| 8 | Cross-currency FX settlement | 12 | `/fx/*` — proposed-only until it ships; `PaymentService` hard-coding |
| 9 | Virtual cards | 10 | `/cards/*` — proposed-only until it ships |
| 10 | Consent management | 4 | any consent endpoint or record; none exists yet |
| 11 | Admin oversight | 6 | admin endpoints implemented vs proposed; dashboard modules landed in `beevia-admin/src` (screens and features, not commits) |

### Client evidence: read the screens, never the commit log

Standing instruction from the project owner (2026-08-07): **commit messages are not
evidence of client progress.** Score the mobile and admin front ends from the
code itself:

- `beevia-mobile` is **Flutter**. The screen inventory is
  `lib/features/*/screens/` (plus `chat/call/`); enumerate it and map screens to
  capabilities. ~39 screen files across chat, onboarding, settings, home as of
  2026-08-07.
- **Wired vs stub, one grep apart.** A screen with buttons is not a capability.
  Check that the flow reaches the API: grep `lib` for the endpoint path
  (`/payments`, `/wallets`, `/translate`). Found on 2026-08-07: "Send money" /
  "Request money" buttons exist in chat with a local placeholder handler and
  **zero calls to the payments API** — screens present, capability absent.
  A wired flow scores; a stub adds at most ~0.1 over nothing.
- `beevia-admin` is Next.js; the equivalent inventory is `src/app` routes and
  `src/features/*` against the dashboard spec's eight modules.
- **Correctness and testing are explicitly out of scope for now** (owner,
  2026-08-07): tests will be added to the repos separately. The bar is
  *implementation of the design* — the screen exists, matches the designed
  flow, and is wired to the real API. Do not discount a score for missing
  tests, and do not claim functional correctness either; the report's
  "cannot tell you" list carries that caveat.

Score each 0.0–1.0 **from evidence, per line, at report time**: the spec split
(implemented vs proposed operations in that area), the audit's drift check,
the sync report's changed files, and the code facts already verified in past
reports. The board contributes context (epic states, what is in review) but
never the score — the board has never accepted an item, so board status is not
evidence of build state. Weighted sum → the headline percentage, always
written with `≈` and the word "estimate".

Rules:

- **A proposed-only area scores 0.** A spec is a plan, not progress.
- **Score build, not acceptance**, and say so next to the number — the strip
  measures what exists in code, while the review queue measures what has been
  verified, and conflating them flatters the project.
- **Show the table.** The percentage alone is not publishable; the Markdown
  report carries the full capability table with each line's evidence, and the
  web report carries it in the appendix.
- **Never move a score up without naming the evidence** (endpoint shipped,
  module landed, migration merged). "Probably done, sitting in review" keeps
  its old score.

### Rendering

Web report: the `.mvp` strip sits directly under the masthead — one segment
per capability, segment width = weight, solid fill fraction = score, target
date and days remaining beside the percentage. It is the one page-top graphic
the owner has asked for (2026-08-07); keep it data-only and keep the
capability names in the appendix table, not crammed into the strip.

## The team

Confirmed by the project owner. **Use this; do not infer roles from the board** —
an earlier report inferred them from activity counts and got a non-contributor
badly wrong, reading a high action count as evidence of building the admin
dashboard. Board administration produces the highest action counts on the
board, and it is not delivery.

**Only people whose work is tracked appear in the report.** Supervisors and
other non-contributors are readers of it, not rows in it: do not give them a
team-table row, a per-person section, or an attribution in a finding. Where an
audit trail names one as the actor, state the transition without the name
("3 items left review, all sent back for rework"). This is a standing
instruction from the project owner, not a per-report judgement call.

| Person | Role | Owns | On the board? |
|---|---|---|---|
| **Promise Udo** | Admin dashboard | `beevia-admin`, `beevia-admin-api` | **Absent entirely** |
| **Ayomikun Araoye** | App backend lead; also contributes to the admin API | `beevia-api`, `beevia-db-schema` | 28 items |
| **David Samuel** | Mobile front end | `beevia-mobile` | 47 items |
| **Philip Chidera** | UI/UX design | — | 14 items |

### One workstream is invisible to the board

- **Promise has no board presence at all** — zero assigned items, zero audit
  actions, name absent from both the CSV and the activity sidecar. The admin
  dashboard is nevertheless being built. Until tasks are assigned to Promise,
  report the responsibility and judge the work from commits in `beevia-admin` /
  `beevia-admin-api`, which step 2's sync report lists.

Consequences for the report:

- **Board totals understate delivery**, because a whole workstream (the admin
  dashboard, 29 endpoints) happens outside them. Say so when quoting completion
  percentages, rather than reporting "12% done" as if it covered the project.
- **Never infer a role from activity counts.** Cross-check against this table;
  if someone appears who is not listed, say so and ask rather than guessing —
  a name that is absent may be a non-contributor who is deliberately not
  reported, and adding them back is a regression, not a fix.

Roles also tell you which repo a person's board items belong to: David's are
mobile, Ayomikun's are backend, Philip's are design. A backend item in review
waits on a different reviewer than a mobile one.

### Git identities do not match board names

Commit authorship uses different handles from the Zoho display names, so
attributing commits needs care. Observed over 90 days:

| Git author | Repos | Almost certainly |
|---|---|---|
| `Phoenixdadhev` | `beevia-api` (98), `beevia-db-schema` (18), `beevia-admin-api` (7) | Ayomikun — same repos as his stated ownership, and he also commits under `Ayomikun Araoye` |
| `Davidtariq96` | `beevia-mobile` (48) | David — also commits there under `David Samuel` |
| `Promise Udo` | `beevia-admin` (2) | Promise |
| `Victor Peynado` | `beevia-mobile` (4) | The project owner |

**The first two mappings are inference, not confirmation.** They are consistent
and unlikely to be wrong, but treat them as provisional: if a report attributes
commits by person, say which identity it counted.

## Step 1 — board

Delegates to the **`beevia-sprint-export`** skill. Read that skill's SKILL.md
before touching its script or interpreting its output; it documents several
non-obvious API traps.

Always pass `--modified --activity`:

| Flag | Why |
|---|---|
| `--modified` | Fills `Last Modified`, which no endpoint returns — recovered by date-sweeping the `I-modifiedon` filter. |
| `--activity` | Writes `sprint-board-exports/beevia-activity-<date>.json`, per-item audit trails. **The status report's flow analysis must use this, not `Last Modified`** — see the trap below. |

Takes ~4 minutes, most of it the per-item description fetch. Exit `2` means
zero items matched, usually a stale `ZOHO_SPRINT_FILTER` in `.env` after a
sprint rolls over — the error lists the sprint names that do exist.

## Step 2 — code

```bash
python3 .claude/skills/beevia-refresh/scripts/sync_repos.py
python3 .claude/skills/beevia-refresh/scripts/sync_repos.py --dry-run   # preview
python3 .claude/skills/beevia-refresh/scripts/sync_repos.py --json      # for follow-up
```

Checks out `main` and fast-forwards each sub-repo, then reports the commits and
changed files — highlighting controller/DTO/schema paths, so step 4 knows where
to look instead of re-scanning both codebases.

Exit `0` = all synced · `1` = something was skipped or diverged · `2` = not a workspace.

**This is the only sanctioned write to the service repos.** `.claude/rules.md`
forbids modifying them; this skill is the "unless specifically asked to"
exception, and it is limited to git synchronisation. It never edits a file,
commits, pushes, or resolves a conflict — and neither should you.

Three behaviours worth knowing before you run it:

- **A dirty repo is skipped, not stashed.** Stashing hides work behind a command
  the user did not run; skipping is loud and reversible. Report it and move on —
  the audit will then be running against stale code for that repo, which the
  script says explicitly.
- **Merges are `--ff-only`.** A local `main` with unpushed commits stops with
  `diverged` rather than creating a merge commit in a repo you are only meant to
  read.
- **Branch switches are reported.** `beevia-mobile` in particular has sat on
  feature branches (`Mock-data`). Switching it to `main` is intended here, but
  surface it in your summary — someone may be mid-task on it.

## Step 3 — drift

Delegates to the **`beevia-audit`** skill. Read its SKILL.md for how to act on
each finding; it covers the four spec files, the house style for adding an
operation, and the `x-beevia-*` prohibition.

## Step 4 — update the specs

Driven by the audit output, not by re-reading everything. For each finding:

| Finding | Action |
|---|---|
| Route in code, absent from spec | Add to the **implemented** spec. Read the controller *and* its DTO for the real contract — summary, request schema, status codes, auth, error codes. |
| Proposed endpoint now shipped | **Move** it from the proposed file to the implemented one and delete it from proposed. Never leave it in both. |
| Route in spec, absent from code | It was removed or renamed. Confirm in the sync diff before deleting. |
| Contract changed (new field, new guard) | Update the operation in place. |

Four spec files, split by **file, not by marker**:

| | Implemented | Proposed |
|---|---|---|
| `beevia-api` | `openapi.yaml` | `openapi.proposed.yaml` |
| `beevia-admin-api` | `openapi.admin.yaml` | `openapi.admin.proposed.yaml` |

The implemented files carry **no status markers at all** and must stay safe to
generate clients from. An earlier design used `x-beevia-status` extensions in
one merged file; it was dropped because `x-` is indistinguishable from an HTTP
header and the merged file produced SDKs full of dead methods. The audit fails
if any `x-beevia-*` reappears. Proposed operations cite the PRD via
`externalDocs`.

Then update the affected narrative documents — `api-rfc.md`, `admin-api-rfc.md`,
`suggestions.md` — so their counts and inventories still match. A spec change
that leaves the RFC claiming the old total is worse than no change.

## Step 5 — the status report

Write `project-status/project-status-YYYY-MM-DD.md`, dated today. **A new file
each run** — the folder is a history, so never overwrite a previous day's report.

### First: read the previous report and the delta

**Before writing a word, do both of these.** A status report whose only input is
today's snapshot cannot say whether anything is getting better or worse, which
is the main thing a reader wants from it.

1. **`audit.py` emits a `SINCE <previous export>` section** (and `delta` in
   `--json`): status movement, how many items *left* review, how many became
   Done, what entered, and any items added or removed. Throughput is not
   derivable from one export — a queue of 74 looks identical whether it is
   frozen or turning over completely. Use these numbers; do not eyeball two
   CSVs.

2. **Read the most recent `project-status/*.md`.** Two obligations come from it:

   - **Carry its recommendations forward.** For each "what I would do this week"
     item, say whether it happened. A recommendation that silently disappears
     between reports teaches the reader that the section is decorative.
   - **Correct it where it was wrong, prominently.** If new data contradicts a
     previous claim, say so in the overview, name the claim, and explain what
     changed. This is not optional politeness — an uncorrected error compounds,
     because the next reader treats the old report as established fact.

   The 2026-08-05 edition asserted "the review queue is new, not stale" from the
   `Last Modified` column. It was wrong by roughly 5×, and the 2026-08-06 edition
   opens by correcting it. That correction happened because someone remembered;
   this step exists so it does not depend on memory.

If there is no previous report or only one export, say so in the appendix rather
than presenting a first snapshot as if it showed a trend.

Match the existing structure (`project-status-2026-08-05.md` is the reference):

1. Title, `**As of <date>**`, sprint name and window, and the source files used.
2. `## Quick overview` — **the whole point of the report.** One bolded sentence
   that states the actual situation, a small table of headline numbers **with a
   change column against the previous report**, and "the three things worth
   knowing". Someone who reads only this section and stops should not be misled
   by anything in it.
3. Numbered detail sections: sprint breakdown (including movement since the last
   export), what shipped, PRD gap, risks, what to do this week — with the
   previous edition's recommendations resolved.
4. `## Appendix — method`, including anything the data cannot support.

Ground every number in the export or the audit JSON. Where the data cannot
answer a question, say so in the report rather than estimating — the 2026-08-05
edition has a "the board cannot measure velocity" section for exactly this
reason (all 120 items carry 0 estimation points and no tags).

### The trap that has already produced one wrong report

**Do not measure flow with the `Last Modified` column.** Bulk board operations
rewrite it on dozens of items at once without producing any per-item audit
entry. Bucketing by it once suggested "97 items entered review in the final
three days" — a cliff that did not happen. The activity sidecar showed the real
distribution spread across the whole sprint.

For anything about *when work moved* — queue age, throughput, time-in-status —
read `sprint-board-exports/beevia-activity-<date>.json` and use the
`actiontime` of the relevant status-change entry.

### Team performance — required, in both the overview and detail

**These reports are read daily before standup.** The overview must carry a
per-person table someone can scan in fifteen seconds, and there must be a
detailed section behind it.

In the **quick overview**, a compact table: person, what they own, items
submitted to review in the last 7 days, median cycle time, open WIP, commits in
the last 7 days, and a flag column for anything that needs raising. Follow it
with the one or two questions worth asking at standup.

In the **detail section**, the same figures with a paragraph per person, the
weekly submission trend, per-repo last-commit dates, and an explicit limits
subsection.

#### How to compute it

All of it comes from the activity sidecar and git — never from `Last Modified`.

| Metric | Source |
|---|---|
| Submitted to review | Count of transitions to `REVIEW/QA` in the sidecar, by assignee |
| Median cycle time | Days from an item entering `In progress` to reaching `REVIEW/QA` |
| Open WIP + age | Items currently `In progress`, dated from their entry into it |
| Commits | `git log --since=7.days --author=…`, **summing each person's identities** (§ Git identities) |
| Repo staleness | `git log -1` per repo — a repo with no commits for days is a signal the board cannot show |

#### Framing rules — these matter

Performance sections are easy to write badly. Four rules:

1. **Measure flow, not people.** Report what moved and when. Do not rank, score,
   or imply effort. Commit counts reward small commits; cycle time rewards small
   items; neither measures difficulty or quality.
2. **Never blame an individual for a systemic block.** When items sit in review
   because nobody reviews, that is a process finding, not a personal one. Say so
   in the same breath.
3. **Always include a "what this does not measure" subsection.** Without
   estimation points there is no workload normalisation, so a raw item count
   says nothing about who is carrying more.
4. **Absence of data is not absence of work.** Promise has no board presence,
   yet the admin dashboard is being built. Report that explicitly rather than
   letting a blank row read as a zero.

#### The standup-useful signals

Prefer these over totals — they are what changes day to day:

- A repo with no commits for several days (caught `beevia-admin`, stalled 7 days).
- Someone with zero submissions and zero WIP — finished, blocked, or working
  untracked. Worth a question, not an assumption.
- WIP older than the person's median cycle time — probably stuck.
- The team's weekly submission rate against the acceptance rate. If output is
  steady and acceptance is zero, the bottleneck is not the developers, and the
  report should say that plainly.

### Counting items

The board mixes 54 parent Stories with 66 child Tasks. Report both, and say
which you are using: totals that silently double-count parents and their
children make a sprint look twice as large as it is.

## Guardrails

- Never edit a service repo's files. Step 2's git sync is the only write, and
  the rest of this skill is read-only against them.
- Never overwrite a previous day's status report.
- Everything else is written at the workspace root or in `project-status/`.
- Do not commit or push anything unless asked.
- Do not print or commit `.env`; the Zoho refresh token is a live credential.

## When steps fail

The chain is deliberately not `&&`-linked, because a later step is still useful
when an earlier one degrades:

| Failure | Do this |
|---|---|
| Export fails or is rate-limited | Use the most recent CSV in `sprint-board-exports/` and **say in the report which date it is**. Zoho locks out token refresh for 10–30 min; retrying makes it worse. |
| A repo is dirty or diverged | Continue. Report that repo's analysis as based on stale code. |
| Audit exits 2 | Something structural is broken (missing spec, unparseable YAML). Fix that first; its other findings are unreliable. |
| Epic column blank | Known: the refresh token lacks `ZohoSprints.epic.READ`. Note it, do not treat 40 blank epics as "no epic assigned". |
