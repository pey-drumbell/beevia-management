# Beevia — Project Status

**As of 2026-09-24** · Sprint **0901** (3 Sep → 22 Sep) — **closed two days ago, still the working board** · Sprint **0901-admin** (3 Sep → 22 Sep) — closed, static · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-24.csv` + `beevia-activity-2026-09-24.json` (64 items, sprint 08-01 — frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-24.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**58 items**) + sidecar in `/tmp/beevia-scratch/`; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. **Window 23 Sep 15:05 UTC → 24 Sep 13:30 UTC — about 0.9 day.**

---

## Quick overview

> **The backend shipped the server half of a QA bug the same morning the board marked that bug blocked — and the board never noticed.** `beevia-api` and `beevia-admin-api` both merged `feat/transaction-names` at 12:41 UTC: every wallet-statement row now carries `name` ("Transfer to Bola Ahmed") and `counterparty_name`, localised into the caller's language on the consumer side. That is precisely `BVA-I262`, *"Recipient Name Missing From Transactions List"* — which sat in REVIEW/QA overnight, was moved to BLOCKED at 11:29, and to In progress at 13:30, 49 minutes after the fix merged. **No route changed, so the audit reports both services clean**; the contract changed underneath it, and both implemented specs needed editing by hand. Meanwhile the review queue grew again to 25, Done is flat at 6 for a sixth edition, and there is still no open sprint on either board.

**On yesterday's edition — no factual correction, but one framing needs replacing.** The 23 Sep report treated `origin/BVA-I239`'s three commits as work at risk of being *lost* to the `BVA-1239`/`BVA-I239` name collision, and recommended rescuing them. That reading is now wrong: the branch is **live, not stranded**. Its owner merged `main` into it at 16:26 UTC on 23 Sep — after PR #35 landed — and then added seven more commits that evening. It is **11 commits and 30 files ahead of `main`** today, not 3. The recommendation changes from "cherry-pick before it is lost" to "this is an active branch; decide when it merges." Related: `origin/BVA-I242`, named yesterday as the rival l10n branch, **has been deleted** — the collision hazard is half retired.

| Measure | 23 Sep | 24 Sep | Δ (0.9 day) |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 24 | **8** (2 api, 2 admin-api, 4 db-schema) | −16 |
| Board transitions, all three boards, in window | 35 entries / 14 status changes | **19 entries / 17 status changes** | +3 status |
| Items added to sprint 0901 | 12 | **0** | −12 |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | **0** |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 0 |
| **Response-contract changes needing a hand spec edit** | 0 | **2 schemas, 4 operations** | **+2** |
| Sprint 0901 leaves, total | 49 | 49 | 0 |
| Sprint 0901 leaves To do | 12 | **6** | **−6** |
| Sprint 0901 leaves In progress | 4 | **8** | **+4** |
| Sprint 0901 leaves BLOCKED | 5 | **4** | −1 |
| Sprint 0901 leaves REVIEW/QA | 22 | **25** | **+3** |
| Sprint 0901 leaves Done | 6 | 6 | **0 — sixth edition flat** |
| Review-queue median age (0901) | 7.2 d | **6.4 d** | −0.8 — dilution again (§1.3) |
| Oldest item in the queue | 14.9 d | **15.9 d** | +1.0 |
| `beevia-api` / `beevia-admin-api` days since a commit | 4.8 / 2.0 | **0.0 / 0.0** | **−4.8 / −2.0** |
| `beevia-db-schema` days since a commit | 4.8 | **0.1** | −4.7 |
| `beevia-mobile` days since a commit | 0.0 | 1.0 | +1.0 |
| `beevia-admin` days since a commit | 0.9 | 1.9 | +1.0 |
| Admin board: days since *any* activity | 9.0 | **9.9** | +0.9 |
| Ayomikun commits (7d, both identities, merged, non-merge) | 21 | **25** | rolling window |
| David commits (7d, merged to `main`) | 4 | **3** | rolling window |
| Promise commits (7d, merged) | 2 | 2 | 0 |
| `origin/BVA-I239` commits not on `main` | 3 | **11** | **+8** |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 58 · 0 / 12 · 0 / 64 | 0 / 58 · 0 / 12 · 0 / 64 | 0 |
| **Sprints open on either board** | 0 | **0** | 0 |
| MVP readiness (estimate) | ≈67% (66.72) | **≈67% (66.72)** | **0.00** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **16 on 0901 in REVIEW/QA** (15 solely his, all of them) · 3 on 0901-admin · co-owns 4 In progress/BLOCKED bugs | 10 | 1.48 d (n=6) | **0** solely-owned · 1 on 0901-admin (`BVA-I8`, 9.9 d) · co-owns 4 bugs | **25** | **Highest commit count recorded, and still nothing of his has ever been reviewed.** His queue's median age is **12.0 d** against David's 2.4 — the queue is not one queue, it is his |
| David Samuel | mobile | **30 on 0901** — 10 REVIEW/QA, 8 In progress, 4 BLOCKED, 6 To do, 2 Done | 11 | 0.96 d (n=9) | **12** (8 In progress + 4 BLOCKED) — every open WIP item on the board is his | **3** | **All 6 board actions today were his own**, second edition running. But zero mobile commits in 24 h while 12 items are open against him |
| Philip Chidera | design | 5 on 0901 — 4 Done, **1 In progress** (`BVA-I274`) | 0 | — | 1 (`BVA-I274`, 0.0 d) | — | **First non-Done item in five editions.** Yesterday's recommendation #6 was actioned within 80 minutes of the report — but only for the branding item, not the eight Figma-mismatch bugs |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, 9.9 d) | 2 | Tenth day with no admin-board movement and no `beevia-admin` commit since 22 Sep. The board exists; nobody is using it |

**The two questions for standup:** (1) **`BVA-I262`'s server half merged at 12:41 — does David know?** The item was moved to In progress at 13:30 without a comment, and the client work is the only thing left on it. (2) **Sprint 0902 — third edition asking.** Zoho still lists only `0901, 08-01, 0702, 0701` and `0901-admin`; 43 of 49 leaves are open inside a container that expired two days ago.

**The three things worth knowing:**

1. **This is the failure mode `suggestions.md` §5.4 predicted, caught in the act.** Today's merge added no route, so the inventory diff reported both services clean. It nevertheless changed the response body of four endpoints: two consumer (`GET /wallets/transactions`, `GET /wallets/{walletId}/transactions`) and two admin (`GET /admin/transactions`, `GET /admin/transactions/users/{userId}`). The consumer rows also stopped being the raw DAL row and became an explicit projection — which is a real security improvement, because `metadata` (bank codes, rail counterparty references, provider payment ids) had been travelling on the history row and is now excluded by name. Both implemented specs were corrected by hand this cycle (§3). **A generated-and-diffed spec would have caught all of it automatically; the audit structurally cannot.**

2. **The review queue is now two queues, and only one of them is stuck.** 25 items, median 6.4 days — but split by owner, David's 10 items have a median age of 2.4 days while Ayomikun's 16 have a median of **12.0 days** and an oldest of 15.9. The headline median has fallen for two editions running purely because David keeps adding fresh items to it; the backend half has not moved at all. Three items left REVIEW/QA today — the first to leave on any board in the project's history — and **none of them left by being accepted.** `BVA-I262` went to BLOCKED and then back to In progress; the queue has still never produced a single acceptance.

3. **Every open work item on the board belongs to one person.** All 8 In progress and all 4 BLOCKED leaves are David's (four co-assigned to Ayomikun, one to Philip). Ayomikun has 25 commits in seven days and zero solely-owned items that are not waiting for a reviewer; his four co-assignments are the backend work behind David's blocked bugs, and they are still not items anyone can schedule. That is yesterday's recommendation #5, unactioned.

**If you read nothing else:** the backend had its most productive day in a fortnight and fixed a live QA bug, the board recorded none of it, and the sprint it all happened in ended on Tuesday.

---

## 1. Sprint 0901 — closed 22 Sep, still the working board

**58 items: 49 leaves + 9 parent Stories.** All figures below are leaves unless stated. The sprint's dates ended 22 September; nothing succeeds it.

### 1.1 Status distribution

| Status | 23 Sep | 24 Sep | Δ |
|---|---:|---:|---:|
| REVIEW/QA | 22 | **25** | +3 |
| In progress | 4 | **8** | +4 |
| BLOCKED | 5 | **4** | −1 |
| To do | 12 | **6** | −6 |
| Done | 6 | **6** | **0** |
| **Total leaves** | **49** | **49** | 0 |

No items were added or removed today — the first edition since 18 September with no scope change. The movement is entirely internal: six items left To do, and the queue took three more.

### 1.2 Everything that moved, in order

Seventeen status changes across nine items. The two-day split is stark and worth reading as two separate events.

| When (UTC) | Item | Move | Actor |
|---|---|---|---|
| 23 Sep 15:53 | `BVA-I276` | description edited | board administration |
| 23 Sep 16:05 | `BVA-I266` | BLOCKED → REVIEW/QA | board administration |
| 23 Sep 16:23–16:24 | `BVA-I262` | In progress → REVIEW/QA → BLOCKED → REVIEW/QA | board administration |
| 23 Sep 16:24 | `BVA-I267` | In progress → REVIEW/QA | board administration |
| 23 Sep 16:24 | `BVA-I261` | In progress → REVIEW/QA | board administration |
| 23 Sep 16:24 | `BVA-I274` | To do → BLOCKED, **owner set to Philip Chidera + David Samuel** | board administration |
| 23 Sep 16:26 | `BVA-I276` | To do → In progress | board administration |
| 23 Sep 16:29 | `BVA-I278` | To do → In progress | board administration |
| 23 Sep 16:29 | `BVA-I281` | To do → REVIEW/QA → BLOCKED | board administration |
| **24 Sep 11:29** | `BVA-I262` | **REVIEW/QA → BLOCKED** | **David Samuel** |
| 24 Sep 12:24 | `BVA-I282` | To do → In progress | David Samuel |
| 24 Sep 12:56 | `BVA-I284` | To do → In progress | David Samuel |
| 24 Sep 13:30 | `BVA-I281`, `BVA-I262`, `BVA-I274` | BLOCKED → In progress (three items, same minute) | David Samuel |

**Thirteen of the nineteen entries are board administration, all inside 36 minutes on 23 September**, and they are the triage pass that yesterday's report asked for. The six entries on 24 September are all David's own, continuing the pattern that started yesterday: he is now moving his own items, which he had never done before 23 September.

**`BVA-I262` is the item to watch.** Its path today was REVIEW/QA → BLOCKED (11:29) → In progress (13:30). The backend fix for it merged at **12:41**, between those two transitions. Nobody commented on the item, so the causal link is inference from timing — but the content match is exact (§3.1).

### 1.3 The review queue — 25 items, and it is really two queues

Ages are the `actiontime` of each item's last transition into REVIEW/QA, from the activity sidecar.

| | Items | Median age | Oldest |
|---|---:|---:|---:|
| Ayomikun Araoye | 16 | **12.0 d** | 15.9 d |
| David Samuel | 10 | **2.4 d** | 9.9 d |
| **Whole queue** | **25** | **6.4 d** | **15.9 d** |

(26 rows, 25 items — `BVA-I266` is co-assigned.)

The headline median fell from 7.2 to 6.4 days for the second edition running, and both falls are **dilution, not drainage**: three fresh items entered, nothing was accepted. Ayomikun's half of the queue has a median almost exactly five times David's. The seven-item Notification block (`BVA-I246`–`BVA-I252`), submitted together on 8 September, is now **15.9 days old** and remains the oldest thing on the board.

**Three items left REVIEW/QA today — a first for this project — and none of them left by review.** `BVA-I262` was moved out by its own assignee and is now back in development. The acceptance count across all three boards, for the entire life of the project, is still zero.

### 1.4 A caveat on the three items that entered review

`BVA-I261`, `BVA-I266` and `BVA-I267` were moved into REVIEW/QA by board administration on 23 September at 16:05–16:24. **There has been no `beevia-mobile` commit since 13:58 UTC that day** (PR #35). Either their fixes were inside PR #35 — plausible, it merged 2.5 hours earlier and carried seven weeks of work — or they were moved without a merge to review. This report cannot distinguish the two, and the items carry no comment. It is the recurrence of recommendation #2 from 22 September: *only move an item to REVIEW/QA when there is a merge to review.*

### 1.5 What is open

Twelve leaves are open (8 In progress, 4 BLOCKED) and **all twelve are David's**, four co-assigned to Ayomikun and one to Philip.

| Item | Status | Age | Owners |
|---|---|---:|---|
| `BVA-I263` | In progress | 1.1 d | David |
| `BVA-I276` | In progress | 0.9 d | David |
| `BVA-I278` | In progress | 0.9 d | David |
| `BVA-I282` | In progress | 0.1 d | David |
| `BVA-I284` | In progress | 0.0 d | David |
| `BVA-I262` | In progress | 0.0 d | David, **Ayomikun** |
| `BVA-I281` | In progress | 0.0 d | David, **Ayomikun** |
| `BVA-I274` | In progress | 0.0 d | **Philip**, David |
| `BVA-I260` | BLOCKED | 1.1 d | David |
| `BVA-I275` | BLOCKED | 1.1 d | David |
| `BVA-I279` | BLOCKED | 1.1 d | David, **Ayomikun** |
| `BVA-I280` | BLOCKED | 1.1 d | David, **Ayomikun** |

Nothing here is older than David's median cycle time of 0.96 days by more than a day, so nothing is yet "stuck" by the usual test. The four BLOCKED items have all been blocked for 1.1 days, and three of them (`I279`, `I280`, plus `I266` now in review) are blocked on backend work that exists only as a co-assignment.

---

## 2. Admin dashboard board — `0901-admin`

**12 items: 8 leaves + 4 parent Stories. Unchanged in every respect.**

| Status | Leaves |
|---|---:|
| Done | 6 |
| In progress | 2 |

| Item | Status | Owner |
|---|---|---|
| `BVA-I5` · `BVA-I11` | Done | Ayomikun Araoye |
| `BVA-I6` · `BVA-I12` · `BVA-I15` | Done | Promise Udo |
| `BVA-I14` | Done | Unassigned |
| `BVA-I8` — Report Data Query | **In progress, 9.9 d** | Ayomikun Araoye |
| `BVA-I9` — Report Content Display | **In progress, 9.9 d** | Promise Udo |

**Last activity of any kind: 14 September 14:53 UTC — 9.9 days ago.** The board that was created to make this workstream visible has now been static for longer than it was ever active, and `beevia-admin` itself has no commit since 22 September. The blind spot this pipeline reported for eleven editions is no longer structural — the board exists, it has items, and Promise has a row — it is simply unused. Sprint 0901-admin closed 22 September with no successor, like the main board.

Its counts are never added to the main sprint's.

---

## 3. API surface and spec drift

**Audit: clean, exit 0.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18. Run against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow`, because three working trees are still `diverged`.

