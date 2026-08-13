# beevia-db-schema — agent rules

Beevia's database layer, published as one shared package
(`@drumbell-technologies/beevia-db-schema`): Drizzle schema, migrations, the
typed DAL, and the migration binary. Both APIs pin it by **exact version**.

That makes this repo different from the others: **a mistake here ships to every
consumer at once, and a bad migration is not revertible in production.** The
rules are correspondingly stricter.

Read `../agent-rules/shared-testing-principles.md` first.

---

## 1. Commands

```bash
pnpm lint:ci
pnpm typecheck
pnpm build          # nest build → dist/ (this is what consumers import)
pnpm test           # vitest run — src/**/*.spec.ts (includes *.int.spec.ts)
pnpm test:cov
pnpm db:generate    # drizzle-kit generate — the ONLY way to author a migration
pnpm db:migrate
pnpm db:push        # local scratch only — never against staging/production
pnpm db:studio
pnpm db:seed
```

## 2. Migration rules (hardest rules in the repo)

1. **Never hand-write a migration file.** Change `src/schema/`, run
   `pnpm db:generate`, review the generated SQL, commit both.
2. **Never edit a migration that has been applied anywhere.** Consumers have
   already run it; editing it makes their journal diverge silently. Write a new
   migration instead.
3. **Never delete or renumber a migration**, and never edit the drizzle
   journal by hand.
4. **Review the generated SQL before committing.** Drizzle will happily emit a
   destructive `DROP COLUMN` for a rename. Confirm intent, and for a rename
   write the two-step (add → backfill → drop) across two releases rather than a
   drop.
5. **Any migration that adds a constraint, unique index, check, or FK that code
   relies on gets an `*.int.spec.ts` asserting the constraint actually
   rejects the bad row.** A constraint nobody tested is a constraint that might
   not exist.
6. Additive-first: new columns are nullable or defaulted, so the old API
   version keeps working during a rolling deploy. If a change cannot be
   additive, say so in the PR and coordinate the deploy order.

## 3. Testing layers here

| Subject | How | Reference |
| --- | --- | --- |
| `DalService` wiring — a DAL per table, correct subclass, inherited CRUD surface | Pure unit, **no DB** (the constructor only reads table metadata) | `src/dals/dal.service.spec.ts` |
| `BaseDal` generic behaviour (findMany, paginate, count, exists, error mapping) | Unit once + int spec once against **one** table | — |
| Every **custom** DAL method (anything beyond BaseDal CRUD: `findByPhone`, `findLatest`, `findActive`, joins, aggregates) | **`*.int.spec.ts` against real Postgres — mandatory** | `admin-dals.int.spec.ts`, `chat-dals.int.spec.ts` |
| Query correctness: filters, ordering, pagination boundaries, soft-delete exclusion | Int spec | — |
| `dal.errors.ts` mapping (pg error code → `DalError`) | Unit for the mapping table; int spec for at least the unique-violation and FK-violation paths so the real codes are proven | — |
| Migrations | See §2.5 | — |
| Seeds | Not tested; excluded from coverage | — |

**Do not unit-test a query by mocking Drizzle.** Asserting that a query builder
was called with certain arguments tests your memory of Drizzle's API, not
whether the SQL returns the right rows. Query behaviour is int-spec territory,
full stop.

## 4. Integration spec hygiene

- Guard on DB reachability and **skip** when unreachable — a laptop without
  Postgres must still get a green `pnpm test`. Keep this; CI provisions
  Postgres and runs the suite fully.
- Unique per-run prefix for every column with a uniqueness constraint; track
  created IDs; clean up in `afterAll`.
- Each int spec creates its own fixtures. No cross-file shared state, no
  reliance on seed data, no `TRUNCATE` of a shared database.
- Test the boundaries that only a real DB shows: unique violations, FK cascade
  vs. restrict, `ON CONFLICT` behaviour, transaction rollback, and default/
  generated column values.

## 5. Custom DAL checklist

Adding a method to a `*.dal.ts`? It is not done until there is an int spec
covering:

- the match case (returns the expected row);
- the **no-match** case (returns `null`/`[]` — assert which, since callers
  branch on it);
- the filter that must exclude (deleted/inactive/other-tenant rows are *not*
  returned — this is where authorisation bugs originate);
- ordering, if the method promises any;
- pagination edges: page 0/1 semantics, limit larger than the row count, and
  the total count.

## 6. Publishing and versioning

- `package.json` `version` is the contract. **Bump it in the same PR as the
  schema or DAL change** — consumers pin exact versions and will otherwise
  install a stale package that no longer matches the migrations.
- Breaking change (removed column, renamed export, changed return type):
  say so explicitly in the PR description and coordinate the consumer bumps in
  `beevia-api` and `beevia-admin-api`.
- `files` ships `dist` and `drizzle` only. If you add a runtime asset, add it
  to `files` or consumers get a package that fails at runtime but passes CI.
- `pnpm build` must pass before release — `dist/` is the published artifact and
  `main`/`types` point into it. A typecheck-clean source with a broken build is
  a broken release.

## 7. Coverage configuration

Add `test.coverage` to `vitest.config.mts`:

- provider `v8`, reporters `['text', 'lcov']`.
- **Exclude**: `src/index.ts` and `src/dals/index.ts` (barrel re-exports),
  `src/schema/**` (declarative table definitions — no branches; if a schema file
  grows logic, move the logic out), `src/seed/**`, `src/bin/**`,
  `src/database.module.ts`, `src/drizzle.tokens.ts`, `drizzle/**`, `dist/**`.
- **Thresholds**: `src/dals/**` at **100% lines and branches** — it is the whole
  product. `src/migrator.ts` and `src/env.ts` at 90%+.
- Because most DAL coverage comes from int specs, **coverage measured without a
  database is meaningless**. Enforce thresholds only in the CI job that has
  Postgres; locally, `test:cov` without a DB will under-report and that is
  expected, not a signal to add mocked tests.

## 8. Things not to do

- Do not add business logic here. This layer is schema + data access; fee
  calculation, permission decisions, and workflow belong in the API repos.
  A DAL method that makes a policy decision is misplaced.
- Do not use `db:push` against anything shared — it bypasses the migration
  history the consumers replay.
- Do not export a type or symbol you do not intend to support; everything
  exported from `src/index.ts` is public API for two other repos.
- Do not mock Postgres to raise a coverage number.
