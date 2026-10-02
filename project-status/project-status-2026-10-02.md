# Beevia — Project Status

**As of 2026-10-02** · Sprint **0902** (30 Sep → 15 Oct): **day 3, 25 items, 5 leaves In progress, 3 transitions in the window** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-02.csv` + `beevia-activity-2026-10-02.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-02.csv` + its activity sidecar (12 items, sprint 0901-admin); read-only scratch exports of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/` and sprint 0901 (76 items) in `/tmp/beevia-scratch/`, each with its sidecar. All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 1 Oct 14:10 UTC → 2 Oct 14:05 UTC, one working day.**

---

## Quick overview

> **All three backend repositories now go to production on any push to `main` without waiting for a test, and mobile `main` still does not build.** Yesterday afternoon `beevia-admin-api` #20 merged unchanged. It is the branch the last two editions asked to fix before merge, and it makes every push to `main` sync and deploy, with no CI gate. In the same hour, `beevia-api` #62 and `beevia-db-schema` #20 moved the production deploy and migration jobs from the broken self-hosted runner to GitHub-hosted runners. That removes the stated reason `beevia-api` gave on 24 Sep for deploying without its test job, and the gate was not put back. On mobile, the fix for the conflicted `pubspec.yaml` now exists, pushed an hour before this report to a branch named `BVA-I317`. It is bundled with the theme feature and has not merged. The same commit adds the missing `X-Device-Id` to `createConversation`. The iOS project file is still conflicted, on `main` and on the branch. The board was nearly still: one click by David started the text-size parent, and its two children followed.

**Correction.** The 30 Sep and 1 Oct editions named `beevia-db-schema` as the backend repo that reaches production without CI, and `beevia-admin-api` as the one with the same change pending. That implied `beevia-api` was gated. It was not. **`bf2b27a` ("ci: deploy without waiting on the test job", 24 Sep 21:49 UTC) removed `needs: test` from `beevia-api`'s `sync` job**, so every push to `beevia-api` `main` since then has rsynced, migrated and deployed without waiting for its tests. Five editions (25 Sep → 1 Oct) missed it. Found today while reading #62, which edits the same file. `suggestions.md` §7.7 now carries it.

| Metric | 1 Oct | 2 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / Done | 18 / 3 / 0 / 0 | **16 / 5 / 0 / 0** | `BVA-I327`, `I328` started (one parent move) |
| Board actions in the window (all boards) | 28 | **3** | one click on `BVA-I326` and its cascade, 2 Oct 12:18 UTC |
| Backend repos that deploy or migrate production on push with no test gate | 1 reported (in fact 2) | **3 of 3** | admin-api #20 merged; `beevia-api` corrected (since 24 Sep) |
| Self-hosted runners in the org | ≥1 (broken) | **0** | api #62, db-schema #20 |
| Files on mobile `main` with conflict markers (excluding `.cxx`) | 3 | **3** | unchanged, day 2 |
| …on `origin/BVA-I317` | n/a | **1** (`project.pbxproj`, 11 blocks) | `pubspec.yaml`/`.lock` parse there |
| Mobile calls that omit `X-Device-Id` (`main` / `BVA-I317`) | 1 / n/a | **1 / 0** | fix on branch, not on `main` |
| Biometric step-up offered on `main` (server accepts `{ pin }` only) | yes | **yes** | also on `BVA-I317` |
| Appearance preferences: where the client stores them | undecided | **device (`Prefs`), on `BVA-I317`** | the three server items have no client caller |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | only `.github/` changed |
| `beevia-mobile` days since a commit on `main` | 0.9 | **1.9** | branch commit 0.04 d ago |
| `beevia-api` days since a commit | 1.5 | **0.9** | CI only |
| `beevia-admin-api` days since a commit on `main` | 7.1 | **0.9** | the CI merge; no code since 24 Sep |
| `beevia-admin` days since a commit | 8.9 | **9.9** | |
| Admin board: open sprint / days since any activity | none / 17.0 | **none / 18.0** | +1.0 |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: nothing merged that the rubric scores |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 4** (2 In progress, 2 To do) · 0901-admin: 2 In progress | 1 (board administration) | 0.98 d (n=10) | `BVA-I319` (1.9 d), `BVA-I328` (0.1 d): **both started by a parent move, not by them** · `BVA-I8` on 0901-admin (**18.0 d**) | **11** | Merged the admin-api deploy chain without a test gate. The client's appearance work makes their three preference-endpoint items unnecessary as written |
| David Samuel | mobile | **0902: 15** (3 In progress, 12 To do) | 19 (9 own; 10 board administration) | 0.96 d (n=24) | `BVA-I286`, `BVA-I318` (1.9 d each), `BVA-I327` (0.1 d) | **4** on `main` (+1 on `BVA-I317`) | The `pubspec` fix and the `createConversation` header are written, but they ride a feature branch. `main` is unbuildable for a second day |
| Philip Chidera | design | **0902: 2** (`BVA-I314`, `BVA-I321`), both To do | 2 (1 own; 1 board administration) | 0.55 d (n=2) | 0 | n/a | `BVA-I321` (dark palette) is still To do, and `BVA-I317`'s branch already ships a dark palette (`app_colors.dart`, +141 lines) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**18.0 d**) | **0** | `beevia-admin` **9.9 days** without a commit. No admin sprint |

