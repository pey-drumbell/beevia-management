# Beevia — Project Status

**As of 2026-09-17** · Sprint **0901** (3 Sep → 22 Sep) — **day 15** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 15** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-17.csv` + `beevia-activity-2026-09-17.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-17.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (35 items) + sidecar; all five repos at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` read via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. Window **16 Sep 14:04 UTC → 17 Sep 14:01 UTC** (~24 hours, Tue→Wed).

---

## Quick overview

> **Nothing was built. The work moved onto the board instead.** For the first time this report has recorded, **zero commits landed on any ref in any of the five repositories** in a full 24-hour window — not a merge, not a branch push, not a bot. What happened instead is the more interesting half: **five new items appeared on sprint 0901, all under a new `security` epic, and four of them are recommendations this report has been making for five consecutive editions** — branch protection, SAST on every PR, dependency scanning, secret scanning with push protection. Ayomikun picked up three of them within two hours. That is the first time a code-shaped ask from this document has become tracked work with an owner. It comes with a catch worth catching before anyone starts: **all five are scoped to "every backend repository", which excludes the two repos the recommendations were actually about** — `beevia-admin`, which still has no CI of any kind, and `beevia-mobile`, which is missing both org security workflows and is sitting on nine unmerged Dependabot pull requests, the oldest 37 days. Meanwhile the review queue did not move at all: the same eleven items, now **8.9 days median**, with five days left in the sprint.

**A correction to sixteen previous editions, including yesterday's.** Every appendix since 6 August has stated that the `Epic` column is blank because the refresh token lacks `ZohoSprints.epic.READ`, and warned readers not to read blanks as "no epic assigned". **That is false, and has been for at least ten days.** Every sprint-0901 export since 7 September has resolved the epic name on 25 of 25 items (`Language` 18, `Notification` 7), and today's carries 30 of 35 including the new `security` five. The claim survived because the export script's warning samples only the first 50 rows, and on the stale 08-01 board those happen to be blank — so the warning fired, and the report repeated it as fact instead of reading the column. Epic data is available and has been usable for grouping this whole time.

| Measure | 16 Sep | 17 Sep | Δ |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 14 | **0** | **−14** |
| Commits on *any* ref, all five repos, in window | 17 | **0** | **−17** |
| Board transitions, all three boards, in window | 4 | **6** (4 distinct + 2 artefact — §1.2) | +2 |
| **New board items created** | 0 | **5** | **+5** |
| API surface (consumer / admin) | 137 / 47 | 137 / 47 | 0 |
| Proposed operations (consumer / admin) | 38 / 19 | 38 / 19 | 0 |
| Spec drift vs `origin/main`, both services | 0 | 0 | 0 |
| Sprint 0901 leaves, total | 21 | **26** | **+5** |
| Sprint 0901 leaves To do | 3 | **4** | +1 |
| Sprint 0901 leaves In progress | 2 | **5** | **+3** |
| Sprint 0901 leaves REVIEW/QA | 11 | 11 | **0 — none in, none out** |
| Sprint 0901 leaves Done | 5 | **6** | +1 |
| Admin board leaves In progress / Done | 2 / 6 | 2 / 6 | 0 |
| Review-queue median age (0901) | 7.9 d | **8.9 d** | **+1.0** |
| Oldest open WIP (0901) | 1.9 d | **2.9 d** | +1.0 |
| `origin/BVA-I242` tip | 15 Sep 14:48 UTC | **unchanged — 2.0 d stale** | l10n half still on the branch |
| `beevia-mobile` `main` days since a commit | 0.9 | **1.9** | +1.0 |
| `beevia-admin` `main` days since a commit | 2.1 | **3.1** | +1.0 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 each | **1.1 each** | +1.0 each |
| Ayomikun commits (7d, 2 identities, merged) | 36 | **28** | −8 (window slid past 10 Sep) |
| David commits (7d, merged to `main`) | 1 | 1 | 0 |
| Promise commits (7d, merged) | 1 | 1 | 0 |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 30 · 0 / 12 | **0 / 35** · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈61% (61.40) | **≈61% (61.40)** | **0** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **15 on 0901** (was 10) · 3 on 0901-admin | 1 leaf (`BVA-I245`, self-reported) | 4.2 d (n=1 — §5.1) | **3** on 0901, all 0.9 d, all the new security items · 1 on 0901-admin, 3.0 d | **28** (was 36 — window slid) | **Picked up three of the five new security items within two hours of their creation.** Also: nine of the eleven items in review are still his, now 8.9 d, and he wrote no code in the window |
| David Samuel | mobile | 7 on 0901 — 1 To do, 2 In progress, 2 REVIEW/QA, 2 Done | 2 leaves (`BVA-I233`, `BVA-I243`), both moved **on 14 Sep by a non-contributor** | 8.1 d (n=2 — §5.1) | 2: `BVA-I229` 2.9 d, `BVA-I238` 1.1 d | **0 in window** (1 in 7d — the squash) | **No activity of any kind.** Both his WIP items are the l10n half of `BVA-I242`, and the branch tip has not moved in 2.0 days — the work is In progress on the board and static in git |
| Philip Chidera | design | 4 on 0901 — **all 4 Done** | 1 (`BVA-I268`, moved to review by a non-contributor) | — | **0** | — | **Completed `BVA-I256` himself** at 16:05 UTC — his second self-completion in two days, and **the first Trust & Safety item to move in four editions**. His board is now empty |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 — zero self-made transitions, still | — | 1 (`BVA-I9`, moved for him on 14 Sep, 3.0 d) | 1 | Sixth consecutive edition of zero self-attributed board activity. No `beevia-admin` commit for **3.1 days**, and that repo still has no `.github` directory — and is **not covered by any of the five new security items** |

**The two questions for standup:** (1) **Was "every backend repository" the intended scope of the five security items?** As written, `beevia-admin` and `beevia-mobile` are excluded from all five — and those are the two repos with the actual gaps: one has no CI whatsoever, the other has nine Dependabot PRs nobody has merged since 11 August. If the intent was project-wide, it is one word in five descriptions, changed before work starts rather than after. (2) **Five days left, eleven items in review at 8.9 days, and a day with no commits — what is the plan for 22 September?** The queue has now been asked about in four consecutive editions and has not lost a single item.

**The three things worth knowing:**

1. **A full day with zero commits, verified across every ref.** Not "zero merged to `main`" — zero anywhere: `git log --all --since` returns nothing for all five repositories. The last commit in the project is `447638c` / `186b944` at **16 Sep 10:47 UTC**, which landed inside the *previous* window. The three backend repos, which have been the reliable source of daily movement, went quiet together. This is a one-day observation and one day is not a trend; it is recorded here because the board simultaneously gained five items, and a reader looking only at the board would conclude the opposite of what the code shows.
2. **The report's own recommendations became board items — and the scope excludes the repos they were about.** `BVA-I269`–`BVA-I273` were created 16 Sep 14:16–14:21 UTC, twelve minutes after yesterday's window closed, under a `security` epic. Branch protection, Semgrep on every PR, fixing what Semgrep finds, Dependabot, and secret scanning with push protection map almost line-for-line onto recommendations carried here for five editions. **This report cannot claim it caused that** — it has no evidence beyond the timing and the wording. What it can check is the scope, and the scope says "backend": `beevia-admin` (Next.js, no CI at all) and `beevia-mobile` (Flutter, missing `secrets-scan` and `supply-chain-guard`) fall outside every one of the five. Two are also already partly satisfied in ways the descriptions do not acknowledge — Dependabot is live on `beevia-api` but not on `beevia-admin-api` or `beevia-db-schema`, and a `secrets-scan` workflow already exists in all three backend repos, which is a different control from the GitHub platform feature `BVA-I273` asks for.
3. **The eleven-item review queue is now the oldest it has ever been, and it is the only thing in the sprint that has never moved.** Median 8.9 days, the seven-item notification block unchanged since 8 Sep 16:02, five days to 22 September. Everything else in 0901 has now moved at least once — the branch merged, Philip's board emptied, three security items opened — which leaves this queue as the one part of the sprint no process has yet reached.

**If you read nothing else:** yesterday the project shipped the largest merge in six weeks; today it shipped nothing and planned instead. Planning the right things, mostly — but with a scope line that omits the two repositories the plan was written for, and with a review queue that five days from sprint close has still never lost an item to review.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

**35 items — 26 leaves, 9 parent Stories.** Up from 30/21/9 yesterday; all five new items are leaves. Day 15 of 20, **5 days remain**.

| Status | Leaves | 16 Sep | Δ |
|---|---:|---:|---:|
| To do | **4** | 3 | +1 |
| In progress | **5** | 2 | **+3** |
| REVIEW/QA | 11 | 11 | 0 |
| Done | **6** | 5 | +1 |
| BLOCKED | 0 | 0 | 0 |

| Owner | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Ayomikun Araoye | **15** | 3 | **3** | **9** | 0 |
| David Samuel | 7 | 1 | 2 | 2 | 2 |
| Philip Chidera | 4 | 0 | 0 | 0 | **4** |

Ayomikun's leaf count rises from 10 to 15 in one day, entirely from the new security scope. He now owns 58% of the sprint's leaves and 100% of its review queue bar two items.

### 1.2 Who actually moved each item

Six status entries in the window, from the activity sidecar's exact `actiontime`:

| Item | Owner | Change | When (UTC) | Moved by |
|---|---|---|---|---|
| `BVA-I269` | Ayomikun Araoye | To do → In progress | 16 Sep 16:04:30 | **Ayomikun Araoye** (self) |
| `BVA-I269` | Ayomikun Araoye | In progress → BLOCKED | 16 Sep 16:04:37 | **Ayomikun Araoye** (self) |
| `BVA-I270` | Ayomikun Araoye | To do → In progress | 16 Sep 16:04:46 | **Ayomikun Araoye** (self) |
| `BVA-I271` | Ayomikun Araoye | To do → In progress | 16 Sep 16:04:50 | **Ayomikun Araoye** (self) |
| `BVA-I269` | Ayomikun Araoye | BLOCKED → In progress | 16 Sep 16:04:55 | **Ayomikun Araoye** (self) |
| `BVA-I256` | Philip Chidera | To do → Done | 16 Sep 16:05:43 | **Philip Chidera** (self) |

**All six were made by the person who owns the item** — the second consecutive edition in which self-attribution is the norm rather than the exception, after four editions where it was neither.

**Two of the six are an artefact, not an event.** `BVA-I269` went To do → In progress → BLOCKED → In progress in **25 seconds**. Nothing was blocked; it reads as a mis-click corrected immediately. It is itemised here so that a future reader who finds `BLOCKED` in that item's history does not reconstruct an impediment that never existed — and it is why the status table shows BLOCKED at 0 despite a BLOCKED transition in the window.

### 1.3 The five new items — this report's recommendations, scoped to backend

Created 16 Sep **14:16–14:21 UTC** by a non-contributor, all assigned to Ayomikun Araoye, all tagged to a new `security` epic at 14:22, all **0 estimation points**. Yesterday's report could not see them: its window closed at 14:04, twelve minutes earlier.

| Item | Title | Status | Matches a standing recommendation? |
|---|---|---|---|
| `BVA-I269` | Enable Branch Protection on Main Branches | In progress | Yes — "branch protection … remains unverifiable", carried since 8 Sep |
| `BVA-I270` | Integrate Semgrep as an Automated Check on Every Pull Request | In progress | Yes — SAST in CI, the substance of "add both CI security controls" |
| `BVA-I271` | Check and Fix any vulnerabilities Already Found | In progress | Partly — the remediation half, newly explicit |
| `BVA-I272` | Enable Dependabot for Dependency Vulnerability Scanning | To do | Yes — supply-chain scanning |
| `BVA-I273` | Enable Secret Scanning and Push Protection | To do | Yes — the `secrets-scan` half of the same recommendation |

The descriptions are unusually good for this board: each is written as a user story with an explicit "What to Do" checklist, and `BVA-I269` correctly names requiring status checks *including the new Semgrep check* as a precondition. That is a better-specified ask than the one this report has been making.

**The scope line is the problem.** Every one of the five says *backend*:

- `BVA-I269` — "every backend repository's `main` branch, including at minimum the admin API repository and the shared database schema package repository"
- `BVA-I270` — "the CI pipeline … following the same pattern as the existing CI setup already used for the database schema repository", for "the TypeScript/Node.js/NestJS stack"
- `BVA-I271` — "each backend repository"
- `BVA-I272` — "every backend repository"
- `BVA-I273` — "every backend repository"

`beevia-admin` is a Next.js front end and `beevia-mobile` is Flutter. Neither is a backend repository on any reading, and the §3.2 finding that produced these recommendations was specifically about them. Verified at `origin/main` today:

| Repo | `.github/workflows` | `dependabot.yml` | In scope of the five items? |
|---|---|---|---|
| `beevia-api` | `pr` · `release` · `secrets-scan` · `supply-chain-guard` · `test` | **yes** | yes |
| `beevia-admin-api` | `ci` · `deploy` · `postman-sync` · `secrets-scan` · `supply-chain-guard` · `sync` | no | yes |
| `beevia-db-schema` | `ci` · `release` · `secrets-scan` · `supply-chain-guard` · `sync` | no | yes |
| `beevia-mobile` | `flutter-ci` · `main` · `pr` — **missing both org security workflows** | yes | **no** |
| `beevia-admin` | **no `.github` directory exists** | no | **no** |

Two further things the descriptions do not account for:

- **`BVA-I272` is already one-third done, in the wrong third.** `beevia-api` has a `dependabot.yml`; `beevia-admin-api` and `beevia-db-schema` do not. The other repo that has one is `beevia-mobile` — which is out of scope.
- **`beevia-mobile` is the live demonstration of what `BVA-I271` asks for, and it is excluded.** Dependabot has opened **nine branches** there that have never been merged: two from **11 August** (37 days), four from 27 August, one from 2 September, two from 16 September. Automated dependency scanning is already running in that repo and already producing output nobody acts on. An item about "vulnerabilities already noticed … actually investigated and fixed" that does not cover the one repo with a visible backlog of exactly that is missing its best example.
- **Semgrep appears nowhere**, in any repo, in any workflow — `BVA-I270` starts from zero, which matches its description.

### 1.4 The review queue — same eleven items, now 8.9 days median

Zero entered, zero left. Item for item identical to yesterday and to the day before.

| Item(s) | Owner | Entered REVIEW/QA (UTC) | Age |
|---|---|---|---:|
| `BVA-I246`–`BVA-I252` (7 items) | Ayomikun Araoye | 8 Sep 16:02–16:04 | **8.9 d** |
| `BVA-I231` | Ayomikun Araoye | 10 Sep 10:25 | 7.1 d |
| `BVA-I245` | Ayomikun Araoye | 14 Sep 14:53 | 3.0 d |
| `BVA-I233` | David Samuel | 14 Sep 16:04 | 2.9 d |
| `BVA-I243` | David Samuel | 14 Sep 16:04 | 2.9 d |

**Median 8.9 days** (was 7.9). Nine of the eleven are Ayomikun's; the seven-item notification block is the oldest thing on the board.

The forward path out of this queue has been exercised exactly once on this project — a 47-second bulk sweep at sprint close on 3 September — plus `BVA-I268` on 16 September, which was created, reviewed and closed inside 46 hours and never actually queued. Neither is evidence that these eleven will be reviewed. Five days remain.

`FCM_SERVICE_ACCOUNT` is still blank in `beevia-api/.env.example` (line 79) and still `.optional()` in `common/env.ts` (line 111), re-verified at `origin/main`. Accepting `BVA-I246` without checking the deployed value still accepts a `StubPushAdapter`.

### 1.5 WIP is five items and none of it produced code

| Item | Owner | In progress since (UTC) | Age | Code in window |
|---|---|---|---:|---|
| `BVA-I229` Translation Engine Integration | David Samuel | 14 Sep 16:05 | 2.9 d | none |
| `BVA-I238` Auto-Translation Display | David Samuel | 16 Sep 11:25 | 1.1 d | none |
| `BVA-I269` Branch Protection | Ayomikun Araoye | 16 Sep 16:04 | 0.9 d | none (largely a platform setting) |
| `BVA-I270` Semgrep in CI | Ayomikun Araoye | 16 Sep 16:04 | 0.9 d | none |
| `BVA-I271` Fix found vulnerabilities | Ayomikun Araoye | 16 Sep 16:04 | 0.9 d | none |

Two of these are legitimately GitHub-settings work that leaves no trace in a clone (`BVA-I269`, and the alerts half of `BVA-I272`/`BVA-I273`) — this report cannot observe branch protection or secret scanning being switched on, and says so in the appendix. `BVA-I270` and `BVA-I271` are not: a Semgrep workflow is a file, and fixes are commits. Neither exists yet, after one day.

### 1.6 `origin/BVA-I242` — the l10n half is now static as well as unmerged

The branch tip is still `92982c5` "translation engine", authored **15 Sep 14:48 UTC**, unchanged for **2.0 days**. No commit was pushed to it in the window.

That matters because both of David's In-progress items are precisely this work. Yesterday's edition read `BVA-I229` returning to In progress as evidence the branch was "being worked, not abandoned". One day on, the board still says In progress and git says nothing has happened. One quiet day is not abandonment; it does mean the *only* signal that the l10n half is progressing is currently a board status, which is the kind of evidence this report declines to score.

> **A correction to yesterday's edition.** It gave this commit's timestamp as "15 Sep 15:48 UTC". The author date is `2026-09-15T15:48:21+01:00` — the `+01:00` offset was read as UTC. The correct value is **14:48 UTC**, one hour earlier. It changes nothing material; it is corrected because the merge/branch timeline is a recurring subject here and the two nearby timestamps (branch tip 14:48, merge 16:07) should not be an hour apart in the record.

### 1.7 Trust & Safety — one of three moved, and it is the design third

`BVA-I256` *Mobile Sheet Update* was completed by Philip Chidera at 16 Sep 16:05:43 UTC. It is a child of `BVA-I253` *Trust & Safety*, which this report has flagged as entirely stalled for four editions.

The other two are unchanged: `BVA-I254` (David — report sheet, message count, confirmation state) and `BVA-I255` (Ayomikun — report submission, storage and actions) are both still **To do**, both **0 points**, with no code anywhere. The design is done; the build has not started, and there are five days left. The honest read is that this scope still will not ship in 0901, and that yesterday's recommendation to price or defer it applies to two items now rather than three.

### 1.8 Still no estimates — twelfth consecutive edition

**0 of 35 on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01.** Confirmed at the raw field level — every value is the literal string `0`. The five new security items arrived unpriced like everything else, so the sprint absorbed a new scope of unknown size on day 14 of 20 with no way to say what it displaces.

---

## 2. What shipped this cycle

**Nothing.** Zero commits on any ref in any of the five repositories, in the full 24-hour window.

| Repo | Commits in window | Last commit on `origin/main` | Days stale |
|---|---:|---|---:|
| `beevia-api` | 0 | `447638c` 16 Sep 10:47 UTC | 1.1 |
| `beevia-admin-api` | 0 | `00be69a` 16 Sep 10:44 UTC | 1.1 |
| `beevia-db-schema` | 0 | `186b944` 16 Sep 10:47 UTC (release bot) | 1.1 |
| `beevia-mobile` | 0 | `874697a` 15 Sep 16:07 UTC | 1.9 |
| `beevia-admin` | 0 | `f12135b` 14 Sep 11:36 UTC | **3.1** |

This was checked with `git log --all --since` after a `--prune` fetch on each repo, so it covers feature branches, Dependabot branches and the unmerged `BVA-I242` — not merely the default branch. No new branch appeared either.

The three backend repos produced 28 commits in the trailing seven days and had shipped every weekday before this one, so a single quiet Wednesday is unremarkable on its own and this section does not claim otherwise. It is reported because it coincides exactly with the board gaining five items and three WIP entries, and the divergence between those two signals is what a standup would want named.

---

## 3. Spec updates made this cycle

**None required.** The deterministic audit run against a read-only `origin/main` shadow reports:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 47  spec= 47  proposed= 19  [OK]
```

