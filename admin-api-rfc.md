# RFC: Beevia Admin API Surface

| | |
|---|---|
| **Status** | Draft — for review · created 2026-08-05 |
| **Scope** | The HTTP surface of `beevia-admin-api`: what exists today, and what "Beevia Admin Dashboard.md" specifies that does not exist yet |
| **Companion artifacts** | [`openapi.admin.yaml`](./openapi.admin.yaml) — implemented, 42 operations · [`openapi.admin.proposed.yaml`](./openapi.admin.proposed.yaml) — designed but unbuilt, 19 operations |
| **Sibling RFC** | [`api-rfc.md`](./api-rfc.md) — the consumer API |
| **Sources** | `beevia-admin-api/src/**`, `beevia-db-schema/src/schema/*`, `Beevia Admin Dashboard.md` |
| **Base path** | `/api/v1`, with every business route further prefixed `/admin` |

> **Paths in this document.** Unless prefixed otherwise, `src/` refers to `beevia-admin-api/src/`. The service repositories are unmodified by this work.

---

## 1. Summary

`beevia-admin-api` is a **separate NestJS service** from the consumer API, sharing the database through the published `@drumbell-technologies/beevia-db-schema` package. It is **42 operations** across eleven controllers, backing the admin dashboard specified in `Beevia Admin Dashboard.md`.

**Three of the spec's eight modules are built, a fourth opened on 2026-09-02** when the cross-module activity feed merged (§5.4a), **and a fifth opened on 2026-09-04** when transaction oversight and reconciliation landed (§3.9, §3.10, §5.2) — the first money-oversight surface this service has ever had. Module 5 widened again on **2026-09-06** with the wallets screen (§3.12), leaving flagging as its only unbuilt operation. **On 2026-09-08 a sixth module opened, and it is the one this RFC has called blocking since 5 August**: the `/admin/chats` module merged to `main` (§3.13), implementing Module 4 as the metadata-only Option A of §5.1 — no message content, and the first reader `conversation_reports` has ever had. What exists is well-made: the permission model is more capable than the spec asked for, KYC values are masked by default with reveals logged, case notes are append-only, and account actions require a structured reason and land in a queryable history.

Against that, three findings need attention before this service is exposed to real staff:

| # | Finding | Severity |
|---|---|---|
| 1 | **No 2FA**, despite the spec making it mandatory. Email + password is the only barrier to an account that can read BVNs and suspend users. Also no lockout and no rate limiting on login. | **High** |
| 2 | **Guards are per-controller, not global.** A new controller that omits `@UseGuards(...)` is completely unauthenticated — not merely under-authorised. | **High** |
| 3 | **Module 4 (Trust & Safety) cannot be built as specified.** It asks the moderation queue to show "reported messages"; chat is end-to-end encrypted and the server holds no key. **Resolved in code on 2026-09-08** — Option A (metadata-only) shipped (§3.13, §5.1a). The product decision it implies is still recorded nowhere but the code. | ~~Blocking~~ → **Decided in code, unrecorded** |

### Module coverage

| # | Spec module | State | Ops |
|---|---|---|---:|
| 1 | Authentication & Access Control | 🟡 **Partial** — login and invite work; **no 2FA** | 2 |
| 2 | Admin Account Management | ✅ **Built** — re-invite added 2026-09-08 | 4 |
| 3 | User Management & Support Tools | 🟡 **Partial** — no assisted PIN reset | 18 |
| 4 | Trust & Safety / Content Moderation | 🟡 **Built as Option A, merged 2026-09-08** (§3.13); not buildable *as written*. A queue, not yet a workflow — no status, no resolve | 4 |
| 5 | Transaction & Wallet Oversight | 🟡 **Partial** — feeds and reconciliation shipped 2026-09-04, wallets 2026-09-06; no flagging, no partner-balance comparison | 6 |
| 6 | Country & Feature Configuration | ⛔ **Not built** | 0 |
| 7 | Analytics & Reporting Dashboard | 🟡 **Partial** — activity feed + the landing-screen summary (2026-09-06); no time-series analytics. A report-generation feature sits unmerged on `feat/admin-reports` (§5.4b) | 2 |
| 8 | Account Deletion Requests | ⛔ **Not built** | 0 |

Modules 3 and 2 being the built ones is the right call — user search and support tooling is what a support agent needs on day one, and admin account management is its prerequisite.

Module 5 opening is the notable change of 2026-09-04, and it did not arrive the way §6 sequenced it. It was placed in Phase 4, behind config and the deletion queue, on the reasoning that reconciliation was blocked on a partner statement API nobody had built. That dependency was simply resolved — the admin service grew its own Anchor adapter — and four operations shipped in a day. The sequencing advice below is left as written rather than retro-fitted, because the useful lesson is that the blocker was smaller than this RFC judged it to be.

---

## 2. Architecture

### 2.1 What was chosen

| Decision | Implementation |
|---|---|
| Codebase | **Separate repository** (`beevia-admin-api`) |
| Deployment | Separate service and port |
| Database | **Shared** via `@drumbell-technologies/beevia-db-schema` |
| Principal | Separate — `admins` table, not `users` |
| Token | Separate `type` claim (`admin_access`), **same signing secret** |

This is a reasonable shape. Extracting the schema into a package is what makes it defensible: the classic failure of splitting a fintech back office into its own service is ending up with two divergent definitions of the same money, and a shared schema package removes that at the data layer.

### 2.2 What the split does not cover

The package shares **tables**, not **behaviour**. `ResponseInterceptor`, `AllExceptionsFilter`, `ZodValidationPipe` and the pagination helper are duplicated source files in both repositories. They agree today because they were copied recently; nothing keeps them in step.

That is tolerable for presentation-layer code. It would **not** be tolerable for ledger operations — see §5.3, which is why the proposed transaction endpoints are read-and-annotate only.

---

## 3. Implemented surface

Auth legend: 🔓 public · 🔑 admin token · plus the `module:action` permission each route requires.

### 3.1 Admin Auth (2) — spec Module 1

| Method | Path | Auth | Notes |
|---|---|---|---|
| POST | `/admin/auth/login` | 🔓 | 🟡 Email + password. **No 2FA, no lockout, no rate limit, no password reset** |
| POST | `/admin/auth/accept-invite` | 🔓 | ✅ Invite token → set password → account becomes `active` |

Invite-only account creation is correct and matches the spec — there is no registration route.

