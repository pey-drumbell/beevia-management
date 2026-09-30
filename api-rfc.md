# RFC: Beevia API Surface

| | |
|---|---|
| **Status** | Draft — for review · **updated 2026-08-05** |
| **Scope** | The complete HTTP surface of `beevia-api` (the consumer API): what exists today, and what the PRD requires that does not exist yet |
| **Companion artifacts** | [`openapi.yaml`](./openapi.yaml) — implemented, **137 operations** · [`openapi.proposed.yaml`](./openapi.proposed.yaml) — designed but unbuilt, **38 operations** (35 net-new + 3 live-endpoint modifications) · [`suggestions.md`](./suggestions.md) · [`Beevia_PRD.md`](./Beevia_PRD.md) |
| **Sibling RFC** | [`admin-api-rfc.md`](./admin-api-rfc.md) — the `beevia-admin-api` back-office service |
| **Sources** | `beevia-api/src/**/*.controller.ts`, `beevia-api/src/**/dto/*.ts`, `beevia-db-schema/src/schema/*`, `beevia-api/postman/Beevia.postman_collection.json`, `Beevia_PRD.pdf` |
| **Base path** | `/api/v1` (global prefix set in `src/main.ts`; `/i/:code` is explicitly excluded) |

> **Paths in this document.** This RFC lives at the root of the `beevia-management` workspace. Unless prefixed otherwise, every `src/`, `postman/` and `docs/` path refers to the `beevia-api/` service directory — e.g. `src/main.ts` means `beevia-api/src/main.ts`. The service repositories are unmodified by this work.

---

## 0. What changed since the last revision

Re-derived from the code on 2026-08-05. The consumer API grew from **90 to 100 operations**; nothing was removed or renamed.

| Change | Detail |
|---|---|
| **New: `/upgrade/*` (6 ops)** | A second KYC ladder for `chat_only` users who later want banking. See §5.1 — it duplicates `/kyc/*` closely enough to be worth consolidating. |
| **New: `DELETE /messages/{id}`** | **Was proposed in the last revision; now shipped.** Moved out of `openapi.proposed.yaml`. Implemented sender-only in both modes, for a reason worth reading — see §5.2. |
| **New: `POST /conversations/{id}/clear`** | Per-user `cleared_seq` watermark. Distinct from the archive/delete bulk action. |
| **New: `POST /users/me/contact-change` + `/verify`** | Phone/email change, step-up gated on initiation. |
| **New: `GET /users/{id}` is now a contact profile** | Returns relationship-scoped `phone`, `joined_at`, shared `media_count` / `payment_count`. The scoping is deliberate anti-harvesting design — see §5.3. |
| **Database extracted to a package** | Schema and migrations now ship as `@drumbell-technologies/beevia-db-schema`, consumed by both services. This is what makes a separate admin service defensible — see §2.9. |
| **New service: `beevia-admin-api`** | 42 operations. Documented separately in [`admin-api-rfc.md`](./admin-api-rfc.md). |
| **Unchanged** | FX/multi-currency, virtual cards, international KYC tier and consent management remain entirely unbuilt. `PaymentService.activeNgn()` is still there at `payment.service.ts:63`. |

---

## 1. Summary

The consumer API is **100 HTTP operations** across 18 domains, plus a Socket.IO gateway with 30 client commands and 15 server events. Chat, calling, identity verification, NGN wallets and peer-to-peer payments are implemented and coherent. The engineering conventions remain unusually consistent: one response envelope, one error filter, one validation strategy, one guard model.

Measured against the PRD, three MVP capabilities are **still absent from the codebase entirely**, and one is present in name only:

| PRD capability | State |
|---|---|
| Virtual cards (§1.2, §8.2, §10.3, Phase 4) | **Shipped 2026-08-27** — 13 operations under `/cards`, backed by `cards` + `card_transfers` tables and an Anchor issuance path. See §4.2 |
| Cross-currency conversion (§1.2, §5.2, §9 Flows 5–6) | **No code at all** — `PaymentService` hard-codes NGN via an `activeNgn()` helper |
| Two verification tiers (§1.2, §1.4) | **Local tier only** — BVN/Nigeria; no international path for USD/GBP/EUR |
| Consent management (§10.4) | **Listed as MVP, no endpoint or record** |

None of these moved in the last cycle. The ten endpoints that shipped are all chat, profile and onboarding refinements — valuable, but orthogonal to the four gaps that separate the product from its own PRD. That is the single most important thing this document says.

This RFC proposes **49 additional operations** to close those gaps and the smaller ones around them, specified to match the conventions already in use.

### How implemented and proposed are separated

**By file, not by marker.** Four spec files now cover two services:

| File | Contents | Use it for |
|---|---|---|
| [`openapi.yaml`](./openapi.yaml) | **100 operations that exist today** in `beevia-api`. No status markers. | Client generation, contract tests. Safe to trust. |
| [`openapi.proposed.yaml`](./openapi.proposed.yaml) | **52 operations that do not exist.** Every one 404s. | Design review and planning only. |
| [`openapi.admin.yaml`](./openapi.admin.yaml) | **42 operations that exist today** in `beevia-admin-api`. | Same, for the back office. |
| [`openapi.admin.proposed.yaml`](./openapi.admin.proposed.yaml) | **23 operations that do not exist.** | Design review only. |

The consumer proposed file's 52 operations are 49 new endpoints plus 3 restatements of live endpoints whose *request contract* needs to widen (`POST /payments/send`, `POST /payments/request`, `POST /payments/{id}/pay`) — OpenAPI has no way to express "add these fields", so the whole operation is restated in its target state under a clearly delimited **MODIFICATIONS TO LIVE ENDPOINTS** section.

An earlier draft used `x-beevia-status` / `x-beevia-prd` extensions inside a single merged file. That was dropped: the `x-` prefix that OpenAPI *requires* for extensions is visually indistinguishable from an HTTP header, and the merged file silently produced client SDKs containing 50 dead methods. Splitting removes both risks, and makes shipping an endpoint a visible file-to-file move in review rather than a one-word edit that is easy to forget. PRD traceability moved to `externalDocs`, which is first-class OpenAPI and unmistakably not a header.

The tables in §6 and §7 below are the human-readable view of the same split.

---

## 2. Conventions the API already follows

These are descriptive, not aspirational — they are enforced in code today, and every proposed endpoint in §7 conforms to them.

### 2.1 Response envelope

`ResponseInterceptor` wraps every non-webhook JSON response:

```jsonc
{ "success": true, "message": "Wallets", "data": [...], "meta": {...}, "timestamp": "2026-07-10T12:00:00.000Z" }
```

`AllExceptionsFilter` owns the error shape:

```jsonc
{ "success": false, "message": "Insufficient funds.", "error": "insufficient_funds", "timestamp": "..." }
```

Two routes opt out via `@SkipResponseInterceptor()` — partner webhooks (which return a bare `{ received: true }`) and the `/i/:code` HTML landing page.

### 2.2 Casing asymmetry

**Requests are camelCase; responses are snake_case.** The Zod schemas define camelCase inputs (`recipientPhone`, `signedPrekeySig`); `camelToSnake` converts only on the way out. This is deliberate and consistent, but it is a real footgun for client authors and is not stated anywhere outside the Swagger preamble — see `suggestions.md` §3.

### 2.3 Private-field stripping

`pin_hash`, `otp_hash`, `bvn`, `nin` and `password` are removed from anywhere in the response tree, with per-route additions available through `@PrivateFields([...])`.

### 2.4 Validation

Per-route Zod schemas via `ZodValidationPipe`, with parallel `@ApiProperty`-decorated classes existing solely so Swagger renders an accurate request schema. Validation failures return `400` with `error: "validation_error"` and a `details[]` array of `{ path, message }`.

The duplication between the Zod schema and the DTO class is a maintenance hazard — nothing enforces that they stay in sync. See `suggestions.md` §1.

### 2.5 Authentication and step-up

`JwtAuthGuard` is global; `@Public()` opts a route out. `StepUpGuard` demands `X-Step-Up-Token` and is applied to exactly four routes today:

- `POST /payments/send`
- `POST /payments/{id}/pay`
- `POST /wallets/withdraw`
- `DELETE /users/me`

The guard cross-checks the step-up token's `sub` against the session user, which correctly prevents token transplant.

Note the asymmetry: `accept` and `decline` are *not* step-up gated. That is defensible — accepting moves money toward the caller, declining returns it to the sender — but it is an implicit policy that should be written down rather than inferred.

### 2.6 Money

Major-unit decimal strings (`"2500.00"`), `numeric(20, 8)` in Postgres, `decimal.js` with `ROUND_HALF_EVEN` in code. Floats are never used. This is done well.

### 2.7 Pagination

`page` / `limit` query parameters; `meta` in the envelope. The shape emitted is:

```jsonc
{ "total": 42, "current_page": 1, "limit": 20, "total_pages": 3, "has_next_page": true, "has_prev_page": false }
```

**The Postman collection documents a different, stale shape** (`{ total, page, limit, pages }`). The code is correct; the examples are wrong.

Chat history does not use this scheme — it uses `afterSeq` / `beforeSeq` cursors with `has_more`, which is the right choice for an append-only log. The two schemes coexisting is fine, but the divergence is undocumented.

### 2.8 Transport duality