**Route-level drift: zero, both services, both directions.** All four spec files parse; no `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s. With zero commits in the window this is the expected result, and it is stated rather than assumed — the audit was run.

**No file was edited at the workspace root this cycle.** That is a first for this pipeline and it is the correct outcome: the audit skill's instruction is to say so and stop rather than rewrite documents that are already right.

### 3.1 Standing code findings, re-verified at `origin/main`

Because nothing merged, every code-shaped finding is unchanged by construction. The five load-bearing ones were re-checked directly rather than presumed:

| Finding | Location | State today |
|---|---|---|
| Report read-scoping gap | `beevia-admin-api/src/reports/reports.service.ts:133` | Unchanged — `viewableModules` still resolved once at generation, never re-applied at read |
| `POST /translate` bound to a stub | `beevia-api/src/translate/translate.module.ts:23` | Unchanged — `TRANSLATE_PORT` → `StubTranslateAdapter` |
| FX not started | `beevia-api/src/payments/payment.service.ts` | Unchanged — `activeNgn()` at line 506, called from lines 70, 128, 288 |
| Push falls back to a stub | `beevia-api/src/common/env.ts:111`, `.env.example:79` | Unchanged — `FCM_SERVICE_ACCOUNT` still `.optional()` and blank |
| `beevia-admin` has no CI | `beevia-admin/` | Unchanged — no `.github` directory exists |

### 3.2 The working-tree audit still reports 19 phantom drift lines

6 in `beevia-api`, 13 in `beevia-admin-api`, because three repositories remain `diverged` from the 8 September incident and their working trees are still 4 September code. **Tenth consecutive edition flagging it**, so that nobody "fixes" the spec by deleting operations that exist at `origin/main`. Every code claim in this report is made against the shadow.

---

## 4. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 15.** 12 items — **8 leaves, 4 parent Stories**. **Zero transitions and zero non-status activity in the window** — the sidecar records nothing at all.

| Status | Leaves | 16 Sep | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 2 | 2 | 0 |
| Done | 6 | 6 | 0 |

| Owner | Leaves | In progress | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 | 3 |
| Ayomikun Araoye | 3 | 1 | 2 |
| Unassigned | 1 | 0 | 1 |

Both In-progress items — `BVA-I8` *Report Data Query* (Ayomikun) and `BVA-I9` *Report Content Display* (Promise) — were moved there **on 14 September by Ayomikun**, and have sat unchanged for **3.0 days** with no `beevia-admin` commit behind them for **3.1 days**.

**Promise still has zero self-attributed transitions on this board, across every edition it has existed** — now six. The question of who owns his board state has been asked in three different framings and answered in none. It is compounded this edition by §1.3: the five new security items do not cover `beevia-admin`, so the repo with no CI, no board self-activity and the longest commit gap is also the one repo the new security scope leaves out.

### 4.1 Never summed with the main board

8 leaves here and 26 on sprint 0901 are different projects and different backlogs. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards and report invented movement.

---

## 5. Team performance — detail

All figures from the activity sidecars and git, never `Last Modified`. Commits are trailing-7-day (since 10 Sep 14:01 UTC), merged to the default branch except where stated, summing each person's git identities, excluding bots.

**Ayomikun Araoye — backend + admin API.** **28 commits** in the trailing 7 days across `beevia-api` (18), `beevia-admin-api` (5) and `beevia-db-schema` (5), counting `Phoenixdadhev` and `Ayomikun Araoye` together. **Zero in this window.** The drop from 36 is the window sliding past his 10 September work, not a reversal. On the board he did the opposite of nothing: he opened three of the five new security items within two hours of their creation, taking his open WIP from 0 to 3 and his sprint leaf count from 10 to 15. He also still owns **nine of the eleven items in REVIEW/QA**, including the entire seven-item notification block now 8.9 days old. That remains a queue problem rather than a throughput problem — his submissions are self-reported and land close to the code they describe — but he is now simultaneously the largest producer of unreviewed work and the owner of the newest scope on the sprint.

**David Samuel — mobile.** **No activity in the window** — no commit on any ref, no board transition. One merged commit in the trailing 7 days, the 15 September squash. His two In-progress items, `BVA-I229` (2.9 d) and `BVA-I238` (1.1 d), are both the localisation half of `BVA-I242`, and that branch's tip has not moved in 2.0 days. Neither item exceeds his measured median cycle, so neither reads as stuck on the numbers — but see §5.1 on what that median is worth.

**Philip Chidera — design.** **Completed `BVA-I256` himself** at 16:05:43 UTC — his second self-completion in two days, and the first Trust & Safety item to move since the scope appeared. **All four of his leaves on 0901 are now Done and his board is empty.** For a designer on a sprint with five days left and two unbuilt Trust & Safety items behind his completed design, an empty board is worth a question at standup rather than a tick: is there more design work queued, or is he now waiting on the build?

**Promise Udo — admin dashboard.** **1 merged commit** in the trailing 7 days, none in the window. Zero board transitions by him, again — sixth consecutive edition. `beevia-admin` has had no commit for 3.1 days, has no CI of any kind, and is excluded from the new security scope.

### 5.1 What these figures do not measure

- **The cycle-time column is close to meaningless and should be read as such.** It is computed as days from a leaf entering `In progress` to reaching `REVIEW/QA`, from the sidecar. Only **three leaves in the entire sprint** have both transitions recorded: `BVA-I233` (10.0 d) and `BVA-I243` (6.2 d) for David, `BVA-I245` (4.2 d) for Ayomikun. Every other item in review — including all seven notification items — went **To do → REVIEW/QA directly**, never passing through In progress, so it contributes no cycle time at all. A "median" over one and two observations should not be read as a measurement of anything. Yesterday's edition reported 6.2 d and 2.6 d for the same two people; today's method gives 4.2 d and 8.1 d. Rather than assert which is right, the honest statement is that this metric cannot be computed reliably on a board where most work skips a status.
- **It cannot see settings-shaped work.** `BVA-I269` and `BVA-I273` are largely GitHub platform configuration. If branch protection was enabled yesterday afternoon, nothing in this workspace would show it. Their being In progress with no commits is therefore not evidence of inactivity — unlike `BVA-I270`, where the deliverable is a file.
- **No estimation points exist on any item, on any of three boards** — 0/64, 0/35, 0/12, confirmed at the raw-field level.
- **Absence of data is not absence of work.** A day with zero commits is not a day with zero effort; review, design, configuration and reading all leave no trace in `git log`.
- **Correctness and testing remain out of scope for scoring**, per the owner's 2026-08-07 instruction.
- **Commit-identity mapping is inference.** `Phoenixdadhev` → Ayomikun and `Davidtariq96` → David are consistent and near-certain, but unconfirmed.

---

## 6. Previous recommendations — where they stand

With zero commits in the window, every code-shaped item is unchanged by construction; the five most load-bearing were re-verified directly (§3.1) rather than presumed.

| Recommendation from 16 Sep | Status on 17 Sep |
|---|---|
| **1. Decide the fate of the l10n half of `BVA-I242`** | ❌ **Not done, and now static.** Branch tip unchanged for 2.0 days; both related items are In progress with no code (§1.6) |
| **2. Do for the review queue what was done for the branch** | ❌ **Not done, and worse.** Same eleven items, median 7.9 → **8.9 d**, five days left (§1.4) |
| **3. Give `beevia-admin` a CI workflow** | ❌ **Not done — and now explicitly out of scope.** No `.github` directory; the five new security items cover backend repos only (§1.3) |
| **4. Copy `secrets-scan.yml` and `supply-chain-guard.yml` into `beevia-mobile`** | ❌ **Not done — also out of scope** of all five new items, in the repo with nine unmerged Dependabot PRs (§1.3) |
| 5. Fix the report read-scoping gap | ❌ Not done. `reports.service.ts:133` re-verified unchanged |
| 6. Settle the `email`-shaped inconsistency | ❌ Not done. No commit touched the schema |
| 7. Decide what happens to `POST /translate` | ❌ Not done. `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 8. Price or defer the Trust & Safety scope | ⚠️ **Partially moved, not priced.** `BVA-I256` Done; `BVA-I254` and `BVA-I255` still To do at 0 points (§1.7) |
| 9. Have Promise make one board transition himself | ❌ Not done. Zero admin-board activity of any kind |
| 10. Put estimation points on all three boards | ❌ Not done. Twelfth edition asking; five new items arrived unpriced |
| 11. Move the export's sprint filter to `0901` and the cut-off later | ❌ **Not done — and it cost a day again.** `ZOHO_SPRINT_FILTER` re-verified still `08-01`. The five security items were created at 14:16–14:21 UTC, **twelve minutes after yesterday's 14:04 cut-off**, so the largest board event in two weeks was invisible to the edition that closed just before it. Second consecutive edition to lose its headline to this window (§ appendix) |

