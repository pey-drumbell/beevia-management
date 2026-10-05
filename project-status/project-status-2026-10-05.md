# Beevia — Project Status

**As of 2026-10-05** · Sprint **0902** (30 Sep → 15 Oct): **day 6 of 16, 25 items, 7 leaves In progress, 1 Done, 0 ever submitted to REVIEW/QA** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-05.csv` + `beevia-activity-2026-10-05.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-05.csv` + its activity sidecar (12 items, sprint 0901-admin); read-only scratch exports of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/` (diffed against the 2 Oct file in the same folder) and sprint 0901 (76 items) in `/tmp/beevia-scratch/`, each with its sidecar. All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 2 Oct 14:05 UTC → 5 Oct 16:46 UTC, 3.1 days including a weekend.**

---

## Quick overview

> **Nothing reached any `main` branch in three days, so mobile `main` has now been unbuildable for five days and every backend deploy is still ungated.** The only code that moved is a second commit on David's `BVA-I317` branch, pushed an hour before this report. It moves 60 more screens onto the new theme tokens. That is real progress on the dark-mode work, but it makes the branch that holds the `pubspec` fix bigger: it is now 87 files (+2,171 / −1,097), and the fix still cannot reach `main` without the whole Appearance feature. `project.pbxproj` keeps its 11 conflict blocks on `main` and on the branch. No backend repository has had a commit since 1 Oct, so all three still deploy or migrate production on push with no test gate. On the board, Philip closed the Activity-tab design and started the dark-mode design. A fourth item, money notifications, gained Ayomikun as a co-owner, and that one needs real backend work. **Nobody on any board has submitted anything to REVIEW/QA in seven days.**

**Correction.** The 2 Oct edition said Philip's `BVA-I321` dark-palette design "may arrive after the code it was meant to drive." In fact, the first `BVA-I317` commit (`03a3035`) said in its own comment that the dark values were *"taken from the Figma dark-mode 'Home screen | Appearance' frame (node 2959:29904) and extended to the remaining tokens."* The palette came from one existing design frame, and the developer extrapolated the rest. `BVA-I321` covers that rest, so it is a check on extrapolated values, not a design that arrives after its code. Today's commit deleted that provenance comment, so the reference to the Figma frame now survives only in history.

