# Beevia — Project Status

**As of 2026-11-19** · Sprint **1002** (21 Oct → 5 Nov, **ended fourteen days ago, day 30**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, **now 12 of 12 items Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-19.csv` + `beevia-activity-2026-11-19.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-19.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 18 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 18 Nov 15:02 UTC → 19 Nov 15:02 UTC, 1.0 day (Wed → Thu).**

---

## Quick overview

> **A second day with no commit by anyone on any branch of any repository. The only change is on the admin board: 92 seconds after the previous edition's cut-off, Ayomikun closed the story `BVA-I7` (*User & KYC Report*), and its two children `I8` and `I9` went to Done with it in the same millisecond. That ends the two 65-day In-progress items the last nine editions carried, and the closed 0901-admin sprint is now 12 of 12 Done. The code behind it is not new. The signups report with verification and account-type breakdowns reached `beevia-admin-api` on 10 Sep and the dashboard on 14 Sep, so this is the board catching up with code, not delivery in the window. Sprint 1002 is unchanged: no action for 8.3 days, fourteen days past its end, 24 of 33 review items with merged code, none accepted.**

| Metric | 18 Nov | 19 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 18 Nov; last action 11 Nov 06:53 UTC (**8.3 days**) |
| Board actions on 0901-admin in the window | 0 | **3** | `I7`, `I8`, `I9` In progress → Done, 18 Nov 15:03:34 UTC, one action, by the story's owner |
| 0901-admin leaves In progress / Done | 2 / 6 | **0 / 8** | all 12 items (8 leaves + 4 parents) Done |
| Transitions into REVIEW/QA, last 7 days (leaves) | 0 | **0** | second consecutive zero |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **36.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | the admin closes went In progress → Done, not out of review |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 | **0 / 0** | audit clean, exit 0 |
| API surface (consumer / admin) | 166 / 76 | **166 / 76** | no backend commit |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Person-authored commits on any branch in the window | 0 | **0** | in all five repos; no Dependabot commit either |
| `feat-forget-pin-fixes` ahead of `main` | 3 commits, +7,443 / −774 | **unchanged** at `d55630e` | still no PR (non-Dependabot pull refs end at #58) |
| Open Dependabot PRs on `beevia-mobile` | 8 (#60, #62–#68) | **8** | no new branch or commit |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no commit to `release.yml` |
| `beevia-admin` days since a commit | 19.0 | **20.0** | |
| `beevia-mobile` days since a person's commit on `main` / on any branch | 8.0 / 1.4 | **9.0 / 2.4** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 2.1 / 11.1 / 2.1 | **3.1 / 12.1 / 3.1** | |
| Admin board: open sprint / days since any activity | none / 65.0 | **none / 1.0** | the 18 Nov 15:03 closes |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: nothing reached `main`, and board status is never score evidence (appendix) |

**No correction to the previous edition, with one timing note.** The 18 Nov edition said `BVA-I8` and `BVA-I9` had been In progress "for all 65 days" and that the admin board had not changed since 14 Sep. Both were true at its 15:02 UTC cut-off; the closes landed at 15:03:34. Its admin figures are superseded today, not wrong.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 4, **all Done** | **0** (last own: `I362`, 11 Nov) | 1.48 d (n=22) | **none on any board** (`BVA-I8` closed) | **3** (2 `beevia-api`, 1 `beevia-db-schema`) | Closed `I7`/`I8`/`I9` yesterday; last commit 3.1 d ago; #111, #112 and #36 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**28.2 d**), `I361` (16.3 d). Both have code on `main` | **1**, on `feat-forget-pin-fixes` | Branch 7,400 lines ahead with no PR. Last own submission 36 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 17.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4, **all Done** · **1002: 0** | 0 | n/a | **none** (`BVA-I9` closed with its story) | **0** (`beevia-admin`, last 30 Oct) | No commit in 20.0 days; no item open on any board |

**The three questions for standup:** (1) **When does `feat-forget-pin-fixes` become a pull request, and should it be split first?** It has not changed since 17 Nov. (2) **Who reviews the 24 REVIEW/QA leaves that have merged code, and when?** The admin closes show the board can be brought in line with code; 1002 has had no action for 8.3 days. (3) **What is Promise working on now?** The admin board has nothing open, `beevia-admin` has had no commit for 20 days, and the three admin items on 1002 (`I348`, `I349`, `I351`) have no assignee.

**The three things worth knowing:**

1. **The admin board is closed out, and it took one click on a parent.** `I7`, `I8` and `I9` changed within 4 ms of each other, the pattern of a parent close moving its children. Ayomikun owns `I7` and `I8`; `I9` (*Report Content Display*) is Promise's and moved with them. Every Done on that board has arrived the same way since 8 Sep. Nothing on it ever passed through REVIEW/QA. This is a point about how the board is used, not about either person (§1.1, Admin dashboard board).

2. **The code behind the close is real, and two months old.** `I7` asks for signups in a period with counts by verification status and by account type. `beevia-admin-api` `5654c7e` (10 Sep) added exactly that to the `user_signups` report, and `beevia-admin` `f12135b` (14 Sep) renders breakdown cards from the report's totals. So the 65-day "In progress" was a stale card, not stuck work. MVP line 11 does not move, because it already counted this code (§3.1).

3. **Everything else held still.** No commit by a person or by Dependabot on any ref of any repo. Sprint 1002's export and sidecar are byte-identical to 18 Nov. Transitions into review have now been zero for seven days, and transitions out of review on 1002 have been zero since it began (§1.2, §6.5).

**If you read nothing else:** open the pull request for `feat-forget-pin-fixes` (or split it), and give the 24 REVIEW/QA items whose code is already on `main` the same treatment the admin board got yesterday, but through review rather than a parent close.

---

## 1. Board movement

### 1.1 Sprint 0901-admin

**Three items moved, all in one action:** 18 Nov 15:03:34.773–.777 UTC, In progress → Done, by Ayomikun Araoye.

| Item | Type | Owner | Parent | Was In progress since |
|---|---|---|---|---|
| `BVA-I7` *User & KYC Report* | Story | Ayomikun Araoye | — | 14 Sep |
| `BVA-I8` *Report Data Query* | Task | Ayomikun Araoye | `I7` | 14 Sep |
| `BVA-I9` *Report Content Display* | Task | Promise Udo | `I7` | 14 Sep |

The three timestamps are 4 ms apart. That is how a parent close cascades to its children in Zoho (seen before on 1002, 30 Oct). So `I9` reads as moved by its story's close, not by its owner. There is no comment on any of the three. The board now holds 12 items, 8 leaves and 4 parents, **all Done**. Every Done on the admin board (8 Sep, 10 Sep twice, 18 Nov) has been a story close by the same person, carrying its children, and none of the 12 items ever entered REVIEW/QA. Zoho still lists no sprint after `0901-admin` for this project.

### 1.2 Sprints 1002, 0902, 0901 and 08-01

**1002: 63 items, 44 leaves + 19 parents, unchanged. No action in the window.** The 1002 sidecar is byte-identical to 18 Nov, and so is the CSV apart from its date line. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–19 Nov (to 15:02) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

The 08-01 sidecar is byte-identical to 18 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported, because they are closed. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

### 1.3 Fourteen days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902 was swept six days after its end; 1002 is eight days beyond that, with no sweep and no successor. A sweep would mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

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

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 28.2 d and 16.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-19`), it reported 166/166 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). No spec file was edited. The in-repo audit still reports the same phantom lines from the three `diverged` working trees (2 / 37 / 42). They were not acted on.

| Repo | `origin/main` | What |
|---|---|---|
| `beevia-api` | `a5cf9b5` | Unchanged. `feat/message-edit` and `feat/voice-notes` still on the remote, 0 commits ahead of `main` |
| `beevia-admin-api` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50. `feat/support-inbox` still on the remote |
| `beevia-db-schema` | `bcc45fb` (v0.0.55) | Unchanged |
| `beevia-admin` | `64304ef` (30 Oct) | Unchanged. No branch besides `main`, no pull ref |
| `beevia-mobile` | `e40116d` | Unchanged. `feat-forget-pin-fixes` at `d55630e`, no PR. The eight Dependabot branches and `App-bundle` unchanged |

**No commit on any ref in any repository in the window**, by a person or by a bot.

### 3.1 The code behind the admin-board close

Checked because a parent close has marked children Done without code before (`I381`, 30 Oct). This one has code.

| `I7` acceptance criterion | Code on `origin/main` |
|---|---|
| Total new signups in the period | `beevia-admin-api` `src/reports/report-catalog.ts`, report `user_signups`: `totals: { signups }` |
| Counts by verification status (verified / pending / failed) | Same report, breakdown `By verification outcome`, computed with the Users list's own rule. Added by `5654c7e`, 10 Sep |
| Breakdown by account type (Chat Only vs Chat + Banking) | Same report, breakdown `By account type` |
| Uses the shared generation shell | The report is one entry in the shared catalogue (`89932f9`, 8 Sep) |
| Content display (`I9`) | `beevia-admin` `src/features/reports/components/report-totals.tsx` renders stat cards and breakdown cards. Last changed by `f12135b`, 14 Sep |

The board item and the code agree. The close is two months after the code, so it changes what the board shows, not what is built. Nothing was run, so whether the report returns correct counts is not established.

### 3.2 The standing checks

- **PIN lock (#110):** no `beevia-api` commit since 16 Nov. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists.
- **`beevia-api` `release.yml`:** no commit touched it. `sync` still has no `needs: test` and still runs `pnpm db:migrate` on push to `main`.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is on 0.0.55.
- **`call.ended`** is still unhandled, and Forgot PIN on `main` is still a stub. Neither file changed.
- **Dependabot:** #64–#68 unchanged since 18 Nov. The cautions in the 18 Nov edition §3.1 stand (#66 and #67 together; #68 needs a push test on a device).
- **Branch protection, PR reviews and CI results:** cannot be seen from here.

### 3.3 Document changes this cycle

**None.** The audit was clean and no route moved, so no OpenAPI file, `api-rfc.md`, `admin-api-rfc.md` or `suggestions.md` changed. Per the audit skill, on a clean day documents that are already correct are left alone.

---

## 4. Risks

- **Done on the admin board means "closed by the story's owner", never "reviewed".** None of its 12 items passed through REVIEW/QA, and a child owned by someone else is closed with its parent. On this occasion the code exists (§3.1). The same mechanism closed `I381` on 1002 without its code. *(New framing of a known pattern.)*
- **One large unreviewed branch is the only path for three user-facing fixes:** a way out of the PIN lock, offline delete, and edit. Unchanged since 17 Nov.
- **Major dependency bumps waiting on a reviewer.** #66/#67 (ML Kit) and #68 (notifications) are unchanged.
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A locked-out user has no way out on `main`.** The lock is live, and Forgot PIN on `main` is still a stub.
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **A production data migration with no test gate.** Whether 0.0.55 ran cleanly is not visible.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended fourteen days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **The admin dashboard has no open board item anywhere** and no commit for 20 days, while three admin items on 1002 have no assignee.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **The 30-day NIN clock.** The limits are still not enforced. The grace for existing users ends about 6 Dec, **17 days from now**.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** "two admin-board items In progress for 65 days". They were closed, and the code behind them exists.

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. Nothing in the window touched any of them. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 12 Nov 15:02 → 19 Nov 15:02 UTC. Commit counts are non-merge commits on all remote branches in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (1 release commit on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3). The admin closes went In progress → Done and do not enter the cycle-time measure, which runs from In progress to REVIEW/QA.

### 6.1 Ayomikun Araoye: backend + admin API

**3 commits in 7 days**: 2 in `beevia-api` (#111 on 12 Nov, #112 on 16 Nov) and 1 in `beevia-db-schema` (#36). The drop from 5 is the window moving past #110 and #35 (11 Nov), not a change of pace. **Zero submissions** into review. **One board action**: the close of `I7` on 18 Nov 15:03 UTC, which took `I8` and `I9` with it (§1.1). Ayomikun now has **no WIP on any board**. No commit since 16 Nov, 3.1 days. None of the three commits is an item on any board.

### 6.2 David Samuel: mobile

**1 commit** in 7 days, `d55630e` on `feat-forget-pin-fixes` (17 Nov 05:51 UTC); the 11 and 12 Nov commits have aged out. None in the window. **Zero submissions.** The last own submission was `I286` on 14 Oct, **36.0 days** ago. A branch with no PR cannot meaningfully be moved to review, so this reads as a board gap rather than idle time. **WIP: 2 items, both with code on `main`**: `I331` at 28.2 days and `I361` at 16.3 days. This still reads as items left in the wrong column rather than stuck work; that is for David to say.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** The last board action by Philip was on 2 Nov 15:58 UTC, **17.0 days** ago. Philip may be finished, blocked or working untracked; worth a question, not an assumption. Forwarding, starred messages, message editing and Forgot PIN exist in code with no design item on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **20.0 days** old, and `beevia-admin` has no other branch or pull ref. `BVA-I9`, Promise's only open item, was closed with its parent story by someone else; the display it describes is in `beevia-admin` since 14 Sep (§3.1). **Promise now has no open item on any board**, and the admin items on 1002 (`I348` in REVIEW/QA, `I349` and `I351` To do) are unassigned. This report does not read a quiet remote as nothing having been done; the question is what the current work is and where it is tracked.

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
| 2026-W47 (16 → 19 Nov, to 15:02 UTC) | — | — | 0 | 0 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. Yesterday's admin closes bypassed review rather than passing through it. **The bottleneck is the board and review process, not the developers.**

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 4,000-line commit and a one-line fix count the same.
- **Who moved an item is not whether it is done.** `I9` was moved by its parent's close, not by its owner.
- **Untracked work.** #110, #111, #112, #35, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits,** and a quiet week after a 47-file commit is not a slowdown.
- **Unpushed work.** A quiet remote says nothing about local work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 18 Nov | Status on 19 Nov |
|---|---|
| **1. Open a PR for `feat-forget-pin-fixes`, or split it, and review it** | ❌ **No.** Non-Dependabot pull refs still end at #58; the branch is unchanged |
| **2. Put that work, and #110–#112, #35, #36, on the board** | ❌ **No** |
| **3. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No action on 1002** |
| **4. Close 1002 deliberately** | ❌ **Not done, fourteen days late.** No successor, no sweep, filter still 08-01 |
| **5. Give the Dependabot queue an owner** | ❌ **Not visible.** All eight PRs still open |
| **6. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No `beevia-api` commit |
| **7. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No** |
| **8. Two-device chat on a build of the branch** | ❌ **Not visible** |
| **9. Decide whether the tier limits are enforced** | ❌ **No** |
| **10. Confirm migration 0055 ran cleanly in production** | ❌ **Not visible** |
| **11. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **12. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **13. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **14. Handle `call.ended` in the app** | ❌ **No** |
| **15. NIN step and support screens on the board** | ❌ **No** |
| **16. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **17. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **18. Record the consent behind each lookup** | ❌ **No** |
| **19. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **20. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **21. Bring the dashboard onto the real contract** | ❌ **No commit in 20.0 days** |
| **22. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **23. Parent status moves; assign `I348`, `I349`, `I351`, `I359`, `I390`; admin sprint** | ❌ **No.** The admin board's stale items were closed, but by another parent close; no assignment and no admin sprint |
| **24. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **25. `needs: test` on `sync`; verify jobs; admin-api onto 0.0.55** | ❌ **No** |
| **26. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No** |
| **27. Carried items** | ❌ **None moved** |

**None of the 27 moved, fully or in part.** The admin-board close is the first board action in eight days, but it was not one of the recommendations.

---

## 8. What I would do this week

1. **Open a PR for `feat-forget-pin-fixes`, or split it first, and review it (carried).** It holds three separable pieces: Forgot PIN, the app side of #112, and forwarding/starred/voice-note work. Smaller PRs would let the PIN way-out and the offline-delete fix ship without waiting for the rest. In that review, settle the 15-minute edit window (`suggestions.md` §4.20) and ask whether the in-app Paystack WebView was a decision.
2. **Put that work, and #110–#112, #35 and #36, on the board with an owner and a design item (carried).**
3. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code. Yesterday's admin close shows one person can bring a board in line with code in a minute; doing it here through review rather than by parent close is the difference that matters.
4. **Then close 1002 deliberately (carried, fourteen days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and the new items from point 2. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
5. **Give the admin dashboard current work on a board, with Promise as owner (new).** The admin board is fully Done with no next sprint. Either open one, or assign `I348`, `I349` and `I351` on 1002 to Promise. Then agree that a child owned by someone else is not closed by its parent's close.
6. **Give the Dependabot queue an owner (carried).** Merge #64 and #65 after a build. Merge #66 and #67 together, after one on-device translation run. Merge #68 after a push test on a device. Close #60, #62 and #63 or merge them with the rest.
7. **Make the PIN check reserve its attempt before comparing (carried).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
8. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
9. **Run one two-device chat on a build of the branch (carried).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
10. **Decide whether the tier limits are enforced, and what the end of the grace does (carried, 17 days left).** About 6 Dec is the date for existing users.
11. **Confirm migration 0055 ran cleanly in production (carried).**
12. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
13. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
14. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
15. **Handle `call.ended` in the app (carried).**
16. **Put the NIN step and the support screens on the board with a design and an owner (carried).**
17. **Decide the seeded card default and what a card limit is, on the record (carried).**
18. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
19. **Record the consent behind each BVN and NIN lookup (carried).**
20. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
21. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
22. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
23. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
24. **Assign `I359` and `I390` (carried; `I348`, `I349`, `I351` moved to point 5).**
25. **Retire `GET /cards/{id}/transactions` (carried).**
26. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.55 (carried).
27. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
28. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

**`0901-admin` is now fully Done: 12 of 12 items (8 leaves + 4 parents).** On 18 Nov at 15:03:34 UTC, 92 seconds after the previous edition's cut-off, Ayomikun closed the story `BVA-I7` (*User & KYC Report*) and its children `BVA-I8` (*Report Data Query*, Ayomikun's) and `BVA-I9` (*Report Content Display*, Promise's) moved to Done in the same action. They had been In progress for 65 days. The code they describe has existed since 10 Sep (`beevia-admin-api`) and 14 Sep (`beevia-admin`), §3.1.

| Status | 18 Nov | 19 Nov |
|---|---:|---:|
| Leaves In progress | 2 | **0** |
| Leaves Done | 6 | **8** |
| Parents Done | 3 of 4 | **4 of 4** |
| Days since any activity | 65.0 | **1.0** |

The sprint ended 22 Sep. **Zoho lists no successor sprint for this project**, so the admin dashboard now has no open item on its own board. Admin-dashboard work that is tracked at all sits on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 20.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-nine days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** Nothing reached `main` in any repo. The admin-board close does not move line 11: board status is never score evidence, and the report code it describes has counted since September.

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
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed. The closed report items (`I7`–`I9`) describe code already counted |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether the branch builds, runs, or edits and deletes correctly against the server.** Nothing was run.
- **Whether the signups report returns correct counts.** The code matches `I7`'s criteria on reading; it was not run.
- **Why `I7` was closed now, two months after its code,** and whether Promise agreed to `I9` closing. There is no comment.
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

1. Three sequential background exports from 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 18 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, **sidecar changed** (three closes, §1.1). A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical and CSV identical apart from its date line. Then a sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects). 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-19`: exit 0. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow19.py`, a date-shifted copy of 18 Nov's). It listed every action in the window (the three admin closes), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `fetch` of heads and `refs/pull/*` in all five repos; a `git log` of every remote ref since 18 Nov 15:00 UTC (empty). For the admin close: `I7`'s acceptance criteria against `beevia-admin-api` `src/reports/report-catalog.ts` and commit `5654c7e`, and `beevia-admin` `src/features/reports/` and its history.
6. Document update: none needed (§3.3).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch` (including the `refs/pull/*` mirror into `refs/remotes/origin/pr/*`), `git archive`, and read-only `log`/`show`/`diff`/`grep`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-19.html` and `web-report/index.html`. New board exports for 19 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 18 Nov 15:02 UTC → 19 Nov 15:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
