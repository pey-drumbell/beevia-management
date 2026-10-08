# Beevia — Project Status

**As of 2026-10-08** · Sprint **0902** (30 Sep → 15 Oct): **day 9 of 16, 25 items, 4 leaves To do · 10 In progress · 6 REVIEW/QA · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-08.csv` + `beevia-activity-2026-10-08.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-08.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 7 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`. `beevia-admin` and `beevia-mobile` were read in the working tree. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 7 Oct 14:03 UTC → 8 Oct 14:05 UTC, 1.0 day** (Wednesday afternoon to Thursday afternoon in Lagos).

---

## Quick overview

> **Push notifications reached the app's `main` today, and for the first time in ten days the team moved its own board items. Both arrived at the sprint's midpoint with nothing estimated, and work in progress went from 4 leaves to 10.** `beevia-mobile` PR #44 (8 Oct 10:38 UTC) puts every acceptance criterion of `BVA-I306` on `main`: FCM, a permission prompt tied to first use of Home, token registration on start and on refresh, and deregistration on logout. Its board item is still In progress. On the board, David and Ayomikun made all 10 actions in the window: seven leaves started, and one parent moved to REVIEW/QA. Nothing left REVIEW/QA, which now holds 6 leaves. The backend broke a six-day silence with a dependency refresh in all three repos. It went through the ungated production pipelines. `beevia-api`'s break was caught on its branch before merge, and `beevia-db-schema`'s Release has not completed six hours later.

**No correction to the 7 Oct edition.** Its claims were re-checked against today's data. One clarification: `beevia-mobile` has run Flutter CI on every pull request and every push to `main` (`pr.yml`, `main.yml` → `flutter-ci.yml`) since before September. The open question in the last three editions was always whether that check is *required* before merge, and it still cannot be seen.

| Metric | 7 Oct | 8 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / Done | 11 / 4 / 5 / 1 | **4 / 10 / 6 / 1** | 7 started, 1 → QA |
| Board actions in the window (all boards) | 13 | **10** | **all by David or Ayomikun**; none by board administration |
| Transitions into REVIEW/QA, last 7 days (leaves) | 5 | **6** | 5 by board administration, **1 by David** (Philip's `BVA-I321`, via its parent) |
| Owners' last submission of their *own* leaf | 28 Sep (9.0 d) | 28 Sep (**10.0 d**) | |
| Items that left REVIEW/QA in the window | 0 | **0** | |
| 0902 leaves whose code is on `main` but whose item is not in REVIEW/QA | — | **2** | `BVA-I306` (In progress), `BVA-I329` (To do) |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | first dependency refresh went through them today |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | |
| `beevia-mobile` days since a commit on `main` | 0.2 | **0.1** | PR #44 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 5.9 / 5.9 / 5.9 | **0.1 / 0.3 / 0.3** | dependency refresh |
| `beevia-admin` days since a commit | 14.9 | **15.9** | |
| Admin board: open sprint / days since any activity | none / 23.0 | **none / 24.0** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: push notifications are outside the rubric |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6** (4 In progress, 2 REVIEW/QA) · 0901-admin: 1 In progress | 2 (**both moved by board administration**) | 1.22 d (n=12) | `BVA-I308`, `I310`, `I315` (0.9 d, started by them) · `BVA-I325` (0.1 d, started by David's parent move) · `BVA-I8` on 0901-admin (**24.0 d**) | **6** (4 today: dependency refresh in all three repos; 2 CI on 1 Oct) | Started `BVA-I310` (the one MVP-relevant 0902 item) and `BVA-I315` (still specified against E2EE). No server code for either yet |
| David Samuel | mobile | **0902: 15** (8 In progress, 3 REVIEW/QA, 4 To do) | 3 (**all moved by board administration**) | 0.96 d (n=27) | **8 leaves.** `BVA-I286` (**7.9 d**, own) · `I306`, `I312` (1.9 d, started by board administration) · `I308`, `I310` (0.9 d, Ayomikun) · `I313`, `I316` (0.9 d, own) · `I324` (0.1 d, own) | **5** on `main` + PR #43, #44 merges | `BVA-I306`'s code is merged; the item is still In progress. Eight items open at once |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 1 (**moved by David**, via parent `BVA-I320`) | 0.99 d (n=3) | none | n/a | — |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**24.0 d**) | **0** | `beevia-admin` **15.9 days** without a commit. No admin sprint |

**The two questions for standup:** (1) **It is the midpoint. Which of the ten open leaves will land by 15 Oct, and which will not?** Work in progress went from 4 to 10 in one day, David holds eight, and nothing is estimated. (2) **Who reviews, starting with `BVA-I306`?** Its code merged this morning. Six leaves are already waiting in REVIEW/QA with no named reviewer. Two of them (`BVA-I319`, `I328`) are backend tasks with no backend code.

**The three things worth knowing:**

1. **The app now registers for push notifications, and the server was already sending them.** PR #44 (`BVA-I306`, 2 commits, merged 55 minutes after the last one) adds `PushNotificationManager`. It requests permission on first Home load, not at launch. It registers the FCM token with `POST /notifications/token` on every socket connect and on token refresh, deregisters it on logout, and shows foreground pushes as local notifications. The request bodies match `RegisterTokenRequest` and `ClearTokenRequest` exactly. On the server, `beevia-api` already sends pushes for new messages (content-free), incoming calls, eight payment events and new-device alerts. It uses FCM when `FCM_SERVICE_ACCOUNT` is set, and whether production sets it cannot be seen. Two gaps remain. First, **every tap opens Home**: the client's own comment says the push `data` shape is not documented. It is now, in `api-rfc.md` §5.13, and that is all `BVA-I307` (deep links) needs from the server. Second, **the 7 Oct Firebase config was only partly untracked**. `lib/firebase_options.dart` and `google-services.json` were removed and `.gitignore`d, but `ios/GoogleService-Info.plist` (with its `API_KEY`) is still tracked on `main`, and all three stay in history (`suggestions.md` §5.13).

2. **The team moved its own board items. Their number in progress jumped, and nothing left review.** All 10 actions in the window were David's or Ayomikun's, the first day since 28 Sep without a single move by board administration. Ayomikun started `BVA-I308`, `I310` and `I315` on 7 Oct 16:03–16:05 UTC. David started `BVA-I313`, `I316` and, this morning, the Chat Background group (`BVA-I323` → `I324` and Ayomikun's `I325`). David also moved parent `BVA-I320` to REVIEW/QA, which carried Philip's dark-palette leaf `BVA-I321` with it. That is the first move into the column by a team member since 28 Sep, though not by the leaf's owner. Against that: In progress went 4 → 10 leaves at the sprint midpoint, with 0 of 25 estimated. `BVA-I325` (*Chat Background Preference Storage*) was started rather than closed, although the client stores that preference on the device. `BVA-I306`, whose code is merged, stays In progress. Six leaves sit in REVIEW/QA with no reviewer. **Apart from the two bulk sweeps (3 Sep and 30 Sep), no item on any board has ever been accepted by someone other than its submitter.**

3. **The backend's first change in a week was a dependency refresh, deployed through the ungated pipelines.** `package-update` PRs merged in `beevia-admin-api` (#21, 07:53 UTC, 3 min after its commit), `beevia-db-schema` (#21, 07:58 UTC, 5 min) and `beevia-api` (#63, 12:31 UTC). There are two major bumps, `dotenv` 17→18 and `unplugin-swc` 1→2, and `beevia-admin-api` jumps from schema package 0.0.36 to 0.0.39. **`beevia-api`'s bump broke the TypeScript build on the branch** (two `socket.io` copies), and `5343364` fixed it before the merge. The PR-time check did its job, and the episode shows what a direct push would have deployed. **`beevia-db-schema`'s Release has not completed.** On 1 Oct its version bump followed the merge within a minute. Six hours after #21 there is no `v0.0.40` tag or bump commit. Sync migrates production only after a *successful* Release, so production was probably not migrated, but nothing here shows why Release stalled. `beevia-api`'s `sync` still has no `needs: test`.

**If you read nothing else:** push registration is on `main` and matches the server, but the board still shows the item In progress. The team is moving its own items again, and in-progress work jumped to ten at the midpoint with no estimates and no reviewer. The backend's dependency refresh went straight to production pipelines; one build break was caught on the branch, and the schema release stalled.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The comparison is file-level, against the 7 Oct scratch export in `/tmp/beevia-scratch/0902/`. The only fields that changed are `Status` and `Last Modified`: no item was added, removed, re-owned or re-described.

| Status | 7 Oct | 8 Oct | Δ |
|---|---:|---:|---:|
| To do | 11 | 4 | −7 |
| In progress | 4 | 10 | +6 |
| REVIEW/QA | 5 | 6 | +1 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

**All 10 audit entries in the window, in order (UTC):**

| Time | Item(s) | Action | By |
|---|---|---|---|
| 7 Oct 16:03:26 | `BVA-I308` *New Message Notification Handling* | To do → In progress | Ayomikun Araoye |
| 7 Oct 16:03:28 | `BVA-I315` *Activity Feed Backend* | To do → In progress | Ayomikun Araoye |
| 7 Oct 16:04:07 | `BVA-I316` *Build the Activity Screen* | To do → In progress | David Samuel |
| 7 Oct 16:05:17 | `BVA-I313` *Notification Settings Screen* | To do → In progress | David Samuel |
| 7 Oct 16:05:44 | `BVA-I320` (parent), `BVA-I321` | In progress → REVIEW/QA | David Samuel |
| 7 Oct 16:05:55 | `BVA-I310` *Money Notification Handling* | To do → In progress | Ayomikun Araoye |
| 8 Oct 10:30:46 | `BVA-I324` *Background Swatch Picker & Application* | To do → In progress | David Samuel |
| 8 Oct 10:30:54 | `BVA-I323` (parent), `BVA-I325` | To do → In progress | David Samuel |

All of these arrived after the 7 Oct edition's 14:03 UTC cut-off. **There were no comments, no reopens and no completions.** Every 0902 item still has a blank Epic and 0 estimation points. `BVA-I306` (In progress since board administration started it on 6 Oct) did not move, although PR #44 merged its code seven minutes after David's 10:30 UTC board update.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC). The 0901-admin and 08-01 sidecars are byte-identical to 7 Oct's, and their CSVs differ only in the `Date` preamble line. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 9: the midpoint

| Block | Leaves | State | Code on `main` |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **5 In progress** (`I306`, `I308`, `I310`, `I312`, `I313`), 3 To do (`I307`, `I309`, `I311`) | **`I306` complete on `main`** (PR #44, §3.1). `I312` is partly there: foreground pushes show as OS notifications, but there is no in-app banner component and no grouping. `I307` (deep links) has the server payload it needs (`api-rfc.md` §5.13). `I308`'s server half exists (`notifyNewMessage`). `I310`'s reminders have no server event and no scheduler. `I313` has no settings screen yet, though `/notifications/preferences` exists |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done; backend `I315` and screen `I316` **In progress** since 7 Oct | none. `BVA-I315` still asks for server-side message previews, which E2EE rules out, and it is now being worked on |
| Appearance (`BVA-I318`–`I329`) | 9 | 5 REVIEW/QA, **1 more to QA** (`I321`), 2 In progress (`I324`, `I325`), 1 To do (`I329`) | On `main` since PR #43. All three preferences are stored on the device. Nothing in `lib/features/chat` reads the chosen background yet (`I324`) |
| Carried bug `BVA-I286` | 1 | In progress, **7.9 d** | not identified on any branch |

**The board and the code disagree in both directions:**

- **Behind the code:** `BVA-I306` (In progress, code merged), `BVA-I329` (To do, the Appearance screen has been on `main` since 7 Oct).
- **Ahead of the code:** `BVA-I319` and `I328` (REVIEW/QA, backend storage that does not exist because the client stores locally), and now `BVA-I325` (In progress, same situation).

**At the midpoint,** 10 leaves are open and 4 untouched, and seven calendar days remain. Without estimates, nothing here can say whether that fits. The question has to be answered by the people doing the work, and today is the day the last two editions asked for it.

---

## 3. Code, API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. This was run against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-08`). The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees, and they were not acted on. **No spec file changed this cycle.** The sync touched no controller, DTO or schema file, and the backend commits are `package.json`/lockfile only.