**The two questions for standup:** (1) **Can the `pubspec` fix and the `createConversation` header land on `main` today on their own, ahead of the theme work, and who resolves `project.pbxproj`?** Both are already written on `BVA-I317`. Waiting for the theme feature keeps `main` unbuildable for as long as the feature takes. (2) **Can `needs: test` go back on `beevia-api`'s deploy now?** The 24 Sep commit that removed it said to restore it "once hosted runners are back". Since #62, the deploy itself runs on hosted runners.

**The three things worth knowing:**

1. **Nothing between a push and production waits for a test, in any backend repo.** `beevia-admin-api` #20 (merged 1 Oct 15:56 UTC) replaced Sync's `workflow_run` trigger and its `conclusion == 'success'` guard with a plain `push` to `main`. Deploy follows Sync, so a push now deploys. CI runs only on pull requests. Both of `beevia-admin-api`'s scheduled and push-triggered code scans are gone too. `beevia-db-schema` has been in the same state since #19 (30 Sep). `beevia-api` has been since `bf2b27a` (24 Sep; see the correction). All three rest on one sentence in their workflow files: *"CI is a required check, so anything on main has already passed it."* Branch protection cannot be seen from here, and a forced update to `beevia-db-schema` `main` was observed on 28 Sep. The `beevia-api` case is the cheapest to fix, by its own terms. The commit that removed the gate gave unavailable hosted runners as the reason. #62 moved the deploy onto hosted runners, so either they work, and the gate can come back, or they do not, and nothing deploys anyway. This is a missing process control, not anyone's error: one person owns all three pipelines, and no second reviewer is visible on any of the three merges.

2. **The fix for mobile `main` exists, on the wrong branch.** `origin/BVA-I317` (`03a3035`, 2 Oct 13:10 UTC) resolves `pubspec.yaml` exactly as the last edition suggested: #36's upgraded versions plus `local_auth`. `pubspec.yaml` and `pubspec.lock` both parse on it. It also makes `deviceId` required on `createConversation` and `fetchConversations`, which closes the last `X-Device-Id` gap. But the same commit carries the whole Appearance feature (theme tokens, dark palette, chat backgrounds, text sizes, settings screen; 36 files, +835/−254) and an Android `compileSdk` 36 → 37 bump. The feature's parent items are still In progress. **`ios/Runner.xcodeproj/project.pbxproj` keeps all 11 conflict blocks on the branch,** so even a merge today leaves iOS broken. The biometric step-up is untouched (`wallet_service.dart:78`).

3. **The client answered the Appearance storage question in code, and the board has not caught up.** `appearance_provider.dart` on the branch stores theme, chat background and text size on the device through `Prefs`. It makes no server call. That is the device-storage option from yesterday's standup question, and it meets every item's "persists across app restarts" criterion. Ayomikun's three "GET/PATCH preference endpoint" items (`BVA-I319`, `I325`, `I328`) therefore have no caller. Two of them now show **In progress** only because David moved their parents (`BVA-I317` on 30 Sep, `BVA-I326` today). Neither the decision nor a comment is recorded on any of the four parents.

