# Beevia — Project Status

**As of 2026-09-10** · Sprint **0901** (3 Sep → 22 Sep) — **day 8** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 8** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-10.csv` + `beevia-activity-2026-09-10.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-10.csv` + its activity sidecar (12 items); a read-only scratch export of sprint 0901 (25 items); all five repos read at `origin/main`.

Scope: three boards, kept separate and never summed. Window 9 Sep 14:03 UTC → 10 Sep 14:03 UTC.

---

## Quick overview

> **The best delivery day this project has had, and a correction that this pipeline has now had to make twice. Eleven endpoints merged across two services — the translation language-preference surface and the whole admin Reports module — and for the first time the board moved *because* code merged rather than instead of it: `BVA-I231` entered review an hour after its own commit landed. Against that, yesterday's report said "the review queue has never had anything leave it on this project". It has: 46 items left it on 3 September, in 47 seconds, in a sprint-close sweep that this pipeline's own 3 September edition documented in full. The claim was not missed — it was *un-corrected*, six days after being corrected.**

| | 9 Sep | 10 Sep | Δ |
|---|---:|---:|---:|
| API surface (consumer / admin) | 131 / 42 | **137 / 47** | **+6 / +5** |
| Proposed operations (consumer / admin) | 42 / 19 | **38** / 19 | **−4** / 0 |
| Spec drift vs `origin/main`, both services | 0 | **0** | 0 |
| Sprint 0901 leaves in REVIEW/QA | 7 | **8** | +1 |
| Sprint 0901 leaves In progress | 6 | 7 | +1 |
| Sprint 0901 leaves To do | 3 | 2 | −1 |
| Sprint 0901 leaves BLOCKED | 1 | **0** | **−1** |
| Admin board leaves Done | 2 | **6** | **+4** |
| Admin board leaves In progress | 2 | **0** | −2 |
| Items recorded leaving REVIEW/QA forward | **"never"** | **46, in one sweep** | **correction, §0.1** |
| Ayomikun commits (7d, 3 identities) | 22 | **30** | +8 |
| `beevia-mobile` `main` days since a commit | 14 | **15** | +1 |
| Estimation points set (0901 / 0901-admin) | 0 / 25 · 0 / 12 | 0 / 25 · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈57% | **≈58%** | **+1.2 pt** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 9 on 0901 · 3 on 0901-admin | **1** (was 8) | 3.0 d | 1 (0.2 d) | **30** | Eleven endpoints, two services, one migration, all with tests. Also made **every one of the 22 transitions on the admin board**, including four items he does not own (§5.2) |
| David Samuel | mobile | 6 on 0901 — **4 In progress** | **0** — last was 3 Sep | 2.6 d | 4; ages **5.9 d ×2**, 2.1 d, 1.9 d | 0 to `main`, 0 new on `BVA-I192` | `beevia-mobile` `main` untouched **15 days**; the 14-commit branch has not moved in 3 days; two WIP items at ~2.3× his median. Second edition asking |
| Philip Chidera | design | 2 on 0901 — both In progress | 0 — last was 28 Aug | 0.9 d | 2; ages **5.9 d**, 1.9 d | — | `BVA-I240` at **6.6× his own median**. No submission in 13 days |
| Promise Udo | admin dashboard | 4 on 0901-admin — **3 now Done** | — | — | 0 | 4, none since 8 Sep | **His three Done items have no code.** `beevia-admin/src/features/reports/api.ts` is still `MOCK IMPLEMENTATION`, untouched since 1 Sep — and he did not mark them Done (§5.1) |

**The two questions for standup:** (1) **On the admin board, does "Done" mean the backend half is merged?** Three of the six Done leaves are Promise's front-end halves, the reports client is still a mock file, and all three were marked Done by someone else. Either the definition is "my side is written" — in which case three items are simply wrong — or the board is being closed ahead of the work (§5.1). (2) **Who reviews the eight items in REVIEW/QA, and does anything stop them being closed the way the last 46 were?** §0.1 changes this question: the queue is not frozen, it is *emptied at sprint close*, in one action, by one person.

**The three things worth knowing:**

1. **The review-queue claim regressed, and it regressed against this pipeline's own reporting.** Yesterday's risk #5 read *"the review queue has never had anything leave it on this project"*. The 3 September edition of this same report opens by describing the sweep that emptied it — 46 items marked Done in 47 seconds, from a queue that had waited a median of 16.7 days. **The precise truth is sharper than either version: the forward path out of REVIEW/QA has been exercised exactly once, in one bulk action, and every other completion on this project skipped the queue rather than passing through it** (§0.1). The diagnosis changes with it: the problem is not that nothing is ever accepted, it is that **acceptance is a sprint-close formality rather than a review** — which is different, and actionable before 22 September.
2. **Eleven endpoints merged, and the board moved because of them.** `beevia-api` gained the six-operation translation language-preference surface (`a08bf13`, schema `v0.0.30`); `beevia-admin-api` gained the five-operation Reports module (`434d5e6` plus two same-morning extensions). `BVA-I231` entered REVIEW/QA at 10:25 UTC — **one hour and nine minutes after its own commit merged**. That is the first time in this pipeline's history that a board transition and the code it describes have lined up on the same morning; contrast yesterday's seven items, which described July (§1.3). Three admin-board items followed their backend within 20 minutes of the same pattern.
3. **The `/admin/reports` path collision landed seven hours after this report predicted it, and the recommendation had no chance of being acted on.** Yesterday's §4.3 said *"a five-minute edit today and a breaking rename after the merge"*. The branch merged at 23:02 UTC that evening. Nothing broke — no client consumed either path — but the pattern is worth keeping: **a conflict caught by a daily review is caught on a daily cadence, while a merge happens on the author's, which can be hours.** Resolved today by renaming Module 4's proposal to `/admin/chats/reports/{reportId}` (§4.4).

**If you read nothing else:** the review-queue risk this report has escalated for two editions was stated wrongly and is now downgraded — the queue is not frozen, it is *swept at sprint close*, and sprint 0901 closes on 22 September with eight items in it; a genuinely good day of delivery landed eleven endpoints and, for once, a board that agrees with the codebase; three items are marked Done on the admin board for client code that does not exist; and one new access-control gap shipped with the Reports module and is cheapest to fix this week (§4.5).

---

## 0. Corrections

### 0.1 Correction — items *have* left REVIEW/QA, and this pipeline said so six days ago before un-saying it

**Claim (2026-09-09 risk #5 and §6.3): "the review queue has never had anything leave it on this project" · "nothing has *left* REVIEW/QA on any board".**

Both are false, and — this is the part that matters — **they contradict this pipeline's own 3 September edition**, which opens with: *"Sprint 08-01 was closed by marking 46 items Done in a two-minute window, taking the twenty-three-day-old review queue from 28 to zero without a line of code changing."* That edition carries the timestamps, the actor, the 16.7-day median wait, and a full list. Nothing was discovered today. **A finding this pipeline documented in detail was quietly reverted to a pre-correction sentence six days later.**

Re-derived from `beevia-activity-2026-09-10.json`, the main board's audit trail records **66 transitions into Done**, and the split is sharper than either version of the claim:

| When | Count | From | By | Reading |
|---|---:|---|---|---|
| 12 Aug – 31 Aug, over 6 days | **20** (12 leaves, 8 parents) | In progress (8), BLOCKED (6), To do (6) — **never REVIEW/QA** | Philip Chidera (11), Ayomikun Araoye (9) | Owners closing their own items, **bypassing review entirely** |
| **3 Sep, 09:07:58 → 09:08:45 UTC** | **46** (30 leaves, 16 parents) | **REVIEW/QA — all 46** | One person, a non-contributor | **The sprint-close sweep, in 47 seconds** |

So the precise statement, which no previous edition has made and which is stronger than either the "never" or the "66 times" version:

> **The forward path out of REVIEW/QA has been exercised exactly once, in one bulk action, by one person who does not write the code.** Every other completion on this project skipped the queue rather than passing through it.

That is why all 41 leaves of sprint 08-01 read `Done` today. They were not reviewed to Done; the sprint closed over them.

**How the claim regressed.** The 31 August edition corrected an earlier "zero exits" figure to "items have left REVIEW/QA 22 times, all backwards, zero to Done" — true on that date. The 3 September edition then recorded the sweep. The 8 and 9 September editions restated the pre-31-August sentence. **This is the second consecutive edition to reinstate a superseded claim by carrying a sentence forward instead of re-deriving it** — the first was the admin board on 8 September, and yesterday's §0.2 named the failure mode exactly: *"a claim that has been true for nineteen days is the most dangerous kind to restate, because nothing about repeating it feels like an assertion."* A claim that was **already corrected once** is more dangerous still.

**One mechanical note worth keeping**, because it makes the check easy to get wrong: Zoho does not record a move into Done as a status update. Every other transition carries `action: "Updated the status"`; a move into Done carries **`action: "Item Completed"`**, and the reverse carries `"Item Reopened"`. An extraction that keys on the word "status" sees 176 transitions on this board and silently drops 66 more. That is the same shape as the `Last Modified` trap the export skill documents at length, and it is why the deterministic audit's `delta` block — which reports "0 left review" — should not be read as "nothing was ever completed".

**Three consequences, and the third is the one that matters:**

- **The two-edition "output with zero acceptance" framing was wrong**, and any recommendation built on it should be re-read. Sprint 08-01 did not end with a frozen queue; it ended with a swept one.
- **What is true is narrower and still true: nothing has left review on sprint 0901.** Eight leaves sit there, the oldest 1.9 days old. On a sprint 8 days into 20, that is unremarkable — not a bottleneck. **This risk is downgraded, not closed.**
- **The real finding is the 47 seconds, and it is a forecast rather than a complaint.** Forty-six items — including `BVA-I192`, whose 14-commit branch is *still* unmerged today — went to Done in under a minute on the day the last sprint closed. Sprint 0901 closes on **22 September** with eight items sitting in the same column, seven of which describe July code. **The question worth asking is not "why does nothing get reviewed" but "what happens to these eight on the 22nd".**

It also settles a puzzle three editions have carried. `BVA-I192` has been reported as "a Done board item over an unmerged 14-commit branch", implying someone marked it Done in error. Nobody did. It was swept up with 45 others when the sprint closed.

### 0.2 Correction — the collision resolution came a day too late to be a recommendation

Yesterday's recommendation #3 read: *"Decide `/admin/reports` before `feat/admin-reports` merges. Moving Module 4's proposal to `/admin/chats/reports/{reportId}` is a five-minute edit today and a breaking rename after the merge."*

The branch merged as `434d5e6` at **23:02 UTC that same evening**, roughly seven hours after the report was written and before anyone would have read it. The advice was correct and unactionable, which is a specific kind of failure worth naming rather than filing as "not done".

Nothing was actually lost — no client consumes either path, so the resolution executed today is a rename inside a proposal file (§4.4). But the lesson generalises and is now in `suggestions.md` §5.6: **a daily review pass detects conflicts on a daily cadence; merges happen on the branch author's cadence.** A check that runs on push is not a nicer version of the daily audit — it is the only one of the two that is fast enough for this class of problem.

### 0.3 The 14:00 UTC cut-off did not bite today — and that is not evidence it is fixed

Yesterday's §0.4 measured the cut-off costing a full day on eighteen transitions, because the team's board activity clustered at 15:54–16:08 UTC, just after the export ran. Today every event — five merges between 08:49 and 09:25 UTC, and nine board transitions between 09:05 and 10:25 UTC — landed comfortably inside the window, and this edition reports all of it same-day.

That is because the work happened in the morning UTC, not because the cut-off moved. The recommendation stands at its previous strength: a 14:00 UTC cut-off catches a morning-UTC working session and misses an afternoon-UTC one, and there is no way to tell in advance which today was.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

25 items — **17 leaves, 8 parent Stories**. Day 8 of 20.

| Status | Leaves | 9 Sep | Δ |
|---|---:|---:|---:|
| To do | 2 | 3 | −1 |
| In progress | 7 | 6 | +1 |
| REVIEW/QA | **8** | 7 | +1 |
| BLOCKED | **0** | 1 | **−1** |

| Owner | Leaves | To do | In progress | REVIEW/QA |
|---|---:|---:|---:|---:|
| Ayomikun Araoye | 9 | 0 | 1 | **8** |
| David Samuel | 6 | 2 | 4 | 0 |
| Philip Chidera | 2 | 0 | 2 | 0 |

### 1.2 The window's movement — four transitions, all in 90 seconds, all backed by code

| Time (UTC) | Items | Transition |
|---|---|---|
| 10:24:59 | `BVA-I244`, `BVA-I245` | **BLOCKED → In progress** |
| 10:25:03 | `BVA-I230`, `BVA-I231` | To do → **REVIEW/QA** |

Small, and the most legible movement this board has produced. Both halves follow directly from `a08bf13`, merged at **09:16 UTC**:

- **`BVA-I231` *Preference Storage & Precedence Logic* is exactly what merged**, and it entered review **69 minutes later**. Six endpoints, a schema migration released as `beevia-db-schema v0.0.30`, and precedence logic that matches the item's own acceptance criteria (§2.1). This is the first item on this project whose board state, commit and specification can all be checked against each other and agree.
- **`BVA-I245` was unblocked by the same commit**, which confirms an inference rather than leaving it hanging. Yesterday's §1.4 read the BLOCKED state as *"an ordering dependency inside the same person's own queue — but that is inference, and the board should say"*. It was: `BVA-I244`/`BVA-I245` need a stored per-user language to render backend text into, `BVA-I230`/`BVA-I231` provide it, and they moved to In progress four seconds before their prerequisite went to review. The board still does not say — `Blocked by` and `Blocked On` were empty throughout — so the dependency is now *confirmed by behaviour* rather than documented.

Unlike yesterday, no transition in this window was made on behalf of somebody else, and none skipped `In progress`.

### 1.3 Yesterday's seven are unchanged, and the question about them is still open

`BVA-I246`–`BVA-I252` — the notification workstream, all describing code merged in July and August — have sat in REVIEW/QA for **1.9 days** with no further movement. Nothing has touched `src/notifications/`, `src/devices/` or `src/messaging/` in this window either.

The recommendation to settle whether these are being reviewed as new work or acknowledged as already-shipped work is unactioned, and §0.1 raises its stakes: on this project the default fate of an item in REVIEW/QA at sprint close is to be marked Done in bulk. If these seven ride that path on 22 September, the board will record seven notification stories delivered in sprint 0901, and no commit in sprint 0901 will support it.

**`FCM_SERVICE_ACCOUNT` is still blank in `beevia-api/.env.example`** and still optional in `env.ts`, so accepting `BVA-I246` without checking the deployed value still accepts a `StubPushAdapter`.

### 1.4 The translation workstream now has backend code and still has no client code

The sprint's two halves have swapped positions since yesterday.

**Backend: moving.** `BVA-I230`/`BVA-I231` in review, `BVA-I244`/`BVA-I245` unblocked and in progress, six endpoints merged.

**Client: nothing, for the fifteenth day.** `beevia-mobile` `main` is unchanged since 26 August. `BVA-I229` *Translation Engine Integration* — the on-device engine the whole sprint is built on — is still **To do** on day 8 of 20. No branch in the repository carries translation work. Of the four mobile leaves In progress, two have been open **5.9 days against David's 2.6-day median**.

The one client-side reference to translation anywhere in `beevia-mobile/lib` is a route entry in `core/routes.dart`. There is no call to `/translate`, and now no call to `/translate/preferences` either — the endpoints that shipped this morning have no consumer.

`POST /translate` itself is unchanged: `TranslateModule` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`, and the new `GET /translate/languages` is **not** used to validate its `to` field, so the two halves of the translate surface still disagree about what a language is (§4.2).

