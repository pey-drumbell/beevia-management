# Suggestions — `beevia-api`

Observations from a read-only review of the codebase, the Postman collection and the PRD, written while producing [`api-rfc.md`](./api-rfc.md), [`openapi.yaml`](./openapi.yaml) (implemented surface) and [`openapi.proposed.yaml`](./openapi.proposed.yaml) (designed but unbuilt).

**No code was changed.** Everything below is a proposal.

> **Paths in this document.** This file lives at the root of the `beevia-management` workspace. Unless prefixed otherwise, every `src/`, `postman/`, `docs/`, `README.md` and `.gitignore` path refers to the `beevia-api/` service directory — e.g. `src/common/env.ts` means `beevia-api/src/common/env.ts`. The `beevia-api` repository is unmodified.

Findings are grouped by theme and ordered within each group by impact. Each names the specific file or behaviour so it can be verified independently.

---

## What is already good

Worth stating plainly, because the rest of this document is criticism and the baseline is high.

- **One envelope, one error filter, one validation strategy, one guard model.** `ResponseInterceptor`, `AllExceptionsFilter`, `ZodValidationPipe`, `JwtAuthGuard`/`StepUpGuard` are applied uniformly. There are no bespoke response shapes hiding in individual controllers.
- **Money is handled correctly.** `numeric(20, 8)` in Postgres, `decimal.js` at `precision: 40` with `ROUND_HALF_EVEN`, major-unit strings across the wire, and a single `money.ts` module that is the only sanctioned way to parse and serialize. No floats anywhere.
- **REST and WebSocket share services, not logic.** `ConversationsHttpController` and `MessagingGateway` both call `ConversationsService` / `MessagesService` / `ReceiptsService` / `ReactionsService`. There is no second implementation to drift. Protect this invariant.
- **Escrow ordering is deliberate.** `PaymentService.send()` places the hold *before* creating the payment row, so a rejected send leaves nothing behind; expiry is idempotent and scheduled through BullMQ.
- **Route-ordering hazards are handled and commented.** `GET /users/:id` is declared last with an explanatory comment; `POST /conversations/bulk` precedes the `:id` routes.
- **Private-field stripping is centralized** and recursive, with a per-route escape hatch (`@PrivateFields`).
- **Webhooks verify signatures over raw bytes.** `rawBody: true` is enabled in `main.ts` specifically so HMAC is computed over the exact bytes received, and `partner_webhook_events` provides dedup.
- **Comments explain *why*, not *what*.** The `MUTE_FOREVER` sentinel, the `acceptedInviteId` no-FK decision, the read-through cache TTL rationale in `ProviderResolverService` — these are genuinely useful.

---

## 1. Correctness

### 1.1 A malformed UUID in a path parameter returns 500, not 400

**Severity: high — trivially reachable from any client.**

No route validates path parameters. `ParseUUIDPipe` appears nowhere in `src/`; every id is taken as `@Param('id') id: string` and passed straight to a DAL.

`BaseDal.findById()` does not wrap driver errors — only `create`, `update` and `paginate` throw `DalError`. So a non-UUID id reaches `node-postgres`, which raises `22P02` (`invalid input syntax for type uuid`).

`AllExceptionsFilter.mapPostgresError()` handles only `23505`, `23503` and `23502`, and returns `null` otherwise. The exception is not a `DalError` and not an `HttpException`, so it falls through to:

```ts
return { status: HttpStatus.INTERNAL_SERVER_ERROR, message: 'Internal server error' };
```

`GET /api/v1/users/not-a-uuid` therefore returns **500** where it should return **400**, and logs at `error` level with a stack trace. Affected routes include every `/users/{id}`, `/payments/{id}/*`, `/conversations/{id}/*`, `/messages/{id}/*`, `/calls/{id}/*`, `/devices/{id}`, `/attachments/{id}/*`, and `/wallets/{walletId}/transactions`.

Two independent fixes, both worth applying:

