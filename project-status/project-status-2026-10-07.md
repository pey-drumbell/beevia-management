# Beevia — Project Status

**As of 2026-10-07** · Sprint **0902** (30 Sep → 15 Oct): **day 8 of 16, 25 items, 11 leaves To do · 4 In progress · 5 REVIEW/QA · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-07.csv` + `beevia-activity-2026-10-07.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-07.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 6 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 6 Oct 14:06 UTC → 7 Oct 14:03 UTC, 1.0 day** (Tuesday afternoon to Wednesday afternoon in Lagos).

---

## Quick overview

> **Mobile `main` is free of conflict markers for the first time in seven days, because the whole `BVA-I317` branch was merged rather than the fix being split out.** `beevia-mobile` PR #43 (7 Oct 10:23 UTC) brought the Appearance work, the `pubspec` resolution, a fresh Firebase commit that also resolves `project.pbxproj`, and the `createConversation` device header onto `main`. `origin/main` now has **zero conflict markers** and every route `beevia-api` #60 guards gets `X-Device-Id`. On the board, five Appearance leaves entered REVIEW/QA on 6 Oct 16:03 UTC, the first entries in eight days, but **all five were moved by board administration, not by their owners**, and nothing has left the column. The backend is unchanged for a sixth day: no commit, three ungated production pipelines.

**No correction to the 6 Oct edition.** Its claims were re-checked; everything that changed did so after its 14:06 UTC cut-off. Two things it said are now resolved rather than wrong: the build break (day 6 there) and the `createConversation` gap.

| Metric | 6 Oct | 7 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / Done | 13 / 7 / 0 / 1 | **11 / 4 / 5 / 1** | 5 → QA, 2 started |
| Board actions in the window (all boards) | 0 | **13** | all on 0902 |
| Transitions into REVIEW/QA, last 7 days (leaves) | 0 | **5** | **all 5 by board administration**; owners' last own submission 28 Sep, **9.0 d** ago |
| Items that left REVIEW/QA in the window | 0 | **0** | |
| Files on mobile `main` with conflict markers (excluding `.cxx`) | 3 | **0** | **fixed by PR #43**, after 6.8 days |
| Mobile calls that omit `X-Device-Id` on `main` | 1 | **0** | fixed by PR #43 |
| Biometric step-up offered on `main` (server accepts `{ pin }` only) | yes | **yes** | 5 call sites in 4 files |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no backend commit since 1 Oct |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | |
| `beevia-mobile` days since a commit on `main` | 5.9 | **0.2** | PR #43 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 4.9 / 4.9 / 4.9 | **5.9 / 5.9 / 5.9** | |
| `beevia-admin` days since a commit | 13.9 | **14.9** | |
| Admin board: open sprint / days since any activity | none / 22.0 | **none / 23.0** | |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: the merge closes gaps, it adds no rubric capability |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6** (2 REVIEW/QA, 4 To do) · 0901-admin: 1 In progress | 2 (**both moved by board administration**) | 1.22 d (n=12; 0.98 on the 10 own-flow items) | none on 0902 · `BVA-I8` on 0901-admin (**23.0 d**) | **2** (CI, 1 Oct) | No commit for 5.9 days. Their two QA items have no backend code: the client stores those preferences on the device |
| David Samuel | mobile | **0902: 15** (3 In progress, 3 REVIEW/QA, 9 To do) | 3 (**all moved by board administration**) | 0.96 d (n=27) | `BVA-I286` (6.9 d, own) · `BVA-I306`, `BVA-I312` (0.9 d, started by board administration) | **4** on `main` + PR #43 merge | Conflict markers cleared on `main`. Merged their own PR 93 min after pushing a new Firebase commit |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` In progress (5.0 d) | 0 | 0.55 d (n=2) | `BVA-I321` | n/a | — |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**23.0 d**) | **0** | `beevia-admin` **14.9 days** without a commit. No admin sprint |