**And that clean result is the finding.** Today's merge changed four operations' response bodies without touching a single route.

### 3.1 `feat/transaction-names` — what actually changed

Merged 12:41 UTC into both services (`beevia-api` `98d3eea`, `beevia-admin-api` `431277b`), with the supporting ledger metadata in `beevia-db-schema` (`41b31c2`, released as v0.0.36).

Every statement row in both APIs now carries two new fields:

- **`name`** — the title to show the row under: `Transfer to Bola Ahmed`, `Withdrawal to …`, `Card top-up`, `Payment held`. Seventeen title forms across nine transaction types.
- **`counterparty_name`** — that party alone, or `null` when there is nobody to name (a self-funded top-up, a fee, or a peer whose account has been deleted).

Three details that matter for anyone integrating:

1. **The title is relative to the wallet being read.** One peer transfer is `Transfer to Bola Ahmed` on the sender's statement and `Transfer from …` on the recipient's. The two legs of one transaction are deliberately not the same string.
2. **The consumer API localises it; the admin API does not.** `beevia-api` renders through a new message catalogue (`src/i18n/locales/{en,es,fr,zh}.ts`) in the caller's locale — the user's saved translation language, else `Accept-Language`, resolved by a new `@CurrentLocale()` parameter decorator. `beevia-admin-api` deliberately mirrors the logic in plain English, because a staff console has no locale to render into. The two `transaction-name.ts` files are an intentional duplicate, and the code says so: *"If a transaction type is added, both copies want updating."*
3. **The consumer rows stopped being the raw DAL row.** They are now an explicit field projection. This is the substantive part: `metadata` — bank codes, the rail's own counterparty references, provider payment ids — had been riding along on the history row and is now excluded by name rather than by luck.