WebSocket is the primary chat transport; REST is the documented fallback. Every REST chat route wraps the same service the gateway calls — `ConversationsHttpController` and `MessagingGateway` share `ConversationsService`, `MessagesService`, `ReceiptsService`, `ReactionsService`. There is no parallel business path. This is the single best architectural decision in the codebase and should be protected: any new chat capability must land in the service, not in one transport.

The two transports are **not** at parity, though — see §6.9.

### 2.9 The database is now a shared package

Schema and migrations were extracted to `@drumbell-technologies/beevia-db-schema` and are consumed by both `beevia-api` and `beevia-admin-api`. Both services import the same table definitions and enums; neither owns a private copy.

This is the decision that makes a separate admin service defensible rather than reckless. The usual failure mode of splitting a fintech back office into its own deployment is two divergent definitions of the same money — and the package removes that for the *schema* layer. It does **not** remove it for the *service* layer: `ResponseInterceptor`, `AllExceptionsFilter`, `ZodValidationPipe` and the pagination helper are duplicated source files in both repositories. See `admin-api-rfc.md` §4.5.

---

## 3. Domain inventory

Consumer API only. The admin service is inventoried in [`admin-api-rfc.md`](./admin-api-rfc.md) §3.

| Domain | Implemented | Proposed | Notes |
|---|---:|---:|---|
| Platform | 1 | 2 | Only a static root route today; no real health probe |
| Auth & Onboarding | 13 | 3 | Session listing/revocation missing |
| KYC | 6 | 3 | Local tier only. `POST /kyc/entrust/webhook` is counted under Webhooks |
| **Upgrade** | **6** | 0 | **New.** Parallel KYC ladder for chat_only → chat_banking |
| Users | 14 | 7 | +2 contact-change. No consent, limits, deletion-status or export surface |
| Contacts | 2 | **1** | **No longer complete.** `POST /contacts/sync` now accepts 25,000 entries but resolves only the first 500 inline, queueing the rest with **no completion signal** — proposed `GET /contacts/sync/status` |
| Devices & Keys | 6 | 0 | Complete |
| Invites | 3 | 0 | Complete (no dispatch, by design) |
| Currencies | 1 | 0 | Complete |
| Wallets | **13** | 5 | **+6:** bank list, account resolution, beneficiary rename/remove, and payout listing/status. Bank-transfer payouts are now observable end to end |
| **Top-ups** | **3** | 0 | **New.** Card funding of the NGN wallet via Paystack: initialize, list, status |
| FX | **0** | 3 | Does not exist |
| Payments | **9** | 4 | Direct transfer + recipient picker shipped 17 Aug. Still no read path — no `GET /payments`. (Plus the 3 live-endpoint modifications counted below.) |
| Cards | **13** | 0 | **New, and larger than proposed.** Issue, list, get, rename, reveal, reveal-PIN, freeze, unfreeze, terminate, fund, withdraw, transfers, transactions. Each card carries its **own 4-digit PIN**, a model the proposal did not anticipate |
| Chat (REST) | 19 | 0 | +2 clear, delete. Message deletion now shipped |
| Calls | 5 | 0 | Complete |
| Attachments | 2 | 1 | No single-attachment download presign |
| Upload | 5 | 0 | Public, permanent objects — distinct from Attachments (encrypted, presigned-only) |
| Translate | **7** | **1** | **+6 (2026-09-10):** the language-preference surface — `GET /translate/languages`, plus app-wide and per-conversation preferences with precedence. **−4 proposed:** `/translate/languages` moved, and all three proposed preference operations shipped under `/translate/preferences` instead. Only `/translate/batch` is left proposed, and it is probably obsolete (§5.5a). The engine itself is still a stub (§5.5) |
| Notifications | 5 | 0 | Complete |
| Support | **0** | 4 | Does not exist. Includes `POST /payments/{id}/dispute`, listed under §7.2 but tagged Support |
| Webhooks | **4** | 1 | **+1:** `POST /webhooks/paystack` for card top-ups. Card issuer callback still missing |
| **Total** | **137** | **35** | +3 live-endpoint modifications = 38 operations in the proposed file |

---

## 4. The four structural gaps

### 4.1 Cross-currency movement does not exist

This is the most consequential finding.

`PaymentService.send()` and `PaymentService.request()` both begin by calling a private `activeNgn()` helper and use the returned currency row unconditionally:

```ts
const currency = await this.activeNgn();
const senderWallet = await this.requireWallet(initiatorId, currency.id);
await this.requireWallet(recipient.id, currency.id);   // recipient must be able to receive
```

There is no `sourceWalletId` in `sendMoneySchema`, no `currencyCode` in `requestMoneySchema`, no rate lookup, no quote, no conversion, and no FX column on `payments` or `ledger_entries`. A transfer can only ever be NGN → NGN.

The infrastructure *anticipates* this and then stops short. `provider_capability` already declares `exchange_rate`; `ProviderResolverService.getProviderForCapability()` can already route it; the `payment_provider` enum already reserves a second rail for USD/GBP/EUR; `currencies` already seeds all four codes with an `is_active` gate. Everything is in place except the feature.

Meanwhile the PRD treats multi-currency as *the* differentiator — "Multi-Currency by Design", "conversion happens automatically and transparently, with the exchange rate always confirmed before any money moves" — and Flows 5 and 6 spell out rate-lock semantics precisely enough to implement directly:

- The sender picks a source wallet at send time; the rate locks **at the sender's confirmation**.
- For requests, the requester names the amount and currency they want to *receive*; the payer picks their own source wallet, and the rate locks **at the payer's confirmation, not when the request was created**.
- The requester sees a *non-binding* preview of the payer's likely cost while composing.

Proposed: `GET /fx/rates`, `POST /fx/quotes`, `GET /fx/quotes/{id}`, plus `sourceWalletId`/`quoteId` on send, `currencyCode` on request, and a body on `POST /payments/{id}/pay`. The quote object is what makes "the rate the user saw is the rate the ledger applied" auditable rather than merely intended.

### 4.2 Virtual cards — shipped 2026-08-27, on a different security model

This gap is closed. Thirteen operations shipped under `/cards`, backed by `cards` and `card_transfers` tables and an Anchor issuance path: issue, list, get, rename, reveal, reveal-PIN, freeze, unfreeze, terminate, fund, withdraw, transfer history and spend history.

**The shipped design differs from what this RFC proposed, and the difference is the interesting part.** The proposal assumed cards would be gated by the account step-up token, like every other money-adjacent action. The implementation gives **each card its own 4-digit PIN**, set at issuance:

| Action | Proposed gate | Shipped gate |
|---|---|---|
| Issue a card | step-up | step-up (unchanged) |
| Reveal PAN/CVV | step-up | **the card's PIN** |
| Unfreeze | step-up | **the card's PIN** |
| Terminate | step-up | **the card's PIN**, and refused while the card holds a balance |
| Fund / withdraw | not proposed | **the card's PIN** |
| Recover a forgotten card PIN | not proposed | step-up — the account PIN recovers the card PIN |
| Freeze | no gate | no gate (unchanged) |

Both designs keep freeze ungated, for the reason the proposal gave: a user reacting to a suspected compromise should never be slowed by a prompt. The per-card PIN is a stronger model than proposed — compromise of the account step-up alone does not expose a card's PAN — at the cost of one more secret for the user to remember, which is what `POST /cards/{cardId}/reveal-pin` exists to handle.

Two proposal details did **not** ship and remain open:

- **`reveal_ttl_seconds` is absent.** The PRD requires automatic re-masking after a fixed window; the shipped `CardSecrets` response carries no TTL, so each client must invent that window itself.
- **No issuer webhook.** `POST /webhooks/cards` is still proposed; card state changes are read by polling the partner rather than pushed.

### 4.3 Only one verification tier exists

The PRD defines two independent tiers — local (NGN) and international (USD/GBP/EUR) — each unlocking the wallets relevant to it. The codebase implements the local tier thoroughly: email verification, BVN lookup, BVN ownership proof by face or record, KYC profile, document verification via workflow run and webhook.

There is no international path, and — more immediately actionable — **no way to ask what tier the user has reached or what is outstanding**. The only signal is `kyc_level`, an opaque integer on `/auth/me`. A client cannot render a verification hub, cannot tell the user why USD is greyed out, and discovers the gate only by calling `POST /wallets` and reading `bvn_required` / `kyc_profile_required` / `provider_not_implemented` back as *errors*.

Proposed: `GET /kyc/status` (per-tier state and unlocked currencies), `GET /kyc/requirements?currency=` (ordered outstanding steps), `POST /kyc/international/start`.

### 4.4 Payments have no read path

`POST /payments/send`, `POST /payments/transfer` and `POST /payments/request` return a payment object exactly once. After that, the only handles on it are the `{id}` action routes. There is no `GET /payments` and no `GET /payments/{id}`.

The August direct-transfer work made this worse rather than better: `POST /payments/transfer` settles immediately and is idempotent on `idempotencyKey`, but with no read path a client that loses the response cannot confirm whether the transfer landed — its only recovery is to replay the same key and rely on the idempotent return. That works, but it means correctness now depends on the client having persisted a key it may never see again.

The consequences are concrete:

- A client that cold-starts, reinstalls, or drops the response cannot rediscover its pending sends and requests.
- The countdown the PRD explicitly requires — *"a visible countdown shows how long I have to respond before funds return to the sender"*, with *"escalating visual urgency in the final hour of the 24-hour window"* — cannot be rendered after a restart, because `expires_at` is unreachable.
- The `payment_card` message type carries only a `ref_id`. Resolving that reference to a payment is impossible.
- Push notifications for payment events give the client an id and nowhere to take it.

