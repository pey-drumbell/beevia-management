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

**Resolved 2026-09-24.** Both saved examples now carry the real `PaginationMeta` shape, updated in the same commit that added transaction row titles (`beevia-api` `4d81f9f`). The `GET /wallets/transactions` example was also widened from one row to five, one per title form. `openapi.yaml`'s `TransactionPageOk` note, which pointed here, has been corrected. This is §5.3's hand-maintenance policy working — but note it took fifty days and only happened because the same commit had another reason to touch the collection.

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

`src/payments/dto/payments.dto.ts` validates them as `z.string().trim().min(6).max(20)`, while every other phone input in the service now goes through `src/common/phone.util.ts`.

Money-moving routes are the *last* place that should have the loosest input validation. `"abc123"` passes the schema and fails later in lookup. The original ask was to reuse a shared E.164 validator, ideally hoisted into `src/common/`.

**Escalated 2026-09-25 — the gap widened rather than closed.** §5.2's consolidation landed on 24 September and `payments.dto.ts` was not part of it: it still declares its own local `const phone = z.string().trim().min(6).max(20)` and imports nothing from `phone.util.ts`. So `/payments/send` and `/payments/request` are now the only two endpoints in `beevia-api` that will accept a phone number nobody has checked is dialable — and, more to the point, the only two that do **not** get the trunk-prefix repair. A payer who types `08089421407` where every other screen in the app would have resolved it now fails, or worse, matches nothing and is treated as a non-user. The fix is one import and one deleted line; the spec records the looseness on both fields so a client is not misled in the meantime.

**Escalated again 2026-09-28 — a third caller now depends on it.** `beevia-api` #57 (25 Sep) exposed escrowed send over the socket as `payment.send`, reusing `sendMoneySchema` unchanged. That command is the one the unmerged mobile branch `update-fixes` now uses for every in-chat send, so once the branch merges, **every chat payment in the product will pass through the one phone field that is not parsed**. The fix is still one import and one deleted line.

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

### 4.7 A generated report outlives the permissions it was generated under

**Added 2026-09-10**, on `beevia-admin-api`'s new Reports module (`admin-api-rfc.md` §3.14).

`ReportsService.generate` does the careful thing: it resolves the requesting admin's `viewableModules` **at request time**, so a role change mid-run cannot widen or narrow the output. The comment says so explicitly — *"the report must reflect what the admin who asked for it was allowed to see, even if their role changes mid-run"*.

That scoping is then never re-applied. `GET /admin/reports/{id}` and `GET /admin/reports/{id}/download` are gated by `reports:view` and `reports:export` and nothing else — neither checks who requested the report, and the run history is team-wide by default. So an admin whose role sees one module can list, preview and download an `admin_activity` report generated by an admin who sees all of them.

Three properties make this worth fixing before the module is used rather than after:

- **The artifact is durable.** The CSV is stored on the row, so it keeps the wider scope permanently — narrowing the generating admin's role later does not narrow the file.
- **It is discoverable, not just reachable.** The history lists every report with its requester's name, so a narrower admin does not have to guess an id.
- **It is a generic escalation, not a report-specific one.** Any future report type inherits it, and the module is explicitly designed for report types to be added server-side without a client release.

Two fixes, either sufficient: persist the generating admin's `viewableModules` on the row and re-filter the preview and the CSV on read; or scope reads to reports whose requester's permissions are a subset of the reader's. The first is more honest about what a stored export *is* — a snapshot of one person's view — and it is the one to prefer if the reports are ever going to be shared.

**The general shape is worth naming**, because it will recur: *authorisation applied when an artifact is produced is not authorisation applied when it is read.* Every export, cache, snapshot and emailed attachment in this system has the same structure.

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

### 5.2 ~~The E.164 regex is copy-pasted into three DTO files~~ — **resolved 2026-09-24**

`^\+[1-9]\d{6,14}$` appeared in `auth.dto.ts`, `invites.dto.ts` and `users.dto.ts`, with a fourth, looser variant in `payments.dto.ts` (see §3.6). The ask was to hoist a shared `phoneSchema` into `src/common/`.

**Done, and for a better reason than tidiness.** `feat/contact-sync-normalisation` (merged 24 Sep) replaced the regex with `libphonenumber-js` behind `src/common/phone.util.ts`. Verified at `origin/main`: the string `[1-9]\d{6,14}` now occurs in exactly one file, and that occurrence is the doc comment explaining why the regex was retired.

The retirement note is worth reading, because the regex was not merely duplicated — it was **wrong in a way that created duplicate accounts**. `^\+[1-9]\d{6,14}$` accepts `+23408089421407`: a Nigerian number pasted on in national form, trunk `0` and all. E.164 requires that `0` to be dropped, so the same person typing their number the two obvious ways produced two distinct strings, and a unique index stored both happily. Knowing which leading digits are a trunk prefix, and which countries keep theirs, is exactly the knowledge a phone library holds and a regex cannot.

**§3.6 is the remaining half** — `payments.dto.ts` was not migrated, so the money-moving routes are now the *only* phone inputs in the service that are not parsed.

### 5.3 The Postman collection is maintained by hand

Its description sets the policy — *"when a session ships a new endpoint, add that one request here in the same change"* — which is disciplined but relies entirely on memory, and §1.4 shows it has already drifted.

Now that `openapi.yaml` exists, two options:

- Generate the collection from the OpenAPI document in CI (`openapi-to-postman`), keeping hand-written examples in a separate overlay.
- Keep it hand-maintained, but add a CI check that every route registered by Nest appears in the collection. The route list is enumerable at runtime from the Nest router, so this is a short script.

