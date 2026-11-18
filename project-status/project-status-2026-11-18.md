# Beevia — Project Status

**As of 2026-11-18** · Sprint **1002** (21 Oct → 5 Nov, **ended thirteen days ago, day 29**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-18.csv` + `beevia-activity-2026-11-18.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-18.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 17 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 17 Nov 15:02 UTC → 18 Nov 15:02 UTC, 1.0 day (Tue → Wed).**

---

## Quick overview

> **Nothing moved in the window. No person committed to any repository on any branch, no board item changed on any of the five boards, and no document needed an update. The only new activity is five Dependabot pull requests on `beevia-mobile` (#64–#68). Two of them are major-version bumps of the on-device translation libraries. Because the 11 Nov submission has aged out, the rolling 7-day count of items moved into review is now zero for the first time since sprint 1002 began. The board has had no action for 7.3 days. 1002 is thirteen days past its end. None of its 33 review items has been accepted. `feat-forget-pin-fixes` still has no pull request.**

| Metric | 17 Nov | 18 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 17 Nov; last action 11 Nov 06:53 UTC (**7.3 days**) |
| Transitions into REVIEW/QA, last 7 days (leaves) | 1 | **0** | `I362` (11 Nov 06:53) left the window; **first zero since 1002 began** |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **35.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 | **0 / 0** | audit clean, exit 0 |
| API surface (consumer / admin) | 166 / 76 | **166 / 76** | no backend commit |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Person-authored commits on any branch in the window | 1 (`d55630e`) | **0** | in all five repos |
| `feat-forget-pin-fixes` ahead of `main` | 3 commits, 109 files, +7,443 / −774 | **unchanged** | still no PR (non-Dependabot pull refs end at #58) |
| Open Dependabot PRs on `beevia-mobile` | 5 (#59–#63) | **8** (#60, #62–#68) | #64–#68 opened 03:54–03:58 UTC; #59 and #61 superseded by #64 and #68 |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no commit to `release.yml` |
| `beevia-admin` days since a commit | 18.0 | **19.0** | |
| `beevia-mobile` days since a person's commit on `main` / on any branch | 7.0 / 0.4 | **8.0 / 1.4** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 1.1 / 10.1 / 1.1 | **2.1 / 11.1 / 2.1** | |
| Admin board: open sprint / days since any activity | none / 64.0 | **none / 65.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: nothing reached `main` (appendix) |

**No correction to the previous edition.** Every claim in it still holds. One figure has moved only because time passed: the 7-day submission count was 1 because `I362` was inside the window, and today it is 0.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **0** (last own: `I362`, 11 Nov) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**65.0 d**) | **5** (3 `beevia-api`, 2 `beevia-db-schema`) | Last commit 2.1 d ago; #110, #111, #112 and #36 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**27.2 d**), `I361` (15.3 d). Both have code on `main` | **3**, all on `feat-forget-pin-fixes` | Branch 7,400 lines ahead with no PR. Last own submission 35 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 16.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**65.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 19.0 days; possibly unpushed work |

**The three questions for standup:** (1) **When does `feat-forget-pin-fixes` become a pull request, and should it be split first?** It has been unchanged for a day and is ready to be opened as it stands. (2) **Who reviews the 24 REVIEW/QA leaves that have merged code, and when?** The board has had no action for 7.3 days. (3) **Who handles the Dependabot queue?** It now has eight open PRs, two of them major bumps of the libraries behind on-device translation.

**The three things worth knowing:**

1. **A quiet day, not yet a trend.** No person committed anywhere and nobody touched any board. The last board action was 11 Nov. The last person-authored commit was `d55630e` on the branch, 17 Nov 05:51 UTC. 13–15 Nov were just as quiet and were followed by #112 and the branch commit, so one silent day says little on its own (§1, §6).

2. **Moves into review have stopped as well as moves out of review.** The 7-day count of transitions into REVIEW/QA is 0. Transitions out of REVIEW/QA have been 0 on 1002 since the sprint began. Code kept landing through 16 Nov without board items (#110, #111, #112, #36), so the board now records neither the work arriving nor its acceptance. This is a process gap, not anyone's output (§1.3, §6.5).

3. **Two of the new Dependabot PRs are major bumps that touch shipped code paths.** #66 and #67 move `google_mlkit_language_id` and `google_mlkit_translation` from 0.15.1 to 1.0.3. `lib/core/language/on_device_translation_service.dart` on `main` uses both. #68 moves `flutter_local_notifications` from 22.3.3 to 23.0.2; `push_notification_manager.dart` and `notification_service.dart` use it. Each changes only `pubspec.yaml` and `pubspec.lock`. Whether the app still builds against them is not visible from here. Merging them needs a build, not a glance at the diff (§3.1).

**If you read nothing else:** open the pull request for `feat-forget-pin-fixes` (or split it), and spend this week's review time on the 24 items whose code is already on `main`.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 17 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change (0 left review, 0 newly Done, 0 entered review). 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **No action in the window.** The 1002 sidecar is byte-identical to 17 Nov, and so is the CSV apart from its date line. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–18 Nov (to 15:02) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 Thirteen days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902, the one precedent, was swept six days after its end; 1002 is now seven days beyond that, with no sweep and no successor. A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111 (the unreadable-message count), #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes`, which carries Forgot PIN, the app side of #112, forwarding, starred messages and voice-note work; eight open Dependabot PRs. That is a gap in the board, not a judgement on the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

Unchanged since 11 Nov.

| REVIEW/QA leaves (33) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | 12 | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391`, `I362` | Routes on `origin/main`. `I387` caps funding, not spending. `I391` lacks the pagination, search and filter it asks for. `I362` reports limits and does not enforce them |
| Mobile, matching merged code | 12 | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, `I386` | On `main` since #58 (10 Nov). `I390` is still unassigned |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Moved to review, no matching code | 2 | `I348`, `I372` | `I348`: the dashboard screen is mock only. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 27.2 d and 15.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-18`), it reported 166/166 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). No spec file was edited. The in-repo audit still reports the same phantom lines from the three `diverged` working trees (2 / 37 / 42). They were not acted on.

| Repo | `origin/main` | What |
|---|---|---|
| `beevia-api` | `a5cf9b5` | Unchanged. `feat/message-edit` and `feat/voice-notes` are still on the remote, 0 commits ahead of `main` |
| `beevia-admin-api` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50. `feat/support-inbox` still on the remote |
| `beevia-db-schema` | `bcc45fb` (v0.0.55) | Unchanged |
| `beevia-admin` | `64304ef` (30 Oct) | Unchanged. No branch besides `main`, no pull ref |
| `beevia-mobile` | `e40116d` | Unchanged. `feat-forget-pin-fixes` unchanged at `d55630e`, no PR. **Five new Dependabot branches and PRs** |

### 3.1 The new Dependabot pull requests (`beevia-mobile`)

All five were opened between 03:54 and 03:58 UTC by `dependabot[bot]`. Each touches only dependency manifests. Their branches were read; nothing was built.

| PR | Bump | Kind | Code on `main` that uses it |
|---|---|---|---|
| #64 | Android Gradle plugin 9.4.1 → 9.5.1, `google-services` 4.5.0 → 4.6.0, Gradle wrapper | minor | build only. **Supersedes #59** (its branch was rewritten) |
| #65 | `flutter_svg` 2.3.2 → 2.4.0, `flutter_dotenv` 6.0.1 → 6.0.2, `cached_network_image` 4.0.6 → 4.0.7 | minor / patch | widespread |
| #66 | `google_mlkit_language_id` 0.15.1 → **1.0.3** | **major** | `lib/core/language/on_device_translation_service.dart` |
| #67 | `google_mlkit_translation` 0.15.1 → **1.0.3** | **major** | the same file |
| #68 | `flutter_local_notifications` 22.3.3 → **23.0.2** | **major** | `push_notification_manager.dart`, `notification_service.dart`. **Supersedes #61** (23.0.0) |

#60, #62 and #63 (Firebase BoM, `firebase_messaging`, `firebase_core`) remain open from 11 Nov. Whether GitHub shows #59 and #61 as closed cannot be seen from here; their branches no longer exist. **Two cautions for whoever merges them.** #66 and #67 should move together. Both also bump the shared `google_mlkit_commons`, so merging one without the other is likely to leave the two plugins disagreeing on it. And #68 changes the library behind the app's push-notification code, so test a push on a device before merging. Neither caution is a finding about the code: nothing here was run.

### 3.2 The standing checks

- **PIN lock (#110):** no `beevia-api` commit since 16 Nov. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists.
- **`beevia-api` `release.yml`:** no commit touched it. `sync` still has no `needs: test` and still runs `pnpm db:migrate` on push to `main`.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is on 0.0.55.
- **`call.ended`** is still unhandled, and Forgot PIN on `main` is still a stub. Neither file changed.
- **Branch protection, PR reviews and CI results:** cannot be seen from here.

### 3.3 Document changes this cycle

**None.** The audit was clean and no route moved, so no OpenAPI file, `api-rfc.md`, `admin-api-rfc.md` or `suggestions.md` changed. Per the audit skill: on a clean day, do not rewrite documents that are already correct.

---

## 4. Risks

- **One large unreviewed branch is the only path for three user-facing fixes:** a way out of the PIN lock, offline delete, and edit. Unchanged since 17 Nov.
- **Major dependency bumps waiting on a reviewer who is not there.** If the review step stays empty, Dependabot PRs pile up and are later merged in bulk, or skipped. Either way the translation and notification paths take on untested changes. *(New.)*
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A locked-out user has no way out on `main`.** The lock is live, and Forgot PIN on `main` is still a stub.
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **A production data migration with no test gate.** Whether 0.0.55 ran cleanly is not visible.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended thirteen days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **The 30-day NIN clock.** The limits are still not enforced. The grace for existing users ends about 6 Dec, **18 days from now**.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** none.

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. Nothing in the window touched any of them. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 11 Nov 15:02 → 18 Nov 15:02 UTC. Commit counts are non-merge commits on all remote branches in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (2 release commits on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**5 commits in 7 days**: 3 in `beevia-api` (#110 on 11 Nov, #111 on 12 Nov, #112 on 16 Nov) and 2 in `beevia-db-schema` (#35, #36). The drop from 9 is the window moving past four 11 Nov commits made before 15:02, not a change of pace. **Zero submissions in the window**: `I362` (11 Nov 06:53) has aged out. **No WIP on 1002.** No commit since 16 Nov, 2.1 days. None of the five commits is an item on any board. `BVA-I8` has been In progress on the closed admin board for 65.0 days.

### 6.2 David Samuel: mobile

**3 commits** in 7 days, all on `feat-forget-pin-fixes`: 11 Nov 19:09, 12 Nov 06:49 and 17 Nov 05:51 UTC. None in the window. **Zero submissions.** His last own submission was `I286` on 14 Oct, **35.0 days** ago. As before, a branch with no PR cannot meaningfully be moved to review, so this reads as a board gap rather than idle time. **WIP: 2 items, both with code on `main`**: `I331` at 27.2 days and `I361` at 15.3 days. This still reads as items left in the wrong column rather than stuck work; that is for him to say.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** His last board action was on 2 Nov 15:58 UTC, **16.0 days** ago: he may be finished, blocked or working untracked. Worth a question, not an assumption. Forwarding, starred messages, message editing and Forgot PIN exist in code with no design item on the board. Design files are not in git, so whether a design preceded them is not visible.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **19.0 days** old, and `beevia-admin` has no other branch or pull ref. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee; `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 65.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (2 → 8 Nov) | — | — | **16** | 8 | 6 | 2 |
| 2026-W46 (9 → 15 Nov) | — | — | **1** | 1 | 0 | 0 |
| 2026-W47 (16 → 18 Nov, to 15:02 UTC) | — | — | 0 | 0 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. Code arrived in the same period that the board went quiet: #110 to #112, #35 and #36, and the branch. **The bottleneck is the board and review process, not the developers.**

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 4,000-line commit and a one-line fix count the same.
- **Who moved an item is not whether it is done.**
- **Untracked work.** #110, #111, #112, #35, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits,** and a quiet day after a 47-file commit is not a slowdown.
- **Unpushed work.** A quiet remote says nothing about local work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 17 Nov | Status on 18 Nov |
|---|---|
| **1. Open a PR for `feat-forget-pin-fixes`, or split it, and review it** | ❌ **No.** Non-Dependabot pull refs still end at #58; the branch is unchanged |
| **2. Put that work on the board, with an owner and a design item** | ❌ **No board action at all** |
| **3. Settle the edit window in that review** | ❌ **No.** There is no review yet |
| **4. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No `beevia-api` commit |
| **5. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No board action at all** |
| **6. Close 1002 deliberately** | ❌ **Not done, thirteen days late.** No successor, no sweep, filter still 08-01 |
| **7. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No** |
| **8. Two-device chat on a build of the branch** | ❌ **Not visible** |
| **9. Confirm migration 0055 ran cleanly in production** | ❌ **Not visible** |
| **10. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **11. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **12. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **13. Handle `call.ended` in the app** | ❌ **No** |
| **14. NIN step and support screens on the board** | ❌ **No** |
| **15. Decide whether the tier limits are enforced** | ❌ **No** |
| **16. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **17. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **18. Record the consent behind each lookup** | ❌ **No** |
| **19. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **20. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **21. Bring the dashboard onto the real contract** | ❌ **No commit in 19.0 days** |
| **22. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **23. Parent status moves; assign `I348`, `I349`, `I351`, `I359`, `I390`; admin sprint** | ❌ **No** |
| **24. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **25. `needs: test` on `sync`; verify jobs; admin-api onto 0.0.55** | ❌ **No** |
| **26. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No** |
| **27. Carried items** | ❌ **None moved** |

**None of the 27 moved, fully or in part.**

---

## 8. What I would do this week

1. **Open a PR for `feat-forget-pin-fixes`, or split it first, and review it (carried).** It holds three separable pieces: Forgot PIN, the app side of #112, and forwarding/starred/voice-note work. Smaller PRs would let the PIN way-out and the offline-delete fix ship without waiting for the rest. In that review, settle the 15-minute edit window (`suggestions.md` §4.20) and ask whether the in-app Paystack WebView was a decision.
2. **Put that work, and #110–#112, #35 and #36, on the board with an owner and a design item (carried).**
3. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
4. **Then close 1002 deliberately (carried, thirteen days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and the new items from point 2. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
5. **Give the Dependabot queue an owner (new).** Merge #64 and #65 after a build. Merge #66 and #67 together, after one on-device translation run. Merge #68 after a push test on a device. Close #60, #62 and #63 or merge them with the rest.
6. **Make the PIN check reserve its attempt before comparing (carried).** Use one conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
7. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
8. **Run one two-device chat on a build of the branch (carried).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
9. **Decide whether the tier limits are enforced, and what the end of the grace does (carried, 18 days left).** About 6 Dec is the date for existing users.
10. **Confirm migration 0055 ran cleanly in production (carried).**
11. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
12. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
13. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
14. **Handle `call.ended` in the app (carried).**
15. **Put the NIN step and the support screens on the board with a design and an owner (carried).**
16. **Decide the seeded card default and what a card limit is, on the record (carried).**
17. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
18. **Record the consent behind each BVN and NIN lookup (carried).**
19. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
20. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
21. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
22. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
23. **Agree how parent status moves work; assign `I348`, `I349`, `I351`, `I359` and `I390`; give the admin dashboard a sprint (carried).**
24. **Retire `GET /cards/{id}/transactions` (carried).**
25. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.55 (carried).
26. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
27. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 65.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 65 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 19.0 days ago and has no other branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-eight days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** Nothing reached `main` in any repo, and no branch changed apart from Dependabot's. When `feat-forget-pin-fixes` merges, line 1 (E2EE messaging) is the line to revisit.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Edit client, catch-up `changes` and the voice-note recorder are all on an unmerged branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound. The ML Kit major bumps (#66, #67) are unmerged and change no score |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether the branch builds, runs, or edits and deletes correctly against the server.** Nothing was run.
- **Whether the app builds against the Dependabot bumps**, and whether GitHub shows #59 and #61 as closed.
- **Whether #112 is live and whether migration 0055 ran cleanly.** The workflow deploys and migrates on push; its result is not visible.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the pull requests were reviewed or approved.**
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag, on the in-app Paystack checkout, on the 15-minute edit window or on device-only stars, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three sequential background exports from about 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 17 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical and CSV identical apart from its date line. Then a sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects). 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-18`: exit 0. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow18.py`, a date-shifted copy of 17 Nov's). It listed every action in the window (none), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `fetch` of heads and `refs/pull/*`, and `ls-remote`, in all five repos. A `git log` of every remote ref since 17 Nov 15:00 UTC. In `beevia-mobile`: the five new Dependabot commits (stat and manifest diff), the PR-to-branch mapping for #59–#68, and a `git grep` of `main` for the bumped packages. The ahead-count and shortstat of `feat-forget-pin-fixes`.
6. Document update: none needed (§3.3).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch` (including the `refs/pull/*` mirror), `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-18.html` and `web-report/index.html`. New board exports for 18 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 17 Nov 15:02 UTC → 18 Nov 15:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
