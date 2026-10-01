# Beevia — Project Status

**As of 2026-10-01** · Sprint **0902** (30 Sep → 15 Oct): **day 2, grew from 11 to 25 items overnight, 3 leaves In progress** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-01.csv` + `beevia-activity-2026-10-01.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-01.csv` + its activity sidecar (12 items, sprint 0901-admin); read-only scratch exports of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/` and sprint 0901 (76 items) in `/tmp/beevia-scratch/`, each with its sidecar. All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 30 Sep 14:03 UTC → 1 Oct 14:10 UTC, one working day.**

---

## Quick overview

> **Mobile `main` caught up with a week of work, and in the same merge it stopped building.** `update-fixes` merged as `beevia-mobile` PR #42 at 15:45 UTC yesterday. It brought the escrowed chat send, `X-Device-Id` on the inbox fetch, an offline outbox, the minimised-call banner, and the fixes for the four QA items that 0901's sweep closed while their code was off `main`. But the commit that brought the branch up to date ("resolved some conflicts", 77 seconds before the merge) **left raw conflict markers in `pubspec.yaml`, `pubspec.lock` and the iOS project file.** `pubspec.yaml` no longer parses, so `flutter pub get` fails and no platform can build `main` as committed. The merge also brought in the biometric step-up, which the server rejects. `createConversation` still sends no `X-Device-Id`. Separately, **sprint 0902 more than doubled on its first afternoon**: board administration added 14 items, 13 of them an Appearance block (theme, dark mode, chat background, text size) that the PRD does not mention. The backend and admin repos were quiet. Nobody has moved anything on any board today.

**No correction this edition.** I re-derived the 30 Sep headline figures that today's data can check (mobile `X-Device-Id` coverage, 0902's composition at the time, the sweep counts in the 0901 sidecar). They hold.

| Metric | 30 Sep | 1 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 11 (11+0) | **25 (21+4)** | **+14** (13 created, 1 moved in from the backlog) |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / Done | 11 / 0 / 0 / 0 | **18 / 3 / 0 / 0** | 3 started (`BVA-I286`, `I318`, `I319`) |
| Sprint 0902 leaves with no basis in the PRD | 3 of 11 (Activity) | **12 of 21** (Activity 3, Appearance 9) | Appearance block added on day 1 (§2) |
| Sprint 0901 leaves Done | 67 of 67 | 67 of 67 | 0 (no reopen, no activity since the sweep) |
| Board actions in the window (all boards) | 68 (the sweep) | **28** | all on 0902, all 30 Sep 15:00–16:03 UTC, none on 1 Oct |
| `update-fixes` vs `beevia-mobile` `main` | 4 ahead · 100 files | **merged (PR #42), 0 ahead** | tree on `main` = branch tip |
| Files on mobile `main` with unresolved conflict markers (excluding old `.cxx` artefacts) | 0 | **3** (`pubspec.yaml`, `pubspec.lock`, `project.pbxproj`) | **new: `main` cannot `pub get`** |
| 0901 items marked Done whose fix was not on `main` | ≥4 | **0 of those 4** | all four fixes now on `main` |
| Mobile calls that omit the now-required `X-Device-Id` (`main`) | 2 | **1** (`createConversation`) | inbox fixed by the merge |
| Chat Send on `main` | `/payments/transfer` (no escrow) | **`payment.send` (escrowed)** | via PR #42 |
| Biometric step-up on mobile `main` (server accepts `{ pin }` only) | branch only | **on `main`** | `wallet_service.dart:78` |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | no backend commit in the window |
| `beevia-db-schema` Release gated on CI | no | **no** | unchanged since #19 |
| `beevia-mobile` days since a commit on `main` | 5.9 | **0.9** | |
| `beevia-api` days since a commit | 0.5 | **1.5** | |
| `beevia-admin-api` days since a commit on `main` | 6.1 | **7.1** | CI branch still pending |
| `beevia-admin` days since a commit | 7.9 | **8.9** | |
| Admin board: open sprint / days since any activity | none / 16.0 | **none / 17.0** | +1.0 |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/11 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈66% (65.52) | **≈67% (66.76)** | **+1.24**: #7 0.85→0.92, #2 0.80→0.85 (appendix) |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 4** (1 In progress, 3 To do) · 0901-admin: 3 | 5 (4 own; 1 board administration) | 0.98 d (n=10) | `BVA-I319` (0.9 d, moved with its parent, not by them) · `BVA-I8` on 0901-admin (**17.0 d**) | **28** | Three of their four 0902 items are new GET/PATCH endpoints for appearance preferences. `/users/me/settings` already exists for this (§2) |
| David Samuel | mobile | **0902: 15** (2 In progress, 13 To do) | 32 (11 own; 17 board administration; 4 Ayomikun) | 0.96 d (n=24) | `BVA-I286`, `BVA-I318` (0.9 d each) | **5 merged** (+ the merge) | Merged `update-fixes`, the ask of four editions. The conflict markers it carried break `main`'s build (§3.1). `createConversation` still lacks `X-Device-Id` |
| Philip Chidera | design | **0902: 2** (`BVA-I314`, `BVA-I321`), both To do | 3 (1 own; 2 board administration) | 0.55 d (n=2) | 0 | n/a | Two design items now gate two features: Activity (`I314`) and dark mode (`I321`) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**17.0 d**) | **0** | `beevia-admin` **8.9 days** without a commit. No admin sprint |

