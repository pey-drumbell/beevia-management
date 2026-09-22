# Beevia — Project Status

**As of 2026-09-15** · Sprint **0901** (3 Sep → 22 Sep) — **day 13** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 13** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-15.csv` + `beevia-activity-2026-09-15.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-15.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (30 items) + sidecar; all five repos at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` read via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. Window **14 Sep 14:03 UTC → 15 Sep 14:04 UTC** (~24 hours, Sun→Mon).

---

## Quick overview

> **The backend had its most substantial day in two weeks — a real internationalisation feature, a bug fix that was silently duplicating accounts, and a second CI security control — while the mobile board caught up on paper without a single new line of code landing anywhere.** Ten commits merged to `beevia-api` (five of them a genuine server-side response-localisation feature, plus fixes for phone-number normalisation and refresh-token diagnostics), and an org-wide secrets scan went live in the three backend repos. On the client side, four of David's items on sprint 0901 moved — one to In progress, three all the way to REVIEW/QA — but every one of those moves was made by a non-contributor in a single bulk action, not by David, and `origin/BVA-I242` (the branch that holds all of it) has not received a new commit since before the last report. The board looks like a stall just ended; the branch says it did not. The admin board shows the same pattern in miniature: Ayomikun moved Promise's own item for him, again.

| Measure | 14 Sep | 15 Sep | Δ |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 4 | **12** | **+8** |
| Commits on *any* ref, all five repos, in window | 6 | 12 | −0 (0 unmerged this window vs 2 last time) |
| Board transitions, all three boards, in window | 6 | **11** | **+5** |
| API surface (consumer / admin) | 137 / 47 | 137 / 47 | 0 |
| Proposed operations (consumer / admin) | 38 / 19 | 38 / 19 | 0 |
| Spec drift vs `origin/main`, both services | 0 | 0 | 0 |
| Sprint 0901 leaves, total | 20 | **21** | **+1** |
| Sprint 0901 leaves To do | 5 | 5 | 0 |
| Sprint 0901 leaves In progress | 3 | **1** | **−2** |
| Sprint 0901 leaves REVIEW/QA | 8 | **11** | **+3** |
| Sprint 0901 leaves Done | 4 | 4 | 0 |
| Admin board leaves In progress / Done | 0 / 6 | **2 / 6** | **+2 / 0** |
| Review-queue median age (0901) | 5.9 d | **6.9 d** | **+1.0** |
| Oldest open WIP (0901) | 9.9 d | **0.9 d** | **−9.0** (queue drained, not resolved — see below) |
| `beevia-mobile` `main` days since a commit | 18.4 | **19.4** | +1.0 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 1.7 / 1.7 / 1.7 | **0.8 / 0.8 / 0.8** | −0.9 each |
| Ayomikun commits (7d, 3 identities, merged) | 23 | **31** | **+8** |
| Promise commits (7d, merged) | 5 | 4 | −1 (an older commit aged out) |
| David commits (7d, any ref) | 1 (branch) | 1 (branch) | 0 |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 29 · 0 / 12 | 0 / 30 · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈58% (58.10) | **≈58% (58.10)** | **0.00** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---:|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 10 on 0901 · 3 on 0901-admin | **10** (7 old + 1 new on 0901, 2 on 0901-admin — see below) | 3.0 d | **0** | **31** (was 23) | The +8 rise is his i18n batch: five feature commits, one bugfix, one merge, one CI commit. His own `BVA-I245` moved itself to REVIEW/QA the same hour the code merged — the cleanest submission this project has recorded. He also moved **Promise's** `BVA-I9` on the admin board without Promise touching it |
| David Samuel | mobile | 7 on 0901 — 2 To do, **1 In progress**, 2 REVIEW/QA, 2 Done | 0 by him — **all three of today's submissions were made by a non-contributor** | 2.6 d | 1: `BVA-I229`, 0.9 d | 1 on `origin/BVA-I242` (unchanged from 14 Sep — no new commit this window) | Four of his items moved status today (`I229`→In progress, `I233`/`I243`→REVIEW/QA) at 16:04–16:06 UTC on **14 Sep**, four hours after his last commit, all three by the same non-tracked actor. The code the moves describe does exist on the branch — but the branch itself has not changed since 14 Sep 11:51 UTC |
| Philip Chidera | design | 4 on 0901 — 2 Done, 2 To do (incl. new `BVA-I268`) | 0 — last 28 Aug, now **18.1 d** | 0.9 d | 0 | — | A new Story, `BVA-I268` *Design the Transaction Receipt Image*, was created 15 Sep 13:58 UTC, ten minutes before this export — no context or child tasks yet |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, **1 In progress** | 0 — zero self-made transitions, still | — | 0 | **4** (was 5, one commit aged out of the 7d window) | His `BVA-I9` moved To do → In progress today, moved by **Ayomikun**, not him. Fourth consecutive edition of zero self-attributed board activity |

**The two questions for standup:** (1) **Has anyone actually looked at `origin/BVA-I242` today, or did the board just get transcribed?** Three of David's items advanced two statuses each in one bulk action four hours after his last commit — the code timeline is plausible (commit at 11:51 UTC, board update at 16:04–16:06 UTC) but it was not David who updated it, and the branch is still 15 commits and unmerged. (2) **Why is a second person now moving Promise's items for him?** First it was nobody touching his board at all; today it's Ayomikun moving `BVA-I9` in the same action as his own work. If Promise is meant to own his board state, that has not happened once in five editions.

**The three things worth knowing:**

1. **A real, substantial backend feature shipped, and it does not move the MVP number — correctly.** Five commits add server-side response-message localisation: `Accept-Language` resolution before sign-in, saved-language precedence after, rendered at the response interceptor and exception filter, cached in Redis. This is genuinely new, well-scoped infrastructure — and it is a *different* feature from the PRD's "message translation" capability (chat messages via `/translate`), which is still a stub bound to `StubTranslateAdapter`, still unmerged on the client side. Crediting this work to capability #3 would be wrong; it is reported here because it is real progress the rubric is not designed to see.
2. **The review queue got older, not because nothing moved, but because what moved joined it rather than left it.** Three new items entered REVIEW/QA and the seven-item notification backlog aged another day; nothing came out. Median age is now 6.9 days with 7 days left in the sprint.
3. **The "Done with no code" trap was avoided this time, narrowly, and by the pattern that avoided it is worth naming.** Unlike 11 September, today's bulk board move sent items to REVIEW/QA and In progress — not Done — and the underlying branch commit predates the board update by about four hours. That is consistent with someone reading the branch before transcribing it, which is a better process than the alternative. It is still not the owner doing the transcription, and it still describes a review queue whose only exit routes on record are a 47-second bulk sweep and closing items without a queue at all.

**If you read nothing else:** the backend keeps shipping real, verifiable work (i18n, a duplicate-account bug fix, a second security scan) while the mobile side's board activity continues to be performed by someone other than its owner, on a branch that has been unmerged for 40 days. Nothing about today's board movement should be read as the branch getting closer to landing — it is the same 15 commits it was on 14 September.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

30 items — **21 leaves, 9 parent Stories** (was 29 / 20 / 9). Day 13 of 20, 7 days remain.

| Status | Leaves | 14 Sep | Δ |
|---|---:|---:|---:|
| To do | 5 | 5 | 0 |
| In progress | **1** | 3 | **−2** |
| REVIEW/QA | **11** | 8 | **+3** |
| Done | 4 | 4 | 0 |
| BLOCKED | 0 | 0 | 0 |

| Owner | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Ayomikun Araoye | 10 | 1 | 0 | **9** | 0 |
| David Samuel | 7 | 2 | **1** | **2** | 2 |
| Philip Chidera | 4 | 2 | 0 | 0 | 2 |

### 1.2 Who actually moved each item

Every status change this window traces to an exact timestamp in the activity sidecar. Laid out by actor, because the actor is not always the assignee:

| Item | Owner | Change | When (UTC) | Moved by |
|---|---|---|---|---|
| `BVA-I245` | Ayomikun Araoye | In progress → REVIEW/QA | 14 Sep 14:53:15 | **Ayomikun Araoye** (self) |
| `BVA-I229` | David Samuel | To do → In progress | 14 Sep 16:05:06 | *non-contributor* |
| `BVA-I233` | David Samuel | In progress → REVIEW/QA | 14 Sep 16:04:40 | *non-contributor* |
| `BVA-I243` | David Samuel | In progress → REVIEW/QA | 14 Sep 16:04:45 | *non-contributor* |
| `BVA-I268` | Philip Chidera | Created | 15 Sep 13:58:17 | *non-contributor* |

Per the standing instruction on non-contributors, the actor behind the second and third rows is not named here — they are not one of the four people whose work this report tracks. What matters is the pattern: **Ayomikun's own submission is self-reported and lands within minutes of the merge it describes; David's are administrative and lag his last commit by about four hours.** Neither is inherently wrong, but they are not the same kind of evidence, and this report has now seen the second pattern from two different non-tracked actors in two different editions (Philip's predecessor did this for David on 11 September; a different actor did it again today).

**The code timeline is at least plausible.** `origin/BVA-I242` gained `b91d765` ("app localization") on 14 Sep at 11:51 UTC — before the 16:04 board update, not after. So unlike the 11 September Done-with-no-code case, this transcription followed the code rather than anticipating it. It is still not self-reported, and the branch is still unmerged.

### 1.3 The review queue — now 6.9 days median, still nothing has come out

| Item(s) | Owner | Entered REVIEW/QA | Age |
|---|---|---|---:|
| `BVA-I246`–`BVA-I252` (7 items) | Ayomikun Araoye | 8 Sep 16:02–16:04 UTC | **6.9 d** |
| `BVA-I231` | Ayomikun Araoye | 10 Sep 10:25 UTC | 5.2 d |
| `BVA-I245` | Ayomikun Araoye | 14 Sep 14:53 UTC | 1.0 d |
| `BVA-I233` | David Samuel | 14 Sep 16:05 UTC | 0.9 d |
| `BVA-I243` | David Samuel | 14 Sep 16:05 UTC | 0.9 d |

**Median age: 6.9 days** (was 5.9), because the original seven-item block is still the majority of the queue and it aged another day. **Nothing has left REVIEW/QA on this sprint in the eight editions this report has tracked it.** Seven days remain before 22 September; the queue is now larger (11 vs 8) and its oldest members older, in the same window that added three fresh items to the back of the line.

`FCM_SERVICE_ACCOUNT` is still blank in `beevia-api/.env.example` (line 79) and still optional in `common/env.ts`, re-verified at `origin/main` today. Accepting `BVA-I246` without checking the deployed value still accepts a `StubPushAdapter`.

### 1.4 WIP dropped to near-zero, and that is a queue effect, not a resolution

Only one leaf is In progress anywhere on this sprint: `BVA-I229` (David), 0.9 days old. The two items that made "oldest open WIP" 9.9 days on 14 September (`BVA-I233`, `BVA-I243`) did not get finished — they moved to REVIEW/QA in the same bulk action described in §1.2. **A queue that goes from "old WIP" to "old REVIEW/QA" has not gotten faster; it has moved the same backlog one column to the right.**

### 1.5 `origin/BVA-I242` — unchanged since 14 September, now 40 days old

- Still **15 commits ahead of `main`**, tip unchanged at `b91d765` (14 Sep 11:51 UTC).
- First commit on this lineage (`origin/BVA-I192`, 6 Aug) is now **40 days** old; the branch has carried the wallet flow, p2p transfers, external transfers, transaction history, notifications and localisation for that entire span without merging.
- By the MVP rubric's rules, all of it remains worth zero until it reaches `main`.

### 1.6 Trust & Safety scope — unchanged, unpriced

`BVA-I253`–`BVA-I256`, created 11 September, are all still **To do** with **0 estimation points**. No code exists for any of them. The previous edition's recommendation to price or defer this scope has not been acted on.

### 1.7 New scope: one Story, no context yet

`BVA-I268` *Design the Transaction Receipt Image* (Philip Chidera, Story, To do) was created 15 Sep 13:58 UTC — 10 minutes before this export ran. It has no child tasks, no epic, and no description yet, so nothing else can be said about it this edition. Flagged rather than analysed, since analysing an item minutes after creation risks the same error as reading `Last Modified` too early.

### 1.8 Still no estimates — tenth consecutive edition

**0 of 30 on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01.** Every item on every board carries the literal value `0`, not a blank — confirmed by checking the raw field, not just truthiness. Velocity remains underivable.

---

## 2. What shipped this cycle

**12 commits merged to `origin/main` across three repositories; zero to `beevia-admin` or `beevia-mobile`.**

| Repo | Commits | What |
|---|---:|---|
| `beevia-api` | **10** | 5× `feat(i18n)`: response-message localisation (chat/attachments/invites/devices/uploads/ledger; payments/cards; users/wallets/topups; KYC/banking-upgrade; the response-interceptor + exception-filter foundation with Redis-cached locale); `fix(auth)`: real E.164 phone normalisation (was silently creating duplicate accounts for numbers pasted in national form); `origin/fix/refresh-rejection-diagnostics` merged (previously branch-only); `ci: run the org secrets scan`; 2 merge commits |
| `beevia-admin-api` | 1 | `ci: run the org secrets scan` |
| `beevia-db-schema` | 1 | `ci: run the org secrets scan` |
| `beevia-admin` | 0 | No change since `f12135b` (14 Sep) |
| `beevia-mobile` | 0 | No change on any ref since `b91d765` (14 Sep) |

**No commit added, removed or changed a route.** The shadow audit against `origin/main` confirms zero drift (§3).

### 2.1 The i18n feature is real, well-scoped, and outside every current rubric line

Response messages now render in the caller's language: `Accept-Language` is resolved and quality-ordered before sign-in (regional tags folded — `es-MX`→`es`, `en-AU`→`en-US`); the user's saved language preference takes over once one exists. Rendering happens at exactly the two edges every response passes through — the interceptor and the exception filter — so services stay ignorant of who is asking. This reuses the resolver `/translate/preferences` already built.

This is **not** the PRD's chat-message-translation capability, and does not move that score (§Appendix). It is UI/system-message localisation, a different and legitimate piece of internationalisation work that the current 11-capability rubric has no line for. Recorded here so it is not mistaken for progress on `/translate`, and not lost either.

### 2.2 A real duplicate-account bug is fixed

Signup accepted `+23408089421407` — a country code with a Nigerian number in national form (trunk zero included) pasted on. The old regex (`/^\+[1-9]\d{6,14}$/`) validated shape, not dialability, and nothing normalised the stored value, so `users.phone` — unique on the string — recorded two spellings of one person as two rows, neither able to see the other's onboarding. Fixed and normalised to real E.164 today.

### 2.3 A second CI security control lands, in the same three repos as the first

`ci: run the org secrets scan` calls a shared reusable workflow that scans full commit history (not just the working tree), on push, pull request and weekly — so a credential that was committed and later deleted still surfaces. This is a second, independent control alongside the 12 September supply-chain guard, and it has the same gap: **`beevia-admin` and `beevia-mobile` have neither workflow.** `beevia-mobile` remains the one repository that has gone the longest without a commit to `main` (19.4 days) — precisely the case both controls exist to protect, and it now has zero of the two available guards.

---

## 3. Spec updates made this cycle

**None, and none were warranted.** No merged commit added, removed or altered a route (confirmed: the i18n batch changes message content, not endpoints; the E.164 fix changes internal validation; the diagnostics fix changes error detail, not shape). The deterministic audit run against a read-only `origin/main` shadow reports:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 47  spec= 47  proposed= 19  [OK]
```

