# beevia-admin — agent rules

> **Append this to the existing `beevia-admin/AGENTS.md`.** That file already
> contains a managed `BEGIN:nextjs-agent-rules` / `END:nextjs-agent-rules`
> block — leave it intact and untouched at the top; it is generated, and its
> instruction ("read `node_modules/next/dist/docs/` before writing code")
> still applies to everything below.

The Beevia admin panel. Next.js 16 (App Router) + React 19 + TanStack Query +
Tailwind/shadcn + Vitest/jsdom/Testing Library.

Read `../agent-rules/shared-testing-principles.md` first.

---

## 1. Current state — read this before planning work

This repo has **one test file** (`account-status-badge.test.tsx`), **no CI
workflow**, and **no coverage provider installed**. It is the largest testing
gap in the Beevia estate. Two consequences:

- Do not treat "the suite is green" as evidence of anything yet.
- Coverage thresholds must be introduced at today's measured value and
  ratcheted, not set to 90% on day one (see §7).

## 2. Commands

```bash
pnpm lint          # eslint .
pnpm typecheck     # tsc --noEmit
pnpm test          # vitest (watch mode — use `vitest run` in scripts/CI)
pnpm build
```

Before a PR: `pnpm lint && pnpm typecheck && pnpm vitest run && pnpm build`.

## 3. Conventions

- Tests are **colocated** and named `*.test.ts(x)` (note: `.test`, not `.spec`
  as in the API repos — match what is here).
- Explicit imports from `vitest` (`import { describe, expect, test } from
  "vitest"`) — `globals` is **not** enabled here, unlike the backend repos.
- `@testing-library/jest-dom/vitest` is loaded via `vitest.setup.ts`; matchers
  like `toBeInTheDocument` are available without importing.
- Path aliases resolve through `vite-tsconfig-paths`; import as the app does.

## 4. What to test, in priority order

Work down this list; the top of it is where the value is.

1. **`src/lib/**` — pure utilities. Target 100%.** `format.ts`, `csv.ts`,
   `roles.ts`, `utils.ts`, `token-store.ts`. Cheapest coverage in the repo and
   the code most reused. Table-driven cases: money and date formatting across
   locales/zero/negative/null; CSV escaping of commas, quotes and newlines;
   role→permission resolution across the full matrix.
2. **`src/features/*/api.ts` — request/response mapping.** Assert the URL,
   method, query serialisation, and the domain object produced from a
   representative payload — including how an error response is surfaced.
3. **`src/hooks/**` — render with a `QueryClientProvider` wrapper** (a fresh
   `QueryClient` with retries disabled per test) and assert loading → success
   and loading → error transitions.
4. **Components with branching**: status badges, permission-gated controls,
   empty/error/loading states, table row rendering, dialogs that confirm
   destructive actions. Every visual branch gets a case.
5. **Presentational components with no logic** — do not test. A component that
   renders its props into markup and nothing else adds no signal.
6. **Pages / Server Components / layouts** — do not unit test. Cover the
   critical paths (login, suspend a user, run an export) with an e2e tool when
   one is adopted; until then, they are excluded from coverage and that is a
   known, stated gap.

## 5. How to write them

- **Query by accessibility, in this order**: `getByRole` → `getByLabelText` →
  `getByText` → `getByTestId` (last resort, and add a comment saying why). This
  makes the test double as an accessibility check.
- **Interact with `@testing-library/user-event`**, not `fireEvent` — it models
  the real event sequence (focus, keydown, click) that components depend on.
- **Await with `findBy*` / `waitFor`.** Never a fixed `setTimeout`. Never
  `act()` wrappers added to silence a warning — the warning means something is
  unawaited.
- **Assert what the user sees**, not internal state: rendered text, disabled
  state, whether the confirm dialog appeared. Never reach into component
  internals, never assert on class names as a proxy for behaviour (Tailwind
  classes change; behaviour should not).
- **Mock at the network boundary**, not the module under test. `src/mocks/`
  (`adapter.ts`, `fixtures.ts`) already exists — extend it rather than
  `vi.mock`ing the axios client per file, and keep fixtures shared so a shape
  change breaks one file.
- **Never call the real API.** No test may depend on a running backend.
- Socket-driven UI (`use-socket-status`, notifications): inject a fake socket
  and assert the UI reacts to emitted events; do not open a real connection.

## 6. Destructive-action components

Suspend/reactivate, role changes, deletions, exports. Each needs:

- the confirm step is required — the action does **not** fire on first click;
- cancelling fires nothing;
- the action is disabled or absent for an admin lacking the permission
  (assert both the disabled control *and* that invoking it is a no-op);
- the in-flight state prevents a double submit;
- the failure path shows an error and leaves the UI in a recoverable state.

## 7. Setup this repo is missing (proposed, not applied)

1. **Add a coverage provider**: `@vitest/coverage-v8` (dev dependency), plus
   `test.coverage` in `vitest.config.mts` — provider `v8`, reporters
   `['text','lcov']`.
   - **Exclude**: `src/app/**` (pages/layouts — see §4.6), `src/components/ui/**`
     (generated shadcn primitives), `src/mocks/**`, `src/types/**`,
     `*.config.*`, `src/proxy.ts` if it is pure passthrough.
   - **Thresholds**: `src/lib/**` at 100%; everything else set at the measured
     baseline and ratcheted upward, never lowered.
2. **Add scripts**: `"test:run": "vitest run"`, `"test:cov": "vitest run
   --coverage"`. `pnpm test` alone starts watch mode and will hang CI.
3. **Add a CI workflow** — this repo has none. Mirror `beevia-admin-api`'s
   `ci.yml`: on `pull_request` (unfiltered, for stacked PRs) and push to main,
   matrix Node 22/24, `pnpm install --frozen-lockfile` → `lint` → `typecheck` →
   `test:run` → `build`. No Postgres service needed.
4. Husky + lint-staged are installed; keep the pre-commit hook to lint and
   format staged files, but do **not** run the full suite on commit — it
   belongs in CI.

## 8. Things not to do

- Do not snapshot-test a page or a table. Snapshots of large trees get
  regenerated on failure without being read.
- Do not test TanStack Query itself (caching, retries, invalidation) — test
  *your* query/mutation functions and *your* cache keys.
- Do not add `data-testid` to production markup when a role or label would
  work; fix the accessible name instead, and both the test and the user win.
- Do not disable ESLint rules inline to land a test.
- Do not assume the Next.js API you remember still exists — read
  `node_modules/next/dist/docs/` first, per the block at the top of this file.
