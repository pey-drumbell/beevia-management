# Beevia — Project Status

**As of 2026-09-04** · Sprint **0901** (3 Sep → 22 Sep) — **day 2** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-04.csv` + `beevia-activity-2026-09-04.json` (64 items, sprint 08-01), a read-only scratch export of sprint 0901 (25 items), and all five repos at `origin/main` plus every pushed branch.

Scope: both sprints, kept separate. **This edition reports a defect that makes several past claims wrong — see §0.1.**

---

## Quick overview

> **The board did nothing today and the code did a great deal, and they are no longer describing the same project. Sprint 0901 is on day 2 with all 17 leaves in To do, zero transitions, zero estimates. Meanwhile ten commits shipped four admin endpoints that open a whole spec module — including the reconciliation work the board recorded as *withdrawn* yesterday — plus a treasury change to how every payout is funded. None of it appears on any board. And reading those commits surfaced the most consequential defect this pipeline has found: `POST /webhooks/anchor` acknowledged every real Anchor delivery with a `200` and processed none of it, for sixty-seven days, until it was fixed yesterday.**

| | 3 Sep | 4 Sep | Δ |
|---|---:|---:|---:|
| Sprint 0901 leaves in To do | 17 | 17 | 0 |
| Sprint 0901 leaves started | 0 | **0** | 0 |
| Sprint 0901 board transitions | — | **0** | **none in 24 h** |
| Estimation points set (0901) | 0 / 25 | **0 / 25** | 0 |
| Sprint 08-01 (closed) | 41 leaves, all Done | unchanged | 0 |
| API surface (consumer / admin) | 131 / 30 | **131 / 34** | **0 / +4** |
| Admin spec modules built | 4 of 8 | **5 of 8** | **+1 (Module 5)** |
| Commits authored today | 1 | **10** | **+9** |
| MVP readiness (estimate) | ≈54% | **≈55%** | **+1** |

**Team, at a glance:**

| Person | Owns | 0901 leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---:|---:|---:|---|---:|---|
| Ayomikun Araoye | backend + admin API | 9, all To do | 4 | 3.0 d | — | **41** | Shipped 10 commits today, **none traceable to any board item** (§2.2) |
| David Samuel | mobile | 6, all To do | 3 | 2.6 d | — | **0 to `main`** | `beevia-mobile` `main` untouched **9 days**; `BVA-I192` still 12 commits unmerged with its item Done |
| Philip Chidera | design | 2, all To do | 2 | 0.9 d | — | — | No board activity since 3 Sep |
| Promise Udo | admin dashboard | **0** | — | — | — | 3 | **17th consecutive edition with no board row.** `beevia-admin` silent 4 days while its blocking endpoint shipped (§5) |

Submission and cycle-time figures are unchanged from 3 Sep because **no item on either board moved today**; they describe the closed sprint and are carried forward for continuity, not recomputed from new data.

**The two questions for standup:** (1) **Is sprint 0901 actually running?** It is day 2 of 19, nothing has been picked up, nothing is estimated, and the person with 9 of its 17 leaves spent the day on work that is not in it. If the real plan is to finish the money surface first and start 0901 later, that is defensible — but the sprint window is already burning. (2) **What else did the Anchor webhook silently drop?** Sixty-seven days of real deposit, payout, virtual-account and card events were acknowledged and discarded (§0.1). Someone needs to decide whether that needs a backfill, and reconciliation now exists to answer it.

**The three things worth knowing:**

1. **`POST /webhooks/anchor` processed nothing real for sixty-seven days.** Anchor's live webhooks arrive with `{ id, type, attributes, relationships }` at the top level; the handler read everything from `payload.data`, which only its *test probes* send. Every real delivery hit the unknown-type guard and returned `200` without doing anything — and the commit message reports the event inbox confirming it: only wrapped test probes were ever recorded. This ran from the endpoint's introduction on **2026-06-28** to the fix on **2026-09-03**, and it covers deposit crediting, payout settlement, virtual-account linking and card events. It is a silent no-op on the money path that looked healthy from the outside the entire time, and **no audit could have caught it** — the route existed and returned `200` throughout (§0.1, §4.3).
2. **Ten commits shipped today and not one is on a board.** Four new admin endpoints open Module 5 of the dashboard spec — a global transaction feed, a per-user statement, per-user ledger↔Anchor reconciliation and a pool solvency check — plus a pooled-treasury change to how every NGN payout is funded. **Two of those four are the reconciliation work whose board items were dropped from sprint 08-01 yesterday** as unfinished (§2.2). Yesterday's edition read that withdrawal as the reconciliation workstream losing its home; the code says it shipped the next morning. The board was wrong, not the work — but nothing on the board says so.
3. **Sprint 0901 has not started.** Day 2 of 19, 17 leaves, all To do, zero transitions in 24 hours, and still **0 of 25 items estimated** — yesterday's recommendation to estimate it "while it is still day one" was not taken, and day one has passed. Its foundation is unchanged too: `POST /translate` still returns its input unchanged, and there is still no board item asking anyone to connect a provider.

**If you read nothing else:** a webhook on the money path was dead for two months and is now fixed; today's real delivery — four admin endpoints and a treasury change — is invisible to every board and to yesterday's report's conclusions; and the sprint that is supposed to be running has not moved.

---

## 0.1 Corrections

### Correction 1 — to every edition that scored the Anchor webhook as working

**Claim: deposits, payouts and virtual-account linking are live via `POST /webhooks/anchor`.** Every edition since this pipeline began has treated that endpoint as functioning, because it exists, is HMAC-verified, deduplicates, and returns `200`.

It processed **no real Anchor delivery** between 2026-06-28 and 2026-09-03. Anchor sends `{ id, type, attributes, relationships }` at the top level with no `data` wrapper; the handler keyed every field off `payload.data`, so `type` was always undefined and every real event fell through `if (!type) return` and was acknowledged. Only Anchor's data-wrapped test probes — the shape the fixtures were built from — were ever recorded in the event inbox.

**This is the same reasoning error as yesterday's translation correction, on a more serious route.** In both cases the report inferred a capability from the existence of a route. The difference is that translation is still a stub while this one is now genuinely fixed, so the correction does not lower today's score — it changes what the score was ever worth. **Any claim about the ledger's deposit or payout history before 2026-09-03 should assume the webhook path contributed nothing.**

Two consequences that are not cosmetic:

- **Reconciliation over that period will surface real discrepancies**, not tooling noise. The endpoint that shipped today is the right instrument for measuring the damage, which is a fortunate accident of sequencing rather than a plan.
- **The tests could not have caught it.** The fixtures used the wrapped shape, because that is the shape the provider's documentation and test console produce. The bug lived in the gap between the documented example and the live delivery — where integration tests written from documentation cannot reach. The fix adds fixtures in both shapes.

`openapi.yaml` now documents both accepted body shapes and states the dead window on the operation; `api-rfc.md` gains §5.6.

### Correction 2 — to yesterday's reading of the dropped reconciliation items

**Claim (2026-09-03, §1.3 and §5): "Dropping the two items that would have built [reconciliation] leaves that mock with nothing scheduled behind it," and the reconciliation workstream "lost both its board items and has nothing scheduled."**

`BVA-I224` *Anchor Reconciliation View* and `BVA-I225` *Reconciliation Logic* were indeed removed from sprint 08-01 on 3 September. The engine merged at **01:29 UTC-7 on 4 September** and the aggregate solvency check at **04:12**, roughly nineteen hours after the items were withdrawn. The work was not abandoned; it was taken off the board and finished immediately.

The inference was reasonable from the board and wrong about the world, which is the recurring hazard this report has now hit from both directions in two days: yesterday a Done column that overstated delivery, today a withdrawal that understated it. **The board is not a reliable signal of build state in either direction.** Only the code is, and §2.2 is where this edition looks.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

| Status | Leaves | Share | Δ vs 3 Sep |
|---|---:|---:|---:|
| **To do** | **17** | **100%** | 0 |
| In progress | 0 | 0% | 0 |
| Review / QA | 0 | 0% | 0 |
| Done | 0 | 0% | 0 |

25 board rows = 17 leaves + 8 parent stories. Window 3 Sep → 22 Sep (19 days); **2 elapsed, 17 remaining.**

**The activity sidecar records zero events on 4 September.** The last board action of any kind on this sprint was 3 Sep at 16:16 UTC — a single edit to `BVA-I228`. Nothing was picked up, started, commented on or estimated in the intervening day.

| Owner | Leaves | All in state |
|---|---:|---|
| Ayomikun Araoye | 9 | To do |
| David Samuel | 6 | To do |
| Philip Chidera | 2 | To do |
| Promise Udo | **0** | — |

### 1.2 The two structural problems are unchanged

Both were raised yesterday and neither has moved:

- **`POST /translate` is still a stub.** `TranslateModule` binds its port unconditionally to `StubTranslateAdapter`, which returns the caller's own text. No provider adapter, no environment switch, one commit in the module's history (2026-07-10). The sprint asks the client to integrate a translation engine and display per-message auto-translations on top of it. **There is still no board item for connecting a provider**, and no statement anywhere of whether the engine is meant to be server-side or on-device.
- **Seven of the nine backend notification stories describe merged code.** Yesterday's §2.3 mapped each one to a live call site. Nothing has changed in `beevia-api`'s notifications module since, so the mapping stands: what is genuinely outstanding is the mid-window pending-transfer reminder, KYC-outcome notifications, the admin→consumer notification path (`BVA-I251`, which needs the two backends to talk for the first time), and a `type`/`kind` payload-naming reconciliation.

### 1.3 Still no estimates — and the cheap moment has passed

**0 of 25 items carry estimation points**, unchanged from sprint creation. Yesterday's recommendation was specifically to do this on day one, when 0901 was the first sprint this pipeline had seen early enough for the question to be cheap. It was not done, and two of nineteen days are now spent. With §1.2's finding that seven backend stories are already built, the sprint's real content is very likely smaller than its story count, which makes estimating it more useful rather than less.

---

## 2. What shipped this cycle

**Ten commits**, all authored by one person, across two repositories. The consumer API stays at 131 operations; **the admin API goes 30 → 34.**

### 2.1 `beevia-admin-api` — Module 5 opens

Four operations, all read-only, all gated `transactions:view` behind both guards:

| Operation | What it does |
|---|---|
| `GET /admin/transactions` | Platform-wide ledger feed, newest first, paginated, each row attributed to its user |
| `GET /admin/transactions/users/{userId}` | One user's statement across all their wallets |
| `GET /admin/reconciliation/users/{userId}` | That user's Anchor-rail ledger vs Anchor's own transactions, in three discrepancy buckets |
| `GET /admin/reconciliation/pool` | Σ every user's NGN balance vs the pooled FBO account — system solvency |

This is the first money-oversight surface the admin service has ever had, and the quality is high in a specific way worth naming: **the reconciliation engine is honest about its own limits inside the response, not only in comments.** Payouts correlate exactly on Anchor's `transfer.id`; deposits carry a `payment.id` the service does not store, so they fall back to amount + direction + a ten-minute window — and the response's `notes` says so, rather than declaring a heuristic match a match. Internal transfers, escrow, fees and Paystack top-ups are excluded up front so they cannot false-flag as missing. Money is compared in integer kobo and formatted to naira only for display.

**It also resolves a dependency this pipeline called blocking.** `admin-api-rfc.md` §5.2 and the proposed spec both said reconciliation needed "a statement or balance-report call on the partner adapter, which does not exist in either service today", and §6 sequenced Module 5 into Phase 4 partly on that basis. The admin service simply built the call on its own Anchor adapter. **The RFC's judgement was wrong in a repeatable way — it treated an absent integration as a blocker without checking how much of one was actually needed** — and §6 now records that rather than quietly re-sequencing.

Three things to watch, none a defect today:

1. **`status: not_configured` returns `solvent: false`.** That means *unknown*, not *insolvent*. A dashboard binding a red/green badge to `solvent` will show an unconfigured pool as a solvency failure.
2. **The per-user balance check will break when the treasury pool is switched on.** It compares the wallet balance against Anchor's `balance_after` in *that user's own* account — which the sweep shipped today (§2.2) empties. Once `ANCHOR_POOL_ACCOUNT_ID` is set, every fully-reconciled user's VBA reads near zero while their ledger balance does not, and `balance_matches` goes false for everyone. **The two commits landed thirty-eight minutes apart in different repositories**, which is exactly the interaction no single-repo review catches.
3. **Reconciliation is unbounded and capped.** No date range, NGN only, 500 payouts and 1000 ledger rows. On an active account those caps bind silently and older movements fall into the discrepancy buckets as false positives. Exceeding a cap produces wrong output rather than a truncation the caller can see.

### 2.2 `beevia-api` — pooled treasury, and the webhook fix

- **`feat(anchor): add bookTransfer + pool account config`** and **`feat(treasury): sweep deposits to the pool + fund payouts from it`.** NGN payouts now draw on a pooled For-Benefit-Of account rather than the paying user's own virtual account, and each credited deposit is swept from the user's VBA into the pool by an instant Anchor `BookTransfer`. The motivation is concrete: a user can withdraw money the ledger says they own even when it physically landed in another customer's VBA. **Both behaviours are guarded on `ANCHOR_POOL_ACCOUNT_ID` and are off until it is set**, so the rollout is a config change rather than a deploy. A failed sweep is deliberately non-fatal — the money is safe in the VBA and the ledger is already credited, so it alerts and defers to reconciliation, which is the right trade and makes today's aggregate endpoint load-bearing rather than decorative. **No HTTP contract changed**, which is why the audit sees none of it.
- **`fix(webhooks): process real Anchor deliveries + sync cards`** (merged late on 3 Sep, after yesterday's cut-off). §0.1 covers the envelope defect. The same commit adds card lifecycle handling: `card.created` / `terminated` / `frozen` fetch the card from Anchor and sync status, last4 and expiry. Anchor emits no distinct activation event — a card is created `PENDING` and goes `ACTIVE` silently — so pending cards are also refreshed when the card list is read, which is the catch-up that flips a freshly-issued card to active. **This is the first point at which card issuance can actually complete.**

### 2.3 None of it is on a board

Ten commits, four new endpoints, a change to how every payout is funded, and a two-month-old money-path defect fixed. **Zero board items reference any of it.** Two of the four admin endpoints correspond to items that were removed from sprint 08-01 nineteen hours before they merged (§0.1, Correction 2); the treasury work and the webhook fix have never had a board item at all.

This is not a process complaint for its own sake. It has three concrete costs, all of which this report is currently absorbing by hand:

- **The board understates delivery**, in the same week it also overstated it. Yesterday it read 100% complete on work that was not all merged; today it reads 0% moved on a day of substantial delivery.
- **Nobody is reviewing this.** All four admin endpoints went through pull requests authored and merged by the same person within hours. That is unavoidable when one person owns both backends and there is no second backend reviewer — it is a staffing fact, not a discipline failure — but it means the money-oversight surface has had no second pair of eyes, and neither did the treasury change.
- **Cross-service interactions have no owner.** §2.1's second watch item is a real interaction between two commits in two repositories on the same morning. No board item, no PR and no CI check spans both.

### 2.4 Repo staleness

| Repo | Last commit to `main` | Days silent | Δ |
|---|---|---:|---:|
| `beevia-api` | **4 Sep** | **0** | 0 |
| `beevia-admin-api` | **4 Sep** | **0** | −2 |
| `beevia-db-schema` | 1 Sep | 3 | +1 |
| `beevia-admin` | 31 Aug | **4** | +1 |
| `beevia-mobile` | 26 Aug | **9** | +1 |

Unmerged remote branches unchanged: `beevia-mobile` carries **`origin/BVA-I192` at 12 commits ahead** (last pushed 2 Sep), whose board item was marked Done yesterday, plus nine dependabot branches, `Deps-updates-2026-08-20` and `self-hosted-runners`. `beevia-api` carries `origin/victor` (1 ahead, 20 July). Unmerged work is not scored.

---

## 3. Sprint 08-01 — closed, and frozen

The closed sprint is unchanged: 64 rows = 41 leaves + 23 parent stories, all 41 leaves Done, no activity since the closing sweep of 3 September. The audit's period-over-period section confirms it — **no net status change, 0 items left review, 0 newly Done, 0 entered.**

Yesterday's analysis of how it closed stands and is not repeated here. One item from it is now answered: the two reconciliation items were dropped and then built (§0.1, Correction 2). The other two dropped items — `BVA-I171` *Correct Bank Name Display* (Philip) — remain withdrawn with no successor anywhere.

**A pipeline problem this creates.** `ZOHO_SPRINT_FILTER` in `.env` is still `08-01`, so the daily export now targets a **closed** sprint: today's run wrote 64 rows of frozen data and the audit dutifully reported "sprint ends 2026-08-28 (−7d left)". The active sprint reaches this report only through a scratch export outside the repository (§Appendix). That is deliberate for one edition — the audit globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest files as one board, so dropping an 0901 CSV in there would make tomorrow's delta compare two different sprints and report invented movement — **but it is not sustainable, and the cutover needs doing before the next report.** See §9, item 3.

---

## 4. Spec updates made this cycle

The audit opened at **131/131 consumer, 30/34 admin — four routes in code and absent from the spec** — and closed clean at 131/131 and 34/34, all four specs valid, no `x-beevia-*`, no broken refs, no orphaned components.

### 4.1 `openapi.admin.yaml` — four operations added, two proposals retired

The four new routes are documented from their controllers, DTOs, services and response types, with the wire shape rather than the handler shape: `ResponseInterceptor` wraps every payload as `data` and converts keys to snake_case recursively, so the spec carries `balance_after`, `total_pages`, `anchor_txn_id`, `in_beevia_not_anchor` and so on. New schemas: `AdminTransactionRow`, `GlobalTransactionRow`, `TransactionsPagination`, `TransactionUserRef`, `UserReconciliationReport`, `PoolReconciliationReport`, `ReconciliationSummary` and the three bucket-row types.

Two proposals shipped and have been **moved, not copied** — `openapi.admin.proposed.yaml` drops from 23 to 21, and the now-orphaned `ReconciliationReport` component went with them. Both shipped **differently from their proposal**, which is the usual case and worth recording rather than smoothing over:

| Proposed | Shipped as | Difference |
|---|---|---|
| `GET /admin/users/{id}/transactions` | `GET /admin/transactions/users/{userId}` | Different path shape; **no `direction` / `from` / `to` filters** |
| `GET /admin/reconciliation` (one op, date-ranged) | `/reconciliation/users/{userId}` + `/reconciliation/pool` (two ops) | **No period or currency parameters**; restructured into three named buckets plus a balance check |

`admin-api-rfc.md` gains §3.9 and §3.10 for the implemented contracts, and **§6.3** for the three gaps a dashboard build will hit: the missing statement filters, the unbounded-and-capped reconciliation, and a **third pagination convention** in one service (`meta`/`PaginationMeta`, then cursor on the activity feed, now `data.pagination` with `page` where `PaginationMeta` says `current_page`). Module 5's coverage row moves from ⛔ Not built (0 ops) to 🟡 Partial (4).

### 4.2 `openapi.yaml` — the webhook's two body shapes and its dead window

`POST /webhooks/anchor` now documents that it accepts both the top-level and `data`-wrapped envelopes, that card lifecycle events sync status/last4/expiry with a pending-card refresh on list read, that a `200` acknowledges receipt and never successful processing — and, in a blockquote on the operation, the sixty-seven-day window in which real deliveries were acknowledged and dropped. `api-rfc.md` gains §5.6, and §5.7 for the pooled-treasury change; the §6.8 Webhooks row is annotated.

This is description of implemented behaviour, not a status marker — the implemented specs stay free of `x-beevia-*` and safe to generate clients from.

### 4.3 The audit worked today, and still missed the two things that mattered

Today is the pipeline's good case: four routes appeared, the inventory diff caught all four, and the spec was correct within the hour. It is worth stating plainly because the same twenty-four hours contain its structural blind spot in its sharpest form yet.

**Neither the webhook no-op nor the treasury change altered a route, a parameter or a response.** The webhook went from processing nothing to processing everything with an identical contract; payouts changed which account funds them with an identical contract. Nineteen consecutive clean audits ran over an endpoint that was a silent no-op on the money path, and every one of them was correct by its own definition.

**This also bounds the fix this report has recommended six times.** Publishing both services' generated OpenAPI documents and diffing them in CI would have caught the contacts response shape, the five wrong admin facts of 2 September, and today's pagination divergence. It would **not** have caught either of today's two findings. Generation closes the *contract*-drift class; it does not close the *behaviour*-drift class, and this cycle produced one of each. `suggestions.md` §5.4 is updated to say so, and to name the cheaper second instrument: an alert on "webhook received, no handler matched" instead of a silent `200`. That is roughly five lines of code, and it would have surfaced the defect in §0.1 within a day of its introduction.

### 4.4 Still open from previous editions

`beevia-admin` still calls `GET /users/{id}/audit-trail` (`src/features/users/api.ts`) without the `/admin` prefix every other admin route carries, still through a mock adapter, still matching no operation in either admin spec. Unchanged as a decision for the two owners.

---

## 5. Admin dashboard board

The second Zoho project, *Beevia Admin Dashboard* (`187554000000127002`), **still has no sprints**; step 1b returned exit 3 again, for the **sixteenth consecutive edition**. The board contributes nothing, so Promise Udo's row remains sourced from commits.

This cycle: no commits, none since 31 August — four days. The nine feature modules, four of them explicitly `MOCK IMPLEMENTATION — no network calls` (`transactions`, `wallet`, `pending-transfers`, `reconciliation`), are unchanged, as are the seventeen `src/app` routes.

**The blocker on two of those four mocks was removed today, and the dashboard does not know.** `reconciliation` was mock-backed waiting on `GET /admin/reconciliation`; `transactions` was mock-backed waiting on a transaction feed. Both endpoints now exist (§2.1) — at paths that differ from what the mocks were written against, and with a third pagination shape (§4.1, `admin-api-rfc.md` §6.3). Yesterday this workstream's problem was that nothing was scheduled behind its mocks; today the problem is the opposite and better: **the API is ahead of the dashboard, and nobody has told the dashboard.** Communicating that costs one message; there is no board on which it would otherwise surface.

**Pipeline note, unchanged:** the two boards are never summed; admin exports would land in `sprint-board-exports/admin/` because `beevia-audit` globs the main folder non-recursively; when the admin board gets a sprint its name will not match `ZOHO_SPRINT_FILTER`, so step 1b will keep skipping until `--sprint` is passed.

---

## 6. Team performance — detail

All figures come from the activity sidecar and git, never from `Last Modified`. **No board item on either sprint moved in the last 24 hours**, so every flow metric below is carried forward from 3 September rather than recomputed; only the commit and staleness figures are new today.

**Ayomikun Araoye — backend + admin API.** **41 commits in the trailing 7 days** across `beevia-api` (21), `beevia-admin-api` (14) and `beevia-db-schema` (6), summing the `Ayomikun Araoye` and `Phoenixdadhev` identities and excluding bots — up from 29 a day ago, with **10 of them today**. He shipped the whole of §2.1 and §2.2. He also owns 9 of sprint 0901's 17 leaves, none of which he touched, and §1.2 finds seven of those nine already built. The honest reading is that he is working on what is most valuable and the board is describing something else; that is a planning problem, not a performance one, and it is the second day in a row it has cost this report an hour of reconstruction. **He is the only person who can confirm §1.2's mapping**, and it remains worth asking him directly.

**David Samuel — mobile.** Three genuine submissions in the trailing 7 days, last on 28 August; median cycle 2.6 d over 14 passes. **Zero commits to `main` in 7 days** — `beevia-mobile` `main` has now been static for **9 days** — and nothing new on `origin/BVA-I192`, which stays 12 commits ahead with its board item marked Done. He owns 6 of 0901's leaves, all untouched. Two days without a commit to any branch is not itself a signal; combined with a Done-but-unmerged branch and a sprint that has not started, it is worth a question rather than an assumption.

**Philip Chidera — design.** Two genuine submissions in 7 days; median cycle 0.9 d over 7 passes. Two leaves in 0901, both To do. His withdrawn 08-01 item (`BVA-I171`) has no successor anywhere.

**Promise Udo — admin dashboard.** No board presence, seventeenth consecutive edition. Three commits in the trailing window, all build configuration, none since 31 August. §5 is the substantive read: his workstream's two blocking endpoints shipped today, from someone else's repository, with no channel to tell him.

### 6.1 Weekly submission trend

First-ever genuine submissions into REVIEW/QA, by ISO week: **W34 (17–23 Aug) — 17 · W35 (24–30 Aug) — 10 · W36 (31 Aug onward) — 1.** No submissions have been made since sprint 08-01 closed, on either board.

The team's throughput signal is now entirely blind: the closed sprint cannot produce more transitions, and the open sprint has produced none. **For the first time this pipeline has no flow data at all** — which is itself the finding, and it is what §9's first two items address.

### 6.2 Cycle times

Unchanged from 3 September; no new passes have been measured. Method: one measurement per pass, from an item's most recent entry into `In progress` to the next time it reaches `REVIEW/QA`.

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

Every distribution is bimodal — same-day board hygiene at one end, multi-day builds at the other. The distributions are the useful part; the medians are reported because the format asks for them.

### 6.3 What these figures do not measure

- **They do not see today's work at all.** The largest delivery day in a week produced a zero in every board-derived column, because none of it was tracked. Commit counts are the only column that noticed.
- **They do not see branches.** `beevia-mobile` reads zero commits while twelve sit on `origin/BVA-I192`, whose board item is Done. Every "commits" figure means *merged to `main`*.
- **No estimation points exist on any item, in either sprint** — 0/64 and 0/25. Nothing is normalised for size.
- **Board actions are not evenly attributable.** Per-person figures key to the item's **assignee**, not to whoever clicked.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality, and today's ten commits include one two-line env addition and one two-month-old defect fix.
- **Review and triage work is invisible**, and today there was none to record: all four admin pull requests were authored and merged by the same person (§2.3).
- **Absence of board data is not absence of work** — proven twice in two days, in both directions.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction. Nothing here asserts that any shipped endpoint works.

---

## 7. Risks

1. **Sixty-seven days of real Anchor events were acknowledged and dropped** (§0.1). Fixed, but the historical impact is unquantified and nobody has decided whether a backfill is needed.
2. **The per-user reconciliation balance check will report false discrepancies for every user the moment the treasury pool is enabled** (§2.1). Two commits, two repositories, thirty-eight minutes apart, no owner for the interaction.
3. **Sprint 0901 has not started** — day 2 of 19, nothing picked up, nothing estimated (§1.1, §1.3).
4. **Sprint 0901's foundation is still a stub and still not on the board** (§1.2). `POST /translate` returns its input unchanged.
5. **Sprint 0901 is probably mis-sized** — seven of nine backend stories describe merged code, and there are no estimates to check that against.
6. **The board is not tracking the work that is actually happening** (§2.3). Ten commits, four endpoints, one treasury change, zero board items.
7. **The money-oversight surface has had no second reviewer** (§2.3) — unavoidable with one backend engineer, but it should be a known exposure rather than an unnoticed one.
8. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows (§2.1); exceeding the caps produces wrong output, not visible truncation.
9. **The admin dashboard is now behind its own API** (§5), at paths its mocks were not written against, with no channel to communicate the change.
10. **A finished mobile payout feature has been unmerged for seven days** with its board item closed (§2.4).
11. **Behaviour drift is invisible to automation** (§4.3), and the fix this report has recommended six times would not have caught either of today's findings.
12. **The daily export now targets a closed sprint** (§3); the active sprint reaches this report only via an out-of-repo scratch export.
13. **The same silent-200 is still live on `POST /kyc/profile`** — fourth consecutive edition; a five-line guard already written on the other ladder.
14. **A hard-coded account number still reaches a money screen on `main`** — fourth consecutive edition, under a Done item.
15. **Failed provisioning is still invisible to the user** — no endpoint reports the outcome of the queued job.

---

## 8. Previous recommendations — where they stand

| Recommendation from 3 Sep | Status on 4 Sep |
|---|---|
| Decide and state what "Done" means on this board | **Not done.** No sprint description, comment or note was added. The question is now sharper, since the board has been wrong in both directions in two days (§0.1). |
| Put a translation provider on the board, or say the engine is on-device | **Not done.** No new item; no statement either way (§1.2). |
| Re-scope the seven notification stories before the sprint runs | **Not done**, and the sprint is now running — or would be, if anything had been picked up (§1.1). |
| Decide `BVA-I192` — merge it or close the branch | **Not done.** Still 12 commits ahead, unchanged since 2 Sep. |
| Give the reconciliation work a home | **Done, off-board.** Both endpoints shipped this morning (§2.1), nineteen hours after the items were dropped. The recommendation is satisfied; the visibility problem it was really about is worse, not better (§2.3). |
| Publish both services' generated OpenAPI documents and diff them in CI | **Not done.** §4.3 now qualifies it: still worth doing, and it would not have caught either of today's findings. |
| Put estimation points on sprint 0901 while it is still day one | **Not done**, and day one has passed (§1.3). |
| Apply the BVN-ordering guard to `POST /kyc/profile` | **Not done.** Re-checked today; unchanged. |

One of eight resolved, and that one was resolved by work that no longer appears anywhere a reader would look.

---

## 9. What I would do this week

1. **Decide whether sprint 0901 is running.** Two of nineteen days are gone with zero movement while its owner shipped ten commits of other work. Either start it, or re-plan it around what is actually being built — the money surface is clearly the live priority and the board says nothing about it. This is one decision and it unblocks items 3, 4 and 7.
2. **Scope the Anchor webhook backfill.** Sixty-seven days of real deposit, payout, virtual-account and card events were dropped (§0.1). The reconciliation endpoint that shipped today can measure it — run `GET /admin/reconciliation/users/{userId}` across the active users and see what the buckets say. That converts an unbounded worry into a number, probably in an afternoon.
3. **Fix the per-user balance check before enabling the pool** (§2.1). `ANCHOR_POOL_ACCOUNT_ID` is currently unset, so there is time; the moment it is set, reconciliation reports a discrepancy for every user and the tool becomes untrustworthy exactly when it is first needed.
4. **Tell Promise the two endpoints he was blocked on exist** (§5), at what paths, and with which pagination shape. Four days of silence in `beevia-admin` while its blockers cleared is the most avoidable thing in this report.
5. **Move the daily export to sprint 0901** (§3). It targets a closed sprint today. The safe cutover is to move the eleven `08-01` CSVs and sidecars into `sprint-board-exports/08-01/` and let the main folder start fresh on 0901 — the audit globs non-recursively, so a subdirectory isolates them, and the first 0901 edition then reports "no previous export" honestly instead of diffing two different sprints.
6. **Add the five-line "webhook received, no handler matched" alert** (§4.3). It is the cheapest instrument that would have caught the defect in §0.1, and it generalises to the Entrust and Paystack callbacks.
7. **Put estimation points on 0901, or state that this project does not estimate.** Third consecutive edition asking. Either answer is workable; the current state — asking every day and getting silence — is not.
8. **Get a second pair of eyes on the money-oversight code** (§2.3). One person authored and merged all four endpoints and the treasury change on the same morning. With one backend engineer that cannot be a review requirement, but it can be a scheduled read-through by someone else before this reaches real staff.
9. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Unchanged from the last four editions; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:00 UTC) → admin board (exit 3, no sprints, 16th edition) → fast-forward sync (**12 commits pulled across 2 repos; all five repos clean, none dirty, none diverged, none switched branch**) → deterministic audit (exit 1, four undocumented admin routes) → manual contract review of all ten of today's commits plus yesterday's late webhook fix, which produced §0.1, §2.1, §2.2, §4.1 and §4.2 → re-audit (exit 0) → read-only scratch export of sprint 0901 → this report.

**Sprint 0901 was exported to `/tmp/beevia-scratch/`, outside the repository**, as it was on 3 September and for the same reason: `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest files as snapshots of one board, so a second CSV covering a different sprint would make tomorrow's delta compare 08-01 against 0901 and report invented movement. No file for it was written into the workspace. **This is the last edition for which that workaround is appropriate** — §9, item 5.