1. Add `ParseUUIDPipe` (or a Zod param pipe, for consistency with the rest of the codebase) to every uuid path parameter.
2. Map `22P02` in `mapPostgresError()` to a `400` with `error: 'invalid_identifier'`, as a backstop for any route that is missed.

The second matters more than the first: it also protects query parameters and future routes.

### 1.2 `OTP_ECHO` is guarded by a comment, not by code

`src/common/env.ts` documents `OTP_ECHO` as *"MUST be off (unset) in real production"*, and `SLACK_OTP_CHANNEL` carries the same warning. Neither is enforced. There is no `.refine()` or `.superRefine()` tying either to `NODE_ENV`.

The failure mode is that a production deploy with a copied `.env` echoes live OTPs in the `POST /auth/register` response body (`dev_otp`) and mirrors them to Slack — a complete bypass of phone-possession verification, which is the *only* identity factor at signup.

Suggested: a cross-field refinement on the env schema that fails startup when `NODE_ENV === 'production'` and `OTP_ECHO` is true (and likewise for `SLACK_OTP_CHANNEL`). The app already fails fast on env validation, so this costs one refinement and makes the misconfiguration unbootable rather than silent.

### 1.3 `WalletQueryService` reimplements pagination metadata

`src/wallets/wallet-query.service.ts:124` defines a private `meta()` helper that duplicates the construction in `BaseDal.paginate()` (`src/database/dals/base.dal.ts:242`). They already differ: the DAL computes `Math.ceil(total / limit)`, while the service computes `Math.ceil(total / limit) || 1` — so an empty result set reports `total_pages: 0` from one path and `1` from the other.

Extract one `buildPaginationMeta(total, page, limit)` into `src/common/` and have both call it.

### 1.4 Postman pagination examples are stale

The saved examples for `GET /wallets/transactions` and `GET /wallets/{walletId}/transactions` show:

```json
"meta": { "total": 1, "page": 1, "limit": 20, "pages": 1 }
```

The code emits `PaginationMeta` (`src/database/dals/dal.types.ts:39`) snake_cased:

```json
"meta": { "total": 1, "current_page": 1, "limit": 20, "total_pages": 1, "has_next_page": false, "has_prev_page": false }
```

A client author working from the collection will write `meta.page` and `meta.pages` and get `undefined`. The collection is the artifact most likely to be trusted by someone integrating, so stale examples there cost more than stale prose.

### 1.5 `POST /devices` documents 200 but returns 201

`src/devices/devices.controller.ts:40` combines `@HttpCode(HttpStatus.CREATED)` with `@ApiOkResponse(...)`. The generated OpenAPI document claims `200`; the route returns `201`. Use `@ApiCreatedResponse`.

---

## 2. Documentation and repository hygiene

### 2.1 The canonical design documents are gitignored

`.gitignore` ends with:

```
documents/
service-account.json
```

Yet code comments across the repository cite that directory as authoritative:

- `src/common/all-exceptions.filter.ts` — *"Single source of truth for the error envelope (see `documents/api-surface.md`)"*
- `src/common/money.ts` — *"see the ledger plan (`documents/ledger-wallets-payments-plan.md`)"*
- `src/database/schema/enums.ts` — *"see `documents/chat-engine-plan.md`"*
- `src/database/schema/users.ts` — *"Onboarding follows the state machine in `documents/onboarding-flow.md`"*
- The Postman collection description — *"full planned surface: `documents/api-surface.md`"*

No collaborator, new hire, or reviewer can read any of them. Comments reference documents that, from a fresh clone, do not exist. ADR identifiers are cited the same way (`ADR-0003`, `ADR-0004`, `ADR-0006`) with no ADR directory in the repo, and open-question tags (`OQ-CHAT-2`, `OQ-FREEZE`, `LD-5`, `CH-E2EE-3`) have no glossary.

If the directory is ignored because it contains commercially sensitive vendor terms, split it: keep the architectural documents and ADRs in version control, and move only the sensitive material elsewhere. If it is ignored because the files live in an external tool, replace the paths in comments with links that resolve.

This is the single highest-leverage fix in this document. Everything else is a defect; this one silently degrades every other document's usefulness.