The same check should compare against `openapi.yaml` so the three artifacts cannot silently diverge.

### 5.4 Generate `openapi.yaml` from the running app

`SwaggerModule.createDocument()` already builds a complete document at startup. A script that boots the app, writes the document to `beevia-api/docs/openapi.generated.yaml`, and fails CI if it differs from the committed `openapi.yaml` would keep the implemented surface honest automatically — no annotation, marker or decorator required, because that file now contains *only* implemented routes.

`openapi.proposed.yaml` stays hand-maintained, which is correct: it describes routes that do not exist, so nothing can generate it.

**Update 2026-09-03 — this is now the highest-value item in this document, and there is a second demonstration.** On 2026-09-02 five contract facts were found wrong in `openapi.admin.yaml`, four of them shipped on 6 August and unnoticed through nineteen daily audits. Today `POST /contacts/sync` and `GET /contacts` changed the shape of the `user` object they return — a new `path` field — with no route added, renamed or removed. The daily audit compares route inventories, so it reported both services clean on both days. Every one of these findings came from a person reading a diff.

The pattern is now well enough evidenced to state as a property rather than a run of incidents: **this pipeline reliably detects new routes and reliably misses changed contracts.** Response bodies, query parameters, enum values and status codes are all invisible to an inventory diff. Generating the document from the app and diffing it in CI is not a tidiness improvement — it is the only proposal here that closes the class, and it applies to `beevia-admin-api` (whose `main.ts` also already calls `SwaggerModule.createDocument`) exactly as much as to `beevia-api`.

Credit where it is due on the same commit: the Postman examples for both contacts responses were updated in the same change, which is §5.3's stated policy actually being followed.

**Update 2026-09-04 — the strongest evidence yet, and it cuts the other way too.** Today the audit *worked*: four new admin routes were added, the inventory diff caught all four, and the spec was corrected the same morning. That is the pipeline's good case, and it took minutes.

In the same twenty-four hours it missed two changes that matter more than any of the four:

- **`POST /webhooks/anchor` went from processing nothing to processing everything.** For sixty-seven days it acknowledged every real Anchor delivery with `200` and dropped it (`api-rfc.md` §5.6). No route changed, so no audit ever saw it — nineteen consecutive clean runs over an endpoint that was a silent no-op on the money path.
- **NGN payouts changed which account they draw on** (`api-rfc.md` §5.7). Same path, same request, same response; different money movement.

Neither is a documentation slip. The first is the single most consequential defect this pipeline has encountered, and an inventory diff was structurally incapable of noticing it — the route existed and returned `200` throughout, which is exactly what "healthy" looks like from the outside.

**That bounds what generating the document from the app would buy, and it is worth being honest about.** It would have caught the contacts response shape, the five wrong admin facts, and today's pagination divergence. It would **not** have caught the webhook no-op or the treasury change, because neither altered the document. Generation closes the contract-drift class; it does not close the behaviour-drift class, and this cycle produced one of each. The second class needs a different instrument — a provider-event fixture exercised end to end against a real delivery shape, and an alert on "webhook received, no handler matched" rather than a silent acknowledgement. That last one is five lines and would have flagged this on day one of sixty-seven.

Two cheap CI guards are worth adding alongside:

- **No overlap.** Fail if any `(path, method)` appears in both files, except the three deliberate entries under `MODIFICATIONS TO LIVE ENDPOINTS`. This catches the most likely mistake — copying an operation across instead of moving it.
- **Shared schemas agree.** The proposed file duplicates component definitions rather than `$ref`ing across files (so it opens in Swagger UI and any generator without bundling). Assert that same-named components are structurally identical in both, or they will drift.

  Two must be **excluded** from that assertion — `SendMoneyRequest` and `RequestMoneyRequest` differ *by design*, since the proposed file carries their widened target form. Keep the exclusion list in the check itself, next to the `MODIFICATIONS TO LIVE ENDPOINTS` allowlist, so both shrink together as those endpoints ship.

### 5.5 Test coverage is uneven in a predictable way

Unit specs sit next to almost every service, and integration specs exist for the ledger, payments, attachments, devices, chat DALs and account deletion. E2E specs cover messaging, chat groups, chat flow and the queue.

The gap is that **no controller has an HTTP-level test**. Guards, pipes, the response interceptor and the exception filter have unit specs, but nothing asserts the composed behaviour — that `POST /payments/send` without `X-Step-Up-Token` returns 401 with `error: "step_up_required"`, or that a validation failure produces the documented `details[]` shape. §1.1 is exactly the kind of defect a thin supertest pass over each route would have caught.

---

### 5.6 A shipped feature and a standing proposal claimed the same path — and the merge decided it

**Added 2026-09-09. Resolved 2026-09-10, by the branch merging rather than by anyone deciding.**

`openapi.admin.proposed.yaml` had reserved `/admin/reports/{reportId}` for Module 4's moderation-report detail since 5 August. The branch `feat/admin-reports` implemented `GET /admin/reports/{id}` as a *generated CSV report*. Same path, unrelated resources.

**The timing is the lesson.** This section was written on 2026-09-09 saying "whichever merges first silently takes the name", and recommending the decision be made *before* the merge. The branch merged as `434d5e6` at **23:02 UTC that same evening** — roughly seven hours later. The recommendation was correct, actionable, and had no chance of being acted on, because nobody reading it had until the next morning.

Nothing broke: no client consumed either path, so the resolution was a rename inside a proposal file (`admin-api-rfc.md` §5.4b). But the general shape is worth keeping. **A conflict noticed by a human review pass is noticed on that pass's cadence — daily, here — while a merge happens on the branch author's cadence, which can be hours.** A check that runs on push is not a nicer version of the review; it is the only one of the two that is fast enough.