**This is `BVA-I262`.** The bug reads *"the transaction list screen should display the recipient's name for each transaction. Actual: the recipient name is not currently shown."* Ayomikun was added as its owner on 22 September; the server side of it merged today. The client side has not been written.

### 3.2 Spec files updated this cycle

| File | Change |
|---|---|
| `openapi.yaml` | `LedgerEntry` rewritten to the explicit projection — added `type`, `status`, `reference`, `description`, `name`, `counterparty_name`, with a `required` list and a note that `metadata` is deliberately not published. `AcceptLanguageHeader` added to both transaction operations; both descriptions rewritten. |
| `openapi.admin.yaml` | `AdminTransactionRow` gains `name` and `counterparty_name` (plain English, no locale); both transaction operation descriptions rewritten. `GlobalTransactionRow` inherits via its existing `allOf`. |
| `suggestions.md` | **§1.4 marked resolved** (below). §7.7 updated with today's CI consolidation. |

No route was added, moved or deleted; the proposed files are untouched; no `x-beevia-*` marker was introduced. The audit re-run clean after the edits.

### 3.3 A fifty-day-old finding closed itself

`suggestions.md` §1.4 — *"Postman pagination examples are stale"* — is **resolved**. The same commit that added row titles also fixed both saved examples to the real `PaginationMeta` shape (`current_page`, `total_pages`, `has_next_page`, `has_prev_page`) and widened the all-transactions example from one row to five, one per title form. A note in `openapi.yaml`'s `TransactionPageOk` that pointed at the stale examples has been corrected — it had become the wrong claim as of this morning.

