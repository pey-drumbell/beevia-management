# Beevia — Project Status

**As of 2026-10-20** · Sprint **0902** (30 Sep → 15 Oct): **ended five days ago, not closed, no successor. 25 items, 0 leaves To do · 1 In progress · 18 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-20.csv` + `beevia-activity-2026-10-20.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-20.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 19 Oct file in the same folder; the 19 Oct scratch export of sprint **0901 (76 items, closed and static)** in `/tmp/beevia-scratch/0901/`, for cycle times. All five repos were read at `origin/main`, along with `beevia-api`'s open ring-expiry PR (#75, re-pushed as #76 during the run). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 19 Oct 14:02 UTC → 20 Oct 14:02 UTC, 1.0 day (Mon → Tue).**

---

## Quick overview

> **The two call defects this report has flagged since 13 Oct are now on mobile `main`. PR #49 merged `BVA-I316` unchanged at 14:30 UTC yesterday, 28 minutes after the last edition's cut-off. Two hours later `beevia-api` made the incoming-call push silent. On iOS, that removes the only alert a backgrounded iPhone used to get for a call.** Read together, the code says a backgrounded or killed iPhone on a build from `main` now gets nothing for an incoming call, and may stop getting pushes of any kind once the VoIP token overwrites its FCM token. That is a code reading; nothing was built or run. On Android the same server change completes the native ring path, with the caller's name. Nothing moved on any board: 0902 is five days past its end with 18 of 21 leaves in review.

| Metric | 19 Oct | 20 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 0 / 1 / 18 / 1 / 1 | **0 / 1 / 18 / 1 / 1** | none. The 0902 sidecar is byte-identical to 19 Oct's |
| Board actions in the window (all boards) | 0 | **0** | last action 15 Oct 16:05 UTC, **4.9 days** ago |
| Transitions into REVIEW/QA, last 7 days (leaves) | 8 | **3** | 1 by the leaf's owner (`I286`), **2 by board administration** (`I307`, `I313`). Five 12 Oct moves left the window |
| Owners' last submission of their *own* leaf | 14 Oct 16:01 UTC (David, `I286`) | 14 Oct 16:01 UTC (David, `I286`) | **5.9 days** ago |
| Items that left REVIEW/QA in the window | 0 | **0** | nothing has left review since 0902 opened 20.6 days ago, apart from the two bulk sweeps on older sprints |
| 0902 leaves in REVIEW/QA whose code is not (fully) on `main` | 5 | **2** | PR #49 brought `I307`, `I316` and `I324`'s client code to `main`. Left: `I325` (no server code anywhere) and `I286` (rename still missing) |
| Call defects from §3 now live on mobile `main` | 0 (branch only) | **3** | VoIP token registration, no `call.ended` handler, white-tinted light-mode mic |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #73 and #74 went out that way |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 5 call/activity operation descriptions updated in place (§3.4) |
| `beevia-mobile` days since a commit on `main` | 11.1 | **1.0** | PR #49 merge, 19 Oct 14:30 UTC |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 3.9 / 11.3 / 10.1 | **0.9 / 12.3 / 11.1** | `beevia-api` #73 and #74, 19 Oct; ring-expiry PR open since this morning (#75, re-pushed as #76) |
| `beevia-admin` days since a commit | 26.9 | **27.9** | |
| Admin board: open sprint / days since any activity | none / 35.0 | **none / 36.0** | |
| Successor sprint to 0902 in Zoho | none | **none** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | 0/25 · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0. Line 2 held: Android gained, iOS lost (appendix) |