### 3.1 `beevia-mobile`: PR #44 (`BVA-I306`)

`main` moved `01bcf2a` → **`4f9c29f`** (fast-forward; the working tree was already on `main`, so there was no branch switch). Two `Davidtariq96` commits, merged by David at 10:38 UTC:

- **`64637f1`** "semgrep workflow" (7 Oct 21:27 UTC). Despite the name, it carries the whole feature: `push_notification_manager.dart` (+209), `registerPushToken`/`clearPushToken` in `notification_service.dart`, `POST_NOTIFICATIONS` on Android, push entitlements on iOS, `flutter_local_notifications` re-enabled, mock-server routes for the token endpoints, and a contract-test update. It also adds **`code-scan.yml`**, the org reusable-workflow caller that `beevia-api` and `beevia-admin-api` use. That closes the mobile half of a recommendation carried since 16 Sep.
- **`69770ff`** "updated workflow" (8 Oct 09:43 UTC). Untracks `lib/firebase_options.dart` and `android/app/google-services.json` and adds all four Firebase config paths to `.gitignore` (*"contains API keys"*). It makes every Flutter CI job write them from three repository secrets.

| Check at `origin/main` | 7 Oct | 8 Oct |
|---|---|---|
| Push token registered with the server | no | **yes**: on socket connect (if permission granted), on refresh; cleared on logout |
| Push permission prompt | none | on first Home load, not at launch |
| Notification tap | n/a | **always opens Home**: payload shape undocumented (`api-rfc.md` §5.13) |
| Firebase config tracked | 3 files | **1 file: `ios/GoogleService-Info.plist`** (the `.gitignore` entry names `ios/Runner/`) |
| Conflict markers (`pubspec.yaml` / `.lock` / `project.pbxproj`) | 0 / 0 / 0 | 0 / 0 / 0 |
| Biometric step-up (`wallet_service.dart:78`) | yes | **yes** |
| `X-Device-Id` on all six #60 routes | yes | yes |