### 2.2 `README.md` is still largely the NestJS starter

The file opens with the Nest logo, CircleCI badges pointing at `nestjs/nest`, a PayPal donation link for Kamil Myśliwiec, and *"Nest framework TypeScript starter repository"* as the description. Genuinely project-specific content (env var table, Drizzle usage) has been added beneath it.

It also contains a stale path: *"The schema lives in `src/database/schema.ts`"* — it is a directory, `src/database/schema/`, with 30+ modules.

For a repository this substantial, the README should open with what Beevia is, the architecture in a paragraph, how to run it (Postgres + Redis + MinIO), where the API docs are (`/api/docs`, plus the `openapi.yaml` at the workspace root), and how the WebSocket and REST transports relate.

### 2.3 Vendor names leak inconsistently through the abstraction

The PRD is explicit that the product describes *capabilities, not vendors*, and that partners are named only in a companion specification. The codebase half-follows this: some seams are abstracted (`ProviderResolverService`, `payment_provider` enum, `TranslatePort`, `NotificationPort`, `StoragePort`), while elsewhere vendor names are load-bearing in public-facing surface area:

- The identity webhook path is `POST /kyc/entrust/webhook` — a partner-facing URL naming a vendor, in a module named `entrust`, whose own comment in `main.ts` says the signature is *"Onfido's X-SHA2-Signature"*. Two vendor names for one integration, one of them in the route.
- `anchor_customer_id` and `entrust_applicant_id` are column names in `users`.
- `POST /webhooks/anchor` and `POST /webhooks/livekit` name vendors in paths.

Webhook paths naming the sender is a defensible convention — the partner configures that URL, and it aids routing and log triage. But it should be a stated convention rather than an accident, and `entrust` vs `Onfido` should be reconciled either way. User-table columns would be better as `provider_customer_id` + `provider` given the enum already supports multiple rails.

### 2.4 Swagger is served unauthenticated

`SwaggerModule.setup('/api/docs', ...)` in `main.ts` has no guard. In production this publishes the complete API surface — every route, schema, error code and example — to anyone who requests it. That is reconnaissance material for an app that moves money, and it is at odds with the PRD's compliance posture.

Serve it only when `NODE_ENV !== 'production'`, or place it behind basic auth or an internal-network check.

---

## 3. API design consistency

### 3.1 The camelCase-in / snake_case-out asymmetry is undocumented outside Swagger

Requests use camelCase (`recipientPhone`, `signedPrekeySig`, `messageHistorySyncEnabled`); responses use snake_case (`recipient_phone`, `signed_prekey_sig`, `message_history_sync_enabled`). This is intentional and consistently applied, but it means no round-trip is symmetric: a client cannot take a response object, modify a field, and send it back.

The Swagger description mentions snake_case responses but never states that requests are camelCase. Worth a prominent note in the README and the Postman collection description — or, if the cost is acceptable, converting requests on the way in as well so the wire format is uniform.

### 3.2 POST status codes are inconsistent

Creating resources returns 201 in some places and 200 in others, with no discernible rule:

| Creates a resource | Returns |
|---|---|
| `POST /devices` | 201 |
| `POST /conversations` | 201 |
| `POST /conversations/{id}/messages` | 201 |
| `POST /attachments/upload-url` | 201 |
| `POST /conversations/{id}/calls` | 201 |
| `POST /wallets` | **200** |
| `POST /invites` | **200** |
| `POST /payments/send` | **200** |
| `POST /payments/request` | **200** |
| `POST /users/me/username` | **200** |

Chat and device creation use 201; money and invites use 200. Pick one rule — *"201 when a new addressable resource is created, 200 otherwise"* is the conventional one — and note the deliberate exceptions (`POST /wallets` is idempotent and returns the whole list, so 200 is arguably right).

### 3.3 `POST /wallets` returns a list, not the created wallet

`WalletsController.create()` provisions the wallet and then returns `this.query.listWallets(user.id)`. Convenient for the client's wallet screen, but it makes the response indistinguishable from `GET /wallets`, and the caller cannot tell which entry was just created — particularly awkward because provisioning is asynchronous, so the new wallet may have `vba: null` and look identical to a stale one.

