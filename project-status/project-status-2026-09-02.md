# Beevia — Project Status

**As of 2026-09-02** · Sprint **08-01** (10 Aug → 28 Aug) — **closed 5 days ago, still no successor sprint**
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-02.csv` + `beevia-activity-2026-09-02.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision. **This edition corrects two claims from 1 Sep and one that four documents have carried since 6 August — see §0.1.**

---

## Quick overview

> **Nothing moved today. Zero board transitions in 27 hours, zero commits authored in any repo, zero items accepted for the twenty-third consecutive day. What the quiet bought was a proper look at the code, and it found two things worth more than the day's activity would have been: `openapi.admin.yaml` has been describing a contract the admin service stopped honouring on 6 August — five separate facts wrong, through nineteen "clean" audits — and the mobile bank-payout flow that yesterday's report called an unwired stub has in fact been fully built, on a branch, unmerged for five days.**

| | 1 Sep | 2 Sep | Δ |
|---|---:|---:|---:|
| To do (leaves) | 0 | 0 | 0 |
| In progress (leaves) | 2 | 2 | 0 |
| Blocked (leaves) | 2 | 2 | 0 |
| In review / QA (leaves) | 28 | 28 | 0 |
| Done (leaves) | 11 | 11 | 0 |
| **Board transitions in the last 24 h** | 5 | **0** | **−5** |
| **Forward review exits, whole sprint** | 0 | **0** | **23 days** |
| API surface (consumer / admin) | 131 / 29 | 131 / **30** | 0 / **+1** |
| Commits authored today | 24 | **0** | −24 |
| Successor sprint | none | **still none** | — |

**Team, at a glance:**

| Person | Owns | Leaf state | First submissions to review (7d) | Median cycle | Open WIP (age) | Commits (7d) | Flag |
|---|---|---|---:|---:|---|---:|---|
| Ayomikun Araoye | backend + admin API | 1 In prog, **14 Review**, 3 Done, 1 Blocked | 3 | 2.4 d | 1 item @ 4 d | **52** | Shipped the admin activity feed; no commits today after the busiest day on record |
| David Samuel | mobile | **9 Review**, 1 Blocked | 4 | 2.0 d | — | 1 | **11 unmerged commits on `BVA-I192`** that build the payout flow §6 called missing |
| Philip Chidera | design | 1 In prog, 5 Review, **8 Done** | 3 | 0.9 d | 1 item @ **6 d** | — | 8 of the sprint's 11 completions; open item now 6 d against a 0.9 d median |
| Promise Udo | admin dashboard | — (no board presence) | — | — | — | 3 | Unchanged: build config only, mock-backed money modules untouched |

Cycle-time medians are unchanged from 1 Sep because no item completed a pass today; the method is the one fixed in the 1 Sep edition §0.1. Commit counts are a sliding 7-day window, so they move a little even on a zero-commit day.

**The two questions for standup:** (1) **`BVA-I192` has been sitting unmerged on `beevia-mobile` since 28 August** — eleven commits, ~3,900 lines, and it wires bank payout to `GET /wallets/banks`, `POST /wallets/resolve-account` and `POST /wallets/withdraw` with tests. Yesterday this report asked whether anyone had picked up that wiring; the answer is that it was picked up weeks ago and is waiting. What is it waiting for? (2) The two card items have now been BLOCKED for two days with no recorded reason, and the fix that most plausibly clears them merged on 1 September. Is the blocker gone?

**The three things worth knowing:**

1. **The admin API spec has been wrong since 6 August, and the audit could not see it.** Documenting yesterday's activity-feed merge meant reading the admin service properly, which surfaced four contract changes that shipped on 6 August and were never written down, plus one error that was wrong from the day the spec was authored. Admin `deactivate` stopped meaning "hand the account to the erasure pipeline" and became a reversible state; suspend and deactivate began revoking every live session; `GET /admin/users` gained a filter and changed how it reads dates; and the four lifecycle endpoints have *never* returned the response shape the spec claims. **Nineteen consecutive daily audits reported this service clean**, because every one of these lives inside an operation and the check compares route inventories. All five are now fixed in `openapi.admin.yaml` (§3).
2. **The mobile payout flow is built and unmerged, which changes yesterday's diagnosis but not the score.** `origin/BVA-I192` replaces the hard-coded bank list and the fake `'John Doe'` account resolver with real API calls, and adds provider and widget tests. It has been ready for five days. The rubric does not score unmerged work and capability 6 does not move — but "nobody has wired it" was the wrong reading, and "it is written and nobody has merged it" is a different and more fixable problem. **The add-money side is not fixed**: `0099873456` is still compiled in on both `main` and the branch, in two files (§6).
3. **`GET /admin/activity` merged, taking the admin API to 30 operations** and opening a fourth of the dashboard's eight modules. It is the first proposal this pipeline has watched ship, and the one-day round trip from "documented as proposed-because-unmerged" to "moved to the implemented spec" is the process working. Its transcription had one real defect, now corrected: it was written from the controller's TypeScript property names, but the response interceptor converts every key to snake_case, so the wire shape is `occurred_at` and `next_cursor`, not `occurredAt` and `nextCursor` (§3.2).