### 3.2 Admin Accounts (4) — spec Module 2

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/accounts` | `admin_accounts:view` | ✅ Paginated; filter by search, access level, status |
| POST | `/admin/accounts/invite` | `admin_accounts:create` | ✅ Role assigned at invite time |
| POST | `/admin/accounts/{id}/reinvite` | `admin_accounts:create` | ✅ **Shipped 2026-09-08.** Re-issues the setup link for an account still `invited` |
| PATCH | `/admin/accounts/{id}` | `admin_accounts:edit` | ✅ Re-role and activate/deactivate — the immediate-revocation path the spec requires |

**Re-invite closes a real dead end.** The invite token has a fixed TTL; before this, an admin whose link expired had no path forward at all — the account was stuck in `invited`, the row could not be re-invited, and the only workaround was deleting and recreating it. Three details are worth carrying into the UI:

- **It invalidates the previous link.** The stored hash is replaced before the new mail goes out, so a forwarded or stale invite cannot be redeemed afterwards. This is the right default and it is also a support trap: telling a user "check your email again" after a resend means *the newest* one.
- **Only an `invited` account qualifies.** `active` and deactivated accounts both return `409 admin_not_invited`, distinguished only by the message text. A UI that reads the error code alone cannot tell "already set up" from "deactivated — reactivate instead", which are opposite next actions.
- **It records `admin_invited`, not a distinct action.** The `admin_action` enum has no `admin_reinvited` value, so a resend and a first invite are the same event type in `GET /admin/activity`; the summary string ("Re-invited …") and `metadata.resent: true` are the only discriminators. Reasonable — a schema release for one label is expensive — but any client counting invites from the feed will double-count resends.

### 3.3 Roles & Permissions (5) — beyond spec Module 1

| Method | Path | Permission |
|---|---|---|
| GET | `/admin/roles` | `roles_permissions:view` |
| GET | `/admin/roles/{id}` | `roles_permissions:view` |
| POST | `/admin/roles` | `roles_permissions:create` |
| PATCH | `/admin/roles/{id}` | `roles_permissions:edit` |
| POST | `/admin/roles/{id}/assign-admins` | `roles_permissions:manage` |

**The implementation is broader than the spec.** The spec describes three fixed roles — Support, Compliance, Super Admin. The code implements a **general role builder**: roles are database rows with a full 11-module × 7-action permission matrix, and the three named roles become seed data rather than a constraint.

This is a defensible trade — a fixed enum would have needed a migration for every new role — but it has consequences worth stating:

- **The spec's guarantees are now conventions.** "Support cannot view KYC detail" is true only while nobody ticks `kyc:view` on the Support role. Nothing in the code enforces the spec's role boundaries.
- **`access_level` (`full` / `limited` / `read_only`) is derived, never stored**, from the permission matrix. Good — one source of truth. But it means the dashboard's role labels are computed, not authoritative.
- **A role with no permission rows is vacuously `read_only`**, the safest default. Deliberate, and documented in `views.ts`.

Recommendation: seed the three spec roles and add a test asserting their permission matrices match the spec table, so drift is caught rather than discovered.

### 3.4 User Management (10) — spec Module 3

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/users` | `users:view` | ✅ Rich filters: country, account type, status, verification, wallet, join window |
| GET | `/admin/users/export` | `users:**export**` | ✅ CSV. Correctly gated behind a distinct action, not `view` |
| GET | `/admin/users/recent-searches` | `users:view` | ✅ Per-admin |
| POST | `/admin/users/recent-searches` | `users:view` | ✅ |
| GET | `/admin/users/{id}` | `users:view` | ✅ Verification detail deliberately excluded — see §4.4 |
| GET | `/admin/users/{id}/actions` | `users:view` | ✅ Lifecycle audit trail |
| POST | `/admin/users/{id}/suspend` | `users:edit` | ✅ Structured reason required; revokes every live session |
| POST | `/admin/users/{id}/restrict` | `users:edit` | ✅ Softer sanction; sessions deliberately left alone |
| POST | `/admin/users/{id}/activate` | `users:edit` | ✅ Also the **restore** for a deactivated account |
| POST | `/admin/users/{id}/deactivate` | `users:**delete**` | ✅ The admin delete — reversible, separately gated |

The `suspend`/`deactivate` permission split is a good detail: a role can be allowed to suspend without being allowed to terminate.

#### 3.4a The delete semantics — shipped 2026-08-06, first documented 2026-09-02

**Read the two dates.** Everything in this subsection has been on `beevia-admin-api` `main` since 6 August (commits `689acc4`, `c242320`, `e1c1f66`). None of it was in this spec until 2 September — **27 days**, during which `openapi.admin.yaml` described a contract the service had stopped honouring. Nothing caught it: the audit compares *route inventories* between code and spec, and not one route was added, removed or renamed. See the note at the end of this subsection.

Three related changes landed together, and they are worth reading as one design rather than three fixes:

1. **`deactivate` no longer routes into the consumer's erasure pipeline.** It previously moved the account to `deleting` — the same status `DELETE /users/me` uses — so an admin ending an account handed it to a job that scrubs PII and recycles the phone number. It now moves to a distinct `deactivated` status and destroys nothing, which is what makes `activate` a genuine restore. The two paths had been conflated since the service was written; separating them is the right call, because an admin action taken in error was previously unrecoverable.
2. **Ending access now ends the sessions.** `suspend` and `deactivate` revoke every live session in the same transaction as the status change, and report the count as `sessions_revoked`. Previously a suspended user kept working until their access token expired — the sanction was advisory for the length of a token lifetime. `restrict` pointedly does not revoke, because a restricted user is meant to keep using the app.
3. **Ended accounts leave the default list.** `GET /admin/users` excludes `deactivated` and `deleted` unless `includeEnded=true` or `accountStatus` names one explicitly, which makes `accountStatus=deactivated` the restore queue with no new endpoint.

Two further changes from the same 6 August batch were equally undocumented: `GET /admin/users` gained the `includeEnded` filter and learned to accept a bare `YYYY-MM-DD` on `joinedFrom`/`joinedTo` (widening the `To` bound to end-of-day, so the named day is included rather than silently dropped), and the shared pagination cap rose from 100 to 500 for roles and admin accounts — but *not* for users, which keeps its own 100. The spec's single shared `Limit` parameter could no longer describe both; it is now `Limit` (users) and `ConfigLimit` (roles, admin accounts).

