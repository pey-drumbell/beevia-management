# RFC: Beevia API Surface

| | |
|---|---|
| **Status** | Draft — for review · **updated 2026-08-05** |
| **Scope** | The complete HTTP surface of `beevia-api` (the consumer API): what exists today, and what the PRD requires that does not exist yet |
| **Companion artifacts** | [`openapi.yaml`](./openapi.yaml) — implemented, 100 operations · [`openapi.proposed.yaml`](./openapi.proposed.yaml) — designed but unbuilt, 52 operations · [`suggestions.md`](./suggestions.md) · [`Beevia_PRD.md`](./Beevia_PRD.md) |
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
| **New service: `beevia-admin-api`** | 29 operations. Documented separately in [`admin-api-rfc.md`](./admin-api-rfc.md). |
| **Unchanged** | FX/multi-currency, virtual cards, international KYC tier and consent management remain entirely unbuilt. `PaymentService.activeNgn()` is still there at `payment.service.ts:63`. |

---

## 1. Summary

The consumer API is **100 HTTP operations** across 18 domains, plus a Socket.IO gateway with 30 client commands and 15 server events. Chat, calling, identity verification, NGN wallets and peer-to-peer payments are implemented and coherent. The engineering conventions remain unusually consistent: one response envelope, one error filter, one validation strategy, one guard model.

Measured against the PRD, three MVP capabilities are **still absent from the codebase entirely**, and one is present in name only:

| PRD capability | State |
|---|---|
| Virtual cards (§1.2, §8.2, §10.3, Phase 4) | **No code at all** — no module, controller, table, or provider capability |
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
| [`openapi.admin.yaml`](./openapi.admin.yaml) | **29 operations that exist today** in `beevia-admin-api`. | Same, for the back office. |
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
| Contacts | 2 | 0 | Complete |
| Devices & Keys | 6 | 0 | Complete |
| Invites | 3 | 0 | Complete (no dispatch, by design) |
| Currencies | 1 | 0 | Complete |
| Wallets | 7 | 8 | No bank list, account resolution, single-wallet read, or payout status |
| FX | **0** | 3 | Does not exist |
| Payments | **9** | 4 | **+3:** direct `POST /payments/transfer` (non-escrow, idempotent) and the recipient picker (`GET /payments/recipients`, `GET /payments/recent-recipients`). Still no read path — no `GET /payments` |
| Cards | **0** | 8 | Does not exist |
| Chat (REST) | 19 | 0 | +2 clear, delete. Message deletion now shipped |
| Calls | 5 | 0 | Complete |
| Attachments | 2 | 1 | No single-attachment download presign |
| Upload | 5 | 0 | Public, permanent objects — distinct from Attachments (encrypted, presigned-only) |
| Translate | 1 | 5 | Stateless only; no preference storage |
| Notifications | 5 | 0 | Complete |
| Support | **0** | 4 | Does not exist. Includes `POST /payments/{id}/dispute`, listed under §7.2 but tagged Support |
| Webhooks | 3 | 1 | Card issuer callback missing |
| **Total** | **108** | **49** | +3 live-endpoint modifications = 52 operations in the proposed file |

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

### 4.2 Virtual cards do not exist

`grep -ri card src/` returns the `payment_card` *message type* and nothing else. No module, no controller, no `cards` table, no `card_issuance` provider capability, no issuer webhook.

The PRD places cards in the key modules list (§1.2), gives them a user story (§8.2), a full flow (§9 Flow 7), a detailed feature spec (§10.3), and makes them the headline of roadmap Phase 4. The spec is specific: masked by default, reveal behind biometric/PIN with automatic re-mask after a fixed window, freeze/unfreeze at any time, issuer legal name and compliance disclosure shown in-app, and a clear status message with retry when the issuer is unavailable.

Proposed: eight operations under `/cards` plus `POST /webhooks/cards`. Two deliberate asymmetries in the design:

- **Freeze is not step-up gated; unfreeze is.** A user reacting to a suspected compromise should never be slowed by a PIN prompt. Restoring spending ability is the direction that warrants friction.
- **`POST /cards/{id}/reveal` returns `reveal_ttl_seconds`**, so the re-mask window the PRD requires is server-specified rather than invented per client.

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

**No deletion status.** `DELETE /users/me` returns `{ deleted: true }` synchronously, but partner-side deletion is asynchronous. Flow 8 explicitly requires that a partner delay surface as *"deletion in progress"*, "not a silent failure", and §7.4 tracks completion within 5 days. The `user_status` enum already has a `deleting` state with nothing reading it.

**No health probe.** `GET /` returns a static `"Hello World!"` and stays 200 with Postgres down. There is nothing for a load balancer or orchestrator to key on, against a 99.9% uptime objective.

**Translation is stateless only.** §8.1 requires opt-in translation "set per conversation **or globally**". `POST /translate` is a one-shot call with the target language supplied every time, so the preference lives only in client storage and does not survive reinstall or follow the user to a new device. There is also no supported-language list (so no validated picker) and no batch endpoint (so opening a thread with auto-translate on means one HTTP round trip per visible message).