**If you read nothing else:** no work moved today; the spec drift found while reading the code is the most consequential thing in this report; and there is a finished mobile payout feature that needs a merge decision, not more development.

---

## 0.1 Corrections

### Correction 1 — to four documents, standing since 2026-08-06

**Claim: "the `user_status` enum already has a `deleting` state that nothing reads."**

This sentence, or a paraphrase, appears in `api-rfc.md`, `suggestions.md`, `openapi.proposed.yaml` and `openapi.admin.proposed.yaml`, and it has been the load-bearing premise of the proposed account-deletion work: the hard part is done, someone just needs to surface the queue.

**It has been false since 2026-08-06.** Migration `0027` renamed the enum value `deleting` to `deactivated` and handed it to the *admin* deactivate path. `AccountDeletionService` now writes `deleted` directly. There is no in-flight deletion state at all, so there is no queue to list — an account is either untouched or finished.

The consequence is that Module 8 and `GET /users/me/deletion-status` are **larger than every previous edition has scoped them**, not smaller. Both need either a new in-flight status or a deletion-request table, and the table is the better answer because the PRD wants per-partner progress and a retention basis, neither of which fits in a status column. All four documents are corrected.

### Correction 2 — to the 1 September edition

**Claim: "an identity guard (`bvn_registered_elsewhere`)."**

That error code existed for one day. It was introduced on 31 August and replaced on 1 September by `anchor_customer_claimed`, which the 1 Sep report was written too early to see. The semantics also changed, and for the better: the guard no longer compares Anchor's name for the customer (frequently test data) but asks whether another *Beevia* user already holds that Anchor customer — which is the invariant that actually matters, since two users sharing one deposit account would mix funds. Neither code has ever appeared in a spec, correctly: see §2.2 for why.

**Claim: "`GET /admin/activity` returns 404 against `beevia-admin-api` main."**

True when written, superseded within hours. `BVA-1226` merged at 15:14 UTC on 1 September. The operation has moved from `openapi.admin.proposed.yaml` to `openapi.admin.yaml`, exactly as that edition instructed its successor to do.

---

## 1. Sprint 08-01 — five days after close

### 1.1 Where the 43 leaves sit

| Status | Leaves | Share | Δ |
|---|---:|---:|---:|
| **Review / QA** | **28** | **65%** | 0 |
| Done | 11 | 26% | 0 |
| Blocked | 2 | 5% | 0 |
| In progress | 2 | 5% | 0 |
| To do | 0 | 0% | 0 |

Owner split of the review queue: Ayomikun 14, David 9, Philip 5.

67 board rows = 43 leaves + 24 parent stories. All figures above are leaves; parents are excluded to avoid double-counting.

### 1.2 The board did not move at all

**The newest audited action anywhere on the board is 1 September at 11:11 UTC** — roughly 27 hours before this report's cut-off. Not one status change, assignment, comment or item creation has been recorded since. This is the first edition in which the correct answer to "what moved" is *nothing*.

That is worth stating plainly rather than dressing up, because a reader scanning §1.1 for movement will find none and should not have to wonder whether the export failed. It did not: 67 items, 67 audit trails, 67/67 modified dates recovered.

### 1.3 The review queue

| Measure | 1 Sep | 2 Sep |
|---|---:|---:|
| Leaves currently in REVIEW/QA | 28 | 28 |
| Transitions **into** REVIEW/QA (all time) | 49 | 49 |
| Transitions **out of** REVIEW/QA (all time) | 22 | 22 |
| Transitions REVIEW/QA → **Done** | **0** | **0** |
| Median queue age | 6 d | **7 d** |
| Oldest backed by a submission | 15 d | **16 d** (7 items) |
| Arrived in the last 2 days | 1 | **0** |

All 22 recorded exits went backwards — 13 to In progress, 8 to To do, 1 to BLOCKED — and **all 22 were performed by the same person**, the mobile lead. **The transition REVIEW/QA → Done has never occurred in this sprint.** All 11 completions went In progress → Done, bypassing the queue entirely. Twenty-three days, 49 submissions, zero acceptances.

