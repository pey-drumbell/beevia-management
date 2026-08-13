# beevia-api — agent rules

The customer-facing Beevia API. NestJS 11 + Drizzle (via the shared
`@drumbell-technologies/beevia-db-schema` package) + Postgres + Redis/BullMQ +
Socket.IO. Money is real here — treat it that way.

Read `../agent-rules/shared-testing-principles.md` first; it defines the
coverage contract, the overkill test, and the doubles policy. This file adds
what is specific to this repo.

---

## 1. Commands

```bash
pnpm lint:ci      # check-only — CI fails on violations, never auto-fixes
pnpm build        # nest build
pnpm test         # vitest run — src/**/*.spec.ts
pnpm test:cov     # + coverage
pnpm test:e2e     # vitest run --config ./vitest.config.e2e.ts — test/**/*.e2e-spec.ts
pnpm db:migrate   # required before int/e2e specs on a fresh DB
```

Before opening a PR run, in order: `pnpm lint:ci && pnpm build && pnpm test`.
Run `pnpm test:e2e` too if you touched a controller, gateway, guard, module
wiring, or the queue.

## 2. Layout and file conventions

- Feature folders under `src/<feature>/`, flat — `*.controller.ts`,
  `*.service.ts`, `*.module.ts`, `dto/*.dto.ts`.
- **Unit specs are colocated**: `fee.service.ts` → `fee.service.spec.ts`.
- **Integration specs** end `.int.spec.ts` and live next to their unit spec.
  They run in the same `pnpm test` invocation and **skip themselves** when
  `DATABASE_URL` is unreachable — preserve that behaviour so a laptop without
  Postgres still gets a green suite.
- **E2E specs** live in `test/` and end `.e2e-spec.ts`.
- `globals: true` is set — do not import `describe`/`it`/`expect` from vitest in
  `src/` specs. Match the neighbouring file.
- Vitest uses **SWC, not esbuild** (`oxc: false` + `unplugin-swc`), because Nest
  needs `emitDecoratorMetadata` for DI. Do not "simplify" the vitest config.

## 3. What gets tested, by layer

| Layer | How | Why |
| --- | --- | --- |
| **Services** | Unit spec, stub `DalService`. Every branch. | Where the logic is. |
| **Controllers** | **No unit spec.** Covered by e2e. | They are argument-shuffling + decorators; a unit spec re-tests the framework. |
| **Zod DTO schemas** | Unit spec, table-driven accept/reject per constraint. | Cheap, and they are the input boundary. |
| **Guards / pipes / interceptors / filters** | Unit spec, exhaustive. | Security and response-shape critical; already the pattern in `src/common/` and `src/auth/`. |
| **BullMQ processors** | Unit spec the handler with a fake job object. | Business logic without the broker. |
| **Producers / queue wiring** | E2E (`queue.e2e-spec.ts`). | Only real Redis proves it. |
| **Socket.IO gateways** | E2E with `socket.io-client`. | Handshake + auth + fan-out are the risk. |
| **Ledger / payments / wallets / fees** | Unit **and** `.int.spec.ts`. | See §4. |
| **Provider adapters** (Anchor, Slack, Resend, S3, Firebase, LiveKit) | Unit spec with an injected fake client. Never the network. | See §6. |

## 4. Money rules (non-negotiable)

1. **Never assert on floating-point numbers.** Money is `decimal.js` via
   `src/common/money.ts`. Assert `expect(fee.toString()).toBe('200')`, never
   `toBe(200)` or `toBeCloseTo`.
2. **Every fee/ledger/payout calculation needs boundary cases**: zero, the
   `minFee` clamp, the `maxFee` clamp, a null config, and the internal/free
   path. `fee.service.spec.ts` is the reference — copy its shape.
3. **Rounding is behaviour, not detail.** If a function rounds, there is a test
   asserting the rounding mode at a `.005` boundary.
