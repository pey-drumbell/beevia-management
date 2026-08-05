# RFC: Beevia Admin API Surface

| | |
|---|---|
| **Status** | Draft — for review · created 2026-08-05 |
| **Scope** | The HTTP surface of `beevia-admin-api`: what exists today, and what "Beevia Admin Dashboard.md" specifies that does not exist yet |
| **Companion artifacts** | [`openapi.admin.yaml`](./openapi.admin.yaml) — implemented, 29 operations · [`openapi.admin.proposed.yaml`](./openapi.admin.proposed.yaml) — designed but unbuilt, 23 operations |
| **Sibling RFC** | [`api-rfc.md`](./api-rfc.md) — the consumer API |
| **Sources** | `beevia-admin-api/src/**`, `beevia-db-schema/src/schema/*`, `Beevia Admin Dashboard.md` |
| **Base path** | `/api/v1`, with every business route further prefixed `/admin` |

> **Paths in this document.** Unless prefixed otherwise, `src/` refers to `beevia-admin-api/src/`. The service repositories are unmodified by this work.

---

## 1. Summary

`beevia-admin-api` is a **separate NestJS service** from the consumer API, sharing the database through the published `@drumbell-technologies/beevia-db-schema` package. It is **29 operations** across four controllers, backing the admin dashboard specified in `Beevia Admin Dashboard.md`.

**Three of the spec's eight modules are built.** What exists is well-made: the permission model is more capable than the spec asked for, KYC values are masked by default with reveals logged, case notes are append-only, and account actions require a structured reason and land in a queryable history.

Against that, three findings need attention before this service is exposed to real staff:

| # | Finding | Severity |
|---|---|---|
| 1 | **No 2FA**, despite the spec making it mandatory. Email + password is the only barrier to an account that can read BVNs and suspend users. Also no lockout and no rate limiting on login. | **High** |
| 2 | **Guards are per-controller, not global.** A new controller that omits `@UseGuards(...)` is completely unauthenticated — not merely under-authorised. | **High** |
| 3 | **Module 4 (Trust & Safety) cannot be built as specified.** It asks the moderation queue to show "reported messages"; chat is end-to-end encrypted and the server holds no key. | **Blocking — needs a product decision** |

### Module coverage

| # | Spec module | State | Ops |
|---|---|---|---:|
| 1 | Authentication & Access Control | 🟡 **Partial** — login and invite work; **no 2FA** | 2 |
| 2 | Admin Account Management | ✅ **Built** | 3 |
| 3 | User Management & Support Tools | 🟡 **Partial** — no assisted PIN reset | 18 |
| 4 | Trust & Safety / Content Moderation | ⛔ **Not built** — and not buildable as written | 0 |
| 5 | Transaction & Wallet Oversight | ⛔ **Not built** | 0 |
| 6 | Country & Feature Configuration | ⛔ **Not built** | 0 |
| 7 | Analytics & Reporting Dashboard | ⛔ **Not built** | 0 |
| 8 | Account Deletion Requests | ⛔ **Not built** | 0 |

Modules 3 and 2 being the built ones is the right call — user search and support tooling is what a support agent needs on day one, and admin account management is its prerequisite.

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

### 3.2 Admin Accounts (3) — spec Module 2

| Method | Path | Permission | Notes |
|---|---|---|---|
| GET | `/admin/accounts` | `admin_accounts:view` | ✅ Paginated; filter by search, access level, status |
| POST | `/admin/accounts/invite` | `admin_accounts:create` | ✅ Role assigned at invite time |
| PATCH | `/admin/accounts/{id}` | `admin_accounts:edit` | ✅ Re-role and activate/deactivate — the immediate-revocation path the spec requires |

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
| POST | `/admin/users/{id}/suspend` | `users:edit` | ✅ Structured reason required |
| POST | `/admin/users/{id}/restrict` | `users:edit` | ✅ Softer sanction |
| POST | `/admin/users/{id}/activate` | `users:edit` | ✅ |
| POST | `/admin/users/{id}/deactivate` | `users:**delete**` | ✅ Terminal action, separately gated |

The `suspend`/`deactivate` permission split is a good detail: a role can be allowed to suspend without being allowed to terminate.

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

All 23 proposed operations are in [`openapi.admin.proposed.yaml`](./openapi.admin.proposed.yaml).

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