The renamed proposal now also renames its schemas — `Report` → `ChatReport`, `ReportDetail` → `ChatReportDetail` — because the collision had already reproduced itself one level down, in the shared schema namespace, where the audit caught it as a cross-file divergence rather than as the naming problem it actually was. **A path collision between two meanings of a word will collide again in every namespace that word touches.**

This is not a mistake by either author — the proposal is a year-old design document and the branch is this week's work, and nobody read one against the other. It is a structural gap worth one cheap habit: **`/admin/reports` was never a good name for either of them.** "Report" means both "a complaint about a user" and "an exported dataset", and the admin API now needs both.

Two mitigations, in order of cost:

- **Grep the proposed specs for the path before naming a new controller.** Four files, one `grep -n "'/admin/<segment>"`. It costs seconds and it is the only check that catches this class of collision before the merge rather than after.
- **A CI check** that fails when a route in either service matches a path in the *proposed* spec for a different operation. The audit already extracts routes and parses all four specs, so it is a small addition to work already done — and unlike most lint rules it catches a design problem rather than a formatting one. **Run on push, not on the daily audit**, for the reason above: the daily pass found this one and was still a day too slow.

For this specific case the resolution is recorded in `admin-api-rfc.md` §5.4b: Module 4's workflow operations now sit at `/admin/chats/reports/{reportId}`, where the shipped queue already lives.

### 5.7 A commit labelled `otp fix` fixed nothing, and deleted four safety rationales (2026-09-16)

`5843ccf otp fix` in `beevia-api` touches `auth.service.ts` and `otp.service.ts` and changes **no behaviour whatsoever**. Diffed with `-w` and with comment lines filtered out, the entire remainder is line-wrapping: multi-line import braces, a wrapped `ForbiddenException` literal, a wrapped `verify()` signature. It is a Prettier pass wearing a bug-fix label.

What it did remove is four comment blocks, and all four documented *why* the code around them is safe:

- on `login()`, that the response is deliberately identical whether or not the account exists, **to avoid phone-number enumeration** — and separately, why the falsy check rather than `!== null` (the DAL is typed `Row | null` but returns `undefined` on a miss);
- on `verifyOtp()`, that `assertCanSignIn` is the *real* gate because a code may have been issued before the account was stopped, or through another purpose;
- on `sendOtp()`, that the Slack echo is gated on `OTP_ECHO` and **must never fire unconditionally, because that would post live OTP codes for real users into Slack in production** — which is §1.2 on this list, still open.

Two separate problems, both cheap to avoid:

- **The message is wrong.** A reader scanning `git log` for the OTP behaviour change that this cycle's board items describe will open this commit and find nothing, or worse, assume the OTP path was fixed. Formatting passes should say so and should not ride along with a domain noun.
- **Deleting a rationale is a real change even when the bytes around it are not.** Each of those comments answers a question that a future reader will otherwise re-derive or, more likely, guess — and one of them is the only in-code marker on the single most dangerous config flag in the service. If the project wants Prettier to own this file, run it as its own commit; the comments should survive it either way, since Prettier does not remove comments on its own.

### 5.8 A green pipeline shipped a release that could not boot (2026-09-18)

**The strongest single piece of evidence §5.4 has produced, and it arrived as a production incident rather than an argument.**

Sequence, from the commits and their messages:

| Time (UTC) | Event |
|---|---|
| 17 Sep 02:58 | `sentAt: z.coerce.date()` added to the reported-message DTO (`dc53f63`, §5.9 of `api-rfc.md`) |
| 18 Sep 03:55–04:34 | NestJS 12 upgrade + validation moved to Nest 12's Standard Schema support |
| 18 Sep 10:28 | PR #47 merged to `main`. **CI green.** |
| — | The deploy rolled back: the new release never bound `:3000`, the health check failed, the previous release was reactivated |
| 18 Sep 11:29 | PR #48 merged — `fix(openapi): render Zod dates instead of crashing the boot` |

`@nestjs/swagger` 12 derives request schemas from the Zod schema a route carries, asking Zod for JSON Schema with Zod's defaults — and those **throw** on any type JSON Schema cannot express. `z.coerce.date()` is one such type. `SwaggerModule.createDocument()` runs at boot, so **one optional field on one route took the process down before it could listen.**

Three things are worth extracting, in increasing order of importance.

**1. The failure mode was the bad one.** The app stayed up on old code and nothing looked down. A crash-loop announces itself; a rolled-back deploy behind a passing health check on the previous release looks like a quiet afternoon. The commit message says this plainly, which is to its credit.

**2. The fix chose the honest option.** Narrowing `z.coerce.date()` to an ISO string would also have made the document render — and would have quietly stopped accepting the epoch numbers and offset timestamps the route takes today, i.e. a wire-contract change smuggled in as a crash fix. Instead the conversion goes through a `zodOpenApiConverter` with `unrepresentable: 'any'` and a `date` override rendering `{ type: string, format: date-time }`. Validation is untouched. That is the right call and it is worth naming, because the wrong one was cheaper.

**3. CI was green because nothing ran `main.ts`.** This is the general finding. The e2e suites boot `AppModule` through `Test.createTestingModule` and never call `SwaggerModule.createDocument`, so a schema Swagger cannot render **throws nowhere in the pipeline and everywhere in production**. Every test passed, on code that could not start.

The same commit added `openapi-schema.spec.ts`, which builds the document the way `main.ts` does and asserts the date renders. **That closes the class, not just this instance**, and it is the single most valuable file added this cycle — any future schema the document cannot express now fails in CI instead of at a health check.

