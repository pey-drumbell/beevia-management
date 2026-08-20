# Beevia — Project Status

**As of 2026-08-18** · Sprint **08-01** (10 Aug → 28 Aug, day 9 of 18, 10 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-18.csv` + `beevia-activity-2026-08-18.json` (67 items), cross-checked against all five repos re-synced to `origin/main`, plus every pushed branch on `beevia-api`, `beevia-mobile` and `beevia-admin`.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **The review queue went from 1 to 9 leaves — but not one of those nine corresponds to code merged during this sprint, and two people spent yesterday and today disagreeing about which items belong there at all.**

| | 17 Aug | 18 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 33 | 24 | −9 |
| In progress (leaves) | 7 | 6 | −1 |
| Blocked (leaves) | 1 | **3** | **+2** |
| **In review / QA (leaves)** | **1** | **9** | **+8** |
| Done (leaves) | 1 | 1 | 0 |
| Left review | 0 | **0** | still never drained |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| Commits merged to `main` | 11 | **0** | −11 |
| Estimation points set | 0/67 | 0/67 | still zero |

**Team, at a glance:**

| Person | Owns | Current leaf state | Commits to `main` | Flag |
|---|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 8 To do, 2 In progress, **7 Review/QA**, 2 Blocked | 0 | Bulk-moved ~24 items in 3 minutes on 17 Aug; now holds 7 of the 9 review leaves |
| David Samuel | mobile | 5 To do, 2 In progress, 2 Review/QA, 1 Blocked | 0 | **Has 5 unmerged commits on `origin/BVA-I189`** — the first client payments wiring. Reverted 11 of Ayomikun's review moves today |
| Philip Chidera | design | 11 To do, 2 In progress, 1 Done | — | Dark-mode items started then returned to To do |
| Promise Udo | admin dashboard | one co-assigned parent Story | 0 | `beevia-admin` **12 days** silent, and **has no branches** — only `main` |

**The question for standup:** `origin/BVA-I189` calls `GET /payments/transactions`. That endpoint does not exist — not in the implemented spec, not in the proposed one, not in the code. Wallet transactions live at `GET /wallets/transactions`. This will 404 the moment the branch runs against a real backend.

**The three things worth knowing:**

1. **The review queue is not evidence of finished work.** At 16:04–16:07 on 17 Aug — minutes after yesterday's export was taken — Ayomikun moved roughly 24 items in three minutes: 20 into REVIEW/QA and 4 into BLOCKED. Checked one by one against the code (§1.4), **none of the nine leaves now in review corresponds to anything merged during 08-01.** Four have no implementation anywhere, three match code that shipped in June or early August, and two are mobile items whose work sits unmerged on a branch.
2. **Two people are disagreeing about the board in public.** Today at 13:48–13:49 David moved 11 of those items straight back to To do — the whole in-chat send/request money group and the wallet transaction history group. Neither the move nor the reversion carries a comment. This is worth resolving as a definition question, not left as a silent edit war.
3. **The client work exists — it is just not merged, and it has a wrong URL.** `origin/BVA-I189` (David, 5 commits, tip 17 Aug) carries p2p screens, wallet implementation and recent-transaction work, and contains the **first `/payments` references anywhere in the client**. One of the two is correct (`/payments/recent-recipients`, shipped yesterday). The other points at an endpoint that does not exist.

**If you read nothing else:** the work is more real than the board suggests and the board is more finished-looking than the work. Merge the mobile branch after fixing one URL, and decide who is allowed to declare something ready for review.

### MVP readiness — ≈46% (estimate, unchanged)

**Target 2026-09-01 (provisional) · 14 days out.** No score moves. Nothing merged to `main` in any repo today, and the rubric scores merged, reachable capability — not branches, not board status, not items in review. Capability #7 stays at 0.50: the API side landed yesterday, and the client side now demonstrably exists but is unmerged, so it is a leading indicator rather than a score change. If `BVA-I189` merges with its URL corrected, #7 moves next edition.

**A scope signal the rubric cannot absorb on its own:** on 17 Aug Ayomikun commented on BVA-I218 "Live Auto-Translation in Conversations" — *"we moved this to version 2 we cannot have this currently"* — and the whole translation stack is now BLOCKED (§1.5). Weights are frozen, so this report does **not** silently re-weight capability #3. If translation is formally out of MVP, that is a methodology change and needs an explicit decision; flagged here rather than absorbed quietly.

---

## 1. Sprint 08-01 — the board moved, the code did not

### 1.1 Status, day 9

| Status | Leaves | Share |
|---|---:|---:|
| To do | 24 | 56% |
| In progress | 6 | 14% |
| **Review / QA** | **9** | **21%** |
| Blocked | 3 | 7% |
| Done | 1 | 2% |
| **Total** | **43** | |

67 rows: 24 parent Stories grouping 43 leaf Tasks. Counting rows rather than leaves gives 13 in review; the leaf figure of 9 is the one to use.

### 1.2 What actually happened, from the activity trail

The snapshot delta says "+8 into review, 0 out". The audit trail shows considerably more churn than that, and the difference matters.

| When (UTC) | Who | What |
|---|---|---|
| 17 Aug 16:04–16:06 | Ayomikun Araoye | ~24 items moved in **three minutes**: 20 To do → REVIEW/QA, 4 To do → BLOCKED (the translation stack) |
| 17 Aug 16:06 | Ayomikun Araoye | Comment on BVA-I218: *"we moved this to version 2 we cannot have this currently"* |
| 17 Aug 16:07 | `Fortune Okwu` | BVA-I189 and BVA-I198 moved In progress → REVIEW/QA — both David's mobile items |
| 18 Aug 13:38 | David Samuel | BVA-I174 Add Money (Bank Transfer) Screens → In progress |
| 18 Aug 13:48–13:49 | David Samuel | **11 items moved REVIEW/QA → To do** |

The 11 David reverted: BVA-I176/I177/I178/I179 (In-Chat Send Money), BVA-I180/I181/I182/I183 (In-Chat Request Money), BVA-I199/I200/I201 (Wallet Transaction History).

A three-minute, 24-item transition is a bulk triage, not twenty completions. Reporting it as throughput would repeat the `Last Modified` error this pipeline made on 05 Aug — the timestamps are what distinguish the two, which is why they are quoted here.

### 1.3 The nine leaves now in review

| Item | Owner | Moved by | Code evidence |
|---|---|---|---|
| BVA-I165 Preference Storage & Precedence Logic | Ayomikun | Ayomikun, bulk | **None.** `/users/me/translation` is in `openapi.proposed.yaml` only |
| BVA-I169 Anchor Integration | Ayomikun | Ayomikun, bulk | Code exists — `POST /webhooks/anchor`, last changed **28 June** |
| BVA-I173 Incoming Transfer Webhook Handling | Ayomikun | Ayomikun, bulk | Same controller, same **28 June** commit |
| BVA-I185 Wallet Summary Endpoint | Ayomikun | (14 Aug) | **None on any pushed branch** — see §1.4 |
| BVA-I189 Send Money (P2P) Screens | David | `Fortune Okwu` | Unmerged: `origin/BVA-I189`, 5 commits, tip 17 Aug |
| BVA-I198 Card Preview UI | David | `Fortune Okwu` | **No branch exists** for it in `beevia-mobile` |
| BVA-I203 Hold/Escrow, Auto-Refund Job & Notifications | Ayomikun | Ayomikun, bulk | Code exists — `escrow.service.ts` + expiry processor, predates **2 Aug** |
| BVA-I221 Wallet Summary & Transaction History Endpoint | Ayomikun | Ayomikun, bulk | Transaction history exists (`/wallets/transactions`); **the summary half does not** |
| BVA-I223 Transfer Status Lookup & Overdue-Pending Query | Ayomikun | Ayomikun, bulk | **None.** No such route in code or in either spec |

**Not one of the nine maps to code merged during sprint 08-01.** Three map to work that shipped weeks before it started. That is not an accusation of anything: items can legitimately be marked for review because the work was done earlier and is only now being verified. But it does mean the queue depth cannot be read as sprint progress, and someone should say which of the two it is.

### 1.4 BVA-I185: yesterday's open question, now closed

Yesterday's edition said the wallet-summary endpoint was not on `main` and explicitly noted the search "says nothing about unmerged branches." That gap is now closed. Across **every pushed branch** of `beevia-api` (`main`, `feat/payments-direct-transfer`, `feat/bvn-lookup-cache`, `fix/upgrade-path-flip-after-provision`, `feat-super-admin-panel`, `victor`, and the dependabot branch):

- `src/wallets/wallets.controller.ts` is **byte-identical to `main` on all of them** — seven routes, unchanged since 22 July.
- No branch contains a wallet-summary route.

So the endpoint is not on `origin` at all. The only remaining benign explanation is work that has never been pushed. BVA-I185 has now been in REVIEW/QA for **4 days**, and BVA-I170 has been BLOCKED on it for **5**.

### 1.5 The translation stack is blocked and may be out of scope

| Item | Status |
|---|---|
| BVA-I162 Translation Service Integration *(parent)* | BLOCKED |
| BVA-I163 Translation Provider Integration | BLOCKED |
| BVA-I166 Translate-Message Endpoint *(parent)* | BLOCKED |
| BVA-I167 Translate Endpoint | BLOCKED |
| BVA-I218 Live Auto-Translation in Conversations | To do, commented *"moved to version 2"* |

All four blocks were set in the same 16:04 bulk operation. `POST /translate` remains live and unchanged; what is blocked is the provider integration and the per-message endpoint behind it. Combined with the v2 comment, this reads as translation being deferred — but no decision is recorded anywhere this report can cite, so it is reported as a signal, not a fact.

### 1.6 What is still missing

- **Estimation points: 0 of 67**, day 9 of 18. Recommended on days 2, 3, 4, 5 and 8. The sprint will end without a velocity baseline.
- **Epics: 8 of 67. Tags: 0 of 67.**
- **Blocked reasons:** still no reason field on any of the three blocked leaves.
- **No comment on either the bulk review move or the 11-item reversion.**

---

## 2. What shipped this cycle

**Nothing merged.** Zero commits to `main` in any of the five repos since yesterday's 11. All five were already at `origin/main` on sync. The audit is clean at 108 consumer / 29 admin operations with no drift, and the four specs needed no edits — yesterday's three payment endpoints are already documented.

**But unmerged work exists, and this is the first edition able to quantify it:**

| Repo | Branch | Commits ahead | Tip | Contents |
|---|---|---:|---|---|
| `beevia-mobile` | `origin/BVA-I189` | 5 | 17 Aug | p2p screens, wallet implementation, recent wallet transactions, notifications |
| `beevia-mobile` | `origin/BVA-I184` | 3 | 13 Aug | wallet implementation |
| `beevia-mobile` | `origin/BVA-I107` | 2 | 11 Aug | fixes |
| `beevia-api` | — | — | — | all feature branches already merged; nothing outstanding |
| `beevia-admin` | **none** | — | — | **only `main` exists** |

Repo staleness on 18 Aug: `beevia-api` 1d · `beevia-db-schema` 1d · `beevia-mobile` 7d on `main` (but 1d on `BVA-I189`) · `beevia-admin-api` **12d** · `beevia-admin` **12d**.

That `beevia-admin` has no branches at all is worth stating plainly: for the mobile workstream, "silent `main`" turned out to hide real branch activity. For the admin dashboard, there is nothing pushed anywhere to hide behind.

### 2.1 The integration bug

`origin/BVA-I189` declares two payment URLs and calls both from `lib/features/wallet/services/wallet_service.dart`:

| Constant | URL | Status |
|---|---|---|
| `recentWalletRecipientsUrl` | `/payments/recent-recipients` | ✅ Correct — shipped 17 Aug |
| `walletTransactionsUrl` | `/payments/transactions` | ❌ **Does not exist** |

There is no `GET /payments/transactions` in the code, in `openapi.yaml`, or in `openapi.proposed.yaml`. Wallet transactions are served by `GET /wallets/transactions` and `GET /wallets/{walletId}/transactions`. The call is live in `wallet_service.dart`, not a leftover constant, so it will 404 against a real backend.

This is a one-line fix, and it is exactly the class of error a merged branch and a running CI would have surfaced days ago.

---

## 3. Product-vs-PRD gap

| PRD capability | State |
|---|---|
| Cross-currency conversion | **Not built.** `PaymentService` resolves NGN unconditionally, including in the new `transfer()` path. |
| Virtual cards | **Not built.** BVA-I198 is in review with no branch behind it. |
| International KYC tier | **Not built.** Local Nigerian path only. |
| Consent management | **Not built.** |
| Payments read path | **Still missing.** No `GET /payments`. The client branch's attempt to read transactions from `/payments/transactions` is a direct symptom of this gap. |
| Send-money client wiring | **Exists, unmerged.** First `/payments` calls in the client, on `origin/BVA-I189`. |
| Message translation | **Live but blocked, possibly descoped** — see §1.5. |

---

## 4. Risks

1. **Review-queue depth no longer means what it appears to mean.** Nine leaves in review, zero traceable to sprint code, and the queue has never once drained across seven editions.
2. **Two contributors are silently contradicting each other on the board.** 24 items moved in, 11 moved back out a day later, no comment on either action.
3. **`origin/BVA-I189` will fail on a nonexistent endpoint** the moment it is exercised, and it is the branch carrying the flagship capability.
4. **Unmerged work is accumulating.** Five commits and 11 days of mobile work sit on a branch while `main` looks idle. Long-lived branches are how integration bugs like §2.1 survive.
5. **BVA-I185 is 4 days in review with no code on any pushed branch**, and blocks BVA-I170 at 5 days.
6. **The admin dashboard has no code and now demonstrably no branches** — 12 days silent, and the workstream still has no owned leaf.
7. **Translation may have been descoped by comment rather than by decision** (§1.5).
8. **Estimation remains 0/67** on day 9; scope-fit for the last 10 days cannot be defended numerically.

---

## 5. Previous recommendations — where they stand

| Recommendation from 17 Aug | Status on 18 Aug |
|---|---|
| Locate BVA-I185 — unmerged branch, or item ahead of the work? | **Answered, negatively.** Not on any pushed branch of `beevia-api` (§1.4). Still in review. |
| Repeat the small-branch → PR → merge pattern | **Not repeated.** Zero merges today, after 11 commits yesterday. |
| Point the mobile work at the API that now exists | **Underway, unmerged.** `origin/BVA-I189` has the first `/payments` calls — one correct, one pointing at a nonexistent route (§2.1). |
| Name an accept/reject owner for REVIEW/QA and cap WIP | **Not done, and it got worse.** The queue went 1 → 9 with no named owner, then 11 items were reverted by a second person. |
| Ask about the two admin repos | **No change.** 12 days silent; confirmed today that `beevia-admin` has no branches either. |
| Estimate or stop measuring | **Not done.** Still 0/67. |

One answered, four open, one that moved backwards.

---

## 6. What I would do today

1. **Fix one line and merge `BVA-I189`.** Change `/payments/transactions` to `/wallets/transactions`, open the PR, merge. That single action converts 11 days of invisible work into build evidence and would move the MVP number next edition.
2. **Decide who may move an item into REVIEW/QA, and say it out loud.** Yesterday one person moved 24 items in; today another moved 11 back. Both are acting reasonably under different definitions. The cost is not the disagreement, it is that it is happening silently.
3. **Split the review queue into "already shipped, needs verifying" and "not built yet."** §1.3 does this for the current nine; the board should carry the distinction itself, otherwise queue depth is unreadable.
4. **Get a straight answer on BVA-I185.** Four days in review, nothing on `origin`, and it has blocked David for five days. If it is unpushed local work, push it; if it was moved prematurely, move it back.
5. **Record the translation decision.** If live auto-translation is v2, put it in the sprint scope rather than in a comment on one item, and say whether capability #3 stays in the MVP rubric.
6. **Ask about `beevia-admin` directly.** Twelve days, no commits, no branches, no owned board items. This is the fourth consecutive edition raising it.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`) → fast-forward-only sync of five product repos (already current) → deterministic API/spec audit (**clean, no drift, no spec edits needed**) → this report.