Suggested: return the created wallet as `data`, and let the client refetch the list. If the current behaviour is retained for convenience, document it explicitly.

### 3.4 `DELETE /notifications/token` takes a request body

`deviceId` is sent in a JSON body on a `DELETE`. This is legal but poorly supported — some HTTP clients, proxies and caches drop `DELETE` bodies. Prefer `DELETE /notifications/token/{deviceId}` or `DELETE /notifications/token?deviceId=`.

### 3.5 The identity webhook sits outside `/webhooks`

`POST /kyc/entrust/webhook` is under `/kyc`; the other two partner callbacks are under `/webhooks`. Grouping them makes the set easier to secure at the edge — rate limits, IP allowlists and body-size caps are naturally expressed per path prefix.

### 3.6 `recipientPhone` and `payerPhone` are validated more loosely than every other phone field

`src/payments/dto/payments.dto.ts` validates them as `z.string().trim().min(6).max(20)`, while `auth.dto.ts`, `invites.dto.ts` and `users.dto.ts` all use the strict E.164 regex `^\+[1-9]\d{6,14}$`.

Money-moving routes are the *last* place that should have the loosest input validation. `"abc123"` passes the schema and fails later in lookup. Reuse the shared E.164 validator — ideally hoisted into `src/common/` since it is currently copy-pasted into three DTO files.

### 3.7 There is no API versioning mechanism

`app.setGlobalPrefix('api/v1')` hard-codes the version into a string prefix. Nest's `enableVersioning()` (URI or header) would let `v2` routes coexist with `v1` during a migration, which matters once a mobile app is in the field and cannot be force-upgraded. Not urgent pre-launch, but cheap to adopt now and expensive to retrofit later.

---

## 4. Security and operations

### 4.1 No rate limiting anywhere

`@nestjs/throttler` is not a dependency and no equivalent exists. The OTP service enforces a *resend cooldown* and a max-attempts counter, which is good and specific, but it is per-phone application logic, not transport-level protection.

Unprotected and reachable without authentication or with a single valid session:

- `POST /auth/register`, `/auth/login`, `/auth/otp/request` — SMS cost amplification, phone enumeration.
- `POST /auth/pin/verify`, `/auth/step-up` — PIN brute force. A 4-digit PIN has 10,000 combinations; without a lockout, exhausting it is seconds of work.
- `POST /users/lookup`, `POST /contacts/sync` (500 numbers per call) — bulk phone enumeration of the user base.
- `GET /keys/{userId}` — **consumes a one-time prekey per call.** An authenticated attacker can drain a victim's entire prekey pool in a loop, degrading their forward secrecy until the pool is replenished.
- `POST /translate` — third-party cost amplification.

Add global throttling with tighter per-route limits on the auth, lookup and key-bundle routes. The PIN routes additionally need a lockout, not just a rate limit.

### 4.2 No CORS policy, and the WebSocket gateway allows all origins

`main.ts` never calls `enableCors()`, so browser clients are blocked by default — fine for a mobile-only product today, but it means the policy is unstated rather than chosen.

Meanwhile `src/messaging/gateway/messaging.gateway.ts:82` declares:

```ts
@WebSocketGateway({ cors: { origin: '*' } })
```

Any origin may open a socket. Authentication still gates what can be done, so this is not an immediate breach, but `*` should not survive to production. Drive both from an env-configured allowlist.

### 4.3 No security headers

`helmet` is not a dependency. HSTS, `X-Content-Type-Options`, frame options and referrer policy are all absent. This matters most for `/i/:code`, which serves HTML to browsers, and for `/api/docs` if it stays public.

### 4.4 No real health probe

`GET /` returns a static `"Hello World!"` and will happily return 200 with Postgres, Redis and MinIO all down. There is nothing an orchestrator or load balancer can key on, against a stated objective of 99.9% uptime and 2-second transaction latency.

`@nestjs/terminus` provides this with very little code. Proposed as `GET /health` in `openapi.proposed.yaml`.