The queue aged by exactly one day because nothing entered and nothing left. Seven items are now 16 days old.

Unchanged data gap: `BVA-I185` (Wallet Summary Endpoint, Ayomikun) shows status REVIEW/QA with no status-change transition into it — completed 13 Aug, reopened 14 Aug, current status apparently set by that reopen. It is the one queue entry not backed by a submission; 27 of the 28 are measurable, and the median above is over those 27.

### 1.4 The two blocked items — unchanged, and now two days silent

`BVA-I182` (*In-Chat Request Flow & Cards*, David Samuel) and `BVA-I197` (*Card Issuance Integration*, Ayomikun Araoye) both moved In progress → BLOCKED at 15:11 UTC on 31 August and have not moved since. `BVA-I197` has been blocked and unblocked three times in eight days. The board still records no reason for any of them.

The 1 Sep edition's reading still stands and has not been acted on: `beevia-api` merged `fix/card-anchor-endpoints` on 1 September, correcting two defects (`updateCard` issuing `POST` where Anchor serves `PATCH`; the reveal token read from `data.attributes.token` rather than `data.token`) that would break card issuance and card reveal outright. That is a plausible cause for both blocks and it appears fixed. **Nobody has moved either item, so if it is fixed, the board does not know.**

### 1.5 Still no successor sprint

The Zoho project holds exactly three sprints: `08-01`, `0702`, `0701`. **08-02 has not been created**, five days after 08-01 closed. This is the fifth consecutive edition reporting it.

---

## 2. What shipped this cycle

**Nine commits were pulled, all authored on 1 September after the last edition's cut-off. Nothing was authored on 2 September in any of the five repositories.**

The consumer API stays at 131 operations. The admin API moves 29 → 30.

### 2.1 `beevia-admin-api` (6 commits) — the activity feed, merged

`BVA-1226` merged, bringing `GET /admin/activity` and the `record()` call sites that feed it. It is the first occupant of the dashboard's Module 7 and the first thing to write to the `admin_activity` table that landed on `beevia-db-schema` the day before.

Two properties are deliberate and both are unusual enough to want a reviewer's eye:

- **No `@RequirePermission`.** Any authenticated admin may call it; the service resolves the caller's viewable modules and filters rows in SQL, returning an empty list — not a 403 — to an admin entitled to nothing. Right shape for a feed, but it is the one route in the service where "no permission declared" is the *normal* state, which makes it the hardest place to notice a missing guard.
- **Events are appended inside the producing module's own transaction**, so the feed cannot record a change that rolled back nor miss one that committed. That is the correct construction and rarer than it should be.

**"Cross-module" currently means three modules of eleven** — `users`, `roles_permissions`, `admin_accounts`. Nothing from money, KYC, chats or reports appends. Those are the modules an oversight feed exists for, so the console's home feed today shows admin housekeeping rather than platform activity. Extending it is cheap; it just has not been done.

### 2.2 `beevia-api` (3 commits) — provisioning, and a new silent success

The provisioning path learned to **connect an Anchor deposit account the customer already holds** instead of opening a duplicate. The reasoning in the code is sound and worth repeating: a BVN belongs to exactly one Anchor customer, so re-creating one and re-submitting the BVN fails *"BVN already exists"* and the fresh account can never be verified — the "does not have kyc verification" dead-end. Connecting the existing ACTIVE account, preferring the funded one so no balance is orphaned, avoids it.

It also added `400 anchor_customer_claimed`, refusing to connect an Anchor customer another Beevia user already holds. Correct guard, real invariant.

**But it throws inside the queued provisioning job, not inside the request** — and that is the finding. `maybeProvision()` only ever enqueues. So a user whose BVN is already linked to another account receives a `200` from `/upgrade/profile`, sees a completed upgrade, and never gets a wallet. No client-visible error is produced at any point, because the failure happens after the response was sent.

This is the third distinct silent-200 found on the same seam in two days, and it should be read as a category rather than three incidents: **nothing surfaces a failed provisioning job to the user.** Guards keep being added at the point of failure, inside a job whose outcome no endpoint reports. The durable fix is a readable provisioning state on the user — `GET /upgrade/status` is the obvious home — carrying `failed` and a reason, so the client can say *"we could not open your account, and here is why."* That is worth more than either individual guard, and it is now recorded in `api-rfc.md` §5.1.