### 1.5 Still no estimates — seventh consecutive edition

**0 of 25 on 0901, 0 of 12 on 0901-admin.** No tags. Velocity, burn-down and any normalisation of one person's load against another's remain underivable.

---

## 2. What shipped this cycle

Eleven merged operations across two services, plus a schema release. The busiest day this project has had.

### 2.1 `beevia-api` — translation language preferences, 131 → 137

`a08bf13` (`Phoenixdadhev`), merged as `f4f6dd1` at 09:16 UTC. Six operations, all now in `openapi.yaml`.

| Method | Path | What it does |
|---|---|---|
| GET | `/translate/languages` | Five languages with display labels, in picker order |
| GET | `/translate/preferences` | The caller's app-wide language, with where it came from |
| PUT | `/translate/preferences` | Set it. Leaves per-conversation overrides untouched |
| GET | `/translate/preferences/conversations/{id}` | The effective language for one thread, with its precedence |
| PUT | `/translate/preferences/conversations/{id}` | Override it, or clear with `language: null` |
| DELETE | `/translate/preferences/conversations/{id}` | Clear the override |

Backed by `beevia-db-schema` **v0.0.30**: `users.translation_language`, nullable, plus a `conversation_translation_preferences` table keyed on (user, conversation).

**Three design decisions worth keeping, because each closes a trap the client would otherwise fall into:**