Worth being precise about why it closed: not because anyone worked the backlog, but because the same commit had another reason to open the file. That is §5.3's hand-maintenance policy working, and also the reason it took fifty days.

### 3.4 CI consolidation in two of three backend repos

`beevia-api` and `beevia-admin-api` replaced `secrets-scan.yml`, `semgrep.yml` and `supply-chain-guard.yml` with one `code-scan.yml` that calls the org's shared workflow with `secrets: inherit`. Detection now lives in `Drumbell-Technologies/.github`, so a rule change reaches every caller on its next run, and the secrets scan went from weekly to daily. Real improvement.

Two qualifications: `beevia-db-schema` still carries the three standalone copies, so it is now the odd repo out; and **neither front-end repo gained anything** — `beevia-mobile` still has no security scanning and `beevia-admin` still has no `.github` directory at all. The consolidation does make yesterday's recommendation cheaper: one four-line file each, instead of three.

---

## 4. PRD gap

No change. The four MVP gaps — international KYC tier, multi-currency/FX settlement, virtual cards beyond listing, and consent management — are where they were.

`PaymentService.activeNgn()` is re-verified present at `payment.service.ts:506`, called from lines 70, 128 and 288. While it exists, FX has not started, whatever else ships. `StubTranslateAdapter` is still bound at `translate.module.ts:23`.