The remaining gap, and it is small: **the new spec builds the document but does not compare it to the committed `openapi.yaml`.** That is the other half of §5.4, and the boot check has now paid for the infrastructure it needs — the document is already constructed in a test. Diffing it against the committed file, and failing on a difference, is a few more lines in a file that already exists and would close the contract-drift class §5.4 has been arguing for since 3 September.

**A second, narrower lesson for the upgrade itself.** Nest 12 runs global guards for gateway handlers as well as HTTP routes, which Nest 11 did not. `JwtAuthGuard` read `switchToHttp().getRequest().headers.authorization` unconditionally, so every WebSocket message threw a `TypeError` before its handler ran and the chat e2e suites hung on events that were never coming. The fix stands the guard aside for non-HTTP contexts, which is correct rather than a relaxation: the socket is authenticated on its handshake by `WsPrincipalService`, and `handleConnection` calls `socket.disconnect(true)` when that fails — verified at `messaging.gateway.ts:156`. Per-message re-authentication was not happening on Nest 11 either, because the guard never ran there. Worth recording because "a guard now runs where it did not before" is exactly the kind of major-version change that is safer to find in a test than in an incident, and this one was found by a hanging suite rather than by reading the changelog.

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
| **No deletion status.** `DELETE /users/me` acknowledges synchronously while partner deletion is asynchronous. | Flow 8 explicitly requires "deletion in progress", "not a silent failure". **Corrected 2026-09-02:** this row used to add that "the `user_status` enum already has a `deleting` value that nothing reads" — migration `0027` (2026-08-06) renamed it to `deactivated` for the admin deactivate path, so there is now no in-flight state at all and the work is larger than this row implied. |
| **`account_resolution` has no endpoint.** | The payee's account name is returned only *after* the debit, so a user cannot confirm who they are paying. |
| **Message deletion is modelled but unreachable.** `message_delete_scope` and `deleted_for` exist; no route sets them. | Flow 1 lists deletion as an expected thread action. |
| **Translation is stateless only.** | §8.1 requires per-conversation *and* global opt-in; the preference cannot survive a reinstall. |

---

## 7. Supply chain and repository integrity

Added 2026-09-07, after `origin/main` of `beevia-api`, `beevia-admin-api` and `beevia-db-schema` was force-pushed with a malware loader appended to `eslint.config.mjs`. Full incident detail is in `project-status/project-status-2026-09-07.md` §0; this section is the durable engineering lesson, not the incident log.

### 7.1 `main` was force-pushable

The single control whose absence turned a stolen token into a rewrite of three repositories' history. **Enable branch protection on all five repos with force-push disabled and deletion disabled**, require a pull request to `main`, and enable signed commits if the org plan allows it. This is a settings change, not an engineering task, and it is the highest value-per-minute item in this document.

The rewrite was also detectable in seconds and nobody was watching: `git reflog show origin/main` printed `forced-update` on all three. A CI job or a scheduled script that alerts when the default branch's history is not a fast-forward of its previous state is a few lines and would have raised this at the moment it happened.

### 7.2 Config files are executable code, and nothing treats them that way

The payload lived in `eslint.config.mjs`. That is a JavaScript module, executed by any lint invocation — `npm run lint`, a pre-commit hook, an editor integration, a CI job. Two properties made it a good hiding place, and both generalise beyond this incident:

- **The file exempts itself from linting.** Its first line is `globalIgnores(['eslint.config.mjs'])`, so no lint run will ever inspect it.
- **The payload was appended to the last line**, after a long run of tab characters. In a diff view the line reads as unchanged; in an editor it is off-screen.

The same is true of `jest.config.js`, `next.config.js`, `vite.config.*`, `postcss.config.js`, `tailwind.config.js` and every `package.json` lifecycle script. **Review them with the same care as application code**, and consider a CI check that fails on any config file exceeding a sane line length or byte size — a 9 KB ESLint config is not a thing that happens by accident.

### 7.3 Lockfiles and install scripts

`npm ci` runs arbitrary `postinstall` scripts from every transitive dependency. Given a compromise of this shape, the cheap hardening is `npm config set ignore-scripts true` in CI with an explicit allowlist for the packages that genuinely need to build, plus `npm audit signatures` to verify registry provenance. Neither would have stopped this particular payload, but both narrow the next one.

### 7.4 The spec pipeline cannot see this class of problem — and one guardrail could

For the second consecutive cycle the most serious finding touched no route, no DTO, no schema and no spec. §5.4's recommendation — generate both services' OpenAPI documents and diff them in CI — closes *contract* drift. It does not close behaviour drift (the Anchor webhook no-op, 3 Sep) and it does not close *supply chain* drift. Three distinct classes, one instrument.

What actually caught this was `sync_repos.py` refusing a non-fast-forward merge. That rule exists so the refresh pipeline never creates a merge commit in a repository it is only meant to read; it caught a malware push as a side effect, because **"the remote's history changed shape" and "the remote is hostile" produce the same signal**. The generalisable version: *prefer tooling that fails closed on an unexpected repository state rather than reconciling it automatically.* A `git pull` with default settings would have merged the payload into this workspace without comment.

### 7.5 Rotate on the assumption of workstation compromise, not remote compromise

The payload reached `origin/main` in a commit that also contained genuine, well-written application work (`09fda4f`, the admin dashboard endpoint). That means it was authored on a machine whose working copy already held the malicious file — so the remote is a symptom. **Cleaning the remote without cleaning the workstation does not hold**, because the next legitimate commit re-introduces the file. Credential rotation should assume everything that machine could read: GitHub and npm tokens, both services' `.env` files, and the Anchor, Paystack, Entrust and database credentials in them.

