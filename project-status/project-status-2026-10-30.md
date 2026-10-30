# Beevia — Project Status

**As of 2026-10-30** · Sprint **1002** (21 Oct → 5 Nov, day 10 of 16): **63 items, 44 leaves: 12 To do · 13 In progress · 16 REVIEW/QA · 0 BLOCKED · 3 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-30.csv` + `beevia-activity-2026-10-30.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-30.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 29 Oct file in the same folder; the 27 Oct scratch export of **0902** and a fresh re-export of **0901** (both closed) for cycle times. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 29 Oct 14:03 UTC → 30 Oct 14:02 UTC, 1.0 day (Thu → Fri).**

---

## Quick overview

> **A still day. Sprint 1002's board recorded no action at all in the window. Its export and audit trail are byte-identical to yesterday's, and the last move was at 11:33 UTC on 29 Oct. The only code was `beevia-api` #88: ten real-Postgres tests for blocking and unblocking, merged at 16:29 UTC yesterday. They changed no route, but they showed that `openapi.yaml` described blocking wrongly in three places. That is corrected today. None of the previous edition's fourteen recommendations moved. 1002 ends on Thursday 5 Nov, four working days away, with 41 of 44 leaves not Done and no item yet accepted by a reviewer.**

| Metric | 29 Oct | 30 Oct | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 12 / 13 / 16 / 0 / 3 | **12 / 13 / 16 / 0 / 3** | **no transition**; sidecar identical |
| Board actions on 1002 in the window | 6 | **0** | first weekday of 1002 with none |
| Transitions into REVIEW/QA, last 7 days (leaves) | 16 | **10** | 6 from 22–23 Oct aged out; nothing new. 5 by the leaf's owner (Ayomikun), 5 moved by Ayomikun on David's and Philip's items |
| Owners' last submission of their *own* leaf | 28 Oct 16:22 UTC (Ayomikun, `I341`) | **unchanged** | David's last own submission is 14 Oct, **15.9 days** ago |
| Items accepted by a reviewer | 0 | **0** | |
| 1002 REVIEW/QA leaves with matching **merged** code | 4 of 16 | **4 of 16** | |
| Routes in code but not in the spec (consumer / admin) | 3 / 3 → 0 | **0 / 0** | route drift clean before any edit |
| Spec operations corrected in place (behaviour, not routes) | — | **2** | `blockUser`, `unblockUser` (§3.1) |
| API surface (consumer / admin) | 149 / 63 | **149 / 63** | |
| Proposed operations (consumer / admin) | 37 / 18 | **37 / 18** | |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #88's ten tests gate nothing |
| `beevia-mobile` days since a commit on `main` | 7.2 | **8.2** | `BVA-I353` unchanged since `a444ec9` (1.2 d), still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 0.9 / 0.9 | **0.9 / 1.9 / 1.9** | #88 is the only new commit |
| `beevia-admin` days since a commit | 36.9 | **37.9** | |
| Admin board: open sprint / days since any activity | none / 45.0 | **none / 46.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: tests are out of the rubric's scope |