**A fourth defect was found and fixed alongside them, and it is the worst of the set.** The four action endpoints have always returned the *transition* — `user_id`, `action`, `previous_status`, `status`, `reason`, `at`, and since 6 August `sessions_revoked` — but `openapi.admin.yaml` documented their `200` as an `AdminUserAction` history row (`id`, `note`, `performed_by`, `created_at`). Every field but `action` differed, and this one was wrong from the day the spec was written, not merely stale. A client generated from it would have read `created_at` off a body that has never carried one. The response is now a distinct `AdminUserActionResult` schema.

**What this says about the audit.** Four contract changes and one original error survived roughly nineteen consecutive daily runs, all reported clean, because every one of them lives *inside* an operation: a response body, a query parameter, an enum value, a status code. The route-level diff is a genuinely useful check and it is not the check that would have caught any of this. The cheapest real fix is for the service to publish its generated OpenAPI document — `main.ts` already builds one with `SwaggerModule.createDocument` — and for the audit to diff *that* against these files, instead of inferring the surface from controller decorators.

### 3.5 KYC Review (6) — spec Module 3

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/users/{id}/verification` | `kyc:view` | ✅ All checks, **values masked** |
| GET | `/admin/users/{id}/verification/{type}/unmask` | `kyc:view` | ✅ **Logged with the admin id** |
| POST | `.../{type}/approve` | `kyc:**approve**` | ✅ |
| POST | `.../{type}/reject` | `kyc:approve` | ✅ |
| POST | `.../{type}/request-reverification` | `kyc:edit` | ✅ |
| POST | `.../{type}/reset` | `kyc:**manage**` | ✅ Most destructive; highest permission |

This is the best-designed part of the service. Masking by default, treating a *reveal* as an auditable event in its own right ("looking at someone's BVN is itself an event"), and escalating the permission with the destructiveness of the action are all correct instincts, applied consistently.

### 3.6 Case Notes (2) — spec Module 3

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/users/{id}/case-notes` | `users:view` | ✅ Newest first, author resolved |
| POST | `/admin/users/{id}/case-notes` | `users:create` | ✅ **Append-only** — never edited or deleted |

Append-only is the right model for a compliance record.

### 3.7 Platform (1)

`GET /` — liveness. Same limitation as the consumer API: a static string that stays 200 with Postgres down.

### 3.8 Admin Activity (1) — spec Module 7

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/activity` | *(none — filtered per viewer)* | ✅ Merged 2026-09-02. Cursor-paginated cross-module event feed |

Merged from `BVA-1226` and moved out of the proposed spec (§5.4a). Two properties make it unlike every other operation in this service, and both are deliberate:

- **No `@RequirePermission`.** Any authenticated admin may call it; the service resolves the caller's viewable modules and filters rows in SQL, returning an empty list — not a 403 — to an admin entitled to nothing. That is the right shape for a feed, but it moves access control off the route decorator and into the service, so a reviewer checking authorisation by reading controllers will not see it. It is also the one route where an `@UseGuards` omission (§4.2) would be hardest to notice, since "no permission declared" is its normal state.
- **Cursor pagination** (`before` / `next_cursor`) where every other list operation is page-based. Defensible for an append-only feed; worth being a decision rather than an accident.

Events are appended by the producing module inside that module's own transaction, so the feed cannot record a change that rolled back nor miss one that committed. That is the correct construction and it is rarer than it should be.

**"Cross-module" currently means three modules of eleven.** Only `users` (status changes), `roles_permissions` (role assignment) and `admin_accounts` (invite, deactivate, reactivate) write to it. Nothing from money, KYC, chats or reports appends, and those are the modules an oversight feed exists for. The table and the `record()` call site are cheap to extend; until they are, the console's home feed shows admin housekeeping rather than platform activity.

### 3.9 Transactions (2) — spec Module 5, shipped 2026-09-04

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/transactions` | `transactions:view` | Platform-wide ledger feed, newest first, page-based |
| GET | `/admin/transactions/users/{userId}` | `transactions:view` | One user's statement across all their wallets |

Both read the ledger directly, which is the right source: every balance change in the product flows through `ledger_entries`, so this is complete by construction rather than by assembling per-feature histories.

Three contract facts a client needs and cannot guess:

- **A two-sided flow is two rows.** A peer transfer appears as the sender's debit and the recipient's credit, each attributed to its own user. The row count is therefore not the transaction count, and a naive "total transfers today" over this feed double-counts.
- **System and escrow wallets are excluded** by the inner join to `users`. That is correct for a customer-money feed and it means the feed cannot be used to audit the platform's own float — Module 5's wallet-detail operation, still proposed, is where that would live.
- **`direction` is relative to the row's user**, not to Beevia.

**The per-user route shipped at a different path from its proposal** — `/admin/transactions/users/{userId}`, not `/admin/users/{id}/transactions`. Every other user-scoped operation in this service hangs off `/admin/users/{id}`; these two nest the user under the resource instead. Both readings are defensible and the split is now permanent in client code, so it is recorded here rather than argued: **the service has two conventions for user-scoped routes.**