One observation on today's work: the i18n catalogue that landed (`en`, `es`, `fr`, `zh`) is **response localisation, not message translation**. It renders the API's own copy in the user's language. It is genuinely useful plumbing — and it is the first time the user's saved translation language has driven anything server-side — but it does not advance capability #3, which is about translating users' messages to each other. That remains on-device on the client, with the server adapter still a stub.

---

## 5. Team performance — detail

All flow figures are from the activity sidecars (`actiontime` of the relevant transition), never from `Last Modified`. Commit counts are non-merge commits on `origin/main` in the last 7 days, summing each person's git identities.

### 5.1 Ayomikun Araoye — backend + admin API

**25 commits in 7 days** (`beevia-api` 10 across both identities, `beevia-admin-api` 8, `beevia-db-schema` 7) — the highest count this report has recorded for anyone, and up from 21 yesterday. Today alone he shipped the transaction-naming feature across three repositories, including a database migration, a mirrored labelling module in two services, and 431 lines of new test code.

**Sixteen of his items are in REVIEW/QA; fifteen of those are solely his; that is every solely-owned item he has.** Their median age is 12.0 days and the oldest is 15.9. He has zero solely-owned items in progress on the main board, and one on the admin board (`BVA-I8`, In progress for 9.9 days).

His median cycle time, In progress → REVIEW/QA, is 1.48 days (n=6). His four co-assignments (`BVA-I262`, `BVA-I279`, `BVA-I280`, `BVA-I281`) are the backend halves of David's blocked bugs and are not separately schedulable.

**This is a process finding, not a personal one**: a developer who submits at this rate into a queue with no reviewer will accumulate exactly this profile, and nothing he can do changes it.

### 5.2 David Samuel — mobile

**11 submissions to REVIEW/QA in 7 days, median cycle 0.96 days (n=9)** — the fastest on the board, though his sample includes several items that went To do → In progress → REVIEW/QA inside one triage session, which compresses the figure.

**All six board actions in the window were his own**, the second edition running in which he self-moves. **He now holds every open item on the board**: 8 In progress, 4 BLOCKED. Against that, **zero mobile commits in the last 24 hours** and 3 in 7 days. The gap is explainable — the twelve items opened against him are one to two days old and the seven-week merge landed yesterday — but it is the thing to watch tomorrow: twelve open items and a quiet repo is the shape that precedes a stall.

### 5.3 Philip Chidera — design

**First non-Done item in five editions.** `BVA-I274` (App Logo and Branding) was assigned to him and David at 16:24 UTC on 23 September — 80 minutes after yesterday's report asked for exactly that — and is now In progress.