**Degraded inputs.** The `Epic` column is blank across the board — the OAuth refresh token lacks `ZohoSprints.epic.READ`. Known scope gap, not "no epic assigned". `Comments` bodies are unavailable from the API. The admin board produced no export because the project has no sprints (expected, not a failure). **`ZOHO_SPRINT_FILTER` is stale**: it still reads `08-01`, so the in-repo export covers a sprint that closed on 28 August, and the active sprint reached this report only through the scratch export above (§3). No step was skipped and no repo was analysed against stale code.

**Window.** 3 Sep 14:30 UTC → 4 Sep 14:00 UTC. This window includes `beevia-api`'s webhook fix, which was merged at 16:44 UTC on 3 September — after the previous edition's cut-off, which is why a change dated yesterday is reported today. All `actiontime` values and every time quoted in this report are UTC; git timestamps are as recorded (UTC−7) and are converted where compared against board times. The CSV's datetime columns render UTC+1.

**Sources.** Board: `beevia-sprint-board-2026-09-04.csv` (64 rows, 41 leaves, sprint 08-01), `beevia-activity-2026-09-04.json`. Active sprint: scratch export of `0901` (25 rows, 17 leaves) with its own activity sidecar. Admin board: none. Code: five repos at `origin/main`, plus read-only inspection of `origin/BVA-I192` on `beevia-mobile`. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (**34**), `openapi.admin.proposed.yaml` (**21**) — all validated, no drift, no markers, no broken refs, no orphaned components.

