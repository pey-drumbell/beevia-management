# Beevia — Project Status

**As of 2026-10-16** · Sprint **0902** (30 Sep → 15 Oct): **ended yesterday, not closed, no successor. 25 items, 0 leaves To do · 1 In progress · 18 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-16.csv` + `beevia-activity-2026-10-16.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-16.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 15 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`, and `beevia-mobile`'s unmerged `origin/BVA-I316` too. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 15 Oct 14:03 UTC → 16 Oct 14:04 UTC, 1.0 day.**

---

## Quick overview

> **Sprint 0902 ended yesterday with nothing reviewed, no close and no sprint after it. Two more leaves were moved into review after it ended, so 18 of its 21 leaves now wait for a review step that has not taken an item in sixteen days.** One of the two, `BVA-I307`, has its code only on the unmerged `BVA-I316` branch. The day's code change was on the server: `beevia-api` #72 now rings a callee by push even when their app looks online, and sends a silent `call.ended` push when a call stops. Both are sound fixes. But the mobile build on `main` was not written for the first, and no client branch handles the second.

| Metric | 15 Oct | 16 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 0 / 3 / 16 / 1 / 1 | **0 / 1 / 18 / 1 / 1** | `I307`, `I313` In progress → REVIEW/QA |
| Board actions in the window (all boards) | 1 | **2** | both by board administration, 15 Oct 16:05 UTC |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **8** | 3 by the leaf's owner, 1 by another team member, **5 by board administration** |
| Owners' last submission of their *own* leaf | 14 Oct 16:01 UTC (David, `I286`) | 14 Oct 16:01 UTC (David, `I286`) | none since |
| Items that left REVIEW/QA in the window | 0 | **0** | none, apart from the two bulk sweeps |
| 0902 leaves in REVIEW/QA whose code is not (fully) on `main` | 4 | **5** | `I307` joins `I316`, `I324` (branch only), `I325` (nowhere), `I286` (partly) |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #72 went out the same way |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 4 call/notification descriptions updated for #72 |
| `beevia-mobile` days since a commit on `main` | 7.1 | **8.1** | no push to any mobile branch since 14 Oct 16:10 UTC |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 1.8 / 7.3 / 6.1 | **0.9** / 8.3 / 7.1 | #72, 15 Oct 15:46 UTC |
| `beevia-admin` days since a commit | 22.9 | **23.9** | |
| Admin board: open sprint / days since any activity | none / 31.0 | **none / 32.0** | |
| Successor sprint to 0902 in Zoho | none | **none** | 0902 ended 15 Oct |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | 0/25 · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: #72 is a reliability fix, not new capability |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | 1 (**own**, `I325`, 12 Oct) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**32.0 d**) | **6** (all `beevia-api`) | Shipped #72 (call pushes) with no board item. Did not add the caller's name to `call.incoming` |
| David Samuel | mobile | **0902: 15** (13 REVIEW/QA, 1 In progress, 1 BLOCKED) | 8 (**2 own**, 1 by Ayomikun, **5 by board administration**) | 0.99 d (n=36) | `I309` (4.0 d) | **0 on `main`** + **4 on `origin/BVA-I316`** | No push or board action since 14 Oct 16:10 UTC. `I307` was moved to review for them; its code is branch-only |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 0 | 0.99 d (n=3) | none | n/a | No board action since 2 Oct |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**32.0 d**) | **0** | `beevia-admin` **23.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **Who reviews 0902, and where do its open leaves go?** The sprint has ended, 18 leaves are in review, and `I309` and `I311` have no sprint to move into. (2) **Should `main`'s mobile build be patched before `BVA-I316` lands?** Since #72, a call received with the app open shows a duplicate "Incoming call" banner that stays after the call ends (§3.1). (3) **Who adds the `call.ended` handler on mobile?** It is about ten lines, and without it the server's new teardown push does nothing.

**The three things worth knowing:**

1. **0902 ran out without a close, and the queue grew after the end date.** At 16:05 UTC on 15 Oct, about two hours after the sprint's last edition, board administration moved `BVA-I307` (*Deep Link Routing & Badge Count*) and `BVA-I313` (*Notification Settings Screen*) from In progress to REVIEW/QA, nine seconds apart and with no comment. `I307`'s routing exists only on the unmerged `BVA-I316` branch. On `main`, every push tap still opens Home. `I313`'s screen has been on `main` since July; the open question last week was whether it matches the new design, and nothing on the board answers it. The sprint is not swept, and Zoho still lists no `0903`. 18 of 21 leaves are now in review, and **nothing has left review since 0902 opened**. The bottleneck is the review step, not the developers.

2. **`beevia-api` #72 fixes two real call faults on the server.** First, the ring was gated on `isUserOnline`, which only asks whether a socket exists. A backgrounded app keeps its socket, so the push was dropped in exactly the case where the app could not show the call itself. Now `call.incoming` always goes out as a push as well as over the socket. Second, nothing told a backgrounded device that a call had ended. Now `decline`, `end` and the media server's room-closed event each send a silent `call.ended` (`status`: `ended`, `declined` or `missed`) to every member. That push ignores the call preference switches, which is the right call: there is no alert left to protect anyone from. The commit also repairs a test that had stubbed the ring out, and gives the two pushes separate dedupe keys so the teardown is not dropped as a duplicate of the ring. It shipped on push to production with no test gate, like every backend change since September, and no board item names it.

3. **The client half is missing, and `main` is now slightly worse in one case.** The server's own docs ask the client to "dedupe on `callId`". **Mobile `main` does not.** Its foreground handler shows a local banner for any push with a visible `notification` block (`BVA-I312`'s work, in review). So a call received with the app open now shows the ringing screen *and* an "Incoming audio call" banner, which stays after the call ends. `BVA-I316` already handles that case correctly. **No branch handles `call.ended`.** Both handlers ignore pushes that have no `notification` block, so a native ringing screen on Android is dismissed only by the socket or its own 30-second timeout. The VoIP token clash on `BVA-I316` is unchanged (§3.2).

**If you read nothing else:** 0902 is over and unreviewed, with 18 of 21 leaves waiting and no sprint after it. The server now rings reliably and sends a teardown, but the mobile app on `main` shows a duplicate banner for calls taken in the foreground, and no build listens for the teardown yet.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. Against the 15 Oct scratch export, two rows changed (`I307`, `I313`: status and `Last Modified`). The activity sidecar has exactly two new entries in the window.

| Status | 15 Oct | 16 Oct | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 3 | **1** | −2 |
| REVIEW/QA | 16 | **18** | +2 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

| Time (UTC) | Item | Move | By |
|---|---|---|---|
| 15 Oct 16:05:26 | `BVA-I307` *Deep Link Routing & Badge Count* | In progress → REVIEW/QA (2.3 d in progress) | board administration |
| 15 Oct 16:05:35 | `BVA-I313` *Build and Implement Notification Settings Screen* | In progress → REVIEW/QA (8.0 d in progress) | board administration |

No comment, reopen, completion or re-assignment on any board. Both moves came after 0902's end date and about twenty minutes after #72 merged. Neither item concerns call pushes.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static, and their sidecars are byte-identical to 15 Oct's. 0901's last entry is still the 30 Sep sweep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 after its end date

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **6 REVIEW/QA** (`I306`, `I307`, `I308`, `I310`, `I312`, `I313`), 1 In progress (`I309`), **1 BLOCKED** (`I311`) | `I306`, `I312` on `main` (PR #44). `I308`/`I310` server halves on `main` (#64, #65). **`I307`: routing on `origin/BVA-I316` only.** `I309`: Android contract aligned on the branch, iOS token clash open, `call.ended` unhandled. `I313`: screen and wiring on `main` since July. `I311`: the server sends neither push it displays |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, screen `I316` REVIEW/QA | Feed on `main` (#66). Screen on `origin/BVA-I316` only |
| Appearance (`BVA-I318`–`I329`) | 9 | all 9 REVIEW/QA | On `main` (PR #43) except `I324`'s chat-background application (branch only). `I319`, `I325`, `I328` have no server code |
| Carried bug `BVA-I286` | 1 | REVIEW/QA since 14 Oct | Partly on `main`: the "Transactions History" rename is still not on any branch |

**Five review items do not have their code (fully) on `main`**: `I307`, `I316`, `I324` (branch only), `I325` (no code anywhere) and `I286` (partly). A close by bulk sweep, as 0901 had on 30 Sep, would mark all five Done.

---

## 3. Code, API surface and spec drift

**Audit: clean at route level.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-16`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees, identical to 15 Oct. They were not acted on.