That resolves the narrow half of the request. The broader half is untouched: the eight "doesn't match Figma"-class bugs from the two QA batches are all still David's alone, including `BVA-I284` (search icon larger than spec), which he picked up himself today. Design-shaped work is still being done by the mobile developer.

### 5.4 Promise Udo — admin dashboard

2 commits in 7 days, both on 22 September (the wallets summary/detail integration, 939 lines with tests). No commit since. Four items on the admin board, one In progress for 9.9 days, and **no board action by him anywhere, ever** — every transition on the admin board was made by someone else.

The reporting gap is closed: the board exists, he has a row, and his work is visible in `beevia-admin`. What remains is that nobody moves items on it, so the board's 9.9-day silence carries no information about whether the work is progressing.

### 5.5 Weekly submission trend (sprint 0901, transitions into REVIEW/QA)

| ISO week | Submissions |
|---|---:|
| 2026-W37 | 8 |
| 2026-W38 | 11 |
| 2026-W39 (partial) | 10 |

Steady-to-rising input. **Acceptances over the same three weeks: zero.** When submission is steady and acceptance is zero, the bottleneck is not the developers — it is that no reviewing role is staffed, and this report has now said so in eight consecutive editions.

### 5.6 What this does not measure

- **No estimation points on any of 58 items** (nor on 12, nor on 64). There is no workload normalisation, so item counts say nothing about who is carrying more. Fifteenth edition.
- **Commit counts reward small commits; cycle times reward small items.** Neither measures difficulty or quality, and today's comparison — 25 backend commits against 3 mobile ones — is not a statement about relative output.
- **Co-assignment is counted for both owners**, so per-person board counts sum to more than the board.
- **Nothing here measures correctness.** No build, test or lint was run by this pipeline in any repository.

---

## 6. Previous recommendations — where they stand

| Recommendation from 23 Sep | Status on 24 Sep |
|---|---|
| **1. Open sprint 0902 on both boards today, and decide the queue as you do it** | ❌ **Not done.** Zoho still lists only `0901, 08-01, 0702, 0701` and `0901-admin`. Third edition with zero open sprints |
| **2. Merge or cherry-pick `origin/BVA-I239`'s three commits; delete `BVA-I239`/`BVA-I242`** | 🟡 **Overtaken by events — and the premise was wrong.** `BVA-I242` **is deleted** ✅. `BVA-I239` was not stranded: its owner merged `main` into it and added 7 more commits, so it is now 11 ahead. It needs a merge *decision*, not a rescue (§7.2) |
| **3. Review something — 22 items, none ever accepted** | ❌ **Not done.** The queue is 25. Three items left it today, none by acceptance; `BVA-I262` was sent back to development by its own assignee |
| **4. Write down the translation decision; `BVA-I282` is a caching decision in the same note** | 🟡 **Half-started, by accident.** No decision record exists and `StubTranslateAdapter` is still bound. But `BVA-I282` (re-translates on every open) was picked up today and is In progress — the caching half is being coded before the decision is written |
| **5. Give `BVA-I266`/`I279`/`I280` their own items and an owner** | ❌ **Not done.** `I266` moved to REVIEW/QA, `I279`/`I280` are still BLOCKED, all three still co-assignments rather than schedulable backend items |
| **6. Pull Philip onto the eight Figma bugs and `BVA-I274`** | 🟡 **`BVA-I274` done within 80 minutes** ✅ — his first non-Done item in five editions. The eight Figma-mismatch bugs are still David's alone ❌ |
| **7. Put Promise's two commits on the admin board** | ❌ **Not done.** The board is now 9.9 days static |
| **8. Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`; close the nine Dependabot branches** | ❌ **Not done for the front ends** — but the two backend APIs consolidated to `code-scan.yml` today (§3.4), which makes the copy cheaper. The nine mobile Dependabot branches are still open; the owner's `BVA-I239` work addresses the same dependencies on a branch instead |
| **9. Confirm branch protection / secret scanning / Dependabot in the GitHub UI** | ❌ Not done, still unobservable from here. Sixth edition |
| **10. Estimation points on sprint 0902 as it is created** | ❌ Not done — there is still no sprint 0902 |
| **11. Carried: `openapi-schema.spec.ts` diffing the committed spec; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`** | ❌ **None done.** `docs/` is still absent from `origin/main`; `beevia-admin-api/src/reports/` has no commit since 21 Sep; no schema-diff test exists. **Item 1 escalates sharply** — today is the clearest demonstration yet that it is needed (§3.1) |

