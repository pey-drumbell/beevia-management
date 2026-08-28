# Beevia — Project Status

**As of 2026-08-27** · Sprint **08-01** (10 Aug → 28 Aug, day 18 of 18, 1 day left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-27.csv` + `beevia-activity-2026-08-27.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **The biggest delivery day of the project: 21 commits, 23 new API operations, virtual cards shipped end to end — and the step-up fix merged, so money can finally move through the app. The MVP estimate moves 50% → 58%.**

| | 26 Aug | 27 Aug | Δ |
|---|---:|---:|---:|
| **API surface (consumer)** | 108 | **131** | **+23** |
| Proposed operations | 53 | 42 | −11 (10 shipped, 1 net) |
| Commits merged | 16 | **21** | across 3 repos |
| **Send money reachable?** | no — 401 | **yes** | step-up merged 03:30 UTC |
| To do (leaves) | 6 | 3 | −3 |
| In progress (leaves) | 14 | 2 | −12 |
| **In review / QA (leaves)** | 13 | **27** | **+14 — 63% of the sprint** |
| Done (leaves) | 8 | 9 | +1 |
| Review exits, all sprint | 0 | **0** | 18 days |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| Ayomikun Araoye | backend + admin API | 2 To do, **13 Review/QA**, 1 Blocked, 3 Done | Shipped the cards, top-ups and bank-transfer surfaces |
| David Samuel | mobile | **9 Review/QA**, 1 Blocked | **Merged the step-up fix** (PR #29) |
| Philip Chidera | design | 1 To do, 2 In progress, 5 Review/QA, **6 Done** | Two-thirds of the sprint's completions |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **21 days** silent |

**The question for standup:** the sprint closes tomorrow with **27 of 43 leaves in a review queue that has never released a single item in 18 days**. Nothing about today's delivery changes that. What happens to those 27 tomorrow — accepted, carried, or cut?

**The three things worth knowing:**

1. **Send money works now.** PR #29 merged at 03:30 UTC and brought the step-up fix onto `main`: `stepUpUrl = "/auth/step-up"`, the token held in `WalletProvider`, and `Options(headers: {'X-Step-Up-Token': stepUpToken})` on the transfer. Five editions have opened on this being one merge away. It is done, and `POST /payments/transfer` is reachable by a real user for the first time.
2. **Virtual cards went from zero to thirteen operations in a day** — issue, list, get, rename, reveal, reveal-PIN, freeze, unfreeze, terminate, fund, withdraw, transfer history, spend history — backed by new `cards` and `card_transfers` tables and an Anchor issuance path. Card top-ups via Paystack (3 operations + webhook) and the bank-payout surface (banks, account resolution, beneficiary management, transfer status) shipped alongside. `beevia-api` also caught its db-schema pin up from 0.0.17 to **0.0.24**, which was yesterday's recommendation.
3. **The review queue absorbed almost everything else.** Twelve items left In progress and fourteen entered review, mostly in two clusters by Ayomikun (14 transitions at 16:09 UTC, 6 more at 20:10). In progress is down to 2. With one day left, 63% of the sprint sits in a state that has never had an exit.

**If you read nothing else:** the engineering delivered a genuinely large day and the flagship capability is finally reachable. The sprint still closes tomorrow with two-thirds of its items unverified.

---

## 1. What shipped — the largest cycle of the project

**21 commits across three repos**, and the first time the API surface has moved by more than three operations in a day.

### 1.1 Virtual cards (13 operations, new)

| Route | Gate | Notes |
|---|---|---|
| `POST /cards` | step-up | Sets the card's **own 4-digit PIN**; issuance fee charged only on success |
| `GET /cards` | access token | Terminated cards excluded |
| `GET /cards/{id}` | access token | Refreshes balance from the partner |
| `PATCH /cards/{id}` | access token | Rename |
| `POST /cards/{id}/reveal` | **card PIN** | PAN/CVV/expiry, fetched on demand, never stored |
| `POST /cards/{id}/reveal-pin` | step-up | Recovers a forgotten *card* PIN using the *account* PIN |
| `POST /cards/{id}/freeze` | none | Deliberately ungated — the safety action |
| `POST /cards/{id}/unfreeze` | card PIN | |
| `POST /cards/{id}/terminate` | card PIN | Refused while the card holds a balance |
| `POST /cards/{id}/fund` / `withdraw` | card PIN | Wallet↔card; funding refunds if the partner rejects |
| `GET /cards/{id}/transfers` / `transactions` | access token | Funding history; spend history read live from the partner |

**The shipped security model differs from what the RFC proposed**, and the difference is an improvement worth recording: the proposal gated everything on the account step-up token, while the implementation gives each card its own PIN. Compromising the account step-up alone no longer exposes a card's PAN. `api-rfc.md` §4.2 has been rewritten with the full comparison.

Two proposal details did **not** ship and remain open: `reveal_ttl_seconds` (the PRD's automatic re-mask window — each client must now invent it) and the card issuer webhook, so card state is polled rather than pushed.

### 1.2 Card top-ups and bank payouts (10 operations, new)

- **Top-ups (3 + webhook):** `POST /topups/initialize` returns Paystack checkout handles; `amount` is credited to the wallet and the fee is added on top, so the card is charged `charge_amount`. `GET /topups/{reference}` verifies against Paystack when still pending — the client fallback for a missed webhook. `POST /webhooks/paystack` is HMAC-SHA512 verified over raw bytes.
- **Bank payouts (6):** `GET /wallets/banks` (cached, `?search=`), `POST /wallets/resolve-account` (the "Verifying…" step, cache-first), beneficiary rename/remove, and `GET /wallets/transfers` + `/{reference}` — the latter re-checks a pending payout against the bank, so a missed webhook cannot strand it.

Also in this cycle: `fix(kyc)` auto-provisions the NGN wallet after BVN + profile; `fix(wallets)` correlates payout webhooks by provider transfer id and reads the bank name from Anchor's nested `bank.name`; `fix(queues)` hyphenates jobIds for BullMQ.

### 1.3 The step-up fix, merged

`beevia-mobile` PR #29 (David, **27 Aug 03:30 UTC**) merged `BVA-I187`; the branch is now deleted. Verified on `origin/main`:

| Requirement | State on `main` |
|---|---|
| `/auth/step-up` called | ✅ `const stepUpUrl = "/auth/step-up";` |
| Token retained | ✅ `_stepUpToken` in `WalletProvider` |
| `X-Step-Up-Token` sent | ✅ `Options(headers: {'X-Step-Up-Token': stepUpToken})` |

This closes a finding first raised on 21 August. `POST /payments/transfer` is now reachable end to end.

---

## 2. Spec and document updates made this cycle

The audit found **23 undocumented routes and 10 proposals that had shipped** — the largest drift since this pipeline began. All resolved.

| File | Change |
|---|---|
| **`openapi.yaml`** | +23 operations: 13 Cards, 3 Top-ups, 6 Wallets, 1 Webhook. New `Cards` and `Top-ups` tag sections, `CardId`/`BeneficiaryId` parameters, a `CardOk` response, and 15 schemas (`Card`, `CardSecrets`, `CardTransaction`, `CardTransfer`, `Topup`, `Bank`, `BankTransfer`, `ResolvedAccount`, and the request bodies). Count 108 → **131** |
| **`openapi.proposed.yaml`** | **10 shipped proposals removed** (`/cards` ×6, `/wallets/banks`, `/wallets/resolve-account`, `DELETE /wallets/beneficiaries/{}`) plus 10 orphaned components. Count 53 → **42** |
| **`api-rfc.md`** | §3 inventory: Cards 0 → **13**, Wallets 7 → **13**, new Top-ups row, Webhooks 3 → 4; total 108 → **131**, proposed 50 → 39. §4.2 rewritten from "Virtual cards do not exist" to a comparison of proposed versus shipped security models |

**Contracts were written from the controllers and DTOs, not copied from the proposals** — which mattered: the proposed `IssueCardRequest` was `{walletId, label}`, whereas the shipped body is `{pin, description}` with no wallet field. Copying the proposal forward would have produced a spec that lies.

`POST /wallets/beneficiaries` was deliberately **left in proposed** — the audit did not list it as shipped, and the controller has no POST, only GET/PATCH/DELETE.

Post-edit audit: `code=131 spec=131`, `29/29` admin, all four specs valid, no drift, no `x-beevia-*` markers.

---

## 3. Sprint 08-01 — final day

### 3.1 Status, day 18

| Status | Leaves | Share |
|---|---:|---:|
| To do | 3 | 7% |
| In progress | 2 | 5% |
| **Review / QA** | **27** | **63%** |
| Blocked | 2 | 5% |
| Done | 9 | 21% |
| **Total** | **43** | |

### 3.2 What moved

24 transitions in the window, concentrated in two clusters:

| When (UTC) | Who | What |
|---|---|---|
| 26 Aug 16:09 | Ayomikun Araoye | **14 items** In progress → REVIEW/QA |
| 26 Aug 16:19 | `Fortune Okwu` | 2 transitions |
| 26 Aug 20:10 | Ayomikun Araoye | 6 more transitions |
| 27 Aug 05:29 | Philip Chidera | BVA-I211 Language Selection Screen → Done |

Unlike the 26 August batch, **this one has code behind it**: the items moved are the cards, top-up, bank-transfer and send-money work that shipped in the same window. The board and the code agree today, which has not been true for most of this sprint.

### 3.3 The review queue, day 18

**27 leaves. Zero exits in 18 days.** Ayomikun holds 13, David 9, Philip 5.

The queue is now larger than every other state combined. Its median age reads 1 day only because 14 items arrived yesterday; the oldest — BVA-I185 "Wallet Summary Endpoint" — has been there since 14 August and its endpoint still does not exist in any form.

---

## 4. Risks

1. **The sprint closes tomorrow with 27 of 43 leaves unverified** and no exit ever recorded from that state.
2. **A large amount of money-handling code shipped in one day with no verification path.** Cards, top-ups and payouts move real money; all of it went straight into a queue that has never released anything.
3. **The client is 23 endpoints behind the API.** `beevia-mobile` has **zero** references to `/cards`, `/topups`, `/wallets/banks`, `/wallets/resolve-account` or `/wallets/transfers`. Cards exist entirely server-side.
4. **`reveal_ttl_seconds` did not ship**, so the PRD's automatic re-mask window is undefined and each client will pick its own.
5. **No card issuer webhook** — card state is polled, so a status change is only as fresh as the last read.
6. **Both admin repos at 21 days**, no commits, no branches, no owned leaves — eleventh consecutive edition.
7. **Estimation still 0/67** on the final day, so tomorrow's carry-over decision has no size data.

---

## 5. Previous recommendations — where they stand

| Recommendation from 26 Aug | Status on 27 Aug |
|---|---|
| Merge `BVA-I187` before the sprint closes | **Done.** PR #29 at 03:30 UTC; branch deleted; send money reachable. |
| Label each Done item: shipped earlier, cut, or genuinely done | **Not done.** Done went 8 → 9; no labels or comments added. |
| Record the translation decision explicitly | **Not done.** BVA-I218's "version 2" comment still stands against its Done status. |
| Agree who may move an item to Done, and require a reason | **Not done.** Two more bulk clusters yesterday, unannotated. |
| Bump `beevia-api` to db-schema v0.0.20 | **Done, and past it** — now pinned **0.0.24**. |
| `beevia-admin`, twenty days | **Not done.** Now 21. |

Two done — both of them the ones that unblocked delivery. Four open, all of them about recording decisions.

---

## 6. What I would do today

1. **Spend the last day on the review queue, not on new work.** Twenty-seven items, one day. Even a coarse triage — accepted / send back / carry to 08-02 — is worth more than any code that could land tomorrow.
2. **Exercise one real card end to end**: issue, fund, reveal, freeze, terminate. Thirteen endpoints shipped today and none has been demonstrated. The same applies to one real transfer, now that step-up is merged.
3. **Decide `reveal_ttl_seconds` before a client implements against the gap.** Either the server returns the window or every client invents a different one, and re-masking is a PRD requirement.
4. **Point the mobile work at the new surface.** The API is 23 operations ahead of the client; cards have no UI at all.
5. **`beevia-admin`, twenty-one days.** Eleventh edition.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`, cut-off 13:01 UTC) → fast-forward-only sync (**21 commits across `beevia-api` +13, `beevia-db-schema` +7, `beevia-mobile` +1**) → deterministic API/spec audit (**drift: 23 routes, 10 shipped proposals**) → spec + RFC migration (§2) → re-audit clean → this report.

**Contract sourcing.** Every new operation was written from `card.controller.ts`, `topup.controller.ts`, `paystack-webhook.controller.ts`, `wallets.controller.ts` and their DTOs, plus the `CardView` / `TopupView` / `BankTransferView` / `CardTransferView` interfaces for response shapes. Where the proposal and the implementation disagreed — most sharply on `IssueCardRequest` — the implementation won.

**Window.** 26 Aug 15:27 UTC → 27 Aug 13:01 UTC. Today's export ran earlier than usual, so this window is 21½ hours. Per the 20 Aug correction, CSV header times are the exporting machine's local MDT; `actiontime` values are UTC.

**Sources.** Board: `beevia-sprint-board-2026-08-27.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-27.json`. Code: five repos at `origin/main`. Specs: `openapi.yaml` (**131**), `openapi.proposed.yaml` (**42**), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈58% (estimate, **up from ≈50%**)

**Target 2026-09-01 (provisional) · 5 days out.** The largest movement since the rubric began, and all of it merged-to-`main` evidence.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live since 10 July, unchanged. Batch, languages and preference operations still proposed. Board marked the stack Done on 26 Aug with no code (see that edition) |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; NGN wallet now auto-provisioned after BVN + profile |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | **0.75** ↑ | **Moved.** Bank payouts now observable end to end (banks, account resolution, transfer status, beneficiary management) and card top-ups added. Ceiling: server still NGN-only via `activeNgn()` |
| 7 | Send / request / receive | 12 | **0.80** ↑ | **Moved — the capability is reachable.** Step-up merged (PR #29), so `POST /payments/transfer` succeeds for a real user. Ceiling: request/receive have no client flow; NGN only |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | **0.45** ↑ | **Moved from zero.** 13 operations live with Anchor issuance, per-card PIN, funding and spend history. Ceiling: **client has zero `/cards` references**, no issuer webhook, no `reveal_ttl_seconds` |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 21 days silent |
| | **Weighted total** | **100** | | **57.8 → ≈58%** |

Weights frozen. Scores measure **merged, reachable build evidence**. #9 is held to 0.45 rather than higher precisely because no client can reach it — the same treatment #7 received while its screens were stubbed.

**Team performance — what these figures do not measure.** Ayomikun shipped the entire backend surface and holds 13 review items; David merged the step-up fix and holds 9; Philip closed six items. Volume here reflects a release landing, not sustained daily rates, and the 20 board transitions Ayomikun made are administration rather than delivery. With 0/67 estimation points nothing is normalised.

**What this report cannot tell you:**
- **Whether any of today's 23 endpoints work.** They are verified as present and correctly specified, not as functional; no test was run and testing remains out of scope for scoring.
- Whether a real card has ever been issued, or a real transfer completed now that step-up is merged.
- What becomes of the 27 review items when the sprint closes tomorrow.
- Whether translation is descoped — ten days since the "version 2" comment.
- Velocity or scope-fit — still 0/67 estimated on the final day.