This is a small amount of work relative to its impact and is the highest value-per-line item in this RFC.

---

## 5. Smaller gaps worth naming

**No preview before confirmation.** PRD Flow 5 requires insufficient funds to be *"blocked with clear message **before** confirmation"*, and the sender to *"see the converted amount and exchange rate before confirming"*. Today the only way to discover either is to submit the real send — which means the user has already been prompted for their PIN and issued a step-up token. `POST /payments/send/preview` fixes the ordering.

**No bank directory or account resolution.** `POST /wallets/withdraw` requires a `bankCode`, but nothing tells the client what codes exist, so the mobile client must hard-code a NIP bank list that drifts. Worse, `account_resolution` is a *declared provider capability with no endpoint*: the account name is returned only in the withdrawal receipt, i.e. after the debit. A user cannot confirm who they are paying before paying them, which sits awkwardly against the PRD's "increased risk of fraud and payment mistakes" framing.

**No withdrawal status.** `POST /wallets/withdraw` returns `status: "pending"` and a reference; settlement arrives asynchronously on the partner webhook. Nothing lets the client ask what happened. The error path already tells users to quote a reference number to support — there is nowhere to look it up.

**No transaction detail.** PRD Flow 4 ends with "tap any transaction to see full detail". The list row *is* the full representation. There is no counterparty, fee breakdown, provider reference, or status timeline — which is also exactly what a dispute needs.

**No limits anywhere.** The PRD names "inconsistent user control across platforms" as a gap Beevia solves: "users want to set limits, get alerts, and control who they transact with. Most apps treat these as afterthoughts." No limit is surfaced or settable, so the client cannot pre-empt a limit rejection.

**No consent record.** §10.4 lists Consent Management as an MVP feature — revoking location, biometrics and translation independently, with dependent features disabled until consent is restored — and Phase 4 calls for consent logging and audit trails. There is no consent table, endpoint, or log.

**No dispute or support surface.** §7.4 tracks "Dispute Resolution Time — 90% within 72 hours" and "Financial Partner Escalations" as compliance KPIs, and §8.3 commits that a user is never told to contact the partner directly. Neither the promise nor the metric is instrumentable today.

**No deletion status — and, since 2026-08-06, nothing left to build it on.** `DELETE /users/me` returns `{ deleted: true }` synchronously, but partner-side deletion is asynchronous. Flow 8 explicitly requires that a partner delay surface as *"deletion in progress"*, "not a silent failure", and §7.4 tracks completion within 5 days.

> **Correction.** Every previous edition of this RFC closed this item by noting that "the `user_status` enum already has a `deleting` state with nothing reading it" — i.e. that the hard part was already done. **That is no longer true, and has not been since migration `0027` on 2026-08-06**, which renamed the value to `deactivated` and reassigned it to the admin deactivate path. `AccountDeletionService` writes `deleted` directly, so an account is never observably mid-deletion. The gap is therefore one step wider than this document has been reporting for roughly four weeks: the status this feature was going to read no longer exists, and a deletion-request record is now the more likely design.

**No health probe.** `GET /` returns a static `"Hello World!"` and stays 200 with Postgres down. There is nothing for a load balancer or orchestrator to key on, against a 99.9% uptime objective.

**Translation is stateless only — and does not translate.** §8.1 requires opt-in translation "set per conversation **or globally**". `POST /translate` is a one-shot call with the target language supplied every time, so the preference lives only in client storage and does not survive reinstall or follow the user to a new device. There is also no supported-language list (so no validated picker) and no batch endpoint (so opening a thread with auto-translate on means one HTTP round trip per visible message). **On top of all of that, no provider is connected at all — see §5.5.**

~~**Message deletion is modelled but unreachable.**~~ **Closed 2026-08.** `DELETE /messages/{id}` shipped — see §5.2 below.

---

## 5A. Notes on the work that shipped this cycle

Design decisions worth recording, because each one constrains what can be built next. The list started as three notes on the ten endpoints that shipped in the 2026-08-05 cycle and has grown as later cycles added their own; each subsection is dated where it was added or revised.

### 5.1 `/upgrade/*` duplicates `/kyc/*` and should converge

The upgrade ladder is a near-copy of the KYC ladder with different entry conditions:

| Step | KYC path | Upgrade path |
|---|---|---|
| Email code | `POST /kyc/email` | `POST /upgrade/email` |
| Verify email | `POST /kyc/email/verify` | `POST /upgrade/email/verify` |
| BVN lookup | `POST /kyc/bvn` | `POST /upgrade/bvn` |
| Verify BVN | `POST /kyc/bvn/verify-ownership` | `POST /upgrade/bvn/**verify**` |
| Profile | `POST /kyc/profile` | `POST /upgrade/profile` |
| Progress | *(none)* | `GET /upgrade/status` |

The separation is defensible — entry conditions, resumability and error codes genuinely differ (`onboarding_incomplete`, `already_upgraded`), and the upgrade profile omits `email` and makes `gender` optional. But three things are worth flagging:

1. **The verify step has a different path segment** (`/verify` vs `/verify-ownership`) for identical semantics and an identical request schema. That is a gratuitous difference a client author will trip on.
2. **`phone` as a BVN ownership method is still accepted by both schemas and implemented by neither**, returning `method_unavailable` at runtime. The same defect is now duplicated.
3. **`GET /upgrade/status` is the progress endpoint this RFC asked for** (§7.4, `GET /kyc/status`) — but scoped only to the upgrade path, so a user who chose `chat_banking` at signup still has no way to query verification progress. Two endpoints answering "how far through verification am I?" for two cohorts is worse than one answering it for both.

**Recommendation:** keep the distinct entry points, but converge the ladder onto one set of step routes and one status endpoint that reports for either cohort.

**Update 2026-09-01 — the ladders have now diverged further, in a way that argues the same point.** `POST /upgrade/profile` gained a precondition the KYC profile does not have: the BVN must already be verified, or the call fails `400 bvn_required`. The fix is correct — provisioning is enqueued from the profile step, so accepting a profile on an unverified BVN returned a 200 that looked like a completed upgrade while no account was ever opened. But it now exists on one of the two ladders only, and `POST /kyc/profile` still has no equivalent guard. Both schemas were also widened the same day to accept `gender` case-insensitively (`Male` → `male`), which is the second correction applied twice because the code is duplicated. Converging the ladder would have made both of these one change instead of two.

**Update 2026-09-02 — still one-sided, and the class of bug it fixed has reappeared one layer down.** `POST /kyc/profile` was checked again today and still accepts a profile on an unverified BVN, still returns 200, and still leaves `maybeProvision()` to no-op. Second consecutive edition reporting it; the fix is a five-line copy of a guard already written on the other ladder.

Separately, today's provisioning work introduced a *new* silent-success path of exactly the same shape, and it is worth understanding as a category rather than an incident. `WalletProvisioningService` now refuses to connect an Anchor customer that another Beevia user already holds, throwing `400 anchor_customer_claimed` — the right guard, and it protects a real invariant (two users sharing one Anchor deposit account would mix funds). But **it throws inside the queued provisioning job, not inside the request.** `maybeProvision()` only ever enqueues. So a user whose BVN is already linked to another account gets a `200` from `/upgrade/profile`, sees a completed upgrade, and never receives a wallet — and no client-visible error is produced at any point, because the failure happens after the response was sent.

This is not an argument against the guard. It is an argument that **the enqueue boundary is where this API keeps losing errors**: three distinct silent-200s have now been found on the same seam in two days. Nothing surfaces a failed provisioning job to the user. The durable fix is a readable provisioning state on the user — the `GET /upgrade/status` endpoint (§5.1.3) is the obvious place — carrying `failed` and a reason, so the client can say *"we could not open your account, and here is why"* rather than showing a finished upgrade with nothing behind it. That is more valuable than either individual guard.

One further note on today's changes: `anchor_customer_claimed` **replaces** `bvn_registered_elsewhere`, the code the 2026-09-01 report named. That code existed for one day and never appeared in any spec. The new guard also has different semantics — it gates on whether another *Beevia user* already claims the Anchor customer, not on whether the customer's name matches — which is the better invariant, since Anchor's own customer names are frequently test data.

### 5.2 Message deletion is sender-only in both modes — and the reason is a schema limit

The implementation notes it plainly: `deleted_for` is a *single scope on the message row*, not a per-user flag, so a recipient hiding a message has nowhere to record that. Rather than fake it, the route returns 403 to a non-sender in both modes.

That is the right call — a no-op that returns 200 would be worse. But it means **"delete for me" is unavailable to the person most likely to want it**: the recipient of an unwanted message. Making that work needs a per-user table (or a `deleted_for_user_ids` array), not a new endpoint. Worth deciding deliberately rather than inheriting the current shape by default.

Note also the query parameter is `?forEveryone=true`, whereas this RFC had proposed `?scope=sender|everyone`. The shipped form is fine; `openapi.yaml` documents the real one.

### 5.3 The contact profile's relationship-scoped `phone` is good design

`GET /users/{id}` now returns `phone` **only** when the caller and target already share a 1:1 conversation, or the caller is viewing themselves. The reasoning in the source is exactly right: any authenticated caller can pass an arbitrary id or handle, so returning it unconditionally would turn the endpoint into a number-harvesting tool.

This is the kind of thinking §4 of `suggestions.md` asks for elsewhere — worth naming because it should be the template for the proposed admin and support surfaces, where the same temptation exists at greater scale.