### 4.5 No request correlation id

Logs record `[METHOD] url status - message` with no request id, and error responses carry no reference the user can quote. `POST /wallets/withdraw`'s documented error path tells the user to keep a reference number for support — there is no correlation identifier to tie that to a log line.

A `RequestIdMiddleware` populating an `X-Request-Id` header, echoed in the error envelope and included in every log line, is small and pays for itself the first time someone debugs a production payment.

### 4.6 `POST /cards/{id}/reveal` (when built) must be excluded from logging

Flagged now so it is not overlooked: the proposed reveal endpoint returns PAN and CVV. Whatever request/response logging is added later must exclude it explicitly, and the same applies today to `POST /kyc/bvn/verify-ownership`, which accepts a base64 selfie and an 11-digit BVN in the request body. `bvn` is stripped from *responses* by the interceptor, but nothing prevents a future request logger from capturing it on the way in.

---

## 5. Maintainability

### 5.1 Zod schemas and Swagger DTO classes are duplicated by hand

Every DTO file defines the validation schema twice — once as Zod, once as a decorated class purely so `@ApiBody({ type: ... })` renders. `auth.dto.ts` says so directly:

> *"These classes exist only so `@ApiBody({ type: … })` can render an accurate request schema in Swagger. Keep them in sync with the schemas above."*

Nothing enforces that. The drift risk is not hypothetical: `verifyBvnOwnershipSchema` accepts `method: "phone"`, the route then rejects it at runtime with `method_unavailable`, and the only record of that is a prose note on the Swagger class (`"phone is not yet supported"`). Three places describe one rule, and only one of them is executable.

Options, roughly in order of effort:

- `nestjs-zod` — derives both the pipe and the Swagger schema from one Zod schema.
- `zod-to-openapi` — generates OpenAPI components from Zod, keeping the pipe as-is.
- Keep the duplication but add a test that asserts the class's declared keys match the schema's shape.

Any of the three removes an entire class of silent documentation drift.

### 5.2 The E.164 regex is copy-pasted into three DTO files

`^\+[1-9]\d{6,14}$` appears in `auth.dto.ts`, `invites.dto.ts` and `users.dto.ts`, with a fourth, looser variant in `payments.dto.ts` (see §3.6). Hoist a shared `phoneSchema` into `src/common/`.

### 5.3 The Postman collection is maintained by hand

Its description sets the policy — *"when a session ships a new endpoint, add that one request here in the same change"* — which is disciplined but relies entirely on memory, and §1.4 shows it has already drifted.

Now that `openapi.yaml` exists, two options:

- Generate the collection from the OpenAPI document in CI (`openapi-to-postman`), keeping hand-written examples in a separate overlay.
- Keep it hand-maintained, but add a CI check that every route registered by Nest appears in the collection. The route list is enumerable at runtime from the Nest router, so this is a short script.

The same check should compare against `openapi.yaml` so the three artifacts cannot silently diverge.

### 5.4 Generate `openapi.yaml` from the running app

`SwaggerModule.createDocument()` already builds a complete document at startup. A script that boots the app, writes the document to `beevia-api/docs/openapi.generated.yaml`, and fails CI if it differs from the committed `openapi.yaml` would keep the implemented surface honest automatically — no annotation, marker or decorator required, because that file now contains *only* implemented routes.

`openapi.proposed.yaml` stays hand-maintained, which is correct: it describes routes that do not exist, so nothing can generate it.

Two cheap CI guards are worth adding alongside:

- **No overlap.** Fail if any `(path, method)` appears in both files, except the three deliberate entries under `MODIFICATIONS TO LIVE ENDPOINTS`. This catches the most likely mistake — copying an operation across instead of moving it.
- **Shared schemas agree.** The proposed file duplicates component definitions rather than `$ref`ing across files (so it opens in Swagger UI and any generator without bundling). Assert that same-named components are structurally identical in both, or they will drift.

  Two must be **excluded** from that assertion — `SendMoneyRequest` and `RequestMoneyRequest` differ *by design*, since the proposed file carries their widened target form. Keep the exclusion list in the check itself, next to the `MODIFICATIONS TO LIVE ENDPOINTS` allowlist, so both shrink together as those endpoints ship.