**On the Firebase keys.** Firebase client keys are meant to ship inside the app, so this is not a credential leak. The team's own `.gitignore` comment treats them as sensitive, though, and the clean-up is incomplete. The protection that matters is restricting each key to the app's package/SHA-1 and bundle ID in Google Cloud. The 7 Oct edition recommended that, and it is still not visible from here (`suggestions.md` §5.13).

**Remote branches:** `main`, `BVA-I306` (contained), `BVA-I317` (contained), `update-fixes` (contained), `App-bundle` (contained), five Dependabot branches. Nothing is stranded.

### 3.2 Backend: dependency refresh through ungated pipelines

| Repo | PR | Merged (UTC) | Commit → merge | Notable |
|---|---|---|---|---|
| `beevia-admin-api` | #21 | 8 Oct 07:53 | 3 min | `beevia-db-schema` 0.0.36 → **0.0.39**; Nest 12.0 → 12.1; `unplugin-swc` 1 → 2 |
| `beevia-db-schema` | #21 | 8 Oct 07:58 | 5 min | `dotenv` 17 → **18**; `unplugin-swc` 1 → 2; drizzle patch |
| `beevia-api` | #63 | 8 Oct 12:31 | 4 min after the fix | `dotenv` 17 → **18**; Nest 12.1; OpenTelemetry; `socket.io` **pinned to exactly 4.8.3** (`5343364`) |