**The two questions for standup:** (1) **Who fixes `pubspec.yaml` on mobile `main` today, and is Flutter CI a required check?** The fix is to keep the 24 Sep dependency upgrade and add back `local_auth`, which the merged biometric code imports. The CI question is whether a red check could have stopped the merge. (2) **Do the three Appearance preferences need the server at all, and if so, can they be three fields on `/users/me/settings` instead of three new endpoint pairs?** Each item's acceptance criteria ask only for "persists across app restarts", which device storage already satisfies.

**The three things worth knowing:**

1. **The merge did what four editions asked, and the conflict resolution undid the result.** PR #42's tree is identical to `update-fixes`'s tip, so everything the branch held is now on `main`. That includes the escrowed send, the inbox device header and the four QA fixes (`BVA-I287`, `I292`, `I294`, `I303`). It also includes commit `21e042e`, which merged the 24 Sep dependency upgrade (#36) into the branch and committed both sides of the `pubspec.yaml` conflict, markers and all. The two sides disagree on real things. The branch side pins older plugin versions and adds `local_auth`. #36's side upgrades five plugins and has no `local_auth`. Picking either side wholesale loses something. The repo's own CI runs `flutter pub get` first and would have failed within seconds. The merge landed 77 seconds after the commit, by the branch's author. Whether CI ran, and whether it was required, cannot be seen from here (`suggestions.md` §5.12). This is a process gap, not a personal one. With no reviewer staffed (thirteenth edition), there was no second person to look at the merge before it landed.

2. **Two of the three client-contract problems from last week moved, one of them only part of the way.** The escrow bypass is fixed on `main`. The chat send now arms a step-up and emits `payment.send` over the socket (`chat_send_money_flow.dart:664`). `/payments/transfer` is left for the wallet tab's own send, which is instant by design. The `X-Device-Id` gap is half fixed: the inbox now sends the header, but `POST /conversations` (`chat_service.dart:204–206`) still does not. Once `beevia-api` #60 is deployed, starting a new chat returns `400`. The biometric step-up went the wrong way. It was on a branch, and now it is on `main`, offered on every money sheet, and rejected by `stepUpSchema` (`auth.dto.ts:77`). The PIN works.