**Drift: zero, both services, both directions.** All four spec files parse; no `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s.

Per the audit skill's instruction for a clean run, `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin.yaml`, `openapi.admin.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md` and `suggestions.md` are unmodified today. (Separately, these files already carry an uncommitted diff from a prior session reconciling them to this same 137/47 state — that diff predates this run, was not touched today, and is left as-is per the no-commit instruction.)

**The working-tree audit still reports 19 phantom drift lines** (6 `beevia-api`, 13 `beevia-admin-api`) because three repositories remain `diverged` from the 8 September incident and their local working trees are still 4 September code. **Eighth consecutive edition flagging it**, so nobody "fixes" the spec by deleting operations that exist at `origin/main`.

### 3.1 The access-control gap is unchanged and still open

Re-verified: `GET /admin/reports/{id}` and `GET /admin/reports/{id}/download` still resolve `viewableModules` only at generation time (`reports.service.ts:133`) and never re-apply it at read. No commit touched this file this cycle. Still live behind a client that consumes it.

---

## 4. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 13.** 12 items — **8 leaves, 4 parent Stories**. Two transitions in the window, both by the same person, in the same second as unrelated work.

| Status | Leaves | 14 Sep | Δ |
|---|---:|---:|---:|
| To do | 0 | 2 | **−2** |
| In progress | **2** | 0 | **+2** |
| Done | 6 | 6 | 0 |

| Owner | Leaves | In progress | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | **1** | 3 |
| Ayomikun Araoye | 3 | **1** | 2 |
| Unassigned | 1 | 0 | 1 |

`BVA-I7` (Story, parent), `BVA-I8` (Ayomikun's own task) and `BVA-I9` (**Promise's** task) all moved To do → In progress at **14 Sep 14:53:48 UTC — the same second as `BVA-I245`'s move on the main board (§1.2)** — and all three were moved by **Ayomikun Araoye**, not by Promise or by a board administrator.

**This is a new variant of a finding this report has carried for five editions.** Previously the concern was that *nobody* moved Promise's items. Today a specific, tracked teammate moved one for him, in the same action as his own unrelated backend work — which reads as a courtesy or a habit, not malice, but it means the "have Promise move his own items" recommendation has now been overtaken by someone else consistently doing it for him. **Promise still has zero self-attributed transitions on this board, across every edition it has existed.**

### 4.1 Never summed with the main board

8 leaves here and 21 on sprint 0901 are different projects and different backlogs. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards.

---

## 5. Team performance — detail

All figures from the activity sidecars and git, never `Last Modified`. Commits are trailing-7-day, merged to the default branch except where stated, summing each person's git identities, excluding bots.

**Ayomikun Araoye — backend + admin API.** **31 commits** in the trailing 7 days (`beevia-api` 15, `beevia-admin-api` 11, `beevia-db-schema` 5). The rise from 23 is entirely today's i18n batch, the phone-normalisation fix, and the secrets-scan commit — recomputed and consistent with the raw `git log` listing. **His own `BVA-I245` moved to REVIEW/QA at 14:53:15 UTC, three minutes after the last i18n commit merged (PR #42 at 14:56:49 UTC)** — self-reported and essentially real-time, the cleanest submission-to-code correlation this report has recorded. Zero open WIP on 0901. On the admin board, he also moved his own `BVA-I8` and Promise's `BVA-I9` in the same bulk action (§4).

**David Samuel — mobile.** **Zero self-made submissions**, again. All three of today's board moves on his items were made by a non-contributor (§1.2), four hours after his last commit (`b91d765`, 14 Sep 11:51 UTC) — which itself remains the only commit on `origin/BVA-I242` since the last report; the branch is unchanged at 15 commits, now 40 days old. One open WIP, `BVA-I229`, 0.9 days — freshly created by the same bulk action, not by him working on it today.

> The question this report has now asked across several editions — *is the mobile board being transcribed by someone other than its owner* — has a second, independent data point today: a different non-tracked actor did exactly what Philip's predecessor did on 11 September, on the same branch, for the same person's items.

**Philip Chidera — design.** No submissions; last was 28 August, now **18.1 days** ago. Zero open WIP. One new Story appeared under his name today (`BVA-I268`, §1.7), created by a non-contributor 10 minutes before export — too fresh to say anything about beyond noting it exists.

**Promise Udo — admin dashboard.** **4 commits** in the trailing window (was 5 — one commit from 7 September aged out of the 7-day window; nothing was lost, the window simply moved). Zero board transitions by him, still — his `BVA-I9` moved today, by Ayomikun (§4). His three Done items retain their merged code from last cycle; nothing new shipped to `beevia-admin` this window.

### 5.1 What these figures do not measure

- **They cannot see a branch.** `origin/BVA-I242`'s 40 days and 15 commits remain invisible to every board metric.
- **They cannot tell who actually did the board update.** Three of today's four leaf-level transitions were administrative, not self-reported, and the sidecar is the only place that distinguishes them.
- **They say nothing about review quality.** The review queue has had exactly one exit route in this project's history: a 47-second bulk sweep. Nothing has left it item-by-item.
- **No estimation points exist on any item, on any of three boards** — 0/64, 0/30, 0/12, confirmed at the raw-field level today (§1.8).
- **Correctness and testing remain out of scope for scoring**, per the owner's 2026-08-07 instruction.

---

## 6. Previous recommendations — where they stand

| Recommendation from 14 Sep | Status on 15 Sep |
|---|---|
| Merge `BVA-I242`, or say why it cannot merge | ❌ **Not done.** Unchanged at 15 commits, now 40 days |
| Scope the eight items in REVIEW/QA before 22 September | ❌ **Not done, and worse.** Queue is now 11 items, median age up to 6.9 d |
| Decide whether Done requires merged | ⚠️ **Not decided as a rule**, but today's bulk move went to REVIEW/QA rather than Done — the safer of the two failure modes, whether or not it was deliberate |
| Fix the report read-scoping | ❌ **Not done.** No commit touched `reports.service.ts` |
| Add the `enabled` flag to the translation preference | ❌ **Not done** |
| Settle what happens to `POST /translate` | ❌ **Not done.** `translate.module.ts:23` unchanged, re-verified |
| Add the supply-chain guard to `beevia-admin` and `beevia-mobile` | ❌ **Not done** — and a *second* guard (secrets scan) landed today, also skipping both repos |
| Move the cut-off to ~20:00 UTC and the daily export to sprint 0901 | ❌ **Not done.** `ZOHO_SPRINT_FILTER` re-verified still `08-01` |
| Price the Trust & Safety scope, or defer it | ❌ **Not done.** All four items still To do, 0 points |
| Have Promise move his own board items | ❌ **Not done — and today someone else moved one for him again** (§4) |
| Adopt the Reports truncation pattern in reconciliation | ❌ **Not done** |
| Add the route-collision check to CI, on push | ❌ **Not done** |
| Put estimation points on all three boards | ❌ **Not done.** 0/30, 0/12, confirmed at the raw-value level |
| Apply the BVN-ordering guard to `POST /kyc/profile` | ❌ **Not done** |

**One of fourteen resolved, one downgraded from "open" to "handled once, informally."** The pattern from the last four editions continues: code-shaped asks (merge the branch, add a flag, add a CI check) sit untouched regardless of how cheap they are, while the team's actual output this window went to a well-executed piece of work that was not on this list at all (the i18n feature). That is not a criticism of the choice — the work was good — but it means the list itself may not be reaching the people prioritising day to day.

---

## 7. What I would do this week

Reordered by remaining time. **Seven days left in sprint 0901.**

1. **Merge `origin/BVA-I242`, or explicitly split it.** Forty days, fifteen commits, and it is now the single largest gap between the board and reality on this project. Every day it does not move is a day the MVP estimate cannot reflect real client work.
2. **Get a human decision on the REVIEW/QA queue before 22 September, not on it.** Eleven items, 6.9-day median, zero item-by-item exits ever recorded. If the plan is another bulk sweep, say so now rather than let the sprint end with the question open.
3. **Ask David directly whether he made today's board moves, or whether someone did it for him.** The code timeline is consistent with a good-faith transcription, but this is now two editions running where his items moved without him touching them — worth confirming rather than assuming.
4. **Fix the report read-scoping gap** (§3.1). Unchanged, free two editions ago, now guarding a live consumer.
5. **Decide what happens to `POST /translate`.** The client's own architecture (on-device translation) has answered this in practice for weeks; a decision costs one sentence.
6. **Add both CI security controls to `beevia-admin` and `beevia-mobile`.** Two workflows now exist and both skip exactly the two repos with the least other oversight.
7. **Have Promise make at least one board transition himself**, or agree explicitly that someone else owns his board state — the current arrangement (silently done by whoever else is already moving things) is a process choice nobody has actually made.
8. **Price or defer the Trust & Safety scope.** Four editions unpriced.
9. **Put estimation points on all three boards, or say the project does not estimate.** Tenth edition asking.
10. **Move the daily export's sprint filter and cut-off.** The workaround (scratch export) works, but it is manual and has now run for nine consecutive editions.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync attempt (**0 repos advanced — `beevia-admin` and `beevia-mobile` already current; 3 refused as `diverged`, unchanged from prior editions**) → deterministic audit against the working tree → a second audit against a read-only `origin/main` shadow built with `git archive` → read-only scratch export of sprint 0901 (30 items) → `git log` sweep of every ref across all five repositories for the window → this report. No spec file was modified, because the audit was clean.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran. No repository was reset, rebased, reverted, or cleaned; no sub-repo file was edited; the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed, or deployed.

**Degraded inputs.**

- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are still `diverged` from the 8 September incident; `sync_repos.py` correctly refuses to force a merge. Their working trees remain 4 September code, the sole cause of the working-tree audit's 19 phantom drift lines. Every code claim in this report is made against `origin/main`, read via a `git archive` shadow, not the stale working tree.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, a sprint that closed 28 August. The in-repo main export therefore reads a closed, frozen sprint (delta: zero movement, as expected). All sprint-0901 figures in this report come from a read-only scratch export to `/tmp/beevia-scratch/`, not from `sprint-board-exports/`. Ninth consecutive edition working around this.
- **The `Epic` column is blank** on both in-repo boards — a known OAuth scope gap (`ZohoSprints.epic.READ` not granted), not "no epic assigned."
- **`Comments` bodies are unavailable** from the API.
- **The window ends at 14:04 UTC**, so anything after that today is unobserved by this edition.
- **Repository integrity was not hash-swept this cycle**; the three CI/i18n commits and the two non-i18n backend commits were read via `git show`/`git log` but not diffed byte-for-byte against a known-good baseline.
- **Branch protection, credential rotation, and workstation remediation remain unverifiable** from this workspace.
- **No estimation points exist on any of the three boards**, confirmed at the raw CSV value level (every field literally contains `"0"`, not blank) — velocity is not derivable and no per-person load is size-normalised.
- **The activity sidecars only carry history for items currently on their board**; an item since removed would not appear.

**Window.** 14 Sep 14:03 UTC → 15 Sep 14:04 UTC — a normal ~24-hour cadence, unlike the 3-day window in the previous edition. All `actiontime` and board figures are UTC; the local export host runs UTC−6.

**Sources.** Boards: `beevia-sprint-board-2026-09-15.csv` (64 rows, 41 leaves, sprint 08-01, unchanged) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-15.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (30 rows, 21 leaves) + activity sidecar. Code: all five repositories at `origin/main` — `beevia-admin`, `beevia-mobile` read from the synced working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` read from a `/tmp` shadow built with `git archive`. Specs: `openapi.yaml` (137), `openapi.proposed.yaml` (38), `openapi.admin.yaml` (47), `openapi.admin.proposed.yaml` (19) — all validated, zero drift against `origin/main`.