Also: `onboarding_step` now jumps straight to `completed` whenever an NGN wallet is provisioned, from whatever step the account was on, self-healing users stranded outside the normal step machine. Sensible, and it means a client must not assume the value only ever advances to its immediate successor. Documented in `openapi.yaml`.

### 2.3 Repo staleness

| Repo | Last commit to `main` | Days silent | Δ |
|---|---|---:|---:|
| `beevia-api` | 1 Sep | 1 | +1 |
| `beevia-db-schema` | 1 Sep | 1 | +1 |
| `beevia-admin-api` | 1 Sep | 1 | +1 |
| `beevia-admin` | 31 Aug | 2 | +1 |
| `beevia-mobile` | 26 Aug | **7** | +1 |

Every repo aged by exactly one day, which is the arithmetic of a day with no commits.

Unmerged remote branches: **`beevia-mobile` carries `origin/BVA-I192` at 11 commits ahead (§6)** plus nine dependabot branches and `self-hosted-runners` (7 ahead); `beevia-api` carries `origin/victor` (1 ahead, last touched 28 July). Unmerged work does not count toward readiness scoring.

---

## 3. Spec updates made this cycle

The audit opened at `code=30 spec=29` on the admin API — one route in code, undocumented, and the same route flagged as a shipped proposal. Closing that took reading the admin service, and reading it found four more contract changes that had nothing to do with today's merge. The audit now reports `131/131` consumer and `30/30` admin, all four specs valid, no `x-beevia-*`, no broken refs, no orphaned components.

### 3.1 The main finding — 27 days of invisible drift

Four contract changes shipped to `beevia-admin-api` `main` on **2026-08-06** (commits `689acc4`, `c242320`, `e1c1f66`) and were never written into `openapi.admin.yaml`. A fifth defect was wrong from the day the spec was authored. Every one of them survived **nineteen consecutive daily audits reported clean.**

| # | What the spec said | What the service does | Since |
|---|---|---|---|
| 1 | `deactivate` moves the account to `deleting`, the consumer erasure path — "not a hard delete" but not reversible either | Moves it to `deactivated`. **Nothing is destroyed**, and `activate` restores it whole, answering `User restored.` A `deleted` account is refused `409` | 6 Aug |
| 2 | Nothing about sessions | `suspend` and `deactivate` **revoke every live session in the same transaction** and report `sessions_revoked`. `restrict` deliberately does not | 6 Aug |
| 3 | `GET /admin/users` returns everyone | Excludes `deactivated` and `deleted` unless `includeEnded=true` or `accountStatus` names one — which makes `accountStatus=deactivated` the restore queue | 6 Aug |
| 4 | `joinedFrom`/`joinedTo` are `date-time`; one shared `Limit` capped at 100 | Both accept a bare `YYYY-MM-DD`, with `joinedTo` widened to end-of-day so the named day is included. Roles and admin accounts cap at **500**; users still 100 | 6 Aug |
| 5 | The four lifecycle endpoints return an `AdminUserAction` history row (`id`, `note`, `performed_by`, `created_at`) | They return the **transition** (`user_id`, `action`, `previous_status`, `status`, `sessions_revoked`, `reason`, `at`). Every field but `action` differs | always |

Item 5 is the worst of them: a client generated from that spec would read `created_at` off a body that has never carried one. It is now a distinct `AdminUserActionResult` schema, and `Limit` has split into `Limit` (users, 100) and `ConfigLimit` (roles and admin accounts, 500).

**Why the audit missed all five, and what would catch them.** Not one of these adds, removes or renames a route. The drift check compares route inventories between controller decorators and spec paths — a genuinely useful check, and not the one that would have caught any of this. Response bodies, query parameters, enum values and status codes are all invisible to it.

The cheapest real fix is available today: `beevia-admin-api/src/main.ts` already builds a full OpenAPI document with `SwaggerModule.createDocument`. If the service published that artifact, the audit could diff *it* against these files instead of inferring the surface from decorators, and all five would have been caught on 7 August. That is a recommendation for the backend owner, not something this workspace can do to a read-only repo.

**Read this next to the standing "contract drift is invisible to automation" note.** Previous editions have counted six such findings in twelve days and treated each as a one-off. Five more today, one of them four weeks old, makes the pattern the finding: this pipeline reliably detects *new routes* and reliably misses *changed contracts*, and it has been reporting the admin service clean while it was not.

### 3.2 `GET /admin/activity` moved from proposed to implemented (admin 29 → 30, proposed 24 → 23)

Transcribed into the proposed file on 1 September with an explicit instruction to move it on merge; it merged the next day and has moved. `admin-api-rfc.md` gains §3.8 and its counts are updated; §5.4a is rewritten from a proposal into a record of what shipped.