**The two questions for standup:** (1) **Who reviews the five Appearance leaves now in REVIEW/QA, and against what?** Their code is already on `main`, so review is now after the fact, and two of them (`BVA-I319`, `I328`) are backend tasks with no backend code. (2) **What does 0902 still intend to finish by 15 Oct?** Tomorrow is the midpoint. Push notifications have their first code (Firebase set-up) but six of eight leaves are untouched, and nothing is estimated.

**The three things worth knowing:**

1. **Mobile `main` is repaired, by merging the feature, not by splitting the fix.** PR #43 (`01bcf2a`, 7 Oct 10:23 UTC, a true merge) took `BVA-I317` whole: 3 commits, 95 files, +2,384 / −1,200. It resolves all three conflicted files — `pubspec.yaml` and `pubspec.lock` now parse, and `project.pbxproj`'s 11 blocks are gone (+11 / −57 in `1a1f39f`). It also gives `createConversation` a required `deviceId`, so all six #60 routes are covered. That ends a 6.8-day break. Two things to weigh against it. First, the last commit, `1a1f39f` ("notification configuration": Firebase SDK, `google-services.json`, `GoogleService-Info.plist`, `Firebase.initializeApp` in `bootstrap.dart`), landed at 08:50 UTC and was merged 93 minutes later. It belongs to a push-notification item that board administration had started only the evening before. Second, whether `main` *builds* is still not something this workspace can see: no `flutter` command ran, and CI results return `404`.

2. **The review column moved, but nobody submitted anything.** On 6 Oct, between 16:03:42 and 16:04:21 UTC, board administration moved `BVA-I318`, `I319`, `I322`, `I327` and `I328` (plus parents `I317` and `I326`) to REVIEW/QA. Three of them made a five-second detour through BLOCKED on the way. Two minutes later it started `BVA-I306` and `I312`. Every one of those 13 actions was board administration's. The owners' last own submission is still **`BVA-I298`, 28 Sep 15:14 UTC, 9.0 days ago**. The code those five leaves describe reached `main` 18 hours *after* they entered review, and the person who merged it was their owner. So the column now holds work that is already shipped, with no named reviewer. This is a process finding: the board is being maintained on the team's behalf rather than by it, and review is happening, if at all, outside the board. The standing record holds: **apart from the two bulk sweeps (3 Sep and 30 Sep), no item on any board has ever been accepted by someone other than its submitter.**

3. **The backend has gone six days without a commit, and the risks it carries have not moved.** No commit on any backend `origin/main` since 1 Oct 15:59 UTC. `beevia-api`'s `release.yml` `sync` job still has no `needs: test`. `beevia-admin-api`'s Sync → Deploy and `beevia-db-schema`'s Release → Sync still run on push with nothing waiting for a verify job. 0902's push-notification block needs one server piece that does not exist (reminder scheduling for `BVA-I310`). Everything else it needs is already there: `POST /notifications/token` and an FCM adapter that activates when `FCM_SERVICE_ACCOUNT` is set. The client now has Firebase initialised but does not yet register a token.

**If you read nothing else:** mobile `main` is fixed and the device-header gap is closed, both via one large merge. The review column now holds five items that were moved there by board administration and shipped before any review was recorded on the board. The backend is quiet and still deploys untested.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. The comparison is file-level, against the 6 Oct scratch export in `/tmp/beevia-scratch/0902/`.

| Status | 6 Oct | 7 Oct | Δ |
|---|---:|---:|---:|
| To do | 13 | 11 | −2 |
| In progress | 7 | 4 | −3 |
| REVIEW/QA | 0 | 5 | +5 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

**All 13 audit entries in the window, in order (UTC):**