**No correction to 29 Oct.** Nothing in today's data contradicts the previous edition. The one error found today was in the **spec**, not the report: `openapi.yaml` has said since it was written that a block hides the thread, and that unblocking can return `404`. Neither is true (§3.1).

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (7 To do, 4 In progress, 7 REVIEW/QA) · `I392` shared · 0901-admin: 1 In progress | **5 own** (+5 moves on teammates' items) | 0.99 d (n=20) | `I332` (**8.2 d**), `I347` (3.9 d), `I344` (2.0 d), `I381` (1.1 d) · `BVA-I8` on 0901-admin (**46.0 d**) | **21** (13 `beevia-api`, 3 `beevia-admin-api`, 5 `beevia-db-schema`) | #88: unblock tests. **`disputes` and `help_center` are still granted to no role** |
| David Samuel | mobile | **1002: 16** (3 To do, 7 In progress, 6 REVIEW/QA) · `I392` shared | 4 (**0 own**, 4 moved by Ayomikun) | 0.99 d (n=40) | 7: `I331`, `I354` (**8.2 d**), `I346`, `I383`, `I386` (3.9 d), `I343` (2.0 d), `I380` (1.1 d) | **0 on `main`** · **5 on `BVA-I353`** (6 on the branch) | No push since 29 Oct 10:18. `didnt_make_transaction` still wrong; branch still has no PR |
| Philip Chidera | design | **1002: 7** (1 To do, 1 In progress, 3 REVIEW/QA, 2 Done) · `I392` shared (Done) | 1 (0 own, 1 moved by Ayomikun) | 0.94 d (n=4) | `I379` (1.1 d) | n/a | `I392` still Done with 0 of 63 boxes ticked |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**46.0 d**) | **0** | `beevia-admin` **37.9 days** without a commit |

**The three questions for standup:** (1) **How does 1002 close on Thursday?** 16 leaves wait in review with 0 accepted, 12 have not started, and 0902 ended in a bulk sweep that marked 7 review items Done and moved 15 leaves where the export cannot follow. Who reviews before then, and what carries over? (2) **Who grants `disputes` and `help_center`?** Still not visible in any migration, two days after users could start filing disputes. (3) **Which model does `I381` build for card verification?** `I380` and `I381` have been In progress for 1.1 days, and the three-way mismatch from 29 Oct §2.3 is unresolved.

**The three things worth knowing:**

1. **The board stopped.** No status change, comment, description edit, assignment or new item on 1002 since 29 Oct 11:33 UTC: 26.5 hours, spanning a full working day. The 7-day submission count fell from 16 to 10 only because six 22–23 Oct moves aged out. This is a reading of the board, not of the work: Thursday and Friday are also when the branch work of 27–29 Oct would be tested locally, and none of that is visible here. But a sprint with four working days left and nothing reviewed needs a plan for its last week, and the board does not show one.

2. **#88 pins blocking end to end, and the spec was wrong about it.** Ten tests against real Postgres walk the lifecycle: messaging allowed, a block refusing it in both directions, only the blocker seeing the `blocked` flag, the thread staying in both inboxes, and unblocking restoring everything with no cache to wait out. Both calls are idempotent. The tests contradict `openapi.yaml` in three places: the thread is not "hidden", `DELETE /users/blocks/{id}` never returns `404`, and `POST /users/blocks` does return `404` for a missing user, which the spec omitted. All three are corrected (§3.1). The client branch's block screens (`9e489f3`, 28 Oct) already read exactly this contract. **The payments half of blocking is still open** (`suggestions.md` §4.9): a blocked user can still send a money request.

3. **Nothing from the 29 Oct list moved, and most items need a decision rather than work.** Granting two permissions, fixing one enum value, choosing a verification model, opening a PR and reopening one checklist together come to well under a day of work. They are still undone. The bottleneck is still the review and decision step, not the developers, whose last three days produced disputes end to end, the app's FAQ and dispute wiring, and today's tests.