**A note on who appears here.** Only people whose work is tracked have rows. Board transitions performed by non-contributors are reported as transitions without attribution, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈55% (estimate; 55.37, from 53.95)

**Target 2026-09-01 (provisional) · the target date passed three days ago.** On merged build evidence the product is roughly 55% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. Unchanged |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present; incoming-call push wired. Unchanged |
| 3 | Message translation | 7 | 0.15 | Unchanged. `TranslateModule` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`; no provider adapter, no environment switch. A translation sprint is open and nothing in it addresses this |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full onboarding flow wired in the client. **Held, with a caveat now on the record:** virtual-account linking runs through the Anchor webhook, which processed nothing real until 3 Sep (§0.1). Provisioning does not depend on it alone — the 1 Sep commits connect the Anchor customer synchronously — so the score stands, but it was worth less than 0.9 for most of its life. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | **Held, and the reason changed.** Deposit crediting via the Anchor webhook is now genuinely live for the first time (§0.1) — a real gain that exactly offsets the discovery that it never worked before, so the number is unchanged while what it rests on is not. Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` unset), so it is not scored. Bank payout still unmerged on `origin/BVA-I192`; add-money still hard-coded on `main`. Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. P2P send wired end to end; ten server-side payment push triggers live. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; `PaymentService.activeNgn()` still present |
| 9 | Virtual cards | 10 | **0.55** ↑ | **+0.10.** Card lifecycle events are processed for the first time: `card.created` / `terminated` / `frozen` now sync status, last4 and expiry from Anchor, and pending cards refresh on list read — the catch-up that flips a freshly-issued card to `ACTIVE`, since Anchor emits no activation event. Before 3 Sep every one of those events was dropped (§0.1), so issuance could not complete. Ceiling unchanged and still low: the client has **zero** `/cards` references and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | **0.62** ↑ | **+0.07.** Admin API 30 → 34 operations; **Module 5 opens** with a global feed, per-user statement, per-user reconciliation and pool solvency (§2.1) — the first money-oversight surface this service has had, and 5 of 8 spec modules now have something behind them. Offset by the dashboard not moving: `beevia-admin` wires 3 of 8 modules, four of its nine feature modules are still `MOCK IMPLEMENTATION`, and it has had no commit for 4 days — including the two mocks whose blocking endpoints shipped today (§5) |
| | **Weighted total** | **100** | | **55.37 → ≈55%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, and never merged-but-disabled code.