- **The null is load-bearing, and the migration commit says so.** `users.translation_language` is null until the user picks, which separates *"chose English (US)"* from *"never chose"*. A default would have erased that distinction on the first row. It is what allows the read path to fall back to the device's language and still report `is_explicit: false`, so a picker never shows a phantom selection.
- **A derived default is never persisted.** With no explicit choice the answer comes from `Accept-Language` (or `?deviceLanguage`, which wins), and reading does not write. Storing a guess on a read would turn "we defaulted for you" into "you chose this" and would ignore a later OS language change. `es-MX` collapses to `es`, `en-AU` to `en-US`, and a quality-ordered header is walked in order so a device's second choice beats the fallback.
- **Precedence is returned, not recomputed.** Every conversation response carries `override`, `app_wide` and a `source` naming the winner. No client re-implements the rule, so no client can implement it differently. And because the app-wide setting is a *column* and an override is a *row*, "changing the default does not reset overrides" holds by construction rather than by remembering — the service comment makes exactly that argument.

**Two smaller correctnesses.** Setting a language for a thread you are not in is a `403`, because the module imports `MessagingModule` and reuses `ConversationsService.assertMember` rather than copying the check. And `language: null` is a *required* value, so an empty body is a `400` rather than a silent clear.

**What did not ship is the PRD's actual requirement**, and it is a small gap in a good piece of work. PRD §8.1 asks for translation that is *"opt-in, set per conversation or globally"*. What shipped stores a **target language** and nothing else — there is no `enabled` flag at either scope, and the proposal it replaces had one at both. The server always resolves *some* language; there is no way to say "do not auto-translate this thread". `is_explicit` is not that flag. So the opt-in half of an opt-in feature still lives only in client storage, which is the exact problem the proposal existed to solve. **The route now exists and adding a field to it is cheap; doing it after the mobile client is written against these endpoints is a contract change.** Recorded in `api-rfc.md` §5.5b.

### 2.2 `beevia-admin-api` — the Reports module, 42 → 47

Three commits, ~2,400 lines, each with its own `.spec.ts` and each adding its own Postman folder.

| Commit | Merged (UTC) | What |
|---|---|---|
| `89932f9` → `434d5e6` | **9 Sep 23:02** | The Reports screen — catalogue, async generation, run history, download |
| `b2ca0dd` → `da01324` | 10 Sep 09:17 | The admin-actions report becomes a real audit trail |
| `5654c7e` → `4f3df97` | 10 Sep 09:25 | The signups report answers verification outcomes |

Five operations: `GET /admin/reports/types`, `POST /admin/reports`, `GET /admin/reports`, `GET /admin/reports/{id}`, `GET /admin/reports/{id}/download`. Four report types — `user_signups`, `transactions`, `kyc_verifications`, `admin_activity`.

**The catalogue drives the form, and that is the best structural decision in the module.** `GET /admin/reports/types` returns each type's columns and each filter's allowed options, so the parameter screen is rendered from the response rather than hard-coded per report. It is why the two follow-up commits could each add a report type without touching the shell, and it means adding a report type is a server change with no client release.

Four contract facts, written onto the operations in `openapi.admin.yaml` rather than left to be discovered:

- **Generation is in-process, not queued.** `POST` returns immediately and the run is a detached `void this.run(...)` in the same Node process — no worker, no job table beyond the report row. The edges are handled honestly: a restart sweeps every `queued`/`generating` row to `failed` at boot with a message telling the operator to re-run, rather than leaving a spinner that never resolves. It does mean several concurrent 50,000-row reports compete with live request handling in one process.
- **Truncation is reported, not silent** — a 50,000-row cap with a `truncated` flag on the row. Worth naming because it is the **opposite** of the reconciliation caps this report has carried as risk #17 for weeks, where exceeding 500 payouts / 1,000 ledger rows produces wrong output with no signal. Same service, same author, two weeks apart. Reconciliation should adopt the newer pattern.
- **The CSV is stored and never recomputed.** `content` is a column on `admin_reports`, so a report downloaded next month is byte-for-byte today's file even if the underlying rows have moved. Correct for an audit artifact. It also means the table grows without bound — a 50,000-row CSV per run, no retention policy. Nothing to fix today; something to have decided before anyone schedules a monthly export.
- **`409 report_not_ready` covers two opposite situations** — still generating (retry) and failed (regenerate) — distinguished only by the message text. That is the second operation in this service to overload a `409` that way, after `409 admin_not_invited` two days ago. Clients should branch on the report's `status`, not on the error code.

**And one access-control gap, which is the finding of this cycle** — see §4.5.

### 2.3 `beevia-db-schema` — v0.0.30