3. **Sprint 0902 doubled on day 1, mostly with work the PRD does not mention, and none of it is estimated.** Yesterday's 11 items (push notifications, Activity tab, one UI fix) became 25. The 14 additions are `BVA-I312` (in-app notification banners, from the backlog) and an **Appearance** block of 4 parents and 9 leaves: Light/Dark/System theme, a dark palette applied to every screen, four chat backgrounds, and three text sizes for chat. The PRD mentions none of these. Three of the leaves are backend items, each "GET/PATCH endpoint for the … preference". `GET`/`PATCH /users/me/settings` already exists and returns one settings object, so three new endpoint pairs would be three times the surface for one screen. With the Activity tab, 12 of the sprint's 21 leaves now trace to nothing in the PRD. On day 2 of a 16-day sprint, David holds 15 of 21 leaves. With no estimation points, the board cannot say whether that fits.

**If you read nothing else:** `update-fixes` is finally on `main`, and with it the escrowed send and the four QA fixes. But `main` does not build until someone resolves the conflict markers in `pubspec.yaml`, and it still starts new chats without the header the API now requires. Sprint 0902 doubled overnight with an unestimated Appearance block that sits outside the MVP.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated.

| Status | 30 Sep | 1 Oct | Δ |
|---|---:|---:|---:|
| To do | 11 | **18** | +7 |
| In progress | 0 | **3** | +3 |
| REVIEW/QA | 0 | 0 | 0 |
| Done | 0 | 0 | 0 |
| **Total leaves** | **11** | **21** | **+10** |

**Every action in the window happened between 15:00 and 16:03 UTC on 30 Sep.** That is 28 audit entries, and there were none on 1 Oct up to 14:10 UTC.