Note the data already accumulates: `conversation_reports` is populated by the consumer app's `POST /conversations/{id}/report`, and **nothing reads it**. Reports are piling up unreviewed today.

### 5.2 Module 5 — Transaction & Wallet Oversight (4 proposed)

`GET /admin/users/{id}/wallets`, `GET /admin/users/{id}/transactions`, `POST /admin/transactions/{id}/flag`, `GET /admin/reconciliation`.

Two design points:

**Flagging annotates, never mutates.** Flagging marks a transaction for investigation; it does not reverse, hold, or alter the ledger. Any actual reversal must go through the consumer API's ledger primitives, so there remains exactly one implementation of money movement. This is the constraint §2.2 exists to protect.

**Reconciliation has an unmet dependency.** Comparing Beevia's ledger against the partner's records needs a statement or balance-report call on the partner adapter, which does not exist in either service today. The endpoint is specified; the integration behind it is a separate piece of work.

### 5.3 Module 6 — Country & Feature Configuration (4 proposed)

`GET/PATCH /admin/countries`, `GET/PATCH /admin/feature-flags`.

The spec's motivation — "expanding banking to a second country requires an engineering release" — is accurate. Country eligibility is not modelled anywhere.

There is a second, sharper case for this module that the spec does not make: `currency_provider_configs` and `fee_configs` are both documented in code as **"admin-managed"**, and `ProviderResolverService.invalidate()` carries the comment *"call after admin mutations"*. Neither service exposes a route. **Changing a fee or repointing a currency's banking rail is today a hand-written `UPDATE` against production Postgres, unaudited.** That is a more urgent gap than country gating, and it belongs in this module.

One safety rule for the toggle: disabling banking for a country must gate **new** onboarding and wallet creation only. Existing wallets and balances must be unaffected, or a config toggle becomes a way to strand customer funds.

### 5.4 Module 7 — Analytics & Reporting (5 proposed)

Signups, onboarding funnel, path split, engagement, and a dashboard overview.

Mostly queries over data that already exists — the `onboarding_step` enum models the whole state machine, so funnel analysis needs no new instrumentation. Engagement counts read message and call *metadata* rows, never content.

The `dashboard` permission module exists in the enum with no routes behind it; the overview endpoint is its natural first occupant.

### 5.5 Module 8 — Account Deletion Requests (3 proposed)

`GET /admin/deletion-requests`, `GET /admin/deletion-requests/{id}`, `POST /admin/deletion-requests/{id}/confirm`.

The consumer API's `DELETE /users/me` moves accounts to the `deleting` status, and nothing reads that queue. The PRD tracks deletion completion within 5 days as a compliance KPI, which is unmeasurable today.

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
Modules 5 and 7. Module 5's reconciliation depends on a partner statement API that does not exist yet; scope that separately.

**Blocked on a decision — Module 4.**
Do not start until §5.1 is resolved. Building the queue on metadata (option A) is a day's work; building it on reporter-attached excerpts (option B) requires a consumer-app change and a consent flow. Choosing C would trade the product's core claim for a moderation feature and should be an explicit, documented decision if it is ever made.

---

## 7. Open questions

1. **Do the three spec roles have fixed permission matrices?** The code allows any matrix. If Support must *never* have `kyc:view`, that needs to be an invariant with a test, not a convention.

2. **What happens to a suspended user's money?** `POST /admin/users/{id}/suspend` blocks access. Can they still receive an incoming transfer? Does a pending escrow still expire and refund on schedule? The account and ledger lifecycles are not obviously joined up.

3. **Who reviews the reviewers?** `admin_user_actions` records actions against consumer accounts, and role and account changes are described as security-relevant with their own audit trail. Is there a single admin-activity log spanning both, and can a Super Admin edit their own role?

4. **Is there an admin session model?** The consumer API has a `sessions` table with refresh-token rotation. The admin API issues an access token at login with no visible refresh, revocation or session listing. Deactivating an account should invalidate live sessions immediately — does it?

5. **Where does this service run?** The security posture depends almost entirely on the answer. If it is publicly routable, §4.2 and §4.6 become urgent; if it is VPN-only, they are still worth fixing but the exposure is bounded.

6. **Should the two services share more than the schema?** §4.5 duplicates four presentation-layer files today. That is manageable, but the boundary should be a decision rather than an accident — particularly before anything ledger-adjacent is written on the admin side.