### 3.10 Reconciliation (2) — spec Module 5, shipped 2026-09-04

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/reconciliation/pool` | `transactions:view` | Σ user NGN ledger vs the pooled FBO balance |
| GET | `/admin/reconciliation/users/{userId}` | `transactions:view` | One user's Anchor-rail ledger vs Anchor's own transactions |

Report-only — neither writes to the ledger, which is the constraint §2.2 exists to protect, honoured here without being asked.

**The unmet dependency this RFC flagged (§5.2, and the proposed spec's own note) is resolved.** Both said reconciliation needed "a statement or balance-report call on the partner adapter, which does not exist in either service today". The admin service grew one: `AnchorService.listAccountTransactions` and `getAccountBalanceKobo` on its own copy of the adapter. That closes the gap and widens §4.5 — the duplicated-code finding now covers a provider integration, not just presentation-layer files.

What makes the implementation worth trusting is that it is honest about its own limits, in the response rather than only in comments:

- **Scope is narrow by construction.** Only deposits and NIP payouts have an Anchor counterpart; internal transfers, escrow, fees and Paystack top-ups are excluded up front so they cannot false-flag as missing.
- **Match confidence differs by rail and is disclosed.** Payouts correlate exactly on Anchor's `transfer.id`. Deposits carry a `payment.id` this service does not store, so they fall back to amount + direction + a 10-minute window — and the response's `notes` says an unmatched deposit may be a real gap or a near-duplicate rather than declaring a match.
- **Money is compared in integer kobo**, formatted to naira only for display.

Two things to watch, neither a defect today:

1. **`status: not_configured` is returned with `solvent: false`.** That means "unknown", not "insolvent". A dashboard binding a red/green badge to `solvent` will show an unconfigured pool as a solvency failure. Read `status` first.
2. **The per-user balance check assumes the user's own VBA holds their money.** It compares the wallet balance against Anchor's `balance_after` on the newest transaction in *that* account. The consumer API's treasury change, merged the same day, sweeps deposits out of individual VBAs into the pool — so once `ANCHOR_POOL_ACCOUNT_ID` is set, a fully-reconciled user's VBA reads near zero while their ledger balance does not, and `balance_matches` goes false for everyone. The pool endpoint is the aggregate answer to this, and the per-user balance line will need to stop being a straight equality. **The two commits landed within half an hour of each other in different repositories**, which is exactly the kind of cross-service interaction no single-repo review catches.

---

### 3.11 Dashboard (1) — spec Module 7, shipped 2026-09-06

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/dashboard` | `dashboard:view` | Every landing-screen metric in one payload |

One endpoint backing the whole console landing screen: user counts (total, active, new today/7d/30d, split by onboarding path and account status), the KYC review queue, transaction counts and volume for today and the last 7 days plus volume by ledger type over 30 days, pending payouts, treasury solvency, and admin-account counts.

The shape is the right one for a dashboard. A handful of parallel `COUNT`/`SUM` queries in a single `Promise.all`, no schema change, no new tables, and the treasury tile reuses `ReconciliationService.reconcilePool()` rather than duplicating the solvency logic — so there is exactly one definition of "solvent" in the service. `dashboard` was already a value in `adminModuleEnum`, so the permission is seedable without a migration.

Three contract facts worth stating:

- **"Volume" is gross value moved, not net position.** It sums the ledger's credit legs, so a peer transfer contributes its full amount once. That is the right definition for a dashboard tile and the wrong one for a balance sheet.
- **`by_type_this_month` is an open map**, keyed by ledger transaction type. New ledger types appear as new keys with no spec change — which is deliberate, and means a client must not exhaustively switch on the keys.
- **Nothing is cached.** Every call recomputes, and `generated_at` is the moment of the call. Fine at current volume; the 30-day group-by is the line that will need an index or a materialised rollup first.

**It inherits §3.10's `solvent` trap and puts it on the landing screen.** `treasury.solvent` is `false` whenever the pool is unconfigured, which means *unknown*, not insolvent. §3.10 flagged this as something "a dashboard binding a red/green badge to `solvent`" would get wrong; that dashboard is now specified, and the payload does expose `configured` alongside so the client can distinguish the two. The remaining risk is entirely on the front end reading `solvent` without reading `configured` — which is worth saying to whoever builds the tile, because the naming does not steer them to it.

One inconsistency to note for whoever writes the client: `dashboard.types.ts` documents `configured` with the comment "null when `ANCHOR_POOL_ACCOUNT_ID` is unset", but the field is typed `boolean` and the implementation sets it to `pool.status !== 'not_configured'`. The comment describes `pool_balance_ngn`, not `configured`. The implementation is correct; the comment is stale.

### 3.12 Wallets (2) — spec Module 5, shipped 2026-09-06

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/wallets` | `wallets:view` | Platform summary + filterable, paginated wallet list |
| GET | `/admin/wallets/users/{userId}` | `wallets:view` | One user's wallets across every currency |

The money-shaped counterpart to `GET /admin/users`: where that list answers "who is this person", this one answers "where is the money". A user holding three currency wallets is one row there and three rows here. Both endpoints exclude `wallet_type = 'user'`'s complement — the platform's own fee, escrow and card wallets — so the totals are customer liability rather than the platform's balance sheet. `wallets` was already a value in `adminModuleEnum`, so like `dashboard` the permission seeds without a migration.

Four contract facts worth stating:

- **The summary ignores the query's filters.** `total_wallets`, `by_currency` and `by_status` are computed over every user wallet regardless of `currency`, `status` or `search`. This is deliberate — a "total held" tile should not move as the operator pages — but it is the single most likely thing to be read as a bug by whoever binds the two together. Say it in the UI, not just the spec.
- **`by_status` is a sparse map.** A status with no wallets is absent, not zero. A client that assumes four keys will render `undefined`.
- **`search` matches the owner, not the wallet** — display name, first/last name, username, email or phone, case-insensitively. There is no way to look a wallet up by its own id or by account number, which is the lookup a support call actually starts from ("a transfer went to 9901234567").
- **Balances are presentation values.** `money()` rounds the ledger's scale-8 value to 2 decimals. Summing the displayed column will not reproduce `total_balance`, and neither is a reconciliation input; §3.10 remains the authoritative comparison.

**One `N+1`-shaped edge.** `listWallets` fetches VBAs for the page's users in a single `inArray` query, which is right. `listForUser` instead loads *every* currency and *every* VBA for the user and joins in memory — fine at a handful of rows, and worth remembering only if a user can ever hold many wallets.

**What it does not do is the reason it was proposed.** The retired proposal asked for the ledger balance shown *alongside the partner-reported balance*, with an `in_sync` flag, so a per-wallet mismatch was visible without a reconciliation run. The shipped row carries the ledger balance only. That gap is now the substantive one in Module 5 — see §6.3.

### 3.13 Chats (4) — spec Module 4, shipped 2026-09-08

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/chats` | `chats:view` | Conversations list; filters `type`, `reportedOnly`, `search` |
| GET | `/admin/chats/reports` | `chats:view` | The moderation queue — reporter, reason, conversation, newest first |
| GET | `/admin/chats/users/{userId}` | `chats:view` | A user's conversations plus both directions of their block graph |
| GET | `/admin/chats/{conversationId}` | `chats:view` | Conversation detail — metadata, participants, its reports |

**This is the module §5.1 has called unbuildable since 5 August, built the way §5.1 recommended.** The spec asks the moderation queue to show "reported messages"; chat is E2EE and the server holds no key. Rather than fake it or stall, the module implements Option A — metadata only. The constraint is honoured explicitly, not incidentally: the controller docstring reads *"Chat is end-to-end encrypted, so these endpoints serve metadata + moderation only — never message content"*, and every operation description repeats it. There is no field anywhere in the module for message text, and none should ever be added.