**Update 2026-09-03 — the same reasoning was applied again, correctly, and it changed a response shape.** `POST /contacts/sync` and `GET /contacts` now return the peer's `path` (`chat_only` | `chat_banking`) on the user object, so the client can grey out "send money" against a chat-only contact instead of discovering the restriction at submit time. The field was deliberately **not** added to the shared lean projection: search, phone lookup and the block list still return `PublicProfile` without it, because those routes accept an arbitrary handle or number and would otherwise let an enumerator harvest account attributes. A contact is a relationship the caller already had, so the disclosure is bounded by their own address book.

The spec now carries this as a distinct `ContactUserProfile` (`PublicProfile` + `path`), mirroring the code's own split rather than widening `PublicProfile` for every consumer. Note the name collision to watch: `ContactProfile` is the richer single-user shape from `GET /users/{id}`; `ContactUserProfile` is the peer inside a contact row.

**This is a contract change with no route change, which is the class of drift the daily audit cannot see** — the same class as the five `beevia-admin-api` corrections recorded on 2026-09-02. It was caught by reading the commit, not by the check. That remains the argument for having both services publish their generated OpenAPI documents.

### 5.5 `POST /translate` has never translated anything

**Recorded 2026-09-03, and it corrects an impression every previous revision of this document has left.** `TranslateModule` binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`, whose entire behaviour is to return the submitted text unchanged with `from` resolved to `auto`. No provider adapter exists anywhere in the repository, and there is no environment switch — the module has looked exactly like this since its only commit, `feat(translate): add translate module`, on 2026-07-10.

Contrast `NotificationsModule`, which uses the same port/adapter shape but selects a real FCM adapter when `FCM_SERVICE_ACCOUNT` parses and falls back to a stub otherwise. That is the pattern this module needs; connecting a provider here is currently a code change rather than configuration.

Nothing about the route is wrong: the contract, validation, envelope and the deliberate statelessness (ADR-0004) are all real and stable to build a client against. What is wrong is reading "`POST /translate` is live" — which this document, `openapi.yaml` and every status report have said since July — as "the product can translate a message". It cannot, and the distinction matters now because the sprint that started on 2026-09-03 is a translation sprint whose client-side stories assume a working engine underneath.

The implemented spec now states this plainly on the operation.

#### 5.5a Correction, 2026-09-08 — the sequencing conclusion above was wrong

**This section previously ended: "connecting a real provider is a prerequisite for the translation sprint, and it is not on the board."** It is not a prerequisite, and the reason is on the board — it was simply not read.

Sprint 0901's foundation story, `BVA-I228` *On-Device Translation Engine Integration*, states the design in its own acceptance criteria: *"a working on-device translation capability, so chat messages can be translated without any message content leaving the user's phone"*, integrating **iOS's native Translation framework and Android's ML Kit Translation behind one unified internal service**, for English (UK/US), French, Spanish and Mandarin, including on-device model download and offline fallback.

That is a different architecture from the one this document assumed, and it is the **right** one for this product. Server-side translation of chat requires plaintext at the server, which is precisely what E2EE forbids — the same constraint that makes the admin API's content-moderation module unbuildable (`admin-api-rfc.md` §5.1). A server-side translation provider would have been a hole in the product's central privacy claim. The team appears to have reached that conclusion; nothing in writing records it, which is why this document reached the opposite one.

Three consequences follow, and the third needs a decision rather than an edit:

1. **`POST /translate`'s stub is no longer on the critical path** for chat. It remains a live route returning its input unchanged, which is still a trap for any *other* caller, so §6.8's marker stays.
2. **Preference storage is unaffected and is now board-backed.** `BVA-I230`/`BVA-I231` (*Language Preference Storage, App-Wide & Per-Conversation*) is exactly §7.7's `/users/me/translation` and `/conversations/{id}/translation`. Those three proposed operations are still needed — a client-side engine still needs a server-side preference that survives reinstall.
3. **`GET /translate/languages` and `POST /translate/batch` are probably obsolete.** Both exist to serve a server-side engine: the language list is the provider's, and batching exists to avoid one HTTP round trip per visible message. On-device translation has no round trip to batch and its language list is the platform framework's, not the server's. They are **annotated, not deleted**, in `openapi.proposed.yaml` — nothing is built either way, no decision is recorded, and retiring a proposal on inference is how a spec starts lying in the other direction. **This is an open question for the owner**, not a finding.

Separately, `BVA-I244`/`BVA-I245` (*Static Backend-Originated Text Localization*) is a genuinely server-side translation requirement that no proposed operation covers: push-notification bodies, OTP and transaction messages rendered from per-user language preference. That is string bundles and template selection, not a translation API, and it should not be conflated with §7.7.

#### 5.5b Preference storage shipped, 2026-09-10 — and one requirement did not come with it

`BVA-I231` merged as `a08bf13`, with the schema in `beevia-db-schema` v0.0.30. Point 2 of §5.5a — "preference storage is unaffected and is now board-backed" — is now built, and it is the first code in this workstream: six operations under `/translate/preferences`, an app-wide language on `users`, and per-conversation overrides in their own table.

**Three things it does better than the proposal it replaces**, all worth keeping when the client is written against it:

1. **Precedence is returned, not recomputed.** Every conversation response carries `override`, `app_wide` and a `source` naming the winner. No client re-implements the rule, so no client can implement it differently.
2. **A derived default is never persisted.** With no explicit choice, the answer comes from `Accept-Language` (or `?deviceLanguage`, which wins), and reading it does not write it. `is_explicit` distinguishes "you chose this" from "we guessed", so a later OS language change is still honoured and a picker does not show a phantom selection. `es-MX` collapses to `es`, `en-AU` to `en-US`, and a quality-ordered header is walked in order — a device's second choice beats the fallback.
3. **Clearing an override is expressible.** `language: null`, or `DELETE`, and `language` is *required* — so an empty body is a `400` rather than a silent clear.

**What did not ship is the PRD's actual requirement.** §8.1 asks for translation that is *"opt-in, set per conversation or globally"*. What shipped stores a **target language**, and nothing else. There is no `enabled` flag at either scope — the proposal had one at both — so the server always resolves *some* language and there is no way to say "do not auto-translate this thread". `is_explicit` is not that flag; it says the user picked a language, not that they want translation on.

So the opt-in half of an opt-in feature still lives only in client storage, which is the exact problem `/users/me/translation` was proposed to solve. **The fix is small and the route now exists**: add `enabled` to `AppWideLanguage` and a nullable `enabled` to the conversation override, alongside `language`. Doing it before the mobile client is written against these routes costs a migration; doing it after costs a contract change.

The consent gate the proposal also described (`translation` scope) remains unbuildable — consent management is still entirely absent (§1).

### 5.6 `POST /webhooks/anchor` acknowledged every real delivery without processing it

**Recorded 2026-09-04, from the fix that landed on 2026-09-03** (`fix(webhooks): process real Anchor deliveries`). Anchor's real webhooks arrive as `{ id, type, attributes, relationships }` at the top level; its test probes wrap the same object under `data`. The handler read everything from `payload.data`, so a real delivery produced no `type`, hit the unknown-type guard, and returned `200` without doing anything. The commit message reports the event inbox confirming it: **only wrapped test probes were ever recorded.**

The window is the endpoint's whole life — introduced 2026-06-28, fixed 2026-09-03, roughly **sixty-seven days**. Everything downstream of the callback was affected: deposit crediting, payout settlement, virtual-account linking, and card events.

Three things make this worth more than a changelog line.

**It is the exact failure mode this document keeps naming, on the highest-stakes route in the API.** A `200` that means "received" and never "processed" cannot distinguish a handled event from a silently dropped one, and here the two were indistinguishable for two months. §4 already argues that failed provisioning surfaces nowhere; this is the same absence one layer down, on money settlement.

**Tests did not and could not catch it**, because the fixtures were built from the same wrapped shape the probes send. The bug lived in the gap between the provider's documented example and its actual delivery, which is precisely where integration tests written from the documentation cannot reach. The fix adds fixtures in both shapes.

**It bounds what the ledger can be trusted to contain.** Any reasoning about deposits or payouts settling before 2026-09-03 should assume the webhook path contributed nothing, and reconciliation runs over that period will surface it as real discrepancies rather than tooling noise — which is the correct outcome, and worth expecting rather than discovering.

### 5.7 Payouts now source from a pooled FBO account

`feat(treasury): sweep deposits to the pool + fund payouts from it` (2026-09-04) moves NGN payouts to draw on a pooled For-Benefit-Of account rather than the paying user's own virtual account, and sweeps each credited deposit from the user's VBA into that pool via an instant Anchor `BookTransfer`. The motivation is sound and specific: a user can withdraw money the ledger says they own even when it physically landed in another customer's VBA.

**No HTTP contract changes**, which is why the audit sees nothing — the whole change is behavioural, behind `POST /wallets/payout` and the deposit webhook.

Two properties worth recording:

- **It is off until configured.** Both behaviours are guarded on `ANCHOR_POOL_ACCOUNT_ID`; unset, payouts still draw on the VBA and no sweep runs. The rollout is therefore a config change, not a deploy, which also means the "before" and "after" states can coexist across environments.
- **A failed sweep is deliberately non-fatal.** The money is already safe in the VBA and the ledger is already credited, so a sweep failure alerts (`deposit_sweep_failed`) and defers to reconciliation rather than failing the deposit. That is the right trade, and it makes the aggregate reconciliation endpoint load-bearing rather than merely informational.

The interaction to watch is cross-service: the admin API's per-user reconciliation compares a user's wallet balance against the balance on *their own* Anchor account, which sweeping empties. See `admin-api-rfc.md` §3.10 — the two commits landed within half an hour of each other in different repositories.

### 5.8 The self view now carries `email`, and it is absent rather than null (2026-09-16)

`feat(auth): return the user's email when they have one` adds an optional `email` to `PublicUser`, the shape behind `GET /auth/me`, `POST /auth/otp/verify` and `POST /auth/pin`. **No operation was added or removed** — the surface stays at 137 — so the route-level audit sees nothing; `openapi.yaml`'s `User` schema was updated in place.