| Metric | 2 Oct | 5 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / Done | 16 / 5 / 0 / 0 | **13 / 7 / 0 / 1** | `BVA-I314` Done; `I321`, `I322` started (one parent move) |
| Board actions in the window (all boards) | 3 | **5** | 4 by Philip on 2 Oct 14:18 UTC; 1 owner change on 5 Oct |
| Transitions into REVIEW/QA, last 7 days (all boards) | 20 | **0** | the last was 28 Sep 15:14 UTC |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no backend commit since 1 Oct |
| Files on mobile `main` with conflict markers (excluding `.cxx`) | 3 | **3** | unchanged, **day 5** |
| …on `origin/BVA-I317` | 1 | **1** (`project.pbxproj`, 11 blocks) | unchanged |
| `origin/BVA-I317` size vs `main` | 1 commit, 36 files | **2 commits, 87 files, +2,171 / −1,097** | `6f38116` "app theming", 5 Oct 15:37 UTC |
| Files still importing the old `colors.dart` (`main` → branch) | 57 → 55 | **57 → 15** | 64 files now read `context.colors` |
| Mobile calls that omit `X-Device-Id` (`main` / `BVA-I317`) | 1 / 0 | **1 / 0** | unchanged |
| Biometric step-up offered on `main` (server accepts `{ pin }` only) | yes | **yes** | also on the branch |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | no backend commit |
| `beevia-mobile` days since a commit on `main` | 1.9 | **5.0** | branch commit 0.04 d ago |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 0.9 / 0.9 | **4.0 / 4.0 / 4.0** | |
| `beevia-admin` days since a commit | 9.9 | **13.0** | |
| Admin board: open sprint / days since any activity | none / 18.0 | **none / 21.1** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: nothing reached `main` |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 5** (2 In progress, 3 To do) · 0901-admin: 1 In progress | 0 | 0.98 d (n=10) | `BVA-I319` (5.0 d), `BVA-I328` (3.2 d): **both started by a parent move, not by them** · `BVA-I8` on 0901-admin (**21.1 d**) | **4** | No commit since 1 Oct. Newly co-owns `BVA-I310`, which needs payment reminders the server does not have |
| David Samuel | mobile | **0902: 15** (4 In progress, 11 To do) | 0 | 0.96 d (n=24) | `BVA-I286`, `BVA-I318` (5.0 d), `BVA-I327` (3.2 d), `BVA-I322` (3.1 d, started by Philip's parent move) | **2** on `main` (+2 on `BVA-I317`) | Today's commit is the `BVA-I322` work. `main` is unbuildable for a fifth day, and the fix is on the same branch |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` In progress (3.1 d) | 0 | 0.55 d (n=2) | `BVA-I321` | n/a | Closed `BVA-I314` straight from To do to Done, so no review |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**21.1 d**) | **0** | `beevia-admin` **13.0 days** without a commit. No admin sprint |

**The two questions for standup:** (1) **Can the build fix go to `main` on its own today?** It is three files and `project.pbxproj` on a branch that is now 87 files. Each day the theme work grows, separating the fix gets harder. (2) **Is 0902's REVIEW/QA column going to be used?** It is day 6 of 16, and all 7 In-progress leaves are older than their owner's median cycle time. Nothing has been submitted, and no reviewer is named.

**The three things worth knowing:**

1. **The build fix is getting harder to separate, not easier.** On 2 Oct the fix for mobile `main` (`pubspec.yaml`, `pubspec.lock`, the `createConversation` header) was one commit of 36 files, already bundled with the theme work. Today's `6f38116` adds 60 files that change only colours: screens move from the old `colors.dart` constants to `context.colors`, and the old imports fall from 57 files to 15. None of it touches the fix. Yet the fix can still reach `main` only by merging the whole Appearance feature, whose parents are still In progress. Taking the three files across is still a small job: a `git checkout origin/BVA-I317 -- pubspec.yaml pubspec.lock` plus the two chat files. The iOS project file is conflicted on both refs, so that part needs someone who can open Xcode either way. Mobile `main` has been unbuildable since 30 Sep 15:45 UTC.

2. **Zero submissions to review in seven days, on any board.** The last transition into REVIEW/QA anywhere was `BVA-I298` on 28 Sep 15:14 UTC. On 0902, nothing has been submitted in six days. Seven leaves are In progress, all older than their owner's median cycle time (0.96–0.98 d). Three of those seven were started by a parent cascade rather than by their owner. The one completion, `BVA-I314`, went straight from To do to Done, closed by its own owner. That is not a sign of idle developers: David pushed a 60-file commit today. It means the board's review step is not being used, and with no named reviewer and no definition of Done, nothing prompts anyone to use it. The standing record holds: **apart from the two bulk sweeps (3 Sep and 30 Sep), no item on any board has ever been accepted by someone other than its submitter.**

3. **`BVA-I310`'s new backend owner has real work, unlike the Appearance items.** Board administration added Ayomikun to *Money Notification Handling* this morning (10:50 UTC). The item asks for four money notification types and **two reminders during a pending transfer's 24-hour window**, at 12 hours and 1 hour before expiry. The server already sends payment notifications (`notifyPayment`) and expires holds through a BullMQ `escrow-expiry` queue (`ESCROW_HOLD_TTL_MS` = 24 h). It has **no reminder scheduling**: the word `remind` does not appear in `beevia-api/src`. This is the first 0902 backend item with a clear server gap. By contrast, the client already stores the three Appearance preferences on the device, so those items still have no caller (2 Oct §2), and two of them still show In progress.

**If you read nothing else:** three days passed with no merge anywhere. Mobile `main` is still broken, every backend deploy is still untested, and nobody has submitted anything to review in a week. The build fix is three files. Take them across on their own today.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The comparison is file-level, against the 2 Oct scratch export in `/tmp/beevia-scratch/0902/`, which survived this time.

| Status | 2 Oct | 5 Oct | Δ |
|---|---:|---:|---:|
| To do | 16 | **13** | −3 |
| In progress | 5 | **7** | +2 |
| REVIEW/QA | 0 | 0 | 0 |
| Done | 0 | **1** | +1 |
| **Total leaves** | **21** | **21** | **0** |

**The window holds five audit entries:**

| Time (UTC) | Item | Who | What |
|---|---|---|---|
| 2 Oct 14:18:41 | `BVA-I314` *Complete the Activity Tab Design* | Philip | **Item Completed**, To do → Done. Never In progress, never in review |
| 2 Oct 14:18:46 | `BVA-I320` *Dark Mode Visual Design & Coverage* (parent) | Philip | To do → In progress |
| 2 Oct 14:18:46 | `BVA-I321` *Dark Mode Palette for Every Screen* (Philip's) | cascade | To do → In progress |
| 2 Oct 14:18:46 | `BVA-I322` *Apply Dark Palette & Check for Hardcoded Colors* (David's) | cascade | To do → In progress |
| 5 Oct 10:50:13 | `BVA-I310` *Money Notification Handling* | board administration | Added owner Ayomikun Araoye (co-owner with David) |

There were no comments on any board in the window, no new items, no description edits and no reopens. Every 0902 item still has a blank Epic and 0 estimation points. Because `BVA-I314` skipped the queue, the board has no record of anyone checking the Activity design against its own acceptance criteria. Those criteria are specific: per-type row treatment for chat, call and payment, a resolved placeholder icon, and an unread rule. `BVA-I316` (*Build the Activity Screen*, David) and `BVA-I315` (*Activity Feed Backend*, Ayomikun) build against that design, and both are still To do.

**Board versus code.** `BVA-I322` was started by Philip's parent move, not by David. Even so, today's commit is exactly that item's work: *"replace hardcoded colors with references to theme tokens"*. So for once the cascade matches reality. `BVA-I324` and `BVA-I329` remain To do with code on the branch (2 Oct §2).

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC). All 67 leaves are Done, there has been no reopen ever, and no comment since. 0901-admin's last entry is 14 Sep 14:53 UTC (§ Admin dashboard board). 08-01's last entry is 3 Sep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 6

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | all To do | none on any branch. `BVA-I310` now co-owned by Ayomikun (§ Quick overview, 3) |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done (self-closed); backend and screen To do | none. `BVA-I315` still asks for server-side message previews that E2EE rules out |
| Appearance (`BVA-I318`–`I329`) | 9 | 6 In progress (3 by cascade), 3 To do | most of it on `BVA-I317`: tokens, dark palette, chat backgrounds, text size, settings screen, and now 64 screens migrated |
| Carried bug `BVA-I286` | 1 | In progress, 5.0 d | not identified on any branch |

Ten days remain. The Appearance block, which the PRD does not mention, is the only one with code. Eight of the 21 leaves are the push-notification block, and none of them has started. Without estimates, the board cannot say whether the remaining ten days are enough. The Appearance storage decision is still unrecorded: there is no comment on `BVA-I317`, `I323` or `I326`. Two of Ayomikun's three preference-endpoint items still show In progress because of David's parent moves on 30 Sep and 2 Oct.

---

## 3. Code, API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. This was run against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-05b`). The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees. They were not acted on. **No spec file or narrative document changed this cycle**, because no backend repository has had a commit since 1 Oct.

