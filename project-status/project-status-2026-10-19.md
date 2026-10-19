# Beevia — Project Status

**As of 2026-10-19** · Sprint **0902** (30 Sep → 15 Oct): **ended four days ago, not closed, no successor. 25 items, 0 leaves To do · 1 In progress · 18 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-19.csv` + `beevia-activity-2026-10-19.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-19.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 16 Oct file in the same folder; a fresh read-only scratch export of sprint **0901 (76 items)** in `/tmp/beevia-scratch/0901/`, for cycle times. All five repos were read at `origin/main`, and `beevia-mobile`'s unmerged `origin/BVA-I316` too. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 16 Oct 14:04 UTC → 19 Oct 14:02 UTC, 3.0 days (Fri → Mon).**

---

## Quick overview

> **Nothing moved on any board over the weekend, and no `main` branch moved in any repository. Sprint 0902 is four days past its end, with 18 of 21 leaves in review, no close and no `0903`.** The only new work is two commits pushed to the unmerged `BVA-I316` branch at 13:06 and 13:36 UTC today, and **the branch now has an open pull request, `beevia-mobile` #49**, first seen in this edition. They fix dark-mode text colours for leaves already in review, show saved contact names in chats and calls, add bulk unarchive, replace the app icons, and stop tracking the iOS Firebase file. They do not touch the two call problems that should block this merge. One of them also adds a hard-coded white tint that turns the light-mode microphone icon into a blank square.

| Metric | 16 Oct | 19 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 0 / 1 / 18 / 1 / 1 | **0 / 1 / 18 / 1 / 1** | none. The 0902 sidecar is byte-identical to 16 Oct's |
| Board actions in the window (all boards) | 2 | **0** | last action 15 Oct 16:05 UTC, **3.9 days** ago |
| Transitions into REVIEW/QA, last 7 days (leaves) | 9 (printed as 8; see below) | **8** | 2 by the leaf's owner, 1 by another team member, **5 by board administration**. `I329` (9 Oct) left the window. Five more leave it tomorrow |
| Owners' last submission of their *own* leaf | 14 Oct 16:01 UTC (David, `I286`) | 14 Oct 16:01 UTC (David, `I286`) | **4.9 days** ago |
| Items that left REVIEW/QA in the window | 0 | **0** | nothing has left review since 0902 opened 19.6 days ago, apart from the two bulk sweeps on older sprints |
| 0902 leaves in REVIEW/QA whose code is not (fully) on `main` | 5 | **5** | `I307`, `I316`, `I324` (branch only), `I325` (nowhere), `I286` (partly). `I322` now has follow-up fixes on the branch too (§3.1) |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no workflow change |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | no spec edits needed |
| `beevia-mobile` days since a commit on `main` | 8.1 | **11.1** | but `BVA-I316` was pushed **today**, 13:36 UTC |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 8.3 / 7.1 | **3.9 / 11.3 / 10.1** | |
| `beevia-admin` days since a commit | 23.9 | **26.9** | |
| Admin board: open sprint / days since any activity | none / 32.0 | **none / 35.0** | |
| Successor sprint to 0902 in Zoho | none | **none** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | 0/25 · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: nothing new on any `main` |

**Correction to 16 Oct.** That edition's headline table gave 8 transitions into review over 7 days, but its own split ("3 by the leaf's owner, 1 by another team member, 5 by board administration") sums to 9. The split was right. `BVA-I329`'s move at 14:07 UTC on 9 Oct fell two minutes inside its window. The right figure for 16 Oct was **9**. Nothing else in that edition depends on it.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | 1 (**own**, `I325`, 12 Oct) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**35.0 d**) | **5** (all `beevia-api`) | No commit since #72 (3.9 d). `callerName` and the `walletActivity` default still open |
| David Samuel | mobile | **0902: 15** (13 REVIEW/QA, 1 In progress, 1 BLOCKED) | 7 (**1 own**, 1 by Ayomikun, **5 by board administration**) | 0.99 d (n=36) | `I309` (**7.0 d**, past their median) | **0 on `main`** + **5 on `origin/BVA-I316`** (2 today) | Pushed today; no board action since 14 Oct. The VoIP registration and `call.ended` handler are still missing from the branch |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 0 | 0.99 d (n=3) | none | n/a | No board action since 2 Oct (17.0 d) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**35.0 d**) | **0** | `beevia-admin` **26.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **Who reviews 0902, and is there a 0903?** The sprint has been over for four days. Every open question on it waits on a review step that has taken nothing since 30 Sep. (2) **Who reviews PR #49 (`BVA-I316`), and will the two call fixes go in before it merges?** It is 6 commits ahead of `main` and merges cleanly. But it still registers the iPhone VoIP token over the FCM token and ignores `call.ended` (§3.2). (3) **Does today's dark-mode work belong to `I322`, which is already in review?** If so, `I322`'s code is not fully on `main` either.