**If you read nothing else:** as of yesterday afternoon, any push to any backend `main` reaches production without a test, and `beevia-api` has been that way since 24 Sep without this report noticing. Mobile `main` is unbuildable for a second day while its fix sits on a theme-feature branch. Land that fix on its own, and put `needs: test` back.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The day-over-day comparison uses the 1 Oct edition's figures and the sidecar's `actiontime`s, because the 1 Oct scratch export in `/tmp/beevia-scratch/` did not survive (the folder was empty this morning).

| Status | 1 Oct | 2 Oct | Δ |
|---|---:|---:|---:|
| To do | 18 | **16** | −2 |
| In progress | 3 | **5** | +2 |
| REVIEW/QA | 0 | 0 | 0 |
| Done | 0 | 0 | 0 |
| **Total leaves** | **21** | **21** | **0** |

**The window holds three audit entries, all from one action:** at **12:18:56 UTC on 2 Oct**, David moved `BVA-I326` (*Text Size / Font Scaling*, parent) To do → In progress. Its children followed within 4 ms: `BVA-I327` (*Scalable Typography & Live Preview Wiring*, his) and `BVA-I328` (*Text Size Preference Storage*, Ayomikun's). As with `BVA-I319` on 30 Sep, Ayomikun did not start `BVA-I328`.

There were no comments, no new items, no re-assignments and no description edits. Every 0902 item still has a blank Epic and 0 estimation points.

**Board versus code.** The theme branch (§3.1) already contains work for items the board shows as To do. It has four chat background swatches (`BVA-I324`), a reworked Appearance screen (`BVA-I329`) and a dark palette (`app_colors.dart`), while Philip's `BVA-I321`, *Dark Mode Palette for Every Screen*, is the design input for that palette. That is not wrong: a developer can scaffold ahead of a design. But it means the board understates what has been started, and that `BVA-I321`'s design may arrive after the code it was meant to drive.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC). All 67 leaves are Done, there has been no reopen ever, and no comment since. 0901-admin's last entry is 14 Sep 14:53 UTC (§ Admin dashboard board). 08-01's last entry is 3 Sep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902: the Appearance block, two days in

Yesterday's edition asked whether the three Appearance preferences need the server at all. The client has now answered that in code, on `origin/BVA-I317`:

| Item | Owner | Board | Code on `BVA-I317` |
|---|---|---|---|
| `BVA-I318` Theme Token System & Runtime Switching | David | In progress | `app_theme.dart`, `app_colors.dart` (+141), `appearance_provider.dart` (+140) |
| `BVA-I319` Theme Preference Storage (*"GET/PATCH endpoint"*) | Ayomikun | **In progress (cascade)** | Stored on device: `Prefs.saveString(_themeModeKey, …)` |
| `BVA-I324` Background Swatch Picker & Application | David | To do | Swatches and storage present in the provider |
| `BVA-I325` Chat Background Preference Storage (*"GET/PATCH endpoint"*) | Ayomikun | To do | Stored on device: `_chatBackgroundKey` |
| `BVA-I327` Scalable Typography & Live Preview Wiring | David | In progress | Text size in the provider; preview wiring in `appearance.dart` |
| `BVA-I328` Text Size Preference Storage (*"GET/PATCH endpoint"*) | Ayomikun | **In progress (cascade)** | Stored on device: `_textSizeKey` |
| `BVA-I329` Appearance Settings Screen | David | To do | `settings/screens/appearance.dart` rewritten (166 lines changed) |

The three backend items are now the only part of the block with no code and no caller. Either the preferences should follow a user to a new device, in which case they belong as three fields on the existing `PATCH /users/me/settings` rather than three new endpoint pairs, or they should not, in which case the items should close. One line on `BVA-I317` decides it. Until then, two of Ayomikun's four 0902 leaves read as work in progress that nobody is doing.

`BVA-I315` (Activity Feed Backend) is unchanged. It still asks the server for "last message text" previews, which E2EE rules out (30 Sep §2).

---

## 3. Code, API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. This was run against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-02`). The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees. They were not acted on. **No spec file changed this cycle.** The three backend merges in the window touched only `.github/workflows/` (and `beevia-db-schema`'s `package.json` version bump).

### 3.1 `beevia-mobile`: `main` unchanged, fix on `origin/BVA-I317`

