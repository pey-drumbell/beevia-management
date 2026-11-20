# Beevia — Project Status

**As of 2026-11-20** · Sprint **1002** (21 Oct → 5 Nov, **ended fifteen days ago, day 31**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, 12 of 12 items Done · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-20.csv` + `beevia-activity-2026-11-20.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-20.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 19 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 19 Nov 15:02 UTC → 20 Nov 15:02 UTC, 1.0 day (Thu → Fri).**

---

## Quick overview

> **Nothing changed today. No person has committed on any branch of any repository for three days (the last was `d55630e`, 17 Nov 05:51 UTC), and no bot has for two. Nobody touched a board: the audit trails of all three exports are byte-identical to 19 Nov. The working week ends with zero items moved into review and zero moved out, the first week in this report's trend table with nothing submitted. Sprint 1002 is fifteen days past its end with no action for 9.3 days, 24 of its 33 review items have merged code and none has been accepted, and `feat-forget-pin-fixes` is still 7,400 lines ahead of `main` with no pull request, eight days after it first appeared here.**

| Metric | 19 Nov | 20 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 19 Nov; last action 11 Nov 06:53 UTC (**9.3 days**) |
| Board actions on 0901-admin in the window | 3 | **0** | sidecar byte-identical to 19 Nov; last action 18 Nov 15:03 UTC |
| 0901-admin leaves In progress / Done | 0 / 8 | **0 / 8** | all 12 items Done, no successor sprint |
| Transitions into REVIEW/QA, last 7 days (leaves) | 0 | **0** | third consecutive zero |
| Transitions into REVIEW/QA, this ISO week (Mon → Fri 15:02 UTC) | 0 | **0** | first week in the trend table (W39 onwards) with none (§6.5) |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **37.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 | **0 / 0** | audit clean, exit 0 |
| API surface (consumer / admin) | 166 / 76 | **166 / 76** | no backend commit |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Person-authored commits on any branch in the window | 0 | **0** | third day; no Dependabot or release commit either |
| `feat-forget-pin-fixes` ahead of `main` | 3 commits, +7,443 / −774 | **unchanged** at `d55630e` | still no PR (non-Dependabot pull refs end at #58) |
| Open Dependabot PRs on `beevia-mobile` | 8 (#60, #62–#68) | **8** | no new branch or commit |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no commit to `release.yml` |
| `beevia-admin` days since a commit | 20.0 | **21.0** | |
| `beevia-mobile` days since a person's commit on `main` / on any branch | 9.0 / 2.4 | **10.0 / 3.4** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 3.1 / 12.1 / 3.1 | **4.1 / 13.1 / 4.1** | |
| Admin board: open sprint / days since any activity | none / 1.0 | **none / 2.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: nothing reached `main` (appendix) |

**No correction to the previous edition.** Every figure in the 19 Nov report was rechecked against today's exports and refs and still holds. One method note: the pre-1002 rows of the weekly trend table (§6.5) can no longer be rebuilt from a fresh export, because 0902's removed leaves are not exportable; those rows are carried from earlier editions and marked as such.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 4, all Done | **0** (last own: `I362`, 11 Nov) | 1.48 d (n=22) | none on any board | **2** (1 `beevia-api`, 1 `beevia-db-schema`) | Last commit 4.1 d ago; #111, #112 and #36 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**29.2 d**), `I361` (17.3 d). Both have code on `main` | **1**, on `feat-forget-pin-fixes` | Branch 7,400 lines ahead with no PR. Last own submission 37 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 18.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4, all Done · **1002: 0** | 0 | n/a | none | **0** (`beevia-admin`, last 30 Oct) | No commit in 21.0 days; no item open on any board |

**The three questions for standup:** (1) **What is each person working on that has not been pushed?** Three days without a commit on any remote, across four people, more likely means work sitting on laptops than no work; the ask is to push it, even unfinished, to a branch. (2) **When does `feat-forget-pin-fixes` become a pull request, and should it be split first?** It has not changed since 17 Nov. (3) **Who reviews the 24 REVIEW/QA leaves that have merged code, and when?** 1002 has had no action for 9.3 days.

**The three things worth knowing:**

1. **A fully static day, and the third without a person's commit.** No ref moved in any of the five repositories, by a person or a bot. All three sidecars (1002, 0901-admin, 08-01) are byte-identical to 19 Nov, and the CSVs differ only in their date line. The audit is clean at 166 / 76 and no document needed editing. This says nothing was *pushed* or *moved*; it does not say nothing was done. A quiet remote has misled this report before (27 Oct), so it is a question for standup, not a finding (§3, §6).

2. **The week, in one view.** Code: #112 and `beevia-db-schema` #36 merged on Monday (message edit and delete), `d55630e` reached the mobile branch on Tuesday (the app side of #112), Dependabot opened five PRs on Wednesday, and nothing landed on Thursday or Friday. Board: one action all week, Wednesday's close of the admin story `I7` with its two children. Nothing moved into review and nothing moved out. Of yesterday's 28 recommendations none moved; the first of them, a pull request for the mobile branch, is now in its seventh edition (§6.5, §7).

3. **Four clocks keep running while the board stands still.** Sprint 1002 ended fifteen days ago with no sweep, no successor and 36 of 44 leaves not Done. The wrong-PIN lock has been on the API's `main` since 12 Nov, which deploys on push, while the only way out for a locked user sits on the unmerged branch. The grace period before the NIN requirement bites for existing users ends about 6 Dec, **16 days** from now, and whether the tier limits are then enforced is still undecided. The provisional MVP target passed eighty days ago (§1.2, §4).

**If you read nothing else:** ask at standup what is unpushed, open the pull request for `feat-forget-pin-fixes` (or split it), and start review on the 24 REVIEW/QA items whose code is already on `main`.

---

## 1. Board movement

### 1.1 All five boards: no action

**No item on any board was created, moved, reassigned, commented on or edited in the window.**

| Board | Items | Last action | Compared with 19 Nov |
|---|---:|---|---|
| 1002 (live, scratch export) | 63 (44 leaves + 19 parents) | 11 Nov 06:53 UTC, 9.3 days ago | sidecar byte-identical; CSV identical apart from its date line |
| 0901-admin | 12 (8 leaves + 4 parents), all Done | 18 Nov 15:03 UTC, 2.0 days ago | sidecar byte-identical; CSV identical apart from its date line |
| 08-01 (the in-repo main export) | 64, all Done | 3 Sep | sidecar byte-identical |
| 0902, 0901 | closed | 21 Oct, 30 Sep | re-exported today for cycle times only; no action since their closes |

1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–20 Nov (to 15:02) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

The audit's `SINCE` block compares two 08-01 exports and correctly reports no change (0 left review, 0 newly Done, 0 entered review). `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

### 1.2 Fifteen days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902 was swept six days after its end; 1002 is nine days beyond that, with no sweep and no successor. A sweep would mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111 (the unreadable-message count), #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes` (Forgot PIN, the app side of #112, forwarding, starred messages, voice-note work); eight open Dependabot PRs. That is a gap in the board, not a judgement on the work.

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

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 29.2 d and 17.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-20`), it reported 166/166 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). No spec file was edited. The in-repo audit still reports the same phantom lines from the three `diverged` working trees (2 / 37 / 42). They were not acted on.

| Repo | `origin/main` | What |
|---|---|---|
| `beevia-api` | `a5cf9b5` | Unchanged since 16 Nov. `feat/message-edit` and `feat/voice-notes` still on the remote, 0 commits ahead of `main` |
| `beevia-admin-api` | `b4e9744` | Unchanged since 7 Nov. Still pins `beevia-db-schema` 0.0.50. `feat/support-inbox` still on the remote |
| `beevia-db-schema` | `bcc45fb` (v0.0.55) | Unchanged since 16 Nov |
| `beevia-admin` | `64304ef` (30 Oct) | Unchanged. No branch besides `main`, no pull ref |
| `beevia-mobile` | `e40116d` | Unchanged since 10 Nov. `feat-forget-pin-fixes` at `d55630e`, no PR. The eight Dependabot branches and `App-bundle` unchanged |

**No commit on any ref in any repository in the window**, by a person or by a bot. Every `origin/main` is at the same commit as in the 19 Nov edition, so every code finding in that edition stands by identity, not by re-reading.

### 3.1 The standing checks

All of these depend only on code that did not change:

- **PIN lock (#110):** the three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists.
- **`beevia-api` `release.yml`:** `sync` still has no `needs: test` and still runs `pnpm db:migrate` on push to `main`.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is on 0.0.55.
- **`call.ended`** is still unhandled, and Forgot PIN on `main` is still a stub.
- **Dependabot:** #64–#68 unchanged since 18 Nov. The cautions in the 18 Nov edition §3.1 stand (#66 and #67 together; #68 needs a push test on a device).
- **Branch protection, PR reviews and CI results:** cannot be seen from here.

### 3.2 Document changes this cycle

**None.** The audit was clean and no route moved, so no OpenAPI file, `api-rfc.md`, `admin-api-rfc.md` or `suggestions.md` changed. Per the audit skill, on a clean day documents that are already correct are left alone.

---

## 4. Risks

No risk was added or retired today. The order is by how soon each one bites.

- **A locked-out user has no way out on `main`.** The wrong-PIN lock has been on the API's `main` since 12 Nov, which deploys on push, and Forgot PIN on the app's `main` is still a stub. The fix is on the unmerged branch.
- **One large unreviewed branch is the only path for three user-facing fixes:** a way out of the PIN lock, offline delete, and edit. Unchanged since 17 Nov, no PR.
- **The 30-day NIN clock.** The limits are still not enforced. The grace for existing users ends about 6 Dec, **16 days from now**.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended fifteen days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **Work may be sitting unpushed.** Three days with no commit on any remote. If that is local work, it has no backup and no review; if it is not, the team is waiting on something this report cannot see.
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **Major dependency bumps waiting on a reviewer.** #66/#67 (ML Kit) and #68 (notifications) are unchanged.
- **A production data migration with no test gate.** Whether 0.0.55 ran cleanly is not visible.
- **Done on the admin board means "closed by the story's owner", never "reviewed".** None of its 12 items passed through REVIEW/QA. The same mechanism closed `I381` on 1002 without its code.
- **The admin dashboard has no open board item anywhere** and no commit for 21 days, while three admin items on 1002 have no assignee.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. Nothing in the window touched any of them. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 13 Nov 15:02 → 20 Nov 15:02 UTC. Commit counts are non-merge commits on all remote branches in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (1 release commit on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** were recomputed today from fresh exports of 0901, 0902 and 1002 and are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**2 commits in 7 days**: 1 in `beevia-api` (#112's feature commit, 16 Nov) and 1 in `beevia-db-schema` (#36, 16 Nov). The drop from 3 is #111 (12 Nov) leaving the window, not a change of pace. **Zero submissions** into review, and **no board action** in the window. Ayomikun has **no WIP on any board**. The last commit is the #112 merge on 16 Nov, 4.1 days ago. None of the week's commits is an item on any board, so the board gives no hint of what comes next.

### 6.2 David Samuel: mobile

**1 commit** in 7 days, `d55630e` on `feat-forget-pin-fixes` (17 Nov 05:51 UTC), 3.4 days ago. None in the window. **Zero submissions.** The last own submission was `I286` on 14 Oct, **37.0 days** ago. A branch with no PR cannot meaningfully be moved to review, so this reads as a board gap rather than idle time. **WIP: 2 items, both with code on `main`**: `I331` at 29.2 days and `I361` at 17.3 days. This still reads as items left in the wrong column rather than stuck work; that is for David to say.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** The last board action by Philip was on 2 Nov 15:58 UTC, **18.0 days** ago. Philip may be finished, blocked or working untracked; worth a question, not an assumption. Forwarding, starred messages, message editing and Forgot PIN exist in code with no design item on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **21.0 days** old, and `beevia-admin` has no other branch or pull ref. **Promise has no open item on any board**, and the admin items on 1002 (`I348` in REVIEW/QA, `I349` and `I351` To do) are unassigned. This report does not read a quiet remote as nothing having been done; the question is what the current work is and where it is tracked.

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
| 2026-W47 (16 → 20 Nov, to 15:02 UTC) | — | — | **0** | 0 | 0 | 0 |

The 1002 rows were recomputed today. The W39–W42 rows are carried from earlier editions: 15 of 0902's leaves were removed from that sprint on 21 Oct and their history is no longer in any export.

**W47 is the first week in this table with no transition into review**, with the weekend still to come. Two things would produce this even with nobody slowing down: the week's merged backend work (#112, #36) has no board item to move, and the mobile work is on a branch with no PR. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. **The bottleneck is the board and review process, not the developers.**

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 4,000-line commit and a one-line fix count the same.
- **Unpushed work.** A quiet remote says nothing about local work, and three quiet days say no more than one.
- **Untracked work.** #110, #111, #112, #35, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **Who moved an item is not whether it is done.** `I9` was moved by its parent's close, not by its owner.
- **Commit counts reward small commits,** and a quiet week after a 47-file commit is not a slowdown.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 19 Nov | Status on 20 Nov |
|---|---|
| **1. Open a PR for `feat-forget-pin-fixes`, or split it, and review it** | ❌ **No.** Non-Dependabot pull refs still end at #58; the branch is unchanged. First recommended 12 Nov, seventh edition |
| **2. Put that work, and #110–#112, #35, #36, on the board** | ❌ **No** |
| **3. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No action on 1002** |
| **4. Close 1002 deliberately** | ❌ **Not done, fifteen days late.** No successor, no sweep, filter still 08-01 |
| **5. Give the admin dashboard current work on a board, with Promise as owner** | ❌ **No.** No admin sprint; `I348`, `I349`, `I351` still unassigned |
| **6. Give the Dependabot queue an owner** | ❌ **Not visible.** All eight PRs still open |
| **7. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No `beevia-api` commit |
| **8. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No** |
| **9. Two-device chat on a build of the branch** | ❌ **Not visible** |
| **10. Decide whether the tier limits are enforced** | ❌ **No.** 16 days left |
| **11. Confirm migration 0055 ran cleanly in production** | ❌ **Not visible** |
| **12. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **13. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **14. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **15. Handle `call.ended` in the app** | ❌ **No** |
| **16. NIN step and support screens on the board** | ❌ **No** |
| **17. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **18. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **19. Record the consent behind each lookup** | ❌ **No** |
| **20. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **21. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **22. Bring the dashboard onto the real contract** | ❌ **No commit in 21.0 days** |
| **23. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **24. Assign `I359` and `I390`** | ❌ **No** |
| **25. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **26. `needs: test` on `sync`; verify jobs; admin-api onto 0.0.55** | ❌ **No** |
| **27. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No** |
| **28. Carried items** | ❌ **None moved** |

**None of the 28 moved, fully or in part.** "Not visible" marks the ones that could have happened without leaving a trace in git or on a board; the rest would have.

---

## 8. What I would do this week

The list is unchanged from 19 Nov apart from the new first point. Twenty-eight carried items is too many to act on, so the first five are the ones that unblock the rest.

1. **Push what is local, today, to a branch (new).** Three days with nothing on any remote. Unfinished work on a pushed branch can be backed up, seen and reviewed; work on a laptop cannot. This is a habit to agree at standup, not a criticism of anyone.
2. **Open a PR for `feat-forget-pin-fixes`, or split it first, and review it (carried, seventh edition).** It holds three separable pieces: Forgot PIN, the app side of #112, and forwarding/starred/voice-note work. Smaller PRs would let the PIN way-out and the offline-delete fix ship without waiting for the rest. In that review, settle the 15-minute edit window (`suggestions.md` §4.20) and ask whether the in-app Paystack WebView was a decision.
3. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
4. **Then close 1002 deliberately (carried, fifteen days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and the items from point 5. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
5. **Put the untracked work on the board with an owner and a design item (carried):** the branch's three pieces, and #110–#112, #35 and #36.
6. **Give the admin dashboard current work on a board, with Promise as owner (carried).** Either open an admin sprint, or assign `I348`, `I349` and `I351` on 1002 to Promise. Then agree that a child owned by someone else is not closed by its parent's close.
7. **Decide whether the tier limits are enforced, and what the end of the grace does (carried, 16 days left).** About 6 Dec is the date for existing users.
8. **Give the Dependabot queue an owner (carried).** Merge #64 and #65 after a build. Merge #66 and #67 together, after one on-device translation run. Merge #68 after a push test on a device. Close #60, #62 and #63 or merge them with the rest.
9. **Make the PIN check reserve its attempt before comparing (carried).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
10. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
11. **Run one two-device chat on a build of the branch (carried).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
12. **Confirm migration 0055 ran cleanly in production (carried).**
13. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
14. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
15. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
16. **Handle `call.ended` in the app (carried).**
17. **Put the NIN step and the support screens on the board with a design and an owner (carried).**
18. **Decide the seeded card default and what a card limit is, on the record (carried).**
19. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
20. **Record the consent behind each BVN and NIN lookup (carried).**
21. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
22. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
23. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
24. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
25. **Assign `I359` and `I390` (carried).**
26. **Retire `GET /cards/{id}/transactions` (carried).**
27. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.55 (carried).
28. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
29. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

**`0901-admin` is unchanged: 12 of 12 items Done (8 leaves + 4 parents), no action in the window.** Its sidecar is byte-identical to 19 Nov. The last action was the close of the story `BVA-I7` with its children `I8` and `I9` on 18 Nov at 15:03 UTC, 2.0 days ago.

| Status | 19 Nov | 20 Nov |
|---|---:|---:|
| Leaves In progress | 0 | **0** |
| Leaves Done | 8 | **8** |
| Parents Done | 4 of 4 | **4 of 4** |
| Days since any activity | 1.0 | **2.0** |

The sprint ended 22 Sep. **Zoho lists no successor sprint for this project**, so the admin dashboard has no open item on its own board. Admin-dashboard work that is tracked at all sits on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 21.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed eighty days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** No `origin/main` moved in any repo, so every score stands on the same code as on 19 Nov.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Edit client, catch-up `changes` and the voice-note recorder are all on an unmerged branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound. ML Kit bumps (#66, #67) unmerged |
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

- **Whether anyone has unpushed work, and how much.** Only remotes are visible.
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

1. A sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects), then three parallel background exports from 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 19 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical and CSV identical apart from its date line. 0901 (76 items) and 0902 (8 items) were re-exported to scratch with `--activity --no-descriptions`, for cycle times only.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-20`: exit 0. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow20.py`, a date-shifted copy of 19 Nov's). It listed every action in the window (none), split 7-day submissions by actor, and computed cycle medians, WIP ages and the 1002 rows of the weekly trend.
5. Content checks. `fetch` of heads and `refs/pull/*` in all five repos; a `git log` of every remote ref since 19 Nov 15:00 UTC (empty); `origin/main` and branch heads compared with the SHAs recorded in the 19 Nov edition (all equal).
6. Document update: none needed (§3.2).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch` (including the `refs/pull/*` mirror into `refs/remotes/origin/pr/*`), `git archive`, and read-only `log`/`diff`/`rev-list`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-20.html` and `web-report/index.html`. New board exports for 20 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The W39–W42 rows of the weekly trend are carried, not recomputed.** A fresh 0902 export holds 8 items; the 15 leaves removed on 21 Oct are gone from it.
- **The item-to-code mapping for the 24 REVIEW/QA leaves was carried** (backend from 11 Nov, mobile from 10 Nov). No code changed since, so it was not re-derived item by item.

**Window.** 19 Nov 15:02 UTC → 20 Nov 15:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