`beevia-api`'s first commit (`584a6b7`, 07:50 UTC) floated `socket.io` to 4.8.4 while `@nestjs/platform-socket.io` pins 4.8.3. The two copies made `tsc` reject `RedisIoAdapter`. The fix commit explains the cause precisely and pins in lockstep with Nest. The broken commit never reached `main` on its own, since `main`'s first-parent history goes `bcb47bb` → `c145d6e`.

**`beevia-db-schema` Release has not completed.** Release bumps and tags a patch version on every push to `main`. On 1 Oct, `v0.0.39` followed its merge within a minute. As of 14:05 UTC (`git ls-remote`), there is no `v0.0.40` and no bump commit. Sync ("Migrate the production database") runs only when Release concludes `success`, so a failed Release means no migration. That is the safe direction, and this refresh carried no migration anyway. The cause, whether build, publish or the API write-back, is not visible here.

Re-read whole at `origin/main` today: `beevia-api`'s `release.yml` `sync` job still has no `needs: test` (comment at line 29), and `deploy` needs only `sync`. `beevia-admin-api`'s `sync.yml` (on push) → `deploy.yml` (`workflow_run`), and `beevia-db-schema`'s `release.yml` (on push) → `sync.yml`, are unchanged. `PaymentService.activeNgn()`, `StubTranslateAdapter` and `payments.dto.ts`'s unparsed `phone` (`z.string().trim().min(6).max(20)`) are unchanged.