**The three things worth knowing:**

1. **A fully static board for three days.** Every activity sidecar on all four boards is byte-identical to Friday's. The last board action was board administration moving `I307` and `I313` to review at 16:05 UTC on 15 Oct. The last owner submission was David's `I286` on 14 Oct. Zoho still lists `0902, 0901, 08-01, 0702, 0701` for Beevia and only `0901-admin` for the admin project. With 18 of 21 leaves in review and nothing ever taken out of it on this sprint, **the review step, not the developers, is the bottleneck.**

2. **Today's branch commits are real polish, but none of it is on `main`.** `b2fc36f` ("fixes", 56 files) gives the chat input and conversation search proper dark-mode text and cursor colours and adds a dark mic icon. It also prefers the phone's saved contact name over the server profile name in the chat list, contact profile and in-app call screen. It adds multi-select and bulk unarchive to Archived Chats, and refreshes Home after an unarchive. It replaces the Android and iOS launcher icons. `8b267ed` stops tracking `ios/GoogleService-Info.plist`, adds it to `.gitignore`, and turns off the Node-only quality job in the mobile code scan. The plist change is half of last week's recommendation 13 (§7). The file is still tracked on `main` and remains in history, so the keys still need restricting.

3. **One new defect on the branch: the light-mode microphone disappears.** The chat input's mic icon is now drawn with `color: Colors.white` in both themes. `ic_mic.svg`, the light-mode icon, is a white 28×28 square with a dark stroke. `flutter_svg` applies `color` as a `srcIn` tint, so the whole icon becomes a solid white square and the mic glyph is lost. The fix is one line: apply the tint only in dark mode, or drop it, since `ic_mic_dark.svg` is already light-stroked. This is a hard-coded colour in the commit that removes hard-coded colours (`I322`).