**One of eleven resolved outright, two partially.** The resolved one (`BVA-I242` deleted) and both partials (`BVA-I274` assigned, `BVA-I282` picked up) all happened within 100 minutes of yesterday's report, during the same triage pass — after which the board went quiet for 19 hours.

---

## 7. What I would do this week

1. **Tell David that `BVA-I262`'s server half is on `main`.** It merged at 12:41 today; he moved the item to In progress at 13:30 with no comment. If that was coincidence rather than a response, he is about to write a client fix against an API he does not know changed. One comment on the item closes it. The same applies to anyone building the transaction list: `name` and `counterparty_name` are there now, localised, and the client should render `name` rather than composing its own string.
2. **Decide `origin/BVA-I239` — it is live work, not lost work.** Eleven commits and 30 files ahead: the outstanding Dependabot updates applied wholesale, the Gradle-9/AGP fallout fixed over six commits, the wallet-test repairs, and mock-server wallet routes. This is the same dependency debt as recommendation #8's nine Dependabot branches, already solved on a branch. Merge it or say why not — but it should not spend another week diverging from a `main` that is now moving again.
3. **Open sprint 0902 on both boards.** Third edition. 43 of 49 leaves are open inside an expired container, and the admin board has been static for ten days. Nothing else on this list can be scheduled until there is somewhere to schedule it.
4. **Review Ayomikun's sixteen.** His half of the queue has a median age of 12.0 days against David's 2.4; the seven-item Notification block is 15.9 days old and was submitted in one sitting on 8 September. The project has never accepted an item. Until one is accepted, "REVIEW/QA" is a synonym for "finished and abandoned", and the falling headline median is actively misleading — it falls because David adds fresh items, not because anything drains.
5. **Generate the OpenAPI document in CI and diff it against the committed file.** This is `suggestions.md` §5.4 and it stops being a tidiness argument today: a merge changed four response bodies and the audit called both services clean. `beevia-api` and `beevia-admin-api` both already call `SwaggerModule.createDocument()` at boot. It is the only proposal on the list that closes the class rather than one instance of it.
6. **Give the three backend-blocked bugs their own items.** `BVA-I266`, `BVA-I279`, `BVA-I280` — unchanged from yesterday. Ayomikun has 25 commits and zero schedulable in-progress work; three of his real tasks exist only as someone else's co-assignment.
7. **Pull Philip onto the eight Figma-mismatch bugs.** `BVA-I274` proved the mechanism works and took 80 minutes. `BVA-I284` (search icon vs Figma spec) was picked up by the mobile developer today — that is design review being done by whoever is nearest.
8. **Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`, and bring `beevia-db-schema` onto it.** Now a four-line file rather than three files (§3.4). `beevia-admin` still has no CI of any kind.
9. **Estimation points on sprint 0902 as it is created.** Sixteenth edition. Twenty-two QA bugs of wildly varying size are now the bulk of the board and there is no way to size any of them.
10. **Carried, unchanged:** the `reports.service.ts` read-scoping fix (eleventh edition); the Module 4 A-then-B decision record; restoring or retiring `beevia-api/docs/`; and writing the translation decision down before `BVA-I282`'s caching work hard-codes the answer.

---

## Appendix — method and readiness rubric

### MVP readiness — ≈67% (estimate; 66.72, unchanged)

**Target 2026-09-01 (provisional) · the target date passed twenty-three days ago.** Weights frozen — **no methodology change this edition.** Scores measure build, not acceptance: the review queue has still accepted nothing.

**No score moved today, and that is a deliberate call rather than an absence of work.** Today's merge was real engineering across three repositories, but the rubric asks whether a *capability* exists, and a better title on an existing statement row does not add one. Two lines were re-examined and held:

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No change to crypto, keys or sockets |
| 2 | Voice & video calling | 8 | 0.80 | 0 | No `/calls` change; `FCM_SERVICE_ACCOUNT` still optional and blank |
| 3 | Message translation | 7 | 0.60 | **0 — held, re-examined** | The new `src/i18n/locales/{en,es,fr,zh}.ts` catalogue is **response localisation, not message translation**: it renders the API's own copy in the user's saved language. Genuine progress on the language plumbing, and the first server-side use of the saved preference — but `translate.module.ts:23` still binds `StubTranslateAdapter`, and `/translate/batch` and `/translate/languages` are still proposed-only. Users' messages are still translated on-device or not at all |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No API change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | **0 — held, re-examined** | Statement rows gained titles and a locale, which improves an existing surface rather than adding currencies. `activeNgn()` re-verified at `payment.service.ts:506`, called from 70/128/288 — the server remains single-currency, which is the clause holding this line back |
| 7 | Send / request / receive in chat | 12 | 0.95 | 0 | The held-back clause is "no REST read path for a single payment". A named counterparty on a *list* row is not that read path |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only; `activeNgn()` confirmed present |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card endpoint wired since yesterday; `reveal`, `freeze`, `fund` and the rest still have no client constant |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | `beevia-admin-api` transaction rows gained titles, but the rubric line scores **dashboard modules landed in `beevia-admin/src`** — and `beevia-admin` has no commit since 22 Sep |
| | **Weighted total** | **100** | **66.72** | **0.00** | **≈67%** |

A flat edition immediately after the largest move ever recorded is the expected shape: PR #35 released seven weeks of accumulated build in one day, and there is no comparable reservoir left on a branch — except `BVA-I239`, which is dependency and build work rather than product surface and would not move a capability line if it merged tomorrow.

### What this report cannot tell you

- **What the next sprint is called or when it starts.** Nothing is open on either project.
- **Whether `BVA-I262`'s In-progress move was a response to the merge** or coincidence. The timing fits (49 minutes) and the content matches exactly, but no comment records it.
- **Whether `BVA-I261`, `BVA-I266` and `BVA-I267` have merged code behind them** (§1.4). No mobile commit exists since PR #35; their fixes may or may not be inside it.
- **Whether any of the transaction-naming code works.** No `npm`, `node` or `flutter` command was run; nothing was built or executed. The 431 lines of new tests that came with it were not run by this pipeline.
- **Whether branch protection, secret scanning and Dependabot are on**, and on which repos — the `gh` token here gets `404` on every repo's rules endpoint. Sixth edition.
- **Whether `origin/BVA-I239` is intended to merge**, or is a private working branch. Its author is the project owner.
- **Velocity for any of the three sprints** — 0 of 58, 0 of 12, 0 of 64 items estimated.
- **Whether Philip is working untracked.** He now has one item, which is one more signal than the last four editions had.

### Method

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, exit 0) → admin board export with `--sprint 0901-admin` (12 items, exit 0) → read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/` (58 items, exit 0) → sprint-name discovery on both projects (confirming no successor sprint) → fast-forward sync (**0 repos advanced; 2 already current, 3 refused as `diverged`**; exit 0) → audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow` (clean, exit 0) → item-by-item diff of today's 0901 scratch export against the 23 Sep one → activity-sidecar sweep for the window → content reads of the merged transaction-naming, i18n and ledger-metadata paths across all three backend repos → spec edits → audit re-run (clean) → this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages are the `actiontime` of each item's last transition into `REVIEW/QA`; cycle times are `In progress` → `REVIEW/QA` pairs; WIP ages are the entry into the current status.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran; no repository was reset, rebased or cleaned; no sub-repo file was edited; the sync's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-24.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `suggestions.md`; new board exports for 24 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`. **The proposed specs and the two RFCs needed no change** — no route was added, removed or renamed, and no proposal shipped.