| Time | Item(s) | Action | By |
|---|---|---|---|
| 6 Oct 16:03:42 | `BVA-I317` (parent), `I318`, `I319` | In progress → REVIEW/QA | board administration |
| 6 Oct 16:03:57 | `BVA-I326` (parent), `I327`, `I328` | In progress → BLOCKED | board administration |
| 6 Oct 16:04:01 | `BVA-I326`, `I327`, `I328` | BLOCKED → REVIEW/QA (4 s later) | board administration |
| 6 Oct 16:04:21 | `BVA-I322` | In progress → REVIEW/QA | board administration |
| 6 Oct 16:04:50 | `BVA-I306` | To do → In progress | board administration |
| 6 Oct 16:07:06 | `BVA-I312` | To do → In progress | board administration |
| 7 Oct 13:28:45 | `BVA-I308` | owner added: Ayomikun Araoye | board administration |

The BLOCKED detour lasted four seconds and carries no comment, so it reads as a mis-click, not a block. **There were no comments, no reopens and no items added or removed.** Every 0902 item still has a blank Epic and 0 estimation points. `BVA-I320` (parent, Philip/David) stays In progress because its child `BVA-I321` (Philip's dark palette) is still open.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static. 0901's last entry is still the 30 Sep sweep (07:56:53 UTC): all 67 leaves are Done, there has never been a reopen, and there has been no comment since. The 0901-admin and 08-01 sidecars are byte-identical to 6 Oct's, and their CSVs differ only in the `Date` preamble line. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 8

| Block | Leaves | State | Code on `main` |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | 2 In progress (`I306`, `I312`, started by board administration), 6 To do | **First code landed:** `firebase_core` + `firebase_messaging` in `pubspec.yaml`, Firebase config for Android and iOS, `Firebase.initializeApp` in `bootstrap.dart` (`1a1f39f`). `firebase_messaging` is not yet used anywhere in `lib`: no permission request, no token, no call to the server's `POST /notifications/token`. `BVA-I310`'s reminder scheduling is still absent from `beevia-api` |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done (self-closed); backend and screen To do | none. `BVA-I315` still asks for server-side message previews that E2EE rules out |
| Appearance (`BVA-I318`–`I329`) | 9 | 5 REVIEW/QA, 1 In progress (`I321`), 3 To do | **On `main` since PR #43.** Theme tokens and dark palette, an Appearance screen with Theme / Chat background / Text size / live Preview (`settings/screens/appearance.dart`), text size applied app-wide via `TextScaler`. All three preferences are stored **on the device** (`Prefs`, `appearance_provider.dart:124–138`) |
| Carried bug `BVA-I286` | 1 | In progress, 6.9 d | not identified on any branch |

**The board and the code now disagree in both directions on Appearance:**

- **Ahead of the code.** `BVA-I319` (*Theme Preference Storage*) and `BVA-I328` (*Text Size Preference Storage*) are Ayomikun's backend tasks, now in REVIEW/QA. There is no backend change for either: no commit, and the client never calls the server for these preferences. If device storage is the decision, these items should be closed as not needed, not reviewed as delivered. That decision is still written nowhere — there is no comment on `BVA-I317`, `I319`, `I323`, `I326` or `I328`.
- **Behind the code.** `BVA-I329` (*Appearance Settings Screen*) is To do, but the screen its acceptance criteria describe — Light/Dark/System, White/Bone/Ink/Graphite swatches, Small/Medium/Large, live Preview, no Save step — is on `main`. `BVA-I324` (*Background Swatch Picker & Application*) is half there: the picker exists, but nothing in `lib/features/chat` reads the chosen background, so it is not applied to chat screens yet.

Eight days remain, and tomorrow is the midpoint. Six of the eight push-notification leaves and both Activity-tab build leaves have not started.

---

## 3. Code, API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. This was run against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-07`). The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees. They were not acted on. **No spec file changed this cycle**; the sync touched no controller, DTO or schema file.

### 3.1 `beevia-mobile`: PR #43 merged `BVA-I317` whole

`main` moved `d51e3d1` → **`01bcf2a`** (fast-forwarded in the working tree, which was already on `main`, so no branch switch). The merge brings three `Davidtariq96` commits: `03a3035` (2 Oct, manifest fix + `createConversation` header + Appearance start), `6f38116` (5 Oct, 60-file theme-token migration), and the new **`1a1f39f`** (7 Oct 08:50 UTC, Firebase). `origin/BVA-I317` is still present and fully contained (0 ahead). Two Dependabot branches were refreshed this morning; nothing else moved.

| Check at `origin/main` | 6 Oct | 7 Oct |
|---|---|---|
| Conflict markers: `pubspec.yaml` / `pubspec.lock` / `project.pbxproj` | 1 / 5 / 11 blocks | **0 / 0 / 0** |
| `pubspec.yaml` and `pubspec.lock` parse as YAML | no | **yes** (`local_auth` present, #36's versions kept) |
| `createConversation` sends `X-Device-Id` | no | **yes** (`chat_service.dart:212`, `deviceId` now required) |
| Biometric option on the money sheets (`_verifyBiometrics`) and `{method: biometric}` in `wallet_service.dart:78` | yes | **yes** (chat send ×2, bank transfer, card request, wallet) |
| `android/app/.cxx/` tracked, with markers in its `.bin` files | yes | yes (build artefacts, no build effect) |

**On the Firebase commit.** Committing `google-services.json` and `GoogleService-Info.plist` is normal for a Firebase client, and the keys in them are not secrets. It is still worth confirming in Google Cloud that the API key is restricted to the app's package and bundle IDs. `Firebase.initializeApp` now runs unconditionally at start-up, including mock-backend builds. Per the owner's standing instruction, test and correctness effects are out of scope here; it is noted in "cannot tell you".

**How it merged.** PR #43's merge commit is authored by David at 10:23 UTC, 93 minutes after `1a1f39f`. PR metadata (reviews, required checks) is not visible from this workspace — `gh` cannot resolve the organisation's repositories with the available token. Nothing here says whether anyone else reviewed it.

### 3.2 Backend and CI: no change

No commit on any backend `origin/main` since 1 Oct 15:59 UTC (**5.9 days**). Re-read at `origin/main` today, whole files: `beevia-api`'s `release.yml` `sync` job still has no `needs: test` (the comment at line 29 still explains why), and `deploy` waits only on `sync`. `beevia-admin-api`'s `sync.yml` (on push) → `deploy.yml` (`workflow_run`) chain and `beevia-db-schema`'s `release.yml` (on push) → `sync.yml` chain are unchanged and ungated. `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged, as is the absence of any reminder scheduling.

### 3.3 Document changes this cycle

- **`suggestions.md`** — §5.12 gains a 7 Oct update: the markers are resolved on `main` via PR #43, by merging the feature; Flutter CI as a required check and untracking `android/app/.cxx/` remain. §8 item 3f is updated to match.
- **`api-rfc.md`** — §5.12 gains a 7 Oct update: all six `X-Device-Id` routes are now covered by `main` (`chat_service.dart:34`, `:69`, `:212`, plus the socket handshake). The mock server still does not enforce the header.
- `openapi*.yaml` and `admin-api-rfc.md`: unchanged. The audit is clean, and no backend contract moved.

---

## 4. Risks

- **Every backend repo deploys or migrates production on push without a test gate** (§3.2), now for 13 days in `beevia-api`'s case. How severe this is depends on branch protection, which nobody here can see.
- **Merges to mobile `main` are not gated on anything visible.** PR #42 merged conflict markers 77 s after its last commit. PR #43 merged a new Firebase commit 93 minutes after it was pushed. Both times the result could have been checked by a required Flutter CI run; whether one exists cannot be seen from here. This time the outcome was good. The control is still missing.
- **Production SSH accepts connections from any address**, per the 1 Oct deploy commits' own description. Unverified.
- **The review step is maintained by board administration, not used by the team.** Five leaves entered it, none by their owners, and their code shipped before any review was recorded on the board. There is still no named reviewer and no definition of Done.
- **The biometric step-up on `main` fails against the real API** on every money sheet (`suggestions.md` §5.11).
- **0902 reaches its midpoint tomorrow with 11 untouched leaves and no estimates**, including six of eight push-notification leaves and the one MVP-relevant item, `BVA-I310`.
- **`BVA-I315` is still specified against E2EE.**
- **The admin workstream is silent:** 14.9 days with no `beevia-admin` commit, 23.0 days with no board activity, and no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

Retired this edition: **"mobile `main` does not build"** (as far as manifests and markers go) and **"Start a chat breaks once #60 deploys"**.

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. Push notifications and Appearance are product work the PRD's MVP list does not score: the first serves several MVP flows indirectly, the second none. `BVA-I310`'s payment reminders remain the one 0902 item that serves an MVP flow directly (Transfer Acceptance & Escrow, PRD §10.2), and it has not started.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 30 Sep 14:03 → 7 Oct 14:03 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move**, and this week every one was board administration's.

### 6.1 Ayomikun Araoye: backend + admin API

**2 commits in 7 days**, both `Phoenixdadhev` CI edits on 1 Oct 15:48 UTC (`fa5a5de` in `beevia-api`, `aabd858` in `beevia-db-schema`). The last was **5.9 days** ago. On 0902 they now hold six leaves. They were added as co-owner of `BVA-I308` (*New Message Notification Handling*) today. Two are in REVIEW/QA — `BVA-I319` and `BVA-I328`, the preference-storage tasks. Both were started by a parent cascade (David, 30 Sep and 2 Oct) and submitted by board administration, and neither has backend code, because the client stores those preferences on the device (§2). Four are To do: the Activity Feed backend (blocked on the E2EE question), `BVA-I308`, `BVA-I310` (reminders) and `BVA-I325`. `BVA-I8` has been In progress on the admin board for 23.0 days. Median cycle time **1.22 d (n=12)**. That figure now includes the two 0902 items above (6.0 d and 4.2 d), where neither the start nor the submission was theirs. Their own-flow median is unchanged at 0.98 d (n=10). Nearly six days without a backend commit is worth one question: what are they working on? It may well be work this board does not track.

### 6.2 David Samuel: mobile

**4 commits on `main` in 7 days** (`0973bbc` 30 Sep, `03a3035` 2 Oct, `6f38116` 5 Oct, `1a1f39f` 7 Oct), plus the PR #43 merge. They hold 15 of 0902's 21 leaves: 3 In progress, 3 in REVIEW/QA, 9 To do. Their three 7-day submissions (`BVA-I318`, `I322`, `I327`) were all moved by board administration. `BVA-I286` (profile-screen UI mismatch) has been In progress for 6.9 d against a 0.96-day median and has no identifiable code. It is the one WIP item that looks stuck. `BVA-I306` and `I312` are 0.9 d old, and `1a1f39f` is `I306`'s first code. The marker fix landed on `main`, bundled rather than split, as the last three editions recommended against. What it shows about process: one person both writes and merges mobile changes, with no review step visible on the board or (from here) on GitHub.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC. `BVA-I321` (dark palette for every screen) has been In progress for 5.0 days. The dark palette is now on `main` in code (`app_colors.dart`), so this item may only be waiting for its owner to close it. Design work does not land in these repositories, so commits are not applicable.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **14.9 days** ago. The admin board has had no activity for 23.0 days, `BVA-I9` has been In progress for all of it, and no successor sprint exists. **Absence of data is not absence of work**: `beevia-admin` has no branch except `main`, so local work would be invisible here. This is the eighth edition to ask whether the workstream is paused.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | of which by the owner |
|---|---:|---:|---:|
| 2026-W37 | 7 | — | — |
| 2026-W38 | 11 | — | — |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 |
| 2026-W41 (from Mon 5 Oct) | — | **5** | **0** |

Acceptance is still zero, and owner submissions have been zero for nine days, while code reached `main` this morning. The bottleneck is not output. It is that review is not a step anyone on the team performs on the board.

### 6.6 What this does not measure

- **No estimation points on any item on any board**: 0 of 25 on 0902. Item counts say nothing about who is carrying more.
- **Who moved an item is not who did the work.** Board administration made every status change this week. The work behind the five Appearance leaves is David's (and Philip's design), and it is on `main`.
- **A parent's cascade is not a start.** `BVA-I319` and `I328` were started by David's parent moves, `BVA-I322` by Philip's.
- **Commit counts reward small commits.** `6f38116` is 60 files. Both of Ayomikun's commits are workflow edits.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 6 Oct | Status on 7 Oct |
|---|---|
| **1. Take the build fix across to mobile `main` on its own; resolve `project.pbxproj`; require Flutter CI** | ◐ **Outcome achieved, not as recommended.** Markers gone and `pbxproj` resolved on `main` via PR #43, which merged the whole 95-file feature. Required CI: not visible |
| **2. Decide 0902's scope before Thursday's midpoint; estimate the untouched leaves** | ❌ **Not done.** 0 of 25 estimated, no scope comment. One day left before the midpoint |
| **3. Put `needs: test` back on `beevia-api`'s `sync`; gate db-schema Release and admin-api Sync** | ❌ **Not done.** No backend commit |
| **4. Name a reviewer for 0902 and use the column; start with `BVA-I314`** | ◐ **Column used, reviewer not named.** Five leaves entered it, all moved by board administration. Nothing left it. `BVA-I314` is unreviewed. Seventeenth edition |
| **5. Scope `BVA-I310`'s server half** | ❌ **Not done.** No comment, no edit, no code |
| **6. Write the Appearance storage decision on `BVA-I317`; close `I319`/`I325`/`I328` if device storage stands** | ◐ **The code decided; the board did not record it.** Device storage is on `main`. `I319`/`I328` went to REVIEW/QA instead of being closed, `I325` is still To do, and no comment explains why |
| **7. Check the production host's SSH settings** | ? **Not visible from here** |
| **8. Hide the biometric option outside mock mode** | ❌ **Not done.** Still on `main`, now on every money sheet |
| **9. Correct `BVA-I315`'s acceptance criteria for E2EE** | ❌ **Not done** |
| **10. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **11. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Zoho lists only `0901-admin` |
| **12. Carried: comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec** | ❌ **None done** |

**One of twelve achieved in outcome (the build), two partly. Nine did not move.**

---

## 8. What I would do this week

Re-ranked: the build fix is done, so the 0902 scope call and the review step move to the top.

1. **Decide 0902's scope tomorrow, at the midpoint.** Estimate the 11 untouched leaves, at least the six push-notification ones, and say what will not make 15 Oct. If something must give, keep `BVA-I310`: it is the one item that serves an MVP flow.
2. **Review the five Appearance leaves for real, then close the ones that are not work.** Name the reviewer. Close `BVA-I319`, `I325` and `I328` with a one-line comment recording device storage, rather than reviewing backend tasks that have no backend code. Move `BVA-I329` forward to match `main`, and leave `BVA-I324` open until the chosen background is applied to chat screens.
3. **Make Flutter CI a required check on mobile `main`.** It is the half of `suggestions.md` §5.12 that is still open, and the one control that would have stopped PR #42's markers and checked PR #43's late Firebase commit.
4. **Put `needs: test` back on `beevia-api`'s `sync` job**, then give `beevia-db-schema`'s Release and `beevia-admin-api`'s Sync a verify job to wait on (`suggestions.md` §7.7, option (a)).
5. **Scope `BVA-I310`'s server half**: a reminder job at +12 h and at −1 h on the existing `escrow-expiry` queue, plus the notification types. With Firebase now on the client and `POST /notifications/token` on the server, this is the missing middle.
6. **Restrict the Firebase API key** to the app's Android package and iOS bundle ID in Google Cloud, if that is not already done.
7. **Check the production host's SSH settings**: `PasswordAuthentication no`, root login off, and rate limiting.
8. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
9. **Correct `BVA-I315`'s acceptance criteria for E2EE.**
10. **Bring `payments.dto.ts` onto `phone.util.ts`.**
11. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
12. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 23.0 days ago**. Today's export and sidecar are identical to 6 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 23 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 14.9 days without a commit. `beevia-admin-api`'s last change was the 1 Oct CI merge, and its last code change was 24 Sep. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed thirty-six days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance, and not whether `main` compiles.

**No score moved.** PR #43 closes two gaps that were holding scores in place rather than lowering them: the device header (#1) and the build break (never scored, by rule). The Appearance work and the Firebase set-up are outside the rubric's eleven capabilities.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | `createConversation` now sends `X-Device-Id` on `main` (`chat_service.dart:212`), so the gap that held this score is closed. No new crypto, key or socket capability, so nothing to raise it |
| 2 | Voice & video calling | 8 | 0.85 | 0 | PR #43 restyled call screens only |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter`; `translate_chat_screen.dart` restyled only |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | Onboarding screens restyled only; no `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; wallet screens restyled only |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Escrowed `payment.send` on `main`; biometric option still rejected by `stepUpSchema` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep; no `beevia-admin-api` code change since 24 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether mobile `main` actually builds.** The markers are gone and the manifests parse, but no `flutter` command ran, and CI results return `404` to this workspace.
- **Whether anyone but the author reviewed PR #43**, or whether any check was required before it merged.
- **Whether `Firebase.initializeApp` at start-up affects mock-backend builds or the test suite.** Out of scope per the owner's standing instruction; noted so nobody reads silence as a pass.
- **Whether `beevia-api` #60 is live.** It matters less now that `main` sends the header everywhere, but builds from before PR #43 still omit it on new chats.
- **Whether branch protection requires CI on any `main`.** All three ungated backend pipelines depend on it.
- **The production host's real SSH configuration.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Main board export (step 1a): 64 items, sprint 08-01, exit 0.
2. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0.
3. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0), diffed against the 6 Oct file there.
4. Fast-forward sync (step 2), exit 1: `beevia-mobile` fast-forwarded by 4 commits to `01bcf2a` (already on `main`; no branch switch), `beevia-admin` already current, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` refused as `diverged` (unchanged since 8 Sep). No controller, DTO or schema file was touched.
5. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-07`: route level and spec health clean. The in-repo audit was run too, for the board section; its 21 drift lines are the known phantom. Both ran through `uv run --no-project --with pyyaml` (see Degraded inputs).
6. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
7. File comparison of every export and sidecar against 6 Oct: 08-01 and 0901-admin identical; 0902 changed. The flow script (`flow07.py`) re-derived cycle times, the 7-day submission count split by actor, WIP ages and the weekly trend, matching all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`) and comment actions.
8. Content checks in `beevia-mobile` at `origin/main` (`d51e3d1..01bcf2a`): conflict-marker `git grep`, YAML parse of `pubspec.yaml`/`pubspec.lock`, `X-Device-Id` and biometric greps, `ChatBackground`/`Prefs` use, and the `firebase_messaging` and `/notifications` call sites. In the backend shadow: the `on:` and `needs:` lines of every workflow in all three repos, and the notifications module (`POST /notifications/token`, FCM/stub adapter selection).
9. `suggestions.md` §5.12 / §8 3f and `api-rfc.md` §5.12 status updates.
10. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive` and read-only `log`/`show`/`grep`/`diff`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-07.html`, `web-report/index.html`, `suggestions.md`, `api-rfc.md`, plus new board exports for 7 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`, which leaves nothing installed.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.** `gh` cannot resolve the organisation's repositories with the available token.
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 6 Oct 14:06 UTC → 7 Oct 14:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
