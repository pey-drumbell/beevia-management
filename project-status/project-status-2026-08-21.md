# Beevia — Project Status

**As of 2026-08-21** · Sprint **08-01** (10 Aug → 28 Aug, day 12 of 18, 7 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-21.csv` + `beevia-activity-2026-08-21.json` (67 items), cross-checked against all five repos and every pushed branch.

> **Revised edition.** This replaces the version issued earlier today. `beevia-mobile` PR #27 merged at 14:10 UTC, two minutes before the refreshed board snapshot, and it changes the headline: the send-money flow is now wired end to end. The MVP estimate moves 47% → 50%. Sections §2, §4 and the rubric are substantially rewritten.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **Send money is wired end to end for the first time — the client now calls `POST /payments/transfer` with a correct request body, the wallet reads real balances, and yesterday's wrong URL is fixed. It will still fail: the transfer requires a step-up token the client never obtains.**

| | 20 Aug | 21 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 19 | 19 | 0 |
| In progress (leaves) | 11 | 10 | −1 |
| **Blocked (leaves)** | 2 | **3** | **+1 — P2P Transfer, again** |
| In review / QA (leaves) | 10 | 10 | 0 — *zero exits, 12 days running* |
| Done (leaves) | 1 | 1 | **0 — still one, on day 12** |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| Commits merged | 2 (mobile) | **4 (api + mobile)** | KYC fix + **PR #27** |
| **Client `/payments/transfer` calls** | 0 | **1** | **wired at last** |
| Client endpoints called (real) | 1 of 2 | **4 of 4** | URL bug fixed |
| Estimation points set | 0/67 | 0/67 | still zero |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| David Samuel | mobile | 3 To do, 4 In progress, 3 Review/QA | **Merged PR #27** — the send-money wiring |
| Ayomikun Araoye | backend + admin API | 6 To do, 3 In progress, **7 Review/QA**, **3 Blocked** | Shipped the KYC selfie fix; all three blocked leaves are his |
| Philip Chidera | design | 10 To do, 3 In progress, 1 Done | Unchanged |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **15 days** silent, still no branches |

**The question for standup:** `POST /payments/transfer` is guarded by `StepUpGuard`, which requires an `X-Step-Up-Token` header minted by `POST /auth/step-up`. The client calls `POST /auth/pin/verify` instead — which the spec says explicitly **does not mint a step-up token** — and sends no such header anywhere in `lib/`. Every transfer will return **401**. Who is fixing that, today?

**The three things worth knowing:**

1. **The send-money flow is genuinely wired.** PR #27 (`Bva i187`, David, 14:10 UTC) added `WalletService.transferMoney()` posting to `/payments/transfer` with `recipientUserId`, `amount`, `note` and `idempotencyKey` — matching the API contract exactly — plus loading and error state through `WalletProvider`, surfaced in the send screen. `_reviewPayment()` no longer ends in `Navigator.pop(true)`; it awaits the transfer and reports failure. Four days after the endpoint shipped, something calls it.
2. **The wallet is now real, and yesterday's bug is fixed.** `walletTransactionsUrl` changed from the nonexistent `/payments/transactions` to `/wallets/transactions`. A new `GET /wallets` call (`fetchWallets`) feeds the balance — `wallet?.numericBalance ?? widget.balance`, with the default dropped from `100000` to `0`. A `transaction_history` screen was added. Every client endpoint now points at a route that exists.
3. **It will not work yet, for one specific reason.** The step-up gap above is a missing step of the designed auth flow (ADR-0003), not a typo. The fix is small — call `/auth/step-up`, keep the returned token, attach `X-Step-Up-Token` on the transfer — but until it lands, the flow is complete on paper and 401 in practice.

**If you read nothing else:** the sprint's headline capability went from inert to wired in one merge. One missing header stands between it and working.

### MVP readiness — ≈50% (estimate, **up from ≈47%**)

**Target 2026-09-01 (provisional) · 11 days out.** Two capabilities move on merged evidence:

- **#6 Multi-currency wallets 0.50 → 0.65.** `GET /wallets` drives the balance, `/wallets/transactions` is correct and called, transaction history has a screen. Ceiling: server still NGN-only (`activeNgn()`), no wallet-summary endpoint, no currency selection.
- **#7 Send / request / receive 0.55 → 0.65.** The send path is wired end to end with a correct request body. Held at 0.65, not higher, because the step-up step of the designed flow is **absent** — so the wiring is incomplete, not merely buggy — and because request/receive have no client flow at all.

Weighted total 50.3. Weights unchanged and still frozen. This is the largest single-day movement since the rubric began, and it is entirely attributable to one merge.

---

## 1. Sprint 08-01 — wired, and one header short

### 1.1 Status, day 12

| Status | Leaves | Share |
|---|---:|---:|
| To do | 19 | 44% |
| In progress | 10 | 23% |
| Review / QA | 10 | 23% |
| Blocked | 3 | 7% |
| Done | 1 | 2% |
| **Total** | **43** | |

### 1.2 Everything in the window

Window: **20 Aug 15:28 UTC → 21 Aug 14:12 UTC** (16:28 → 15:12 WAT). The board was re-exported after the merge; its cut-off is 14:12 UTC, two minutes after PR #27 landed.

| When (UTC) | Who | What |
|---|---|---|
| 20 Aug 15:43 | David Samuel | BVA-I187 *(parent)* and BVA-I188 In progress → **BLOCKED** |
| 20 Aug 16:09 | Ayomikun (`Phoenixdadhev`) | `fix(kyc): send the selfie as a URI so face verification can actually run` |
| 20 Aug 16:12 | Ayomikun Araoye | `beevia-api` PR #23 merged |
| **21 Aug 14:10** | **David Samuel** | **`beevia-mobile` PR #27 `Bva i187` merged** |

**The board has not caught up with the code.** BVA-I187 "Send Money to Another Beevia User (P2P)" is the item PR #27 is named for, and at the 14:12 UTC snapshot both it and BVA-I188 still read **BLOCKED** — set 22 hours earlier. Either the block is stale, or it refers to something the merge does not resolve. Nobody can tell from the board, because neither transition carries a comment (§1.4).

### 1.3 What PR #27 changed

Twelve files under `lib/`, read from `origin/main`:

| Area | Change |
|---|---|
| `core/constants/api_url.dart` | `walletTransactionsUrl` **`/payments/transactions` → `/wallets/transactions`** (yesterday's 404 fixed); added `walletsUrl = "/wallets"`, `walletTransferUrl = "/payments/transfer"`, `verifyPinUrl = "/auth/pin/verify"` |
| `wallet/services/wallet_service.dart` | Added `fetchWallets()`, `verifyPin()`, and **`transferMoney()`** |
| `wallet/screens/wallet_screen.dart` | Balance now `wallet?.numericBalance ?? widget.balance`; hardcoded default **`100000` → `0`** |
| `wallet/screens/send_money_screen_p2p.dart` | `_reviewPayment()` awaits `walletProvider.transferMoney(...)`, handles `paymentError`, drives a `transferring` loading state |
| `wallet/screens/transaction_history.dart` | New screen |
| `wallet/models/wallet_account.dart` | New model |

The transfer request body:

```dart
{'recipientUserId': …, 'amount': amount.toString(), 'note': …, 'idempotencyKey': …}
```

That matches `TransferRequest` in `openapi.yaml` — three required fields present, `note` optional, `conversationId` correctly omitted. The amount is sent as a string, as the `Money` schema expects.

### 1.4 The step-up gap, precisely

This is the one thing standing between the merged flow and a working one.

| Layer | State |
|---|---|
| API | `POST /payments/transfer` carries `@UseGuards(StepUpGuard)`; the guard reads `x-step-up-token` and throws `UnauthorizedException` when it is absent |
| Spec | `POST /auth/step-up` — *"Verifies the PIN and mints a short-lived step-up token (default 5m). Send it as `X-Step-Up-Token` on financial and destructive actions (ADR-0003)."* |
| Spec | `POST /auth/pin/verify` — *"Confirms the PIN (app unlock / new-device owner confirmation). **Does not mint a step-up token.**"* |
| Client | Calls `/auth/pin/verify`. **Zero** occurrences of `x-step`, `stepUp` or `step_up` anywhere in `lib/` |
| Client | The Dio interceptor sets only `authorization: Bearer …`; `transferMoney()` passes no per-call headers |

So the client verifies the PIN against the endpoint that explicitly does not produce a step-up token, and never sends the header the guard requires. **Every transfer returns 401.**

The fix is three changes: point PIN verification at `/auth/step-up`, retain the returned token, and attach it as `X-Step-Up-Token` on the transfer call. Note the token's default TTL is 5 minutes, so it should be minted at the confirm step, not at app unlock.

### 1.5 The review queue, day 12

Ten leaves, **zero exits in twelve days**, median age 4 days. Ayomikun holds 7.

| Item | In review since | Age |
|---|---|---:|
| BVA-I184, **BVA-I185** | 14 Aug 12:19 | **7d** |
| BVA-I164, I165, I169, I173, I189, I198, I203, I220, I221, I222, I223 | 17 Aug 16:04–16:07 | 4d |
| BVA-I170 | 19 Aug 16:05 | 2d |

BVA-I185 "Wallet Summary Endpoint" is 7 days in review and `wallets.controller.ts` is **still unchanged since 22 July** — 7 routes, no summary. Note PR #27 works around this: the client reads `GET /wallets` and `/wallets/transactions` rather than waiting for a summary route. That may make BVA-I185 unnecessary; someone should decide rather than leave it ageing in a queue.

---

## 2. What shipped this cycle

**Four commits across two repos.**

**`beevia-mobile` PR #27 `Bva i187`** (David, 14:10 UTC) — the send-money wiring described in §1.3. `beevia-mobile` `main` moves to 21 Aug.

**`beevia-api` PR #23** (Ayomikun, 20 Aug 16:12 UTC) — `fix(kyc): send the selfie as a URI so face verification can actually run`. YouVerify validates `validations.selfie.image` as a URI and rejected raw base64 with a `400 ValidationError` before any face matching ran. The code had been in that state since **29 June** — seven weeks. The commit also widens BVN field extraction and surfaces a `validationMessage`. No controllers or DTOs touched, so no route moved and **no spec change was required**.

| Repo | Last commit to `main` | Days |
|---|---|---:|
| `beevia-mobile` | **21 Aug** | **0** |
| `beevia-api` | 20 Aug | 1 |
| `beevia-db-schema` | 17 Aug | 4 |
| `beevia-admin-api` | 6 Aug | **15** |
| `beevia-admin` | 6 Aug | **15** |

**`beevia-mobile` was skipped by the sync — dirty working tree** (`analysis_options.yaml`, `pubspec.lock` modified locally), so the local clone sits **1 commit behind** `origin/main`. Every client claim in this report is read directly from `origin/main` via `git show` / `git grep`, not from the working tree, so none of it is stale. The local edits — an `analyzer: exclude:` block and a lockfile — are untouched; commit or stash them and the next sync will fast-forward.

**Specs:** audit clean at 108 consumer / 29 admin, no drift, no edits needed. PR #27 consumes existing endpoints; PR #23 changed no routes.

---

## 3. Risks

1. **The wired transfer will 401 on every attempt** (§1.4) until the step-up token is obtained and sent.
2. **The board contradicts the code.** BVA-I187 is BLOCKED while the PR named for it is merged, and no comment explains either state.
3. **Blocked items still carry no reasons** — BVA-I188 has four transitions in eight days, none annotated.
4. **Twelve days, zero review exits.** The oldest item (BVA-I185, 7d) may now be obsolete, and nobody has said so.
5. **A load-bearing integration was broken for seven weeks without detection** (§4) — and the step-up gap is the same class of defect, caught here only by reading the code against the spec.
6. **Both admin repos at 15 days**, no commits, no branches, no owned leaves — seventh consecutive edition.
7. **Estimation still 0/67** with 7 days left.

---

## 4. Two defects, one lesson

Today surfaced two integration failures at opposite ends of their lifecycle, and they make the same point.

**The KYC selfie bug** ran for seven weeks. Capability #4 has been scored **0.9 in every edition since 05 Aug** on evidence reading "BVN, facial verification" — while facial verification could not run at all, rejected with a 400 before the face-match step. The rubric behaved as designed: it scores *implementation of the design*, and every edition has carried the caveat that it "cannot tell you whether a built screen or endpoint functions correctly", because testing is out of scope for scoring per the owner. #4 **stays 0.9** — the fix restores intended behaviour rather than adding capability.

**The step-up gap** is the same shape, caught on day zero instead of week seven — and only because this report reads the client against the spec. Nothing in CI would have caught either.

Two honest conclusions:

- **The MVP percentage measures built surface, not working product.** Today's +3 points are real wiring, and the flow still returns 401. Both statements are true at once, which is exactly the gap the number carries.
- **This is the strongest argument yet for the testing rules staged in `agent-rules/`.** One integration test on the YouVerify payload, and one asserting `POST /payments/transfer` rejects a request without `X-Step-Up-Token`, would have caught both. Those rules remain drafted and unapplied.

If the readiness number should mean "works" rather than "exists", the rubric needs a correctness input — a methodology decision for the owner, not one this report should make alone.

---

## 5. Previous recommendations — where they stand

| Recommendation from 20 Aug | Status on 21 Aug |
|---|---|
| Decide the `/payments/transactions` question | **Done.** PR #27 pointed it at `/wallets/transactions` — the existing route. The client-was-wrong reading was correct. |
| Wire the send button to `POST /payments/transfer` | **Done.** `transferMoney()` posts the correct body. Blocked in practice by the step-up gap (§1.4). |
| Do not accept BVA-I170 as-is | **Overtaken.** The hardcoded balance it covered is gone — the screen now reads `GET /wallets`. The item can probably be re-reviewed against the new code. |
| Cap WIP before opening anything else | **Partly.** WIP 11 → 10, by blocking two items rather than finishing any. |
| `beevia-admin`, fourteen days | **Not done.** Now 15. |

Two done, one overtaken by events, two open — much the best day on this table since the sprint began.

---

## 6. What I would do today

1. **Fix the step-up gap** (§1.4). Call `/auth/step-up` at the confirm sheet, hold the 5-minute token, send `X-Step-Up-Token` on the transfer. Everything else in the flow is already correct.
2. **Then test one real transfer end to end** and say so publicly. It would be the first money moved through the app, and it settles what six editions of board status could not.
3. **Update the board to match the code.** BVA-I187 is merged and still BLOCKED; BVA-I188 has four unannotated transitions. Either unblock them or write down what is blocking.
4. **Decide whether BVA-I185 is still needed.** PR #27 routed around the wallet-summary endpoint. If it is obsolete, close it — that also clears the queue's oldest item.
5. **`beevia-admin`, fifteen days.** Seventh edition.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`, run twice today: the second pass followed the user's merge. Zoho export (67 items, `--modified --activity`, cut-off 14:12 UTC) → fast-forward-only sync (**`beevia-mobile` skipped, dirty working tree; local clone is 1 commit behind `origin/main`**) → deterministic API/spec audit (clean, no drift, no spec edits) → this report.

**Evidence for client claims.** All read from `origin/main`, not the working tree, precisely because the local clone is behind: `git show origin/main:<path>` for `api_url.dart`, `wallet_service.dart`, `send_money_screen_p2p.dart`, `network_service.dart`; `git grep origin/main` for `walletTransferUrl`, `x-step`/`stepUp`/`step_up`; `git diff --name-only HEAD origin/main -- lib/` for the PR #27 file list. The step-up finding in §1.4 cross-references `src/auth/step-up.guard.ts` and the `/auth/step-up` and `/auth/pin/verify` descriptions in `openapi.yaml`.

**Window.** 20 Aug 15:28 UTC → 21 Aug 14:12 UTC. Per the 20 Aug correction, CSV header times are the exporting machine's local MDT; `actiontime` values are UTC. WAT (UTC+1) is inferred for the team, not stated in the data.

**Sources.** Board: `beevia-sprint-board-2026-08-21.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-21.json`. Code: five repos; `beevia-api` +2, `beevia-mobile` +1 on `origin/main`. Specs: `openapi.yaml` (108), `openapi.proposed.yaml` (52), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈50%

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live; provider integration and per-message endpoint BLOCKED; "v2" comment still unrecorded as a decision |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding. **Face verification was non-functional 29 Jun → 20 Aug (§4); fixed by PR #23.** Score unchanged — the rubric measures built surface, not correctness |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | **0.65** ↑ | **Moved.** `GET /wallets` drives the balance (hardcoded default gone), `/wallets/transactions` corrected and called, transaction-history screen added. Ceiling: server NGN-only via `activeNgn()`, no wallet-summary route, no currency selection |
| 7 | Send / request / receive | 12 | **0.65** ↑ | **Moved.** Send wired end to end: `transferMoney()` posts a spec-correct body to `POST /payments/transfer` with loading/error state. Ceiling: **step-up token absent, so it 401s** (§1.4) — a missing step of the designed flow, not a bug; request/receive have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only; BVA-I198 in review with no code |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 15 days silent, no branches |
| | **Weighted total** | **100** | | **50.3 → ≈50%** |

Weights frozen. Scores measure **merged, reachable build evidence** — see §4 for what that deliberately excludes.

**Team performance — what these figures do not measure.** David merged PR #27 and appears as the actor on four BVA-I188 transitions; the first is delivery, the second records who clicked, not who is responsible for a blockage. Ayomikun holding all three blocked leaves reflects that the backend owns the contested work — and he shipped the KYC fix. With 0/67 estimation points there is still no workload normalisation.

**What this report cannot tell you:**
- **Whether the transfer works** — the step-up gap says it will 401, but that is read from code, not observed. No build or test was run.
- **Why BVA-I188 is blocked**, or whether PR #27 resolves it — no reason field, no comment, twice.
- Whether the KYC fix works against live YouVerify; the commit says it was verified, no test covers it.
- What was done on 21 Aug after 14:12 UTC.
- Velocity or scope-fit for the remaining 7 days — still 0/67 estimated.
