# Beevia — Project Status

**As of 2026-10-09** · Sprint **0902** (30 Sep → 15 Oct): **day 10 of 16, 25 items, 2 leaves To do · 7 In progress · 10 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-09.csv` + `beevia-activity-2026-10-09.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-09.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 8 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`. `beevia-admin` and `beevia-mobile` were read in the working tree. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 8 Oct 14:05 UTC → 9 Oct 14:10 UTC, 1.0 day** (Thursday afternoon to Friday afternoon in Lagos).

---

## Quick overview

> **The backend built the server half of three 0902 items in one afternoon, and its owner put all three in review. Those are the first submissions of an owner's own items in eleven days. At 14:07 UTC today David moved a fourth item, already built, into review, and marked another BLOCKED with no comment, the first 0902 item to stay there. The review column now holds 10 leaves, nothing has ever left it, and six calendar days remain.** `beevia-api` merged the Activity feed (#66, `BVA-I315`), payment reminders (#65, `BVA-I310`) and a fix that stops new-message pushes being dropped for a backgrounded app (#64, `BVA-I308`) between 15:11 and 15:57 UTC on 8 Oct. Ayomikun moved the three items to REVIEW/QA in the same window. The feed was being called in production within a day. It returned `500` on a malformed `X-Device-Id`, and #69 fixed that this morning. A test on the feed also failed on `main` while the same commit deployed. That is the first time the missing test gate has mattered in practice.

**Correction to the 6–8 Oct editions.** Those three editions said `BVA-I315`'s acceptance criteria asked for "server-side message previews, which E2EE rules out", and the last two recommended rewriting them before more work went in. **That was wrong.** The criterion asks for "last message text", and #66 meets it without the server reading anything. Each chat row carries the last message as *ciphertext for the calling device*, the same mechanism `GET /conversations` already used, and the client decrypts it. The recommendation is withdrawn (§7, rec 3).

| Metric | 8 Oct | 9 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 4 / 10 / 6 / 0 / 1 | **2 / 7 / 10 / 1 / 1** | 4 → QA, 1 → BLOCKED |
| Board actions in the window (all boards) | 10 | **6** | 3 by Ayomikun (→ REVIEW/QA), 3 by David (`I329` → BLOCKED → REVIEW/QA, `I311` → BLOCKED) |
| Transitions into REVIEW/QA, last 7 days (leaves) | 6 | **10** | 5 by board administration, 1 by David (Philip's leaf), **4 by their owner** (3 Ayomikun, 1 David) |
| Owners' last submission of their *own* leaf | 28 Sep (10.0 d) | **9 Oct 14:07 UTC (David, `I329`)**; Ayomikun 8 Oct 15:43 UTC | first in 11 days |
| Items that left REVIEW/QA in the window | 0 | **0** | never, apart from the two bulk sweeps |
| 0902 leaves whose code is on `main` but whose item is not in REVIEW/QA | 2 | **1** | `BVA-I306` (In progress). `BVA-I329` moved to REVIEW/QA at 14:07 UTC |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | a red test on `main` deployed (§3.2) |
| API surface (consumer / admin) | 137 / 49 | **139** / 49 | **+2**: `GET /activity`, `GET /activity/unattended-count` |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** after this edition's spec update (2 found) | |
| `beevia-mobile` days since a commit on `main` | 0.1 | **1.1** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 / 0.3 / 0.3 | **0.0 / 1.3 / 1.3** | db-schema release bot 9 Oct 10:46 UTC |
| `beevia-admin` days since a commit | 15.9 | **16.9** | |
| Admin board: open sprint / days since any activity | none / 24.0 | **none / 25.0** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: the feed and reminders are server-only, outside or below the rubric's lines |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6** (5 REVIEW/QA, 1 In progress) · 0901-admin: 1 In progress | 5 (**3 own**, 2 by board administration) | 0.99 d (n=15) | `BVA-I325` (1.2 d, started by David's parent move) · `BVA-I8` on 0901-admin (**25.0 d**) | **12** (api 10, admin-api 1, db-schema 1) | Three server halves merged with tests and submitted the same afternoon. `BVA-I325` describes storage the client does on the device |
| David Samuel | mobile | **0902: 15** (6 In progress, 6 REVIEW/QA, 2 To do, 1 BLOCKED) | 6 (**1 own**, 3 by board administration, **2 by Ayomikun** on co-assigned `I308`/`I310`) | 0.97 d (n=29) | **6 leaves.** `BVA-I286` (**8.9 d**) · `I306`, `I312` (2.9 d, started by board administration) · `I313`, `I316` (1.9 d) · `I324` (1.2 d) | **4** | Moved `BVA-I329` to REVIEW/QA (code on `main` since PR #43) and `BVA-I311` to BLOCKED, with no comment. No commit. `BVA-I316` (Activity screen) now has its API. `BVA-I306` is still In progress with its code merged |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 1 (moved by David, via parent) | 0.99 d (n=3) | none | n/a | — |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**25.0 d**) | **0** | `beevia-admin` **16.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **Who reviews, starting today?** Ten leaves wait in REVIEW/QA. Five can be checked against a merged PR in minutes: `BVA-I308` (#64), `I310` (#65), `I315` (#66), `I329` (PR #43), and `I306` (PR #44), which is still In progress. (2) **What is `BVA-I311` blocked on?** No comment says. The code suggests an answer: neither service sends an account-status or verification-result push, and no 0902 item asks for one (§1.1). (3) **What lands by 15 Oct?** Seven leaves are in progress, two untouched, one blocked, none estimated, and six calendar days remain. The Activity screen (`BVA-I316`) and deep links (`BVA-I307`) are what turn this week's server work into something a user sees.

**The three things worth knowing:**

1. **Three server halves of 0902 shipped, each with tests, and the Activity feed treats E2EE correctly.** #66 adds `GET /activity`: chats, calls and payments in one list, keyset-paginated, with `requires_attention` per row and an `unattended_count` badge that ignores filters. Search covers names and payment notes only, and the operation says why. #65 adds the payment `reminder` push at half the 24 h hold and one hour before it ends, on the existing escrow-expiry queue. That is the shape the 7 and 8 Oct editions recommended. #64 narrows new-message push suppression from "has any socket open" to "has *this* conversation open". That was the bug behind missed message notifications for a backgrounded app. #68 restores two integration docs to `beevia-api/docs/`, including the payment push contract. **No client calls the feed yet**, and every notification tap still opens Home. Both routes are now in `openapi.yaml`, and the route audit is clean at 139.

2. **Review is now the whole bottleneck.** In-progress work fell from 10 to 7 because work finished, not because scope was cut. Ayomikun's three moves were the first an owner had made since 28 Sep, and David added `BVA-I329` (Appearance screen, on `main` since 7 Oct) at 14:07 UTC today. The review column grew from 6 to 10, and **apart from the two bulk sweeps (3 Sep and 30 Sep), no item on any board has ever been accepted by someone other than its submitter.** Two of the new entries are co-assigned with David, and their client halves depend on `BVA-I307` (deep links, To do), as their descriptions say. The board still trails the code in both directions: `BVA-I306` is In progress with merged code, and `I319`, `I325` and `I328` describe server storage the client does not use. `BVA-I311` is the first 0902 item to stay BLOCKED. It is the client half of pushes the server does not send, and no backend item exists for them.

3. **The missing test gate mattered for the first time.** By its own message, `d9bb38b` (#67) fixed a test that "passed on the PR and failed on main". In `beevia-api`'s `release.yml`, `test` runs *beside* `sync` → `deploy`, so the red run did not stop the feed reaching production. The failure was a fixture timing race, so no product bug shipped because of it. Separately, production returned `500` on `GET /activity`. A literal `{{device_id}}` from an unresolved Postman variable reached a uuid cast. #69 now rejects any non-UUID `X-Device-Id` with `400 device_id_invalid` on all seven routes that read it. The same class of `500` is still reachable through path parameters (`suggestions.md` §1.1). `beevia-db-schema`'s stalled Release finally published `v0.0.40` at 10:46 UTC today, about 27 hours after the merge. The workflow is unchanged, which suggests a manual re-run.

**If you read nothing else:** the backend finished its share of 0902's notification and Activity work, and submitted it. The bottleneck is now entirely review, which nobody performs, and the mobile client halves, with six days left. The feed's E2EE design is sound, and this report was wrong to call its criteria unbuildable.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The comparison is file-level, against the 8 Oct scratch export in `/tmp/beevia-scratch/0902/`. The only fields that changed are `Status` and `Last Modified` on five items. No item was added, removed, re-owned or re-described.

| Status | 8 Oct | 9 Oct | Δ |
|---|---:|---:|---:|
| To do | 4 | 2 | −2 |
| In progress | 10 | 7 | −3 |
| REVIEW/QA | 6 | 10 | +4 |
| BLOCKED | 0 | 1 | +1 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

**All 6 audit entries in the window (UTC):**

| Time | Item | Action | By | Code behind it |
|---|---|---|---|---|
| 8 Oct 15:25:53 | `BVA-I308` *New Message Notification Handling* (co-assigned David) | In progress → REVIEW/QA | Ayomikun Araoye | #64, merged 15:11 UTC |
| 8 Oct 15:26:10 | `BVA-I310` *Money Notification Handling* (co-assigned David) | In progress → REVIEW/QA | Ayomikun Araoye | #65, merged 15:20 UTC |
| 8 Oct 15:43:46 | `BVA-I315` *Activity Feed Backend* | In progress → REVIEW/QA | Ayomikun Araoye | #66, merged 15:57 UTC (14 min later) |
| 9 Oct 14:03:36 | `BVA-I311` *Account & Verification Status Notification Handling* | To do → **BLOCKED** | David Samuel | none; see below |
| 9 Oct 14:07:20 | `BVA-I329` *Appearance Settings Screen* | To do → BLOCKED | David Samuel | — |
| 9 Oct 14:07:25 | `BVA-I329` | BLOCKED → REVIEW/QA (5 s later) | David Samuel | PR #43, merged 7 Oct |

Ayomikun's three arrived after the 8 Oct edition's 14:05 UTC cut-off. Each took just under a day from start (7 Oct 16:03–16:05 UTC) to review. David's three came between 14:03 and 14:07 UTC today, just after this morning's first export at 14:02 UTC, and were caught by a re-export at 14:10 UTC. `BVA-I329` passed through BLOCKED for five seconds. `I326`–`I328` did exactly the same in the 6 Oct batch, so this is probably how the board routes a To do item to review, not a real block. It never entered In progress, so it has no cycle time. **There were no starts, comments, reopens or completions.**

**`BVA-I311` is blocked, and the code shows why it could be.** The item asks the client to display two pushes: account status changed (restricted, suspended, reactivated) and verification result (verified, failed), each deep-linking to its screen. **Neither push exists on the server.** `beevia-api`'s `NotificationService` sends message, call, payment and security pushes only. The KYC paths (`kyc.service.ts`, `bvn-lookup.service.ts`, `entrust-webhook.service.ts`) alert an operations Slack channel, not the user. `beevia-admin-api`'s user actions change `users.status` without notifying anyone. No 0902 item asks the backend for either push. This is an inference from the code. The board carries no comment saying what the blocker is. Every 0902 item still has a blank Epic and 0 estimation points.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC). The 0901-admin and 08-01 sidecars are byte-identical to 8 Oct's, and their CSVs differ only in the `Date` preamble line. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 10

| Block | Leaves | State | Code on `main` |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **2 REVIEW/QA** (`I308`, `I310`), 3 In progress (`I306`, `I312`, `I313`), 2 To do (`I307`, `I309`), **1 BLOCKED** (`I311`) | `I306` complete (PR #44). **`I308`'s server suppression fix and `I310`'s reminder schedule are on `main`** (#64, #65). On the client, both still depend on `I307`'s deep links, as their descriptions say. Foreground pushes already display (`I312`, partial). `I313`'s settings screen is not on `main`. **`I311` has no server push to display** (§1.1) |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, **backend `I315` REVIEW/QA**, screen `I316` In progress (1.9 d) | **Feed and badge endpoints on `main`** (#66, §3.1). No Activity screen in `beevia-mobile` and no call to `/activity` |
| Appearance (`BVA-I318`–`I329`) | 9 | 7 REVIEW/QA (`I329` since 14:07 UTC today), 2 In progress (`I324`, `I325`) | On `main` since PR #43, stored on the device. The chat screen still does not read the chosen background (`I324`) |
| Carried bug `BVA-I286` | 1 | In progress, **8.9 d** | not identified on any branch |

**The board and the code still disagree in both directions:**

- **Behind the code:** `BVA-I306` (In progress, code merged 8 Oct). `BVA-I329` caught up at 14:07 UTC today.
- **Ahead of the code:** `BVA-I319`, `I328` (REVIEW/QA) and `I325` (In progress). All three describe backend storage for preferences the client keeps on the device.

**Six calendar days remain** (10–15 Oct). Seven leaves are in progress, two untouched and one blocked. Without estimates, nothing here can say whether that fits. The board does show where the dependency sits now. The server side of every open 0902 block is done or not needed, **except `BVA-I311`'s**. What remains is client work (`I307`, `I309`, `I312`, `I313`, `I316`, `I324`, `I286`), `I311`'s missing server pushes, and review.

---

## 3. Code, API surface and spec drift

**Audit: two real drift lines, fixed in this edition.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-09`), `beevia-api` showed code 139 / spec 137: `GET /activity` and `GET /activity/unattended-count` were undocumented. Both are now in `openapi.yaml`, read from the controller, its Zod DTO and its view types. The re-run is clean: `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees (now 8 consumer + 15 admin, because the stale tree also lacks the two new routes). They were not acted on.

### 3.1 `beevia-api`: six PRs in 24 hours

`origin/main` moved `c145d6e` → **`12d8797`**. All commits are `Phoenixdadhev`; all merges are Ayomikun's.

| PR | Merged (UTC) | Item | What it does |
|---|---|---|---|
| #64 `fix/notify-open-conversation` | 8 Oct 15:11 | `BVA-I308` | Suppresses a new-message push only when the recipient has *that* conversation's room joined (`RealtimeService.isUserInConversation`, Redis-backed), not whenever any socket is open. A backgrounded app keeps its socket, so its pushes had been silently dropped. The spec had no notification assertions; it now covers four cases |
| #65 `feat/payment-pending-reminders` | 8 Oct 15:20 | `BVA-I310` | `payment.update` with `event: reminder`, at half the hold TTL and one hour before expiry, to whoever still has to act. Rides the escrow-expiry queue, re-reads the payment and stays silent once it is resolved. The stage reaches only the dedupe key, so the two pushes are identical. The category follows the payment type (`moneyReceived` / `moneyRequests`) |
| #66 `feat/activity-feed` | 8 Oct 15:57 | `BVA-I315` | `GET /activity` and `GET /activity/unattended-count`: 858-line service, 850 lines of unit and integration tests. Keyset cursor; `filter` = `all`/`chats`/`calls`/`payments`; `search` on names and payment notes only |
| #67 `fix/activity-int-spec-flake` | 9 Oct 10:48 | — | Pins a fixture's `joined_at`. A millisecond/microsecond race made an unread-count test pass on the PR and **fail on `main`** |
| #68 `docs/money-in-chat` | 9 Oct 10:53 | — | Restores `docs/money-in-chat.md` and `docs/mobile-chat-integration.md`, which were written on branches after their PRs merged and never reached `main`. Adds the payment push contract and the reminder schedule. Flags the five docs `081441c` deleted on 18 Sep, and leaves them out because they are unverified |
| #69 `fix/device-id-must-be-uuid` | 9 Oct 13:12 | — | A non-UUID `X-Device-Id` now gets `400 device_id_invalid` instead of a `500` from the uuid cast. The trigger was production: `GET /activity` received a literal `{{device_id}}` |

**On E2EE.** The feed's chat preview is `last_message`, the same `Message` shape as the inbox, with `ciphertext` resolved for the device in `X-Device-Id`. The server reads nothing. Search excludes message text explicitly. This is the right design, and it is why the correction at the top of this report is needed. `api-rfc.md` §5.14 records it.

**Spec changes this edition (`openapi.yaml`):** the new `Activity` tag; `listActivity` and `getUnattendedActivityCount`; schemas `ActivityFeed`, `ActivityItem` and three preview variants (discriminated on `kind`); and `DeviceIdHeader` now documents `device_id_invalid`.

### 3.2 Pipelines

- **`beevia-api`:** `release.yml` runs `test` as its own job. `sync` does not wait for it (the comment at line 29 still says to restore the gate "when hosted runners are back", which they have been since 1 Oct), and `deploy` needs only `sync`. #67's message is the first direct evidence of what that costs: a red test on `main`, while the same commit deployed and was then called in production. It did no harm this time.
- **`beevia-db-schema`:** `v0.0.40` was tagged at 10:46 UTC today by the release bot, about 27 hours after #21 merged. `release.yml` is unchanged and has a `workflow_dispatch` trigger, so a manual re-run is the likely explanation. Why the first run stalled is still not visible. Release still triggers on push with no verify job, and Sync follows a successful Release.
- **`beevia-admin-api`:** no change since #21 (8 Oct). Its `sync.yml` (on push) → `deploy.yml` chain is unchanged.

`PaymentService.activeNgn()`, `StubTranslateAdapter` and `payments.dto.ts`'s unparsed `phone` are unchanged.

### 3.3 `beevia-mobile` and `beevia-admin`

No commit on either `main` in the window. `beevia-mobile` is at `4f9c29f` (PR #44), on `main`, clean, with no new remote branches. Every mobile check from 8 Oct still holds: `ios/GoogleService-Info.plist` is still tracked, the biometric step-up at `wallet_service.dart:78` is unchanged, there are no conflict markers, and `X-Device-Id` is sent on all six #60 routes. The client sends a real device UUID on those routes, so #69 does not affect it. `beevia-admin` is at `0b41e35` (22 Sep).

### 3.4 Document changes this cycle

- **`openapi.yaml`:** +2 operations, +5 schemas, one tag, and `DeviceIdHeader` updated (§3.1).
- **`api-rfc.md`:** header and §3 counts 137 → 139, with an Activity row in §3. §5.13 gets a 9 Oct update: the `reminder` event, open-conversation suppression and the restored money doc. New §5.14 covers the feed's E2EE preview, keyset pagination and `device_id_invalid`. §6.8 gets the two routes.
- **`suggestions.md`:** §7.7 gets a 9 Oct update (red test on `main` deployed; db-schema `v0.0.40` 27 h late). §5.9 gets a 9 Oct update (two docs restored, five still gone). §8 items 3g and 5 get notes.
- `openapi.proposed.yaml`, `openapi.admin*.yaml`, `admin-api-rfc.md`: unchanged.

---

## 4. Risks

- **Every backend repo still deploys or migrates production on push without a test gate.** This week there is a concrete case: a test failed on `beevia-api` `main` and the same commit was live and being called within the day.
- **The review step has no reviewer.** Ten leaves are in REVIEW/QA (six for 2.9 days or more, counting `I321` at 1.9), and none has left. The team is submitting again, so the queue will now grow at the rate work finishes.
- **`BVA-I311` is blocked on server work nobody has been asked for.** Account-status and verification-result pushes do not exist in either service, and no 0902 item covers them.
- **The client half of 0902 is the critical path, with six days left.** The Activity screen, deep links, notification settings and CallKit are all mobile and all open or untouched. One person holds six in-progress leaves.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1). #69 closed the header route to that error, not the general one.
- **Firebase keys sit in a tracked file and in history**, unrestricted as far as can be seen here.
- **Production SSH accepts connections from any address**, per the 1 Oct deploy commits. Unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 16.9 days with no `beevia-admin` commit, 25.0 days with no board activity, no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. The payment reminder is the first 0902 change that serves an MVP flow directly: PRD §10.2, Transfer Acceptance & Escrow, which asks the counterparty to act inside the 24 h window. It is server-only for now. The Activity feed is a PRD-adjacent convenience surface, not a rubric capability.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 2 Oct 14:10 → 9 Oct 14:10 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners.

### 6.1 Ayomikun Araoye: backend + admin API

**12 commits in 7 days**: 10 in `beevia-api`, and one dependency refresh each in `beevia-admin-api` and `beevia-db-schema`. They also merged all nine backend PRs. The window's work is described in §3.1. Each change carries tests and a commit message that names the cause, the alternative rejected and the residual gap. For example, #68's message points out the five still-missing docs instead of quietly skipping them. On the board they submitted `BVA-I308`, `I310` and `I315` themselves, each a little under a day after starting it. Their median cycle time is **0.99 d (n=15)**. Five of their six 0902 leaves are now in REVIEW/QA. The sixth, `BVA-I325`, was started by David's parent move and describes storage the client does on the device. `BVA-I8` has been In progress on the admin board for 25.0 days.

### 6.2 David Samuel: mobile

**4 commits on `main` in 7 days**, plus the PR #43 and #44 merges. No commit in this window. On the board, at 14:03–14:07 UTC today, they moved `BVA-I329` to REVIEW/QA, bringing the board into line with code merged on 7 Oct, and marked `BVA-I311` BLOCKED with no comment (§1.1). They hold 15 of 0902's 21 leaves: **6 In progress**, 6 in REVIEW/QA (two reached it through Ayomikun's moves on co-assigned items), 2 To do and 1 BLOCKED. `BVA-I286` (profile-screen UI mismatch) has been In progress for **8.9 d** against a 0.97-day median and has no identifiable code. It remains the one WIP item that looks stuck. The rest of 0902 now runs through this repo. `BVA-I316` has an API to call as of yesterday afternoon, and `BVA-I307` unblocks the client side of two items already in review. Raise it at standup as a capacity question, not as a judgement of effort.

### 6.3 Philip Chidera: design

No board action of their own since 2 Oct 14:18 UTC. `BVA-I321` has been in REVIEW/QA for 1.9 days. Their open WIP is zero. Design work does not land in these repositories, so commits are not applicable.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **16.9 days** ago. The admin board has had no activity for 25.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the tenth edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W37 | 7 | — | | | |
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (from Mon 5 Oct) | — | **10** | **4** | 1 | 5 |

Acceptance is still zero. Output is no longer the question: this week the owners submitted work, and three features reached `main` on the client side and three on the server side. Review is not a step anyone on the team performs on the board.

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more. #66 is about 1,900 lines including tests, and it is one item.
- **Who moved an item is not who did the work.** Two of David's six submissions this week are Ayomikun's moves on co-assigned items, and the client half of each is not done. `BVA-I329`'s move is a status catching up with code merged two days earlier.
- **A parent's cascade is not a start.** `BVA-I325` was started by David's move on `BVA-I323`.
- **Commit counts reward small commits.** Two of Ayomikun's twelve are lockfile refreshes and one is a test fixture.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The production `500` is known only because a commit message reported it.

---

## 7. Previous recommendations: where they stand

| Recommendation from 8 Oct | Status on 9 Oct |
|---|---|
| **1. Decide 0902's scope; stop starting new items until something finishes** | ◐ **Half.** Nothing new was started, and three items finished into review. No scope statement or estimate was written |
| **2. Name a reviewer and drain the column; move `I306`; close `I319`/`I325`/`I328`; move `I329`** | ◐ **One part.** `I329` moved to REVIEW/QA at 14:07 UTC. Nothing left REVIEW/QA, and the column went 6 → 10. `I306` is still In progress |
| **3. Rewrite `BVA-I315`'s preview criterion for E2EE** | ✅ **Withdrawn: it was based on a wrong reading.** #66 meets the criterion with per-device ciphertext, and the server reads nothing (see the correction at the top) |
| **4. Write the push payload down where the client reads it; scope `BVA-I310`'s server half** | ✅ **Largely done.** #65 adds the `reminder` event at half the TTL and one hour before expiry, on the escrow-expiry queue, as suggested. #68's `docs/money-in-chat.md` documents every payment push. The `chat.message` and `call.incoming` keys are still documented only in `api-rfc.md` §5.13 |
| **5. Find out why db-schema's Release stalled; put `needs: test` back on `beevia-api`'s `sync`; gate the other two** | ◐ **`v0.0.40` published 9 Oct 10:46 UTC**, cause still unknown. No gate restored. A red test on `main` deployed this week |
| **6. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ❌ / ? The file is still tracked, and key restriction is not visible from here |
| **7. Make Flutter CI a required check; confirm the three Firebase secrets** | ? **Not visible** |
| **8. Check the production host's SSH settings** | ? **Not visible** |
| **9. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **10. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** #65 changed `payment.service.ts`, not the DTO |
| **11. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **12. Carried items** | ◐ **One part moved:** `beevia-api/docs/` is partly restored (2 docs back, 5 still deleted, `encryption-model.md` among them). The rest did not move |

**Two of twelve done, four partly.** For the first time in this sprint, both items that closed were backend recommendations closed by backend work.

---

## 8. What I would do this week

Re-ranked for the last six days of 0902. Review leads because it is now the only thing between finished work and Done.

1. **Name a reviewer today and drain the column.** Start with the four items each backed by one merged PR: `BVA-I308` (#64), `I310` (#65), `I315` (#66) and `I306` (PR #44, move it to REVIEW/QA first). Add `I329` (PR #43), now in the column. Close `BVA-I319`, `I325` and `I328` with a one-line comment recording device storage.
2. **Say what lands by 15 Oct, and unblock or move `BVA-I311`.** Seven leaves are in progress, two untouched and one blocked. Apart from `I311`, all of the remaining work is mobile. `I311` needs account-status and verification-result pushes that neither service sends. Either open a backend item for them now, or move `I311` to the next sprint. Whichever is chosen, write the blocker on the item. Put `BVA-I316` (Activity screen, the API now exists) and `BVA-I307` (deep links, which `I308` and `I310` depend on) first. Say which of `I309` (CallKit) and `I311` move to the next sprint.
3. **Put `needs: test` back on `beevia-api`'s `sync`.** The condition its comment names was met on 1 Oct, and this week a red test on `main` deployed (`suggestions.md` §7.7). Give db-schema's Release and admin-api's Sync a verify job too.
4. **Wire the client to the feed with a real device id.** `GET /activity` requires `X-Device-Id` as a UUID, the same value the chat routes already send. Point the deep-link work at `payment.update` / `reminder` in `docs/money-in-chat.md`.
5. **Validate path-parameter UUIDs (§1.1).** #69 fixed this week's production `500` for one header. The same failure is still reachable through every `:id`.
6. **Restrict the Firebase API keys and untrack `ios/GoogleService-Info.plist`** (`suggestions.md` §5.13).
7. **Make Flutter CI a required check on mobile `main`**, and confirm the three Firebase secrets are set.
8. **Check the production host's SSH settings**: `PasswordAuthentication no`, root login off, and rate limiting.
9. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
10. **Bring `payments.dto.ts` onto `phone.util.ts`.**
11. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
12. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 25.0 days ago**. Today's export and sidecar are identical to 8 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 25 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 16.9 days without a commit. `beevia-admin-api`'s last change is the 8 Oct dependency refresh, and its last code change was 24 Sep. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed thirty-eight days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance, and not whether `main` compiles.

**No score moved.** The Activity feed is not one of the rubric's eleven capabilities. The payment reminder belongs to line 7, which stays at 0.92. Its remaining gap is the client's biometric step-up, which the real API rejects, and the reminder has no client handling yet. The `X-Device-Id` fix hardens line 1 but adds no capability.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | #64 fixes dropped message pushes; #69 turns a malformed device id into a `400`. No crypto, key or socket-protocol change |
| 2 | Voice & video calling | 8 | 0.85 | 0 | Calls now appear in the Activity feed. No call-screen change |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | **#65: pending-transfer reminders on the server** (PRD §10.2). Client handling none yet; biometric option still rejected by `stepUpSchema` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the Activity feed or reminders work in production**, beyond the one `500` a commit message reported. Deploy outcomes and logs are not visible here.
- **Why `beevia-db-schema`'s first 8 Oct Release run stalled**, and whether `v0.0.40` came from a manual re-run.
- **Whether `beevia-api`'s `main` run is green now.** #67 says it failed before the fix. CI results return `404` to this workspace.
- **Whether mobile `main` builds.** No `flutter` command ran.
- **Whether anyone but the author reviewed any PR in the window**, or whether any check was required before merge.
- **Whether branch protection requires CI on any `main`.**
- **The production host's real SSH configuration.**
- **What `BVA-I311` is blocked on.** No comment records it. §1.1's missing-push explanation is read from the code, not stated by anyone.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
2. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
3. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0), diffed field by field against the 8 Oct file there. **All three exports were re-run at 14:10 UTC**, because an earlier pass of this edition had exported at 14:02 UTC and the report draft lacked a web edition. The re-run caught three 0902 moves made at 14:03–14:07 UTC, and this report includes them. The 08-01 and 0901-admin results were unchanged. The sync and the shadow audit were also re-run: no new commits, still clean.
4. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
5. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
6. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-09`. It found 2 undocumented routes, which were added to `openapi.yaml` from the controller, DTO and view types. The re-run was clean. The in-repo audit was run too, for the board section and the RFC count check. Its 23 drift lines are the known phantom. Both ran through `uv run --no-project --with pyyaml`.
7. File comparison of every export and sidecar against 8 Oct: 08-01 and 0901-admin identical, 0902 changed on three items. The flow script (`flow09.py`) re-derived cycle times, the 7-day submission count split by actor, WIP and queue ages, and the weekly trend.
8. Content checks in the backend shadow: the full diff `c145d6e..12d8797` in `beevia-api` (activity controller, DTO, views and cursor decoding; device-id decorator; notification service; escrow-expiry producer), the whole `release.yml`/`test.yml`/`pr.yml` in `beevia-api`, `release.yml`/`sync.yml` in `beevia-db-schema` and the admin-api chain, `git ls-remote --tags` for `v0.0.40`, and a count of `@DeviceId()` routes. In `beevia-mobile`: remote branch list, and a grep for any `/activity` call or Activity screen.
9. `openapi.yaml`, `api-rfc.md` and `suggestions.md` updates (§3.4).
10. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive`, `ls-remote`, and read-only `log`/`show`/`diff`/`branch`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-09.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 9 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`, which leaves nothing installed.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.** The production `500` and the failed `main` test are known only from commit messages.
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 8 Oct 14:05 UTC → 9 Oct 14:10 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