**One `main` moved:** `beevia-api` to `a7b2170` (#72). `beevia-admin-api` (`c59460a`, 8 Oct), `beevia-db-schema` (`40ecf69`, v0.0.40, 9 Oct), `beevia-admin` (`0b41e35`, 22 Sep) and `beevia-mobile` (`4f9c29f`, 8 Oct) did not. No mobile branch moved either: `BVA-I316` is still `d507fe4`, and the four Dependabot branches from 14 Oct are unchanged.

### 3.1 `beevia-api` #72: `fix: always ring on a call, and push a silent teardown when it ends`

`64fbddc` by `Phoenixdadhev`, merged 15 Oct 15:46 UTC. 5 files, +288/−20, of which 149 lines are tests and 34 are docs.

| Change | Server behaviour | Client on `main` | Client on `BVA-I316` |
|---|---|---|---|
| `call.incoming` push no longer gated on `isUserOnline` | Every callee gets the socket event **and** a push. The socket event is emitted first, then the push is queued | **Duplicate banner.** With the app open, the socket raises the ringing screen and `_showForegroundNotification` shows "Incoming *audio* call / *name* is calling…" on top. Nothing removes it when the call ends. When the app is backgrounded, the user now gets the banner they used to miss, which is the fix working | Handled. The foreground handler drops `call.incoming` on iOS. On Android it skips the native screen when the socket's ring is already showing (`_alreadyHandling`) |
| New silent `call.ended` push (`callId`, `conversationId`, `callKind`, `status`) | Sent on decline, hang-up and the media server's `room_finished`, to every member, ignoring the call switches | Ignored (no `notification` block, no handler) | **Ignored.** The background handler acts only on `call.incoming`, so the Android native ringing screen is dismissed only by the socket's `call.update` or its 30-second timeout |
| Dedupe keys `<callId>:incoming` / `<callId>:ended` | Prevents the teardown being dropped as a duplicate of the ring | n/a | n/a |
| `docs/mobile-chat-integration.md` | Documents both call pushes for the client | | |

**The server is right; the client needs two small changes.** On `main`, the foreground handler should skip `call.incoming`, as the branch does. On both, `call.ended` should call `FlutterCallkitIncoming.endCall(callId)`; the branch already has `CallKitManager.endNativeCall` for this. Whether #72 is live cannot be seen here, but `beevia-api` deploys on every push to `main`.

**One server detail to check.** `call.ended` is the first push this API sends with no `notification` block. `FcmPushAdapter` sends silent pushes with `contentAvailable` but keeps `apns-priority: 10`. Apple's documentation asks for priority 5 on content-available-only pushes, so iOS may throttle or drop them. No iOS code consumes the push yet, so nothing breaks today. It cannot be tested from here.

**Not changed by #72:** `call.incoming`'s `data` still has no caller name, so the native call screen would still say "Beevia" (last edition's recommendation 4). And the push still carries a visible `notification` block.

### 3.2 The standing checks

- **VoIP token clash** (`api-rfc.md` §5.15): **open.** `call_kit_manager.dart:80` on `BVA-I316` still registers the PushKit token as `pushProvider: 'voip'` for the FCM device id. The server still has one token slot per device and no APNs sender. The branch has not merged.
- **Pipelines:** no workflow file changed. `beevia-api`'s `release.yml` `sync` job still has no `needs: test` (its comment still says to restore the gate "when hosted runners are back"). `beevia-db-schema` Release/Sync and `beevia-admin-api` Sync/Deploy still run on push with no verify job. The latest db-schema tag is still `v0.0.40`.
- **Mobile `main`** is the same commit as on 8 Oct, so the earlier checks stand: no conflict markers, `ios/GoogleService-Info.plist` still tracked, and the biometric step-up still on `main` against a PIN-only `stepUpSchema`.
- **Dependabot's mobile branches** are unchanged. The `pub-minor-and-patch` group still hides `flutter_local_notifications` 19 → 22, the plugin both push handlers above depend on.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. `22P02` is still unmapped.

### 3.3 Document changes this cycle

- **`openapi.yaml`:** descriptions updated in place for `startCall` (push sent even to online members; dedupe on `callId`), `declineCall` and `endCall` (silent `call.ended` push to every member, ignoring the call switches), and `NotificationPreferences.voice_calls`/`video_calls` (the teardown is sent regardless). No route, schema or status code changed. Validated as YAML, and the audit is clean.
- **`api-rfc.md`:** §5.13 gets a 16 Oct update with a `call.ended` row in the push table. §5.15 gets a 16 Oct update on the client consequences and the `apns-priority` detail.
- `openapi.proposed.yaml`, `openapi.admin*.yaml`, `admin-api-rfc.md`, `suggestions.md`: unchanged.

---

## 4. Risks

- **0902 has ended with no reviewer, no close and no successor.** 18 leaves sit in review. A bulk sweep would mark five of them Done without their code on `main` (§2). `I309` and `I311` have no sprint to move into.
- **Mobile `main` shows a duplicate call banner when the app is open**, if #72 is deployed (§3.1). It is cosmetic, but it is the shipped build, and it gets worse the longer `BVA-I316` waits.
- **The new teardown push has no consumer**, so a dismissed call still rings on a backgrounded Android device until the 30-second timeout.
- **Merging `BVA-I316` unchanged would break pushes on iPhones** (§3.2).
- **A Dependabot group PR on mobile hides a three-major bump** of the notifications plugin.
- **Every backend repo still deploys or migrates production on push without a test gate.** #72 is the latest change to go out that way.
- **Wallet-failure notices are off by default.** Undecided.
- **PII may be in production logs from before 12 Oct.** Not visible here.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1).
- **`BVA-I311` is blocked on server work nobody has been asked for.** 7 days, no comment.
- **Firebase keys tracked and in history; production SSH open to any address**, per the 1 Oct deploy commits. Both unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 23.9 days without a `beevia-admin` commit, 32.0 days without admin-board activity, no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any sprint touches them. #72 is calling reliability.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 9 Oct 14:05 → 16 Oct 14:05 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners.