**The transcription had one real defect, and it is instructive.** Documenting from the branch got the parameters, the permission model and the pagination scheme right. It got the **key casing** wrong: the operation was written from the controller's TypeScript property names (`adminId`, `entityType`, `occurredAt`, `nextCursor`), but `ResponseInterceptor` converts every response key to snake_case recursively before it leaves the service. The wire shape is `admin_id`, `entity_type`, `occurred_at`, `next_cursor` — and the same conversion reaches inside the free-form `metadata` object, so a `user_status_changed` event carries `previous_status`, not `previousStatus`. The implemented spec now carries the wire shape.

The general lesson is worth keeping: reading a controller tells you the shape a handler *returns*; it does not tell you the shape a client *receives*.

### 3.3 The `deleting` status correction, propagated

Four documents corrected — see §0.1. `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` now say plainly that the deletion-queue designs have lost the status they were built on and need a design decision before anyone starts them; `api-rfc.md` and `suggestions.md` carry the correction inline rather than quietly dropping the old claim.

### 3.4 Still open from previous editions

`beevia-admin` still calls `GET /users/{id}/audit-trail` (`src/features/users/api.ts`), still without the `/admin` prefix every other admin route carries, still routed through a mock adapter, and still matching no operation in either admin spec. The new activity feed does not resolve it — a global stream is not a per-user trail — but it adds a third option: filter `admin_activity` on `target_type = 'user'` and make the trail a query parameter rather than a fourth endpoint. Unchanged as a decision for the two owners.

---

## 4. Admin dashboard board

The second Zoho project, *Beevia Admin Dashboard* (`187554000000127002`), **still has no sprints**; step 1b returned exit 3 again, for the **fourteenth consecutive edition**. The board contributes nothing, so Promise Udo's row remains sourced from commits.

This cycle: no commits at all. The nine feature modules, four of them explicitly `MOCK IMPLEMENTATION — no network calls`, are unchanged. The four Module 5 endpoints those mocks are waiting on (`/admin/transactions/{id}/flag`, `/admin/reconciliation`, `/admin/users/{id}/wallets`, `/admin/users/{id}/transactions`) remain proposed-only.

One genuine change in their favour, from the other side: the admin API's surface grew for the first time since 17 August, and §3.1's corrections mean the spec the dashboard is written against is now accurate about user lifecycle behaviour. A dashboard built on the previous text would have shown a deactivation as irreversible and would not have known that suspending a user signs them out.

**Pipeline note, unchanged:** the two boards are never summed; admin exports land in `sprint-board-exports/admin/` because `beevia-audit` globs the main folder non-recursively; when the admin board gets a sprint its name will not match `ZOHO_SPRINT_FILTER`, so step 1b will keep skipping until `--sprint` is passed.

---

## 5. Team performance — detail

All figures come from the activity sidecar and git. None comes from the `Last Modified` column, which bulk board operations rewrite without producing per-item audit entries.

**Ayomikun Araoye — backend + admin API.** 14 in review, 3 Done, 1 in progress (4 days), 1 blocked. **52 commits in the trailing 7 days** across `beevia-api` (29), `beevia-db-schema` (16) and `beevia-admin-api` (7), summing the `Ayomikun Araoye` and `Phoenixdadhev` identities and excluding the release bot. Three first submissions to review in that window. No commits today, following the two busiest days this pipeline has recorded — which reads as a normal trough, not a signal.

**David Samuel — mobile.** 9 in review, 1 blocked, zero in progress and zero Done for the sprint. One commit to `main` in 7 days, and `beevia-mobile` has not received one in 7 days. He remains **the only person who has ever moved an item out of REVIEW/QA** — all 22 exits are his, all send-backs — and he moved both card items to BLOCKED.

His row has read "zero delivery" for several editions, and **§6 shows that reading was wrong.** `origin/BVA-I192` is eleven commits and roughly 3,900 changed lines of exactly the work the last edition said was missing, last pushed 28 August. It is invisible to every column in this table, because the board tracks status and the delivery column tracks `main`. Two readings still fit — the branch is waiting on a review nobody is doing, or it is waiting on him — and the board cannot distinguish them. It is the first standup question for that reason.

**Philip Chidera — design.** 8 of the sprint's 11 completions, 5 in review, 1 in progress. His open item (`BVA-I171`, Correct Bank Name Display) is now **6 days old against a 0.9 d median** — by the standing heuristic, probably stuck, and it is the second consecutive edition flagging it. Mildly pointed, given that `BVA-I192` contains the real bank list this item is presumably about.