**No correction to 19 Oct.** Its two forward-looking risks both came true within three hours of its cut-off: PR #49 merged as it stood, and the server work it asked for (`callerName`) shipped together with a change it did not foresee (the silent ring).

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | **0** (`I325`, 12 Oct, left the window) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**36.0 d**) | **8** (all `beevia-api`) | #73/#74 shipped yesterday, #76 (ex-#75) open today. None has a board item. The silent ring needs an iOS answer (§3.2) |
| David Samuel | mobile | **0902: 15** (13 REVIEW/QA, 1 In progress, 1 BLOCKED) | 3 (**1 own**, **2 by board administration**) | 0.99 d (n=36) | `I309` (**8.0 d**, past their median) | **3 on `main`** (via PR #49) · 0 unmerged | `I309`'s code is now on `main`, with the VoIP registration and without the `call.ended` handler |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 0 | 0.99 d (n=3) | none | n/a | No board action since 2 Oct (18.0 d) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**36.0 d**) | **0** | `beevia-admin` **27.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **Is any iPhone running a build from today's `main`?** If so, the VoIP registration is probably pruning its push token, and a one-line client change (stop calling `syncVoipTokenIfAvailable`) should go out before anything else (§3.2). (2) **What should a backgrounded iPhone get for a call?** Since #74 the answer is nothing. Either the server grows an APNs VoIP sender with a second token slot, or `call.incoming` carries an iOS-only alert until it does. (3) **Who reviews 0902, and is there a 0903?** The review step has taken nothing since 30 Sep. PR #49's merge moved three more review items' code onto `main`, so most of the queue is now checkable.

**The three things worth knowing:**

1. **PR #49 merged exactly as the last edition described it.** The merge commit `31a77e8` (19 Oct 14:30 UTC) has the same tree as the branch tip `8b267ed`, so nothing was changed at merge time. The good half: `main` now has the Activity screen (`I316`), push tap routing (`I307`), chat-background application (`I324`), CallKit (`I309`) and the dark-mode fixes for `I322`. The iOS Firebase plist is untracked, and the foreground duplicate call banner is gone. The other half: `main` now registers the PushKit token with `pushProvider: 'voip'` on every socket connect (`call_kit_manager.dart:80`) and handles no `call.ended` push. The light-mode mic is drawn with `color: Colors.white` (`chat_widgets.dart:1103`), which by the last edition's reading blanks it to a white square. Who reviewed the PR is not visible from git.

2. **The server shipped three things the client does not consume yet.** `beevia-api` #74 (19 Oct 16:51 UTC) makes `call.incoming` data-only and adds `callerName`/`callerAvatar`. The client already reads both, so the "caller shows as Beevia" gap is closed. On Android, the data-only ring now reaches the background handler. On iOS, both handlers ignore `call.incoming`, so the change removes the banner and leaves nothing. #74 also writes a `call_event` message into the conversation when a call ends, but the client drops any message with no ciphertext except a payment card. The result: a finished call moves its chat to the top of the inbox with the old preview, and no card appears. #73 adds an `activity.updated` socket event that nothing on the client subscribes to, and routes payment rows to their chat (the fix for "money requests don't appear on Activity"). PR #75, opened this morning and re-pushed unchanged as #76 at 14:07 UTC, expires rings nobody ended. Its message reports 16 production calls stuck `ringing` since 23 Sep and says #74 has been live since 19 Oct 16:52 UTC.

3. **The board is now five days static, and the 7-day submission count has fallen to 3.** That fall is the window sliding past 12 Oct, not a new event. Two of the three were board administration's moves. The last owner submission is 5.9 days old, and nothing has left review on 0902 in 20.6 days. Meanwhile 26 files of server work (#73–#75) and a 94-file mobile merge happened with no board item and no board movement. **The board has stopped describing the work.** The review step, not the developers, is still the bottleneck.

**If you read nothing else:** the iOS half of calling went backwards yesterday. CallKit's VoIP registration reached `main`, and the server's ring went silent with no VoIP sender behind it. Android went forwards. The fix is small on both sides (§8, items 1–3), and no board item tracks any of it.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. Against the 19 Oct scratch export, **no row changed** (only the preamble's `Date` line differs), and the activity sidecar is byte-identical (`cmp`).

| Status | 19 Oct | 20 Oct | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 1 | 1 | 0 |
| REVIEW/QA | 18 | 18 | 0 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

No status change, comment, reopen, completion or re-assignment on any board in the window. `BVA-I309` (CallKit) has been In progress for 8.0 days. Its code reached `main` yesterday, so the item's status no longer reflects where the code is. `BVA-I311` has been BLOCKED since 9 Oct with no comment.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. The 08-01 and 0901-admin sidecars are byte-identical to 19 Oct's. 0901 was not re-exported. The 19 Oct copy (last entry the 30 Sep sweep, 67 leaves Done, no reopens) is reused for cycle times. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902, five days past its end

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | 6 REVIEW/QA (`I306`, `I307`, `I308`, `I310`, `I312`, `I313`), 1 In progress (`I309`), 1 BLOCKED (`I311`) | **All on `main` now.** `I307`'s routing came with PR #49. `I309` (CallKit) is on `main` with the VoIP registration and no `call.ended` handling |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, screen `I316` REVIEW/QA | Feed (#66) and screen (PR #49) both on `main`. Server gained `activity.updated` (#73); the screen does not subscribe |
| Appearance (`BVA-I318`–`I329`) | 9 | all 9 REVIEW/QA | All client code on `main`. `I322`'s fixes landed with a hard-coded white mic tint. `I319`, `I325`, `I328` still have no server code, and `I324`'s save call still goes to a route that does not exist |
| Carried bug `BVA-I286` | 1 | REVIEW/QA since 14 Oct | Partly on `main`: the "Transactions History" rename is still not on any branch |

**Two review items do not have their code (fully) on `main`, down from five.** A reviewer can now check the rest of the queue against `main` directly. `I322` should go back for the one-line mic fix. A close by bulk sweep, as 0901 had on 30 Sep, would still mark `I325` and `I286` Done.

---

## 3. Code, API surface and spec drift

**Audit: clean at route level.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-20`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. Clean again after this cycle's spec edits. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin "in spec, not in code"). They are an artefact of the stale working trees and were not acted on.

**Two `main` branches moved.** `beevia-mobile` `4f9c29f` → `31a77e8` (PR #49, 6 commits, 94 files, +4,383/−706). `beevia-api` `a7b2170` → `49c0683` (#73 `fa392e4` + `2646484`, #74 `f346459`, all by `Phoenixdadhev`, merged by `Ayomikun Araoye` at 16:31 and 16:51 UTC). `beevia-admin-api` (`c59460a`, 8 Oct), `beevia-db-schema` (`40ecf69`, v0.0.40, 9 Oct) and `beevia-admin` (`0b41e35`, 22 Sep) did not move. **Open: `beevia-api` PR #76** (`origin/fix/abandoned-ring-timeout`, `7200c55`, 20 Oct 14:07 UTC), 1 commit, 7 files. It replaces **PR #75** (`fix/expire-abandoned-rings`, `860443b`, 14:01 UTC). The tree and the commit message are identical, the old branch is deleted, and #75 has no merge ref. This was seen in the end-of-run recheck, and the rest of this report reads the one commit under either number.

### 3.1 What PR #49 put on mobile `main`

`origin/BVA-I316` and `origin/BVA-I306` are now fully contained in `main` (0 commits ahead). `git diff origin/BVA-I316 origin/main` is empty.

| Landed | Board item | Note |
|---|---|---|
| Activity screen calling `GET /activity` | `I316` | Filter/search run on the client over loaded pages; badge from the feed response (`api-rfc.md` §5.14) |
| Push tap routing by `data.kind` | `I307` | |
| CallKit, PushKit registration, Android native ring from FCM | `I309` | VoIP clash and missing `call.ended` handling (§3.2) |
| Chat background application | `I324` | Saves to `PUT /users/me/appearance/chat-background`, which 404s (`api_url.dart:53–57`, `TODO(backend)`) |
| Dark-mode text and cursor fixes; dark mic icon | `I322` | **Light-mode mic tinted white** (`chat_widgets.dart:1099–1103`) |
| Saved contact names, bulk unarchive, new launcher icons | none | Off-board |
| `ios/GoogleService-Info.plist` untracked and git-ignored; code scan with `code-quality: false` | rec. 13 | No Firebase config file is tracked on `main` now. Still in history at `1a1f39f` |

`main` has no conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`. The biometric step-up is unchanged (`wallet_service.dart:78`, against a PIN-only `stepUpSchema`).

### 3.2 Calls: the client and server changes, read together

Full detail in `api-rfc.md` §5.15 (2026-10-20 update). In short:

| | Android | iOS |
|---|---|---|
| App in foreground | Socket ring; native screen from the push unless the socket's ring is already up | Socket ring |
| App backgrounded or killed | **Native ring from the data-only push, now with the caller's name** (#74 + PR #49) | **Nothing.** The banner went with #74. Both handlers act on `call.incoming` only on Android, and the server has no APNs VoIP sender |
| Ring dismissed when the call ends | Socket `call.update`, or the plugin's 30 s `duration`, which then posts a "Missed Call" notification. `call.ended` push ignored | Same; no iOS consumer |
| Push token | FCM | **FCM and VoIP tokens alternate in one slot.** FCM rejects a PushKit token, and `invalid-argument`/`invalid-registration-token` are in `DEAD_TOKEN_CODES`, so the processor likely prunes the token (`notification.processor.ts:27–31`). The device would then get no pushes until FCM re-registers |

All of this is a reading of the code. Listener order on socket connect, the FCM sync's `force: false` cache, and FCM's exact error code for a PushKit token decide the details, and none of them was tested. Whether any iPhone runs a build from `main` is not visible here.

**PR #75/#76** sweeps `ringing` calls older than 60 s every 15 s and runs each through the normal teardown. It fixes real server state: its message cites 16 calls stuck `ringing` and a LiveKit webhook that is not arriving. It is unlikely to fix the stacked call UIs that mobile reported on its own, for two reasons. The client's own ring times out at 30 s, before the server's 60–75 s, and the teardown arrives as the `call.ended` push no client consumes.

### 3.3 The standing checks

- **VoIP token clash** (`api-rfc.md` §5.15): **now on `main`.** The server is unchanged: one token per device, no APNs sender.
- **`call.ended`**: **unhandled on `main`.**
- **Duplicate call banner on mobile `main`**: **closed.** `_handleForegroundMessage` returns early for `call.incoming`, and #74 removed the `notification` block anyway.
- **Caller name on the native call screen**: **closed** by #74, on the platform that can show it (Android).
- **`apns-priority`**: silent pushes still go at `10` (`fcm.adapter.ts:124`). `call.incoming` is now one of them.
- **Pipelines:** no workflow change on any backend `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`". `beevia-db-schema` and `beevia-admin-api` have no `needs:`. #73/#74 deployed that way; #75's message says #74 was live from 16:52 UTC, a minute after merge.
- **Dependabot (mobile):** the `pub-minor-and-patch` group was re-cut as **PR #51** (19 Oct 14:40 UTC, 10 updates). It still carries `flutter_local_notifications` ^19.5.0 → ^22.3.2, a three-major bump, and `livekit_client` 2.11 → 2.13. New PR #50 bumps the Gradle group (3 updates). The superseded group branches are gone. #45 (`local_auth` 3.0.2) and #47 (`cupertino_icons` 2.0.0) are unchanged.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. `22P02` is still unmapped. `messages.ref_id` is now queried by the Activity feed with no index (#73's TODO, a `beevia-db-schema` change).

### 3.4 Document changes this cycle

- **`openapi.yaml`**: five operation descriptions and one schema field updated in place, no operation added or removed: `startCall` (silent ring, `callerName`/`callerAvatar`), `declineCall` and `endCall` (the `call_event` message and its `content_meta`), `listActivity` and `getUnattendedActivityCount` (`activity.updated`), and `Message.ref_id` (call id for `call_event`). The `Message.type` enum already listed `call_event`. `ActivityItem.conversation_id` already described the behaviour #73 now implements.
- **`api-rfc.md`**: §5.13's push table (`call.incoming` row), a 2026-10-20 update to §5.14 (Activity) and to §5.15 (calls).
- **`suggestions.md`** §5.13: the plist is untracked on `main`; key restriction is still the open half.
- `admin-api-rfc.md`, `openapi.proposed.yaml` and both admin specs: no change needed.

---

## 4. Risks

- **iPhones on a build from mobile `main` probably lose push delivery**, because the VoIP token overwrites the FCM token in the device's one slot (§3.2). If any tester or store build carries `31a77e8`, this is the highest-priority item on the project.
- **A backgrounded iPhone gets no incoming-call alert at all since #74**, independent of the client build.
- **`call_event` cards are written and discarded.** Every finished call reorders the inbox with a stale preview. Harmless but visible, and it gets worse with every call.
- **The light-mode mic renders as a blank square on `main`** (a code reading; no build ran).
- **0902 has been over for five days with no reviewer, no close and no successor.** 18 leaves sit in review. A bulk sweep would mark `I325` and `I286` Done without their code.
- **Rings stuck in `ringing` on production** (16, per #75/#76) until it merges. The LiveKit `room_finished` webhook is reported not to arrive, which also affects ordinary call teardown.
- **The board no longer describes the work.** #71–#75 and PR #49's polish have no items; the board has not moved in 4.9 days.
- **A Dependabot group PR on mobile (#51) hides a three-major bump** of the notifications plugin, the one the call path depends on.
- **Every backend repo still deploys or migrates production on push without a test gate.** Yesterday's call change went live within a minute of merge.
- **Firebase keys are in history.** Untracked on `main` now; restriction not visible.
- Carried, unchanged: wallet-failure notices off by default (undecided); possible pre-12 Oct PII in production logs (not visible); malformed path ids return `500` (`suggestions.md` §1.1); `BVA-I311` blocked 11 days with no comment; production SSH open to any address per the 1 Oct deploy commits (unverified); the biometric step-up on `main` fails against the real API (§5.11); the admin workstream silent (27.9 days without a `beevia-admin` commit, 36.0 without board activity); three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. No item on any sprint touches them. Yesterday's work was calling, the Activity feed and chat polish.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 13 Oct 14:04 → 20 Oct 14:04 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Open-branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners. Cycle times use 0901 and 0902.

### 6.1 Ayomikun Araoye: backend + admin API

**8 commits in 7 days, all in `beevia-api`**: #71 (wallet-activity pushes and package updates, 13 Oct), #72 (call pushes, 15 Oct), and yesterday's #73 (`activity.updated`, payment-row routing) and #74 (call cards, silent ring with caller name). One more is on the open PR #75 this morning. The commit messages are unusually explicit about production evidence (row counts, stuck calls, query timings), which is what made §3.2 checkable. **Zero submissions in the window**: `I325` (12 Oct) has left it, and all six of their 0902 leaves are in review. Median cycle **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 36.0 days. None of #71–#75 has a board item, and #74 responds to "two things the mobile client asked for" that are not on the board either. That is a process gap, not an individual one. The two things still open on the server side, a VoIP-capable push path for iOS and the `walletActivity` default, have no item, so neither is anyone's assigned work yet.

### 6.2 David Samuel: mobile

**3 commits on `main` in the window** (`d507fe4`, `b2fc36f`, `8b267ed`, as `Davidtariq96`), landed through PR #49, merged under the `David Samuel` identity at 14:30 UTC yesterday. No unmerged branch work remains. No board action since 14 Oct 16:10 UTC. Of their three 7-day submissions, one was their own (`I286`) and **two were board administration's** (`I307`, `I313` on 15 Oct). Median cycle **0.99 d (n=36)**. WIP: `I309` (CallKit) for **8.0 d**, the oldest open item on 0902. Its code is now on `main`. The parts still missing (dropping the VoIP registration, a `call.ended` handler) are small, and the server's silent ring has made the iOS side a decision for both developers rather than a mobile task. Whether anyone reviewed PR #49 before it merged cannot be seen from git. That is a process question for the team, not a finding about the author.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC, 18.0 days. `BVA-I321` is still in review, and open WIP is zero. Zero submissions and zero WIP is worth a question rather than an assumption: finished, waiting on review, or working off-board. The new launcher icons that reached `main` yesterday are a design-facing change with no design item. The open design questions are unchanged: whether `I313` matches the new design, and `I286`'s message button and username. #74 adds a new one: the wording of call cards ("Missed call" for the callee, "No answer" for the caller) is left to the client.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **27.9 days** ago. The admin board has had no activity for 36.0 days, and `BVA-I9` has been In progress for all of it. **Absence of data is not absence of work.** `beevia-admin` has only `main`, so local work would be invisible here.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | 2 | 1 | **5** |
| 2026-W43 (from Mon 19 Oct, to 14:02 UTC Tue) | — | **0** | | | |

Acceptance on 0902 is still zero. Over twenty days, 18 leaves went into review and none came out. **The review step, not the developers, is the bottleneck.** This week the gap between the board and the code is wider than ever: two `main` branches took 113 files of work in one afternoon, and the board recorded nothing.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more.
- **Work outside the board.** #71–#75, the contact-name, archive and icon work, and the `call_event` cards have no items.
- **Who moved an item is not whether it is done.** Two review items lack their code on `main`, and one (`I322`) has a regression on it.
- **A merge is not a review.** The merge commit records who pressed the button, not whether anyone read the diff.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. §3.2 and the mic finding are code readings.

---

## 7. Previous recommendations: where they stand

| Recommendation from 19 Oct | Status on 20 Oct |
|---|---|
| **1. Create 0903 and move `I309`/`I311` into it; do not sweep 0902; set `ZOHO_SPRINT_FILTER` to `0903`** | ❌ **Not done.** No 0903, no sweep, no board action |
| **2. Review 0902 against `main`; send `I307`/`I316`/`I324`/`I322` back until `BVA-I316` merges, `I286` until the rename lands; close `I319`/`I325`/`I328` with a note** | ◐ **The condition changed, the action did not.** `BVA-I316` merged, so `I307`/`I316`/`I324` can now be reviewed on `main`. Nothing left review |
| **3. Before PR #49 merges: remove the VoIP registration, add a `call.ended` handler, drop the light-mode mic tint** | ❌ **Overtaken.** PR #49 merged 28 minutes after the edition with none of the three |
| **4. Review PR #49 promptly once item 3 is in** | ◐ **Merged without item 3.** Whether it was reviewed is not visible |
| **5. Patch `main`'s foreground push handler to skip `call.incoming`** | ✅ **Done by the merge.** `main`'s handler now returns early for it; #74 also removed the banner |
| **6. Add `callerName` to `call.incoming`'s `data`; check `apns-priority: 5` for silent pushes** | ◐ **Half.** `callerName` and `callerAvatar` shipped in #74. Silent pushes still go at priority 10, and there are now two of them |
| **7. Give off-board work a board item** | ❌ **Not done.** #73, #74, #75 and PR #49's polish have none |
| **8. Restrict the Firebase API keys** | ? **Not visible.** The plist is now untracked on `main` (PR #49) |
| **9. Hold the Dependabot `pub-minor-and-patch` PR until `BVA-I316` lands** | ◐ **Held, and the condition is met.** Re-cut as #51 after the merge, still carrying `flutter_local_notifications` 19 → 22 |
| **10. Put `needs: test` back on `beevia-api`'s `sync`; verify jobs elsewhere** | ❌ **Not done** |
| **11. Decide the `walletActivity` default** | ❌ **Not done** |
| **12. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done** |
| **13. Check the production logs for pre-12 Oct PII** | ? **Not visible** |
| **14. Map `22P02` to `400`** | ❌ **Not done** |
| **15. Make Flutter CI a required check on mobile `main`; confirm the Firebase secrets** | ? **Not visible** |
| **16. Check the production host's SSH settings** | ? **Not visible** |
| **17. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **18. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **19. Open the admin board's next sprint, or say it is paused** | ❌ **Neither** |
| **20. Carried items** | ❌ **None moved** |

**One done, four partly (two of them overtaken by the merge), the rest not done or not visible.**

---

## 8. What I would do this week

1. **Stop the VoIP token registration on mobile `main` today.** Remove the `addSocketConnectedListener(CallKitManager.syncVoipTokenIfAvailable)` line in `bootstrap.dart:111`, or make it a no-op, until the server can store and use a second token. If an iPhone build from `31a77e8` is already out, also force one FCM re-registration (`_registerToken(token, force: true)`) on the next launch.
2. **Decide what a backgrounded iPhone gets for a call.** The full answer is an APNs VoIP sender plus a `(device, provider)` token slot (`api-rfc.md` §5.15). Until that exists, send `call.incoming` with an APNs `alert` for iOS only, through the `apns.payload` block `FcmPushAdapter` already builds, and keep Android data-only.
3. **Handle `call.ended` and `call_event` on the client.** For `call.ended`, call `CallKitManager.endNativeCall(callId)` from both push handlers. For `call_event`, add a branch beside the `payment_card` one in `_decryptAndPersist`, plus a preview string in `_messagePreview`.
4. **Merge #76 (the re-push of #75), and find out why `room_finished` is not arriving.** The sweep is a safety net. The webhook is the normal teardown path for a dropped call.
5. **Fix the light-mode mic** (`chat_widgets.dart:1103`: tint only in dark mode, or drop it), and send `I322` back until then.
6. **Create 0903 and move `I309` and `I311` into it.** Do not close 0902 by sweep. Then set `ZOHO_SPRINT_FILTER` to `0903`.
7. **Review 0902 against `main`.** Accept what is there and works: `I306`, `I307`, `I308`, `I310`, `I312`, `I315`, `I316`, `I318`, `I321`, `I324` (client half), `I327`, `I329`, and `I313` once design has looked at it. Hold `I322` (item 5) and `I286` (rename). Close `I319`/`I325`/`I328` with a note, or open one backend item to extend `PATCH /users/me/settings`.
8. **Give off-board work a board item:** #71–#75, the iOS call decision (item 2), and PR #49's contact names, bulk unarchive and icons.
9. **Subscribe the Activity screen to `activity.updated`** for the badge, and add the `messages.ref_id` partial index in `beevia-db-schema` before the table grows.
10. **Split `flutter_local_notifications` 19 → 22 out of Dependabot PR #51** and test it on its own; merge the rest of the group.
11. **Send silent pushes at `apns-priority: 5`**, and test `call.ended` on an iPhone once item 3 is in.
12. **Restrict the Firebase API keys.** Untracking the plist does not protect keys already in history.
13. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
14. **Decide the `walletActivity` default.**
15. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4).
16. **Check the production logs for PII from before 12 Oct.**
17. **Map `22P02` to `400`** (`suggestions.md` §1.1).
18. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
19. **Check the production host's SSH settings.**
20. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11), and **bring `payments.dto.ts` onto `phone.util.ts`**.
21. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
22. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 36.0 days ago**. Today's sidecar is byte-identical to 19 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 36 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 27.9 days without a commit, and `beevia-admin-api` 12.3. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-nine days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved, and line 2 was a judgement call.** PR #49 put CallKit on `main`. With #74, Android now has a complete native ring path: data-only push, matching keys, caller name, background handler. That is evidence for raising line 2. On the same day, iOS lost its only background call alert, and `main` gained a registration that probably breaks iPhone push delivery. That is evidence for lowering it. The standing rule is not to move line 2 for CallKit until the server can ring it on both platforms, so line 2 holds at 0.85. If item 1 of §8 is not done and an iOS build from `main` is in use, the next edition should consider lowering it. Nothing else that landed (Activity screen, chat background, contact names, `call_event` cards the client drops, `activity.updated`) maps to a rubric line beyond what is already scored.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change. `call_event` is plaintext by design (call facts are server-visible) |
| 2 | Voice & video calling | 8 | 0.85 | 0 | CallKit on `main` (PR #49); Android ring complete with #74; iOS background ring gone and VoIP token clash live. Held |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Payment rows now route to their chat in the feed (#73); biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether iPhones are losing pushes.** §3.2 follows from the code on both sides, but no device, build or production log was examined, and listener order and FCM's error code for a PushKit token were not tested.
- **Whether any build from mobile `main` is installed anywhere.**
- **Whether the light-mode mic renders as described.** No build ran.
- **Whether PR #49 was reviewed**, or whether branch protection requires CI on any `main`.
- **Whether #74 is deployed.** #75's commit message says so (live from 19 Oct 16:52 UTC). That is the author's statement, not something visible here.
- **Why nothing moved on the board.** No comment on any board records a reason.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0). All three finished by 14:02 UTC. 0901 was not re-exported; the 19 Oct scratch copy of the closed sprint was reused.
3. Fast-forward sync (step 2), exit 1. **`beevia-mobile` fast-forwarded 7 commits on `main`** (`4f9c29f` → `31a77e8`, PR #49; no branch switch). `beevia-admin` was already current. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-20`: clean, exit 0, before and after this cycle's spec edits. The in-repo audit was run too, for the board section (exit 1, the known phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
5. Board comparison: `cmp` of every sidecar against 19 Oct's (all identical), a CSV diff past the preamble (no differences). Flow analysis (`flow20.py`): cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none in the window).
6. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` on every repo. In `beevia-mobile`: the merge's parents and tree against `origin/BVA-I316`, both push handlers, `call_kit_manager.dart` (VoIP sync, `showIncomingCallFromPushData`, `duration`), `bootstrap.dart`'s socket-connect listeners, the FCM token sync, `_decryptAndPersist` and the inbox preview path for messages with no ciphertext, the mic widget, `.gitignore` and the tracked Firebase files, conflict markers, and the Dependabot PR #50/#51 diffs. In `beevia-api`: the full diff `a7b2170..origin/main`, all three commit messages, `fcm.adapter.ts`'s APNs block and `DEAD_TOKEN_CODES`, `notification.processor.ts`'s pruning, `devices.setPushToken` call sites, `stepUpSchema`, and PR #75's commit and doc diff. In all three backend repos: the `needs:` lines of `release.yml` at `origin/main`, and the latest db-schema tag.
7. Spec and RFC updates (§3.4).
8. This report and its web edition.
9. End-of-run recheck at 14:11 UTC: a fast re-export of 0902 (`--activity --no-descriptions`, exit 0) had a sidecar byte-identical to the first one. `ls-remote` showed every `main` at the commits read above. In `beevia-api` it showed one change: `fix/expire-abandoned-rings` (#75) was gone and `fix/abandoned-ring-timeout` (#76, `7200c55`, 14:07 UTC) carried the same tree. That is folded into §3. No new mobile PR appeared.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`/`cat-file`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-20.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 20 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.** PR numbers come from `refs/pull/*` and merge-commit messages.
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap.

**Window.** 19 Oct 14:02 UTC → 20 Oct 14:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