### 3.1 `beevia-mobile`: `main` unchanged, branch grows

`main` is still `d51e3d1` (PR #42, 30 Sep 15:45 UTC). Conflict markers on `main`: `pubspec.yaml` 1 block, `pubspec.lock` 5, `project.pbxproj` 11. That is unchanged.

**`origin/BVA-I317`** gained `6f38116` "app theming" (`Davidtariq96`, 5 Oct 15:37 UTC). The branch is now 2 ahead of `main` and 0 behind, with 87 files, +2,171 / −1,097.

| Change in `6f38116` | Detail |
|---|---|
| 59 screen and widget files across chat, call, onboarding, wallet, settings and home | Hard-coded `colors.dart` constants replaced with `context.colors` tokens. Files still importing the old palette: 55 → **15**. Files reading tokens: 5 → **64** |
| `app_colors.dart` | New `hairline` token (light `deepBlack100`, dark Gray/700). **The comment citing the Figma dark-mode frame was deleted** |
| `chat_send_money_flow.dart` | Colour changes only. The biometric option (`_verifyBiometrics`) is still on both send sheets |
| `pubspec.*`, `ios/`, `android/`, `chat_service.dart` | untouched in this commit. The branch's earlier fixes stand; `project.pbxproj` keeps 11 blocks |

The commit is a mechanical, repo-wide token migration. That is the right way to do `BVA-I322`, and it leaves a short tail of 15 files. It does not change the packaging problem: the build fix and the feature still travel together.

Remote branches: `main`, `BVA-I317` (2 ahead), `update-fixes` (contained), `App-bundle` (contained) and five Dependabot branches from 30 Sep.

### 3.2 Backend and CI: no change

No commit on any backend `origin/main` since 1 Oct 15:59 UTC. Re-read in full at `origin/main` today:

| Repo | Push-to-production chain | Test gate |
|---|---|---|
| `beevia-api` | `release.yml`: `push` to `main` → `sync` → `deploy` (`needs: sync`) | **none**. `sync` has no `needs: test` |
| `beevia-admin-api` | `sync.yml`: `push` to `main` → `deploy.yml` (`workflow_run` on Sync) | **none**. CI is `pull_request` only |
| `beevia-db-schema` | `release.yml`: `push` to `main` → `sync.yml` (`workflow_run` on Release, production migration) | **none** |

**Reflog sweep:** every `origin/main` update in all five repos was a fast-forward. None of them moved in the window.

### 3.3 Document changes this cycle

None. `openapi*.yaml`, `api-rfc.md`, `admin-api-rfc.md` and `suggestions.md` are unchanged. No route, contract or recommendation moved enough to need an edit. §5.11, §5.12 and §7.7 in `suggestions.md` still describe the current state.

---

## 4. Risks

- **Mobile `main` does not build, day 5** (§3.1). The fix is written but coupled to a feature branch that grew by 60 files today. iOS has no fix anywhere.
- **Every backend repo deploys or migrates production on push without a test gate** (§3.2). Unchanged. How severe this is depends on branch protection, which nobody here can see.
- **Production SSH accepts connections from any address**, per the 1 Oct deploy commits' own description. Unverified, unchanged.
- **The review step is unused.** There have been no submissions in seven days. The one completion skipped review, and there is no named reviewer and no definition of Done.
- **"Start a chat" breaks once `beevia-api` #60 deploys**, on `main`. The fix is on `BVA-I317`, and deploy state is still not visible.
- **The biometric step-up on `main` fails against the real API** on every money sheet (`suggestions.md` §5.11).
- **0902 has 8 untouched push-notification leaves, 10 days left and no estimates.** One of them (`BVA-I310`) needs reminder scheduling the server does not have.
- **`BVA-I315` is still specified against E2EE.**
- **The admin workstream is silent:** 13.0 days with no `beevia-admin` commit, 21.1 days with no board activity, and no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. The only code movement in the window is Appearance theming on a branch, which the PRD does not mention. `BVA-I310`'s payment reminders do serve the PRD's Transfer Acceptance & Escrow flow (§10.2), so that is the one 0902 item that touches an MVP capability.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 28 Sep 16:46 → 5 Oct 16:46 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. WIP ages run from each item's last entry into In progress.

### 6.1 Ayomikun Araoye: backend + admin API

**4 commits in 7 days**, all as `Phoenixdadhev`: in `beevia-api`, required `X-Device-Id` (`f1d5a40`), NestJS Observe (`9e4c811`) and the hosted-runner move (`fa5a5de`); in `beevia-db-schema`, the hosted-runner move (`aabd858`). The last was 1 Oct 15:48 UTC, **4.0 days** ago. The count fell from 11 because last week's CI commits rolled out of the window. On 0902 they hold five leaves. Two are In progress only because David moved their parents (5.0 d and 3.2 d). One is the Activity Feed backend (To do, still blocked on the E2EE question). One is the new co-ownership of `BVA-I310`, the first 0902 item with a clear server gap (§ Quick overview, 3). `BVA-I8` has been In progress on the admin board for 21.1 days. Submissions in 7 days: 0. Median cycle time 0.98 d (n=10, all on 0901).

### 6.2 David Samuel: mobile

**2 commits on `main` in 7 days** (`edcadef` 29 Sep, `0973bbc` 30 Sep, both reached `main` through PR #42), **plus 2 on `origin/BVA-I317`** (2 Oct and today). Today's commit is a mechanical migration of 59 files to theme tokens, and it is the actual work of `BVA-I322`. The open problem is packaging, as it was on 2 Oct: the build fix rides the feature branch. That is a process gap, not his. With no reviewer and no required CI on `main`, nothing asks for the fix to be split out. He holds 15 of 0902's 21 leaves, 4 In progress. All four are older than his 0.96-day median, and the two oldest are 5.0 d. `BVA-I286` (a mismatched profile-screen element, carried from 0901) could not be matched to code on any branch. Submissions in 7 days: 0.

### 6.3 Philip Chidera: design

On 2 Oct at 14:18 UTC they closed `BVA-I314` (Activity tab design) and started the dark-mode design parent `BVA-I320`, which also moved their `BVA-I321` and David's `BVA-I322` to In progress. Whether the Activity design meets its acceptance criteria is not recorded, because the item skipped review. `BVA-I321` has been In progress for 3.1 days. It is now the check on the dark values the developer extrapolated from one Figma frame (see the correction). No commits, because design work does not land in these repositories.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **13.0 days** ago. The admin board has had no activity for 21.1 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the sixth edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 |
|---|---:|---:|
| 2026-W37 | 7 | — |
| 2026-W38 | 11 | — |
| 2026-W39 | **42** | — |
| 2026-W40 (28 Sep → 4 Oct) | 1 | **0** |
| 2026-W41 (from Mon 5 Oct) | — | 0 |

Submission rate against acceptance rate: both are zero this week. Last week's pattern (42 submitted, none accepted except by the sweep) has become a column nobody uses. The bottleneck is still the missing review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more.
- **A parent's cascade is not a start.** Three of 0902's seven In-progress leaves were moved by a parent: `BVA-I319` and `I328` (Ayomikun's, by David) and `BVA-I322` (David's, by Philip).
- **Commit counts reward small commits.** David's one commit today is 60 files. Two of Ayomikun's four are workflow edits.
- **Branch work is invisible to the board.** `BVA-I317` holds the work of at least five 0902 leaves.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 2 Oct | Status on 5 Oct |
|---|---|
| **1. Land the build fix on mobile `main` without the theme feature; resolve `project.pbxproj`; require Flutter CI** | ❌ **Not done.** `main` unchanged. The branch grew by 60 files. `project.pbxproj` still has 11 blocks on both refs |
| **2. Put `needs: test` back on `beevia-api`'s `sync`; gate db-schema Release and admin-api Sync** | ❌ **Not done.** No backend commit |
| **3. Check the production host's SSH settings** | ? **Not visible from here** |
| **4. Write the Appearance storage decision on `BVA-I317`** | ❌ **Not done.** No comment on any Appearance parent |
| **5. Hide the biometric option outside mock mode** | ❌ **Not done**, on `main` or the branch |
| **6. Estimate 0902; agree whether `BVA-I321` reviews the branch palette or replaces it** | ◐ **Half.** 0 of 25 estimated. `BVA-I321` started on 2 Oct, and the correction above answers the second half: the branch palette came from one Figma frame |
| **7. Correct `BVA-I315`'s acceptance criteria for E2EE** | ❌ **Not done.** No description edit |
| **8. Name a reviewer for 0902; define REVIEW/QA and Done** | ❌ **Not done.** Fifteenth edition. The one 0902 completion skipped review |
| **9. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **10. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **11. Carried: comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec** | ❌ **None done** |

**None of eleven fully moved; one moved by half.** Nothing merged anywhere in the window, so most of these could not have moved.

---

## 8. What I would do this week

1. **Take the build fix across to mobile `main` on its own, today.** Bring `pubspec.yaml`, `pubspec.lock`, `chat_service.dart` and `conversation_provider.dart` from `BVA-I317` into a small PR, resolve `project.pbxproj` in the same PR, and merge it once Flutter CI is green. Then make that check required. The theme branch can keep growing behind it.
2. **Put `needs: test` back on `beevia-api`'s `sync` job**, then give `beevia-db-schema`'s Release and `beevia-admin-api`'s Sync a verify job to wait on (`suggestions.md` §7.7, option (a)).
3. **Name a reviewer for 0902 and use the column.** Seven leaves are In progress and none has been submitted. Start with `BVA-I314`: have someone other than Philip check the Activity design against its four acceptance criteria before `BVA-I315`/`I316` build on it.
4. **Scope `BVA-I310`'s server half**: a reminder job at +12 h and at −1 h on the existing `escrow-expiry` queue, plus the notification types. That is real backend work on an MVP flow, and it is a better use of Ayomikun's 0902 time than the three preference endpoints.
5. **Write the Appearance storage decision on `BVA-I317`**, and close `BVA-I319`, `I325` and `I328` if device storage stands.
6. **Check the production host's SSH settings**: `PasswordAuthentication no`, root login off, and rate limiting.
7. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
8. **Estimate 0902**, at least the eight push-notification leaves, so the 10 remaining days can be planned.
9. **Correct `BVA-I315`'s acceptance criteria for E2EE.**
10. **Bring `payments.dto.ts` onto `phone.util.ts`.**
11. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
12. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 21.1 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 21 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 13.0 days without a commit. `beevia-admin-api`'s last change was the 1 Oct CI merge, and its last code change was 24 Sep. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed thirty-four days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance, and not whether `main` compiles.

**No score moved.** Nothing reached any `main`. Today's branch commit is theming, which is outside the rubric.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | `createConversation` still omits `X-Device-Id` on `main`; fix on `BVA-I317` |
| 2 | Voice & video calling | 8 | 0.85 | 0 | No change on `main` (call screens restyled on the branch only) |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Escrowed `payment.send` on `main`; biometric option still rejected by `stepUpSchema` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep; no `beevia-admin-api` code change since 24 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether `beevia-api` #60 is live**, and therefore whether "start a chat" is already failing on `main` builds. The Actions API returns `404` to this workspace's token, so deploy state is invisible.
- **Whether branch protection requires CI on any `main`.** All three ungated pipelines depend on it.
- **The production host's real SSH configuration.**
- **Whether `BVA-I317` builds.** No `flutter` command ran. "Parses" means a YAML parser accepted the file.
- **Whether `BVA-I314`'s design meets its acceptance criteria.** Design files are not in these repositories, and the item skipped review.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
4. Read-only scratch exports: sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0), diffed against the 2 Oct file there; sprint 0901 to `/tmp/beevia-scratch/` (76 items, `--no-descriptions --activity`, exit 0, to check for reopens and comments).
5. Fast-forward sync (step 2): `beevia-admin` and `beevia-mobile` already current, three refused as `diverged`. Then `git fetch --all --prune` of all five, read-only.
6. Reflog sweep of all five repos: fast-forwards only, and no `origin/main` moved in the window.
7. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-05b`: route level and spec health clean. The in-repo audit was run too, for the board section. Its 21 drift lines are the known phantom. **Both audit runs used an ephemeral `uv run --with pyyaml` environment**, because the shell's default `python3` no longer has PyYAML (see Degraded inputs).
8. Activity-sidecar sweep of the window across 0902, 0901, 0901-admin and 08-01, matching all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`), owner changes and comment actions.
9. Content reads: in `beevia-mobile`, `git show 6f38116` (full stat, `app_colors.dart` and `chat_send_money_flow.dart` diffs), the `03a3035` version of `app_colors.dart`, conflict-marker `git grep` on both refs, `X-Device-Id` and biometric greps on both refs, and old-palette and token import counts on `main`, `BVA-I317~1` and `BVA-I317`. In the backend shadow: every workflow's `on:` and `needs:` in all three repos; `payments.constants.ts`, `payment.service.ts` and a `remind` search for `BVA-I310`.
10. This report and its web edition.
11. **Re-run at 16:46 UTC, about 11 minutes after the first pass.** That pass ended before `web-report/index.html` was updated, so steps 1a, 1b, the 0902 scratch export, the sync and both audits were run again. All three activity sidecars came back byte-identical to the first pass, and the CSVs differed only in their `Date` preamble line. No `origin/main` or remote branch moved, and the shadow audit was again clean. So no figure in this report changed, and the window end moved from 16:40 to 16:46 UTC. The 0901 scratch export was not repeated, because the sprint is closed and nothing on it has changed since 30 Sep.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Cycle times are `In progress` → `REVIEW/QA` pairs on 0901 leaves (no 0902 item has reached review). Submissions are counted by actor; this week there were none to split.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync and `fetch`, the only git operations were `git archive` and read-only `log`/`diff`/`grep`/`show`/`reflog`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-05.html` and `web-report/index.html`, plus new board exports for 5 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` (`~/.hermes/tools/python-3.14.7+20260901`) has no PyYAML**, so `audit.py` exits 2 with `FATAL: PyYAML required` when run as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`, which leaves no install behind. The results match the 2 Oct figures exactly.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known 50-row sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.

**Window.** 2 Oct 14:05 UTC → 5 Oct 16:46 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
