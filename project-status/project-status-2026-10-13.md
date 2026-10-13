# Beevia — Project Status

**As of 2026-10-13** · Sprint **0902** (30 Sep → 15 Oct): **day 14 of 16, 25 items, 0 leaves To do · 4 In progress · 15 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-13.csv` + `beevia-activity-2026-10-13.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-13.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 9 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`. `beevia-mobile`'s unmerged `origin/BVA-I316` and `origin/BVA-I306` branches were read too. `beevia-admin` and `beevia-mobile` were read in the working tree. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 9 Oct 14:10 UTC → 13 Oct 14:03 UTC, 4.0 days** (Friday afternoon to Tuesday afternoon in Lagos, across a weekend).

---

## Quick overview

> **Two days before 0902 ends, 15 of its 21 leaves sit in REVIEW/QA, nothing is left in To do, and nothing has left review. Five more leaves entered review on Monday. Two of them, the Activity screen (`BVA-I316`) and the chat-background picker (`BVA-I324`), have their code only on an unmerged branch, and one (`BVA-I325`) has no code behind it at all. The branch is real work: the client Activity screen, wired to the live `/activity` feed, and CallKit. Its call-push half does not match what the server sends, and merged as-is it would break ordinary pushes on iPhones.** On the backend, `beevia-api` #70 (12 Oct) fixed a defect present since the project's first commit. Drizzle wraps Postgres errors, so every unique-constraint handler in the API (29 call sites) had silently never fired. Duplicates returned `500` instead of `409`, and failed-query logs carried bound values such as phone numbers.

**Correction to `suggestions.md` §1.1 (in place since 5 Aug) and every report that relied on it.** It said `AllExceptionsFilter.mapPostgresError()` "handles `23505`, `23503` and `23502`". In fact none of those mappings could match before #70, because the driver error sat one level down, in `.cause`. The 409 the spec documents for a uniqueness clash was never returned. `suggestions.md` now carries this as §1.6, resolved, with the two loose ends.

| Metric | 9 Oct | 13 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 2 / 7 / 10 / 1 / 1 | **0 / 4 / 15 / 1 / 1** | 5 → QA, 2 started |
| Board actions in the window (all boards) | 6 | **11** | 5 by board administration, 3 by Ayomikun, 3 by David |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **15** | 8 by board administration, 5 by the leaf's owner, 2 by another team member |
| Owners' last submission of their *own* leaf | 9 Oct 14:07 UTC (David) | **12 Oct 16:03 UTC (Ayomikun, `I325`)**; David 9 Oct 14:07 UTC | |
| Items that left REVIEW/QA in the window | 0 | **0** | never, apart from the two bulk sweeps |
| 0902 leaves in REVIEW/QA whose code is not on `main` | — | **3** | `I316`, `I324` on an unmerged branch; `I325` nowhere |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | workflows unchanged since 1 Oct |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | #70 changed no route or documented contract |
| `beevia-mobile` days since a commit on `main` | 1.1 | **5.1** | 3 commits since on `origin/BVA-I316`, the last at 14:02 UTC today |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.0 / 1.3 / 1.3 | **0.9 / 5.3 / 4.1** | |
| `beevia-admin` days since a commit | 16.9 | **20.9** | |
| Admin board: open sprint / days since any activity | none / 25.0 | **none / 29.0** | |
| Successor sprint to 0902 in Zoho | — | **none** | 0902 ends Thursday |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: the new client work is unmerged, and #70 is correctness, which the rubric does not score |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | 6 (**4 own**, 2 by board administration) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**29.0 d**) | **13** (api 11, admin-api 1, db-schema 1) | #70 fixed a life-of-project error-handling defect. Moved `I325` (backend storage) to review with no server change, and `I324`, David's leaf, with its code unmerged |
| David Samuel | mobile | **0902: 15** (10 REVIEW/QA, 4 In progress, 1 BLOCKED) | 10 (**1 own**, 6 by board administration, 3 by Ayomikun) | 0.98 d (n=33) | `BVA-I286` (**12.9 d**) · `I313` (**5.9 d**) · `I309` (1.0 d) · `I307` (0.2 d) | **3 on `main`** (8 Oct) + **3 on `origin/BVA-I316`** (9, 12, 13 Oct) | ~3,900 lines on one unmerged branch: Activity screen, CallKit, chat background. Two items it covers are already in REVIEW/QA |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 1 (moved by David) | 0.99 d (n=3) | none | n/a | No board action since 2 Oct |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**29.0 d**) | **0** | `beevia-admin` **20.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **Who reviews before Thursday, and what counts as reviewable?** Fifteen leaves wait. Ten have their code on `main` (or are design). `I316` and `I324` do not, and `I325` has nothing behind it. (2) **What happens to `BVA-I316`'s branch before it merges?** The Activity screen half is ready to review. The CallKit half registers a VoIP token that would overwrite the iPhone's FCM token on the server, and on Android it reads push keys the server does not send (§3.3). Split it, or fix the contract first. (3) **Is there a sprint after Thursday?** Zoho lists no 0903. Four leaves are in progress and one is blocked, so something carries over. Last time a sprint ended with no successor (0901, 22 Sep), the team worked inside a closed sprint for eight days.

**The three things worth knowing:**

1. **The client Activity screen exists, wired to the real feed, but only on a branch.** `origin/BVA-I316` (`2aba47a`, 12 Oct) adds the Activity tab with its own call-history view. It calls `GET /activity` with the device's real `X-Device-Id` and the documented cursor, and parses the documented `ActivityFeed` shape. A chat row shows the preview the conversation cache has already decrypted on the device, or a placeholder if it has none. The server reads nothing, so the E2EE design from #66 holds end to end. Filter and search run only over pages already loaded, so search cannot reach older activity. Board administration moved `BVA-I316` to REVIEW/QA 18 minutes after the commit, with the branch unmerged. The same branch carries the chat-background change (`I324`, also in review) and, since 14:02 UTC today, the CallKit work for `I309`, which is still In progress.

2. **CallKit, as built, does not match the server's push contract, on either platform.** On iOS the branch registers a PushKit VoIP token through `POST /notifications/token` with `pushProvider: 'voip'`. The server keeps **one** push token per device and sends everything through FCM regardless of provider. The VoIP token would therefore replace the FCM token, and from then on that iPhone's message, payment and security pushes would go to a token FCM rejects. The server also has no APNs VoIP sender, so the native call screen could never ring. On Android the client expects `data.type == 'call.incoming'`, snake_case keys and a data-only message. The server sends `data.kind`, camelCase keys and a visible notification. Nothing breaks until the branch merges. Recorded in `api-rfc.md` §5.15.

3. **The review column is now nearly the whole sprint, and part of it is ahead of the code.** In-progress work fell from 7 to 4. All five leaves that left In progress went to review, three of them by board administration's hand. Ayomikun's six 0902 leaves are all in review. Three are backend "preference storage" items (`I319`, `I325`, `I328`) with no server code. The branch now calls a placeholder `PUT /users/me/appearance/chat-background` that 404s, and its own `TODO(backend)` says so. **Apart from the two bulk sweeps (3 Sep, 30 Sep), no item on any board has ever been accepted by someone other than its submitter.** `BVA-I311` is still BLOCKED with no comment, and no backend item exists for the pushes it needs.

**If you read nothing else:** 0902 will end Thursday with most of its work submitted and none of it reviewed. The newest mobile work (Activity screen, CallKit) is on a branch whose push half would break iPhone notifications if merged unchanged. The backend fixed a long-standing defect that had made every duplicate-record race return `500` and had written phone numbers to the logs.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The comparison is file-level, against the 9 Oct scratch export in `/tmp/beevia-scratch/0902/`. Only `Status` and `Last Modified` changed. No item was added, removed, re-owned or re-described.

| Status | 9 Oct | 13 Oct | Δ |
|---|---:|---:|---:|
| To do | 2 | 0 | −2 |
| In progress | 7 | 4 | −3 |
| REVIEW/QA | 10 | 15 | +5 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

**All 11 audit entries in the window (UTC).** None fell on the weekend.

| Time | Item | Action | By | Code behind it |
|---|---|---|---|---|
| 12 Oct 14:45:57 | `BVA-I309` *CallKit & ConnectionService Integration* | To do → In progress | David Samuel | `500cdc6` on `origin/BVA-I316`, 13 Oct 14:02 |
| 12 Oct 14:51:30 | `BVA-I307` *Deep Link Routing & Badge Count* | To do → **BLOCKED** | David Samuel | none |
| 12 Oct 16:03:39 | `BVA-I323` (parent) *Chat Background Selection* | In progress → REVIEW/QA | Ayomikun Araoye | — |
| 12 Oct 16:03:39 | `BVA-I324` *Background Swatch Picker & Application* (David's leaf) | In progress → REVIEW/QA | Ayomikun Araoye | `69cf04b`, **unmerged** (`origin/BVA-I306` and `origin/BVA-I316`) |
| 12 Oct 16:03:39 | `BVA-I325` *Chat Background Preference Storage* | In progress → REVIEW/QA | Ayomikun Araoye | **none**: no server change; the client calls a route that does not exist |
| 12 Oct 16:11:58 | `BVA-I312` *In-App Foreground Notification Banners* | In progress → BLOCKED | board administration | — |
| 12 Oct 16:12:01 | `BVA-I312` | BLOCKED → REVIEW/QA (3 s later) | board administration | PR #44 on `main` (foreground display) |
| 12 Oct 16:12:06 | `BVA-I306` *Push Notification Client Integration* | In progress → REVIEW/QA | board administration | PR #44, on `main` since 8 Oct |
| 12 Oct 16:12:18 | `BVA-I316` *Build the Activity Screen* | In progress → BLOCKED | board administration | — |
| 12 Oct 16:12:22 | `BVA-I316` | BLOCKED → REVIEW/QA (4 s later) | board administration | `2aba47a`, **unmerged**, committed 15:54 UTC |
| 13 Oct 09:06:47 | `BVA-I307` | BLOCKED → In progress | David Samuel | none identified; push taps still open Home on every branch |

The BLOCKED-then-REVIEW/QA pairs a few seconds apart are the board's routing pattern, seen on 6 and 9 Oct, not real blocks. `BVA-I307`'s 18 hours in BLOCKED had no comment, so what blocked it and what cleared it are not recorded. **There were no comments, reopens or completions.** A re-export at the end of this edition found nothing after the first cut-off (Method).

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. The 08-01 and 0901-admin activity sidecars are byte-identical to 9 Oct's, and their CSVs differ only in the `Date` preamble line. 0901's last entry is still the 30 Sep sweep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 14

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **4 REVIEW/QA** (`I306`, `I308`, `I310`, `I312`), 3 In progress (`I307`, `I309`, `I313`), **1 BLOCKED** (`I311`) | `I306` and `I312`'s foreground display on `main` (PR #44). `I308`/`I310` server halves on `main` (#64, #65); their client halves wait on `I307`. **`I307`: every push tap still opens Home**, on `main` and on every branch. `I309`: on `origin/BVA-I316` since today, contract mismatch (§3.3). `I313`: no notification-settings screen on any branch. `I311`: the server sends neither push it displays |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, **screen `I316` REVIEW/QA** | Feed on `main` (#66). **Screen on `origin/BVA-I316` only** |
| Appearance (`BVA-I318`–`I329`) | 9 | **all 9 REVIEW/QA** | Theme, palette, typography and settings screen on `main` (PR #43). **`I324`'s chat-background application is on a branch only.** `I319`, `I325` and `I328` have no server code; the client keeps all three on the device, and the branch tries a non-existent route for `I325`'s |
| Carried bug `BVA-I286` | 1 | In progress, **12.9 d** | not identified on any branch |

**Two days remain** (14–15 Oct). Four leaves are in progress and one is blocked. With no estimates, the board cannot say whether any of them fits. The code can say this much: none of `I286`, `I307`, `I311` or `I313` has visible code anywhere, and `I309` needs server work that no item asks for. **Zoho lists no sprint after 0902.**

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-13`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin). They were not acted on. **No spec file changed this edition.** #70 makes the code honour the shared `Conflict` response (`409 unique_constraint_violation`) that `openapi.yaml` already documented.