The one thing a client author has to know: **the key is omitted when there is no email, not set to `null`.** Every other optional field on this schema (`first_name`, `last_name`, `path`) is nullable, so `email` is the sole field on the self view where `'email' in user` and `user.email !== null` disagree. An empty stored value is folded into "none", so a blank string can never arrive as a value. Chat-only accounts routinely have no email, making the absent case the common one rather than an edge.

The choice itself is defensible — one less state to tell apart — but it is an inconsistency inside a single schema, and this API's main virtue so far has been that its conventions do not have exceptions. Worth either widening to the other blanks or narrowing this one, rather than leaving one field with its own rule.

---

### 5.9 Reporting a conversation now carries evidence and a block, and the client has not caught up (2026-09-17)

`feat(chat): carry disclosed messages and an optional block on a report` widens `POST /conversations/{id}/report` and the `conversation.report` socket command. **No operation was added or removed** — the surface stays at 137 — so the route-level audit sees nothing; `openapi.yaml`'s `ReportConversationRequest` was updated in place and a `ReportedMessage` schema added.

The body was `{ reason? }`. It is now `{ reason?, messages: ReportedMessage[] (≤20, default []), blockContact: boolean (default false) }`. Both new fields default, so **every existing caller keeps working unchanged** — which is the only reason this is a widening rather than a break.

**This is the consumer half of Option B in `admin-api-rfc.md` §5.1, and it does not weaken E2EE.** The messages arrive as plaintext the reporter can already read on their own device and chose to hand over; nothing is decrypted server-side, and nothing is captured from a conversation nobody reported. Four implementation choices do the load-bearing work:

- **Report, evidence and block commit in one transaction.** A block that outlived a failed report would leave someone silently muted with nothing written down to explain why; a report whose evidence half-landed is worse than one with none. The block is written inline rather than through `UsersService.block` specifically so it can share that transaction, with the same idempotent guard — so reporting the same person twice does not fail on a block that already exists.
- **`message_count` is stored on the report, not derived from the rows.** A message deleted later cannot quietly change what the reporter consented to disclose.
- **Ordinal is the submitted position, not `sentAt`.** `sentAt` is optional and several messages can share one, so it cannot order an exchange a moderator has to read.
- **`blockContact` on a group is refused (`block_requires_direct`)**, not guessed at and not silently dropped. There is no single contact to block, and ignoring the toggle would leave the reporter believing they had blocked someone they had not. Note the consequence for a client author: the *whole report* is rejected, so a group report must not send the flag at all rather than sending `true` and ignoring the error.

**The gap worth naming: the Flutter client has not shipped its half.** As of 2026-09-18 `chat_service.dart` still posts `data: {"reason": reason}` — no `messages`, no `blockContact` — on `main` and on the unmerged `BVA-I239` branch alike. The board item for the client side (`BVA-I254`, "Update Report Sheet, Add Message Count, Build Confirmation") is in REVIEW/QA. So the server accepts up to 20 disclosed messages, the admin queue is built to display them, and every report filed by today's app arrives with `message_count: 0` and an empty `messages` array. The capability exists end-to-end on the server and nowhere on the device that is supposed to originate the consent.

### 5.10 Phone numbers are now parsed rather than pattern-matched, and the inbox gained ordering rules (2026-09-25)