### 3.3 Document changes this cycle

- **`api-rfc.md`** — new §5.13: the push `data` payload as implemented (`chat.message`, `call.incoming`, `payment.update` with its eight events, `security.alert`, `system.test`), with preference categories and senders. It notes that `BVA-I310`'s reminder has no event value, and that the older `messaging/push` module is still hard-wired to the stub.
- **`suggestions.md`** — §5.12 gains an 8 Oct update (Flutter CI runs on PR and push; it now depends on three Firebase secrets; whether it is required is unknown). New §5.13 covers the incomplete Firebase-config untracking and key restriction. §7.7 gains an 8 Oct update (the dependency refresh, the caught `socket.io` break, the stalled db-schema Release, `code-scan.yml` in mobile). §8 3b and 3f gain notes, and there is a new 3h.
- `openapi*.yaml` and `admin-api-rfc.md`: unchanged. The audit is clean, and no contract moved.

---

## 4. Risks

- **Every backend repo deploys or migrates production on push without a test gate** (§3.2). Today it carried a real dependency refresh with two major bumps, minutes after each commit. The one break that occurred was caught at PR time. That is evidence the PR check runs, not that it is *required*.
- **Work in progress is spreading at the midpoint.** 10 of 21 leaves are In progress (David 8), 0 estimated, 7 days left. Starting is not finishing, and the review column has never been drained by a reviewer.
- **The review step has no reviewer.** Six leaves are in REVIEW/QA (five for 1.9 days, one for 0.9), code already shipped, and none has left.
- **`BVA-I315` is being built against acceptance criteria that E2EE rules out** (server-side message previews). Until today it was a spec problem. Now it is work in progress.
- **The db-schema Release stalled for an unknown reason.** If the cause is the dependency refresh, the next real migration will also stall.
- **Firebase keys sit in a tracked file and in history**, unrestricted as far as can be seen here.
- **Production SSH accepts connections from any address**, per the 1 Oct deploy commits. Unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 15.9 days with no `beevia-admin` commit, 24.0 days with no board activity, and no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. Push notifications serve several MVP flows indirectly: chat, calls and payments all now have a delivery path to a device. The rubric does not score them as a capability. `BVA-I310`'s payment reminders remain the one 0902 item that serves an MVP flow directly (Transfer Acceptance & Escrow, PRD §10.2). It is now In progress, but it has no server event or scheduler behind it.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 1 Oct 14:05 → 8 Oct 14:05 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

### 6.1 Ayomikun Araoye: backend + admin API

**6 commits in 7 days.** Four were today: the `package-update` commit in each backend repo, and the `socket.io` pin that fixed `beevia-api`'s build. Two were CI edits on 1 Oct. They also merged all three PRs. On 0902 they hold six leaves: four In progress and two in REVIEW/QA. They started three items themselves on 7 Oct (`BVA-I308`, `I310`, `I315`), their first own board moves on 0902. `BVA-I325` was started by David's parent move this morning. None of the four has server code yet. `BVA-I308`'s server half already exists. `BVA-I310` needs a reminder event and a scheduler. `BVA-I315` needs its E2EE question answered before code. The two REVIEW/QA items (`BVA-I319`, `I328`) describe storage that the client does on the device. `BVA-I8` has been In progress on the admin board for 24.0 days. Median cycle time is **1.22 d (n=12)**, unchanged.

### 6.2 David Samuel: mobile

**5 commits on `main` in 7 days** (`03a3035`, `6f38116`, `1a1f39f`, `64637f1`, `69770ff`), plus the PR #43 and #44 merges. They hold 15 of 0902's 21 leaves: **8 In progress**, 3 in REVIEW/QA, 4 To do. Their three 7-day submissions were all moved by board administration. Their own QA move this week, parent `BVA-I320`, carried Philip's leaf. `BVA-I306`'s code is complete on `main`, but the item was not moved. `BVA-I286` (profile-screen UI mismatch) has been In progress for **7.9 d** against a 0.96-day median and has no identifiable code. It remains the one WIP item that looks stuck. Eight open items for one person is the number to ask about, not as a judgement of effort, but because it makes "what lands by 15 Oct" unanswerable from the board. One process observation stands: the same person writes and merges every mobile change, and no review is visible on the board or (from here) on GitHub.

### 6.3 Philip Chidera: design