**Degraded inputs.**

- **No open sprint on either board.** Sprint 0901 and 0901-admin both closed 22 September with no successor. Every sprint figure describes an expired container that is still being worked in. Third edition.
- **Three repositories remain unsynced** — `beevia-api`, `beevia-admin-api`, `beevia-db-schema` still `diverged` (`ahead 1`, behind 40 / 34 / 27, up from 38 / 32 / 23 yesterday). Every backend code claim is made against `origin/main` via the shadow, never the working tree.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, zero activity, and an audit delta of "no net change" that describes nothing). All sprint-0901 figures come from the scratch export. The filter cannot be corrected until a new sprint exists.
- **The audit's own board section is therefore not usable this cycle** — it reports the frozen 08-01 sprint. Its code-vs-spec sections are the parts relied on here.
- **GitHub settings are unobservable.** Branch protection, secret scanning, push protection and Dependabot alerts are reported from the board and commit messages only.
- **Whether any CI run passed is unknowable from a clone.**
- **`Comments` bodies are unavailable** from the Zoho API (`commentCount` only). No comment was added to any item in the window.
- **The export's "no source key" warning fired on `Epic` again** and is the known 50-row sampling artefact, not an OAuth scope gap. On sprint 0901 the column resolves for 22 of 49 leaves; the blanks are genuinely unassigned, mostly QA bugs.
- **Repository integrity was not hash-swept this cycle.**

**Window.** 23 Sep 15:05 UTC → 24 Sep 13:30 UTC. All `actiontime` and board figures are UTC; `git log` was read with local timestamps converted where quoted.
