# beevia-admin-api — agent rules

The backoffice API behind the Beevia admin panel: staff accounts, RBAC, user
console, exports. NestJS 11 + Drizzle via `@drumbell-technologies/beevia-db-schema`.
No Redis, no queue, no sockets — a smaller surface than `beevia-api`, but a more
dangerous one: every endpoint here is a privileged action taken against a real
customer's account.

Read `../agent-rules/shared-testing-principles.md` first. This file adds what is
specific to this repo.

---

## 1. Commands

```bash
pnpm lint:ci      # check-only
pnpm typecheck
pnpm build
pnpm test         # vitest run — src/**/*.spec.ts
pnpm test:cov
pnpm test:e2e     # test/**/*.e2e-spec.ts, serial, boots the full Nest app
pnpm db:migrate
```

Before a PR: `pnpm lint:ci && pnpm typecheck && pnpm build && pnpm test`. Add
`pnpm test:e2e` for anything touching controllers, guards, or module wiring.

## 2. Conventions

- Colocated `*.spec.ts` next to source; e2e in `test/*.e2e-spec.ts`.
- `globals: true` — do not import `describe`/`it`/`expect`.
- SWC transformer (`oxc: false`) is required for Nest DI metadata. Leave the
  vitest configs alone.
- The existing specs under `src/common/`, `src/guards/`, `src/users/` are the
  reference style. Read the neighbour before writing.

## 3. The rule that matters most: authorisation is tested exhaustively

This service exists to gate privileged actions. Coverage of `src/guards/` and
`src/roles/` is **100%, lines and branches, no exceptions.**

For `PermissionGuard` / `AdminAuthGuard` and every role-dependent code path,
test the full matrix, not a sample:

- each role × each permission it **does** grant → allowed;
- each role × a permission it does **not** grant → **403**;
- no token / malformed / expired → **401** (and assert 401 vs 403 is not
  confused — leaking existence is a real finding);
- a permission string that does not exist → denied, never defaults to allow;
- a role with an empty or null permission set → denied;
- superuser/escalated roles, if any, are asserted explicitly rather than
  implied.

Use a table-driven `it.each` over the role×permission matrix so adding a role
adds one row, not one file. **Every new permission added to `roles/` must appear
in that table in the same PR** — a permission with no test is a permission
nobody has checked.

## 4. Privileged actions must prove their audit trail

`user-actions.service.ts`, `verification.service.ts`, and anything that
suspends, reactivates, verifies, or edits a customer account:

- Assert the **effect** (the account state changed), **and**
- assert the **audit/verification-log record was written**, with the acting
  admin's ID, the target ID, the reason, and the timestamp source.
- Assert the **failure path writes nothing**: a rejected action leaves no state
  change and no partial audit entry.

An action test that only checks the happy-path state change is incomplete here.

## 5. Exports and views

- `users-export.service.ts` (CSV): assert the **exact header row**, field order,
  quoting/escaping of values containing commas, quotes and newlines, empty-set
  output, and that no field the admin is not permitted to see appears in the
  file. Exports are the easiest place to leak data.
- `users.views.ts` / `views.ts`: these shape what the panel sees. Test the
  mapping field by field for one representative record, and explicitly assert
  that sensitive fields (tokens, hashes, internal notes not meant for the
  panel) are **absent** — `expect(view).not.toHaveProperty(...)`.
- Assert deterministic ordering. "The list comes back sorted" is a contract the
  UI depends on.

## 6. DTOs and validation

`src/dto/admin.dto.spec.ts` and `src/users/dto/users.dto.spec.ts` are the
pattern. For every zod schema:

- one accepted representative per field;
- one rejection per constraint (min, max, regex, enum, required), table-driven;
- transforms asserted on their output (trim, lowercase), not just acceptance;
- unknown/extra keys: assert the schema's actual strip-or-reject behaviour, so
  a later `.strict()` change is a visible test failure.

## 7. Layer policy

Same as `beevia-api`:

- **Services**: unit spec with a stubbed `DalService`, every branch.
- **Controllers**: no unit spec — covered by `admin-panel.e2e-spec.ts` /
  `users-console.e2e-spec.ts`.
- **Guards, pipes, interceptors, filters**: unit spec, exhaustive.
- **E2E**: one authenticated happy path per vertical, plus **one 401 and one
  403 per vertical**. E2E proves wiring; it does not re-prove branch logic.

## 8. Coverage configuration

Add a `test.coverage` block to `vitest.config.mts` (none today):

- provider `v8`, reporters `['text', 'lcov']`.
- **Exclude**: `src/main.ts`, `src/**/*.module.ts`, `src/views.ts` if it is pure
  re-export, `src/**/*.d.ts`, `dist/**`, `test/**`. Comment each exclusion.
- **Thresholds**:
  - `src/guards/**`, `src/roles/**`, `src/auth/**`, `src/common/**`: **100%**
    lines and branches.
  - `src/users/**`, `src/accounts/**`: 95% lines / 90% branches.
  - global: start at the measured value, ratchet up, never down.

## 9. Cross-repo obligations

- The DB schema is a **published package pinned by exact version**
  (`0.0.14`). Do not point it at a local path or a range to unblock yourself;
  land the schema change in `beevia-db-schema`, release it, then bump here.
- Endpoint or response-shape changes must be reflected in the Swagger
  decorators in the same PR — `openapi.admin.yaml` in the management repo is
  generated from them and is audited for drift.
- Postman collection sync runs in CI (`postman-sync.yml`); keep the repo copy in
  step rather than editing the published collection by hand.

## 10. Things not to do

- Do not stub a guard to `return true` in an e2e to "focus on the handler" —
  that deletes the only test of the thing this service is for.
- Do not assert on error message strings from the framework; assert status
  codes and your own error codes.
- Do not test a service by booting `AppModule`. Construct it with fakes.
- Do not weaken a permission test to accommodate a new role. Add the row.