**If you read nothing else:** no board moved and no `main` moved for three days. 0902 is still unclosed and unreviewed, with no successor. All the new work is on `BVA-I316`, which is now an open PR (#49) and still has both call blockers, plus one small light-mode regression.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. Against the 16 Oct scratch export, **no row changed**, and the activity sidecar is byte-identical (`cmp`).

| Status | 16 Oct | 19 Oct | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 1 | 1 | 0 |
| REVIEW/QA | 18 | 18 | 0 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

No status change, comment, reopen, completion or re-assignment on any board in the window. `BVA-I309` (CallKit) has been In progress for 7.0 days, past David's 0.99-day median, and its code is the subject of §3.2. `BVA-I311` has been BLOCKED since 9 Oct with no comment.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. The 08-01 and 0901-admin sidecars are byte-identical to 16 Oct's. 0901 was re-exported today, because the 5 Oct scratch copy had been cleared from `/tmp`. Its last entry is still the 30 Sep sweep (07:56:53 UTC), all 67 leaves are Done, and it has no reopens. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902, four days past its end date

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | 6 REVIEW/QA (`I306`, `I307`, `I308`, `I310`, `I312`, `I313`), 1 In progress (`I309`), 1 BLOCKED (`I311`) | Unchanged from 16 Oct. `I307`'s routing is on `origin/BVA-I316` only. `I309`: VoIP token clash and `call.ended` handling still open |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, screen `I316` REVIEW/QA | Feed on `main` (#66). Screen on `origin/BVA-I316` only |
| Appearance (`BVA-I318`–`I329`) | 9 | all 9 REVIEW/QA | On `main` (PR #43), except `I324`'s chat-background application (branch only). **New: dark-mode text/cursor fixes for the chat input and search (`I322`'s scope) are on the branch only.** `I319`, `I325`, `I328` have no server code |
| Carried bug `BVA-I286` | 1 | REVIEW/QA since 14 Oct | Partly on `main`: the "Transactions History" rename is still not on any branch |

**Five review items do not have their code (fully) on `main`.** A sixth, `I322`, is on `main` but has fixes after submission on the branch. A close by bulk sweep, as 0901 had on 30 Sep, would mark all of them Done.

---

## 3. Code, API surface and spec drift

**Audit: clean at route level.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-19`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin "in spec, not in code"). They are an artefact of the stale working trees and were not acted on.

**No `main` moved in any repository.** `beevia-api` is still `a7b2170` (#72, 15 Oct). `beevia-admin-api` is `c59460a` (8 Oct), `beevia-db-schema` is `40ecf69` (v0.0.40, 9 Oct), `beevia-admin` is `0b41e35` (22 Sep) and `beevia-mobile` is `4f9c29f` (8 Oct). The only push anywhere was to `beevia-mobile` `origin/BVA-I316`, which moved `d507fe4` → `8b267ed` and is now **6 ahead / 2 behind** `main`. A trial merge (`git merge-tree`) is clean. **`ls-remote` shows `refs/pull/49/head` at `8b267ed` with a `merge` ref, so the branch is now an open pull request, #49.** No earlier edition records it. When it was opened, and by whom, is not visible from git. The four Dependabot branches (PRs #45–#48) and `origin/BVA-I306` are unchanged.

### 3.1 `BVA-I316`: two commits today

Both by `Davidtariq96`. 59 files, +273/−241, of which 40 are icon PNGs and `Contents.json`.

| Commit | Change | Board item it serves | Note |
|---|---|---|---|
| `b2fc36f` "fixes" (13:06 UTC) | Chat input and conversation search: explicit `primaryText` text and cursor colours; new `ic_mic_dark.svg` in dark mode | `I322` (*Apply Dark Palette & Check for Hardcoded Colors*), in review since 2 Oct | **Light-mode regression**, below |
| | `UserProvider.contactNameForUserId()`: prefer the phone's saved contact name in the chat list, contact profile and in-app call screen; Home now fetches the contact list on load | none on 0902 | The native CallKit screen still takes its name from the push, which has none (§3.2) |
| | Archived Chats: long-press multi-select and bulk unarchive; Home refetches after an unarchive so a restored chat reappears | none on 0902 | Uses the existing bulk endpoint; no API change |
| | New Android and iOS launcher icons; `appearance.dart` swatch label ellipsis; two explanatory comments removed from the push router | none | |
| `8b267ed` "updated code scanning" (13:36 UTC) | `git rm --cached ios/GoogleService-Info.plist` and add it to `.gitignore`; code scan called with `code-quality: false` because the reusable workflow's quality job expects a `package.json` | recommendation 13 (16 Oct) | The file stays tracked on `main` and in history until this merges, and the keys in it are already public to anyone with repo access |

**The mic icon.** In `chat_widgets.dart` the idle-state mic is now `SvgPicture.asset(isDarkMode ? icMicDark : icMic, color: Colors.white)`. `flutter_svg` ^2.3 turns `color` into `ColorFilter.mode(color, BlendMode.srcIn)`. `ic_mic.svg` begins with `<rect width="28" height="28" fill="white"/>`, so in light mode every opaque pixel, background and stroke alike, is painted white. The result is a blank white square: invisible on a white chat background, and a white tile on a custom wallpaper. Dark mode is unaffected. This is a reading of the code. No build ran.

### 3.2 The standing checks

- **VoIP token clash** (`api-rfc.md` §5.15): **open.** `call_kit_manager.dart:80` on `BVA-I316` still registers the PushKit token as `pushProvider: 'voip'` for the same device id. The server still has one token slot per device and no APNs sender. Today's commits did not touch it.
- **`call.ended`** (sent by `beevia-api` since #72): **still unhandled on every branch.** `CallKitManager.endNativeCall` exists and is called from the socket path only.
- **Duplicate call banner on mobile `main`:** unchanged, because `main` has not moved.
- **Caller name on the native call screen:** the server's `call.incoming` `data` still carries no name, so CallKit shows "Beevia". Today's contact-name change affects only the in-app screen.
- **Pipelines:** no workflow file changed on any backend `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`". `beevia-db-schema` and `beevia-admin-api` have no `needs:` at all. The latest db-schema tag is still `v0.0.40`.
- **Mobile `main`:** same commit as 8 Oct, so the earlier checks stand: no conflict markers, `ios/GoogleService-Info.plist` tracked, and the biometric step-up still on `main` against a PIN-only `stepUpSchema`.
- **Dependabot (mobile):** unchanged since 14 Oct. The `pub-minor-and-patch` group still hides `flutter_local_notifications` 19 → 22.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. `22P02` is still unmapped.

### 3.3 Document changes this cycle

**None.** The shadow audit is clean and no backend `main` moved, so the four specs, `api-rfc.md`, `admin-api-rfc.md` and `suggestions.md` are still correct. `suggestions.md` §5.13 (Firebase keys) still describes `main` accurately. It should be updated when `8b267ed` reaches `main`, not before.

---

## 4. Risks

- **0902 has been over for four days with no reviewer, no close and no successor.** 18 leaves sit in review. A bulk sweep would mark at least five of them Done without their code on `main` (§2). `I309` and `I311` have no sprint to move into.
- **`BVA-I316` is now an open PR (#49) with its two blockers still in it.** It is 6 commits ahead and merges cleanly, so it could land at any time. Merged as it stands, it would send iPhone FCM pushes to a VoIP token (§3.2).
- **Light-mode mic icon renders as a blank square on the branch** (§3.1). It is small, but it is the first thing a light-mode user sees in every chat.
- **Mobile `main` shows a duplicate call banner when the app is open**, if #72 is deployed. Unchanged.
- **The teardown push has no consumer**, so a dismissed call still rings on a backgrounded Android device until the 30-second timeout.
- **A Dependabot group PR on mobile hides a three-major bump** of the notifications plugin.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **Firebase keys are tracked on `main` and in history.** The branch untracks the file, but untracking does not rotate or restrict the keys.
- **Wallet-failure notices are off by default.** Undecided.
- **PII may be in production logs from before 12 Oct.** Not visible here.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1).
- **`BVA-I311` has been blocked for 10 days on server work nobody has been asked for.** No comment.
- **Production SSH open to any address**, per the 1 Oct deploy commits. Unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 26.9 days without a `beevia-admin` commit, 35.0 days without admin-board activity, no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. No item on any sprint touches them. Today's branch work is chat polish and app identity.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 12 Oct 14:04 → 19 Oct 14:04 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners. Cycle times use 0901 (re-exported today) and 0902.

### 6.1 Ayomikun Araoye: backend + admin API

**5 commits in 7 days, all in `beevia-api`**: #71 (wallet-activity pushes and package updates, 13 Oct) and #72 (call pushes, 15 Oct). #70 (11 Oct) has left the window. Nothing since 15 Oct 15:46 UTC, 3.9 days. One 7-day submission, their own (`I325`, 12 Oct). All six of their 0902 leaves are in review, so they have no open board work on the main board. Median cycle time **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 35.0 days. The two backend follow-ups raised last week, `callerName` in `call.incoming` and the `walletActivity` default, have not been made. Neither has a board item, so neither is anyone's assigned work yet. That is a process gap, not an individual one.

### 6.2 David Samuel: mobile

**No commit on `main` in 7 days** (the last, PR #44, was 8 Oct), and **5 on `origin/BVA-I316`**: 12, 13 and 14 Oct, and two today. No board action since 14 Oct 16:10 UTC. Of their seven 7-day submissions, one was their own (`I286`), one Ayomikun's (`I324`), and **five board administration's** (`I306`, `I312`, `I316` on 12 Oct; `I307`, `I313` on 15 Oct). Median cycle **0.99 d (n=36)**. WIP: `I309` (CallKit) for **7.0 d**, well past the median. That is the clearest "probably stuck" signal on the board, and the work it needs (VoIP registration, `call.ended`) is the part not touched today. Today's commits show the work continues, but it lands on one branch that now carries four tickets' worth of code plus untracked polish. None of it reaches `main` or the review queue in a form a reviewer can accept.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC, 17.0 days. `BVA-I321` is still in review, and open WIP is zero. Zero submissions and zero WIP is worth a question rather than an assumption: finished, waiting on review, or working off-board. Two design questions are still open on the board: whether `I313` matches the new design, and `I286`'s message button and username. Today's new launcher icons are a design-facing change with no design item.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **26.9 days** ago. The admin board has had no activity for 35.0 days, and `BVA-I9` has been In progress for all of it. **Absence of data is not absence of work.** `beevia-admin` has only `main`, so local work would be invisible here.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | 2 | 1 | **5** |
| 2026-W43 (from Mon 19 Oct, to 14:02 UTC) | — | **0** | | | |

Acceptance on 0902 is still zero. Over nineteen days, 18 leaves went into review and none came out. **The review step, not the developers, is the bottleneck.** In W42, more of the moves into review were board administration's than the owners'.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more.
- **Work outside the board.** Today's contact-name, archive and icon work has no item. #71 and #72 had none either.
- **Who moved an item is not whether it is done.** Five review items lack their code on `main`.
- **Branch commits are not delivery,** so they are counted separately. A 56-file commit titled "fixes" is not comparable to a single-purpose one.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The mic finding is a code reading.

---

## 7. Previous recommendations: where they stand

| Recommendation from 16 Oct | Status on 19 Oct |
|---|---|
| **1. Create 0903 and move `I309`/`I311` into it; do not sweep 0902; set `ZOHO_SPRINT_FILTER` to `0903`** | ❌ **Not done.** No 0903, no sweep, no board action at all |
| **2. Review 0902 against `main`; send `I307`/`I316`/`I324`/`I286` back; close `I319`/`I325`/`I328` with a note** | ❌ **Not done.** Nothing left review |
| **3. Patch `main`'s foreground push handler to skip `call.incoming`** | ❌ **Not done.** `main` unchanged |
| **4. Add a `call.ended` handler on `BVA-I316`; remove the VoIP token registration** | ❌ **Not done**, although the branch got two commits today |
| **5. Add `callerName` to `call.incoming`; check `apns-priority: 5` for silent pushes** | ❌ **Not done.** `beevia-api` unchanged |
| **6. Give server work a board item** | ◐ **Nothing to test it on.** No server work this window; today's mobile work has no item either |
| **7. Hold the Dependabot `pub-minor-and-patch` PR** | ◐ **Holding.** Unchanged, not merged |
| **8. Put `needs: test` back on `beevia-api`'s `sync`; verify jobs elsewhere** | ❌ **Not done** |
| **9. Decide the `walletActivity` default** | ❌ **Not done** |
| **10. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done** |
| **11. Check the production logs for pre-12 Oct PII** | ? **Not visible** |
| **12. Map `22P02` to `400`** | ❌ **Not done** |
| **13. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ◐ **Started on a branch.** `8b267ed` untracks the file on `BVA-I316`. Still tracked on `main` and in history; key restriction not visible |
| **14. Make Flutter CI a required check on mobile `main`** | ? **Not visible.** `8b267ed` fixes the code scan for Flutter, which is related but is not branch protection |
| **15. Check the production host's SSH settings** | ? **Not visible** |
| **16. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **17. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **18. Open the admin board's next sprint, or say it is paused** | ❌ **Neither** |
| **19. Carried items** | ❌ **None moved** |

**None of nineteen done; one started on a branch, two holding.**

---

## 8. What I would do this week

1. **Create 0903 and move `I309` and `I311` into it.** Do not close 0902 by sweep. Then set `ZOHO_SPRINT_FILTER` to `0903`.
2. **Review 0902 against `main`.** Accept what is there (`I306`, `I308`, `I310`, `I312`, `I315`, `I318`, `I321`, `I327`, `I329`, and `I313` once design has looked at it). Send `I307`, `I316`, `I324`, `I322` back until `BVA-I316` merges, and `I286` until the rename lands. Close `I319`/`I325`/`I328` with a note, or open one backend item to extend `PATCH /users/me/settings`.
3. **Before PR #49 (`BVA-I316`) merges:** remove the VoIP token registration, add a `call.ended` handler (both push handlers → `CallKitManager.endNativeCall(callId)`), and drop the white tint from the light-mode mic icon (`api-rfc.md` §5.15; §3.1 here).
4. **Review PR #49 promptly once item 3 is in.** It carries four tickets' code plus untracked polish. Every day it waits, more reviewed items depend on code a reviewer cannot see on `main`.
5. **Patch `main`'s foreground push handler to skip `call.incoming`** if the branch is not merging this week.
6. **Add `callerName` to `call.incoming`'s `data`**, and check whether silent pushes should go at `apns-priority: 5`.
7. **Give off-board work a board item.** That covers today's contact names, bulk unarchive and new icons, and last week's #71/#72.
8. **Restrict the Firebase API keys** now. Untracking the plist on a branch does not protect keys already in history.
9. **Hold the Dependabot `pub-minor-and-patch` PR** until `BVA-I316` lands.
10. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
11. **Decide the `walletActivity` default.**
12. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4).
13. **Check the production logs for PII from before 12 Oct.**
14. **Map `22P02` to `400`** (`suggestions.md` §1.1).
15. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
16. **Check the production host's SSH settings.**
17. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
18. **Bring `payments.dto.ts` onto `phone.util.ts`.**
19. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
20. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 35.0 days ago**. Today's sidecar is byte-identical to 16 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 35 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 26.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-eight days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved.** No `main` changed in any repository. Today's `BVA-I316` commits are on a branch, and the rubric scores `main`. Even merged, they would not move a line: contact names, archive bulk actions and icons are polish within capabilities already scored.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change on `main` |
| 2 | Voice & video calling | 8 | 0.85 | 0 | Unchanged. CallKit still on `origin/BVA-I316` only, with the VoIP clash and no `call.ended` consumer |
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

- **Whether the light-mode mic renders as described.** It follows from the SVG and `flutter_svg`'s tint semantics, but no build ran.
- **Whether #72 is deployed.** `beevia-api` deploys on push, so it probably is, but Actions results are not visible from here.
- **Whether anyone reviewed `BVA-I316`**, or whether branch protection requires CI on any `main`.
- **Why nothing moved over the weekend.** No comment on any board records a reason.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0). The three ran in parallel and finished at 14:02 UTC. Later, a read-only re-export of **0901** to `/tmp/beevia-scratch/0901/` (`--activity --no-descriptions`, 76 items, exit 0), because the 5 Oct copy the cycle-time script used had been cleared from `/tmp`.
3. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-19`: clean, exit 0. The in-repo audit was run too, for the board section (exit 1, the known phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
5. Board comparison: `cmp` of every sidecar against 16 Oct's (all identical), a CSV diff past the preamble (no differences). Flow analysis (`flow19.py`): cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none in the window).
6. Content checks. `git fetch --all --prune` and `for-each-ref` on every repo. In `beevia-mobile`: the full diff of `d507fe4..origin/BVA-I316`, both commit messages, the two mic SVGs, `pubspec.yaml`'s `flutter_svg` constraint, `call_kit_manager.dart`'s VoIP registration, every `endNativeCall` call site, and a `git merge-tree` trial merge against `origin/main`. The end-of-run `ls-remote` revealed PR #49; its head was fetched once to confirm it equals `origin/BVA-I316`, and the temporary ref was deleted straight after. In all three backend repos: the `needs:` lines of every workflow at `origin/main`. In the 0902 export: every item name, to match today's branch work to items.
7. Spec and RFC updates: none needed (§3.3).
8. This report and its web edition.
9. End-of-run recheck at 14:07 UTC: a fast re-export of 0902 (`--activity --no-descriptions`, exit 0) had a sidecar byte-identical to the first one. `ls-remote` showed every `main` and `BVA-I316` at the commits read above, plus PR #49 (folded into §3 and the overview).

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch` (once into a temporary `refs/remotes/pr/49`, deleted afterwards), `ls-remote`, `git archive`, `merge-tree` (writes objects only, no ref or working-tree change), and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-19.html`, `web-report/index.html`, plus new board exports for 19 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **The 0901 scratch copy had been cleared from `/tmp`.** It was re-exported. Its content matches the earlier editions' figures (67 leaves Done, last action 30 Sep).
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all four exports. This is the known sampling artefact, not a scope gap.

**Window.** 16 Oct 14:04 UTC → 19 Oct 14:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
