# Beevia — Project Status

**As of 2026-08-20** · Sprint **08-01** (10 Aug → 28 Aug, day 11 of 18, 8 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-20.csv` + `beevia-activity-2026-08-20.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **The mobile work merged overnight — the wallet and send-money screens are on `main` for the first time. It shipped with the wrong URL still in it, the send button still not calling the API, and the wallet balance hardcoded to ₦100,000.**

| | 19 Aug | 20 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 22 | 19 | −3 |
| **In progress (leaves)** | 8 | **11** | **+3** |
| Blocked (leaves) | 3 | 2 | −1 |
| In review / QA (leaves) | 9 | 10 | +1 |
| Done (leaves) | 1 | 1 | **0 — still one, on day 11** |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| **Commits merged to `beevia-mobile`** | 0 | **2 (PR #25 + deps)** | **+2** |
| Client `/payments` calls on `main` | 0 | **2** | **+2** |
| Estimation points set | 0/67 | 0/67 | still zero |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| David Samuel | mobile | 3 To do, **4 In progress**, 3 Review/QA | Work merged via PR #25; started 5 more items today |
| Ayomikun Araoye | backend + admin API | 6 To do, 4 In progress, **7 Review/QA**, 2 Blocked | Picked up 3 items after 2 quiet days; still holds 7 review leaves |
| Philip Chidera | design | 10 To do, 3 In progress, 1 Done | Unchanged |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **14 days** silent, still no branches |

**The question for standup:** BVA-I170 "Wire Real Response into Wallet Screen" entered REVIEW/QA yesterday — but on `main` that screen takes a **hardcoded `balance = 100000`** and its transactions call points at an endpoint that returns 404. What is the reviewer being asked to accept?

**The three things worth knowing:**

1. **The merge happened, and it counts.** Yesterday's first recommendation was "merge `BVA-I189` today". It merged at **02:48 UTC** as PR #25 (`Bva i194`), squashed to `9ed54fc`, bringing p2p screens, the wallet implementation and recent-transactions work onto `main`. `beevia-mobile` went from 8 days stale to 1. Credit where due — this is the first client capability to land all sprint.
2. **It shipped with all three defects intact.** The one-line URL fix was not applied: `walletTransactionsUrl = "/payments/transactions"` is now on `main`, and that route exists in neither the code nor either spec. Beyond that, `_reviewPayment()` in `send_money_screen_p2p.dart` ends in `Navigator.of(context).pop(true)` — **no API call** — and neither `POST /payments/transfer` nor `GET /payments/recipients`, both shipped on 17 Aug, is referenced anywhere in the client. Money still cannot move from the app.
3. **Yesterday's report got the snapshot timing wrong, and it mattered.** I stated the board is pulled at "~09:15" and that "today is roughly two hours old when the data is pulled". The 09:15 is **local MDT**; the export cut-off is **~15:15 UTC ≈ 16:15 WAT** — late afternoon in the team's working day, not two hours in. Yesterday's "zero activity on 19 Aug" therefore covered most of a working day, and my hedge was too generous. Full correction in §4.

**If you read nothing else:** the client shell landed, which is real progress, but every defect flagged before the merge is now on `main` — and one of those files is sitting in review.

### MVP readiness — ≈47% (estimate, **up from ≈46%**)

**Target 2026-09-01 (provisional) · 12 days out.** First headline movement since the rubric began. Two capabilities moved on named, merged evidence:

- **#6 Multi-currency wallets 0.45 → 0.50.** A wallet home with balance, transactions and send-money entry points is now on `main`, with a real `WalletProvider` carrying loading/error state and `DioException` handling. Held to +0.05 because the balance is hardcoded and the transactions fetch 404s — the screens are real, the data is not.
- **#7 Send / request / receive 0.50 → 0.55.** The client now makes its first genuine payments call, `GET /payments/recent-recipients`, against the endpoint shipped 17 Aug. Held well below 0.7 because the send action itself makes no request: the flagship flow is still a stub, just a much more elaborate one.

Weighted total 47.3. Weights unchanged and still frozen.

---

## 1. Sprint 08-01 — the client lands

### 1.1 Status, day 11

| Status | Leaves | Share |
|---|---:|---:|
| To do | 19 | 44% |
| In progress | 11 | 26% |
| Review / QA | 10 | 23% |
| Blocked | 2 | 5% |
| Done | 1 | 2% |
| **Total** | **43** | |

### 1.2 Everything in the window

Window: **19 Aug 15:16 UTC → 20 Aug 15:28 UTC** (16:16 → 16:28 WAT). Seven board actions and two merges.

| When (UTC) | Who | What |
|---|---|---|
| 19 Aug 16:05 | David Samuel | BVA-I170 BLOCKED → In progress |
| 19 Aug 16:05 | `Fortune Okwu` | BVA-I170 In progress → **REVIEW/QA** |
| 20 Aug 01:19 | dependabot | `beevia-mobile` PR #13, CI action bumps |
| 20 Aug 02:48 | **Victor Peynado** | **`beevia-mobile` PR #25 `Bva i194` merged** — squash `9ed54fc` |
| 20 Aug 14:15 | David Samuel | BVA-I192, BVA-I193 To do → In progress |
| 20 Aug 14:16 | David Samuel | BVA-I199, BVA-I200, BVA-I201 To do → In progress |

BVA-I170's two transitions landed 49 minutes after yesterday's snapshot, which is why yesterday's edition reported it as still blocked.

### 1.3 What actually merged, read from `main`

`lib/features/wallet/` now exists on `main` with models, a provider, a service, widgets, and four screens (`wallet_screen`, `add_money_screen`, `send_money_screen_p2p`, `send_money_bank_transfer`).

**What is genuinely wired:**

| Call | Endpoint | Status |
|---|---|---|
| `WalletService.fetchRecentRecipients()` | `GET /payments/recent-recipients` | ✅ Real — endpoint shipped 17 Aug |
| `WalletService.fetchTransactions()` | `GET /payments/transactions` | ❌ **404 — route does not exist** |

`WalletProvider` is properly built around both: loading flags, error strings, `SocketException` and `DioException` handling, tolerant response parsing. That is real engineering, not scaffolding.

**What is not wired:**

- **Send money makes no request.** `_reviewPayment()` shows a review sheet, then a confirm sheet, then calls `Navigator.of(context).pop(true)`. The flow ends in navigation.
- **`POST /payments/transfer` is unreferenced** anywhere in `lib/`, 3 days after it shipped.
- **`GET /payments/recipients`** (the recipient search) is unreferenced; only *recent* recipients is used.
- **Wallet balance is hardcoded**: `wallet_screen.dart` declares `this.balance = 100000`.

Total `/payments` references in `lib/`: **2**, both in `api_url.dart`.

### 1.4 The 404 may be a race, not only a defect

Worth flagging as an open question rather than a verdict. **BVA-I200 "Transaction History Endpoint" moved to In progress today** (Ayomikun). If that item is intended to ship `GET /payments/transactions`, the client is coding against a planned route and the mismatch resolves itself on merge.

Two readings, and the team should pick one deliberately:

- **The client is wrong** — wallet transactions already exist at `GET /wallets/transactions` and `GET /wallets/{walletId}/transactions`. One-line fix, no backend work.
- **The client is early** — BVA-I200 builds `/payments/transactions` as a payments-scoped read path, and `openapi.proposed.yaml` gains an operation.

Either is defensible; what is not defensible is `main` calling a 404 while both readings stay unstated. Note the proposed spec already carries `GET /payments` as the payments read path, so a second payments-transactions route would want reconciling with it.

### 1.5 The review queue, day 11

Ten leaves, none ever drained this sprint. BVA-I170 joined yesterday — and §1.3 documents that the screen it covers reads a hardcoded balance and calls a dead endpoint. Whatever the reviewer is checking, the merged artifact does not yet do what the item title claims.

Ayomikun still holds 7 of the 10.

---

## 2. What shipped this cycle

**Two merges, both in `beevia-mobile`**, after five editions of zero.

| Repo | Last commit to `main` | Days | Note |
|---|---|---:|---|
| `beevia-mobile` | **20 Aug** | **1** | PR #25 + dependabot; was 8 days stale yesterday |
| `beevia-api` | 17 Aug | 3 | |
| `beevia-db-schema` | 17 Aug | 3 | |
| `beevia-admin-api` | 6 Aug | **14** | |
| `beevia-admin` | 6 Aug | **14** | still **no branches** |

`origin/BVA-I189` is gone — merged and deleted, which is the correct outcome. `origin/BVA-I194` remains at 20 Aug 20:41 local.

**Specs: no change required.** Audit clean at 108 consumer / 29 admin, no drift. The merge was client-side and moved no API surface. Yesterday's `openapi.proposed.yaml` description fix (the `GET /payments` rationale, updated to name `/payments/transfer`) is the only spec change this week beyond 17 Aug's three endpoints.

---

## 3. Risks

1. **A merged artifact is in review while known to be incomplete.** BVA-I170 covers a screen with a hardcoded balance and a dead endpoint call. If it is accepted, the queue's first-ever exit will certify something that does not work.
2. **`main` now calls a nonexistent endpoint.** Whatever the intent (§1.4), the shipped client 404s on wallet transactions today.
3. **The flagship capability is still not reachable.** Three days after `POST /payments/transfer` shipped, no client code calls it. Money cannot move from the app.
4. **WIP keeps climbing: 8 → 11 leaves**, against 1 Done on day 11 of 18. David opened five more items today while three of his sit in review.
5. **The review queue has never drained** — eleven days, ten leaves, zero exits.
6. **`beevia-admin` at 14 days**, no commits, no branches, no owned leaves — sixth consecutive edition.
7. **Estimation still 0/67** with 8 days left.

---

## 4. Correction — yesterday's timing claim was wrong

Yesterday's §4 introduced a correction about how these reports use "today". **That correction was itself wrong on its central point**, and it under-stated a real finding.

I wrote that the board snapshot is taken at "~09:15" and concluded that "'today' is roughly two hours old when the data is pulled", so "no activity today" is never a fair claim.

The 09:15 figure is the CSV header, which is the **exporting machine's local time — MDT (UTC−6)**. The activity sidecar's `actiontime` is UTC. Confirmed by file mtimes and by today's export containing actions timestamped 14:16 UTC:

| Export | Header (MDT) | Actual cut-off (UTC) | In team time (WAT, UTC+1) |
|---|---|---|---|
| 18 Aug | 09:14 | 15:14 | 16:14 |
| 19 Aug | 09:16 | 15:16 | 16:16 |
| 20 Aug | 09:28 | 15:28 | 16:28 |

So the daily cut-off is **late afternoon in the team's working day**, not early morning. Consequences:

- Yesterday's "no board action carries a 19 Aug timestamp" covered the Nigerian working day through **16:16 WAT** — most of it. The stall was more real than I allowed, and the "two-hour-old day" hedge should not have been offered.
- The board/git cut-off mismatch noted yesterday still holds and is now quantified: board data ends ~15:20 UTC; git data is current to report time (~15:30 UTC today). About ten minutes apart, not hours.
- Timezone is inferred from the export machine, not stated anywhere in the data. WAT is inferred from the product (BVN, NGN, Anchor) and from activity clustering at 12:00–17:00 UTC. If the team is not in WAT, the third column shifts.

Earlier editions' zero-activity statements should be read against the ~15:15 UTC cut-off, which makes them stronger, not weaker.

---

## 5. Previous recommendations — where they stand

| Recommendation from 19 Aug | Status on 20 Aug |
|---|---|
| Merge `BVA-I189` today | **Done** — PR #25 at 02:48 UTC. But merged **without** the one-line URL fix that was the substance of the ask. |
| Stop starting, start finishing | **Not done, moved backwards.** WIP 8 → 11; five new items opened today. |
| Get one item out of REVIEW/QA — any item | **Not done.** Queue grew 9 → 10; still zero exits all sprint. |
| Check in with Ayomikun | **Apparently yes.** Three items picked up today after two quiet days; the 7 review leaves are untouched. |

Two moved, two did not — the first real progress on this table since 17 Aug.

---

## 6. What I would do today

1. **Decide the `/payments/transactions` question in one conversation** (§1.4): fix the client to `/wallets/transactions`, or confirm BVA-I200 is building that exact route and add it to `openapi.proposed.yaml`. Today `main` 404s either way.
2. **Wire the send button to `POST /payments/transfer`.** The endpoint has been live for three days, the screens are merged, and the confirm sheet already collects everything the request body needs. This is the single change that makes the app able to move money.
3. **Do not accept BVA-I170 as-is.** The screen it names reads a hardcoded ₦100,000. Either wire the balance to `GET /wallets` first, or move the item back and say what "real response" means.
4. **Cap WIP before opening anything else.** 11 in progress, 10 in review, 1 done, 8 days left.
5. **`beevia-admin`, fourteen days.** Sixth edition asking.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`) → fast-forward-only sync (**`beevia-mobile` was on the `Mock-data` branch locally and was switched to `main`** — flagged in case someone was mid-task there) → deterministic API/spec audit (clean, no drift, no spec edits) → this report.

**Evidence for client claims.** Every statement in §1.3 is read from `origin/main` after the merge, not from the branch or from commit messages: `git show origin/main:<path>` for `wallet_service.dart`, `wallet_provider.dart`, `send_money_screen_p2p.dart` and `api_url.dart`, and `git grep` over `lib/` for `/payments` references. The hardcoded balance and the `pop(true)` are quoted from those files.

**Timing.** See §4. All transitions use the sidecar's UTC `actiontime`; the CSV header is MDT and is not a UTC cut-off.

**Sources.** Board: `beevia-sprint-board-2026-08-20.csv` (67 rows, 43 leaves, cut-off 15:28 UTC), `beevia-activity-2026-08-20.json`. Code: five repos at `origin/main`, 2 merges since 19 Aug; all pushed branches re-checked. Specs: `openapi.yaml` (108), `openapi.proposed.yaml` (52), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈47%

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live; provider integration and per-message endpoint BLOCKED; "v2" comment still unrecorded as a decision |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding; BVN cache 17 Aug |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | **0.50** ↑ | **Moved.** Wallet home, balance, transactions and send entry points merged to `main` with a real provider (loading/error/Dio handling). Ceiling: balance hardcoded `100000`, transactions call 404s, server still NGN-only |
| 7 | Send / request / receive | 12 | **0.55** ↑ | **Moved.** First real client payments call (`GET /payments/recent-recipients`). Ceiling: send action makes no request (`pop(true)`); `POST /payments/transfer` and `GET /payments/recipients` unreferenced |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only; BVA-I198 in review with no code |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 14 days silent, no branches |
| | **Weighted total** | **100** | | **47.3 → ≈47%** |

Weights frozen. Scores measure **merged, reachable build evidence**. Both increases this edition are merged-to-`main` facts; both are held well below their ceilings because the merged code does not yet do what the screens imply.

**Team performance — what these figures do not measure.** The merge is credited to Victor Peynado because he merged PR #25; the work in it is David's, squashed. "Items opened today" is not productivity — David opening five items reflects a plan, not effort. With 0/67 estimation points there is still no workload normalisation, and the rising WIP is a system property no individual chose.

**What this report cannot tell you:**
- Whether BVA-I200 intends to build `/payments/transactions` (§1.4) — the item title does not say.
- Whether the merged screens work at runtime; no build or test was run, and testing stays out of scope for scoring.
- What the reviewer of BVA-I170 is checking against.
- Whether the team is in WAT — inferred, not stated (§4).
- Velocity or scope-fit for the remaining 8 days — still 0/67 estimated.