- **15:00–15:44, board administration:** moved `BVA-I312` from the backlog and assigned it to David, then created the Appearance block: 4 parents (`BVA-I317`, `I320`, `I323`, `I326`) with 8 child leaves, plus one standalone leaf (`BVA-I329`, Appearance Settings Screen).
- **15:47, David:** `BVA-I286` (*Mismatched UI element on User Profile screen*) To do → In progress.
- **16:02:57, David:** `BVA-I317` (*Theme Infrastructure*) To do → In progress. Its two children followed in the same millisecond: `BVA-I318` (his) and `BVA-I319` (*Theme Preference Storage*, Ayomikun's). So `BVA-I319` being In progress is the parent's cascade, not Ayomikun starting it.

There were no comments, no re-assignments and no other status moves. The audit's `SINCE` block compares the frozen 08-01 exports and reports no movement, which is correct for that board and says nothing about 0902.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC); 67 of 67 leaves are Done, with no reopen. 0901-admin's last entry was on 14 Sep (§ Admin dashboard board). 08-01 has not moved since 3 Sep.

**What "Done" on 0901 means today.** The four items that the sweep closed while their fixes were only on `update-fixes` (`BVA-I287`, `I292`, `I294`, `I303`) now have those fixes on `main`, because the branch merged whole. But `main` does not currently build (§3.1), so none of them can be demonstrated on a `main` build yet. The other 53 swept queue items have still not been checked line by line.

---

## 2. Sprint 0902: what the additions ask for

| Item | Owner | Kind | In the PRD? |
|---|---|---|---|
| `BVA-I312` In-App Foreground Notification Banners | David | leaf | Yes, as part of notifications |
| `BVA-I317` Theme Infrastructure: Light, Dark & System Mode | David, Ayomikun | parent | **No** |
| ↳ `BVA-I318` Theme Token System & Runtime Switching | David | leaf | |
| ↳ `BVA-I319` Theme Preference Storage: *"GET/PATCH endpoint for the app-wide theme preference"* | Ayomikun | leaf | |
| `BVA-I320` Dark Mode Visual Design & Coverage Across All Screens | Philip, David | parent | **No** |
| ↳ `BVA-I321` Dark Mode Palette for Every Screen | Philip | leaf | |
| ↳ `BVA-I322` Apply Dark Palette & Check for Hardcoded Colors | David | leaf | |
| `BVA-I323` Chat Background Selection (White, Bone, Ink, Graphite) | David, Ayomikun | parent | **No** |
| ↳ `BVA-I324` Background Swatch Picker & Application | David | leaf | |
| ↳ `BVA-I325` Chat Background Preference Storage: *"GET/PATCH endpoint"* | Ayomikun | leaf | |
| `BVA-I326` Text Size / Font Scaling (chat only) | David, Ayomikun | parent | **No** |
| ↳ `BVA-I327` Scalable Typography & Live Preview Wiring | David | leaf | |
| ↳ `BVA-I328` Text Size Preference Storage: *"GET/PATCH endpoint"* | Ayomikun | leaf | |
| `BVA-I329` Appearance Settings Screen | David | leaf | **No** |

Three things to read from it:

- **The block is well specified.** Each parent has real acceptance criteria. For example, the System theme must follow an OS change live, and text scaling is chat-only and must update the preview immediately. That is better input than most of 0901 had.
- **The backend half should be one change, not three, and may not be needed.** `GET`/`PATCH /users/me/settings` already exists (`openapi.yaml`, `getMySettings`/`updateMySettings`) and currently carries one field, `messageHistorySyncEnabled`. Three enum fields on it (`theme`, `chatBackground`, `chatTextSize`) would cover all three items with no new route. First, though, decide whether the server needs to store them at all. Every acceptance criterion says "persists across app restarts", which on-device storage already does. Server storage only matters if the choice should follow the user to a new device. That is a product decision worth one line on `BVA-I317`. Neither form is in the proposed spec yet, so there is nothing to build against.
- **The sprint's balance changed.** Leaves by owner (co-assignment counted for both): David 15, Ayomikun 4, Philip 2. Nine leaves trace to the PRD's notifications scope or the UI audit (`BVA-I286`, `I306`–`I313`). The other 12 do not trace to the PRD: Activity (3) and Appearance (9). The Appearance block was added on day 1, with no estimation points.

`BVA-I315` (Activity Feed Backend) is unchanged. Its description still asks the server for "last message text" previews and for search across message content, which E2EE rules out (30 Sep §2).

---

## 3. Code, API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. This was run against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-01`). The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees, and its `SINCE` block compares two identical frozen 08-01 exports. Neither was acted on. **No spec file changed this cycle.** No backend repository had a commit in the window.

### 3.1 `beevia-mobile` PR #42: `update-fixes` merged, with conflict markers

| Commit | Time (UTC) | Author | What |
|---|---|---|---|
| `0973bbc` "local changes" | Wed 30 Sep 14:42 | `Davidtariq96` | iOS project file only (+23 / −15) |
| `21e042e` "resolved some conflicts" | Wed 30 Sep 15:43 | `Davidtariq96` | Merges `main` (#36, the 24 Sep dependency upgrade) into the branch. 23 files |
| `d51e3d1` Merge PR #42 | Wed 30 Sep 15:45 | David Samuel | Lands the branch. The tree is identical to `21e042e` |

**What reached `main`** (`2094afd..d51e3d1`: 84 files, +5,317 / −993). Escrowed chat send (`payment.step_up` + `payment.send`); `X-Device-Id` on the inbox fetch; an offline outbox (`outbox_store.dart`, with tests); the minimised-call banner and call-audio routing; transaction receipt cards; the E2EE notice; wallet-provider and screen changes; biometric step-up (`biometric_auth_service.dart`, `wallet_service.dart:75–78`); l10n strings in four languages; and mock-server routes.

**What is broken on `main`:**

| File | Conflict blocks | Consequence |
|---|---:|---|
| `pubspec.yaml` | 1 (lines 41–66) | Invalid YAML. `flutter pub get` fails, so there is no build or test on any platform |
| `pubspec.lock` | 5 | Invalid YAML |
| `ios/Runner.xcodeproj/project.pbxproj` | 11 | Xcode cannot open the project |

The `pubspec.yaml` block is a real choice. `HEAD` (the branch) has `permission_handler` ^11, `flutter_secure_storage` ^10, `file_picker` ^10, `google_mlkit_*` ^0.14, `flutter_contacts` pinned to 2.1.0 "until the Android toolchain upgrades", **and `local_auth`**. #36's side has the upgrades (^13, ^11, ^13, ^0.15, ^2.3.1) and **no `local_auth`**. The merged `biometric_auth_service.dart:1` imports `package:local_auth`. The right resolution is probably #36's versions plus `local_auth`, after checking the AGP note.

The four `android/app/.cxx/**/configure_fingerprint.bin` files have carried conflict markers since July. They are tracked build artefacts and do not affect a build, but they should be untracked (`suggestions.md` §5.12).

**Client contracts at the new `main`:**

| Contract | 30 Sep `main` | 1 Oct `main` |
|---|---|---|
| Chat Send → escrow | `/payments/transfer` (instant, no escrow) | **`payment.send` over the socket, after `payment.step_up`** |
| `GET /conversations` sends `X-Device-Id` | no | **yes, when a device id is known** (`chat_service.dart:34`) |
| `POST /conversations` sends `X-Device-Id` | no | **no** (`chat_service.dart:204–206`) |
| Step-up methods offered | PIN | **PIN + biometric.** The server accepts `{ pin }` only (`auth.dto.ts:77`) |
| Phone field on escrowed sends | n/a | `payments.dto.ts:5` is still `z.string().trim().min(6).max(20)`, now on the main payment path |

### 3.2 Backend and CI: unchanged

- No commits on any backend `main` in the window. `beevia-api` last merged #61 (30 Sep 03:21 UTC). `beevia-db-schema` last released v0.0.38 (30 Sep 02:15 UTC). `beevia-admin-api` last merged #18 (24 Sep).
- **`beevia-db-schema` Release still triggers on push to `main` with no `needs:` on a verify job** (`release.yml` lines 3–6), so 30 Sep §3.2 stands.
- `beevia-admin-api` `origin/ci/node-26-only` (`66737d7`) is still unmerged, 2 ahead, and still contains the same ungated deploy-chain change.
- **Reflog sweep:** no forced update in any of the five repos in the window.
- New in `beevia-mobile`: five Dependabot branches (30 Sep 03:54 UTC: Android Gradle plugin 9.4.1, Gradle wrapper 9.8.0, Compose BOM, Crashlytics, and a minor/patch group). The branch `origin/App-bundle` points at `2094afd` and is 0 ahead of `main`, so it is fully contained.
- **Deploy state of `beevia-api` #60 is still not visible.** The GitHub token here gets `404` from the org's Actions API, so CI results cannot be read either.

### 3.3 Document changes this cycle

| File | Change |
|---|---|
| `suggestions.md` | **New §5.12** on the conflict markers on mobile `main`. **§5.11 update:** biometric step-up is now on `main`. **§8:** 3e updated, new 3f |

`openapi*.yaml`, `api-rfc.md` and `admin-api-rfc.md` are unchanged. No route moved, and the Appearance endpoints have no contract to record yet (§2).

---

## 4. Risks

- **Mobile `main` does not build** (§3.1). **New today.** It is a one-file fix with a choice in it. Until it is made, anyone building from `main` gets a YAML parse error, and every open PR inherits it.
- **"Start a chat" breaks once #60 deploys.** That is still true on `main`, though the inbox half is fixed. One header.
- **Biometric step-up is live on `main` and fails against the real API** on every money sheet (`suggestions.md` §5.11). Users can fall back to the PIN, but the button implies a server capability that does not exist.
- **A push to `beevia-db-schema` `main` migrates production with no CI.** This is unchanged, and the same change is pending for `beevia-admin-api`.
- **The unparsed phone field (`payments.dto.ts:5`) is now on the main payment path**, because escrowed chat sends go through it.
- **Sprint 0902 scope doubled on day 1 with no estimates.** The new half is outside the MVP, and 15 of 21 leaves sit with one person.
- **`BVA-I315` is still specified against E2EE.**
- **The admin workstream is silent:** 8.9 days with no repo commit, 17.0 days with no board activity, and no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

The four structural gaps are where they were: the international KYC tier, multi-currency/FX settlement, virtual cards beyond what is wired, and consent management. `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged, because no backend commit landed.

**What PR #42 closed.** It closed the PRD's *Transfer Acceptance & Escrow* gap on the client side (§10.2, Flow 5, §11 Phase 3). It is the first client build that sends chat money through escrow. The 28 Sep edition lowered capability #7 for exactly this bypass. Today that is reversed in part (appendix).

**What 0902 adds to the gap.** Nothing in the Appearance block closes a PRD gap. Neither do the Activity tab or the notification work, which make an existing surface usable. That can be a reasonable choice for a sprint. It is worth saying out loud, because the four structural gaps account for 32 of the rubric's 100 points, and no board item on any open sprint touches them.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 24 Sep 14:10 → 1 Oct 14:10 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities, with bots excluded. **The 30 Sep sweep is not a submission and is not counted as anyone's output.**

### 6.1 Ayomikun Araoye: backend + admin API

**28 commits in 7 days:** `beevia-api` 16 (`Phoenixdadhev` 14, `Ayomikun Araoye` 2), `beevia-db-schema` 12 (11 + 1), `beevia-admin-api` 0. None landed in the window. The count fell from 32 because older commits rolled out of the window, not because of anything that happened today. On 0902 they own four leaves. Three are the Appearance preference endpoints (§2), which are worth a design conversation before they become three routes. The fourth is `BVA-I315`, whose acceptance criteria still need the E2EE correction. `BVA-I319` shows In progress only because its parent was moved. `BVA-I8` has been In progress on the admin board for 17.0 days. Submissions in 7 days: 5 (4 own, 1 by board administration). Median cycle time 0.98 d (n=10).

### 6.2 David Samuel: mobile

**5 commits merged to `main` in 7 days** (`Davidtariq96`; plus the conflict-resolution merge `21e042e` and the PR merge, which are excluded as merges). Nothing is left unmerged. Merging the branch is what four editions asked for, and it brought real, board-requested work onto `main` (§3.1). The conflict markers are the cost of resolving a dependency conflict without a build in the loop. That is a missing control, not carelessness: nothing in this repo stopped it. On the board, David started `BVA-I286` and the theme infrastructure within minutes of the merge, and holds 15 of 0902's 21 leaves. Submissions to REVIEW/QA in 7 days (owner rows): 32 (11 own, 17 board administration, 4 Ayomikun on co-owned items), all from before the 0901 sweep. Median cycle time 0.96 d (n=24).

### 6.3 Philip Chidera: design

No board action in the window. They own `BVA-I314` (Activity tab design) and now `BVA-I321` (dark palette for every screen). Each one gates a feature: Activity backend and screen wait on the first, and the dark palette application waits on the second. No commits, because design work does not land in these repositories.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **8.9 days** ago. The admin board has had no activity for 17.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work.** `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the fourth edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 |
|---|---:|---:|
| 2026-W37 | 7 | — |
| 2026-W38 | 11 | — |
| 2026-W39 | **42** | — |
| 2026-W40 (from Mon 28 Sep) | 1 | 0 |

Acceptances by someone other than the submitter: **none**, apart from the two bulk sweeps (3 Sep and 30 Sep).

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more. This is the twentieth edition to say so.
- **"Submitted" counts any transition into REVIEW/QA, by anyone**, and credits it to the item's owner. For David, 17 of 32 were board administration's moves.
- **Commit counts reward small commits.** `21e042e` is one commit and 23 files. `edcadef`, counted last week, was 44.
- **A parent's cascade is not a start.** `BVA-I319` shows In progress without its owner touching it.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The `pubspec.yaml` finding comes from parsing the file, not from running Flutter.

---

## 7. Previous recommendations: where they stand

| Recommendation from 30 Sep | Status on 1 Oct |
|---|---|
| **1. Add `X-Device-Id` to `createConversation`** | ◐ **Half.** The inbox now sends it (via PR #42). `createConversation` does not (`chat_service.dart:204–206`) |
| **2. Merge `update-fixes`, without the biometric option; add it to 0902 as an item** | ◐ **Merged, with the biometric option and with conflict markers** (§3.1). No board item records it |
| **3. Gate `beevia-db-schema`'s Release on the verify job; same for `beevia-admin-api`'s branch** | ❌ **Not done.** `release.yml` is unchanged. The admin-api branch is still pending, unchanged |
| **4. Correct `BVA-I315`'s acceptance criteria for E2EE** | ❌ **Not done.** The description is unchanged |
| **5. Decide what REVIEW/QA and Done mean on 0902, and name a reviewer** | ❌ **Not done.** Thirteenth edition. Today's merge is the first cost of it on `main` |
| **6. Say what Done means for `BVA-I260`, `I275`, `I277`** | ❌ **No comment** on any of them |
| **7. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho still lists only `0901-admin` |
| **8. Estimate 0902** | ❌ **Not done, and the sprint grew** to 25 items, 0 estimated |
| **9. Bring `payments.dto.ts` onto `phone.util.ts` before item 2 lands** | ❌ **Not done, and item 2 landed.** Line 5 is unchanged |
| **10. Carried: OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec** | ❌ **None done** |

**Two of ten moved, both partly, both through the one mobile merge.** The rest did not move. Most of them sit with the backend, which had no commits in the window.

---

## 8. What I would do this week

1. **Fix `pubspec.yaml`, `pubspec.lock` and `project.pbxproj` on `beevia-mobile` `main` today.** Take #36's dependency versions, add `local_auth`, regenerate the lock file, and re-open the iOS project. Then make Flutter CI a required check on `main` (`suggestions.md` §5.12), which is what would have stopped this.
2. **Add `X-Device-Id` to `createConversation`** in the same change. It is the last call on `main` that #60 will reject.
3. **Hide the biometric option outside mock mode** until the server has a verifiable biometric step-up (`suggestions.md` §5.11).
4. **Decide where Appearance preferences live** before `BVA-I319`, `I325` and `I328` start. Use device storage, or three fields on the existing `/users/me/settings`. Not three new endpoint pairs. Write one line on `BVA-I317`.
5. **Estimate 0902, and say whether the Appearance block is in or out.** It is 25 items, 13 of them an Appearance block added on day 1 that the PRD does not mention.
6. **Gate `beevia-db-schema`'s Release on the verify job**, and fix `beevia-admin-api`'s pending branch before it merges.
7. **Correct `BVA-I315`'s acceptance criteria for E2EE.**
8. **Name a reviewer for 0902 and write down what REVIEW/QA and Done mean.** Today's merge shows what happens on `main` without one, not only on the board.
9. **Bring `payments.dto.ts` onto `phone.util.ts`.** It is now on the main payment path.
10. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
11. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 17.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 17 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 8.9 days without a commit and `beevia-admin-api`'s `main` 7.1 days. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, +1.24)

**Target 2026-09-01 (provisional). The target date passed thirty days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance. They also do not measure whether the code compiles: correctness and testing are out of the rubric's scope. So today's movement assumes the three conflicted manifests get resolved, and the Dart sources that implement the flows are intact. If `main` is still unbuildable at the next edition, that belongs in the overview, not in the strip.

**Two scores moved, both on evidence from the PR #42 diff:**

- **#7 Send / request / receive: 0.85 → 0.92.** The chat Send on `main` now arms `payment.step_up` and emits `payment.send` (`chat_send_money_flow.dart:664–690`), which is the escrowed flow. That is the condition the 28 Sep edition set for restoring this score. It stops short of 0.95 because one of the two authorisation options on that sheet (biometric) is posted in a shape the server rejects (`auth.dto.ts:77`).
- **#2 Voice & video calling: 0.80 → 0.85.** Call-audio routing and the minimised-call banner (`minimized_call_banner.dart`, `call_audio_route.dart`) moved from the branch to `main`.

**#1 E2EE messaging is held at 0.90.** The merge added the E2EE notice, the offline outbox and the inbox device header. `createConversation` still omits `X-Device-Id`, which #60 rejects once deployed. Net: held.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Inbox header, E2EE notice and outbox now on `main`. `createConversation` still omits `X-Device-Id` |
| 2 | Voice & video calling | 8 | 0.85 | +0.05 | Minimised-call banner and audio routing on `main` (PR #42) |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged. Wallet screen changes on `main` are within NGN |
| 7 | Send / request / receive in chat | 12 | 0.92 | +0.07 | Escrowed `payment.send` on `main`. Biometric option rejected by the server |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change on the backend |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep. No `beevia-admin-api` `main` commit since 24 Sep |
| | **Weighted total** | **100** | **66.76** | **+1.24** | **≈67%** |

### What this report cannot tell you

- **Whether `beevia-api` #60 is deployed.** The `createConversation` failure applies from the moment it is.
- **Whether `beevia-mobile` CI ran on PR #42, failed, or is required.** The Actions API returns `404` to this workspace's token.
- **Whether anyone has a local fix for `pubspec.yaml`.** Only pushed branches are visible.
- **Whether the 53 swept 0901 queue items not individually checked are fixed on `main`.**
- **Whether a direct push to any backend `main` is possible.** Branch protection cannot be seen from a clone.
- **Velocity for any sprint.** Nothing on any board is estimated (0 of 25, 0 of 76, 0 of 12, 0 of 64).

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
4. Read-only scratch exports: sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0) and sprint 0901 to `/tmp/beevia-scratch/` (76 items, `--no-descriptions --activity`, exit 0, to check for reopens).
5. Fast-forward sync (step 2): `beevia-mobile` +7 commits, `beevia-admin` already current, three refused as `diverged`. Then `git fetch --all --prune` of all five, read-only.
6. Reflog sweep of all five repos for forced updates. None were found in the window.
7. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-01`: route level and spec health clean. The in-repo audit was run too, for the board section. Its 21 drift lines are the known phantom from the diverged trees.
8. Activity-sidecar sweep of the window across 0902, 0901 and 0901-admin. Status transitions, comments and completions were matched on all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`).
9. Content reads: `beevia-mobile` PR #42 (`git diff 2094afd d51e3d1`, `git show 21e042e`, conflict-marker `git grep` at `origin/main`, a YAML parse of `pubspec.yaml` via `git show`), `X-Device-Id`/`payment.send`/biometric `git grep` at `origin/main`, and `stepUpSchema` and `payments.dto.ts` at `beevia-api` `origin/main`. Also `release.yml` at `beevia-db-schema` `origin/main`, and `/users/me/settings` in `openapi.yaml`.
10. Edits to `suggestions.md`, then this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Cycle times are `In progress` → `REVIEW/QA` pairs on 0901 leaves.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose transitions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync and `fetch`, the only git operations were `git archive` and read-only `log`/`diff`/`grep`/`show`/`reflog`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-01.html`, `web-report/index.html` and `suggestions.md`, plus new board exports for 1 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export. Moving the filter to `0902` would fix both.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all three projects. This is the known 50-row sampling artefact, not a scope gap. On 0901 the column resolves (`Language` 18, `Notification` 6, `security` 5). On 0902 all 25 items are genuinely unassigned.

**Window.** 30 Sep 14:03 UTC → 1 Oct 14:10 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