**If you read nothing else:** a quiet board and one test PR. The things blocking 1002 are decisions, and the sprint ends on Thursday.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 was not re-exported; it has had no entry since its 21 Oct sweep. 0901 was re-exported only for cycle times (its 19 Oct scratch copy had been cleared from `/tmp`). The 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints as yesterday (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project: **no successor to 1002 exists yet.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged.

| Block | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Help & Support (`I330`–`I352`) | 15 | 2 | 7 | 6 | 0 |
| Wallet & card (`I353`–`I391`) | 28 | 10 | 6 | 10 | 2 |
| Activity checklist (`I392`) | 1 | 0 | 0 | 0 | 1 |
| **Total** | **44** | **12** | **13** | **16** | **3** |

**Movement in the window: none.** The 30 Oct export and activity sidecar are byte-identical to 29 Oct's, `Last Modified` included. Board actions per day on 1002:

| 20 Oct | 21 Oct | 22 Oct | 23 Oct | 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct (to 14:02) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 43 | 49 | 112 | 11 | 15 | 17 | 16 | 6 | **0** |

The 20–22 Oct figures are mostly item creation. Since then, the board has carried 6–17 actions per working day, and none today. `I392`'s description still shows 63 × ☐ and 0 ticked.

### 1.3 What the last week of 1002 holds

1002 ends **Thursday 5 Nov**, four working days after today. 41 of its 44 leaves are not Done: 16 in REVIEW/QA (4 with merged code, §2.1 of 29 Oct), 13 In progress, 12 To do. The only precedent is 0902. It ran past its end date for six days, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. A sweep like that would record six mobile items as delivered, although their code is on an unmerged branch, three of them with known route mismatches. It would also record the card screens as delivered while their auth model is undecided. No successor sprint exists to carry the remainder.

---

## 2. Sprint 1002: what is in review, and whether the code exists

Unchanged from 29 Oct §2.1–2.4, because neither the board nor any branch it depends on moved. In short:

- **REVIEW/QA (16):** 4 backend leaves match merged code (`I366`, `I335`, `I338`, `I341`), 3 match endpoints that already existed or show no identifiable change (`I370`, `I377`, `I358`), 6 mobile leaves have code only on `origin/BVA-I353`, and 3 are design.
- **`origin/BVA-I353`:** 6 commits, last `a444ec9` at 29 Oct 10:18 UTC, no PR. The remote-tracking reflog shows no update after yesterday's 14:01 UTC fetch. The `didnt_make_transaction` → `400` mismatch, the two statement and limits routes that do not exist, and the three card calls waiting on `I381` are all unchanged (`suggestions.md` §5.14, §5.15).
- **WIP ages** are a day older: `I331`, `I354` and `I332` at 8.2 d; `I346`, `I347`, `I348` (unassigned), `I383` and `I386` at 3.9 d; `I343` and `I344` at 2.0 d; the verification block `I379`–`I381` at 1.1 d.

**One addition: the branch's block screens match the server.** `9e489f3` (*changes to blocking users*, 28 Oct) calls `GET`/`POST /users/blocks` and `DELETE /users/blocks/{userId}`. It reads `blocked` as a boolean on the peer profile and labels the button from it. That is exactly the contract #88 pins (§3.1). No 1002 leaf tracks blocking, so this work is visible only in git.

---

## 3. Code, API surface and spec drift

**Audit: clean on routes before any edit.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-30`): 149/149 consumer, 63/63 admin, proposed 37/18, spec health clean, no `x-beevia-*`. It is clean again after today's edits. The in-repo audit still reports the phantom lines from the three `diverged` working trees (18 consumer + 29 admin "in spec, not in code"), and they were not acted on.

**One `main` moved.**

| Repo | From → to | What |
|---|---|---|
| `beevia-api` | `e2bc950` → `4c57305` | **#88** *test: cover the way back out of a block* (merged 29 Oct 16:29 UTC): `src/users/block-lifecycle.int.spec.ts`, 187 lines, 10 tests. 1 commit, `Phoenixdadhev`. No source file changed |

`beevia-admin-api` (`b8b6a13`), `beevia-db-schema` (`2fbf657`, v0.0.45), `beevia-admin` (`0b41e35`, 22 Sep) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. **No PR is open on any backend repo.** Mobile has no new branch or PR. The highest PR is still Dependabot #53, and #45, #47, #50 and #53 are still open.

### 3.1 Blocking: what #88 pins, and what the spec said instead

| Behaviour | #88 (and `users.service.ts`) | `openapi.yaml` until today |
|---|---|---|
| Messaging after a block | refused **both ways** (`403 blocked`) | "messaging is disabled" |
| The thread | **stays in both inboxes**, flagged for the blocker only | "**hidden**" (contradicting the spec's own `ConversationListItem` text) |
| Who sees `blocked: true` | the blocker only; the blocked user is not told | correct elsewhere in the spec (`ContactProfile.blocked`) |
| Block twice | `200`, one row | not stated |
| Block a missing user | **`404`** | **not listed** |
| Unblock | immediate both ways, clears flag and list | not stated |
| Unblock someone never blocked, or a missing user | **`200 {blocked:false}`**, never `404` | **`404` listed** |

`blockUser` and `unblockUser` now say all of this, and the `404` moved from unblock to block. The route-level audit cannot see this kind of drift: the routes matched all along, and only the behaviour and status codes were wrong. A spec generated from the running app (recommendation 11) would list the status codes. Only tests like #88 pin the behaviour.

**What #88 does not cover:** payments. No test or code touches `PaymentService`, so a blocked user can still `POST /payments/request` against the blocker (`suggestions.md` §4.9, updated today).

### 3.2 The standing checks

- **Pipelines:** no workflow change on any `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`", so #88 deployed on merge with its ten tests gating nothing.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. `22P02` is still unmapped. A malformed id on `DELETE /users/blocks/{userId}` is the newest documented route where that matters, because the unblock query runs against a `uuid` column. `messages.ref_id` still has no index. FAQ search still has no `en-US` fallback. No migration grants `help_center` or `disputes`.
- **Mobile `main`:** unchanged since PR #52, with no conflict markers. **`call.ended` is still unhandled** on `main` and on `BVA-I353`. The biometric step-up (`wallet_service.dart:78`) is unchanged.

### 3.3 Document changes this cycle

- **`openapi.yaml`** (149, unchanged count): `blockUser` gains a full description and a `404`; `unblockUser` gains a description, and its non-existent `404` is removed (§3.1).
- **`suggestions.md`**: §4.9 gains a 30 Oct update (#88's scope, the spec correction, payments still open).
- `api-rfc.md`, `admin-api-rfc.md` and the other three specs needed no change: no count, route or inventory moved.

---

## 4. Risks

- **1002 ends Thursday with nothing accepted and no successor sprint.** A sweep like 0902's would mark unmerged and mis-wired work as delivered (§1.3).
- **Disputes can be filed and cannot be answered.** Two days now. Every complaint about money waits with no reader except direct database access, and the PRD's 72-hour KPI is counting.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content.
- **A fraud report fails.** "I didn't make this transaction" returns `400` from the branch's dispute sheet.
- **Three verification models for card actions**, with the sheet and the endpoint both in progress.
- **Blocking does not reach payments**, now the only untested and unguarded half of blocking.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **The admin workstream:** 37.9 days without a `beevia-admin` commit and 46.0 days without admin-board activity. Two admin APIs (FAQ content, dispute queue) have no screen and no owner.
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); card spending not disputable (§4.11); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points. Blocking is PRD scope under messaging safety, and #88 adds confidence in it, not capability.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 23 Oct 14:02 → 30 Oct 14:02 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Cycle times use 0901, 0902 and 1002, and are unchanged because no item moved.

### 6.1 Ayomikun Araoye: backend + admin API

**21 commits in 7 days**: 13 in `beevia-api`, 5 in `beevia-db-schema` and 3 in `beevia-admin-api`. Today's addition is #88. Like their earlier tests, its commit names what would break: "making unblock a no-op, or letting the profile flag report either direction … fails four of them". **5 own submissions** in the window (`I366`, `I358`, `I335`, `I338`, `I341`), and 5 moves of David's and Philip's items. `I370`'s 23 Oct submission aged out. Median cycle **0.99 d (n=20)**. WIP: `I332` (8.2 d, past their median; the open-dispute count still has no route), `I347` (3.9 d), `I344` (2.0 d; listing and detail shipped, messaging not), `I381` (1.1 d, waiting on the verification decision). `BVA-I8` has been In progress on the closed admin board for 46.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct). **5 on `origin/BVA-I353`** in the window, 6 on the branch in all, the latest at 29 Oct 10:18 UTC. Nothing was pushed in the 30 Oct window. That says nothing about local work, which this report cannot see (`project-status-2026-10-28.md` corrected an earlier edition on exactly this point). **Zero own submissions**: the last was `I286` on 14 Oct, **15.9 days** ago. Their four 7-day "submissions" were moved by Ayomikun. Median cycle **0.99 d (n=40)**. WIP: **7 items**, still the most on the board, with `I331` and `I354` at 8.2 d. The branch is the larger question for Thursday's close: it holds the code for six REVIEW/QA leaves and five In progress ones (`I331`, `I354`, `I383`, `I386`, `I343`), and none of it is reviewable until it has a PR.

### 6.3 Philip Chidera: design

No board action in the window. One 7-day submission, moved by Ayomikun on 27 Oct. `I379` (verification edge states) has been In progress for 1.1 days. Its outcome feeds the verification decision in standup question 3. `I392` remains Done with no ticks. That is still a question about how the board records review, not about Philip's work. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commit in the window.** The last was `0b41e35` on 22 Sep, **37.9 days** ago. `BVA-I9` has been In progress on the closed admin board for 46.0 days. The dispute queue (`I349`) and FAQ content (`I351`) both have live APIs, no screen and no assignee. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (from Mon 26 Oct, to 14:02 UTC Fri) | — | — | **10** | 5 | 5 | 0 |

W44 is unchanged since Wednesday evening. **Acceptance is still zero.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted by someone other than its submitter since `BVA-I268` on 16 Sep. Output was steady through Wednesday, and acceptance stayed at zero throughout. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Seven WIP items for David and four for Ayomikun are not comparable loads.
- **Unpushed and untracked work.** A board with no actions and a branch with no push are not a team with no work. Testing, review and design happen off both.
- **Who moved an item is not whether it is done**, or whether it was verified.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. #88's tests were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 29 Oct | Status on 30 Oct |
|---|---|
| **1. Grant `disputes` and `help_center`** | ❌ **Not visible.** No db-schema or admin-api change |
| **2. Fix `didnt_make_transaction` → `not_my_transaction`** | ❌ **Not done.** `BVA-I353` unchanged |
| **3. Decide the card verification model** | ❌ **Not visible.** No description, comment or code on `I378`–`I381` |
| **4. Open a PR for `BVA-I353`, or split it** | ❌ **No PR** |
| **5. Make checklists mean something; reopen `I392`** | ❌ **No.** Still Done, 0 of 63 ticked |
| **6. Let card spending be disputed; store the transaction type** | ❌ **Not done** |
| **7. Notify the user when a dispute is answered** | ❌ **Not done** |
| **8. Give the admin dashboard a home** | ❌ **No** |
| **9. Make REVIEW/QA mean merged** | ❌ **No.** Nothing moved back; `I352` still To do |
| **10. Handle `call.ended` on the client** | ❌ **Not done** |
| **11. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done.** #88 shipped ungated |
| **12. Generate `openapi.yaml` from the app; stop vendoring the client spec** | ❌ **Not done.** Today's block correction is another case it would have caught |
| **13. Set `ZOHO_SPRINT_FILTER` to `1002`** | ❌ **Not done** |
| **14. Carried items** | ❌ **None moved** |

**None of fourteen moved**, on a day when the board recorded no action at all. The work that did happen (#88) was not on the list.

---

## 8. What I would do this week

1. **Plan 1002's close before Thursday (new).** Review the four REVIEW/QA leaves with merged code and accept or return them. Move the six branch-only mobile leaves back to In progress until `BVA-I353` merges. Create the successor sprint, carry the remainder into it explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER` to the new sprint.
2. **Grant `disputes` and `help_center`** to Super Admin and the support role, in a db-schema seed or migration (`suggestions.md` §4.10.1, §4.11.1). Disputes first.
3. **Fix `didnt_make_transaction` and open a PR for `BVA-I353`**, splitting it if needed: the FAQ, dispute and block half is ready, and the card half waits on item 4.
4. **Decide the card verification model** before `I380` and `I381` go further (29 Oct §2.3, `suggestions.md` §5.15).
5. **Reopen `I392`** until its boxes reflect what was verified, and agree who ticks such checklists (not the builder).
6. **Close the payments half of blocking** (`suggestions.md` §4.9). Decide whether a transfer from a blocked user is refused or accepted, then add the check to `PaymentService` and extend #88's lifecycle test to cover it.
7. **Disputes follow-ups:** let card spending be disputed, store the transaction type, notify the user on an answer, and make the admin answer conditional (§4.11).
8. **Give the admin dashboard a home.** Assign `I349` and `I351` on an admin-board sprint, or say the dashboard is paused.
9. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job. #88 shows the tests exist; nothing makes a deploy wait for them.
10. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10).
11. **Handle `call.ended` on the client.**
12. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 46.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 46 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002, as two unassigned Stories: `I349` Support Inbox (API: `beevia-admin-api` #24) and `I351` FAQ CMS (API: #23). `beevia-admin` has gone 37.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed fifty-nine days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. #88 adds tests only, and testing is explicitly outside the rubric's scope (owner, 2026-08-07), so it neither raises nor lowers line 1. No other repository's `main` moved.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | #88 is tests only; no crypto, key or socket change |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No server card change. Client card management on unmerged `BVA-I353`; auth model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No change; dispute queue and FAQ admin have no role and no screen; no `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Why the board was still.** It cannot see off-board testing, review, design or planning.
- **Whether any role was granted `disputes` or `help_center` by hand** in production, and whether any dispute has been filed.
- **Whether #88's tests pass**, or whether they run anywhere. CI results are not visible here, and nothing was executed.
- **Whether `BVA-I353`'s screens are reachable** in the built app, or what is still on the author's machine.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items on 5 Nov.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel as three background calls, starting at 14:01 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0. **0901** was re-exported (`--activity --no-descriptions`, 76 items, exit 0) because its scratch copy had been cleared. 0902 was not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-30`: exit 0, before and after this cycle's spec edit. The in-repo audit ran too, for the board section and the RFC-count check (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`q30.py`, `flow30.py`): a day-over-day diff of 1002 (no change; CSV body and sidecar byte-identical), actions per day, 7-day submissions split by actor, cycle times, WIP ages, the weekly trend, and `I392`'s checkbox count. The sprint lists for both projects came from the `__nonexistent__` dry run.
5. Content checks. `git fetch --all --prune` and `for-each-ref` on every repo, `ls-remote` of `refs/pull/*`, and the remote-tracking reflog for `BVA-I353`. In `beevia-api`: #88's commit message and full test file, `users.controller.ts` block routes, `UsersService.block`/`unblock`/`listBlocked`, and the `403 blocked` sites in messages, conversations and calls. In `beevia-mobile`: `9e489f3`'s file list and every block call on `BVA-I353`. Standing greps as in §3.2.
6. Spec and `suggestions.md` updates (§3.3).
7. This report and its web edition.
8. End-of-run recheck at 14:07 UTC. A fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 29 Oct 11:33 UTC. `ls-remote` showed every `main` and `BVA-I353` at the commits read above, and no new branch or PR on any repo.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `reflog`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-30.html`, `web-report/index.html`, `openapi.yaml`, `suggestions.md`, plus new board exports for 30 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **0902 was not re-exported**, and 0901 had to be re-exported because its scratch copy was gone. Both are closed, so neither changes the figures.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **The route-level audit cannot see behavioural drift.** Today's two spec corrections were found by reading a test, not by the audit.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 29 Oct 14:03 UTC → 30 Oct 14:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