**One of eleven partially resolved.** Against that, the most substantive movement this cycle was not on the list at all: four of the five new board items *are* the list, turned into work by someone else. The standing observation that "this document is not reaching whoever sequences the day" is, for the first time, questionable — though the evidence is circumstantial and the scope mismatch in §1.3 suggests the recommendations were arrived at rather than read.

---

## 7. What I would do this week

**Five days left in sprint 0901.** Reordered by remaining time.

1. **Fix the scope line on the five security items before work starts.** As written they exclude `beevia-admin` and `beevia-mobile` — the two repos the underlying finding was about, and the two with the worst posture. `beevia-admin` has no CI at all; `beevia-mobile` is missing both org security workflows and has nine unmerged Dependabot branches, the oldest from 11 August. Changing "every backend repository" to "every repository" in five descriptions costs minutes now and re-scoping after implementation costs days.
2. **Get a decision on the eleven-item review queue.** 8.9-day median, nine of them Ayomikun's notification block, five days to sprint close. Bulk sweep or item-by-item, both are decisions; the fourth consecutive edition of no decision is the only outcome with no upside.
3. **Land `BVA-I270` as a file this week.** Semgrep exists in no repo and no workflow. It is the one of the five security items whose deliverable is unambiguously a commit, which makes it the one that can be verified done — start there and the other four inherit a required status check.
4. **Merge or close `beevia-mobile`'s nine Dependabot PRs.** Two are 37 days old. This is `BVA-I271`'s stated goal — "vulnerabilities already noticed … actually investigated and fixed" — already queued up, already automated, in the repo the item does not cover.
5. **Decide the fate of the l10n half of `BVA-I242`.** Second edition asking. The branch has now been static for two days while two board items claim it is In progress; that gap should either close or be acknowledged.
6. **Price the two remaining Trust & Safety items or move them out of 0901.** The design is done and the build has not started with five days left. Deferring them now is a reasonable call; the costly version is carrying them to 22 September and deferring them then.
7. **Fix the report read-scoping gap** (`reports.service.ts:133`). Fourth edition, still a live access-control gap behind a client that consumes it.
8. **Decide what happens to `POST /translate`.** The client answered this in practice by building on-device translation; the server still binds a stub. One sentence.
9. **Put estimation points on the boards, or state that the project does not estimate.** Five items were added to a sprint on day 14 with no way to say what they displace.
10. **Move `ZOHO_SPRINT_FILTER` to `0901` and the daily cut-off to ~20:00 UTC.** Two consecutive editions have now missed their own headline by minutes — the merge by three, the security items by twelve. Eleventh edition of this workaround, and the first with a measured cost in both directions.
11. **Ask whether Philip has queued work.** His board is empty for the first time, on a sprint with unbuilt design behind it.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync (**0 repos advanced — `beevia-admin` and `beevia-mobile` already current; 3 refused as `diverged`**) → deterministic audit against the working tree → a second audit against a read-only `origin/main` shadow built with `git archive` → read-only scratch export of sprint 0901 (35 items) + sidecar → `git log --all --since` sweep of every ref across all five repositories after a pruning fetch → content checks of the five standing code findings against the shadow → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter`, `eslint` or build step ran. No repository was reset, rebased, reverted or cleaned; no sub-repo file was edited; the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed, or deployed.

**Files changed this cycle:** none at the workspace root beyond this report and the web edition. No spec, RFC or `suggestions.md` edit was warranted — the audit was clean against `origin/main` and no code changed.

**Degraded inputs.**

- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are still `diverged` from the 8 September incident (each `ahead 1`, behind 22/18/13); `sync_repos.py` correctly refuses to force a merge. Their working trees remain 4 September code, the sole cause of the working-tree audit's 19 phantom drift lines. Every code claim here is made against `origin/main` via a `git archive` shadow.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, a sprint that closed 28 August. The in-repo main export therefore reads a closed, frozen sprint — confirmed zero activity, as expected, with all 41 leaves Done. All sprint-0901 figures come from a read-only scratch export to `/tmp/beevia-scratch/`. Eleventh consecutive edition working around this.
- **The window cut-off lost the headline for the second day running.** The five security items were created 16 Sep 14:16–14:21 UTC; yesterday's window closed at 14:04. The day before, the `BVA-I242` merge landed at 16:07 against a 14:04 cut-off. Both are direct costs of recommendation 10, not hypotheticals.
- **`Comments` bodies are unavailable** from the Zoho API — `commentCount` only.
- **The window ends at 14:01 UTC**, so anything after that today is unobserved.
- **Settings-shaped work is invisible from this workspace.** Branch protection, GitHub secret scanning, push protection and Dependabot *alerts* (as distinct from a checked-in `dependabot.yml`) are platform configuration. `BVA-I269` and `BVA-I273` could be complete and nothing here would show it. Their status is reported from the board with that caveat, and neither is scored.
- **Whether any CI workflow has run or passed is unknowable here** — run history lives on GitHub, not in the clone.
- **Repository integrity was not hash-swept this cycle.** Credential rotation and workstation remediation remain unverifiable from this workspace.
- **No estimation points exist on any of the three boards**, confirmed at the raw CSV value level.
- **The activity sidecars only carry history for items currently on their board.**
- **Cycle time is not reliably computable on this board** — see §5.1. Most items skip `In progress` entirely.

**A correction retired, not a degraded input: the `Epic` column works.** Sixteen previous editions carried the line "the `Epic` column is blank — a known OAuth scope gap (`ZohoSprints.epic.READ` not granted), not 'no epic assigned'." Measured across every export on disk: sprint 0901 has resolved epic names on **25 of 25 items on every scratch export since 7 September**, and **30 of 35 today** (`Language` 18, `Notification` 7, `security` 5, 5 genuinely unassigned). Sprint 08-01 shows 6 of 64 (`Admin`), and the admin board 0 of 12 — those are real values, not failures, since resolution demonstrably works. The stale claim persisted because `zoho_export.py` warns when a column is blank across the **first 50 items**, which on the 08-01 board it is; the warning is a sampling artefact and was repeated as fact. The correct standing statement is that epic data is available, and that a blank cell now means what it says.

**Window.** 16 Sep 14:04 UTC → 17 Sep 14:01 UTC — a normal ~24-hour cadence. All `actiontime` and board figures are UTC; the local export host runs UTC−6.

**Sources.** Boards: `beevia-sprint-board-2026-09-17.csv` (64 rows, 41 leaves, sprint 08-01, unchanged) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-17.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (35 rows, 26 leaves) + activity sidecar, diffed item-by-item against the 16 September scratch export rather than read off the previous report. Code: all five repositories at `origin/main` — `beevia-admin`, `beevia-mobile` from the synced working tree; the other three from a `/tmp` `git archive` shadow. Specs: `openapi.yaml` (137), `openapi.proposed.yaml` (38), `openapi.admin.yaml` (47), `openapi.admin.proposed.yaml` (19) — all validated, zero route-level drift against `origin/main`.

**A note on who appears here.** Only people whose work is tracked have rows. The five new board items were created by a non-contributor and are reported without naming the actor.

<a id="mvp-method"></a>

### MVP readiness — ≈61% (estimate; 61.40, unchanged)

**Target 2026-09-01 (provisional) · the target date passed sixteen days ago.** The estimate does not move, and the reason is mechanical rather than judgemental: **the rubric scores merged build evidence, and nothing merged.** Every line below was re-verified against the `origin/main` shadow today rather than carried forward on trust.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | 0 | No commit touched crypto, keys or the socket layer |
| 2 | Voice & video calling | 8 | 0.8 | 0 | `FCM_SERVICE_ACCOUNT` still `.optional()` (`env.ts:111`) and blank in `.env.example:79` — push transport still falls back to a stub |
| 3 | Message translation | 7 | 0.30 | 0 | `translate.module.ts:23` still binds `TRANSLATE_PORT` to `StubTranslateAdapter`; `lib/core/language/` and `lib/l10n/` still do not exist on `main`, and the branch holding them has been static for 2.0 days |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | 0 | Unchanged |
| 5 | International KYC tier | 6 | 0.0 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.75 | 0 | Unchanged. `PaymentService.activeNgn()` re-verified at `payment.service.ts:506` with call sites at 70, 128 and 288 — every wallet is still NGN |
| 7 | Send / request / receive in chat | 12 | 0.90 | 0 | Unchanged since the 15 Sep merge. Still held back from 1.0 by the missing payments read path and the unused `POST /payments/send` and `/payments/{id}/pay` |
| 8 | Cross-currency FX | 12 | 0.0 | 0 | Proposed only. `activeNgn()` still hard-codes the currency |
| 9 | Virtual cards | 10 | 0.70 | 0 | Unchanged. The client still uses 2 of the 13 card operations the server exposes |
| 10 | Consent management | 4 | 0.0 | 0 | No endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.90 | 0 | Unchanged. No `beevia-admin` or `beevia-admin-api` commit in the window; the admin board recorded no activity at all |
| | **Weighted total** | **100** | **61.40** | **0** | **≈61%** |

Weights frozen — **no methodology change this edition.**

Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches. This edition is the cleanest illustration the rubric has produced. The board gained five items and three In-progress entries; the sprint's leaf count rose 24%; and the estimate is identical to yesterday's, to two decimal places, because none of that is code. The next movement will come from whatever merges next.

### What this report cannot tell you

- **Whether one quiet day is a pause or the start of one.** Zero commits across five repos is unprecedented in this record, and a single observation cannot distinguish a slow Wednesday from a stall. Tomorrow's edition can.
- **Whether the five security items were prompted by this report.** The timing (twelve minutes after the window closed) and the wording are suggestive; there is no evidence beyond that, and the backend-only scope argues they were arrived at independently.
- **Whether branch protection, secret scanning or push protection have already been enabled.** They are GitHub settings and leave no trace in a clone. `BVA-I269` and `BVA-I273` could be substantially done.
- **Whether the l10n half of `BVA-I242` will merge, or be rebuilt.** Still the largest single uncertainty in the estimate, and now two days static.
- **Whether the eleven items in REVIEW/QA will be reviewed individually, swept, or left.** Four editions of asking; the queue has never lost an item to review.
- **Why `beevia-admin` has gone 3.1 days without a commit**, or whether work is happening there off-repo.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 35, 0 of 12 items estimated.
