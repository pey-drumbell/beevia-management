# Beevia — shared testing principles

Applies to every Beevia repo. Repo-specific rules build on this; where they
conflict, the repo-specific rule wins.

---

## 1. The coverage contract

**Target: 100% coverage of code that can break. Zero coverage theatre.**

Those two goals only conflict if "coverage" is measured over the wrong
denominator. So we shrink the denominator honestly, then hold the line at 100%.

**In the denominator — must be covered:**

- Business logic: services, use-cases, calculators, state machines.
- Anything touching money, balances, fees, or ledger entries.
- Authentication, authorisation, guards, permission checks.
- Validation schemas and their boundaries.
- Data mapping / serialisation (API ⇄ domain ⇄ DB, CSV/export writers).
- Error handling paths, retries, idempotency keys.
- Pure utilities.

**Out of the denominator — exclude in the coverage config, with a comment
saying why:**

- Framework bootstrap: `main.ts`, `*.module.ts`, `app.dart`, providers wiring.
- Generated code: `lib/gen/**`, `*.g.dart`, `drizzle/**` SQL, `dist/**`.
- Type-only files, barrel `index.ts` re-exports, constant tables.
- Declarative decorator/metadata surface (Swagger `@Api*`, DTO class shells).
- Config objects and seed scripts.
- Third-party SDK shims that contain no branching.

If something is excluded and it later grows an `if`, it comes back into the
denominator. Exclusion is a statement about the code, not a convenience.

**Thresholds are a floor, not a target.** Set them at the current measured
value and ratchet upward. Never lower a threshold to make a build pass — either
write the test or justify a new exclusion in the PR.

## 2. The overkill test

Before writing a test, answer: **"If I broke this line, would this test fail?"**
If no, the test is decoration — delete it. Concretely, do not write:

- Tests that assert a mock was called with what you just told the mock to
  expect, and nothing else.
- Tests that a getter returns the field it was constructed with.
- Tests that the DI container injects (that is the framework's job — a
  compile/boot failure already catches it).
- Snapshot tests of large render trees or JSON blobs. A snapshot that nobody
  reads is a rubber stamp. Snapshot only small, stable, deliberately-frozen
  output.
- Tests of private methods. Reach them through the public surface, or the
  method wants to be its own unit.
- Duplicate tests at multiple levels: if a branch is proven in a unit test, the
  e2e does **not** re-prove it. E2E proves the wiring, once.

**One behaviour per test.** Multiple `expect`s are fine when they describe one
behaviour; two behaviours means two tests.

## 3. Reaching the last branches cheaply

Branch coverage is where suites bloat. Use these, in order:

1. **Table-driven cases** for pure functions and validation — one `it.each` /
   loop covers a dozen branches in ten lines.
2. **Boundary values only.** For a `min <= x <= max` clamp, test `min-1`, `min`,
   `max`, `max+1`. Not seven values in the middle.
3. **Equivalence classes.** All rejected phone formats fail through the same
   line; one representative per class, not one per format.
4. If a branch is genuinely unreachable, delete the branch — do not write a
   contorted test to reach dead code.

## 4. Test naming and shape

Name tests as sentences describing behaviour, matching the existing house
style in `beevia-api`:

```ts
describe('FeeService.computeFee', () => {
  it('is free for internal (Beevia↔Beevia) movements', ...);
  it('clamps up to min_fee', ...);
});
```

Not `it('should work')`, not `it('test 1')`, not `describe('computeFee')` with
`it('returns 200')`. A reader scanning `describe` output should learn the spec
of the unit without opening the source.

Structure every test as **arrange / act / assert**, in that order, with the
arrange collapsed into a named `setup()` helper once it exceeds ~5 lines.

## 5. Test doubles

**Prefer hand-written fakes over mocking frameworks.** The established pattern
in this codebase — keep it:

```ts
function setup(config: Partial<FeeConfig> | null) {
  const dal = {
    feeConfigs: { findActive: () => Promise.resolve(...) },
  } as unknown as DalService;
  return new FeeService(dal);
}
```

Rules:

- **Mock at the boundary you own, not the module under test.** Stub the DAL,
  the HTTP client, the SDK — never the service you are testing.
- **Never mock what you can construct.** Value objects, DTOs, and pure
  functions get real instances.
- **Never let a test hit the real network, a real clock, or real randomness.**
  Freeze time (`vi.useFakeTimers()`), inject clocks/ID generators, or assert on
  shape rather than value.
- One `setup()` per spec file, parameterised. Do not build a shared
  cross-file test framework; it becomes a second codebase to maintain.

## 6. The pyramid we actually want

| Level | What it proves | Cost | Where |
| --- | --- | --- | --- |
| **Unit** (majority) | Every branch of one unit's logic | ms, no I/O | colocated with source |
| **Integration** (targeted) | Real DB/transaction semantics: atomicity, constraints, idempotency, concurrency | seconds, needs Postgres | `*.int.spec.ts`, skips when DB unreachable |
| **E2E** (few) | The wiring and the contract, one happy path + one auth failure per vertical | tens of seconds, serial | `test/*.e2e-spec.ts` |

**Do not** simulate a database in a unit test to prove a database property.
Transactionality, unique constraints, and race conditions are only real against
a real Postgres — that is what `*.int.spec.ts` is for, and it is mandatory for
ledger/money code.

## 7. Determinism is non-negotiable

A flaky test is worse than no test: it trains the team to ignore red.

- No `sleep`/arbitrary waits. Await the condition, not the clock.
- No dependence on test execution order or shared mutable module state.
- Integration tests generate a **unique per-run prefix** for any value with a
  uniqueness constraint (the `RUN` pattern in `ledger.service.int.spec.ts`) and
  clean up in `afterAll`.
- E2E specs that boot a full app run with `fileParallelism: false` (already
  configured) — keep it that way.
- If a test fails intermittently, fix it or delete it the same day. Never
  `retry`, never `skip` it into the backlog without a linked ticket.

## 8. Definition of done for any change

A change is not done until all of these hold:

- [ ] New/changed behaviour has a test that fails without the change.
- [ ] Every new branch is covered, or explicitly excluded with a reason.
- [ ] Bug fixes ship with a regression test that reproduces the bug.
- [ ] Lint (`lint:ci` / `flutter analyze`) is clean — no new warnings.
- [ ] Typecheck passes.
- [ ] The full suite passes locally, not just the new file.
- [ ] No test was skipped, `.only`'d, or commented out to get green.
- [ ] Public API surface changes are reflected in the OpenAPI spec / docs.

## 9. Working agreements for AI-assisted changes

- **Read before writing.** Open the neighbouring spec file first and match its
  structure, helpers, and naming. Consistency beats personal preference.
- **Never change a test to make code pass.** If a test is wrong, say so
  explicitly and fix it as its own reviewed change.
- **Never delete or weaken an assertion** (loosening a matcher, removing a
  case, widening a type) to get green. Flag it instead.
- **Do not add dependencies to write a test.** The stack already has what is
  needed. Propose a new library separately, with a reason.
- Report honestly: if the suite fails, show the output. "Tests pass" must mean
  the command was run and it passed.