### 6.1 Ayomikun Araoye: backend + admin API

**6 commits in 7 days, all in `beevia-api`**: the Drizzle error fix (#70, 11 Oct), wallet-activity pushes and two package updates (#71, 13 Oct), and #72 (15 Oct). #72 is careful work: the commit message explains both faults and why preferences are bypassed for the teardown, and it repairs a test that could never have caught a missing ring. It has no board item, like #71 before it. One 7-day submission, their own (`I325`, 12 Oct); `I308`, `I310` and `I315` (8 Oct) have left the window. All six of their 0902 leaves are in review. Median cycle time **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 32.0 days. The caller-name change suggested on 15 Oct would sit next to #72's edit in `notifyIncomingCall()`, and has not been made.

### 6.2 David Samuel: mobile

**No commit on `main` in 7 days** (the last, PR #44, was 8 Oct), **and 4 on `origin/BVA-I316`** (9, 12, 13 and 14 Oct). Nothing pushed and no board action since 14 Oct 16:10 UTC, 1.9 days. Of their eight 7-day submissions, two were their own (`I329`, `I286`), one Ayomikun's (`I324`) and **five board administration's** (`I306`, `I312`, `I316` on 12 Oct; `I307`, `I313` on 15 Oct). Median cycle **0.99 d (n=36)**; the two new transitions add 2.3 d and 8.0 d, both moved by board administration. WIP: `I309` (CallKit) 4.0 d. Its remaining work grew yesterday: besides the VoIP registration, it now needs a `call.ended` handler to use the server's new teardown.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC. `BVA-I321` is still in review. Open WIP is zero. `I313` is now in review without a design check on record, and whether `I286`'s message button and username match the design is still open. Both are questions only design can answer.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **23.9 days** ago. The admin board has had no activity for 32.0 days, and `BVA-I9` has been In progress for all of it. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible here.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (from Mon 12 Oct, 5 days) | — | **8** | 2 | 1 | **5** |

Acceptance is still zero. Over 0902's sixteen days and one day past it, 18 leaves went into review and none came out. **The review step, not the developers, is the bottleneck.** In W42, more of the moves into review were board administration's than the owners'.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more.
- **Work outside the board.** #72 and #71 had no item. `I307`'s code was written on a branch before the item moved.
- **Who moved an item is not whether it is done.** Five review items lack their code on `main`.
- **Branch commits are not delivery,** so they are counted separately.
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 15 Oct | Status on 16 Oct |
|---|---|
| **1. Create 0903 and move the open leaves into it; do not sweep 0902; set `ZOHO_SPRINT_FILTER` to `0903`** | ❌ **Not done.** No 0903. 0902 not swept, but two open leaves were moved into review instead |
| **2. Review what is on `main`; send `I316`, `I324`, `I286` back; close `I319`/`I325`/`I328` with a note** | ❌ **Not done.** Nothing left review |
| **3. Remove the VoIP token registration before `BVA-I316` merges** | ◐ **Holding.** Not fixed, not merged |
| **4. Add `callerName` to `call.incoming`'s `data`** | ❌ **Not done**, although #72 edited the same function |
| **5. Hold the Dependabot `pub-minor-and-patch` PR** | ◐ **Holding.** Branch unchanged, not merged |
| **6. Rescope `BVA-I313`; decide the `walletActivity` default** | ❌ **Not done.** `I313` moved to review with no comment |
| **7. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done** |
| **8. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done** |
| **9. Check the production logs for pre-12 Oct PII** | ? **Not visible** |
| **10. Map `22P02` to `400`** | ❌ **Not done** |
| **11. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ❌ / ? Still tracked |
| **12. Make Flutter CI a required check** | ? **Not visible** |
| **13. Check the production host's SSH settings** | ? **Not visible** |
| **14. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **15. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **16. Open the admin board's next sprint, or say it is paused** | ❌ **Neither** |
| **17. Carried items** | ❌ **None moved** |

**None of seventeen done, two holding.** #72 is good work, but it answers none of them.

---

## 8. What I would do this week

1. **Create 0903 and move `I309` and `I311` into it.** Do not close 0902 by sweep. Then set `ZOHO_SPRINT_FILTER` to `0903`.
2. **Review 0902 against `main`.** Accept what is there (`I306`, `I308`, `I310`, `I312`, `I315`, `I318`, `I321`, `I322`, `I327`, `I329`, and `I313` once design has looked at it). Send `I307`, `I316`, `I324` back until `BVA-I316` merges, and `I286` until the rename lands. Close `I319`/`I325`/`I328` with a note, or open one backend item to extend `PATCH /users/me/settings`.
3. **Patch `main`'s foreground push handler to skip `call.incoming`**, as `BVA-I316` already does, if `BVA-I316` is not going to merge this week.
4. **Add a `call.ended` handler on `BVA-I316`** (both handlers → `CallKitManager.endNativeCall(callId)`), and **remove the VoIP token registration** before it merges (`api-rfc.md` §5.15).
5. **Add `callerName` to `call.incoming`'s `data`**, and check whether silent pushes should go at `apns-priority: 5` (`api-rfc.md` §5.15).
6. **Give server work a board item.** #71 and #72 changed what users receive and had none, so the review queue cannot see them.
7. **Hold the Dependabot `pub-minor-and-patch` PR** until `BVA-I316` lands.
8. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
9. **Decide the `walletActivity` default.**
10. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4).
11. **Check the production logs for PII from before 12 Oct.**
12. **Map `22P02` to `400`** (`suggestions.md` §1.1).
13. **Restrict the Firebase API keys and untrack `ios/GoogleService-Info.plist`** (`suggestions.md` §5.13).
14. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
15. **Check the production host's SSH settings.**
16. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
17. **Bring `payments.dto.ts` onto `phone.util.ts`.**
18. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
19. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 32.0 days ago**. Today's sidecar is byte-identical to 15 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 32 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 23.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-five days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved.** #72 makes the server ring backgrounded apps and adds a teardown. That makes the existing calling capability more reliable. It adds no part of the PRD's design that was missing, and the rubric does not score correctness. Line 2 also stays where it is because the client cannot yet use the teardown, and CallKit is still on a branch.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change on `main` |
| 2 | Voice & video calling | 8 | 0.85 | 0 | #72: server rings by push always, silent `call.ended`. No client consumer; CallKit on `origin/BVA-I316` only; iOS still cannot ring natively |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | No change; biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether #72 is deployed.** `beevia-api` deploys on push, so it probably is, but the Actions results are not visible from here.
- **Whether iOS delivers `call.ended`** at `apns-priority: 10` with `content-available` only. It needs a device.
- **Why `I307` and `I313` were moved to review.** No comment records it.
- **Whether anyone but the author reviewed any PR**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0). The three ran one after another from about 14:02 UTC; the last finished at 14:04 UTC.
2. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
3. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-16`: clean. The in-repo audit was run too, for the board section. Its drift lines are the known phantom lines, identical to 15 Oct. Both ran through `uv run --no-project --with pyyaml`.
5. Board comparison: `cmp` of every sidecar against 15 Oct's, a CSV diff past the preamble, and a listing of every audit entry after 15 Oct 14:00 UTC. Flow analysis (`flow16.py`): cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none).
6. Content checks. In `beevia-api`: the full #72 diff, its commit message, `fcm.adapter.ts`'s silent-push path and every `notify*` payload. In `beevia-mobile`: the foreground and background push handlers on `main` and `BVA-I316`, `CallKitManager` and the socket's incoming-call path in `CallProvider`, every remote branch with dates. In all three backend repos: the `needs:` lines of every workflow, and db-schema's tags. In the 0902 export: every item description, for any that asks for a call teardown (none).
7. Spec and RFC updates (§3.3).
8. This report and its web edition.
9. End-of-run recheck at about 14:10 UTC: a fast re-export of 0902 (`--activity --no-descriptions`, exit 0) found no audit entry after 15 Oct 16:05 UTC. `ls-remote` showed every `main` and `BVA-I316` at the commits read above, and no new mobile branch. Nothing in this report changed as a result.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `git archive`, `ls-remote` and read-only `log`/`show`/`diff`/`grep`/`ls-tree`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-16.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, plus new board exports for 16 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 15 Oct 14:03 UTC → 16 Oct 14:04 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