**Promise Udo — admin dashboard.** No board presence, fourteenth consecutive edition. Three commits in the trailing window, all build configuration, none today.

### 5.1 Weekly submission trend

First-ever submissions into REVIEW/QA, by ISO week: W34 (17–23 Aug) — 17 items; W35 (24–30 Aug) — 10; W36 (31 Aug onward) — **1**. Against an acceptance rate of **zero for the whole sprint**.

Output is falling and acceptance has never been non-zero. That combination is not a developer-throughput problem: the queue has absorbed 49 submissions and released none forward, so the constraint is downstream of everyone in the table above.

### 5.2 Cycle times

Unchanged from 1 Sep, because no item completed a pass today. Method: one measurement per pass, from an item's most recent entry into `In progress` to the next time it reaches `REVIEW/QA`.

| Person | n | Distribution (days) | Median |
|---|---:|---|---:|
| Philip Chidera | 7 | 0, 0, 0, 0.9, 0.9, 8.2, 13.0 | **0.9** |
| David Samuel | 13 | 0, 0, 0, 0.9, 0.9, 0.9, 2.0, 3.1, 4.1, 4.2, 6.0, 8.2, 9.3 | **2.0** |
| Ayomikun Araoye | 10 | 0, 0, 0.9, 0.9, 0.9, 3.9, 4.1, 6.2, 7.1, 13.0 | **2.4** |

Every distribution is bimodal — same-day board hygiene at one end, multi-day builds at the other. The medians are reported because the format asks for them; the distributions are what to look at.

### 5.3 What these figures do not measure

- **They do not see branches.** This is today's demonstration: the mobile lead's delivery column reads 1 commit and zero Done while eleven commits of finished feature work sit on `origin/BVA-I192`. Every "commits" and "Done" figure in this report means *merged to `main`*, and on a team where review is not draining, that gap is where the work accumulates.
- **No estimation points exist on any of the 67 items.** Nothing is normalised for size.
- **Board actions are not evenly attributable.** Per-person figures are keyed to the item's **assignee**, not to whoever clicked. Of the 49 submissions into review, 40 were performed by one person.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **The zero-acceptance rate is a process finding, not a personal one.** It is not attributable to any individual in the table.
- **Review and triage work is invisible.** All 22 send-backs and both blocks are one person's work, and none of it appears in any delivery column.
- **The 7-day commit window slides**, so counts move slightly between editions even when nothing is committed.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction.

---

## 6. The mobile wallet, revisited — the payout flow exists, on a branch

The 1 Sep edition reported that `send_money_bank_transfer.dart` hard-codes a six-bank list, resolves every account to the literal `'John Doe'` after a fake 650 ms delay, and never submits the transfer — all true of `main`, which has not changed in 7 days. It then asked whether anybody had picked up the wiring.

**They had. `origin/BVA-I192`, eleven commits, last pushed 28 August:**

| Endpoint | On `main` | On `BVA-I192` |
|---|---|---|
| `GET /wallets/banks` | not referenced | wired (`WalletService.fetchBanks` → `WalletProvider`) |
| `POST /wallets/resolve-account` | not referenced | wired (`resolveAccount`) |
| `POST /wallets/withdraw` | not referenced | wired (`withdrawExternal`, with PIN step-up) |

The branch rewrites `send_money_bank_transfer.dart` (−730 lines), adds `bank_transfer_amount_screen`, `bank_transfer_review_screen`, a `payment_events` service, a `wallet_bank` model, and provider/service/widget tests. This is not a sketch; it is the feature.

**What this changes, and what it does not.** The diagnosis changes: "the client team has not built the payout flow" was wrong, and "the payout flow has been finished and unmerged for five days" is the accurate statement. The score does not change — the rubric scores merged, reachable build evidence, and a branch is not that. Capability 6 stays at 0.70. But it is 0.70 with a merge in front of it rather than 0.70 with a build in front of it, which is a materially better position than the last edition described.

**The add-money side is genuinely not fixed.** `accountNumber = '0099873456'` / `accountName = 'Chatbank_John Doe'` are still compiled-in defaults, on **both** `main` and `BVA-I192`, in `add_money_screen.dart` and again in `onboarding/screens/wallet/wallet_details.dart`. `GET /wallets/payin-details` is live and is called — but only from the onboarding KYC provider, never from either of these screens. A user reaching add-money on `main` is still shown a plausible account number and invited to copy or share it. Whether that risk is real depends on distribution, which this pipeline cannot see; it should be a deliberate decision rather than an artifact.