`chats` was already a value in `adminModuleEnum`, so — like `dashboard` and `wallets` — the permission seeds without a migration.

**`GET /admin/chats/reports` is the first reader `conversation_reports` has ever had.** §5.1 has noted since 5 August that the consumer app's `POST /conversations/{id}/report` writes to that table and nothing reads it, so reports accumulated unreviewed. That is now false, which is the single most consequential line in this section.

Four contract facts:

- **It is a queue, not a workflow.** There is no status column, no assignment, no resolve action and no filter for open items — the endpoint returns *every report ever filed*, forever, newest first. A moderator cannot mark one handled, and tomorrow's queue is today's queue plus new arrivals. This is the substantive gap in Module 4 and it is tracked in §6.3.
- **Acting on a report is disconnected from the report.** The account actions exist (`suspend`, `restrict`, §3.4) but nothing links a report to the action taken on it, so "what did we do about this?" is unanswerable from the API. The `admin_activity` feed records the suspension without the reason that prompted it.
- **The counters are correlated sub-selects, one per row.** `participant_count` excludes members who left, `message_count` excludes soft-deleted messages, `report_count` counts everything. Three sub-selects × page size, plus a separate `count(*)`; fine at current volume, and the first thing to watch when the conversations table grows, because the list has no index-friendly ordering path — it sorts on `last_message_at desc nulls last`.
- **`search` scans participants via an `exists` sub-query** matching six user columns with `ilike '%term%'`. Leading-wildcard matching cannot use a b-tree index; this is the same pattern as the users list and will need the same attention at the same time.

**Route ordering is correct and load-bearing.** `@Get('reports')` is declared before `@Get(':conversationId')`, so `/admin/chats/reports` resolves to the queue. Reordering those two methods silently turns the moderation queue into a 404 for a conversation named `reports` — worth a comment in the controller more than a note here.

**The block graph is the quietly good part.** `GET /admin/chats/users/{userId}` returns both who the user blocked and who blocked them. A harassment complaint reads very differently depending on which direction the blocks point, and neither direction is visible anywhere else in the admin API.

---

## 4. Findings

### 4.1 Admin and consumer tokens share a signing secret

`AdminAuthGuard` documents this directly: the consumer API "issues `type: 'access'` against the same secret and rejects anything else".

The mitigation works — each side checks `type` and rejects the other's value, and the guard additionally verifies `sub` resolves to a live `admins` row. This is **not a live vulnerability**.

It is, however, a single point of failure with an unusually bad blast radius. A type-confusion bug, a library change in claim handling, or a future token variant that forgets the check converts a customer session into an admin session. The two realms have nothing in common — different principals, different tables, different threat models — and there is no benefit to sharing a key.

**Recommendation:** give the admin service its own `ADMIN_JWT_SECRET`, and add an `aud` claim to both realms (`aud: "beevia-admin"` / `"beevia-app"`) so the separation is structural rather than a string comparison. This is a small change now and a migration later.

### 4.2 Guards are per-controller — a new controller is wide open

Both guards are applied via `@UseGuards(AdminAuthGuard, PermissionGuard)` on each controller. `app.module.ts` registers only `APP_INTERCEPTOR` and `APP_FILTER` — **there is no `APP_GUARD`**.

Compare the two services:

| | Consumer API | Admin API |
|---|---|---|
| Global guard | `JwtAuthGuard` via `APP_GUARD` | **none** |
| A new controller with no decorators is… | authenticated; reachable by any logged-in customer | **completely unauthenticated** |

The consumer API's default fails *open to customers*, which is bad. The admin API's default fails *open to the internet*, which is worse — and this is the service where a mistake exposes BVNs and account suspension.

**Recommendation:** register `AdminAuthGuard` (and `PermissionGuard`) as `APP_GUARD`, add a `@Public()` decorator for the two auth routes, and make `PermissionGuard` **deny when no `@RequirePermission` is present** rather than allowing through. That inverts the default from fail-open to fail-closed, so forgetting a decorator produces a 403 in testing instead of an incident.

### 4.3 No 2FA, despite the spec making it mandatory

`AdminAuthService` states it plainly: "no password reset, no lockout/rate-limiting, no 2FA".

Module 1 lists "Mandatory two-factor authentication (2FA) for every admin account" as a key capability, and Module 2's rationale explains why — "controlling who has privileged access to user data is a security-sensitive responsibility in its own right".

Today a single leaked or guessed password grants an account that can read unmasked BVNs, suspend users, and (with the right role) create more admin accounts. There is no lockout, so the password can be attacked at whatever rate the network allows.

**This is the highest-severity gap in either service.** Proposed as three routes in `openapi.admin.proposed.yaml` (`/admin/auth/2fa/enrol`, `/verify`, `/challenge`), which also requires changing `POST /admin/auth/login` to return a challenge token rather than a full session.

### 4.4 Role-based field visibility is done structurally — good

The spec requires that Support see standard profile information while Compliance additionally sees verification detail. The implementation does not filter fields inside one response based on role; it puts verification behind a **separate route with a separate permission** (`GET /admin/users/{id}/verification`, `kyc:view`).

That is the more robust choice — no risk of a serializer leaking a field a role should not see, and the boundary is visible in the routing table. Worth preserving as the pattern when Modules 4–8 are built.

### 4.5 Duplicated service-layer code

`ResponseInterceptor`, `AllExceptionsFilter`, `ZodValidationPipe` and the pagination `meta` helper exist as near-identical copies in both repositories.

Note the consumer-side pagination bug from `suggestions.md` §1.3 — `Math.ceil(total/limit)` vs `Math.ceil(total/limit) || 1` — has now had an opportunity to propagate. Either extract these into the shared package alongside the schema, or add a CI check that the copies stay byte-identical.

### 4.6 Same gaps inherited from the consumer API

The admin service reproduces several issues already documented in `suggestions.md`: no `ParseUUIDPipe` on path params (so a malformed uuid yields 500, not 400), no rate limiting, no helmet, no request-id correlation, and Swagger served unauthenticated at `/api/docs`.

The last one matters more here. **The admin API's Swagger UI is an index of every privileged operation in the system.** If this service is ever reachable outside a private network, that page is a map for an attacker. It should be disabled in production, and the service itself should not be publicly routable.