4. **Double-entry invariants belong in `*.int.spec.ts` against real Postgres.**
   A mocked DB cannot prove them. Required cases for any new money movement:
   - the transaction balances (debits == credits) and is atomic — a failure
     mid-way leaves no partial entries;
   - **idempotent replay**: the same `reference` twice produces one effect,
     including under a concurrent unique-violation race;
   - the USER-wallet balance check rejects overdraw, while system wallets may
     go negative;
   - no double-spend under concurrent debits.
5. **Never mock `DalService` in a test whose subject is a transaction
   boundary.** If the thing under test is "does this roll back", it needs a
   real DB.

## 5. Integration spec hygiene

Follow `src/ledger/ledger.service.int.spec.ts`:

- Generate a unique per-run token and prefix every value that has a uniqueness
  constraint (`reference`, `phone`, system-wallet notes) so reruns against a
  shared dev DB never collide.
- Track created IDs and delete them in `afterAll`. Leave the DB as you found it.
- Guard on DB reachability and `skip` rather than fail when it is down.
- Never assume an empty database, and never `TRUNCATE` a shared one.

## 6. External providers

- **No test may make a real network call.** Inject a fake client at the
  constructor boundary.
- Test three things per adapter: the **request mapping** (our domain → their
  payload), the **response mapping** (their payload → our domain, including the
  fields we ignore), and **error/timeout handling** (what the caller sees when
  the provider 500s).
- **Webhook handlers** (`anchor-webhook.service.ts` and any future one) must
  have tests for: valid signature accepted, **invalid/absent signature
  rejected**, replayed event is idempotent, and unknown event type is ignored
  without throwing. Signature verification failing open is the bug that costs
  money.

## 7. Auth and security tests

Every protected route class and every guard needs, at minimum:

- valid token → allowed;
- absent / malformed / expired token → 401;
- valid token, insufficient scope or missing step-up → 403;
- a token for user A cannot read or mutate user B's resource (**the horizontal
  authorisation test — write it for every user-scoped endpoint**).

`JwtAuthGuard` and `StepUpGuard` already have specs; extend them rather than
inventing a parallel pattern. E2E covers at least one 401 path per vertical.

## 8. Coverage configuration for this repo

`vitest.config.ts` currently sets no coverage block. Proposed starting point —
add under `test.coverage`, then ratchet:

- provider `v8`, reporters `['text', 'lcov']`.
- **Exclude** (each with a comment): `src/main.ts`, `src/**/*.module.ts`,
  `src/**/dto/**` (declarative — but *keep* `*.dto.spec.ts` subjects that carry
  refinement logic in the denominator), `src/common/index.ts`, `src/**/*.d.ts`,
  `dist/**`, `test/**`.
- **Thresholds** — set at today's measured number, then raise:
  - `src/ledger/**`, `src/payments/**`, `src/wallets/**`, `src/fees/**`: **100%**
    lines and branches. These are the money paths; there is no acceptable gap.
  - `src/auth/**`, `src/common/**`: **100%**.
  - everything else: start at measured, target 90% lines / 85% branches.

## 9. API surface changes

The parent `beevia-management` repo audits this repo against `openapi.yaml` and
flags drift. Therefore:

- Any new or changed endpoint, status code, or response shape must be reflected
  in the Swagger decorators **in the same PR** — that is what the spec is
  generated from.
- Changing a response shape without an e2e asserting the new shape is not done.
- The `ResponseInterceptor` / `AllExceptionsFilter` define the envelope; if you
  bypass them with `@SkipResponseInterceptor`, the e2e must assert the raw
  shape explicitly.

## 10. Things not to do

- Do not add a unit spec for a controller "for coverage" — exclude it and let
  e2e cover it, or the suite grows without gaining signal.
- Do not `vi.mock` an entire module to avoid constructing a fake. Construct the
  fake.
- Do not introduce a shared `TestModule` that boots `AppModule` in unit specs —
  it turns a 5ms test into a 3s one and hides the dependency graph.
- Do not widen an e2e timeout to fix a flake. Find the unawaited promise.
- Do not commit `.only`, `.skip` without a linked ticket, or a `console.log`.