Domains with zero references anywhere in `beevia-mobile/lib` on `main`: `/cards` (13 live operations), `/topups` (3), `/translate` (1) — the last despite `translate_chat_screen.dart` existing.

---

## 7. Risks

1. **The spec drift found today was four weeks old and the automated check cannot see its class** (§3.1). Five contract facts wrong through nineteen clean audits. Until the admin service publishes its generated OpenAPI document, this will recur.
2. **A finished mobile feature has been unmerged for five days** (§6), invisible to every delivery metric this report produces.
3. **No sprint 08-02 exists**, five days after 08-01 closed. 28 review items, 2 in progress and 2 blocked have no destination.
4. **The forward path out of REVIEW/QA has never been exercised** — 0 of 28 accepted in 23 days, across 49 submissions. A demonstrated property of the process, not a backlog.
5. **Two card items are blocked with no recorded reason**, unmoved for two days, while a plausible fix for both merged on 1 September.
6. **Failed provisioning is invisible to the user** (§2.2). Three silent-200s on the same seam in two days; guards keep landing inside a job whose outcome no endpoint reports.
7. **The same silent-200 bug fixed on `/upgrade/profile` is still live on `/kyc/profile`** — second consecutive edition, and a five-line change already written on the other ladder.
8. **A hard-coded account number reaches a money screen on `main`** (§6), and the branch that fixes the payout flow does not fix this one.
9. **The account-deletion designs have lost their premise** (§0.1) — larger than scoped, and the compliance KPI is unrecorded rather than merely unsurfaced.
10. **A large money-handling surface remains unverified** — cards, top-ups, payouts and bank transfers all sit in the review queue.
11. **The admin dashboard's money modules remain mock-backed** against four endpoints that have not been built.
12. **0/67 estimation points**, so any carry-over conversation still has no size data.

---

## 8. Previous recommendations — where they stand

| Recommendation from 1 Sep | Status on 2 Sep |
|---|---|
| Create 08-02, or say explicitly the project is not running sprints | **Not done.** Still three sprints: `08-01`, `0702`, `0701`. |
| Unblock or annotate the two card items today | **Not done.** Both unmoved for two days; still no recorded reason. |
| Apply the BVN-ordering guard to `POST /kyc/profile` | **Not done.** Re-checked in code today; still returns 200 on an unverified BVN. |
| Run one live provisioning and one card issuance end to end | **No evidence either happened.** The provisioning work that merged is more repair of the same path. |
| Decide what the mobile bank-transfer and add-money screens are | **Answered in part, by evidence rather than by decision** — the bank-transfer wiring exists on `BVA-I192` (§6). The add-money screen is unchanged and the decision on it is still open. |
| Exercise the accept path once, on anything | **Not done.** Zero forward exits, 23 days. |

One of six partially addressed, and that one by discovery rather than by anyone acting. The other five are the same five.

---

## 9. What I would do this week

1. **Merge `BVA-I192` or say why not.** It is the highest-value single action available: a finished, tested payout feature, five days idle, against three live endpoints. If it is waiting on review, that is the same bottleneck as §1.3 and it is now costing shipped features, not just board hygiene. If it is waiting on something else, that should be written down.
2. **Publish `beevia-admin-api`'s generated OpenAPI document and point the audit at it.** `main.ts` already builds one. This is the fix for §3.1 as a class rather than as five corrections, and it would have caught all five on 7 August. Small, one-time, and it converts this report's most expensive manual step into a diff.
3. **Create 08-02, or state that the project is not running sprints.** Fifth consecutive edition. Five days of drift is a decision made by default.
4. **Unblock or annotate the two card items.** Third consecutive edition asking. A third silent block/unblock cycle teaches everyone that BLOCKED means nothing.
5. **Give failed provisioning somewhere to appear** (§2.2) — a `failed` state and reason on `GET /upgrade/status`. This is worth more than the next individual guard, because it turns a whole class of silent failure into something a client can render.
6. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Unchanged from 1 Sep; five lines, already written.
7. **Exercise the accept path once, on anything.** Unchanged from the last four editions and still the single most informative thing anyone could do.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (67 items, cut-off 08:02 MDT) → admin board (exit 3, no sprints, 14th edition) → fast-forward sync (**9 commits pulled across 2 repos; all five repos clean, none dirty, none diverged, none switched branch**) → deterministic audit (exit 1: one route drift + board findings) → manual contract review of `beevia-admin-api` and `beevia-api`, which produced §3.1, §3.2 and §0.1 → read-only inspection of `origin/BVA-I192`, which produced §6 → this report.