**Extended evidence this edition.** Because the central question was whether review items correspond to real work, the usual `origin/main` check was widened to **every pushed branch** on `beevia-api`, `beevia-mobile` and `beevia-admin`, using `git diff` against `main` per branch and `git show <branch>:<path>` to read files directly. That is how §1.4 closes yesterday's caveat and how §2.1 was found.

**Flow measurement.** Every transition, actor and timestamp comes from the activity sidecar's `actiontime`. The three-minute window in §1.2 is what identifies the bulk operation; a snapshot diff alone would have reported it as eight items of progress.

**A limit of the audit line.** The audit reports "0 left REVIEW/QA" between snapshots. That is true of the endpoints but hides the churn: 20 items entered and 11 left between the two exports. Both facts are reported above rather than only the tidier one.

**Sources.**
- Board: `beevia-sprint-board-2026-08-18.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-18.json`
- Code: five repos at `origin/main`, zero commits since 17 Aug; plus all pushed branches
- Specs: `openapi.yaml` (108), `openapi.proposed.yaml` (52), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift

### MVP readiness — ≈46%

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live; batch + language list proposed. **Provider integration and per-message endpoint now BLOCKED; live auto-translation commented "v2"** — unscored pending an explicit decision |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding; BVN cache added 17 Aug |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.45 | NGN only; wallets controller unchanged since 22 July on every branch; no wallet summary anywhere |
| 7 | Send / request / receive | 12 | 0.50 | API write path near-complete after 17 Aug. Client wiring now **exists but is unmerged** (`origin/BVA-I189`) and contains a wrong URL — leading indicator, not yet a score |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only; BVA-I198 in review with no branch behind it |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 12 days silent, no branches |
| | **Weighted total** | **100** | | **46.1 → ≈46%** |

Weights are frozen so the number stays comparable. Scores measure **merged, reachable build evidence** — never board status, items in review, unmerged branches, or design completion. Branch work is reported in the narrative and scored only when it lands.

**Team performance — what these figures do not measure.** With 0/67 estimation points there is no workload normalisation. "Commits to `main`" reads as zero for David today, and that is precisely the metric this edition proves misleading: five commits exist on his branch. The bulk board operation is a process observation about definitions, not about anyone's effort or output, and both contributors' readings of "ready for review" are defensible.

**What this report cannot tell you:**
- Whether BVA-I185's endpoint exists as unpushed local work. Every pushed branch has been checked; local clones cannot be.
- Why the 11 items were reverted — no comment was left.
- Whether translation is formally descoped, or one person's view recorded in a comment.
- Whether the mobile branch works beyond the URL defect — no tests were run, and testing remains out of scope for scoring.
- Velocity or scope-fit for the remaining 10 days — still 0/67 estimated.