---

## 5. The unbuilt modules

All 19 proposed operations are in [`openapi.admin.proposed.yaml`](./openapi.admin.proposed.yaml), and all 19 are designs — nothing in that file describes code that exists. Two left it on **2026-09-04**, when the per-user statement and reconciliation shipped (§5.2); one left it on **2026-09-02**, when the activity feed merged (§5.4a); one left it on **2026-09-06**, when the wallets screen shipped (§3.12); and one left it on **2026-09-08**, when the moderation queue shipped as `GET /admin/chats/reports` (§3.13).

### 5.1 Module 4 cannot be built as specified — needs a product decision

The spec asks for "context needed to assess a report (**reported messages**, reporting user, reported user)".

**The server cannot produce reported messages.** Beevia's chat is genuinely end-to-end encrypted: the server stores ciphertext and per-device envelopes and holds no key that decrypts them. This is not an implementation gap — it is the product's central privacy claim. The PRD states it directly (§1.5: E2EE "limits any form of message moderation") and §2.2 commits that Beevia "is not a content policing platform".

No endpoint can satisfy this requirement. There are three honest options:

| Option | What it means | Cost |
|---|---|---|
| **A. Metadata-only moderation** *(proposed)* | The queue shows who reported whom, when, the reporter's free-text reason, both parties' report history, and conversation metadata. Moderators act on patterns and reporter accounts, not content. | Weaker signal; some reports undecidable |
| **B. Reporter-attached excerpts** *(proposed, needs consumer change)* | At report time the consumer app offers to attach specific messages, decrypted **on the reporter's device** and uploaded as plaintext with explicit consent. | Requires a consumer-side change; only the reporter's view, which they could fabricate |
| **C. Break E2EE** | Escrow keys or server-side plaintext copies. | **Destroys the product's core claim. Not recommended.** |

The proposed endpoints implement **A**, with a `reporter_excerpts` field ready for **B**. `ReportDetail` has no field for server-decrypted content, deliberately.

~~Note the data already accumulates: `conversation_reports` is populated by the consumer app's `POST /conversations/{id}/report`, and **nothing reads it**. Reports are piling up unreviewed today.~~ **Closed 2026-09-08** — `GET /admin/chats/reports` reads it (§3.13). The reports that accumulated between the consumer app shipping reporting and that merge are all still in the queue, undifferentiated from new ones, because the queue has no status.

#### 5.1a Option A was built, and merged on 2026-09-08

**Found 2026-09-08 on an unmerged branch; merged to `main` the same day** as commit `6b105d8`, and now documented in §3.13 and in `openapi.admin.yaml`. The branch it sat on, `feat/admin-chats`, was one of the eight carrying the 2026-09-07 malware payload; it was the only one of the eight with unique content, and rather than being deleted with the rest it was brought onto the clean history. That was the right call and it is the reason this module exists on `main` rather than being lost.

**The product decision is still recorded nowhere but the code.** §5.1 laid out three options and asked for a decision; Option A was implemented, merged and is now the shipped behaviour, and no document anywhere says it was chosen. That matters more now than it did as a branch: the spec module says "reported messages", the API says metadata-only, and the gap between them is currently reconciled only by a controller docstring. Someone should write down that Option A is the answer, so that the next person reading `Beevia Admin Dashboard.md` does not file the difference as a bug.

**What was built is the queue, not the workflow.** Option A as proposed had a `status` filter (open / reviewing / actioned / dismissed) and a `resolve` action; neither shipped. §6.3 carries this as a gap rather than §5.1 carrying it as a blocker, because the unbuildable-as-specified problem is genuinely solved — what remains is ordinary unfinished scope.

### 5.2 Module 5 — Transaction & Wallet Oversight (1 proposed, 6 shipped 2026-09-04 → 09-06)

**Almost all of this module shipped.** The per-user statement and reconciliation are built and documented in §3.9 and §3.10, the wallets screen in §3.12. What remains proposed is a single operation, `POST /admin/transactions/{id}/flag`.

The wallet view shipped at a different path from its proposal (`/admin/wallets/users/{userId}`, not `/admin/users/{id}/wallets`) and alongside a platform-wide list that was never proposed at all. **The proposal's actual point did not ship**: it asked for the partner-reported balance beside the ledger balance with an `in_sync` flag, and the shipped row has neither.

**Flagging annotates, never mutates.** Flagging marks a transaction for investigation; it does not reverse, hold, or alter the ledger. Any actual reversal must go through the consumer API's ledger primitives, so there remains exactly one implementation of money movement. This is the constraint §2.2 exists to protect — and the operations that did ship honour it, being read-only.

**Reconciliation's "unmet dependency" was resolved, not waited out.** This section previously said comparing Beevia's ledger against the partner's records needed a statement or balance-report call on the partner adapter, "which does not exist in either service today", and §6 sequenced Module 5 last partly on that basis. The admin service built the call on its own Anchor adapter and shipped in a day. The judgement was wrong in a specific and repeatable way: it treated an absent integration as a blocker without checking how much of one was actually needed.

**What shipped is not what was proposed**, and the differences matter to whoever builds the dashboard against it — see §6.3.

### 5.3 Module 6 — Country & Feature Configuration (4 proposed)

`GET/PATCH /admin/countries`, `GET/PATCH /admin/feature-flags`.

The spec's motivation — "expanding banking to a second country requires an engineering release" — is accurate. Country eligibility is not modelled anywhere.

There is a second, sharper case for this module that the spec does not make: `currency_provider_configs` and `fee_configs` are both documented in code as **"admin-managed"**, and `ProviderResolverService.invalidate()` carries the comment *"call after admin mutations"*. Neither service exposes a route. **Changing a fee or repointing a currency's banking rail is today a hand-written `UPDATE` against production Postgres, unaudited.** That is a more urgent gap than country gating, and it belongs in this module.

One safety rule for the toggle: disabling banking for a country must gate **new** onboarding and wallet creation only. Existing wallets and balances must be unaffected, or a config toggle becomes a way to strand customer funds.

### 5.4 Module 7 — Analytics & Reporting (5 proposed)

Signups, onboarding funnel, path split, engagement, and a dashboard overview.

Mostly queries over data that already exists — the `onboarding_step` enum models the whole state machine, so funnel analysis needs no new instrumentation. Engagement counts read message and call *metadata* rows, never content.