**Degraded inputs.** The `Epic` column is blank across all 67 items — the OAuth refresh token lacks `ZohoSprints.epic.READ`. This is a known scope gap, not "no epic assigned". `Comments` bodies are unavailable from the API. The admin board produced no export because the project has no sprints (expected, not a failure). No other input degraded; no step was skipped or run against stale code.

**Window.** 1 Sep 14:00 UTC → 2 Sep 15:00 UTC. `actiontime` values are UTC; git timestamps normalised to UTC where quoted; CSV header times are the exporting machine's local MDT.

**Sources.** Board: `beevia-sprint-board-2026-09-02.csv` (67 rows, 43 leaves), `beevia-activity-2026-09-02.json`. Admin board: none. Code: five repos at `origin/main`, plus read-only inspection of `origin/BVA-I192` on `beevia-mobile`. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (**30**, +1), `openapi.admin.proposed.yaml` (**23**, −1) — all validated, no drift, no markers, no broken refs.

**A note on who appears here.** Only people whose work is tracked have rows. Board-administration actions performed by a non-contributor are reported as transitions without attribution, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈58% (estimate; 57.8, from 57.5)

**Target 2026-09-01 (provisional) · the target date passed yesterday.** On merged build evidence the product is roughly 58% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points have not been started at all. The date has arrived and is not met; this report has said so at every edition since the estimate began.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live since 10 July; `translate_chat_screen.dart` exists but `/translate` has zero references in `lib` — the screen is not wired. Batch/languages/preference still proposed |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full onboarding flow wired in the client. Further hardened today (existing-customer/account connect). Ceiling unchanged: the silent-200 remains live on `/kyc/profile`, and §2.2 adds a *new* silent failure at the enqueue boundary — hardening the path without making its failures visible does not raise the score |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | **Not moved, but the reason changed.** Wallet home and history wired to `GET /wallets` and `/wallets/transactions`; bank payout and add-money still make zero network calls **on `main`**. §6 finds the payout flow fully wired on unmerged `origin/BVA-I192` — the rubric does not score branches, so this holds at 0.70 pending a merge. Add-money is unfixed on both. Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | P2P send wired end to end: `send_money_amount_screen` → `WalletProvider.transferMoney` → `POST /payments/transfer`, with `/auth/step-up`. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; `PaymentService.activeNgn()` still present |
| 9 | Virtual cards | 10 | 0.45 | 13 operations live; the two broken Anchor calls fixed 1 Sep. Not moved: restoring intended behaviour is not new capability, the client still has zero `/cards` references, there is no issuer webhook, and both card board items remain BLOCKED |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | **0.55** ↑ | **Moved +0.05.** `GET /admin/activity` **merged** — admin API 29 → 30 operations, and a fourth of eight dashboard modules opened. Held to +0.05 because the feed covers only 3 of 11 modules (no money, KYC or chat events), the client dashboard still wires 3 of 8 modules, and the four Module 5 money endpoints the mocks await are unbuilt. §3.1's spec corrections improve what a dashboard author can rely on but add no surface |
| | **Weighted total** | **100** | | **57.8 → ≈58%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches.

**On the one movement.** Capability 11 moves because something that did not exist on `main` yesterday exists on it today — the standing rule for raising a score, and the merge names it. Capability 6 is the interesting non-movement: the evidence about the code changed materially (the payout flow is written, tested and reviewable) while the evidence about the *product* did not (nothing new is reachable). Holding it flat is the rule working as intended; §6 exists so the reader is not misled by a number that has stopped short of the truth in a specific, nameable way.

**What this report cannot tell you:**
- **Why `BVA-I192` has not merged.** Five days, no review activity anywhere, and the board has no item state that would show it.
- **What blocked the two card items.** No reason recorded for any of the five block/unblock transitions.
- **What the 28 review items are worth.** Twenty-three days of zero acceptances means nobody has recorded an opinion.
- **How many other contracts are wrong.** §3.1 found five in one service by reading it. The consumer API has not had the same treatment, and 131 operations is a lot of surface to have inferred from decorators.
- **Whether the provisioning fixes work.** They ship with tests; none has been demonstrated against live Anchor. Testing is out of scope for scoring.
- **Whether the add-money placeholder can reach a real user** — that depends on distribution, which this pipeline cannot see.
- **Why there is no 08-02** — deliberate pause, unheld planning session, or oversight.
- **Anything about the Admin Dashboard board** beyond its existence — fourteenth edition with no sprint.
- **Velocity or scope-fit for any future sprint** — the board remains at 0/67 estimated.
