# Beevia — Project Status

**As of 2026-09-09** · Sprint **0901** (3 Sep → 22 Sep) — **day 7** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 7, first appearance** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-09.csv` + `beevia-activity-2026-09-09.json` (64 items, sprint 08-01); **`sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-09.csv` + its activity sidecar (12 items — the first admin-board export this pipeline has ever written)**; a read-only scratch export of sprint 0901 (25 items); all five repos inspected at `origin/main`.

Scope: three boards, kept separate and never summed. Window 8 Sep 14:00 UTC → 9 Sep 14:00 UTC.

---

## Quick overview

> **Three things closed today that this pipeline has been reporting as open for weeks. The malware is gone from the repositories entirely — seven infected branches deleted, the eighth merged rather than lost. The admin dashboard board exists and has items, ending a blind spot nineteen editions old. And Module 4, called "blocking, needs a product decision" since 5 August, is merged. Against that, one number needs reading carefully: seven items entered review after eleven days of silence, and all seven describe code that has been on `main` since 11 July. The board moved. The codebase did not.**

| | 8 Sep | 9 Sep | Δ |
|---|---:|---:|---:|
| Payload reachable from any remote ref, all 5 repos | 8 branches | **0** | **−8** |
| `beevia-admin-api` infected branches | 8 | **0** | **−8** |
| Sprint 0901 leaves in REVIEW/QA | 0 | **7** | **+7** |
| Sprint 0901 leaves To do | 13 | **3** | **−10** |
| Sprint 0901 leaves In progress | 4 | 6 | +2 |
| Sprint 0901 leaves BLOCKED | 0 | **1** | **+1** |
| Days since anything entered REVIEW/QA | 11 | **0** | **−11** |
| Admin board items | none | **12** (8 leaves) | **new** |
| API surface (consumer / admin) | 131 / 37 | 131 / **42** | 0 / **+5** |
| Admin spec modules with something built | 5 of 8 | **6 of 8** | **+1** |
| `beevia-admin` modules on the live API | 6 of 10 | **8 of 10** | +2 (recount, §0.3) |
| Estimation points set (0901 / 0901-admin) | 0 / 25 | **0 / 25 · 0 / 12** | 0 |
| `beevia-mobile` `main` days since a commit | 13 | **14** | +1 |
| MVP readiness (estimate) | ≈56% | **≈57%** | +0.4 pt |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 9 on 0901 · 3 on 0901-admin | **8** | 3.0 d | 1 (0.9 d) | **22** | Seven 0901 submissions in 2 minutes map to code merged in **July** (§1.3). Shipped 5 real admin endpoints |
| David Samuel | mobile | 6 on 0901 — **4 In progress** | 1 | 2.6 d | 4; ages **4.9 d ×2**, 1.1 d, 0.9 d | 0 to `main`, 0 new on `BVA-I192` | `beevia-mobile` `main` untouched **14 days**; two WIP items at ~2× his median; the 14-commit branch did not move today |
| Philip Chidera | design | 2 on 0901 — both In progress | 0 | 0.9 d | 2; ages **4.9 d**, 0.9 d | — | WIP at **5× his own median**. Started two items last night |
| Promise Udo | admin dashboard | **4 on 0901-admin** — first board row ever | — | — | 1 (0.9 d) | 4 | **Has a board row for the first time in 20 editions.** Wired the re-invite endpoint the same day it shipped |

**The two questions for standup:** (1) **The seven notification items in review — are they being reviewed as new work, or acknowledged as already-shipped work?** No commit touched `src/notifications/`, `src/devices/` or `src/messaging/` at any point in this sprint; the FCM module merged on 11 July (§1.3). Either answer is fine, but they imply completely different remaining scope. (2) **Is `feat/admin-reports` merging, and does Module 4's proposal move off `/admin/reports` before it does?** The branch and a standing proposal claim the same path for unrelated resources (§4.3).

**The three things worth knowing:**

1. **The compromise is closed, and closed properly.** Yesterday's edition listed eight `beevia-admin-api` branches still carrying the EtherHiding payload and argued for seven deletions and one rebase. That is exactly what happened: seven are gone, and `feat/admin-chats` — the only one with unique content — was brought onto the clean history rather than discarded. A full-history sweep of **every remote ref in all five repositories** now reaches only the two known-good `eslint.config.mjs` blobs. The 9167-byte payload is reachable from nothing (§0.1). What remains open is the two things no git clone can see: the workstation, and credential rotation.
2. **The admin board is live — and it was live yesterday, when this report said it was not.** The project was populated on **7 September at 14:26–15:40 UTC**, before yesterday's export ran. Yesterday's §5 restated a nineteen-edition-old claim — "no sprints and no start/end dates" — without re-reading the message the export actually printed, which lists the sprint by name. §0.2 corrects it. Promise Udo now has a real board row sourced from a board.
3. **Seven items entered review, and none of them is new code.** `BVA-I246`–`BVA-I252` — the whole notification half of sprint 0901 — went To do → REVIEW/QA in 118 seconds on 8 September, skipping `In progress` entirely. Every one maps to a file already on `beevia-api` `main`: the FCM adapter dates to **11 July**, the triggers to August, and **no commit has touched that code at any point in this sprint**. Reconciling a board against a codebase is worth doing, and catching it on day 6 beats catching it on day 20. The caution is only about how the number reads: as throughput it says the team's output went from zero to seven overnight, which is not what happened (§1.3).

**If you read nothing else:** the security incident is over on the remote and the last two steps belong to people, not repositories; the admin dashboard finally has a board and this pipeline was a day late noticing; Module 4 shipped, correctly, and its unshipped half is now the gap that matters (§4.2); and sprint 0901's headline throughput number is a board-reconciliation artifact rather than delivery, which is worth saying out loud before it is quoted at anyone.

---

## 0. Corrections and closures

### 0.1 The malware is gone — repository-wide, verified by content hash

Yesterday's §0.3 listed eight `beevia-admin-api` remote branches carrying `eslint.config.mjs` at 9167 bytes, and recommended seven deletions plus one rebase. Today:

| Check | Result |
|---|---|
| `beevia-admin-api` remote branches | `main` and **one new branch** (`feat/admin-reports`). All seven infected branches are gone |
| `feat/admin-chats` | **Merged to `main`** as `6b105d8`, not deleted — the module survived (§2.1) |
| Every `eslint.config.mjs` blob reachable from **every** remote ref, all 5 repos | `09fc5b23` (1485 B) and `4e9f8271` (899 B) only. **The 9167-byte payload is reachable from nothing** |
| `feat/admin-reports` (the new branch) | `09fc5b23`, 1485 B — clean |
| `beevia-admin`, `beevia-mobile` | Unaffected throughout; `beevia-admin`'s own config is a different 501 B file |

The sweep enumerated every commit reachable from every `refs/remotes/origin/*` ref and hashed every `eslint.config.mjs` blob in each, rather than checking branch tips — a tip can be clean while history is not. `suggestions.md` §7.6 is updated from an open finding to a closed one, with the general lesson kept.

**Two things are still open and neither is visible from here.** Whether the workstation that authored the poisoned commit has been imaged and cleaned, and whether credentials were rotated. Both were open yesterday; nothing observable has changed. Branch protection (§0.5 yesterday) likewise remains unverifiable — the GitHub credential in this environment has no access to the `Drumbell-Technologies` organisation, so "not found" carries no information.

### 0.2 Correction — the admin board was live yesterday, and this report said it was not

**Claim (2026-09-08 §5, and in eighteen editions before it): "The Beevia Admin Dashboard project still has no sprint… The project exists with no sprints and no start/end dates."**

**It had a sprint by 7 September at 15:40 UTC**, roughly 22 hours before yesterday's export ran. The board's own audit trail is unambiguous: twelve items created between 14:26 and 14:33 on 7 September, owners assigned at 15:39, and all twelve moved from Backlog into a sprint named `0901-admin` at 15:40:32.

The mechanical cause is documented and was predicted. `beevia-refresh` §1b says plainly: *"Its sprints will have their own names. The main `ZOHO_SPRINT_FILTER` (`08-01`) will not match, so the step keeps skipping with exit 3 until you pass `--sprint <name>`. A silent exit 3 after the board is live means exactly this."* The export printed the answer as it exited:

```
No sprint matches '08-01' in project 187554000000127002. Available: ['0901-admin']
```

The failure was reading the exit code and not the message — carrying forward a sentence that had been true for nineteen editions instead of checking whether it still was. That is the same failure mode as the 8 September translation correction: the data contained the answer, and the report reused a conclusion instead of re-deriving it. **A claim that has been true for nineteen days is the most dangerous kind to restate**, because nothing about repeating it feels like an assertion.

Today's run passes `--sprint 0901-admin` and the board is exported. §5 is now a real section.

### 0.3 Correction — the admin client is further along than reported

Yesterday's edition put `beevia-admin` at **6 of 10 feature modules on the live API**. Recounted today by extracting every admin path each module's `api.ts` actually calls, it is **8 of 10**:

| Module | Calls | State |
|---|---|---|
| admin-accounts | `/admin/accounts`, `/admin/accounts/invite`, `/admin/accounts/{id}`, **`/admin/accounts/{id}/reinvite`** | Live |
| auth | `/admin/auth/login`, `/admin/auth/accept-invite` | Live |
| dashboard | `/admin/dashboard`, `/admin/activity` | Live |
| reconciliation | `/admin/reconciliation/pool`, `/admin/reconciliation/users/{id}` | Live |
| roles | `/admin/roles`, `/admin/roles/{id}`, `/admin/roles/{id}/assign-admins` | Live |
| transactions | `/admin/transactions`, `/admin/users` | Live |
| users | nine `/admin/users…` paths | Live |
| wallet | `/admin/transactions/users/{id}` | Live — **but see below** |
| reports | — | **Mock only** (`MOCK IMPLEMENTATION` in `api.ts`) |
| pending-transfers | — | **Mock only** |

Only **one** of the two is a genuine change this window (`admin-accounts`, wired to the new re-invite endpoint hours after it merged); the other is a counting correction. The mock-only pair is unchanged from yesterday, so the substance of that finding stood — the total under it did not.

**One concrete thing falls out of the recount.** The `wallet` module derives a user's balance by fetching the most recent transaction row and reading its `balance_after`, with a comment reading *"Swap for a real `/admin/wallets/{userId}` call if/when one exists."* **It exists** — `GET /admin/wallets/users/{userId}` shipped on 6 September. That is a five-minute change and a one-line standup item.

### 0.4 The 14:00 UTC cut-off produced a false finding, exactly as predicted

Yesterday's risk #20 read: *"The 14:00 UTC cut-off is still producing false 'silence' findings."* Yesterday's export ran at **14:08 UTC**. The seven notification submissions happened at **16:02–16:04 UTC** — under two hours later — along with three of Philip's starts at 15:54 and the admin board's first transitions at 16:08.

So yesterday's report said "nothing has entered REVIEW/QA for eleven days" and "Ayomikun has not touched any of his nine leaves for a fifth consecutive day". Both statements were accurate against the data available at the cut-off, and both had a shelf life of under two hours. **That is what the cut-off costs, and this is the first edition to measure it rather than predict it:** the team's board activity clusters in the late afternoon UTC, and the export runs before it. Moving the run to ~20:00 UTC has been recommended for two editions and would have caught all of this a day earlier.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

25 items — **17 leaves, 8 parent Stories**. Day 7 of 20.

| Status | Leaves | 8 Sep | Δ |
|---|---:|---:|---:|
| To do | 3 | 13 | **−10** |
| In progress | 6 | 4 | +2 |
| REVIEW/QA | **7** | 0 | **+7** |
| BLOCKED | **1** | 0 | **+1** |

| Owner | Leaves | To do | In progress | REVIEW/QA | BLOCKED |
|---|---:|---:|---:|---:|---:|
| Ayomikun Araoye | 9 | 1 | 0 | **7** | 1 |
| David Samuel | 6 | 2 | 4 | 0 | 0 |
| Philip Chidera | 2 | 0 | 2 | 0 | 0 |

### 1.2 The window's movement

Eighteen status transitions, **all of them on 8 September between 15:54 and 16:06 UTC** — a single working session after yesterday's export closed.

| Time (UTC) | Items | Transition | By |
|---|---|---|---|
| 15:54 | `BVA-I234`, `BVA-I235`, `BVA-I236` | To do → In progress | Philip Chidera |
| 16:02–16:04 | `BVA-I246`–`BVA-I252` (7) | To do → **REVIEW/QA** | Ayomikun Araoye |
| 16:03 | `BVA-I244`, `BVA-I245` | To do → **BLOCKED** | Ayomikun Araoye |
| 16:03 → 16:06 | `BVA-I230`, `BVA-I231` | To do → BLOCKED → **To do** (reverted after 3 min) | Ayomikun Araoye |

Philip again started an item David owns (`BVA-I236`). That pattern was noted on 8 September and has not changed: **board hygiene is being performed by one person on behalf of others**, which makes "who started this" an unreliable signal on this board.

### 1.3 The seven submissions describe code that shipped in July

This is the finding that matters most in this edition, and it needs stating carefully because the number looks like good news.

`BVA-I246`–`BVA-I252` are the sprint's entire push-notification workstream. All seven went **To do → REVIEW/QA directly**, skipping `In progress`, in 118 seconds. Checked against `beevia-api` at `origin/main`:

| Item | What it asks for | Where it already is | Merged |
|---|---|---|---|
| `BVA-I246` Send capability & device-token storage | FCM credential, token registration | `src/notifications/fcm.adapter.ts`, `POST/DELETE /notifications/token` | **11 Jul** |
| `BVA-I247` Payload structure (routing data) | Typed payload behind a port | `src/notifications/notification.port.ts` | 11 Jul |
| `BVA-I248` New-message trigger | Push on message send | `src/messaging/messages/messages.service.ts` | Aug |
| `BVA-I249` Incoming-call trigger | Push on call invite | `src/messaging/calls/calls.service.ts` | Aug |
| `BVA-I250` Money & wallet triggers | Push on transfer events | `src/payments/payment.service.ts` | Aug |
| `BVA-I251` Account & verification triggers | Push on contact/status change | `src/users/contact-change.service.ts` | Aug |
| `BVA-I252` Preference storage & enforcement | Per-category preferences | `notification-settings.service.ts`, `GET/PATCH /notifications/preferences` | Aug |

**No commit has touched `src/notifications/`, `src/devices/` or `src/messaging/` at any point since sprint 0901 opened on 3 September.** `beevia-api` has had exactly one commit in this window, `3de769c`, and it is a logging-redaction fix touching four files in `src/common/`. The consumer API surface is unchanged at 131 operations.

The honest reading: **someone reconciled the board against the codebase and found seven stories already satisfied.** That is genuinely useful work — the sprint was planned with items that were already built, and discovering that on day 6 is much better than discovering it on day 20. But three consequences follow, and all three are easy to miss:

- **It is not throughput.** Yesterday's "eleven days since anything entered review" becomes "zero days" on a metric that measured nothing moving through a pipeline. Quoting +7 as delivery would be wrong.
- **The remaining sprint is smaller than the board says, and differently shaped.** If those seven are accepted, sprint 0901's real remaining scope is the translation half plus notification *preferences enforcement* verification — and the translation half has produced no merged code either (§3).
- **There is a live gap underneath them that no board item covers.** `NotificationsModule` picks its transport at boot: real FCM when `FCM_SERVICE_ACCOUNT` is set and parses, **otherwise a `StubPushAdapter`**, with a warning log. `FCM_SERVICE_ACCOUNT` is optional in `env.ts` and blank in `.env.example`. So "push notifications work" is true of the code and unknown of any deployment. This is the same silent-fallback shape as `ANCHOR_POOL_ACCOUNT_ID` (risk #14) and LiveKit — a credential whose absence degrades to a no-op rather than a failure. Accepting `BVA-I246` without checking the deployed value accepts a stub.

### 1.4 One item is genuinely blocked, and it is the backend translation work

`BVA-I245` *Backend String Bundles & Selection Logic* (and its parent `BVA-I244`) moved to **BLOCKED** at 16:03 UTC and stayed there. The `Blocked by` and `Blocked On` columns are both empty, so the board records the state without the reason.

`BVA-I244`'s acceptance criteria are translated string bundles for backend-originated user-facing text — push notification bodies, OTP and transaction messages — selected per user from their stored language preference. **That preference does not exist yet**: `BVA-I230`/`BVA-I231` (Language Preference Storage) are its prerequisite and were themselves marked BLOCKED for three minutes before being reverted to To do. So the most likely reading is an ordering dependency inside the same person's own queue — but that is inference, and the board should say.

Worth noting what it means for §1.3: the backend half of the *translation* workstream is blocked, while the backend half of the *notification* workstream is in review because it was built in July. Ayomikun's nine leaves are now 7 in review, 1 blocked, 1 to do — which is a very different picture from "nine untouched items" and a much more legible one.

### 1.5 Still no estimates — sixth consecutive edition

**0 of 25 on 0901, and 0 of 12 on the new admin board.** No tags either. Velocity, burn-down and any normalisation of one person's load against another's remain underivable. The new board arrived without estimates, which was the moment it was cheapest to add them.

---

## 2. What shipped this cycle

### 2.1 `beevia-admin-api` — five operations, 37 → 42

The busiest single day this service has had. All five are on `main` and all five are now in `openapi.admin.yaml`.

**The chats module (4 operations), `6b105d8`** — the branch rescued from the malware cleanup.

| Method | Path | Permission |
|---|---|---|
| GET | `/admin/chats` | `chats:view` |
| GET | `/admin/chats/reports` | `chats:view` |
| GET | `/admin/chats/users/{userId}` | `chats:view` |
| GET | `/admin/chats/{conversationId}` | `chats:view` |

**This is spec Module 4 — the one `admin-api-rfc.md` §5.1 has called unbuildable-as-specified since 5 August — built as §5.1 recommended.** The spec wants the moderation queue to show "reported messages"; chat is E2EE and the server holds no key. The module implements Option A, metadata only, and honours the constraint explicitly rather than incidentally: the controller docstring reads *"Chat is end-to-end encrypted, so these endpoints serve metadata + moderation only — never message content,"* and every operation repeats it. There is no field anywhere in the module for message text.

**`GET /admin/chats/reports` is the first reader `conversation_reports` has ever had.** That finding has been open since 5 August — the consumer app's `POST /conversations/{id}/report` writes to the table and nothing read it, so reports accumulated unreviewed. It is now closed.

Four contract facts, written onto the operations in the spec rather than left to be discovered:

- **It is a queue, not a workflow.** No status, no assignment, no resolve action, no filter for open items — it returns *every report ever filed*, forever. A moderator cannot mark one handled, so tomorrow's queue is today's plus arrivals. The backlog that accumulated before this endpoint existed is in there, undifferentiated from today's.
- **Acting on a report is disconnected from the report.** `suspend` and `restrict` exist, but nothing links a report to the action taken on it. "What did we do about this one?" is unanswerable from the API.
- **`GET /admin/chats/users/{userId}` returns both block directions** — who the user blocked and who blocked them. That is the quietly good part: a harassment complaint reads very differently depending on which way the blocks point, and neither direction is visible anywhere else in the admin API.
- **Route ordering is load-bearing.** `@Get('reports')` is declared before `@Get(':conversationId')`. Swapping those two methods silently turns the moderation queue into a 404.

**`POST /admin/accounts/{id}/reinvite`, `3af6f8b`.** Re-issues the one-time setup link for an admin still in `invited` status. It closes a genuine dead end — before this, an admin whose invite expired was stuck, and the only workaround was deleting and recreating the account. Three details worth carrying into the UI: it **invalidates the previous link** (so "check your email again" means *the newest* one); `409 admin_not_invited` covers both "already accepted" and "deactivated", which are opposite next actions, distinguished only by the message text; and it records an `admin_invited` activity entry rather than a distinct action, so anything counting invites from `GET /admin/activity` will double-count resends.

**`dateFrom` / `dateTo` on both transaction feeds, `e09bba5`.** A contract change rather than a new operation. It is done carefully: a bare `dateTo` widens to `23:59:59.999Z` so picking a day includes that day, `2026-02-30` is a `400` rather than a filter that silently matches nothing, and the bounds narrow **the count as well as the rows**, so a date-scoped `pagination.total` is the total for that range. It ships with its own spec file and moves the shared bound parser into `common/day-boundary.ts`. The same commit adds the Wallets folder to the Postman collection, which shipped without one on 6 September.

### 2.2 `beevia-admin` — the re-invite button, wired the same day

`a33b34c`, Promise Udo, 8 September 16:58 local. The Admin Accounts screen's resend-invite button now calls `POST /admin/accounts/{id}/reinvite` — a net **−12 lines**, because the client had been faking a resend and can now just call the endpoint. It ships with an updated test.

That is the third time in six days this workstream has consumed a new endpoint within hours of it merging (dashboard on 7 Sep, transactions on 4 Sep). **It remains the shortest endpoint-to-client latency in the project**, and until today it was also the least visible.

### 2.3 `beevia-db-schema` — the reports table, released twice

`admin_reports` merged and released as **v0.0.28**, with the `AdminReportType` / `AdminReportStatus` exports following as **v0.0.29**. Both on 8 September. This is infrastructure for the unmerged reports feature (§4.3) — the schema landed before the service that uses it, which is the right order.

### 2.4 `beevia-api` — one commit, and it is a good one

`3de769c`, *"make a redacted field diagnosable (shape + validation details)"*. Redaction now preserves a field's *shape* — length, origin+path for URLs — while still removing the value, and credentials (PIN, OTP, password, token, PAN, CVV) keep a bare `[REDACTED]` because their length is itself a hint. The exception filter appends Zod validation issues as "field: why", capped at five, never values.

It is a small change to logging that makes production incidents debuggable without weakening the redaction, and it is the only consumer-API commit in the window. **Every consumer-API capability in the MVP rubric is otherwise unchanged for a fifth day**: the translate stub, `PaymentService.activeNgn()`, the unset `ANCHOR_POOL_ACCOUNT_ID`, the `POST /kyc/profile` silent-200.

### 2.5 `beevia-mobile` — nothing, for the fourteenth day

`main` is unchanged since 26 August. `origin/BVA-I192` is still **14 commits ahead**, with no new commits since 7 September — so the branch that was resolving conflicts yesterday did not move today either. Sprint 0901's four In-progress mobile items have produced no commits on any branch in this window.

---

## 3. The translation workstream has a design and no code

Worth separating from §1.3, because the two halves of sprint 0901 are now in genuinely different states.

`BVA-I228` establishes the architecture — on-device translation via iOS's Translation framework and Android's ML Kit, so message content never leaves the phone. The 8 September edition corrected this pipeline's earlier claim that the sprint was blocked on a server-side provider; that correction stands and `api-rfc.md` §5.5a carries it.

What has not happened is any code. `BVA-I229` (Translation Engine Integration) is **To do**. `beevia-mobile` `main` has fourteen days without a commit and no branch carries translation work. Four items are In progress — three David's, one Philip's — and two of them have been In progress for **4.9 days against David's 2.6-day median and Philip's 0.9-day median**.

`POST /translate` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter` and returns its input unchanged. On the on-device design that no longer blocks chat, but it remains a live route that lies to any caller that is not the chat client — and now that the notification half looks close to done, it is the translation half that determines whether this sprint lands.

---

## 4. Spec updates made this cycle

### 4.1 `openapi.admin.yaml` — 37 → 42

Five operations added, documented from the controllers, DTOs, services and response types read at `origin/main`:

- **Chats (4)** — new `Chats` tag; new `ConversationId` and `ChatUserId` parameters; new `ChatUserRef`, `ChatConversationRow`, `ChatParticipant`, `ChatReportView`, `ChatReportRow`, `ChatConversationDetail` and `UserChatsView` schemas. `TransactionsPagination` is reused rather than duplicated, consistent with the wallets precedent.
- **`POST /admin/accounts/{id}/reinvite`** — including the `409` ambiguity and the `admin_invited` audit-entry note.
- **`dateFrom` / `dateTo`** added as shared `DateFrom` / `DateTo` parameters on both transaction feeds, with the bare-date widening and the count-narrowing behaviour written onto the operations.

Response keys are documented in **snake_case** — `participant_count`, `last_message_at`, `blocked_by` — because `ResponseInterceptor` converts every key recursively before it leaves the service. This is the same trap that caught the activity feed on 2 September: reading a controller tells you what a handler returns, not what a client receives.

### 4.2 `openapi.admin.proposed.yaml` — 20 → 19

`GET /admin/reports` (the Trust & Safety moderation queue) **shipped as `GET /admin/chats/reports`** and is replaced by a `NOTE` in the house style. Following the wallets precedent, the note records **what did not ship**, because that is the part someone would otherwise re-propose from scratch:

- the `status` filter (open / reviewing / actioned / dismissed),
- the reported user's prior report history beside the row,
- any link from a report to the account action taken on it.

That set is the workflow half of Module 4, and `admin-api-rfc.md` §6.3 now carries it as a gap. Without a status and a resolve action **the queue cannot be worked off at all**, so it only grows; and because metadata-only moderation's entire signal is patterns across reports (§5.1), a queue that does not surface a user's report history delivers Option A's costs without its benefit.

### 4.3 A real path collision, flagged before it lands

The unmerged branch `feat/admin-reports` implements a **report-generation** feature — a catalogue of report types, async CSV generation, run history, download — at `GET /admin/reports/types`, `POST /admin/reports`, `GET /admin/reports`, `GET /admin/reports/{id}` and `GET /admin/reports/{id}/download`.

Module 4's two remaining proposed operations are `GET /admin/reports/{reportId}` and `POST /admin/reports/{reportId}/resolve` — a *moderation* report. **Same path, unrelated resources.** They cannot coexist, and the generation feature has a board behind it (§5) while Module 4's workflow half has nothing, so it wins by default.

The proposed file now carries a `PATH COLLISION` block above both operations rather than a rename, because renaming a proposal on the strength of an unmerged branch is guessing. The recommended resolution is to move Module 4's workflow operations under `/admin/chats/reports/{reportId}`, where the shipped queue already lives. `suggestions.md` §5.6 generalises it: `/admin/reports` was never a good name for either, because "report" means both "a complaint about a user" and "an exported dataset", and this API now needs both.

### 4.4 Narrative documents

- **`admin-api-rfc.md`** — counts 37 → 42 and 20 → 19; §1 summary rewritten (a sixth module opened, and finding #3 downgraded from **Blocking** to *decided in code, unrecorded*); coverage table updated (Module 4: 0 → 4 ops, Module 2: 3 → 4); new **§3.13 Chats**; §3.2 gains the re-invite row and its three UI traps; §5.1 strikes the "nothing reads it" paragraph; **§5.1a rewritten** — Option A merged, and the product decision is still recorded nowhere but the code; new **§5.4b** on the unmerged reports feature and the path collision; **§6.3 grows to five gaps**, with the statement-filter gap marked mostly closed and Module 4's missing workflow added as the one to act on first.
- **`api-rfc.md`** — the two stale "29 operations" references to the admin service corrected to 42.
- **`suggestions.md`** — §7.6 closed with the verification evidence; §8's order re-headed (item 1 struck as done); new §5.6 on the path collision, with a proposed CI check that reuses the audit's existing route extraction.

### 4.5 Spec health

All four files parse. **131 / 42 / 42 / 19** operations. No `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s.

**Drift against `origin/main`: zero, both services, both directions** — `beevia-api` 131 = 131, `beevia-admin-api` 42 = 42. The audit script reports eight phantom "documented, not in code" lines for `beevia-admin-api` because it reads the *working tree*, which is still 4 September code (§7). Flagged for the third consecutive edition so that nobody "fixes" the spec by deleting eight real operations.

---

## 5. Admin dashboard board — the first real section

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 7.** 12 items — **8 leaves, 4 parent Stories**. Created 7 September, 14:26–15:40 UTC (§0.2).

| Status | Leaves |
|---|---:|
| To do | 4 |
| In progress | 2 |
| Done | **2** |

| Owner | Leaves | To do | In progress | Done |
|---|---:|---:|---:|---:|
| Promise Udo | 4 | 2 | 1 | 1 |
| Ayomikun Araoye | 3 | 1 | 1 | 1 |
| Unassigned | 1 | 1 | — | — |

**The board is the Reports module, decomposed cleanly.** Four stories, each split into a backend "Report Data Query" (Ayomikun) and a frontend "Report Content Display" (Promise) — infrastructure, then User & KYC, Transaction & Financial, and Admin Activity / Audit reports. It is the most legibly structured board in this project: the split matches the actual ownership boundary, and every story has both halves.

**Promise Udo has a board row for the first time in twenty editions.** The standing caveat — "report the responsibility and judge the work from commits" — is retired for this workstream. It still applies to nothing else, because the admin *dashboard client* work outside Reports remains untracked on any board.

### 5.1 Three things to read carefully on a seven-day-old board

- **The two Done items describe code that is not on `main`.** `BVA-I11`/`BVA-I12` (Transaction & Financial Report) were marked Done at 16:08:49 UTC on 8 September. The backend half sits on `feat/admin-reports`, unmerged (§4.3). The frontend half is `beevia-admin/src/features/reports/api.ts`, which still opens with `MOCK IMPLEMENTATION — no network calls`. Neither is on a default branch. **Worth settling as a definition-of-done question rather than filing as a defect**: if Done means "my part is written", the board is accurate and means something different from the main board's Done; if it means "merged", two items are ahead of themselves.
- **All three Done transitions were made by one person in a 43-second window**, including the item owned by someone else — marked Done at 16:08:17, reopened at 16:08:30, marked Done again at 16:08:49. That is board setup, not delivery, and it is the same by-proxy pattern the main board shows (§1.2).
- **`BVA-I14` is Unassigned**, and it is the only backend query task without an owner. On this board `Unassigned` is a real gap rather than the parent-story artifact it usually is on the main board — `BVA-I14` is a leaf.

### 5.2 Never summed with the main board

12 items here and 25 on sprint 0901 are different projects, different backlogs, and one person appears on both. A combined "37 items" would be meaningless, and the two boards are kept separate everywhere in this report — including in the team table, where Ayomikun's board leaves are shown as "9 on 0901 · 3 on 0901-admin".

The export is written to `sprint-board-exports/admin/`, not the main folder, because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and treats every match as a snapshot of one board. A second project's CSV in the main folder would make tomorrow's delta diff two unrelated boards and report invented movement.

---

## 6. Team performance — detail

All figures come from the activity sidecars and git, never from `Last Modified`. Commit counts are trailing-7-day, merged to the default branch except where stated, summing each person's git identities and excluding bots.

**Ayomikun Araoye — backend + admin API.** **22 commits** across `beevia-api` (7), `beevia-admin-api` (13) and `beevia-db-schema` (2), summing `Ayomikun Araoye`, `Phoenixdadhev` and `phoenixdahdev`; the count includes merge commits. Up from 20, and unlike yesterday's figure — which was inflated by the history rebuild — **this week's increase is real feature work**: five admin endpoints, a schema release, and a logging fix. He also completed the malware remediation properly, merging rather than deleting the one branch that held unique work. On the boards he holds nine 0901 leaves (7 in review, 1 blocked, 1 to do) and three on the admin board. The seven submissions are the thing to read carefully (§1.3): they are a board reconciliation, and reading them as a week's output would overstate it by a lot.

**David Samuel — mobile.** One genuine submission in the trailing 7 days, on 3 September; median cycle 2.6 d over 14 passes. **Zero commits to `main` and zero new commits on `origin/BVA-I192`** in this window — the branch stands at 14 commits, unchanged since 7 September. He holds four 0901 leaves In progress: `BVA-I233` and `BVA-I241` at **4.9 days against a 2.6-day median**, plus `BVA-I243` (1.1 d) and `BVA-I236` (0.9 d, started for him by Philip). Four items open simultaneously, two of them at roughly twice his own median, with no commits anywhere in a day, is the clearest "is something stuck?" signal on either board. `beevia-mobile` `main` is now **14 days** without a commit and the entire translation workstream depends on it (§3).

**Philip Chidera — design.** No submissions in the window; median cycle 0.9 d over 7 passes. Two leaves In progress: `BVA-I240` at **4.9 days against a 0.9-day median — over five times his own pace**, and the most overdue WIP relative to its owner on any of the three boards — and `BVA-I235`, started last night. He also made three of the window's eighteen transitions, one of them on an item he does not own. His pattern for two weeks has been short bursts of board maintenance separated by quiet days; `BVA-I240` sitting at 5× his median through that is worth one question.

**Promise Udo — admin dashboard.** **4 commits**, and a board row at last. He holds four leaves on `0901-admin` (2 To do, 1 In progress, 1 Done) and shipped the re-invite wiring within hours of the endpoint merging (§2.2). The workstream's characteristic remains the shortest endpoint-to-client latency in the project. The caveat that replaces the old one: **his Done item is not on `main`** (§5.1), so his board and his commit log are not yet telling the same story.

### 6.1 Weekly submission trend

Genuine submissions into REVIEW/QA by leaf items, counting **each pass** (an item sent back and resubmitted counts twice), across the main board and 0901:

| ISO week | Passes | Distinct items |
|---|---:|---:|
| W33 (11–17 Aug) | 1 | 1 |
| W34 (17–23 Aug) | 17 | 17 |
| W35 (24–30 Aug) | 31 | 19 |
| W36 (31 Aug – 6 Sep) | 3 | 3 |
| W37 (7–9 Sep) | **7** | 7 |

**A method note, because this series differs from yesterday's.** The 8 September edition reported W35 as 10; counted as passes it is 31, and as distinct items 19. The gap is real rework: **twelve W35 items entered REVIEW/QA twice**, having been sent back. Both counts are defensible and this edition states which it is using; the pass count is the one that reflects reviewer and developer effort, and it shows W35 as by far the busiest week rather than a quiet one.

W37's seven are the notification items (§1.3) and should not be read as delivery.

### 6.2 Cycle times

Unchanged — **no new passes were measured this window.** The seven submissions went To do → REVIEW/QA without passing through `In progress`, so by this report's method (one measurement per pass, from an item's most recent entry into `In progress` to the next time it reaches `REVIEW/QA`) they produce no measurement at all. **The absence is informative in itself:** these seven were never tracked through a working state, so there is no elapsed duration to measure — which is consistent with §1.3's reading of them as a reconciliation rather than a week's work.

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

### 6.3 What these figures do not measure

- **They cannot distinguish delivery from reconciliation.** The single largest movement in this window — seven items into review — reflects a board being corrected, not work being finished (§1.3). No board metric can tell those apart; only reading the code can.
- **They do not see branches.** David reads zero commits while fourteen sit on `origin/BVA-I192`. Every "commits" figure means *merged to the default branch*.
- **They count merge commits.** Ayomikun's 22 includes merges, which inflates a busy integration week relative to a busy authoring one.
- **They do not measure whether "Done" means merged.** Two items are Done on a board whose code is on an unmerged branch and in a mock file (§5.1).
- **No estimation points exist on any item, on any of the three boards** — 0/64, 0/25, 0/12. Nothing is normalised for size.
- **Board actions are not evenly attributable.** Figures key to the item's assignee, not to whoever clicked; on both boards one person performs transitions for others.
- **Review and triage work is invisible**, and there was again none to record — nothing has *left* REVIEW/QA on any board.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction. Noted anyway because the trend continues: the chats module, the re-invite and the date filter all shipped with `.spec.ts` files in the same commit.

---

## 7. Risks

1. **The infected workstation's status is unknown.** Until it is confirmed clean, the next legitimate commit can reintroduce the payload — and the repositories are now clean enough that a recurrence would be unambiguous.
2. **Credential rotation cannot be verified from here**, and it is the step that decays fastest.
3. **Branch protection cannot be verified from here** — the available GitHub token has no org access. The control this report has recommended for four editions still has no instrument behind it.
4. **Three repositories remain unsynced locally** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`), so the deterministic audit reads 4 September code and reports eight phantom drift lines. Every code claim here was made against `origin/main`.
5. **Seven items are in review that no reviewer has touched**, and the review queue has never had anything leave it on this project. Output with zero acceptance is the same bottleneck the last four editions have named.
6. **Accepting `BVA-I246` may accept a stub.** `FCM_SERVICE_ACCOUNT` is optional and unset in `.env.example`; without it push silently degrades to `StubPushAdapter` (§1.3).
7. **The translation half of 0901 has produced no code in 7 of 20 days**, and its backend prerequisite is BLOCKED with no reason recorded (§1.4).
8. **`beevia-mobile` `main` is 14 days stale** and every mobile item in the sprint depends on it.
9. **A 14-commit mobile branch has been unmerged for twelve days** under a Done board item, and did not move today.
10. **Two admin-board items are Done for code that is on no default branch** (§5.1).
11. **`/admin/reports` is claimed by both an unmerged feature and a standing proposal** (§4.3). Whichever merges first takes the name silently.
12. **Module 4 shipped as a queue with no way to work it off** (§4.2) — no status, no resolve, no reported-user history.
13. **The product decision behind Module 4 is recorded nowhere but a controller docstring.** The dashboard spec still says "reported messages"; the API says metadata-only.
14. **The per-user reconciliation check will report false discrepancies for every user the moment the treasury pool is enabled** — `ANCHOR_POOL_ACCOUNT_ID` is still unset.
15. **`treasury.solvent` is on the live landing screen and reads `false` for "unknown".**
16. **The money-oversight surface still has no second reviewer** — PRs #1–#6 were self-merged.
17. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows; exceeding the caps produces wrong output, not visible truncation.
18. **The Anchor webhook backfill is still unscoped** — 67 days of dropped events, unmeasured, eight days after the fix.
19. **The daily export still targets a closed sprint**, fourth consecutive edition — now with two live sprints it is not covering.
20. **The 14:00 UTC cut-off produced a false silence finding yesterday**, measured this time (§0.4). Third edition recommending the change.
21. **No estimation points on any of three boards** — sixth edition asking.
22. **The same silent-200 is still live on `POST /kyc/profile`** — seventh consecutive edition.
23. **A hard-coded account number still reaches a money screen on `main`** — seventh consecutive edition.
24. **`POST /translate` still returns its input unchanged.**
25. **The admin client's `wallet` module ignores the wallets endpoint** built for it (§0.3).
26. **This service now has three pagination conventions across six endpoints** (`admin-api-rfc.md` §6.3).

---

## 8. Previous recommendations — where they stand

| Recommendation from 8 Sep | Status on 9 Sep |
|---|---|
| Clear the eight infected branches — seven deletions and one rebase | ✅ **Done, exactly as recommended.** Seven gone, `feat/admin-chats` merged onto clean history (§0.1) |
| Sweep every ref and verify by blob hash | ✅ **Done.** Payload reachable from no ref in any of the five repos (§0.1) |
| Confirm the workstation and credential rotation | ❌ **Still invisible from here.** Unchanged |
| Rebase `feat/admin-chats` and decide whether to merge it | ✅ **Merged** (§2.1). The *product* half — recording that Option A is the answer to Module 4 — is **not** done |
| Decide the translation API question | ❌ **No decision recorded.** The two proposed operations stay annotated |
| Start `BVA-I246`, or move the notification half out of 0901 | ⚠️ **Neither, and the question changed.** It went straight to REVIEW/QA because the code already existed (§1.3) |
| Merge `BVA-I192` or say why not | ❌ **Not done**, and it did not move today |
| Move the daily export to sprint 0901 | ❌ **Not done.** Fourth edition — now costing two scratch exports rather than one |
| Put estimation points on 0901 | ❌ **Not done.** 0/25, and the new board arrived at 0/12 |
| Get a token with org read access, or check branch protection by hand | ❌ **Not done** |
| Apply the BVN-ordering guard to `POST /kyc/profile` | ❌ **Not done.** Re-checked at `origin/main`; unchanged |

**Four of eleven actioned, and they are the four that mattered most** — the entire security backlog that was actionable from inside the repositories is now closed. What remains unactioned is almost entirely the process items: estimates, the export target, the cut-off, and decisions that need writing down rather than building.

---

## 9. What I would do this week

1. **Answer the notification question before the seven items are accepted** (§1.3). If they are already-shipped work being reconciled, say so on the board and the sprint's real remaining scope becomes visible. If they are meant as new work, something is wrong, because no commit touched that code this sprint. Either way, **check `FCM_SERVICE_ACCOUNT` in the deployed environment first** — without it, accepting `BVA-I246` accepts a stub adapter.
2. **Review something.** Seven items have been sitting in REVIEW/QA since yesterday afternoon and nothing has ever left that column on this project. The queue is now the constraint in a way it has not been before, because for the first time there is something real in it.
3. **Decide `/admin/reports` before `feat/admin-reports` merges** (§4.3). Moving Module 4's proposal to `/admin/chats/reports/{reportId}` is a five-minute edit today and a breaking rename after the merge.
4. **Write down that Option A is the answer to Module 4.** It is built, merged and shipped; the dashboard spec still says "reported messages", and the only place the decision exists is a controller docstring. This is the second good architectural call in two weeks made silently — the first was on-device translation — and both were found by reading code rather than by being told.
5. **Unblock `BVA-I245`, or record why it is blocked** (§1.4). The board carries the state with an empty `Blocked by`, so the dependency is inference. If it is waiting on `BVA-I230`/`BVA-I231`, that is a two-item ordering problem inside one person's queue and it is solvable today.
6. **Ask David what is happening.** Four items In progress, two at ~2× his median, zero commits anywhere in the window, `main` 14 days stale, and a 14-commit branch that stopped moving. None of that establishes a cause, which is why it is worth asking rather than assuming — but the translation sprint depends on the answer and there are thirteen days left.
7. **Fix the definition of Done on the admin board** (§5.1), while it is seven days old and costs nothing. Two items are Done for code on an unmerged branch and in a mock file. Whichever definition is intended, agreeing it now avoids a board that means something different from the main one.
8. **Point the `wallet` module at `GET /admin/wallets/users/{userId}`** (§0.3). Its own comment asks for the endpoint that shipped three days ago; it is currently inferring a balance from the last transaction row.
9. **Move the daily export to sprint 0901 and add the admin board to the routine.** Fourth edition asking, and the cost has doubled — the pipeline now maintains one in-repo export of a *closed* sprint plus a scratch export of the live one. Relocating the tracked CSVs into `sprint-board-exports/08-01/` and changing `ZOHO_SPRINT_FILTER` is half an hour.
10. **Move the report cut-off to ~20:00 UTC.** Measured cost this edition: a full day's delay on eighteen transitions, three of yesterday's headline findings, and one incorrect claim about the admin board (§0.4).
11. **Put estimation points on all three boards, or state that this project does not estimate.** Sixth edition. The new board is twelve items old and it is cheapest right now.
12. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Unchanged for seven editions; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:00 UTC) → **admin board export, first successful run**, with `--sprint 0901-admin` (12 items) → fast-forward sync (1 commit into `beevia-admin`; 3 repos refused as `diverged`) → repository-wide integrity sweep across every remote ref by blob hash → deterministic audit → static contract review of the five new admin operations read from `origin/main` → spec and RFC updates → re-audit, plus a second drift check run against `origin/main` extracted to a temp directory → read-only scratch export of sprint 0901 → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran during this refresh. The three unsynced repositories were read with `git show`, `git log`, `git cat-file` and `git archive` into `/tmp`, outside the workspace. No repository was reset, rebased, reverted or cleaned, no file in any sub-repo was edited, and the sync step's `--ff-only` limit was not overridden.

**Degraded inputs.**
- **Three repositories could not be synced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` remain `diverged` because `origin/main` was rewritten during the remediation; `sync_repos.py` is `--ff-only` and correctly refuses. Their *working trees* are 4 September code, which is the sole cause of the audit's eight phantom drift lines. Resolving it needs `git reset --hard origin/main` or equivalent, which is outside this pipeline's sanctioned exception and is a decision for whoever owns those clones. The evidence says it is safe: `origin/main` is verifiably clean (§0.1). **Capture the local tips first** (`d9af17b`, `43abc3a`, `5b0592a`) — they are the only offline copy of the pre-incident history.
- **The `Epic` column is blank** on both boards — the OAuth refresh token lacks `ZohoSprints.epic.READ`. A known scope gap, not "no epic assigned"; the audit trail shows epics *are* set (`BVA-I246` carries "Notification").
- **`Comments` bodies are unavailable** from the API.
- **`ZOHO_SPRINT_FILTER` is stale** — still `08-01`, so the in-repo main export covers a sprint that closed on 28 August. Sprint 0901 is exported to `/tmp/beevia-scratch/` for the fifth consecutive edition, and for the same reason: `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest as snapshots of one board.
- **Branch protection, credential rotation and workstation remediation are unverifiable** from this workspace.
- **No estimation points on any item, on any of three boards**, so velocity is not derivable and no per-person figure is normalised for size.
- **The admin board is 7 days old.** Its two Done items and three In-progress items are too few to support any trend; §5 reports state, not throughput, and no cycle time is computed from it.

**Window.** 8 Sep 14:00 UTC → 9 Sep 14:00 UTC. All `actiontime` values and board times are UTC; the local export host runs UTC−6, so the 08:02 local run is a 14:02 UTC cut-off. Note that **every board transition in this window occurred between 15:54 and 16:08 UTC on 8 September** — inside the two hours after the previous export closed (§0.4).

**Sources.** Boards: `beevia-sprint-board-2026-09-09.csv` (64 rows, 41 leaves, sprint 08-01) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-09.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (25 rows, 17 leaves) + activity sidecar. Code: `beevia-admin` and `beevia-mobile` at `origin/main` in the working tree; `beevia-api`, `beevia-admin-api` and `beevia-db-schema` read from `origin/main` refs without checkout. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (**42**), `openapi.admin.proposed.yaml` (**19**) — all validated, no markers, no broken refs, no orphaned components.

**A note on who appears here.** Only people whose work is tracked have rows. Board transitions performed by non-contributors are reported without attribution, per the standing instruction; several of this window's item creations and owner assignments fall into that category.

<a id="mvp-method"></a>

### MVP readiness — ≈57% (estimate; 56.75, from 56.33)

**Target 2026-09-01 (provisional) · the target date passed eight days ago.** On merged build evidence the product is roughly 57% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Unchanged. Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. Only `beevia-api` commit in the window was a logging fix |
| 2 | Voice & video calling | 8 | 0.8 | Unchanged. 4 call endpoints live; `audio_call_screen` / `video_call_screen` present; incoming-call push wired — though the push transport falls back to a stub without `FCM_SERVICE_ACCOUNT` |
| 3 | Message translation | 7 | 0.15 | **Unchanged.** `TranslateModule` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`. The on-device design (`BVA-I228`) is confirmed but **`BVA-I229` is still To do**, `beevia-mobile` `main` has 14 days without a commit, and no branch carries translation work. A design decision is not build evidence |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged; no consumer-API commit touching wallets. Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` unset), so not scored. Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. `PaymentService.activeNgn()` still present at `origin/main`. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. Ceiling still low: the client has **zero** `/cards` references and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | No endpoint or record anywhere. The only `consent` references in the codebase belong to the YouVerify KYC provider |
| 11 | Admin oversight | 6 | **0.85** ↑ | **+0.07 — the only capability that moved, and it moved on merged code.** Admin API 37 → **42**: the chats module (4 ops) opens **spec Module 4**, taking modules with something built from 5 of 8 to **6 of 8**, and `POST /admin/accounts/{id}/reinvite` completes Module 2 (§2.1). On the client, `beevia-admin` is at **8 of 10** feature modules on the live API — one genuine gain (re-invite, wired within hours) and one counting correction (§0.3). Ceiling, and it is still real: `reports` and `pending-transfers` remain mock-only, Modules 6 and 8 have no endpoints at all, Module 4 shipped as a queue with no status/resolve/history, there is still no per-wallet partner-balance comparison, and no 2FA |
| | **Weighted total** | **100** | | **56.75 → ≈57%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, never merged-but-disabled code, and never a design decision on its own. Three of this edition's most prominent events are therefore worth zero points — the seven items in review (already-merged code, already scored), the unmerged reports feature, and the admin board's two Done items.