The `dashboard` permission module exists in the enum with no routes behind it; the overview endpoint is its natural first occupant.

### 5.4a `GET /admin/activity` — **shipped 2026-09-02**, no longer proposed

Documented as proposed on 2026-09-01 with an explicit instruction to move it on merge; `BVA-1226` merged the next day, so it has moved to [`openapi.admin.yaml`](./openapi.admin.yaml) and out of the proposed file. Its contract is now described in §3.8.

Two notes for the record, because this is the first proposal this pipeline has watched ship:

- **The transcribed contract was nearly right, and wrong where it mattered.** Documenting it from the branch rather than from a design got the parameters, the permission model and the pagination scheme correct. It got the **key casing** wrong: the transcription copied the TypeScript property names (`adminId`, `entityType`, `occurredAt`, `nextCursor`), but `ResponseInterceptor` converts every response key to snake_case recursively before it leaves the service. The implemented spec carries the wire shape — `admin_id`, `entity_type`, `occurred_at`, `next_cursor` — and the same conversion applies inside the free-form `metadata` object, so a `user_status_changed` event carries `previous_status`, not `previousStatus`. Reading a controller tells you the shape a handler *returns*; it does not tell you the shape a client *receives*.
- **It closes the drift the 2026-09-01 edition opened deliberately.** Putting a written-but-unmerged route in the proposed file was the right call — it would have created false drift in the live spec and let someone generate a client for a route that 404s — and the move took one day. The pattern is worth reusing, but only with the merge actually following; a "proposed" entry that describes real code is a liability if it sits there.

Not resolved by this: the per-user audit trail the admin console calls at `GET /users/{id}/audit-trail` (`beevia-admin/src/features/users/api.ts`), which still matches no operation in either spec and still lacks the `/admin` prefix every other admin route carries. The activity feed is a global stream, not a per-user one. It does, however, add a third way to close it — filtering `admin_activity` on `target_type = 'user'` would make the trail a query parameter on the feed rather than a fourth endpoint.

### 5.4b A report-generation feature is unmerged on `feat/admin-reports` — and it collides with Module 4's proposed paths

**Found 2026-09-09.** `origin/feat/admin-reports` (pushed 2026-09-08, ~1,700 lines) carries a complete Reports module: a catalogue of report types, asynchronous CSV generation, a run history and a download route, under a new `reports` permission module with an `admin_reports` table already released in `beevia-db-schema` v0.0.28/29.

| Method | Path (unmerged) | Permission |
|---|---|---|
| GET | `/admin/reports/types` | `reports:view` |
| POST | `/admin/reports` | `reports:create` |
| GET | `/admin/reports` | `reports:view` |
| GET | `/admin/reports/{id}` | `reports:view` |
| GET | `/admin/reports/{id}/download` | `reports:export` |

**It is not in `openapi.admin.yaml` and should not be until it merges** — the implemented spec documents `main`. It is recorded here because of what it does to the proposed file.

**The collision.** Module 4's two remaining proposed operations are `GET /admin/reports/{reportId}` and `POST /admin/reports/{reportId}/resolve` — a *moderation* report. This branch's `GET /admin/reports/{id}` returns a *generated CSV report*. Same path, unrelated resources, and the two cannot coexist. The generation feature has a board behind it (project "Beevia Admin Dashboard", sprint `0901-admin`, three of its four stories in flight) while Module 4's workflow half has nothing, so in practice the branch wins by default.

**The resolution is cheap if it is made before the merge and expensive after.** Module 4's workflow operations should hang off the path its shipped queue already occupies — `/admin/chats/reports/{reportId}` and `/admin/chats/reports/{reportId}/resolve` — which is also where a reader would look for them now that §3.13 exists. The proposed file carries this as a comment above both operations rather than a rename, because renaming a proposal on the strength of an unmerged branch is guessing; the note is the decision point.

Worth noting separately: this feature is the answer to "Analytics & Reporting" that Module 7 has been waiting for, and it arrived as exports rather than as the five time-series operations §5.4 proposes. That is a reasonable substitution — an operator who can export a filtered CSV can answer more questions than five fixed charts — but §5.4's proposals should be re-read against it when it merges, not before.

### 5.5 Module 8 — Account Deletion Requests (3 proposed)

`GET /admin/deletion-requests`, `GET /admin/deletion-requests/{id}`, `POST /admin/deletion-requests/{id}/confirm`.

The PRD tracks deletion completion within 5 days as a compliance KPI, which is unmeasurable today.

**Corrected 2026-09-02 — this module's premise no longer holds.** Earlier editions of this RFC said `DELETE /users/me` moves accounts to a `deleting` status that nothing reads, and proposed these endpoints as the reader of that queue. Migration `0027` (2026-08-06) renamed the enum value `deleting` to `deactivated` and handed it to the *admin* deactivate path (§3.4a); `AccountDeletionService` now writes `deleted` directly. **There is no in-flight deletion state any more, so there is no queue.** An account is either untouched or finished, and the 5-day KPI is not merely unsurfaced — it is unrecorded.

Building Module 8 therefore starts one step further back than these three endpoints suggest: either reintroduce an in-flight status, or add a deletion-request table. The table is the better answer, because the detail endpoint below wants per-partner progress and a retention basis, and neither fits in a status column.

The detail endpoint carries what Compliance actually needs: per-partner progress, what is **retained** and under what legal basis, and a `residual_messages` count for ciphertext left in other users' conversations that the deleted user's keys no longer exist to read. The confirm endpoint records a human attestation — an auditor needs a named sign-off, not only a job status.

---

## 6. Suggested sequencing

**Do first — before any staff account exists in production.**
2FA (§4.3), global fail-closed guards (§4.2), separate admin signing secret and `aud` claim (§4.1), Swagger disabled in production and the service made non-publicly-routable (§4.6).

None of these are features. All of them are cheaper now than after the first real admin account is created.

**Phase 1 — finish what is started.**
Assisted PIN reset (the one missing Module 3 capability), and seeding the three spec roles with a test asserting their permission matrices.

**Phase 2 — the config gap.**
Module 6, prioritising `fee_configs` and `currency_provider_configs` over country gating — those are being edited by hand in production today.

**Phase 3 — the deletion queue.**
Module 8. Small, and unblocks a compliance KPI that is currently unmeasurable.