### 3.1 `beevia-api`: #70, and a defect as old as the project

`origin/main` moved `12d8797` → **`b091cb3`**: one PR, `fix/drizzle-wrapped-pg-errors` (#70). `Phoenixdadhev` committed it on 11 Oct at 23:39 UTC, and Ayomikun merged it on 12 Oct at 16:11 UTC.

`drizzle-orm` has been `^0.45` since the first commit (26 Jun). Since 0.44, Drizzle wraps every failed query in `DrizzleQueryError` and puts the node-postgres error, which carries the SQLSTATE, in `.cause`. Both the global exception filter and `isUniqueViolation()` read `code` off the thrown object, so neither ever matched:

- **29 `isUniqueViolation()` call sites in 15 services never fired.** These include the duplicate-delivery handling in four webhook services (Paystack, Anchor, Entrust, LiveKit), the ledger, wallet provisioning, invites and reactions. Each race they were written for fell through to the generic error path.
- **A uniqueness clash returned `500` instead of `409`.** The same was true of `23503` (foreign key) and `23502` (not null), which should return `400`.
- **Failed-query logs carried every bound parameter.** `DrizzleQueryError`'s message includes the values, so phone numbers, account numbers and amounts went to the log sink, past `redactBody`.

The fix walks the `cause` chain (`findPostgresError`, depth 5) and shares it between the filter and the services. It checks `HttpException` first, so deliberate exceptions keep their meaning, and logs failed queries as `Failed query: <sql> (N params withheld)`. It comes with about 140 lines of new tests. **What it does not fix:** anything already written to the logs before 12 Oct, and `22P02` (malformed uuid), which is still unmapped. With #70 in, mapping `22P02` is one more `case` (`suggestions.md` §1.1, §1.6).

The commit message is one line, `fix: drizzle-wrapped pg error`. The code comment explains the defect thoroughly. Nothing records how it was found, or whether production showed the symptom.

### 3.2 Pipelines

No workflow file changed in any backend repo since 1 Oct. In `beevia-api`'s `release.yml`, `sync` still runs without `needs: test` (the comment at line 29 still gives the hosted-runner reason that no longer applies), and `deploy` needs only `sync`. `beevia-db-schema`'s Release still triggers on push with no verify job, and its Sync follows a successful Release. `beevia-admin-api`'s `sync.yml` (on push) → `deploy.yml` chain is unchanged. **#70 therefore reached production, if it deployed, with nothing waiting on its tests.** No new `beevia-db-schema` tag since `v0.0.40` (9 Oct). `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged.

### 3.3 `beevia-mobile`: three commits on a branch, and a push contract that does not match

`main` is unchanged at `4f9c29f` (PR #44, 8 Oct). The re-checks from earlier editions still hold: no conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`; `ios/GoogleService-Info.plist` still tracked; the biometric step-up option still on `main`.

Remote branches now include **`origin/BVA-I316`** (3 ahead, 2 behind) and **`origin/BVA-I306`** (1 ahead, 2 behind). The second holds only `69cf04b`, which is also the first commit of `BVA-I316`. `BVA-I317`, `update-fixes` and `App-bundle` are fully contained in `main`.

| Commit (UTC) | Item | What it does |
|---|---|---|
| `69cf04b` · 9 Oct 14:29 | `BVA-I324` | The chat screen applies the chosen background (808-line rework of `chat_details.dart`). Saves locally, then `PUT /users/me/appearance/chat-background`, **a placeholder its own `TODO(backend)` says 404s, swallowed silently** |
| `2aba47a` · 12 Oct 15:54 | `BVA-I316` | Activity tab: screen, call-history screen, provider, model, mock route and fixtures, and strings in four languages. `GET /activity` with `X-Device-Id` and cursor. Filter and search are local to loaded pages. The badge comes from the feed response, not from `/activity/unattended-count` |
| `500cdc6` · 13 Oct 14:02 | `BVA-I309` | `flutter_callkit_incoming`; iOS `PKPushRegistry` in `AppDelegate.swift`; `CallKitManager`; VoIP token registration |

**The CallKit contract, in detail** (`api-rfc.md` §5.15):

- **iOS.** The client registers its PushKit token with `POST /notifications/token`, `pushProvider: 'voip'`, for the same `deviceId` as the FCM token. `registerToken()` calls `devices.setPushToken()`, which **overwrites** the single `push_token`/`push_provider` pair on the device row. `FcmPushAdapter.send()` ignores the provider. The iPhone's message, payment and security pushes would then go to FCM addressed to a VoIP token. No APNs VoIP sender exists, so the native call UI could not ring either.
- **Android.** The background handler rings only when `data['type'] == 'call.incoming'` and reads `call_id`, `conversation_id`, `kind` and `initiator_user_id` from a data-only message. `notifyIncomingCall()` sends `data.kind = 'call.incoming'` with `callId`, `conversationId` and `callKind`, plus a `notification` block, so FCM shows its own banner and the handler never runs.

Neither affects anyone until the branch merges. The plain "Incoming call" banner keeps working on both platforms. **No MVP score moves for any of this, because nothing is on `main`.**

### 3.4 `beevia-admin`

No commit since `0b41e35` (22 Sep), 20.9 days ago. `beevia-admin` has no branch other than `main`.

### 3.5 Document changes this cycle

- **`suggestions.md`:** new **§1.6** (resolved: Drizzle-wrapped Postgres errors, #70), with the two loose ends. §1.1 gets a 13 Oct update: the `22P02` backstop could not have worked before #70 and is now one `case`. §8 item 5 gets the same note.
- **`api-rfc.md`:** §5.14 gets a 13 Oct update on the client feed (on a branch; local filter and search; badge source). New **§5.15**: CallKit's VoIP token would overwrite the device's single push-token slot; there is no APNs VoIP sender; the Android call-push keys do not match; and the placeholder chat-background route and `/users/me/settings` as the existing home for it. Nothing was added to `openapi.proposed.yaml`, because appearance is outside the PRD.
- `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin*.yaml`, `admin-api-rfc.md`: unchanged.

---

## 4. Risks

- **Merging `BVA-I316` unchanged would break pushes on iPhones** (§3.3). It is the one risk this week that turns working behaviour into broken behaviour, and it is cheap to avoid before the merge.
- **The review step has no reviewer, and the sprint ends Thursday.** Fifteen leaves are in REVIEW/QA and none has ever left except by bulk sweep. Three of the fifteen are not backed by code on `main`, so a sweep at sprint close would mark unbuilt work Done.
- **No sprint after 0902.** The last gap (0901 → 0902) lasted eight days, with the team moving items inside a closed sprint.
- **PII may be in production logs from before 12 Oct** (failed-query parameters, §3.1). Retention and access to the log sink are not visible here.
- **Every backend repo still deploys or migrates production on push without a test gate.** #70 is the latest change to go out that way.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1).
- **`BVA-I311` is blocked on server work nobody has been asked for.** Unchanged since 9 Oct.
- **Firebase keys sit in a tracked file and in history**, unrestricted as far as can be seen here.
- **Production SSH accepts connections from any address**, per the 1 Oct deploy commits. Unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 20.9 days with no `beevia-admin` commit, 29.0 days with no admin-board activity, no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. CallKit (`I309`) serves PRD calling (rubric line 2), but it is unmerged and cannot ring against the current server. Everything else in 0902 is notification, Activity or Appearance work, none of which is a rubric capability.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 6 Oct 14:04 → 13 Oct 14:04 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners.

### 6.1 Ayomikun Araoye: backend + admin API

**13 commits in 7 days**: 11 in `beevia-api` (#63–#70) and one dependency refresh each in `beevia-admin-api` and `beevia-db-schema`. In this window the work was #70 (§3.1), a cross-cutting fix with tests. On the board, at 16:03 UTC on Monday, they moved the Chat Background parent and both its leaves to REVIEW/QA. One leaf is their own `BVA-I325`, backend storage with no server change behind it. The other is David's `BVA-I324`, whose code is on an unmerged branch. That makes all six of their 0902 leaves in review: three with merged server code (`I308`, `I310`, `I315`), and three "preference storage" items (`I319`, `I325`, `I328`) for settings the client keeps on the device. Median cycle time **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 29.0 days.

### 6.2 David Samuel: mobile

**3 commits on `main` in 7 days** (all 8 Oct, PR #44) **and 3 on `origin/BVA-I316`** (9, 12 and 13 Oct), about 3,900 added lines across 42 files. This is the client half of the Activity tab, the chat background and CallKit (§3.3). On the board they started `BVA-I309` on Monday and committed its first cut today. They moved `BVA-I307` to BLOCKED on Monday and back to In progress this morning, with no comment either time. They hold 15 of 0902's 21 leaves: 10 in REVIEW/QA (six moved there by board administration and three by Ayomikun), 4 In progress and 1 BLOCKED. Their own last submission was `BVA-I329` on 9 Oct. `BVA-I286` has been In progress for **12.9 d** against a 0.98-day median, with no identifiable code. `BVA-I313` (notification settings screen, **5.9 d**) has no screen on any branch. The branch's call-push mismatch is a contract gap between two services that were never written down together (§5.13 of `api-rfc.md` was the first attempt, on 8 Oct). It is not an individual's error.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC. `BVA-I321` has been in REVIEW/QA since 7 Oct, moved there by David. Open WIP is zero. Design work does not land in these repositories, so commits are not applicable.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **20.9 days** ago. The admin board has had no activity for 29.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the eleventh edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (from Mon 12 Oct, 2 days) | — | **5** | 1 | 1 | 3 |

Acceptance is still zero. Over two weeks the team submitted 15 leaves and the review step took none. The bottleneck is not the developers, and three of this week's five submissions were made by board administration, not by the people doing the work.

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more. One branch commit (`2aba47a`, the Activity tab) adds about 2,900 lines and covers one item.
- **Who moved an item is not who did the work, or whether it is done.** `BVA-I316` and `I324` reached review with their code unmerged. `I325` reached it with none.
- **Branch commits are not delivery.** They are counted separately because the rubric and the "code on `main`" checks both ignore them.
- **Commit counts reward small commits.** Two of Ayomikun's thirteen are lockfile refreshes.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. #70's defect existed for the project's whole life (15 weeks) and was invisible to this pipeline throughout, because nothing here executes code.

---

## 7. Previous recommendations: where they stand

| Recommendation from 9 Oct | Status on 13 Oct |
|---|---|
| **1. Name a reviewer and drain the column; move `I306`; close `I319`/`I325`/`I328`** | ◐ **One part.** `I306` moved to REVIEW/QA (by board administration). No reviewer named, nothing left REVIEW/QA, and the column went 10 → 15. `I325` was moved *into* review instead of closed |
| **2. Say what lands by 15 Oct; unblock or move `BVA-I311`; put `I316` and `I307` first** | ◐ **Order followed, scope not stated.** `I316` was built (on a branch) and `I307` started this morning. `I311` is still BLOCKED with no comment and no backend item. `I309` was started rather than moved to the next sprint. No scope statement |
| **3. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done.** `release.yml` unchanged since 1 Oct; #70 deployed ungated |
| **4. Wire the client to the feed with a real device id; point deep links at `reminder`** | ◐ **First half done on a branch.** `ActivityService` sends the real `X-Device-Id` (`origin/BVA-I316`, unmerged). Taps still open Home |
| **5. Validate path-parameter UUIDs** | ❌ **Not done.** #70 makes the `22P02` backstop a one-line change |
| **6. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ❌ / ? Still tracked; key restriction not visible |
| **7. Make Flutter CI a required check; confirm the three Firebase secrets** | ? **Not visible** |
| **8. Check the production host's SSH settings** | ? **Not visible** |
| **9. Hide the biometric option outside mock mode** | ❌ **Not done** (mobile `main` unchanged) |
| **10. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **11. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **12. Carried items** | ❌ **None moved** |

**None of twelve done, three partly.** The partial progress is all mobile work that has not merged.

---

## 8. What I would do this week

Re-ranked for the last two days of 0902 and the gap after it.

1. **Before `BVA-I316` merges, fix or remove the VoIP token registration.** The quickest safe path is to merge the Activity screen and chat background, and hold CallKit back until the server stores a token per `(device, provider)` and has an APNs VoIP sender. Agree the Android `call.incoming` keys in the same conversation, adopting the server's existing contract (`api-rfc.md` §5.13) or changing both sides together.
2. **Review before Thursday, starting with what is on `main`.** Ten of the fifteen leaves have code on `main` or are design: `I306`, `I308`, `I310`, `I312`, `I315`, `I318`, `I321`, `I322`, `I327` and `I329`. Send `I316` and `I324` back to In progress until their branch merges. Close `I319`, `I325` and `I328` with a one-line note that the client stores these on the device, or open one backend item to extend `PATCH /users/me/settings`. Then remove the placeholder route from the client.
3. **Create 0903 before Thursday and decide what carries over.** Likely candidates: `I286`, `I307`, `I309`, `I311`, `I313`. Write the blocker on `I311` and `I307`. Neither has a comment. When 0903 exists, set `ZOHO_SPRINT_FILTER` to it, so the in-repo export stops reading 08-01.
4. **Check the production logs for PII from before 12 Oct** (failed-query parameters, §3.1). Shorten retention or purge if the sink keeps them.
5. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
6. **Map `22P02` to `400` in the exception filter** (`suggestions.md` §1.1). After #70 it is one `case`.
7. **Restrict the Firebase API keys and untrack `ios/GoogleService-Info.plist`** (`suggestions.md` §5.13).
8. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
9. **Check the production host's SSH settings.**
10. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
11. **Bring `payments.dto.ts` onto `phone.util.ts`.**
12. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
13. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 29.0 days ago**. Today's export and sidecar are identical to 9 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 29 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 20.9 days without a commit, and `beevia-admin-api`'s last change is the 8 Oct dependency refresh. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-two days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved.** #70 is a correctness fix, which the rubric excludes (owner, 2026-08-07). The Activity screen and CallKit are on an unmerged branch. CallKit would bear on line 2 once merged and once the server can ring it.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change. #70 is error handling |
| 2 | Voice & video calling | 8 | 0.85 | 0 | CallKit on `origin/BVA-I316` only, and cannot ring against the current server (§3.3) |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change. #70 makes Entrust webhook dedup work, which is correctness |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | No change; biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether #70 is deployed**, or whether production ever showed the `500`s or logged parameters it describes. Deploy state and logs are not visible here.
- **Whether `BVA-I316` builds**, or whether its CallKit plumbing works on a device. No `flutter` command ran. §3.3 is read from code on both sides.
- **What blocked `BVA-I307` for 18 hours, or what blocks `BVA-I311`.** No comment records either.
- **Whether anyone but the author reviewed any PR**, or whether branch protection requires CI on any `main`.
- **The production host's real SSH configuration.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
4. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0), compared against the 9 Oct file there. The three exports ran in parallel at about 14:03 UTC.
5. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
6. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-13`: clean. The in-repo audit was run too, for the board section; its 23 drift lines are the known phantom. Both ran through `uv run --no-project --with pyyaml`.
7. Flow analysis (`flow13.py`): cycle times, the 7-day submission count split by actor, WIP ages and the weekly trend, plus a sweep for comments, reopens and completions in the window (none).
8. Content checks. In `beevia-api`: the whole #70 diff, the filter's mapping table, the `drizzle-orm` version history, the `isUniqueViolation` call sites, `registerToken`/`setPushToken`, `FcmPushAdapter.send`, `notifyIncomingCall`, and a search for any VoIP/APNs or appearance code. In all three backend repos: every workflow's triggers and `needs:`. In `beevia-mobile`: the remote branch list with ahead/behind counts, the full diff of `origin/BVA-I316` and `origin/BVA-I306` against `main`, conflict markers, tracked Firebase files, and push-tap handling.
9. `suggestions.md` and `api-rfc.md` updates (§3.5).
10. A second 0902 export at the end (`/tmp/beevia-scratch/0902-recheck/`), checked for any audit entry after the first cut-off.
11. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive` and read-only `log`/`show`/`diff`/`grep`/`branch`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-13.html`, `web-report/index.html`, `api-rfc.md`, `suggestions.md`, plus new board exports for 13 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 9 Oct 14:10 UTC → 13 Oct 14:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