`a9d30be` adds `users.translation_language` and `conversation_translation_preferences`, released as **v0.0.30**. Three releases in three days (v0.0.28, v0.0.29, v0.0.30), each landing before the service that consumes it, which is the right order and has been consistent for a week.

### 2.4 `beevia-admin` — nothing, for the second day

`main` is unchanged since `a33b34c` on 8 September. No branches. **Three of Promise Udo's four board items were marked Done in this window and none of them has any code** (§5.1). The `reports` and `pending-transfers` modules remain `MOCK IMPLEMENTATION`; the client is still at **8 of 10** feature modules on the live API, unchanged.

The `wallet` module still derives a balance from the last transaction row's `balance_after`, with a comment asking for `/admin/wallets/{userId}` — which shipped four days ago. Second edition asking; still a five-minute change.

### 2.5 `beevia-mobile` — nothing, for the fifteenth day

`main` unchanged since 26 August. `origin/BVA-I192` still **14 commits ahead**, with no new commits since 7 September — three days without movement, under a board item that §0.1 now shows was closed by the sprint-close sweep rather than by anyone accepting it. Sprint 0901's four In-progress mobile items have produced no commits on any branch.

### 2.6 Repository integrity — re-verified, still clean

Every `eslint.config.mjs` blob reachable from every remote ref in all five repositories is one of the three known-good files (`09fc5b23`, 1485 B · `4e9f8271`, 899 B · `beevia-admin`'s own 501 B config). The 9167-byte payload is reachable from nothing. `beevia-admin-api` is now down to `main` alone — `feat/admin-reports` was deleted after merging, which is the right hygiene.

Unchanged and still invisible from here: the workstation, credential rotation, and branch protection.

---

## 3. Where the sprint actually stands, at day 8 of 20

Worth stating plainly because the status counts do not show it.

| Workstream | Board | Code |
|---|---|---|
| Notifications (7 items) | All in REVIEW/QA | **Merged in July/August.** Nothing this sprint (§1.3) |
| Translation — language preference (2 items) | In REVIEW/QA | **Merged today**, matches the items (§2.1) |
| Translation — backend text bundles (1 item) | In progress, unblocked today | No code yet |
| Translation — mobile engine + UI (7 items) | 2 To do, 4 In progress, 1 design | **No code, 15 days, no branch** |

**Twelve days remain, and the entire remaining scope is mobile.** The backend half of this sprint is now either merged or one item from it. The client half has not started: `BVA-I229`, the on-device engine everything else depends on, is To do on day 8, and the developer who owns it has no commits on any branch in three days.

---

## 4. Spec updates made this cycle

### 4.1 `openapi.yaml` — 131 → 137

Six operations added, documented from the controller, DTOs, service and types read at `origin/main`. New shared parameters `ConversationIdPath`, `AcceptLanguageHeader`, `DeviceLanguageQuery`; new response `ConversationLanguageOk`; eight new schemas grouped under a `Translation language preferences` banner (`TranslationLanguage`, `SupportedLanguage`, `SupportedLanguages`, `LanguageSource`, `AppWideLanguage`, `ConversationLanguage`, `SetAppWideLanguageRequest`, `SetConversationLanguageRequest`).

Response keys are documented **snake_case** — `is_explicit`, `conversation_id`, `app_wide` — because `ResponseInterceptor` converts every key recursively before it leaves the service. Same trap as the admin activity feed on 2 September and the chats module on 9 September: reading a controller tells you what a handler returns, not what a client receives.

### 4.2 `openapi.proposed.yaml` — 42 → 38

**Four proposed operations shipped**, and none of them shipped at the path proposed:

| Was proposed | Shipped as | Difference recorded |
|---|---|---|
| `GET /translate/languages` | same path | An **object** `{ languages: [...] }`, not a bare array; `value`/`label`, not `code`/`name`/`supports_detection`; a **product** list of five hardcoded values, not "the provider's supported set" |
| `GET`/`PATCH /users/me/translation` | `GET`/`PUT /translate/preferences` | **No `enabled` flag** — see below |
| `PATCH /conversations/{id}/translation` | `GET`/`PUT`/`DELETE /translate/preferences/conversations/{id}` | Own table rather than a column on `conversation_participants`; explicit clear |

All four are replaced by `NOTE` blocks in the house style, recording **what did not ship** rather than deleting the history — following the wallets and moderation-queue precedent. The load-bearing one: *the proposal carried an `enabled` boolean at both scopes and the shipped surface has none*, so the PRD's "opt-in" requirement is unmet by code that otherwise implements the feature well. Four orphaned components (`TranslationPrefOk`, `TranslationPreference`, `UpdateTranslationPrefRequest`, `UpdateConversationTranslationRequest`) and the now-unused `ConversationId` parameter and `Language` schema were removed with them.

`POST /translate/batch` is the only survivor of §7.7, and it is probably obsolete for the on-device design.

### 4.3 `openapi.admin.yaml` — 42 → 47

The five Reports operations, with a new `Reports` tag whose description opens by saying what a report *is not* — *"an exported dataset, not a user complaint; the moderation queue is under `Chats`"* — because that ambiguity has now cost this project a path collision and a schema collision in two days.

Twelve new schemas (`ReportType`, `ReportStatus`, `ReportColumn`, `ReportFilterDef`, `ReportTypeDef`, `ReportBreakdown`, `ReportPreview`, `ReportSummary`, `ReportDetail`, `GenerateReportRequest`) and four parameters. `PaginationMeta` is reused: the reports history returns the *majority* pagination convention rather than adding a fourth.

The four contract facts from §2.2 are written onto the operations, and `GET /admin/reports/{id}` carries the access-control caveat from §4.5 in its description rather than only in the RFC.

### 4.4 `openapi.admin.proposed.yaml` — 19 → 19, and the collision is resolved

`feat/admin-reports` merged, so the reasoning that kept Module 4's proposal at its original path yesterday — *"renaming on the strength of an unmerged branch would be guessing"* — no longer applies. The two workflow operations move:

```
/admin/reports/{reportId}          ->  /admin/chats/reports/{reportId}
/admin/reports/{reportId}/resolve  ->  /admin/chats/reports/{reportId}/resolve
```

Their schemas move with them — `Report` → `ChatReport`, `ReportDetail` → `ChatReportDetail`, `ResolveReportRequest` → `ResolveChatReportRequest`, `ReportId` → `ChatReportId`. **That second rename was not optional**: the audit caught `ReportDetail` as a cross-file schema divergence, which is the same collision reproducing itself one level down. A path collision between two meanings of a word will collide again in every namespace that word touches — now generalised in `suggestions.md` §5.6.

Nothing else changed, so the proposed total is unmoved at 19.

### 4.5 The finding: a generated report outlives the permissions it was generated under

`ReportsService.generate` does the careful thing. It resolves the requesting admin's `viewableModules` **at request time**, with a comment explaining why — *"the report must reflect what the admin who asked for it was allowed to see, even if their role changes mid-run"*.

That scoping is then **never re-applied at read**. `GET /admin/reports/{id}` and `/download` are gated by `reports:view` and `reports:export` and nothing else. Neither checks who requested the report. So an admin whose role sees one module can open, preview and download an `admin_activity` report generated by an admin who sees all of them, and read rows their own role would have excluded.

Three properties make it worth fixing this week rather than later:

- **The artifact is durable.** The CSV is stored on the row, so it keeps the wider scope permanently — narrowing the generating admin's role afterwards does not narrow the file.
- **It is discoverable, not merely reachable.** The run history is team-wide by default (`mine=false`) and lists every report with its requester's name, so a narrower admin does not have to guess an id.
- **It is generic.** Any future report type inherits it, and the module is explicitly designed for types to be added server-side without a client release.

Two fixes, either sufficient: persist the generating admin's `viewableModules` on the row and re-filter the preview and CSV on read; or scope reads to reports whose requester's permissions are a subset of the reader's. The first is more honest about what a stored export is.

The general shape is worth naming because it will recur: **authorisation applied when an artifact is produced is not authorisation applied when it is read.** Every export, cache, snapshot and emailed attachment in this system has that structure. Recorded as `suggestions.md` §4.7 and `admin-api-rfc.md` §6.3.

### 4.6 Narrative documents

- **`api-rfc.md`** — §3 inventory: Translate 1 → **7** implemented, 5 → **1** proposed; totals **131 → 137** and **39 → 35** net-new. §6.8 gains six rows with their traps. §7.7 rewritten as "four of five shipped, and where". New **§5.5b** on what the preference surface does well and the missing `enabled` flag. §7 heading and the companion-artifact counts corrected — they had been stale at "100 operations / 52 operations" since August.
- **`admin-api-rfc.md`** — counts **42 → 47**, eleven → twelve controllers; §1 notes a seventh module opening; Module 7 coverage 2 → **7 ops**. New **§3.14 Reports**. **§5.4b rewritten** from a prediction into a record of the collision and its resolution, including why the rename waited a day and what that cost. **§6.3 grows to six gaps**, with the new access-control gap displacing Module 4's workflow as the one to act on first.
- **`suggestions.md`** — **§5.6 rewritten** around the timing lesson (daily cadence vs merge cadence) and the schema-namespace recurrence; new **§4.7** on the report access-control gap; §8's order re-numbered with §4.7 at position 4.

### 4.7 Spec health

All four files parse. **137 / 38 / 47 / 19** operations. No `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s.

**Drift against `origin/main`: zero, both services, both directions** — `beevia-api` 137 = 137, `beevia-admin-api` 47 = 47.

The audit script run against the *working tree* reports 19 phantom "documented, not in code" lines, because three repositories are still `diverged` and their working trees are 4 September code (§7). Fourth consecutive edition flagging this, and the number has grown from 8 to 19 — so that nobody "fixes" the spec by deleting nineteen real operations.

---

## 5. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 8.** 12 items — **8 leaves, 4 parent Stories**.

| Status | Leaves | 9 Sep | Δ |
|---|---:|---:|---:|
| To do | 2 | 4 | −2 |
| In progress | **0** | 2 | −2 |
| Done | **6** | 2 | **+4** |

| Owner | Leaves | To do | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 | **3** |
| Ayomikun Araoye | 3 | 1 | 2 |
| Unassigned | 1 | 0 | **1** |

Nine transitions in this window, in two clusters that both follow a merge:

| Time (UTC) | Items | Transition | Preceded by |
|---|---|---|---|
| 09:05:10 | `BVA-I4`, `BVA-I5`, `BVA-I6` | In progress → **Done** | `434d5e6`, the Reports module (9 Sep 23:02) |
| 09:11:17 | `BVA-I13`, `BVA-I14`, `BVA-I15` | To do → In progress | — |
| 10:24:42 | `BVA-I13`, `BVA-I14`, `BVA-I15` | In progress → **Done** | `da01324`, the audit-trail report (09:17) |

`BVA-I13`'s story went To do → In progress → Done in **73 minutes**, bracketing the merge of the code it describes. That is the board being kept honest in real time, and it is the tightest board-to-code correspondence anywhere in this project.

### 5.1 Three items are Done for client code that does not exist

The board's stories each split into a backend "Report Data Query" (Ayomikun) and a frontend "Report Content Display" (Promise). Checked against `origin/main`:

| Item | Owner | Half | Done? | Code |
|---|---|---|---|---|
| `BVA-I5` | Ayomikun | backend | ✅ | **Merged** — `434d5e6` |
| `BVA-I11` | Ayomikun | backend | ✅ | **Merged** — was Done yesterday for unmerged code; the code caught up |
| `BVA-I14` | *Unassigned* | backend | ✅ | **Merged** — `da01324` |
| `BVA-I6` | Promise | frontend | ✅ | **None.** `beevia-admin/src/features/reports/api.ts` opens `MOCK IMPLEMENTATION — no network calls` |
| `BVA-I12` | Promise | frontend | ✅ | **None.** Same file |
| `BVA-I15` | Promise | frontend | ✅ | **None.** Same file |

`beevia-admin/src/features/reports/` was last touched by `a537f40` on **1 September** — before the backend existed — and `beevia-admin` has had **no commits at all since 8 September**.

**Two of yesterday's three "Done ahead of the code" items resolved themselves within a day**, which is a real improvement and the reason to raise this as a definition question rather than a defect: `BVA-I11`'s backend merged. But the frontend side moved the other way — from one Done-without-code item to three.

**And Promise did not mark any of them Done.** All 22 transitions this board has ever recorded were made by Ayomikun Araoye, including every transition on all four of Promise's items. So the state of his row is being maintained by someone else, and the question "does Done mean my half is written" cannot be answered by the person whose half it is.

That is a process observation, not a personal one, and it has a cheap fix: **agree what Done means on this board while it is eight days old.** If it means "the backend is merged and the frontend is unblocked", the board is accurate and simply means something different from the main board's Done — which is fine, if written down. If it means "merged", three items are ahead of themselves and the sprint looks 75% complete on day 8 when the client work has not started.

### 5.2 The board is the Reports module, and it is nearly finished — on one side

Two of four stories fully Done, one To do (`BVA-I7` User & KYC Report), one Done. **The `user_signups` report type it describes actually merged this morning** as `4f3df97`, so `BVA-I8`'s backend half is arguably done too and the board has not caught up — the opposite error from §5.1, and a smaller one.

`BVA-I14` remains **Unassigned** and is now Unassigned *and Done*. On this board `Unassigned` is a real gap rather than the parent-story artifact it is on the main board, and an unowned item reaching Done means nobody is on record as having done it.

### 5.3 Never summed with the main board

12 items here and 25 on sprint 0901 are different projects and different backlogs; one person appears on both. A combined figure would be meaningless. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards.

---

## 6. Team performance — detail

All figures come from the activity sidecars and git, never from `Last Modified`. Commit counts are trailing-7-day, merged to the default branch except where stated, summing each person's git identities and excluding bots. **This section's method changed this edition** — see §6.4.

**Ayomikun Araoye — backend + admin API.** **30 commits** across `beevia-admin-api` (19), `beevia-api` (8) and `beevia-db-schema` (3), summing `Ayomikun Araoye`, `Phoenixdadhev` and `phoenixdahdev`; includes merge commits. Up from 22, and the increase is entirely feature work: eleven merged endpoints across two services in one day, a schema release, four report types, and every commit shipping with tests. One submission in the trailing 7 days on the corrected count (§6.4) — `BVA-I231`, 69 minutes after its own merge. Median cycle 3.0 d over 12 passes. One open WIP, `BVA-I245`, 0.2 days old. He also made **all 22 transitions the admin board has ever recorded**, four of them on items he does not own (§5.1); that is board maintenance rather than delivery and should not be read as either.

**David Samuel — mobile.** **Zero submissions in the trailing 7 days** — his last was `BVA-I182` on 3 September, now 7.2 days ago and outside the window. Median cycle 2.6 d over 14 passes. **Zero commits to `main` and zero new commits on `origin/BVA-I192`**, which stands at 14 commits unchanged since 7 September — three days. He holds four 0901 leaves In progress: `BVA-I233` and `BVA-I241` at **5.9 days against a 2.6-day median**, plus `BVA-I243` (2.1 d) and `BVA-I236` (1.9 d). `beevia-mobile` `main` is **15 days** without a commit.

This is the second consecutive edition raising it and the signals have all moved the wrong way: WIP ages up from 4.9 to 5.9 days, submissions from 1 to 0, days since the branch moved from 1 to 3. **Section 3 makes the consequence concrete** — twelve days remain in the sprint and every remaining item is his or Philip's.

**Philip Chidera — design.** No submissions in the window; his last was **28 August, 13 days ago**. Median cycle 0.9 d over 7 passes. Two leaves In progress: `BVA-I240` at **5.9 days against a 0.9-day median — 6.6× his own pace**, the most overdue WIP relative to its owner on any of the three boards, and `BVA-I235` at 1.9 days. He made no transitions in this window, which breaks the two-week pattern of short board-maintenance bursts.

**Promise Udo — admin dashboard.** **4 commits** in the trailing window, **none since 8 September**. He holds four leaves on `0901-admin`, three of them now Done, and none of the three has any client code (§5.1) — the reports module is still the mock file it was on 1 September. He also made **no board transitions at all**; his items were moved by someone else. The workstream's characteristic through last week was the shortest endpoint-to-client latency in the project — five admin endpoints shipped yesterday and this morning and none of them has been consumed, so that characteristic did not hold this window.

### 6.1 Weekly submission trend

Genuine submissions into REVIEW/QA by leaf items, counting **each pass** (an item sent back and resubmitted counts twice), across the main board and 0901:

| ISO week | Passes | Distinct items |
|---|---:|---:|
| W33 (11–17 Aug) | 1 | 1 |
| W34 (17–23 Aug) | 17 | 17 |
| W35 (24–30 Aug) | 31 | 19 |
| W36 (31 Aug – 6 Sep) | 3 | 3 |
| W37 (7–10 Sep) | **8** | 8 |

W37's eight are yesterday's seven notification items — a board reconciliation, not delivery (§1.3) — plus `BVA-I231`, which is delivery.

### 6.2 Cycle times

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

Unchanged. `BVA-I231` produced no measurement: it went To do → REVIEW/QA without passing through `In progress`, so there is no elapsed working duration to measure — the same shape as yesterday's seven, for a different reason.

### 6.3 Completion, put back on the record

Restating §0.1 as a table, because it is the figure the last two editions have been carrying wrongly:

| When | Completions | From | Character |
|---|---:|---|---|
| 12–31 Aug, over 6 days | 20 (12 leaves) | **Never REVIEW/QA** | Owners closing their own items, bypassing the queue |
| **3 Sep, one 47-second action** | **46** (30 leaves) | **REVIEW/QA, all 46** | Sprint close, by a non-contributor |
| Since 3 Sep, on 0901 | **0** | — | — |
| On `0901-admin` | **9** (6 leaves) | In progress / To do | By one person, on 2 days, four of them on someone else's items |

The 0901 zero is not alarming at day 8 with the oldest queue item at 1.9 days. **The 46 is the number to look at**, and §0.1 is the reason.

### 6.4 A method note, stated because it makes the check easy to get wrong

This edition's status-transition extraction matches three Zoho audit actions — `Updated the status`, **`Item Completed`** and **`Item Reopened`**. Keying only on the word "status" — the obvious way to write it — sees 176 transitions on the main board and drops 66 completions silently. Two consequences for reading this edition against earlier ones:

- **Ayomikun's cycle-time sample is 12 passes at a 3.0 d median.** Counting only `Updated the status` gives 11 passes and 3.9 d, because a pass that ended in a completion disappears. Yesterday's edition printed 3.0 d and 12, so the two agree; this is recorded so the difference is not mistaken for movement if a future edition prints 3.9.
- **W33 appears in the trend table** with one pass.

Note that the deterministic audit's `delta` block reports "0 left review" from a same-shape comparison and should not be read as "nothing was ever completed" — it is comparing two consecutive exports, and no completion happened between them.

### 6.5 What these figures do not measure

- **They cannot distinguish delivery from reconciliation.** Seven of W37's eight submissions describe code merged in July and August (§1.3). No board metric separates those; only reading the code does.
- **They say nothing about whether a completion was reviewed.** All 46 of 3 September's came from REVIEW/QA and none of them was reviewed; all 20 before it were reviewed by nobody because they skipped the queue. The transition records the column, not the judgement (§0.1).
- **They do not see branches.** David reads zero commits while fourteen sit on `origin/BVA-I192`. Every "commits" figure means *merged to the default branch*.
- **They count merge commits.** Ayomikun's 30 includes merges, which inflates a busy integration week relative to a busy authoring one.
- **They do not measure whether "Done" means merged.** Three items are Done on the admin board for a mock file (§5.1).
- **No estimation points exist on any item, on any of the three boards** — 0/64, 0/25, 0/12. Nothing is normalised for size.
- **Board actions are not evenly attributable.** Figures key to the item's assignee, not to whoever clicked. On the admin board *one person made every transition*; on the main board the pattern appeared yesterday.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction. Noted anyway because the trend held again: all three Reports commits and the translation commit shipped with `.spec.ts` files.

---

## 7. Risks

1. **A generated report can be read by an admin whose role could not have generated it** (§4.5). New, in code that shipped in the last 24 hours, and cheapest to fix before any report worth reading exists.
2. **Eight items sit in REVIEW/QA and the project's only precedent for emptying that column is a 47-second bulk close** (§0.1). Sprint 0901 ends 22 September.
3. **Seven of those eight describe code merged in July and August** (§1.3), so accepting them would record a sprint's delivery that no sprint-0901 commit supports.
4. **The entire remaining scope of sprint 0901 is mobile, and mobile has not started** (§3). `BVA-I229` is To do on day 8 of 20.
5. **`beevia-mobile` `main` is 15 days stale**; the 14-commit branch has not moved in 3 days; two WIP items sit at 2.3× their owner's median. Second edition asking.
6. **Three admin-board items are Done for client code that does not exist**, and were marked Done by someone who does not own them (§5.1).
7. **Translation shipped without its opt-in flag** (§2.1). PRD §8.1 requires opt-in; the stored preference is a language only. Cheap now, a contract change once the client is written.
8. **`POST /translate` still returns its input unchanged**, and the new `GET /translate/languages` does not constrain its `to` field — the two halves of the surface disagree about what a language is.
9. **Accepting `BVA-I246` may accept a stub.** `FCM_SERVICE_ACCOUNT` is optional and blank in `.env.example`.
10. **Report CSVs are stored in Postgres with no retention policy** — up to 50,000 rows per run, forever (§2.2).
11. **Report generation is in-process and unbounded in concurrency** — several large runs compete with live request handling in one Node process (§2.2).
12. **Three repositories remain unsynced locally**, so the deterministic audit reads 4 September code and now reports **19** phantom drift lines, up from 8. Fourth edition.
13. **The infected workstation's status is unknown.** Repositories verified clean again today (§2.6); the workstation is not observable from here.
14. **Credential rotation cannot be verified from here**, and it is the step that decays fastest.
15. **Branch protection cannot be verified from here** — the available GitHub token has no org access. Fifth edition recommending a control with no instrument behind it.
16. **Module 4 shipped as a queue with no way to work it off** — no status, no resolve, no reported-user history.
17. **The product decision behind Module 4 is recorded nowhere but a controller docstring.**
18. **The per-user reconciliation check will report false discrepancies for every user the moment the treasury pool is enabled** — `ANCHOR_POOL_ACCOUNT_ID` is still unset.
19. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows — and the Reports module now demonstrates the correct pattern in the same service (§2.2).
20. **`treasury.solvent` is on the live landing screen and reads `false` for "unknown".**
21. **The money-oversight surface still has no second reviewer** — PRs #1–#10 self-merged.
22. **The Anchor webhook backfill is still unscoped** — 67 days of dropped events, unmeasured, nine days after the fix.
23. **The daily export still targets a closed sprint**, fifth consecutive edition, now costing a scratch export every run.
24. **The 14:00 UTC cut-off did not bite today, by luck of the working session** (§0.3). Fourth edition recommending the change.
25. **No estimation points on any of three boards** — seventh edition asking.
26. **The same silent-200 is still live on `POST /kyc/profile`** — eighth consecutive edition.
27. **A hard-coded account number still reaches a money screen on `main`** — eighth consecutive edition.
28. **The admin client's `wallet` module ignores the wallets endpoint** built for it — second edition.
29. **This service now has three pagination conventions across seven endpoints** — though the Reports history correctly uses the majority one.

---

## 8. Previous recommendations — where they stand

| Recommendation from 9 Sep | Status on 10 Sep |
|---|---|
| Answer the notification question before the seven are accepted; check `FCM_SERVICE_ACCOUNT` first | ❌ **Not done.** The seven are unmoved at 1.9 days; `FCM_SERVICE_ACCOUNT` still blank in `.env.example` |
| Review something — the queue is now the constraint | ⚠️ **Nothing reviewed**, and §0.1 reframes this: the queue is not frozen, it is emptied at sprint close. Recommendation restated more precisely below |
| Decide `/admin/reports` before `feat/admin-reports` merges | ⚠️ **Overtaken.** The branch merged 7 hours later (§0.2). Resolved today by rename (§4.4) |
| Write down that Option A is the answer to Module 4 | ❌ **No decision recorded.** The dashboard spec still says "reported messages" |
| Unblock `BVA-I245`, or record why it is blocked | ✅ **Unblocked** by the commit it was waiting for (§1.2). The *reason* is still not recorded — `Blocked by` was empty throughout |
| Ask David what is happening | ❌ **Not visible from here**, and every signal moved the wrong way (§6) |
| Fix the definition of Done on the admin board | ❌ **Not done, and it got worse** — from 2 Done-without-code items to 3 (§5.1) |
| Point the `wallet` module at `GET /admin/wallets/users/{userId}` | ❌ **Not done.** `beevia-admin` had no commits in this window |
| Move the daily export to sprint 0901 and add the admin board | ⚠️ **Half.** The admin board is now exported every run with `--sprint 0901-admin`; the main export still targets the closed 08-01 |
| Move the report cut-off to ~20:00 UTC | ❌ **Not done.** Cost nothing today by luck (§0.3) |
| Put estimation points on all three boards | ❌ **Not done.** 0/25, 0/12 |
| Apply the BVN-ordering guard to `POST /kyc/profile` | ❌ **Not done.** Re-checked at `origin/main`; unchanged |

**One of twelve fully actioned, and it was actioned by a commit rather than by a decision.** The pattern of the last three editions holds and sharpens: **things that are code get done; things that are decisions do not.** Eleven endpoints merged in a day, while "write down which of two options we chose", "agree what Done means" and "put numbers on the board" have between them been asked twenty times across editions and done zero times.

---

## 9. What I would do this week

1. **Scope the eight items in REVIEW/QA before 22 September, not on it** (§0.1, §1.3). This project has closed a sprint by marking 46 queued items Done in 47 seconds. Seven of today's eight describe July code. If that is fine, say so on the board now — the sprint's real remaining scope becomes visible and the burn-down stops lying. If it is not, the eight need a reviewer named this week.
2. **Fix the report read-scoping** (§4.5). Persist the generating admin's `viewableModules` on the row and re-filter on read. It is a day-old defect in a module nobody has used yet, which is the cheapest a defect ever gets.
3. **Ask David what is happening — this is the second time.** Zero submissions in 7 days, zero commits on any branch in 3 days, `main` 15 days stale, two items at 2.3× his median, and `BVA-I229` still To do. **§3 is the reason it cannot wait**: twelve days remain and every remaining sprint item is client-side.
4. **Add the `enabled` flag to the translation preference** (§2.1). PRD §8.1 asks for opt-in; the shipped surface stores a language only. One column, one field on two responses, while nothing consumes the endpoints. After the mobile client is written against them it is a contract change.
5. **Agree what Done means on the admin board** (§5.1). Third-ranked yesterday, and it moved from two wrong items to three. Eight days old, twelve items, five minutes of conversation.
6. **Have Promise move his own board items**, or say explicitly that Ayomikun maintains that board. All 22 transitions on `0901-admin` were made by one person, four of them on another person's items — which makes the board unreadable as a signal of who is doing what.
7. **Wire the admin client to the five endpoints waiting for it.** `reports` and `pending-transfers` are still mocks, and the entire Reports backend now exists. The `wallet` module's own comment still asks for an endpoint that shipped four days ago.
8. **Write down that Option A is the answer to Module 4.** Fifth edition asking. It is built, merged, shipped, and recorded in a controller docstring.
9. **Adopt the Reports module's truncation pattern in reconciliation** (§2.2, risk #19). The same service demonstrates the right answer — a row cap with a `truncated` flag — two weeks after shipping the wrong one. It is a ten-line change and it converts silently-wrong output into visibly-partial output.
10. **Add the route-collision check to CI, on push** (`suggestions.md` §5.6). The audit already extracts routes and parses all four specs. §0.2 is the argument: the daily pass found this collision and was still seven hours too slow.
11. **Move the daily export to sprint 0901 and the cut-off to ~20:00 UTC.** Fifth and fourth editions. The admin board half was done this week, so the pattern is established; the main export is the same change.
12. **Put estimation points on all three boards, or state that this project does not estimate.** Seventh edition.
13. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Eighth edition; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:03 UTC) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync (**0 repos synced; 3 refused as `diverged`, 2 already current**) → deterministic audit against the working tree → **a second audit run against a read-only `origin/main` shadow workspace** built with `git archive` into `/tmp` → static contract review of the eleven new operations read at `origin/main` → spec, RFC and suggestions updates → re-audit of the shadow to zero drift → repository-wide integrity sweep by blob hash across every remote ref → read-only scratch export of sprint 0901 → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran. The unsynced repositories were read with `git show`, `git log`, `git cat-file` and `git archive` into `/tmp`, outside the workspace. No repository was reset, rebased, reverted or cleaned, no file in any sub-repo was edited, and the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Degraded inputs.**

- **Three repositories could not be synced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` remain `diverged` because `origin/main` was rewritten during the 8 September remediation; `sync_repos.py` is `--ff-only` and correctly refuses. Their working trees are 4 September code, which is the sole cause of the audit's **19** phantom drift lines — up from 8, because eleven more operations shipped. Resolving it needs `git reset --hard origin/main` or equivalent, which is outside this pipeline's sanctioned exception and is a decision for whoever owns those clones. The evidence says it is safe: `origin/main` is verifiably clean (§2.6). **Capture the local tips first** (`d9af17b`, `43abc3a`, `5b0592a`) — they are the only offline copy of the pre-incident history. Every code claim in this report was made against `origin/main`.
- **The `Epic` column is blank** on both boards — the OAuth refresh token lacks `ZohoSprints.epic.READ`. A known scope gap, not "no epic assigned"; the audit trail shows epics *are* set.
- **`Comments` bodies are unavailable** from the API.
- **`ZOHO_SPRINT_FILTER` is stale** — still `08-01`, so the in-repo main export covers a sprint that closed on 28 August. Sprint 0901 is exported to `/tmp/beevia-scratch/` for the sixth consecutive edition, because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest as snapshots of one board.
- **Branch protection, credential rotation and workstation remediation are unverifiable** from this workspace.
- **No estimation points on any item, on any of three boards**, so velocity is not derivable and no per-person figure is normalised for size.
- **The admin board is 8 days old.** Six Done and zero In-progress items are too few to support a trend; §5 reports state, not throughput, and no cycle time is computed from it.
- **Completion is only visible if the extraction matches `Item Completed`** as well as `Updated the status` (§6.4). Stated so a future edition does not reinstate the claim §0.1 corrects for a third time.

**Window.** 9 Sep 14:03 UTC → 10 Sep 14:03 UTC. All `actiontime` values and board times are UTC; the local export host runs UTC−6, so the 08:03 local run is a 14:03 UTC cut-off. Every event in this window — five merges between 08:49 and 09:25 UTC and nine board transitions between 09:05 and 10:25 UTC — landed inside it, unlike yesterday (§0.3).

**Sources.** Boards: `beevia-sprint-board-2026-09-10.csv` (64 rows, 41 leaves, sprint 08-01) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-10.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (25 rows, 17 leaves) + activity sidecar. Code: all five repositories at `origin/main`; `beevia-admin` and `beevia-mobile` in the working tree, the other three extracted to a `/tmp` shadow. Specs: `openapi.yaml` (**137**), `openapi.proposed.yaml` (**38**), `openapi.admin.yaml` (**47**), `openapi.admin.proposed.yaml` (19) — all validated, no markers, no broken refs, no orphaned components, zero drift against `origin/main`.

**A note on who appears here.** Only people whose work is tracked have rows. Board transitions performed by non-contributors are reported without attribution, per the standing instruction; the 46 completions of 3 September (§0.1) fall into that category and are reported as an event rather than as an action by a named person.

<a id="mvp-method"></a>

### MVP readiness — ≈58% (estimate; 57.92, from 56.75)

**Target 2026-09-01 (provisional) · the target date passed nine days ago.** On merged build evidence the product is roughly 58% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Unchanged. Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. This window's `beevia-api` commit was the translate module, not messaging |
| 2 | Voice & video calling | 8 | 0.8 | Unchanged. 4 call endpoints live; `audio_call_screen` / `video_call_screen` present; incoming-call push wired — though the push transport falls back to a stub without `FCM_SERVICE_ACCOUNT` |
| 3 | Message translation | 7 | **0.30** ↑ | **+0.15, on merged code.** Six operations shipped (`a08bf13`) with a schema release (`v0.0.30`): the supported-language list, app-wide preference, per-conversation overrides, and precedence returned rather than recomputed. Real DB storage, a membership guard reusing `ConversationsService.assertMember`, and device-language fallback that does not persist itself. **Ceiling, and it is still most of the capability:** `TRANSLATE_PORT` is *still* bound unconditionally to `StubTranslateAdapter`; the PRD's opt-in flag did not ship (§2.1); and the client has **zero** code — `beevia-mobile` `main` 15 days stale, `BVA-I229` To do, no branch carries translation work. Language *selection* is built; language *translation* is not |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged; no consumer-API commit touching wallets. Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` unset), so not scored. Ceiling unchanged: server is NGN-only, `PaymentService.activeNgn()` present at three call sites |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. Ceiling: request/receive still have no client flow; the mobile money UI is still mock routes |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. Ceiling still low: the client has **zero** `/cards` references and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | No endpoint or record anywhere. The translation preference that shipped today is explicitly *not* consent-gated, because there is nothing to gate it with |
| 11 | Admin oversight | 6 | **0.87** ↑ | **+0.02 — deliberately much smaller than yesterday's +0.07.** Admin API 42 → **47**: the Reports module deepens Module 7 rather than opening a new one, so **modules with something built stays at 6 of 8**, and the client is unchanged at **8 of 10** — the five new endpoints have no consumer. Against the gain: a new access-control gap in the same code (§4.5). Ceiling unchanged and still real: `reports` and `pending-transfers` mock-only, Modules 6 and 8 with no endpoints, Module 4 a queue with no status/resolve/history, no per-wallet partner-balance comparison, no 2FA |
| | **Weighted total** | **100** | | **57.92 → ≈58%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, never merged-but-disabled code, and never a design decision on its own.

Three of this edition's prominent events are worth **zero points by design**: the eight items in REVIEW/QA (seven describe already-scored July code; the eighth is scored as merged code, not as a board state), the admin board's four new Done items (three have no code at all), and the 46 completions uncovered in §0.1 — board status has never contributed to this number.

### What this report cannot tell you

- **Whether the eight items in REVIEW/QA will be reviewed or swept.** §0.1 establishes the precedent; nothing establishes the intent.
- **Whether the seven notification items are being reviewed as new work or acknowledged as old.** The code's history is unambiguous; the intent behind the board move is recorded nowhere.
- **Whether `FCM_SERVICE_ACCOUNT` is set in any deployed environment.** The fallback is silent by design.
- **Why `BVA-I245` was blocked.** Both blocking columns were empty throughout; the dependency is confirmed by behaviour, not by record.
- **Whether metadata-only moderation is the accepted answer to Module 4.** Built, merged and shipped that way; nothing records the decision.
- **Whether the server-side `/translate` surface is being retired**, and whether the missing opt-in flag is an omission or a decision.
- **Whether any of the eleven new endpoints work.** All ship with unit tests, which continues a good trend; there are no HTTP-level tests and no second reviewer. Testing is out of scope for scoring per the owner's 2026-08-07 instruction.
- **Whether the infected workstation has been cleaned, or whether credentials were rotated.** Invisible from a git clone.
- **Whether branch protection is enabled.** The available GitHub token cannot see the org.
- **What the 67 days of dropped Anchor events cost.** Still unmeasured, nine days after the fix.
- **Why `BVA-I192` has not merged**, fourteen commits deep and three days without movement — though §0.1 now explains how its board item became Done.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 25 and 0 of 12 items estimated.