**On the two movements, and on the one that looks like a non-movement.** Cards and admin oversight rise because specific things merged and can be named. Wallets is the interesting line: it holds at 0.70 while the evidence underneath it changed completely. A capability that was scored on a webhook that did not work is now scored on a webhook that does — the number is the same and it means something different, and pretending that is stability would be a worse report than saying so. Nothing was scored for the pooled treasury, which is merged but off, or for any of the four new admin endpoints beyond capability 11's own line.

**What this report cannot tell you:**
- **What the sixty-seven days of dropped Anchor events actually cost.** No backfill has been attempted and no reconciliation has been run over the period.
- **Whether sprint 0901 is deliberately paused or has simply not been picked up.** No comment, note or status change distinguishes the two.
- **Whether today's four admin endpoints work.** They have no HTTP-level tests, no second reviewer, and testing is out of scope for scoring per the owner's 2026-08-07 instruction.
- **Whether the reconciliation caps (500 / 1000) bind on any real account today.** That needs production data this report does not have.
- **Whether the seven already-built notification stories are known to be already built.** Still a code reading, not a conversation.
- **What the dropped `BVA-I171` was replaced by**, if anything.
- **Why `BVA-I192` has not merged**, now nine days after its last commit and with its board item closed.
- **How many other contracts or behaviours are wrong.** Two behaviour defects surfaced this cycle by reading diffs; 131 consumer operations have never had that treatment.
- **Anything about the Admin Dashboard board** beyond its existence — sixteenth edition with no sprint.
- **Velocity for either sprint** — 0 of 64 and 0 of 25 items estimated, and no board transitions in 24 hours to measure.