Two merges on 24 September — `feat/contact-sync-normalisation` (#56) and the two inbox fixes (#53, #54) — changed the contract of **nine operations without adding, removing or renaming one**. The surface stays at 137, so the route-level audit reports `beevia-api` clean; `openapi.yaml` was updated in place. Third consecutive cycle in which the most consequential change was invisible to a route diff (`suggestions.md` §5.4).

**1. A phone may now be typed the way people actually type it.** `POST /auth/register`, `/auth/otp/request`, `/auth/otp/verify`, `/auth/login`, `/users/lookup` and `/contacts/sync` previously required strict E.164. They now accept a local/national form (`08089421407`) alongside `+2348012345678`, and each grew an optional `countryCode` region hint; where it is omitted the caller's own account country is used. Normalisation happens in the schema, at object level, so a handler never sees an unnormalised number. A new `TypedPhone` schema models the input; responses continue to return the canonical `Phone`.

This is a data-integrity fix, not a convenience feature. The retired regex `^\+[1-9]\d{6,14}$` accepted `+23408089421407` — a national-format number with its trunk `0` pasted after the country code — which E.164 says is the same person as `+2348089421407`. A unique index on the string stored both. `src/common/phone.util.ts` now delegates to `libphonenumber-js` and repairs that specific shape explicitly. See `suggestions.md` §5.2, closed by this change.

**The one route left out is the one that moves money.** `payments.dto.ts` still declares its own `z.string().trim().min(6).max(20)` and imports nothing from `phone.util.ts`, so `POST /payments/send` and `POST /payments/request` are now the only phone inputs in the service that are neither validated nor normalised — and a payer who types a local number there gets no resolution. Both fields carry the looseness as a `description` in `openapi.yaml` so no client is misled. `suggestions.md` §3.6, escalated.

**2. `GET /conversations` has listing rules that were never written down.** A direct conversation is now listed only once a message has been sent in it — creating one does not put it in the inbox — while groups are listed from the moment the caller is added. A client must therefore navigate off the create response rather than waiting for the list to catch up. Rows are ordered by a new `last_message_at`, and `last_message` is `null` in three distinct cases: the previewed message was deleted for everyone, the caller deleted it for themselves, or it sits at or below the caller's `cleared_seq`. `last_message_at` deliberately survives that deletion so a row keeps its place rather than falling to the bottom of the inbox.

**3. Three response fields the server had always sent were missing from the spec.** `last_message_at` is new; `hidden_at` and `cleared_seq` are not — `conversations.service.ts` has been returning both on every conversation row, and `openapi.yaml`'s `Conversation` schema never listed them. All three are now documented. A client that generated its models from the spec has never had access to the clear-chat watermark the API was already sending it.

### 5.11 Escrowed send reaches the socket — and the client has been bypassing escrow (2026-09-28)

`beevia-api` #57 (`feat/ws-payment-send`, merged 25 September) added two socket commands, `payment.step_up` and `payment.send` (§6.9). **No REST route was added, removed or renamed**, so the route-level audit is clean for the fourth consecutive cycle in which the day's most consequential change was not a route. `openapi.yaml` was updated in its prose only — the Transports section, `POST /auth/step-up` and `POST /payments/send` — because the file does not model socket commands.

**1. The PIN gate now lives on the connection for socket spends.** ADR-0003's step-up token is an HTTP header; the gateway previously excluded every debiting command for that reason. The token is now presented once per socket and arms it until the token's *own* expiry — not refreshed by activity, not shared with a second connection. Verification moved into `TokenService.verifyStepUp`, which `StepUpGuard` also calls, so the header and socket paths cannot drift. This is a sound shape. One property to keep in mind: an armed socket may spend repeatedly until expiry (default 5 minutes), where the header path requires the token on every request — equivalent in practice while the TTL stays short.

**2. The reason for the change is a product finding, not a transport one.** The commit records that all six sends on production went through `POST /payments/transfer`, which credits the recipient immediately with no accept step and no 24-hour return. That is the endpoint the mobile client's in-chat Send posts to (`wallet_service.dart`, `walletTransferUrl`). The escrowed path — the PRD's *Transfer Acceptance & Escrow* (§10.2; Flow 5; §11 Phase 3, "universal transfer acceptance and escrow mechanic") — has existed on the server since the payments module shipped and **has never been used by a real payment**. Previous revisions of this RFC and the status reports described the client's use of `/payments/transfer` as expected; it is not what the PRD asks a chat send to do.

**3. The client work to use it exists, on an unmerged branch.** `beevia-mobile` `origin/update-fixes` (2 commits, 24 and 27 September) wires `payment.step_up` → `payment.send` from the chat send flow. Until it merges, `main` still bypasses escrow.

**4. The new door inherits the one unparsed phone field.** `payment.send` reuses `sendMoneySchema`, whose `recipientPhone` is still `z.string().trim().min(6).max(20)` rather than `phone.util.ts` (§5.10). The socket command that finally exposes escrow to the client is therefore also the newest caller of the only un-normalised phone input in the service. `suggestions.md` §3.6.

**5. The same client branch assumes a server feature that does not exist.** `update-fixes` posts `{ "method": "biometric" }` to `POST /auth/step-up` and edits its vendored `api-docs/openapi.yaml` to declare that body. The server's `stepUpSchema` is `z.object({ pin })`; the request fails validation. The client's mock server accepts it, so the client's contract test passes. See `suggestions.md` §5.11 — this is a design decision, not a missing line, because a step-up minted on a client's word that a biometric prompt succeeded carries no factor the server can verify.

### 5.12 `X-Device-Id` is now required on six chat routes — and the client does not send it on two (2026-09-30)

`beevia-api` #60 (`feat/require-device-id`, `f1d5a40`, merged 30 September 02:55 UTC) changed the contract of **six operations without adding, removing or renaming one**: `POST /conversations`, `GET /conversations`, `GET /conversations/{id}`, `GET` and `POST /conversations/{id}/messages`, and `POST /messages/{id}/receipts`. The surface stays at 137, so the route-level audit is clean for the fifth cycle running in which the most consequential change was not a route. `openapi.yaml` was updated in place: `DeviceIdHeader` is now `required: true`, the three reads that lacked it gained a `400`, and `MessageHistory` gained `unresolved`.

**1. The change is right.** Without the header the server fell back to a message's own `ciphertext`, which is `null` for every 1:1 envelope send, so a request succeeded with rows nobody could decrypt and rendered as an empty chat. Success and total failure looked identical. A new `@DeviceId()` decorator now rejects a missing or blank header with `400 device_id_required`, and `sync` reports how many returned messages it could not resolve an envelope for (`unresolved`), logging when it is non-zero. The commit says plainly that this is deliberately strict: a caller with no registered device now gets a `400` from the conversation list.

**2. The mobile client does not send the header on two of the six.** Checked at `beevia-mobile` `origin/main` and `origin/update-fixes`:

| Route | `main` | `update-fixes` |
|---|---|---|
| `GET /conversations/{id}/messages` | sends it | sends it |
| `GET /conversations` (the inbox) | **no header** | sends it when a device id is known (`edcadef`, 29 Sep) |
| `POST /conversations` (start a chat) | **no header** | **no header** |

Messages and receipts are sent over the socket, which carries `X-Device-Id` in its handshake. So once #60 is deployed, a `main` build's inbox fails with `400`, and **starting a new direct chat fails on both branches**. The client's mock server does not enforce the header, so no client test notices. The fix is one line in `chat_service.dart`'s `createConversation`, and merging `update-fixes` covers the inbox.


---

## 6. Implemented surface

Status legend: **✅ Complete** · **🟡 Partial** — works but materially narrower than the PRD describes · **🔴 Facade** — the route is real and the behaviour behind it is not.

Auth: 🔓 public · 🔑 access token · 🔐 access + step-up token.

### 6.1 Platform

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | GET | `/` | 🔓 | 🟡 Static string; not a real probe |

### 6.2 Auth & Onboarding

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | POST | `/auth/register` | 🔓 | ✅ |
| | POST | `/auth/login` | 🔓 | ✅ |
| | POST | `/auth/otp/request` | 🔓 | ✅ Cooldown enforced |
| | POST | `/auth/otp/verify` | 🔓 | ✅ Returns token pair + user; redeems invite code |
| | POST | `/auth/refresh` | 🔓 | ✅ Rotating; old session revoked |
| | GET | `/auth/me` | 🔑 | ✅ `email` present only when set — key absent, not null (§5.8) |
| | POST | `/auth/logout` | 🔑 | ✅ Idempotent |
| | POST | `/auth/pin` | 🔑 | ✅ `currentPin` required to change |
| | POST | `/auth/pin/verify` | 🔑 | ✅ Does not mint step-up |
| | POST | `/auth/step-up` | 🔑 | ✅ |
| | GET | `/onboarding/state` | 🔑 | ✅ |
| | POST | `/onboarding/path` | 🔑 | ✅ |
| | POST | `/onboarding/profile` | 🔑 | ✅ Age ≥ 16 enforced |

### 6.3 KYC

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | POST | `/kyc/email` | 🔑 | ✅ |
| | POST | `/kyc/email/verify` | 🔑 | ✅ |
| | POST | `/kyc/bvn` | 🔑 | ✅ Lookup only |
| | POST | `/kyc/bvn/verify-ownership` | 🔑 | 🟡 `face` + `record`; `phone` declared but unavailable |
| | POST | `/kyc/profile` | 🔑 | ✅ |
| | POST | `/kyc/id/start` | 🔑 | ✅ Requires verified BVN |
| | POST | `/kyc/entrust/webhook` | 🔓 | ✅ HMAC-verified. Path is under `/kyc`, not `/webhooks` |

### 6.3a Upgrade (new)

Parallel ladder for `chat_only` users adopting banking. See §5.1 for why this should converge with §6.3.

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | GET | `/upgrade/status` | 🔑 | 🟡 Progress for the upgrade cohort only |
| | POST | `/upgrade/email` | 🔑 | ✅ Entry point; `onboarding_incomplete` / `already_upgraded` |
| | POST | `/upgrade/email/verify` | 🔑 | ✅ |
| | POST | `/upgrade/bvn` | 🔑 | ✅ Lookup only |
| | POST | `/upgrade/bvn/verify` | 🔑 | 🟡 Same `phone` gap as §6.3; path segment differs from KYC |
| | POST | `/upgrade/profile` | 🔑 | ✅ No `email`; `gender` optional. Since 2026-09-01 requires a verified BVN (`bvn_required`) — see §5.1 |

### 6.4 Users

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | PATCH | `/users/me` | 🔑 | ✅ |
| | DELETE | `/users/me` | 🔐 | 🟡 Synchronous ack; no progress surface |
| | POST | `/users/me/contact-change` | 🔐 | ✅ **New.** Step-up gated; sends a code to the new contact |
| | POST | `/users/me/contact-change/verify` | 🔑 | ✅ **New.** Commits the change |
| | POST | `/users/me/username` | 🔑 | ✅ Set-once |
| | GET | `/users/me/settings` | 🔑 | ✅ |
| | PATCH | `/users/me/settings` | 🔑 | ✅ |
| | POST | `/users/lookup` | 🔑 | ✅ |
| | GET | `/users/search` | 🔑 | ✅ |
| | GET | `/users/blocks` | 🔑 | ✅ |
| | POST | `/users/blocks` | 🔑 | ✅ |
| | DELETE | `/users/blocks/{userId}` | 🔑 | ✅ |
| | GET | `/users/by-username/{username}` | 🔑 | ✅ |
| | GET | `/users/{id}` | 🔑 | ✅ Now a **contact profile** — relationship-scoped `phone`, shared counts (§5.3). Declared last so static routes win |

### 6.5 Contacts · Devices & Keys · Invites · Currencies

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | POST | `/contacts/sync` | 🔑 | ✅ Max 500 entries resolved synchronously; peer carries `path` since 2026-09-03 — see §5.3 |
| | GET | `/contacts` | 🔑 | ✅ Peer carries `path` since 2026-09-03 — see §5.3 |
| | POST | `/devices` | 🔑 | ✅ |
| | GET | `/devices` | 🔑 | ✅ |
| | DELETE | `/devices/{id}` | 🔑 | ✅ |
| | POST | `/keys/prekeys` | 🔑 | ✅ |
| | GET | `/keys/by-username/{username}` | 🔑 | ✅ Consumes one OTP prekey per device |
| | GET | `/keys/{userId}` | 🔑 | ✅ Consumes one OTP prekey per device |
| | POST | `/invites` | 🔑 | 🟡 Returns share text; server dispatches nothing |
| | GET | `/invites/{code}` | 🔓 | ✅ |
| | GET | `/i/{code}` | 🔓 | ✅ HTML; outside the `/api/v1` prefix |
| | GET | `/currencies` | 🔑 | ✅ |

### 6.6 Wallets

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | GET | `/wallets` | 🔑 | ✅ |
| | POST | `/wallets` | 🔑 | 🟡 Idempotent, but only NGN succeeds |
| | GET | `/wallets/payin-details` | 🔑 | ✅ Returns object with `?walletId`, array without |
| | GET | `/wallets/beneficiaries` | 🔑 | 🟡 Read-only; rows appear only after a withdrawal |
| | GET | `/wallets/transactions` | 🔑 | ✅ Paginated |
| | GET | `/wallets/{walletId}/transactions` | 🔑 | ✅ Paginated |
| | POST | `/wallets/withdraw` | 🔐 | 🟡 NGN only; optimistic debit; no status lookup |

### 6.7 Payments

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | POST | `/payments/send` | 🔐 | 🟡 NGN-only; no source wallet, no preview |
| | POST | `/payments/transfer` | 🔐 | 🟡 **New.** Direct, non-escrow, idempotent on `idempotencyKey`; NGN-only, targets a user id |
| | GET | `/payments/recipients` | 🔑 | ✅ **New.** Banking-only search, 20 rows, no phone returned |
| | GET | `/payments/recent-recipients` | 🔑 | ✅ **New.** Distinct recent sends, 15 rows |
| | POST | `/payments/{id}/accept` | 🔑 | ✅ |
| | POST | `/payments/{id}/decline` | 🔑 | ✅ |
| | POST | `/payments/request` | 🔑 | 🟡 NGN-only; no currency selection |
| | POST | `/payments/{id}/pay` | 🔐 | 🟡 Empty body; no wallet choice, no mismatch amount |
| | POST | `/payments/{id}/cancel` | 🔑 | ✅ |

Escrow mechanics themselves are sound: a 24-hour hold scheduled through BullMQ, hold-before-write ordering so a rejected send leaves no payment row behind, idempotent expiry, and auto-return on decline or timeout.

**But no production payment has used them.** Per the #57 commit (2026-09-25), all six sends on production went through `POST /payments/transfer` — the mobile client's in-chat Send posts there — and each completed in the same millisecond it was created. The PRD's *Transfer Acceptance & Escrow* feature (§10.2, MVP Phase 3) is built on the server and bypassed by the client. See §5.11.

### 6.8 Chat, Calls, Attachments, Translate, Notifications, Webhooks

| | Method | Path | Auth | Status |
|---|---|---|---|---|
| | POST | `/conversations` | 🔑 | ✅ Direct or group |
| | GET | `/conversations` | 🔑 | ✅ |
| | GET | `/conversations/{id}` | 🔑 | ✅ |
| | PATCH | `/conversations/{id}` | 🔑 | ✅ Admin only |
| | POST | `/conversations/{id}/members` | 🔑 | ✅ Max 64 incl. creator |
| | DELETE | `/conversations/{id}/members/{userId}` | 🔑 | ✅ Remove or leave |
| | POST | `/conversations/bulk` | 🔑 | ✅ Max 100 ids |
| | POST | `/conversations/{id}/archive` | 🔑 | ✅ |
| | POST | `/conversations/{id}/clear` | 🔑 | ✅ **New.** Per-user `cleared_seq` watermark; not undone by new messages |
| | POST | `/conversations/{id}/mute` | 🔑 | ✅ `null` unmutes; omitted mutes forever |
| | POST | `/conversations/{id}/report` | 🔑 | 🟡 **Widened 2026-09-17.** Takes `messages` (≤20, reporter-disclosed plaintext) + `blockContact`. No server-side decryption — see §5.9 |
| | GET | `/conversations/{id}/media` | 🔑 | ✅ |
| | GET | `/conversations/{id}/messages` | 🔑 | ✅ Seq-cursored |
| | POST | `/conversations/{id}/messages` | 🔑 | ✅ |
| | POST | `/messages/backfill` | 🔑 | ✅ Gated by the history-sync setting |
| | DELETE | `/messages/{id}` | 🔑 | 🟡 **New.** `?forEveryone`. Sender-only in both modes — recipients get 403 (§5.2) |
| | POST | `/messages/{id}/receipts` | 🔑 | ✅ |
| | POST | `/messages/{id}/reactions` | 🔑 | ✅ |
| | DELETE | `/messages/{id}/reactions/{emoji}` | 🔑 | ✅ |
| | POST | `/conversations/{id}/calls` | 🔑 | ✅ |
| | GET | `/conversations/{id}/calls` | 🔑 | ✅ |
| | POST | `/calls/{id}/answer` | 🔑 | ✅ |
| | POST | `/calls/{id}/decline` | 🔑 | ✅ |
| | POST | `/calls/{id}/end` | 🔑 | ✅ |
| | POST | `/attachments/upload-url` | 🔑 | ✅ |
| | POST | `/attachments/{id}/finalize` | 🔑 | ✅ Size enforced from the stored object |
| | POST | `/translate` | 🔑 | 🔴 **Stub engine — returns the input unchanged.** Unchanged on 2026-09-10: `TranslateModule` still binds `TRANSLATE_PORT` to `StubTranslateAdapter`. See §5.5 |
| | GET | `/translate/languages` | 🔑 | ✅ **New 2026-09-10.** Five languages, hardcoded in `device-language.ts`. **`POST /translate` is not validated against this list** — its `to` still accepts any 2–10 character string |
| | GET | `/translate/preferences` | 🔑 | ✅ **New.** App-wide language. Falls back to `Accept-Language` / `?deviceLanguage` without persisting the derivation; `source` and `is_explicit` say which it was |
| | PUT | `/translate/preferences` | 🔑 | ✅ **New.** Leaves per-conversation overrides untouched — separate column, separate table |
| | GET | `/translate/preferences/conversations/{conversationId}` | 🔑 | ✅ **New.** Returns `override`, `app_wide` and `source`, so precedence needs no client-side rule. 403 if the caller is not a current participant |
| | PUT | `/translate/preferences/conversations/{conversationId}` | 🔑 | ✅ **New.** `language: null` clears the override — a required, explicit value, so an empty body is a 400 |
| | DELETE | `/translate/preferences/conversations/{conversationId}` | 🔑 | ✅ **New.** Identical to `PUT … null`; returns the resulting state rather than 204 |
| | POST | `/notifications/token` | 🔑 | ✅ |
| | DELETE | `/notifications/token` | 🔑 | ✅ Body-based, not path-based |
| | GET | `/notifications/preferences` | 🔑 | ✅ |
| | PATCH | `/notifications/preferences` | 🔑 | ✅ |
| | POST | `/notifications/test` | 🔑 | ✅ |
| | POST | `/webhooks/anchor` | 🔓 | ✅ HMAC over raw body; deduped. **Processed no real delivery until 2026-09-03** — envelope mismatch, see §5.6. Now also syncs card lifecycle events |
| | POST | `/webhooks/livekit` | 🔓 | ✅ JWT in `Authorization` |

### 6.9 WebSocket surface

**38 client commands** (re-counted from `@SubscribeMessage` on `origin/main`, 2026-09-28 — this line previously said 30 and had not been updated since before `conversation.clear`, `message.delete` and the six `payment.*` commands landed). Commands: `sync.bootstrap`, `sync.messages`, `number.lookup`, `conversation.{create,get,update,join,leave,archive,unarchive,mute,report,media,clear}`, `conversation.members.{add,remove}`, `conversations.{list,bulk}`, `message.{send,backfill,delete}`, `receipt.send`, `reaction.{add,remove}`, `call.{start,answer,decline,end}`, `typing.{start,stop}`, `presence.ping`, `ping`, `payment.{request,accept,decline,cancel,step_up,send}`.

**`payment.step_up` and `payment.send` (2026-09-25, `beevia-api` #57).** Until this merge the gateway carried every money command *except* the ones that debit the caller, because the step-up credential is an HTTP header and a socket message has none. #57 moves the gate onto the connection: `payment.step_up { stepUpToken }` verifies the token `POST /auth/step-up` mints (same `TokenService.verifyStepUp` the header guard now calls — one implementation, not two) and records `stepUpUntil` on that socket, set to the token's own expiry and never extended. `payment.send` takes the `POST /payments/send` body and answers `step_up_required` until the socket is armed. The arming is per socket, so a second connection is not armed by the first. `payment.pay` does not exist; paying a request stays REST-only.

**The transports are not at parity in either direction**, which is worth stating explicitly because both docs and the Postman collection imply they are:

| Capability | REST | WS |
|---|---|---|
| Typing indicators | — | ✅ |
| Presence | — | ✅ |
| Bootstrap sync | — | ✅ |
| Join / leave a room | — | ✅ |
| Explicit unarchive command | via `{archived:false}` | ✅ dedicated |
| Attachments | ✅ | — (binary never over WS, by design) |
| Payments: send (escrow), request, accept, decline, cancel | ✅ | ✅ — send since 2026-09-25, armed per socket via `payment.step_up` |
| Payments: pay a request, direct transfer | ✅ | — |
| Wallets, KYC | ✅ | — |

Typing and presence being WS-only is correct — they are ephemeral. `sync.bootstrap` having no REST equivalent is a genuine hole: a client that cannot open a socket has no single call to establish initial state.

**Parity was maintained on 2026-09-17** when reporting widened: `conversation.report` took the same `messages` / `blockContact` fields in the same commit as the REST route, by sharing one `reportFields` object between the two Zod schemas rather than copying it. That is the right shape for a dual-transport API and the first time in this file the two have been widened together (§5.9). It also caused the day's production incident — see `suggestions.md` — because `sentAt: z.coerce.date()` is a type the new Swagger version could not render.

---

## 7. Proposed surface

All 35 operations below live in [`openapi.proposed.yaml`](./openapi.proposed.yaml) with full schemas, alongside the 3 live-endpoint modifications described in §7.1 — 38 operations in the file. Each conforms to the existing conventions: `/api/v1` prefix, standard envelope, snake_case responses, camelCase Zod-validated request bodies, `JwtAuthGuard` by default, `StepUpGuard` on anything that moves money or is irreversible.

### 7.1 FX (3) — closes §4.1

| Method | Path | Auth | PRD |
|---|---|---|---|
| GET | `/fx/rates` | 🔑 | §1.2, §5.2, Flows 5–6 |
| POST | `/fx/quotes` | 🔑 | §5.2, §10.2 |
| GET | `/fx/quotes/{quoteId}` | 🔑 | Flows 5–6 |

Plus three **modifications to live endpoints**, restated in their target state under the `MODIFICATIONS TO LIVE ENDPOINTS` section of `openapi.proposed.yaml`:

| Live endpoint | Widened by |
|---|---|
| `POST /payments/send` | `sourceWalletId`, `quoteId` |
| `POST /payments/request` | `currencyCode` (the currency to *receive*) |
| `POST /payments/{id}/pay` | a body at all — `sourceWalletId`, `quoteId`, `amount` |

When one of these ships, update the operation in `openapi.yaml` and **delete** it from the proposed file — do not move the block wholesale, or the live spec will advertise fields the API does not accept.

Quotes are single-use and short-lived. Expiry returns `quote_expired` and the client re-quotes — never extend a quote in place, or the rate the user confirmed stops being the rate that settles.

### 7.2 Payments (5) — closes §4.4

| Method | Path | Auth | PRD |
|---|---|---|---|
| GET | `/payments` | 🔑 | §8.2, §10.2 |
| GET | `/payments/{id}` | 🔑 | §10.2 |
| POST | `/payments/send/preview` | 🔑 | Flow 5 + edge cases |
| POST | `/payments/request/preview` | 🔑 | §8.2, Flow 6 |
| POST | `/payments/{id}/dispute` | 🔑 | §7.4, §8.3 |

Previews deliberately require **no** step-up: they move no money, and requiring one would reintroduce the ordering problem they exist to fix. `request/preview` always returns `is_binding: false` and no quote id, keeping the PRD's non-binding-preview requirement enforceable in the UI.

### 7.3 Cards (8 + 1 webhook) — closes §4.2

| Method | Path | Auth |
|---|---|---|
| GET | `/cards` | 🔑 |
| POST | `/cards` | 🔐 |
| GET | `/cards/{cardId}` | 🔑 |
| DELETE | `/cards/{cardId}` | 🔐 |
| POST | `/cards/{cardId}/reveal` | 🔐 |
| POST | `/cards/{cardId}/freeze` | 🔑 |
| POST | `/cards/{cardId}/unfreeze` | 🔐 |
| GET | `/cards/{cardId}/transactions` | 🔑 |
| POST | `/webhooks/cards` | 🔓 |

Requires: a `cards` table, a `card_issuance` value on `provider_capability`, and an issuer adapter under `src/providers/`. No PAN or CVV is ever persisted — `reveal` proxies the issuer per call, and that route should be excluded from body logging.

### 7.4 KYC (3) — closes §4.3

| Method | Path | Auth |
|---|---|---|
| GET | `/kyc/status` | 🔑 |
| GET | `/kyc/requirements?currency=` | 🔑 |
| POST | `/kyc/international/start` | 🔑 |

`GET /kyc/status` is the cheapest item in this RFC and unblocks the verification hub immediately, independently of whether the international tier ships.

### 7.5 Wallets (8)

| Method | Path | Auth |
|---|---|---|
| GET | `/wallets/{walletId}` | 🔑 |
| GET | `/wallets/banks` | 🔑 |
| POST | `/wallets/resolve-account` | 🔑 |
| POST | `/wallets/beneficiaries` | 🔑 |
| DELETE | `/wallets/beneficiaries/{beneficiaryId}` | 🔑 |
| GET | `/wallets/transactions/{transactionId}` | 🔑 |
| GET | `/wallets/withdrawals/{reference}` | 🔑 |
| GET | `/wallets/limits` | 🔑 |

`resolve-account` needs no new integration — `account_resolution` is already a routable capability.

### 7.6 Users, privacy & sessions (10)

| Method | Path | Auth | PRD |
|---|---|---|---|
| GET | `/users/me/consents` | 🔑 | §10.4 |
| PATCH | `/users/me/consents` | 🔑 | §10.4 |
| GET | `/users/me/limits` | 🔑 | §3.2 |
| PATCH | `/users/me/limits` | 🔐 | §3.2 |
| GET | `/users/me/deletion` | 🔑 | Flow 8, §7.4 |
| POST | `/users/me/exports` | 🔐 | §6.4 |
| GET | `/users/me/exports/{exportId}` | 🔑 | §6.4 |
| GET | `/auth/sessions` | 🔑 | §8.3 |
| DELETE | `/auth/sessions` | 🔐 | §8.3 |
| DELETE | `/auth/sessions/{sessionId}` | 🔐 | §8.3 |

Session listing is a projection of the existing `sessions` table — no new storage.

### 7.7 Translation (1)

| Method | Path | Auth |
|---|---|---|
| POST | `/translate/batch` | 🔑 |

Batch reports failures **per item** rather than failing the batch, so the PRD's fallback ("original message still shown, with a clear notice") stays renderable row by row.

**Four of this section's five operations shipped on 2026-09-10**, and none of them shipped at the path proposed here:

| Was proposed | Shipped as |
|---|---|
| `GET /translate/languages` | `GET /translate/languages` — same path, different shape: an object `{ languages: [{ value, label }] }`, not a bare array, and no detection flag |
| `GET`/`PATCH /users/me/translation` | `GET`/`PUT /translate/preferences` |
| `PATCH /conversations/{id}/translation` | `GET`/`PUT`/`DELETE /translate/preferences/conversations/{conversationId}` |

The shipped surface is better than what was proposed on precedence and on clearing an override, and **short of it on one thing that matters: there is no on/off flag.** See §5.5a. `POST /translate/batch` is the only survivor, and it is probably obsolete for the on-device design.

### 7.8 Attachments, platform, support (6)

| Method | Path | Auth |
|---|---|---|
| GET | `/attachments/{attachmentId}/download-url` | 🔑 |
| GET | `/health` | 🔓 |
| GET | `/status` | 🔑 |
| POST | `/support/tickets` | 🔑 |
| GET | `/support/tickets` | 🔑 |
| GET | `/support/tickets/{ticketId}` | 🔑 |

*(`DELETE /messages/{id}` was proposed here in the last revision and has since shipped — see §5.2. It now lives in `openapi.yaml`.)*

`GET /status` returns user-facing banner copy per capability. That copy must never instruct the user to contact the partner — §8.3 is explicit that Beevia owns escalation.

The support surface is now doubly motivated: `POST /support/tickets` is the consumer-side counterpart to the admin case-notes and moderation queues, which the admin service is beginning to build. Without it, a user has no way to *originate* the thing an admin reviews.

---

## 8. Suggested sequencing

Ordered by unblocked value per unit of work, not by PRD section order.

**Phase A — read paths and state visibility.** No new integrations; unblocks client work immediately.
`GET /payments`, `GET /payments/{id}`, `GET /kyc/status`, `GET /kyc/requirements`, `GET /wallets/{walletId}`, `GET /wallets/transactions/{transactionId}`, `GET /wallets/withdrawals/{reference}`, `GET /auth/sessions` + revocation, `GET /health`.

**Phase B — pre-confirmation safety.** Removes the "submit and read the error" pattern from money flows.
`POST /payments/send/preview`, `GET /wallets/banks`, `POST /wallets/resolve-account`, `GET /wallets/limits`, `GET /status`.

**Phase C — multi-currency.** The largest piece; needs a second rail, an FX provider, and ledger columns for applied conversions.
`/fx/*`, request/response extensions on send / request / pay, `POST /kyc/international/start`, `POST /payments/request/preview`.

**Phase D — cards.** Needs an issuer partner; self-contained once chosen. Maps to PRD Phase 4.
`/cards/*`, `POST /webhooks/cards`.

**Phase E — compliance and support.** Required before public launch per §11 Phase 4 and §12.4.
Consents, limits mutation, deletion status, data export, `/support/*`, `POST /payments/{id}/dispute`.

**Ongoing, no phase:** translation preferences and batch, single-attachment presign, beneficiary CRUD, and converging `/upgrade/*` with `/kyc/*` (§5.1).

### 8.1 Sequencing note after this cycle

Nothing from Phases A–E shipped in the last cycle. The ten new endpoints were chat, profile and onboarding work, plus a second KYC ladder. That is a coherent product direction, but it means the distance between the implementation and the PRD has not narrowed — and two of the four structural gaps (**FX** and **cards**) are the long-lead items that need a partner selected before engineering can even start.

If public launch is still the goal on the PRD's timeline, **Phase C and Phase D need a partner decision now**, independently of whether any code is written this month. Everything else on this list is work the team can do unblocked; those two are not.

---

## 9. Open questions

0. **Is multi-currency still in MVP scope?** Two cycles have now passed with `activeNgn()` untouched while other work shipped. Either the PRD's multi-currency framing should be re-scoped to a post-launch phase, or FX needs to become the active workstream. The current state — documented as core, treated as later — is the expensive option, because it leaves the API shape unsettled for every client that touches money.

1. **Where does conversion happen?** Beevia's ledger is the source of truth for balances, and the partner moves cash. For a cross-currency send, does the ledger record two entries at a locked rate with the partner settling later, or does the partner quote and convert atomically? This determines whether `FxQuote` is a Beevia record or a partner reference, and whether a failed conversion is a ledger reversal or a partner-side rollback.

2. **Mismatched request payments.** Flow 6 permits the payer to pay an amount different from the request, after which the requester must accept or decline. Does the difference sit in the same escrow the exact-match case bypasses, and does an FX quote survive that second acceptance window or require a re-quote?

3. **What is `kyc_level`?** It is an integer with no documented mapping. Before `GET /kyc/status` can be built, the tier → level → unlocked-currency relationship needs to be written down.

4. **Non-Nigerian users.** `POST /auth/register` accepts any ISO country code and `bvn` is Nigeria-specific. What does onboarding look like for a UK or EU user today — is `chat_only` the only viable path until the international tier exists?

5. **Card issuance currency.** Cards link to a wallet, and only NGN wallets exist. Does the first card ship NGN-only, or does card issuance block on the second rail?

6. **Group payments.** Conversations support up to 64 members, but payments are strictly peer-to-peer against a phone number. The PRD scopes MVP payments to a "conversation partner", so this is presumably intentional — worth confirming rather than leaving implicit.

7. **`documents/` is gitignored.** Code comments cite `documents/api-surface.md`, `documents/chat-engine-plan.md`, `documents/ledger-wallets-payments-plan.md` and `documents/onboarding-flow.md` as canonical, and the Postman description names `documents/api-surface.md` as the full planned surface — but the directory is listed in `beevia-api/.gitignore`. No collaborator can read the documents the code treats as authoritative. See [`suggestions.md`](./suggestions.md) §2.1.
