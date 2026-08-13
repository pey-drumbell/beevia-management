# Beevia agent rules — staging folder

Draft engineering rules for each Beevia repo, written to be dropped in as
`AGENTS.md` (with a one-line `CLAUDE.md` that just says `@AGENTS.md`). They are
staged here for review — **nothing has been moved or applied to any repo.**

## Files and where each one goes

| File | Destination | Notes |
| --- | --- | --- |
| `shared-testing-principles.md` | Paste into each repo's `AGENTS.md` as the first section, **or** keep one copy in this repo and link to it | The coverage contract and the "100% without overkill" definition. Everything else assumes it. |
| `beevia-api.md` | `beevia-api/AGENTS.md` | NestJS, Drizzle, BullMQ, Socket.IO, money/ledger. |
| `beevia-admin-api.md` | `beevia-admin-api/AGENTS.md` | NestJS, RBAC, admin actions/audit. |
| `beevia-db-schema.md` | `beevia-db-schema/AGENTS.md` | Published package: schema, migrations, DALs. |
| `beevia-admin.md` | `beevia-admin/AGENTS.md` | Next.js 16 / React 19. **Append** — that file already has a `BEGIN:nextjs-agent-rules` block that must be preserved. |
| `beevia-mobile.md` | `beevia-mobile/AGENTS.md` | Flutter / Dart. |

For each repo also add:

```
# CLAUDE.md
@AGENTS.md
```

`beevia-admin` already follows exactly this pattern — copy it.

## What the review should decide

1. **Coverage thresholds.** Each doc proposes concrete numbers. They are
   deliberately per-directory rather than one global number. Adjust before
   rollout; a threshold that fails on day one gets disabled on day two.
2. **Ratchet vs. big-bang.** `beevia-admin` (1 test file) and `beevia-mobile`
   (3 test files) cannot meet the proposed thresholds today. Recommended: land
   the thresholds at the *current* measured number and raise them only on the
   way up, never down.
3. **Gaps flagged, not fixed** (no code was changed):
   - `beevia-admin` has **no CI workflow at all** and no coverage provider
     installed (`@vitest/coverage-v8` missing) — see `beevia-admin.md` §7.
   - `beevia-mobile` CI runs `flutter test` but not `flutter analyze` and
     collects no coverage — see `beevia-mobile.md` §7.
   - No repo currently sets coverage thresholds; `test:cov` exists in the three
     backend repos but nothing enforces a floor.
   - `beevia-api` has 57 unit specs but no controller specs beyond
     `app.controller.spec.ts` — that is the intended design (controllers are
     covered by e2e), and the rules make it explicit rather than accidental.