### 7.6 Cleaning `main` is not cleaning the repository

**Added 2026-09-08, after the remediation. Closed 2026-09-09.** `main` was rebuilt on all three repositories and is now verifiably clean. On 2026-09-08 `beevia-admin-api` still had **eight other remote branches carrying the payload**, byte-identical.

**As of 2026-09-09 they are gone.** Seven were deleted and `feat/admin-chats` — the only one with unique content — was merged onto the clean history rather than discarded, which is exactly the disposition §7.6 recommended and the one that preserved an entire module (`admin-api-rfc.md` §3.13). A full-history sweep of **every remote ref in all five repositories** now finds only the two known-good `eslint.config.mjs` blobs (`09fc5b23`, 1485 B, and its `4e9f8271` predecessor, 899 B) in the Node services; the 9167-byte payload is reachable from nothing. The one new branch, `feat/admin-reports`, is clean.

The remediation is therefore complete **on the remote**. Two things this workspace still cannot see, and which are the reason this section stays open rather than being deleted: whether the workstation that authored the poisoned commit has been cleaned (§7.5), and whether branch protection is now enabled (§7.1). Both are invisible from a git clone.

The lesson below is kept in full, because it is the part that generalises.

That is the durable lesson, and it is not specific to this incident. A force-push cleanup naturally targets the branch everyone looks at, and every long-lived feature branch that was cut from, or rebased onto, the poisoned tip keeps its own copy. Three consequences follow:

- **The payload is still one `git checkout` away.** Anyone resuming work on a feature branch, and any CI job triggered by a push or PR from one, loads the malicious config and executes it. The exposure did not end with the `main` rebuild.
- **A merge re-infects `main`.** These are open feature branches. Merging one without rebasing onto the clean history reintroduces the file into the branch the cleanup just fixed.
- **A repo-wide sweep is the only check that answers the question.** "Is `main` clean" and "is the repository clean" are different queries. The second is one command:

  ```bash
  git for-each-ref --format='%(refname:short)' refs/remotes/origin/ |
    while read b; do
      s=$(git rev-parse "$b:eslint.config.mjs" 2>/dev/null) || continue
      echo "$b $(git cat-file -s $s)"
    done
  ```

  Run it against every ref, not just the default branch, and compare blob hashes rather than eyeballing diffs — the payload is appended after a run of tabs and is invisible in a diff view (§7.2).

The generalisable rule: **after any history-rewrite remediation, enumerate every ref and every reachable object, and verify by content hash.** Then delete the branches that cannot be salvaged rather than leaving them for someone to find later, because a stale infected branch is indistinguishable from an active one in the GitHub branch list.

### 7.7 `beevia-admin` has no CI at all — not a missing control, a missing directory (2026-09-16)

Previous editions recorded this as "`beevia-admin` and `beevia-mobile` are missing the two org security workflows". Checked properly at `origin/main` today, the two repos are not in the same situation:

| Repo | `.github/workflows` | `dependabot.yml` |
|---|---|---|
| `beevia-api` | `pr` · `release` · `secrets-scan` · `semgrep` · `supply-chain-guard` · `test` | ✅ |
| `beevia-admin-api` | `ci` · `deploy` · `postman-sync` · `secrets-scan` · `semgrep` · `supply-chain-guard` · `sync` | ❌ |
| `beevia-db-schema` | `ci` · `release` · `secrets-scan` · `semgrep` · `supply-chain-guard` · `sync` | ❌ |
| `beevia-mobile` | `flutter-ci` · `main` · `pr` — `secrets-scan`, `supply-chain-guard` **and** `semgrep` absent | ✅ |
| **`beevia-admin`** | **no `.github` directory exists** | ❌ |

**Updated 2026-09-18.** `semgrep.yml` landed in the three backend repos on 18 Sep 03:05 UTC (`BVA-I270`), running `semgrep ci` on `pull_request`, `push` to `main`/`master` and a daily cron. That is a real improvement and it went in cleanly.

Two qualifications a reader needs, and neither is a criticism of the work:

- **It is advisory, not blocking.** A workflow that runs on a pull request cannot prevent a merge unless it is a *required* status check, and that is a branch-protection setting (§7.1). Until that is configured, Semgrep reports findings that nobody is obliged to act on.
- **The remaining coverage gap is not a scope oversight — it is a permissions wall.** The item's own comment records it: *"this is done on all backend repos but I cannot add it organisation wide yet as I do not have admin access to the organisation."* Branch protection, GitHub secret scanning, push protection and org-wide Dependabot alerts are all org-level settings. **Three of the four remaining security items are gated on a GitHub org-admin grant, not on engineering time**, which is why `BVA-I269` is BLOCKED and `BVA-I272`/`BVA-I273` have not started. Granting that access — or having whoever holds it spend twenty minutes in the org settings — unblocks more security posture than any amount of further workflow authoring.

So `beevia-mobile` is one `cp` away from parity: it already has a working CI surface and is missing two specific workflows. **`beevia-admin` has never had CI of any kind** — nothing lints it, nothing builds it, nothing tests it, nothing scans it, and no status check can be required on a pull request because there is no check to require. It is also the repo whose sole contributor has no board presence, so neither the board nor CI observes the work.

That matters more than the security workflows on their own: branch protection (§7.1) is the control that failed in the September incident, and on this repo there is nothing for branch protection to gate.