~~**Message deletion is modelled but unreachable.**~~ **Closed 2026-08.** `DELETE /messages/{id}` shipped — see §5.2 below.

---

## 5A. Notes on the work that shipped this cycle

Three of the ten new endpoints carry design decisions worth recording, because each one constrains what can be built next.

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

### 5.2 Message deletion is sender-only in both modes — and the reason is a schema limit

The implementation notes it plainly: `deleted_for` is a *single scope on the message row*, not a per-user flag, so a recipient hiding a message has nowhere to record that. Rather than fake it, the route returns 403 to a non-sender in both modes.

That is the right call — a no-op that returns 200 would be worse. But it means **"delete for me" is unavailable to the person most likely to want it**: the recipient of an unwanted message. Making that work needs a per-user table (or a `deleted_for_user_ids` array), not a new endpoint. Worth deciding deliberately rather than inheriting the current shape by default.

Note also the query parameter is `?forEveryone=true`, whereas this RFC had proposed `?scope=sender|everyone`. The shipped form is fine; `openapi.yaml` documents the real one.

### 5.3 The contact profile's relationship-scoped `phone` is good design

`GET /users/{id}` now returns `phone` **only** when the caller and target already share a 1:1 conversation, or the caller is viewing themselves. The reasoning in the source is exactly right: any authenticated caller can pass an arbitrary id or handle, so returning it unconditionally would turn the endpoint into a number-harvesting tool.

This is the kind of thinking §4 of `suggestions.md` asks for elsewhere — worth naming because it should be the template for the proposed admin and support surfaces, where the same temptation exists at greater scale.

---

## 6. Implemented surface

Status legend: **✅ Complete** · **🟡 Partial** — works but materially narrower than the PRD describes.

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
| | GET | `/auth/me` | 🔑 | ✅ |
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
| | POST | `/upgrade/profile` | 🔑 | ✅ No `email`; `gender` optional |

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
| | POST | `/contacts/sync` | 🔑 | ✅ Max 500 entries |
| | GET | `/contacts` | 🔑 | ✅ |
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
| | POST | `/conversations/{id}/report` | 🔑 | ✅ Metadata only — E2EE precludes content review |
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
| | POST | `/translate` | 🔑 | 🟡 Stateless; no preference, languages or batch |
| | POST | `/notifications/token` | 🔑 | ✅ |
| | DELETE | `/notifications/token` | 🔑 | ✅ Body-based, not path-based |
| | GET | `/notifications/preferences` | 🔑 | ✅ |
| | PATCH | `/notifications/preferences` | 🔑 | ✅ |
| | POST | `/notifications/test` | 🔑 | ✅ |
| | POST | `/webhooks/anchor` | 🔓 | ✅ HMAC over raw body; deduped |
| | POST | `/webhooks/livekit` | 🔓 | ✅ JWT in `Authorization` |

### 6.9 WebSocket surface

30 client commands and 15 server events. Commands: `sync.bootstrap`, `sync.messages`, `number.lookup`, `conversation.{create,get,update,join,leave,archive,unarchive,mute,report,media}`, `conversation.members.{add,remove}`, `conversations.{list,bulk}`, `message.{send,backfill}`, `receipt.send`, `reaction.{add,remove}`, `call.{start,answer,decline,end}`, `typing.{start,stop}`, `presence.ping`, `ping`.

**The transports are not at parity in either direction**, which is worth stating explicitly because both docs and the Postman collection imply they are:

| Capability | REST | WS |
|---|---|---|
| Typing indicators | — | ✅ |
| Presence | — | ✅ |
| Bootstrap sync | — | ✅ |
| Join / leave a room | — | ✅ |
| Explicit unarchive command | via `{archived:false}` | ✅ dedicated |
| Attachments | ✅ | — (binary never over WS, by design) |
| Payments, wallets, KYC | ✅ | — |

Typing and presence being WS-only is correct — they are ephemeral. `sync.bootstrap` having no REST equivalent is a genuine hole: a client that cannot open a socket has no single call to establish initial state.

---

## 7. Proposed surface

All 50 operations below live in [`openapi.proposed.yaml`](./openapi.proposed.yaml) with full schemas, alongside the 3 live-endpoint modifications described in §7.1. Each conforms to the existing conventions: `/api/v1` prefix, standard envelope, snake_case responses, camelCase Zod-validated request bodies, `JwtAuthGuard` by default, `StepUpGuard` on anything that moves money or is irreversible.

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

### 7.7 Translation (5)

| Method | Path | Auth |
|---|---|---|
| GET | `/translate/languages` | 🔑 |
| POST | `/translate/batch` | 🔑 |
| GET | `/users/me/translation` | 🔑 |
| PATCH | `/users/me/translation` | 🔑 |
| PATCH | `/conversations/{id}/translation` | 🔑 |

Batch reports failures **per item** rather than failing the batch, so the PRD's fallback ("original message still shown, with a clear notice") stays renderable row by row.

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