No board action of their own since 2 Oct 14:18 UTC. `BVA-I321` (dark palette) moved to REVIEW/QA on 7 Oct 16:05 UTC through David's move on the parent. The dark palette has been in code on `main` since PR #43. Their open WIP is now zero. Design work does not land in these repositories, so commits are not applicable.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **15.9 days** ago. The admin board has had no activity for 24.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the ninth edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W37 | 7 | — | | | |
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (from Mon 5 Oct) | — | **6** | **0** | 1 | 5 |

Acceptance is still zero. Owner submissions of their own leaves have been zero for ten days, while three features (Appearance, Firebase set-up, push registration) reached `main`. The bottleneck is not output. Review is not a step anyone on the team performs on the board, and the board trails the code.

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more, and eight open items may be small.
- **Who moved an item is not who did the work.** `BVA-I321`'s submission was David's move on a parent. The palette itself is Philip's.
- **A parent's cascade is not a start.** `BVA-I325` was started by David's move on `BVA-I323`.
- **Commit counts reward small commits.** Four of Ayomikun's six are lockfile refreshes. `64637f1` is 19 files under a misleading message.
- **Co-assignment is counted for both owners** (`BVA-I308`, `I310`).
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 7 Oct | Status on 8 Oct |
|---|---|
| **1. Decide 0902's scope at the midpoint; estimate the untouched leaves** | ❌ **Not done; the opposite happened.** 7 leaves were started, 0 of 25 estimated, and no scope comment was written. Today is the midpoint |
| **2. Review the five Appearance leaves; close `I319`/`I325`/`I328`; move `I329` forward** | ❌ **Not done.** Nothing left REVIEW/QA. `I325` was *started*, not closed. `I329` is still To do. `I324` correctly stays open |
| **3. Make Flutter CI a required check on mobile `main`** | ? **Not visible.** CI runs on every PR and push. PR #44 extended it to write Firebase config from secrets |
| **4. Put `needs: test` back on `beevia-api`'s `sync`; gate db-schema and admin-api** | ❌ **Not done.** The dependency refresh went through all three ungated chains today |
| **5. Scope `BVA-I310`'s server half** | ◐ **Started, not scoped.** Ayomikun moved it to In progress on 7 Oct. No comment, no server code. `api-rfc.md` §5.13 now records that no reminder event exists |
| **6. Restrict the Firebase API key** | ? **Not visible.** Related: two of three config files untracked on 8 Oct, and `ios/GoogleService-Info.plist` is still tracked |
| **7. Check the production host's SSH settings** | ? **Not visible from here** |
| **8. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **9. Correct `BVA-I315`'s acceptance criteria for E2EE** | ❌ **Not done**, and the item is now In progress |
| **10. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** The file is unchanged since 25 Sep |
| **11. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **12. Carried: comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec; untrack `.cxx`** | ◐ **One part done:** `code-scan.yml` is now in `beevia-mobile` (PR #44). `beevia-admin` still has no `.github`. The rest did not move |

**None of twelve fully achieved; two partly.** Rec 1, the one this edition most needed, moved the wrong way.

---

## 8. What I would do this week

Re-ranked for the midpoint. Scope and review lead because the sprint now has more open work than it has days.

1. **Decide 0902's scope today.** With 10 leaves open and 4 untouched, say which will not land by 15 Oct, and stop starting new ones until something finishes. Estimate what remains. If something must give, keep `BVA-I310`, the one item that serves an MVP flow.
2. **Name a reviewer, then drain the column.** Move `BVA-I306` to REVIEW/QA with PR #44 as its evidence, and review it first, since it is complete and verifiable. Close `BVA-I319`, `I325` and `I328` with a one-line comment recording device storage. Move `BVA-I329` to match `main`.
3. **Settle `BVA-I315` before more work goes into it.** Rewrite its preview criterion for E2EE: the server can return type, counterpart, timestamp and payment amount, but not message text. The client can fill text previews from its local store.
4. **Write down the push payload where the client reads it** (`api-rfc.md` §5.13 has the table). Then `BVA-I307`'s deep links need no server work. Scope `BVA-I310`'s server half as one new `payment.update` event (`reminder`) plus a job at +12 h and −1 h on the existing escrow-expiry queue.
5. **Find out why `beevia-db-schema`'s Release did not complete on 8 Oct**, before the next schema change needs it. Then put `needs: test` back on `beevia-api`'s `sync`, and give db-schema's Release and admin-api's Sync a verify job to wait on (`suggestions.md` §7.7).
6. **Restrict the Firebase API keys** (Android package + SHA-1, iOS bundle ID) and `git rm --cached ios/GoogleService-Info.plist` (`suggestions.md` §5.13).
7. **Make Flutter CI a required check on mobile `main`**, and confirm the three Firebase secrets are set, or every CI job now fails at compile.
8. **Check the production host's SSH settings**: `PasswordAuthentication no`, root login off, and rate limiting.
9. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
10. **Bring `payments.dto.ts` onto `phone.util.ts`.**
11. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
12. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 24.0 days ago**. Today's export and sidecar are identical to 7 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 24 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 15.9 days without a commit. `beevia-admin-api` changed today, but only through the dependency refresh (#21), and its last code change was 24 Sep. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed thirty-seven days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance, and not whether `main` compiles.

**No score moved.** PR #44 gives chat, calls and payments a delivery path to the device, but push notifications are not one of the rubric's eleven capabilities, and none of the scored lines gained an endpoint, screen or wiring. The backend changes are dependency versions only.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Push for new messages is content-free and now registered by the client; no crypto, key or socket change |
| 2 | Voice & video calling | 8 | 0.85 | 0 | `call.incoming` pushes can now reach the device; tap opens Home, not the call. No call-screen change |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Escrowed `payment.send` on `main`; biometric option still rejected by `stepUpSchema` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep; `beevia-admin-api` changed dependencies only |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether push notifications work end to end.** That depends on `FCM_SERVICE_ACCOUNT` being set in production and on the three Firebase CI secrets. Neither is visible here.
- **Whether mobile `main` builds.** No `flutter` command ran, and CI results return `404` to this workspace. A fresh clone now needs `flutterfire configure` before it compiles, because `lib/firebase_options.dart` is untracked.
- **Why `beevia-db-schema`'s 8 Oct Release did not complete**, whether it published a package, and whether any Sync ran.
- **Whether the backend dependency refresh is running in production.** `beevia-api` and `beevia-admin-api` deploy on push, but deploy outcomes are not visible.
- **Whether anyone but the author reviewed PR #44**, or whether any check was required before it merged.
- **Whether branch protection requires CI on any `main`.**
- **The production host's real SSH configuration.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
4. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0), diffed field by field against the 7 Oct file there.
5. Fast-forward sync (step 2), exit 1. `beevia-mobile` fast-forwarded by 3 commits to `4f9c29f` (already on `main`, so no branch switch), and `beevia-admin` was already current. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep). No controller, DTO or schema file was touched.
6. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-08`: route level and spec health clean. The in-repo audit was run too, for the board section. Its 21 drift lines are the known phantom. Both ran through `uv run --no-project --with pyyaml` (see Degraded inputs).
7. File comparison of every export and sidecar against 7 Oct: 08-01 and 0901-admin identical, 0902 changed. The flow script (`flow08.py`) re-derived cycle times, the 7-day submission count split by actor, WIP ages and the weekly trend. It matches all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`) and comment actions.
8. Content checks in `beevia-mobile` at `origin/main` (`01bcf2a..4f9c29f`): push manager, token-endpoint bodies against `RegisterTokenRequest`/`ClearTokenRequest`, tracked Firebase files (existence of an `API_KEY` entry only; no value was printed), conflict-marker `git grep`, `X-Device-Id` and biometric greps, and the whole remote-branch list. In the backend shadow: `package.json` diffs in all three repos, `main`'s first-parent history in `beevia-api`, the whole `release.yml`/`sync.yml` in all three repos, `git ls-remote` for tags and tips, the notifications module (payload builders, transport selection), and `payments.dto.ts`.
9. `api-rfc.md` §5.13 and `suggestions.md` §5.12 / §5.13 / §7.7 / §8 updates.
10. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive`, `ls-remote`, and read-only `log`/`show`/`grep`/`diff`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-08.html`, `web-report/index.html`, `api-rfc.md`, `suggestions.md`, plus new board exports for 8 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`, which leaves nothing installed.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.** `gh` cannot resolve the organisation's repositories with the available token (re-checked today on PR #44).
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 7 Oct 14:03 UTC → 8 Oct 14:05 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