### 5.5 Test coverage is uneven in a predictable way

Unit specs sit next to almost every service, and integration specs exist for the ledger, payments, attachments, devices, chat DALs and account deletion. E2E specs cover messaging, chat groups, chat flow and the queue.

The gap is that **no controller has an HTTP-level test**. Guards, pipes, the response interceptor and the exception filter have unit specs, but nothing asserts the composed behaviour — that `POST /payments/send` without `X-Step-Up-Token` returns 401 with `error: "step_up_required"`, or that a validation failure produces the documented `details[]` shape. §1.1 is exactly the kind of defect a thin supertest pass over each route would have caught.

---

## 6. Product-facing gaps

These are specified in detail in [`api-rfc.md`](./api-rfc.md) §4–§5 and appear as operations in [`openapi.proposed.yaml`](./openapi.proposed.yaml). Listed here only so this document stands alone:

| Gap | Impact |
|---|---|
| **Cross-currency conversion does not exist.** `PaymentService` calls a private `activeNgn()` helper at `payment.service.ts:62` and `:155` and uses NGN unconditionally. No rate, quote, or conversion anywhere. | The PRD's headline differentiator ("Multi-Currency by Design") is unimplemented. `exchange_rate` is already a routable provider capability with no consumer. |
| **Virtual cards do not exist.** No module, controller, table or capability. | An MVP feature with a user story, a flow, a feature spec and a roadmap phase has no code. |
| **Payments have no read path.** No `GET /payments`, no `GET /payments/{id}`. | The 24-hour escrow countdown the PRD requires cannot be rendered after an app restart. `payment_card` messages carry a `ref_id` that cannot be resolved. |
| **No preview before confirmation.** | "Blocked with clear message before confirmation" is impossible; the user is prompted for their PIN before the app can know the send will fail. |
| **Only the local KYC tier exists**, and `kyc_level` is an opaque integer with no status endpoint. | The client cannot explain why a currency is locked, and discovers gates only as errors from `POST /wallets`. |
| **No consent record**, despite §10.4 listing Consent Management as MVP and Phase 4 requiring consent logging and audit trails. | A stated MVP feature and a pre-launch compliance requirement are both unmet. |
| **No dispute or support surface.** | §7.4 tracks dispute resolution time and partner escalations as KPIs; neither is instrumentable. |
| **No deletion status.** `DELETE /users/me` acknowledges synchronously while partner deletion is asynchronous. | Flow 8 explicitly requires "deletion in progress", "not a silent failure". The `user_status` enum already has a `deleting` value that nothing reads. |
| **`account_resolution` has no endpoint.** | The payee's account name is returned only *after* the debit, so a user cannot confirm who they are paying. |
| **Message deletion is modelled but unreachable.** `message_delete_scope` and `deleted_for` exist; no route sets them. | Flow 1 lists deletion as an expected thread action. |
| **Translation is stateless only.** | §8.1 requires per-conversation *and* global opt-in; the preference cannot survive a reinstall. |

---

## 7. Suggested order

1. **§1.1** — malformed UUID → 500. Small fix, trivially reachable, currently generates false 500s in monitoring.
2. **§1.2** — enforce `OTP_ECHO` off in production at startup.
3. **§4.1** — rate limiting, especially PIN verification and `GET /keys/{userId}`.
4. **§2.1** — un-ignore the design documents, or make the references resolve.
5. **§4.4 / §4.5** — health probe and request ids, before public launch.
6. **§1.4 / §5.3** — reconcile Postman with the code and add a drift check.
7. **§4.2 / §4.3** — CORS allowlist and security headers.
8. **§5.1** — collapse the Zod/DTO duplication before it drifts further.
9. **§3.x** — status codes, phone validation, webhook grouping; batch into one consistency pass.
10. **§6** — the product gaps, sequenced in `api-rfc.md` §8.