Order: add a build/lint workflow to `beevia-admin` first (it is the prerequisite for everything else), then copy `secrets-scan.yml`, `supply-chain-guard.yml` **and now `semgrep.yml`** into both `beevia-admin` and `beevia-mobile`. All are reusable-workflow callers or short YAML files, and none of them needs org access — which makes them the part of the security push that is *not* blocked and is therefore the part worth doing next.

**Updated 2026-09-24 — the three backend workflows became one, in two of the three repos.** `beevia-api` and `beevia-admin-api` replaced `secrets-scan.yml`, `semgrep.yml` and `supply-chain-guard.yml` with a single `code-scan.yml` that calls `Drumbell-Technologies/.github/.github/workflows/code-scan.yml@main` with `secrets: inherit`. The workflow inventory now reads:

| Repo | `.github/workflows` | `dependabot.yml` |
|---|---|---|
| `beevia-api` | `code-scan` · `pr` · `release` · `test` | ✅ |
| `beevia-admin-api` | `ci` · `code-scan` · `deploy` · `postman-sync` · `sync` | ❌ |
| `beevia-db-schema` | `ci` · `release` · `secrets-scan` · `semgrep` · `supply-chain-guard` · `sync` | ❌ |
| `beevia-mobile` | `flutter-ci` · `main` · `pr` | ✅ |
| **`beevia-admin`** | **still no `.github` directory** | ❌ |

Two things follow. **The consolidation is a genuine improvement to the part it covers:** detection now lives in the org `.github` repo, so a rule change reaches every caller on its next run instead of needing a copy edited in each repo, and the secrets scan went from weekly to daily. **But it makes the gap harder to see, not smaller.** `beevia-db-schema` is now the odd repo out with three ageing standalone copies, and the recommendation below is now cheaper than when it was written — copying one four-line `code-scan.yml` caller into `beevia-mobile` and `beevia-admin` replaces copying three files each. Nothing about the org-permissions wall changed, and neither front-end repo gained a workflow today.

`beevia-mobile` also still carries **nine unmerged Dependabot branches**, the oldest from 11 August (38 days). `BVA-I271` ("check and fix any vulnerabilities already found") was moved to REVIEW/QA on 18 Sep against the three backend repos; the nine open dependency bumps in the repo with the largest attack surface and the least CI are untouched by it. Merging or closing those nine is the cheapest unblocked security work available, and it requires no permissions anybody lacks.

**Updated 2026-09-29 — the scans now run on pull requests only, and nothing yet guarantees every change is a pull request.** `beevia-api` #59 (merged 28 Sep 16:39 UTC, `e8377de` "ci: scan on pull requests only, no cron") removed both the `push` trigger and the daily `cron` from `code-scan.yml`; it now runs on `pull_request` and `workflow_dispatch` only. The same change is written, unmerged, for the other two backends: `beevia-admin-api` `origin/ci/node-26-only` (`66737d7`) and `beevia-db-schema` `origin/ci/pr-only-no-cron` (drops the schedule from its three standalone scan workflows as well). The commit's reasoning is sound as far as it goes — on a merge the push run re-scanned the tree the pull request had just passed — and it is cheaper. Two things it gives up:

- **A direct push to `main` is now never scanned.** That is only safe if `main` requires a pull request, which is §7.1's branch protection — still unverified from here, and shown on 28 Sep *not* to prevent force-pushing `beevia-db-schema`'s `main`. The removed comment recorded the purpose plainly: *"so a payload or a credential committed to a quiet branch surfaces within a day"*. The September payload arrived by exactly that route.
- **A quiet repository is never re-evaluated.** Semgrep rules and supply-chain advisories change while the code does not; a scheduled run is what surfaces a newly disclosed problem in an unchanged lockfile.

The cheap middle ground: keep a **weekly** schedule on the default branch, and restore the `push` trigger on `main` until branch protection requiring a pull request is confirmed. Neither needs org access.

**Updated 2026-09-30 — in `beevia-db-schema` the same assumption now gates a production migration, not just a scan.** `beevia-db-schema` #19 (`de06516`, merged 30 Sep 02:14 UTC) moved `ci.yml` and the three scan workflows to `pull_request` only, as `beevia-api` #59 did. Because Release used to wait on CI (`workflow_run` + `conclusion == 'success'`), it also rewired **Release to trigger on every `push` to `main` directly**, and removed both the success gate and CI's `paths-ignore` list. `sync.yml` ("Migrate the production database", `environment: production`) still runs after every successful Release. The chain is now: **any push to `main` → publish to GitHub Packages → migrate production, with no test, lint or scan in between.** The new comment in `release.yml` states the premise: *"CI is a required check, so anything on main has already passed it."*

That premise is §7.1, and it is unverified. On 28 Sep a forced update to this repository's `main` was observed from here, so a change *can* reach `main` without a pull request. Before #19 such a push still ran CI, and Release waited for it to pass. After #19 it goes straight to production. It is visible already in a benign form: #19 touched only `.github/**`, which the old `paths-ignore` would have kept out of a release, and it produced `be14bc3 chore(release): v0.0.38` 41 seconds after merging. (That bump also closes the version mismatch noted on 28 Sep. `main`'s `package.json` now matches the registry. Tag `v0.0.38` still points at `e285f10`, which is on no branch, and its tree differs from `main`'s only under `.github/`.)

Two options, neither of which needs org access: **(a)** have Release run CI's `verify` job itself before publishing (a `needs:` on a reusable job, not a second `workflow_run`), so a direct push is tested before it can migrate anything; or **(b)** keep the new trigger but confirm, in the GitHub UI, that `main` on `beevia-db-schema` requires a pull request with the CI check required and force-push disabled, and record that confirmation somewhere a reader can find it. (a) is the one that does not depend on a setting nobody here can see.