**A note on who appears here.** Only people whose work is tracked have rows. The two non-contributor board actions this edition (§1.2, David's items; the item-creation for `BVA-I268`) are reported without naming the actor, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈58% (estimate; 58.10, unchanged)

**Target 2026-09-01 (provisional) · the target date passed fourteen days ago.** On merged build evidence the product remains at **58.10 of 100**, unchanged from the previous edition. Zero scores moved this cycle.

**Why the day's most substantial commit does not appear below:** the i18n response-localisation feature (§2.1) is real, merged, and touches more of the codebase than any single commit in the last week — but it is not the PRD's chat-message-translation capability (#3), which is scored specifically on `/translate`, its client consumer, and the opt-in flag. That capability's underlying facts are unchanged: the stub adapter is still bound, the on-device engine is still on the unmerged branch. Crediting today's real work to the wrong line would be worse than not crediting it at all; it is recorded in §2.1 instead.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Unchanged. No merged commit touched `src/messaging/` |
| 2 | Voice & video calling | 8 | 0.8 | Unchanged. Push transport still falls back to a stub without `FCM_SERVICE_ACCOUNT` |
| 3 | Message translation | 7 | 0.30 | **Unchanged, deliberately** (see above). `translate.module.ts:23` still binds `TRANSLATE_PORT` to `StubTranslateAdapter`. On-device engine and `/translate/preferences` client call still exist only on `origin/BVA-I242`, unmerged |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged |
| 5 | International KYC tier | 6 | 0.0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged. `PaymentService.activeNgn()` re-verified |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. No merged client request/receive flow |
| 8 | Cross-currency FX | 12 | 0.0 | Proposed only |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. `main` still has zero client `/cards` references |
| 10 | Consent management | 4 | 0.0 | No endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.90 | Unchanged. No `beevia-admin`/`beevia-admin-api` commit touched a scored module this cycle |
| | **Weighted total** | **100** | **58.10** | **≈58% · Δ 0.00** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches.

### What this report cannot tell you

- **When, or whether, `origin/BVA-I242` will merge.** Still the largest single uncertainty in the estimate.
- **Whether David made today's board moves himself, delegated them, or was unaware of them.** The code timeline is plausible; the sidecar cannot distinguish intent.
- **Whether the eleven items in REVIEW/QA will be reviewed individually, swept, or left.** No new precedent was set this window.
- **Whether the i18n feature has a deployed, tested consumer** beyond the server-side response envelope — that is outside what a git clone can verify.
- **Whether `FCM_SERVICE_ACCOUNT` is set in any deployed environment.**
- **Whether the two CI security controls have actually run, or passed.** Both are committed and scheduled; run history lives on GitHub, not in the clone.
- **What `BVA-I268` actually asks for.** Created 10 minutes before this export, with no description yet.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 30, 0 of 12 items estimated.