`main` is still `d51e3d1` (PR #42, 30 Sep 15:45 UTC). Conflict markers on `main`: `pubspec.yaml` 1 block, `pubspec.lock` 5, `project.pbxproj` 11. That is unchanged.

**New branch `origin/BVA-I317`** (named after the Theme Infrastructure parent): 1 commit, `03a3035` "local changes", `Davidtariq96`, 2 Oct 13:10 UTC. It is 1 ahead of `main` and 0 behind, with 36 files, +835 / −254.

| Change on the branch | Status |
|---|---|
| `pubspec.yaml` conflict resolved: #36's versions (`permission_handler` ^13, `flutter_secure_storage` ^11, `file_picker` ^13, `google_mlkit_*` ^0.15, `flutter_contacts` ^2.3.1) **plus `local_auth` ^2.3.0** | ✅ parses |
| `pubspec.lock` regenerated | ✅ parses |
| `ios/Runner.xcodeproj/project.pbxproj` | ❌ **11 conflict blocks remain** |
| `createConversation` and `fetchConversations` take a required `deviceId` and always send `X-Device-Id`; the provider resolves it first and fails with a message if it cannot (`conversation_provider.dart:487–497`) | ✅ closes the last `#60` gap |
| `ensureSocketConnected()` in `socket_manager.dart`: catches a failed socket init instead of leaving `socketInstance` null for the session | new |
| Appearance feature: theme mode, dark palette, chat backgrounds, text size, settings screen, l10n strings in four languages | new (§2) |
| Android `compileSdk` 36 → 37 | new, unrelated to the item |
| Biometric step-up (`wallet_service.dart:78`) | unchanged, still rejected by `stepUpSchema` |

The branch is the right fix for two of the three files. The trouble is what it is attached to. Merging it means merging the theme feature, which is two parents still In progress. Not merging it keeps `main` unbuildable. The two halves are separable: the manifest and `chat_service.dart` changes touch no Appearance file.

Remote branches now: `main`, `BVA-I317` (1 ahead), `update-fixes` (contained), `App-bundle` (contained) and five Dependabot branches from 30 Sep.

### 3.2 Backend and CI: three merges, all to `.github/`

| Repo | Merge | Time (UTC) | What changed |
|---|---|---|---|
| `beevia-admin-api` | #20 `535da3d` (branch `ci/node-26-only`, commits from 28 Sep) | 1 Oct 15:56 | CI on `pull_request` only, Node 26 only. `code-scan.yml` loses `push` and the daily `schedule`. **`sync.yml` triggers on `push` to `main`, with the `workflow_run` success guard removed.** Deploy follows Sync |
| `beevia-api` | #62 `bcb47bb` (`fa5a5de`) | 1 Oct 15:57 | `test`, `sync`, `deploy` and `postman-sync` move from self-hosted to `ubuntu-latest`. `sync` still has no `needs: test` |
| `beevia-db-schema` | #20 `8531e65` (`aabd858`) → Release `v0.0.39` (`d254961`) | 1 Oct 15:58 → 15:59 | `release`, `semgrep` and `sync` (production migration) move to `ubuntu-latest`. Release still has no `needs:` on a verify job |

**What the commit messages say, and what they mean.** Both #62 and db-schema #20 explain the move the same way. The self-hosted runner's workspace became unwritable and took every scan down across seven repositories, and *"that leaves no self-hosted runner anywhere in the organisation."* Moving off a broken stateful runner is a sound call. Both messages also record that the move was checked first. The deploy authenticates with a key from secrets, and *"the server restricts nothing by source — ufw inactive, iptables INPUT policy ACCEPT with no rules, no AllowUsers or Match in sshd_config."* That is the reason a hosted runner can reach the server. It is also a statement that the production host accepts SSH from the whole internet. Whether password login is disabled cannot be seen from here (`suggestions.md` §7.7, 2 Oct update).

**`db-schema` Release v0.0.39** was published 47 seconds after #20 merged. That is the ungated chain doing exactly what it does: a workflow-only change produced a package release and, if Sync ran, a production migration and seed. Whether Sync ran cannot be seen here, because the Actions API returns `404`.

**Reflog sweep:** every `origin/main` update in all five repos was a fast-forward, with no forced update in the window. `beevia-admin-api`'s `ci/node-26-only` branch is gone after merging.

### 3.3 Document changes this cycle

| File | Change |
|---|---|
| `suggestions.md` | **§7.7, new 2 Oct update:** all three backend repos are ungated; the `beevia-api` correction (`bf2b27a`); #62 removes the stated reason; the production host's SSH posture. **§5.12 update:** the fix on `origin/BVA-I317`; `project.pbxproj` still conflicted. **§8:** 3f updated, new 3g |
| `api-rfc.md` | **§5.12 update:** `X-Device-Id` coverage after PR #42, and the `createConversation` fix on `BVA-I317` |

`openapi*.yaml` and `admin-api-rfc.md` are unchanged. No route or contract moved.

---

## 4. Risks

- **Every backend repo deploys or migrates production on push without a test gate** (§3.2). **Newly complete today**, and `beevia-api`'s share is nine days old (correction). Severity rests on branch protection, which nobody here can see.
- **Production SSH accepts connections from any address**, per the deploy commits' own description. This is low-cost to harden, and how much it matters depends on settings this workspace cannot read.
- **Mobile `main` does not build, day 2** (§3.1). The fix is written but coupled to a feature branch, and iOS has no fix anywhere.
- **"Start a chat" breaks once `beevia-api` #60 deploys**, on `main`. The fix is on `BVA-I317`. Deploy state is still not visible.
- **The biometric step-up on `main` fails against the real API** on every money sheet (`suggestions.md` §5.11).
- **The unparsed phone field (`payments.dto.ts:5`) is on the main payment path.** Unchanged.
- **0902 has no estimates, and the board misstates its own WIP.** Two "In progress" backend items are parent cascades with no planned code. Three To do items already have code on a branch.
- **`BVA-I315` is still specified against E2EE.**
- **The admin workstream is silent:** 9.9 days with no `beevia-admin` commit, 18.0 days with no board activity, and no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. The only code movement in the window is the Appearance feature on a branch, which the PRD does not mention.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 25 Sep 14:05 → 2 Oct 14:05 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. **The 30 Sep sweep is not a submission and is not counted as anyone's output.**

### 6.1 Ayomikun Araoye: backend + admin API

**11 commits in 7 days**, all as `Phoenixdadhev`: `beevia-api` 6, `beevia-db-schema` 3, `beevia-admin-api` 2. Eight of the eleven are CI changes. The other three in `beevia-api` are the escrowed socket send (25 Sep), required `X-Device-Id` (30 Sep) and NestJS Observe (30 Sep). The count fell from 28 because older commits rolled out of the window. Yesterday's work moved the org off a runner that had broken every scan, which was needed. The cost is that all three production chains now run ungated (§3.2). Fixing that is three small edits in files they own. On 0902 they hold four leaves. Two show In progress because David moved their parents, and the client stores all three preferences on the device, so those items need a decision rather than an implementation (§2). `BVA-I8` has been In progress on the admin board for 18.0 days. Submissions in 7 days: 1, moved by board administration. Median cycle time 0.98 d (n=10, all on 0901).

### 6.2 David Samuel: mobile

**4 commits on `main` in 7 days** (`Davidtariq96`, all before the PR #42 merge), **plus 1 on `origin/BVA-I317`** today. That one commit resolves the `pubspec` conflict correctly, closes the `X-Device-Id` gap and builds most of the Appearance block. The issue is packaging, not quality. A one-file fix that unblocks everyone is waiting on a feature, because the branch carries both. That is the same pattern as `update-fixes`, which held four QA fixes off `main` for a week. Without a reviewer, nobody asks for the fix to be split out. On the board, he started the text-size parent today. He holds 15 of 0902's 21 leaves, 3 In progress. Submissions to REVIEW/QA in 7 days (owner rows): 19 (9 own, 10 board administration), all before the 0901 sweep. Median cycle time 0.96 d (n=24).

### 6.3 Philip Chidera: design

No board action in the window. They own `BVA-I314` (Activity tab design) and `BVA-I321` (dark palette for every screen), both To do. A dark palette already exists in code on `BVA-I317`. So `BVA-I321` is now either a review of that palette or a replacement for it, and it is worth agreeing which before either side does more. No commits, because design work does not land in these repositories.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **9.9 days** ago. The admin board has had no activity for 18.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the fifth edition to ask whether the workstream is paused. `beevia-admin-api`'s only `main` change since 24 Sep is yesterday's CI merge.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 |
|---|---:|---:|
| 2026-W37 | 7 | — |
| 2026-W38 | 11 | — |
| 2026-W39 | **42** | — |
| 2026-W40 (from Mon 28 Sep) | 1 | 0 |

0902 is on day 3 with nothing submitted yet. That is normal this early. Acceptances by someone other than the submitter: **none**, apart from the two bulk sweeps (3 Sep and 30 Sep).

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more. This is the twenty-first edition to say so.
- **"Submitted" counts any transition into REVIEW/QA, by anyone**, and credits it to the item's owner. For David, 10 of 19 were board administration's moves.
- **A parent's cascade is not a start.** Both of Ayomikun's In-progress 0902 items were moved by a parent.
- **Commit counts reward small commits.** David's one commit today is 36 files. Eight of Ayomikun's eleven are workflow edits.
- **Branch work is invisible to the board, and the board is wrong about branch work.** Three To do items have code on `BVA-I317`.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository. "Parses" means a YAML parser accepted the file, not that `flutter pub get` succeeded.

---

## 7. Previous recommendations: where they stand

| Recommendation from 1 Oct | Status on 2 Oct |
|---|---|
| **1. Fix `pubspec.yaml`, `pubspec.lock`, `project.pbxproj` on mobile `main`; make Flutter CI required** | ◐ **Two of three fixed, on a branch.** `BVA-I317` resolves both `pubspec` files as recommended. `project.pbxproj` is unfixed everywhere. `main` is unchanged. CI requirement not visible |
| **2. Add `X-Device-Id` to `createConversation`** | ◐ **Done on `BVA-I317`, not on `main`** |
| **3. Hide the biometric option outside mock mode** | ❌ **Not done**, on `main` or the branch |
| **4. Decide where Appearance preferences live** | ◐ **Decided in code (device storage), not on the board.** The three server items remain, two of them In progress by cascade |
| **5. Estimate 0902; say whether Appearance is in or out** | ❌ **0 of 25 estimated.** Appearance is plainly in: two parents In progress and most of it coded on a branch |
| **6. Gate `beevia-db-schema`'s Release; fix `beevia-admin-api`'s branch before it merges** | ❌ **Went the other way.** The admin-api branch merged unchanged (#20). db-schema #20 edited `release.yml` without adding a gate. `beevia-api` turns out to have been ungated since 24 Sep |
| **7. Correct `BVA-I315`'s acceptance criteria for E2EE** | ❌ **Not done.** No description edit |
| **8. Name a reviewer for 0902; define REVIEW/QA and Done** | ❌ **Not done.** Fourteenth edition |
| **9. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** Line 5 unchanged |
| **10. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **11. Carried: comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec** | ❌ **None done** |

**Three of eleven moved, all partly, all through one unmerged mobile commit.** One went backwards (6).

---

## 8. What I would do this week

1. **Land the build fix on mobile `main` today, without the theme feature.** Take `pubspec.yaml`, `pubspec.lock` and `chat_service.dart`/`conversation_provider.dart` from `BVA-I317` into a small PR, resolve `project.pbxproj` in the same PR, and merge it once Flutter CI is green. Then make that check required.
2. **Put `needs: test` back on `beevia-api`'s `sync` job.** The commit that removed it set the condition for restoring it, and #62 met it. Then give `beevia-db-schema`'s Release and `beevia-admin-api`'s Sync a verify job to wait on (`suggestions.md` §7.7, option (a)).
3. **Check the production host's SSH settings**: `PasswordAuthentication no`, root login off, and rate limiting (`ufw limit ssh` or `fail2ban`). An allowlist of GitHub's published ranges is possible but optional.
4. **Write the Appearance storage decision on `BVA-I317`.** Device storage, as the code does, means closing `BVA-I319`, `I325` and `I328`. Cross-device sync means three fields on `PATCH /users/me/settings`, not three new endpoint pairs.
5. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
6. **Estimate 0902**, and agree whether `BVA-I321`'s design reviews the dark palette already on the branch or replaces it.
7. **Correct `BVA-I315`'s acceptance criteria for E2EE.**
8. **Name a reviewer for 0902 and write down what REVIEW/QA and Done mean.** Today a reviewer would have asked for item 1 to be split out, and would have caught item 2 before #20 merged.
9. **Bring `payments.dto.ts` onto `phone.util.ts`.**
10. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
11. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 18.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 18 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 9.9 days without a commit. `beevia-admin-api`'s `main` moved yesterday, but only with the CI merge (§3.2); its last code change was 24 Sep. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed thirty-one days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance, and not whether `main` compiles.

**No score moved.** Nothing the rubric scores reached any `main`. Two candidates were considered and held:

- **#1 E2EE messaging, held at 0.90.** The `createConversation` header fix is on `BVA-I317`, not `main`. If it lands on `main` while #60 is live, #1 stays at 0.90; it would have come down if #60 were confirmed live with `main` still omitting it.
- **#7 Send / request / receive, held at 0.92.** The biometric option is still offered on `main` and still rejected by `stepUpSchema`.

The Appearance work is outside the rubric (no PRD capability), so it would not move the number even on `main`.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | `createConversation` still omits `X-Device-Id` on `main`; fix on `BVA-I317` |
| 2 | Voice & video calling | 8 | 0.85 | 0 | No change on `main` |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Escrowed `payment.send` on `main`; biometric option still rejected |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep; `beevia-admin-api` changed only `.github/` |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether any of yesterday's three backend merges deployed, and whether `beevia-db-schema` v0.0.39 migrated production.** The Actions API returns `404` to this workspace's token.
- **Whether `beevia-api` #60 is live**, and therefore whether "start a chat" is already failing on `main` builds.
- **Whether branch protection requires CI on any `main`.** All three ungated pipelines depend on it.
- **The production host's real SSH configuration.** The only evidence is the description in two commit messages.
- **Whether `BVA-I317`'s `pubspec` resolution actually resolves.** It parses as YAML. `flutter pub get` was not run.
- **Velocity for any sprint.** Nothing on any board is estimated (0 of 25, 0 of 76, 0 of 12, 0 of 64).

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
4. Read-only scratch exports: sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0) and sprint 0901 to `/tmp/beevia-scratch/` (76 items, `--no-descriptions --activity`, exit 0, to check for reopens and comments). The previous days' scratch files were gone, so 0902's day-over-day figures come from the 1 Oct edition plus the sidecar's timestamps.
5. Fast-forward sync (step 2): `beevia-admin` and `beevia-mobile` already current, three refused as `diverged`. Then `git fetch --all` of all five, read-only.
6. Reflog sweep of all five repos: fast-forwards only.
7. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-02`: route level and spec health clean. The in-repo audit was run too, for the board section. Its 21 drift lines are the known phantom.
8. Activity-sidecar sweep of the window across 0902, 0901 and 0901-admin, matching all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`) and comment actions.
9. Content reads: the full diffs of `beevia-admin-api` #20, `beevia-api` #62 and `beevia-db-schema` #20 with their commit messages; `release.yml`/`sync.yml` at each `origin/main`; `git log -S` on `beevia-api`'s release gate comment (found `bf2b27a`). In `beevia-mobile`: `git diff origin/main origin/BVA-I317`, YAML parses of `pubspec.yaml`/`pubspec.lock` on the branch via `git show`, conflict-marker `git grep` on both refs, `createConversation` callers, and `appearance_provider.dart`. At `beevia-api` `origin/main`: `payments.dto.ts:5` and `stepUpSchema`.
10. Edits to `suggestions.md` and `api-rfc.md`, then this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Cycle times are `In progress` → `REVIEW/QA` pairs on 0901 leaves. Submissions are split by actor.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose transitions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync and `fetch`, the only git operations were `git archive` and read-only `log`/`diff`/`grep`/`show`/`reflog`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-02.html`, `web-report/index.html`, `suggestions.md` and `api-rfc.md`, plus new board exports for 2 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The previous scratch exports were lost** (`/tmp/beevia-scratch/` was empty), so there is no file-level 0902 diff against 1 Oct. The sidecar's full audit trail covers the window, so no movement is missed. But a field change that leaves no audit entry would not be seen.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for the 08-01 and admin projects. This is the known 50-row sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.

**Window.** 1 Oct 14:10 UTC → 2 Oct 14:05 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