**The same rewiring is waiting for `beevia-admin-api`.** Its pending branch `origin/ci/node-26-only` (`66737d7`, "check on pull requests only, and trigger the deploy chain from push") makes `sync.yml` ("Sync source") fire on any push to `main`, and Deploy still follows it. It rests on the same sentence: *"CI is a required status check, so a commit cannot reach main without it having passed."* Apply (a) there before it merges.

### 5.9 The backend's own Postman pass found a spec error §5.4 could not, and a "package update" deleted the integration docs (2026-09-22)

Two findings from the 18–21 September commits, both of the "label says one thing, content does another" kind.

**1. `GET /admin/users` has never matched its spec.** `e128cc6` (21 Sep, Postman docs only) probed every admin list route on a running service and reported **four** pagination envelopes, not the one its first pass assumed. Checked against `origin/main`: `users.service.ts:94` calls `buildResponse({ items, page, limit, total, totalPages }, 'Users')` with no `meta` argument, so the wire shape is `data.items` + `data.total_pages` with no `meta` at all. `openapi.admin.yaml` had described it as `data: AdminUserSummary[]` + `meta: PaginationMeta` since 4 August. The dashboard was never misled, because `beevia-admin` reads `data.data.items` and `data.data.total_pages` — it was written against the running service, not against the spec. **Corrected in `openapi.admin.yaml` on 2026-09-22.** This is the fifth contract-level drift the route-level audit could not see (§5.4), and the first one found by the backend team rather than by this pipeline. It is the same argument again: a document generated from the app, and diffed in CI (§5.8's `openapi-schema.spec.ts` is most of the way there), would have caught it on 4 August.

**2. `081441c chore: package update` (`beevia-api`, 18 Sep) deleted `docs/` in full.** Five files, 1,719 lines: `mobile-integration-handoff.md`, `chat-websocket-integration.md`, `encryption-model.md`, `calls-integration.md` and `tier-upgrade-integration.md`. The commit message says nothing about it, the diff also rewrites `package.json` and the lockfile, and nothing at `origin/main` replaces them — `README.md` and `deploy/README.md` are the only Markdown left. This is §5.7's pattern at a larger scale: the deletion may well be intended (the Postman collection is now the richer reference for the admin service), but `encryption-model.md` and `mobile-integration-handoff.md` were the consumer API's only written account of the E2EE contract and of what the Flutter client has to send — exactly what `BVA-I254` (the client half of the report flow) needs. Either restore them, move them somewhere named, or say in a commit that they were retired and why. They are recoverable with `git show 081441c^:docs/<file>`.

### 5.10 The client checks its contract against a vendored copy of the spec that is 27 operations stale (2026-09-25)

`beevia-mobile` carries its own copy of the consumer spec at `api-docs/openapi.yaml`, and `test/mock/spec_contract_test.dart` checks the mock server against **that file**, not against the spec this workspace maintains. The copy was last touched on 21 September (`eeaa2dc`).

Diffed against `openapi.yaml` at `origin/main` today, the vendored copy is missing **27 of 137 operations**, including every one of the thirteen `/cards/*` routes, all three `/topups` routes, `/wallets/banks`, `/wallets/resolve-account`, both `/wallets/transfers` reads, `GET /translate/languages` and the three per-conversation translation-preference routes. Its `LedgerEntry` also predates the transaction-naming work, so it has neither `name` nor `counterparty_name`.

Two consequences, and the second is the expensive one:

1. **The contract test passes while the client is coded against a seven-day-old API.** It is not a weak test — it has a `nowDeclared` guard that fails when an allowlisted drift entry reappears in the spec — but every check it makes is relative to a file that no longer describes the service.

2. **It produced a wrong claim in a merged PR.** `Deps updates 2026-09-22` (#36, merged 24 Sep) added `/wallets/banks`, `/wallets/resolve-account` and `/cards` to a `knownSpecDrift` allowlist on the stated grounds that they "aren't yet declared in openapi.yaml". All three **are** declared, and have been for weeks — they are absent only from the vendored copy. So three endpoints that the canonical spec describes are now on a list that suppresses drift warnings about them.

This is the same class as §5.4, one layer out: §5.4 asks the server to prove its spec matches its code, and this asks the client to read the spec the server publishes. The cheap fix is to stop vendoring — fetch `openapi.yaml` from the API repo in CI, or make `api-docs/openapi.yaml` a checked sync with a job that fails when it falls behind. The expensive version of not fixing it is a client written against endpoints and fields that the server has already moved past, which is precisely what `BVA-I262` is: the mobile half of a bug whose server half shipped on 24 September, against a vendored contract that does not contain the two fields the fix added.

**Update 2026-09-28 — the vendored copy has now been edited in the other direction.** The unmerged `beevia-mobile` branch `update-fixes` still does not sync the 27 missing operations, but it *adds* something to `api-docs/openapi.yaml` that the server does not implement: a `{ method: biometric }` body on `POST /auth/step-up` (§5.11). The mock server was taught the same body. So the vendored spec is no longer only stale; it now declares server behaviour that does not exist, and the contract test certifies the client against it.

### 5.11 The client asks for a biometric step-up the server does not offer — and should not offer in that shape (2026-09-28)

`beevia-mobile` `origin/update-fixes` (unmerged; last commit 27 Sep) adds `WalletService.requestBiometricStepUpToken()`, which posts `{ "method": "biometric" }` to `POST /auth/step-up` after a local `local_auth` prompt succeeds. It is offered next to the PIN on five confirmation sheets — both chat money flows, bank transfer, virtual-card request and a wallet sheet — i.e. on every money-moving action the client has. Its doc comment says "the server accepts this only for a biometric-enabled, registered device".

**The server accepts nothing of the kind.** `stepUpSchema` on `origin/main` is `z.object({ pin })`; there is no `method` field and no biometric path anywhere in `src/`. On the real API this request fails validation, so the biometric button will fail every time it is pressed outside mock mode. The client's mock server (`lib/mock/http/routes/auth_routes.dart`) *does* accept it, and the branch edits the vendored spec to match (§5.10), so no test in the client repo will notice.

**The more important point is that it should not simply be added as written.** The PRD asks for "biometric or PIN confirmation on every financial action" (§11 Phase 3), so the requirement is real. But a request that says "the user passed a biometric prompt" is a claim the server cannot check: anyone holding an access token can send the same body. Minting a step-up token for it would reduce ADR-0003's PIN gate to "has a session", which is precisely the guarantee step-up exists to exceed. The standard shape is a **device-bound key**: at enrolment the device generates a keypair inside the secure enclave/keystore, gated by biometrics, and registers the public key; at step-up the server issues a nonce and the device returns a signature that the enclave only produces after a successful biometric prompt. The server verifies the signature against the registered key. That needs a small design decision and two endpoints, and it is worth making before the client ships a button that implies it already exists.

Until then: either hide the biometric option outside mock mode, or keep the PIN as the only factor the client offers for step-up.


## 8. Suggested order

1. ~~**§7.6** — delete or rebase the eight `beevia-admin-api` branches that still carry the payload.~~ **Done 2026-09-09**: seven deleted, one merged, and a full-ref sweep across all five repos finds the payload nowhere. What is left of §7 is items 2 and 3 below, which are the two nobody outside the team can verify.
2. **§7.1** — branch protection with force-push disabled, on all five repos. Minutes, and it is the control that failed. Cannot be verified from this workspace — the GitHub token available here has no access to the org's repositories — so confirm it in the GitHub UI rather than assuming it. **Escalated 2026-09-18 and it is no longer an engineering task:** the board item for it (`BVA-I269`) is BLOCKED because the person assigned does not hold GitHub org-admin access (§7.7). It now also gates §7.1's own value *and* Semgrep's — a scan that cannot be a required check cannot stop anything. Whoever holds org admin should either use it or delegate it; nothing else on this list is blocked on a single permission grant.
3. **§7.5** — rotate every credential reachable from the affected workstation and CI, if that has not already happened.
3a. **§7.7** — give `beevia-admin` a CI workflow at all. Listed here rather than further down because it is the prerequisite for items 2 and 3 having any effect on that repo, and because "add the two security workflows" — the ask carried for several editions — cannot be done meaningfully until there is a `.github/` to put them in.
3b. **§7.7 continued** — copy `secrets-scan.yml`, `supply-chain-guard.yml` and `semgrep.yml` into `beevia-mobile`, and merge or close its nine stale Dependabot branches. Promoted on 2026-09-18 because it is the largest piece of security work that needs **no** org permission, in the repo with the least CI coverage. **2026-09-29:** before the pending CI branches on `beevia-admin-api` and `beevia-db-schema` merge, keep a weekly scheduled scan and the `push` trigger on `main` (§7.7, last update). `beevia-api` has already dropped both. **2026-09-30:** `beevia-db-schema`'s branch merged as #19 and went further. Release, and therefore the production migration, now triggers on any push to `main` with no CI gate. Make Release run the verify job before publishing (§7.7, 2026-09-30 update).

3c. **§5.8** — extend the new `openapi-schema.spec.ts` to diff the generated document against the committed `openapi.yaml`. Promoted because the expensive half now exists: a green pipeline shipped an unbootable release on 18 September, the fix built the document in a test to stop it recurring, and turning that into §5.4's drift check is a few more lines in a file that is already there.

3d. **§5.10** — stop vendoring the spec in `beevia-mobile`, or add a CI job that fails when `api-docs/openapi.yaml` falls behind the API repo's. Grouped with 3c because they are the same instrument pointed in opposite directions, and because the client copy is currently 27 operations behind — including every field the open `BVA-I262` fix needs.

3e. **§5.11** — decide the biometric step-up design (device-bound key and signed nonce) before `beevia-mobile` `update-fixes` merges with a biometric button that the real API rejects. Added 2026-09-28. Paired with **§3.6**, which the same branch makes load-bearing: once it merges, every chat payment goes through the one unparsed phone field.

4. **§4.7** — re-apply module scoping when a generated report is read, not only when it is generated. Cheapest now, and the only entry on this list that is a live access-control gap in shipped code. **Unchanged on 2026-09-18** — `reports.service.ts:133` re-verified at `origin/main`; ninth consecutive edition.
5. **§1.1** — malformed UUID → 500. Small fix, trivially reachable, currently generates false 500s in monitoring.
6. **§1.2** — enforce `OTP_ECHO` off in production at startup.
7. **§4.1** — rate limiting, especially PIN verification and `GET /keys/{userId}`.
8. **§7.2** — review config files as executable code; add a size/length check in CI.
9. **§2.1** — un-ignore the design documents, or make the references resolve.
10. **§4.4 / §4.5** — health probe and request ids, before public launch.
11. **§1.4 / §5.3** — reconcile Postman with the code and add a drift check.
12. **§4.2 / §4.3** — CORS allowlist and security headers.
13. **§7.3** — `ignore-scripts` in CI with an explicit allowlist.
14. **§5.1** — collapse the Zod/DTO duplication before it drifts further.
15. **§3.x** — status codes, phone validation, webhook grouping; batch into one consistency pass.
16. **§6** — the product gaps, sequenced in `api-rfc.md` §8.