**Phase 4 — oversight and analytics.**
Modules 5 and 7. ~~Module 5's reconciliation depends on a partner statement API that does not exist yet; scope that separately.~~ **Overtaken on 2026-09-04**: half of Module 5 shipped, out of order, and the dependency turned out to be a day's work (§5.2). What remains here is Module 7's analytics queries and Module 5's wallet detail and flagging.

**Blocked on a decision — Module 4.**
Do not start until §5.1 is resolved. Building the queue on metadata (option A) is a day's work; building it on reporter-attached excerpts (option B) requires a consumer-app change and a consent flow. Choosing C would trade the product's core claim for a moderation feature and should be an explicit, documented decision if it is ever made.

### 6.3 What the shipped modules went without — five gaps for the dashboard

The ten operations that landed between 2026-09-04 and 2026-09-08 are narrower than their proposals in five ways. None is a defect; all five are things a dashboard build will hit on day one. **One of the four listed here on 2026-09-08 has since been fixed**, and is kept with its resolution rather than deleted, so the list reads as a record rather than a snapshot.

| Gap | Proposed | Shipped | Consequence |
|---|---|---|---|
| ~~**Statement filters**~~ **— mostly closed 2026-09-08** | `direction`, `from`, `to` on the per-user statement | `dateFrom` / `dateTo` on **both** feeds, bounding the count as well as the rows; `direction` still missing | The date half is done and done carefully: a bare `dateTo` widens to `23:59:59.999Z` so picking a day includes that day, an impossible date is a `400` rather than a filter that silently matches nothing, and `pagination.total` under a filter is the total *for that range*. What remains is `direction` — "show me only money out" is still a client-side filter over a paged feed. |
| **Reconciliation period** | `from` / `to` / `currency`, required | None; the run is unbounded and NGN-only | Reconciliation always covers the account's whole history, capped at 500 payouts and 1000 ledger rows. On an active account those caps bind silently, and movements older than the window fall into the buckets as false discrepancies. |
| **Pagination shape** | `meta: PaginationMeta` | `data.pagination`, with `page` where `PaginationMeta` says `current_page` | This service now has **three** pagination conventions — `meta`/`PaginationMeta` on every earlier list, cursor `before`/`next_cursor` on the activity feed, and `data.pagination` on the transaction feeds *and now the wallets list*. A shared client-side pager cannot cover all three, and the third has stopped being a one-off. |
| **Per-wallet partner balance** | `partner_balance` and `in_sync` beside the ledger balance on every wallet row (§5.2) | Ledger balance only | A per-wallet mismatch is invisible in the Wallets screen. Answering "is this one wallet in sync" means leaving the screen for `GET /admin/reconciliation/users/{userId}`, which runs a full unbounded comparison for the whole account. |
| **Module 4 is a queue without a workflow** *(new 2026-09-09)* | `status` (open/reviewing/actioned/dismissed), the reported user's prior report history, and a `resolve` action closing the report with an outcome | `GET /admin/chats/reports` returns every report ever filed, newest first, with no status and no way to action one | **The queue cannot be worked off.** A moderator who handles a report has no way to say so, so tomorrow's queue is today's plus arrivals and the backlog only grows. Nothing links a report to the suspension it caused, so "what did we do about this?" is unanswerable from the API. And because there is no per-user report history on the row, a reviewer cannot tell a first complaint from a pattern — which is the *only* signal metadata-only moderation has (§5.1). |

The pagination gap is the one worth fixing while it is cheap, and it has now spread from two endpoints to six — the chats list and the report queue both use `data.pagination` too — so it gets cheaper to fix only in the sense that it will never be cheaper than today. The reconciliation caps should become a board item rather than a surprise, because exceeding them produces *wrong output* rather than a truncation the caller can see. The partner-balance gap is the one that most undercuts the screen it shipped for: a wallets list whose whole purpose is custody oversight cannot show whether custody agrees with the partner.

**The fifth is the one to act on first**, because it is the only one where the shipped code changes a *policy* position. Module 4 was blocked on a product decision for a month; it is now unblocked and half-built, and the half that is missing is the half that makes it a moderation tool rather than a list. The reported-user history in particular is not scope creep — §5.1 argues that patterns across reports are the entire signal available to metadata-only moderation, so a queue that does not surface them delivers the option's costs without its benefit.

---

## 7. Open questions

1. **Do the three spec roles have fixed permission matrices?** The code allows any matrix. If Support must *never* have `kyc:view`, that needs to be an invariant with a test, not a convention.

2. **What happens to a suspended user's money?** `POST /admin/users/{id}/suspend` blocks access. Can they still receive an incoming transfer? Does a pending escrow still expire and refund on schedule? The account and ledger lifecycles are not obviously joined up.

3. **Who reviews the reviewers?** ~~Is there a single admin-activity log spanning both?~~ **Answered 2026-09-02**: `admin_activity` is that log, and `GET /admin/activity` reads it (§3.8). What remains open is its coverage — only three of eleven modules append to it, so money and KYC actions are still recorded nowhere but their own module's history. **Can a Super Admin edit their own role?** Still open, and now more visible: the feed would record the change, but nothing prevents it.

4. **Is there an admin session model?** The consumer API has a `sessions` table with refresh-token rotation. The admin API issues an access token at login with no refresh, no revocation endpoint and no session listing.

   **The sub-question "does deactivating an admin invalidate live sessions immediately?" is answered: effectively yes.** `AdminAuthGuard` reloads the admin row and rejects anything but `status === 'active'` on *every* request, so flipping the status locks the account out on its next call without needing a session table at all. That is a legitimate design and it should be recorded as such rather than left as an open worry.

   What stays open is narrower: there is no way to revoke **one** session (a lost laptop) without deactivating the whole account, no way to see where an admin is signed in, and the per-request `admins` lookup is a database read on every authenticated call. Note the contrast with the consumer side, which reaches the same guarantee by the opposite route — an explicit `sessions` table revoked inside the status-change transaction (§3.4a). Two services, two mechanisms, one property; worth converging deliberately rather than by accident.

5. **Where does this service run?** The security posture depends almost entirely on the answer. If it is publicly routable, §4.2 and §4.6 become urgent; if it is VPN-only, they are still worth fixing but the exposure is bounded.

6. **Should the two services share more than the schema?** §4.5 duplicates four presentation-layer files today. That is manageable, but the boundary should be a decision rather than an accident — particularly before anything ledger-adjacent is written on the admin side.
