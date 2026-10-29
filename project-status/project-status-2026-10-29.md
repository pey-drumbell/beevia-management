# Beevia — Project Status

**As of 2026-10-29** · Sprint **1002** (21 Oct → 5 Nov, day 9 of 16): **63 items, 44 leaves: 12 To do · 13 In progress · 16 REVIEW/QA · 0 BLOCKED · 3 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-29.csv` + `beevia-activity-2026-10-29.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-29.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 28 Oct file in the same folder; the 27 Oct scratch export of **0902** and the 19 Oct export of **0901** (both closed, not re-exported) for cycle times. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 28 Oct 14:05 UTC → 29 Oct 14:03 UTC, 1.0 day (Wed → Thu).**

---

## Quick overview

> **Transaction disputes shipped on the server two hours after the last edition closed. A schema, three app routes and a three-route admin queue were merged between 15:49 and 16:21 UTC on 28 Oct, and all six are documented today (149 consumer and 63 admin operations). Users can file a dispute in production now, but no admin can answer one: the new `disputes` permission, like yesterday's `help_center`, is granted to no role. This morning the mobile branch caught up. `BVA-I353` now calls the real FAQ and dispute routes, and every call matches the server except one reason code. The card-route mismatches the 28 Oct edition blamed on the client are partly a design question. The sprint's own "Verify it's you" story, started today, specifies the model the client used.** On the board, the Activity verification checklist `I392` was closed with all 63 of its boxes unticked, and acceptance by a reviewer is still zero.

| Metric | 28 Oct | 29 Oct | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 15 / 14 / 14 / 0 / 1 | **12 / 13 / 16 / 0 / 3** | 2 dispute leaves → REVIEW/QA; `I360`, `I392` → Done; 3 verification leaves → In progress |
| Transitions into REVIEW/QA, last 7 days (leaves) | 14 | **16** | 7 by the leaf's owner (all Ayomikun), **9 moved by Ayomikun on David's and Philip's items**, 0 by board administration |
| Owners' last submission of their *own* leaf | 28 Oct 13:02 UTC (Ayomikun, `I338`) | **28 Oct 16:22 UTC** (Ayomikun, `I341`) | David's last own submission is still 14 Oct, **14.9 days** ago |
| Items accepted by a reviewer | 0 | **0** | all 3 Done leaves were closed by their own owner, none through REVIEW/QA |
| 1002 REVIEW/QA leaves with matching **merged** code | 3 of 14 | **4 of 16** | +`I341` (disputes, #87). `I340` went to review 18 h before its client code was pushed |
| Routes in code but not in the spec (consumer / admin) | 5 / 11 → 0 | **3 / 3 → 0** | `/disputes` and `/admin/disputes` documented today (§3.4) |
| API surface (consumer / admin) | 146 / 60 | **149 / 63** | |
| Proposed operations (consumer / admin) | 38 / 18 | **37 / 18** | `POST /payments/{id}/dispute` shipped as `POST /disputes` and was moved |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | 3 merges and schema release v0.0.45 went out that way |
| `beevia-mobile` days since a commit on `main` | 6.2 | **7.2** | `BVA-I353` +1 commit today: 6 commits, 76 files, +9,670, no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 / 0.0 / 0.1 | **0.9 / 0.9 / 0.9** | |
| `beevia-admin` days since a commit | 35.9 | **36.9** | |
| Admin board: open sprint / days since any activity | none / 44.0 | **none / 45.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: disputes are not a rubric line, and the client work is on an unmerged branch (appendix) |

**Two corrections to 28 Oct.**

1. **The card "wrong credential" rows were judged against the server alone.** That edition said `BVA-I353`'s reveal and unfreeze calls "send the wrong credential". It told the client to use "the card-PIN sheet", because "the server deliberately gates them with the card's own PIN". Sprint 1002 has carried `BVA-I378` *"Verify It's You" Authentication* since 22 Oct. It specifies one reusable PIN-or-biometrics sheet, enforced by the backend, that returns "a short-lived authorization that sensitive card endpoints require". Reveal, card details, delete, update limit and unfreeze need it, and freeze does not. That is the account-level token model the client already uses, not the server's per-card PIN. Its backend task `I381` went to In progress today. **What stands:** against today's server, those calls fail. Statements (`POST /statements`) and `GET /wallets/limits` are client errors whatever the model. But the fix for reveal, unfreeze and terminate is a decision about which model `I381` builds (§2.3), not a client correction.
2. **"Disputes are being built from both ends with no shared contract" did not last the afternoon.** The server shipped its own contract at 16:05 UTC (#87, with Postman examples). The client followed it the next morning and matches it in every path, body field and response key but one (§2.2). The contract came from the code, not a design document, but it is now one contract, documented in `openapi.yaml`.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (7 To do, 4 In progress, 7 REVIEW/QA) · `I392` shared · 0901-admin: 1 In progress | **7 own** (+9 moves on teammates' items) | 0.99 d (n=20) | `I332` (**7.2 d**), `I347` (2.9 d), `I344` (1.0 d), `I381` (0.1 d) · `BVA-I8` on 0901-admin (**45.0 d**) | **20** (12 `beevia-api`, 3 `beevia-admin-api`, 5 `beevia-db-schema`) | Shipped disputes on three repos in 38 minutes. **Grant `disputes` and `help_center` to a role**. `I350` and `I352` are still To do, although #24 and #23 delivered most of them |
| David Samuel | mobile | **1002: 16** (3 To do, 7 In progress, 6 REVIEW/QA) · `I392` shared | 6 (**0 own**, 6 moved by Ayomikun) | 0.99 d (n=40) | 7: `I331`, `I354` (**7.2 d**), `I346`, `I383`, `I386` (2.9 d), `I343` (1.0 d), `I380` (0.1 d) | **0 on `main`** · **6 on `BVA-I353`** | Wired FAQ and disputes to the real API this morning. **One value is wrong**: `didnt_make_transaction` should be `not_my_transaction`. Branch has no PR |
| Philip Chidera | design | **1002: 7** (1 To do, 1 In progress, 3 REVIEW/QA, 2 Done) · `I392` shared (Done) | 3 (0 own, 3 moved by Ayomikun) | 0.94 d (n=4) | `I379` (0.1 d) | n/a | Closed `I392` and `I360`. **`I392`'s 63 checks are all still unticked** (§1.2) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**45.0 d**) | **0** | `beevia-admin` **36.9 days** without a commit. Two admin APIs (FAQ content, dispute queue) now have no screen |

**The three questions for standup:** (1) **Who grants `disputes` and `help_center`, and when?** A user can report a failed or double-charged payment today, and no admin account can read the report through the API. (2) **Which model does `I381` build: the card's own PIN, or an account PIN or biometric token?** The server, the board and the client branch each assume a different one. `I380` (the sheet) and `I381` (the endpoint) both started today. (3) **What did the `I392` checklist find?** It went to Done at 05:03 UTC with every box unticked and no comment. If the checks were done elsewhere, record them on the item. If they were not, it should not be Done.

**The three things worth knowing:**

1. **Disputes exist end to end on the server, and no one can answer them yet.** `beevia-db-schema` #26 (v0.0.45, 15:49 UTC) adds `transaction_disputes` and `dispute_attachments`, with one open report per transaction per user enforced by a partial unique index. `beevia-api` #87 (16:05 UTC) adds `POST /disputes`, `GET /disputes` and `GET /disputes/{id}`. The server resolves the receipt reference against the caller's own transactions and builds the snapshot itself, so a user cannot claim a different amount. Screenshots must be on Beevia's storage origin. `beevia-admin-api` #24 (16:21 UTC) adds the queue, oldest first, with a written answer required to close and no money movement. 22 integration tests run against real Postgres. **The gaps** (`suggestions.md` §4.11): no role holds `disputes`, card spending cannot be disputed (the story says it must be), nothing tells the user when an answer arrives, the transaction type `I341` asked for is not stored, and two admins can claim or answer the same dispute at once.

2. **The mobile branch now talks to the real support API, and the card screens wait on a decision.** Commit `a444ec9` (29 Oct 10:18 UTC) replaces the FAQ and dispute placeholders with real calls to `/help/*`, `/disputes` and `POST /upload/image`. All nine match the server, apart from the "I didn't make this transaction" reason, which returns `400` because the client sends `didnt_make_transaction` instead of `not_my_transaction`. That is the reason a fraud victim would pick. Support chat is still placeholder (5 × `TODO(support-api)`). The five card and statement mismatches from 28 Oct are unchanged. Two of them are client errors. The other three depend on `I381` (correction 1 above).

3. **The first acceptance checklist closed without a tick.** `I392` lists 63 `[Design]`, `[Mobile]` and `[Backend]` checks for the Activity screen. It went to Done at 05:03 UTC with no description edit, comment or attachment since it was created, and every box still reads ☐. `I360` (a design item) went from In progress to Done without passing through review. Both were closed by their own owner. On the review column, 4 of 16 leaves match merged code. `I340` (Report an issue screen) was moved there at 16:22 UTC yesterday, 18 hours before its wiring was pushed. **Acceptance by a reviewer is still zero**, and the bottleneck is still the review step, not the developers.

**If you read nothing else:** the server built disputes carefully, and the app's dispute screens already call it correctly bar one value. Two permission grants and one decision about card verification are what stand between this work and users.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 was not re-exported; it has had no entry since its 21 Oct sweep. The 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01.

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged in count.

| Block | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Help & Support (`I330`–`I352`) | 15 | 2 | 7 | 6 | 0 |
| Wallet & card (`I353`–`I391`) | 28 | 10 | 6 | 10 | 2 |
| Activity checklist (`I392`) | 1 | 0 | 0 | 0 | 1 |
| **Total** | **44** | **12** | **13** | **16** | **3** |

**Movement in the window (leaves): 7 status transitions.**

| Time (UTC) | Leaf | Owner | Move | By | Code |
|---|---|---|---|---|---|
| 28 Oct 16:22 | `I341` Dispute creation & attachment upload | Ayomikun | In progress → REVIEW/QA (0.1 d) | owner | ✅ `beevia-api` #87, merged 16:05 |
| 28 Oct 16:22 | `I340` Build Report an Issue screen | David | In progress → REVIEW/QA (0.1 d) | Ayomikun | ◐ wired on `BVA-I353` at **10:18 the next day**, one reason value wrong |
| 29 Oct 05:03 | `I392` Activity verification checklist | all three | In progress → **Done** | Philip | review artefact; **0 of 63 boxes ticked** |
| 29 Oct 11:31 | `I360` Highest-tier state & upgrade entry | Philip | In progress → **Done** (2.8 d) | owner | design; skipped REVIEW/QA |
| 29 Oct 11:33 | `I379` Verification edge states | Philip | To do → In progress | owner | design |
| 29 Oct 11:33 | `I380` Build verification sheet | David | To do → In progress | Philip | — |
| 29 Oct 11:33 | `I381` PIN & biometric verification endpoint | Ayomikun | To do → In progress | Philip | no server branch |

The parent `I339` (Report an Issue) went to REVIEW/QA with its two leaves, and `I378` ("Verify It's You") went to In progress with its three. No comment, reopen or block was recorded in the window. Board administration made no move.

**`I392` in detail.** It was created by board administration on 27 Oct with a Figma link and 63 checks. Examples: "four filter chips (All, Chats, Calls, Payments)", "sorted newest activity first", "one endpoint returns the combined, paginated feed". Philip started it on 28 Oct at 13:28 UTC and completed it 15.6 hours later. Between those two moves the sidecar records no other action, and the description still shows 63 × ☐, 0 ticked. The checks may have been done in Figma or in conversation, and the board cannot see either. But a checklist closed with no ticks cannot show anyone else what passed. That makes it a process question for standup, not a finding against anyone.

---

## 2. Sprint 1002: what is in review, and whether the code exists

### 2.1 The sixteen REVIEW/QA leaves, checked against the code

| Leaf | Owner | Code on `main` | Code on a branch |
|---|---|---|---|
| `I366` Statement generation & email | Ayomikun | ✅ #84 (27 Oct) | — |
| `I335` FAQ content API | Ayomikun | ✅ #86 (28 Oct) | — |
| `I338` Article feedback endpoint | Ayomikun | ✅ #86 (28 Oct) | — |
| `I341` Dispute creation & attachment upload | Ayomikun | ✅ **#87 (28 Oct)**; no transaction type stored, card spending excluded | — |
| `I370` Card summary & freeze endpoints | Ayomikun | existing since 27 Aug, no change | — |
| `I377` Card termination endpoint | Ayomikun | existing since 27 Aug, no change | — |
| `I358` Wallet account details endpoint | Ayomikun | no change identifiable | — |
| `I334` FAQ screens | David | ❌ | ✅ **now calls `/help/*`** (`a444ec9`) |
| `I337` FAQ yes/no feedback | David | ❌ | ✅ **now posts `{helpful}`** (`a444ec9`) |
| `I340` Report an Issue screen | David | ❌ | ◐ **now posts `/disputes`**; `didnt_make_transaction` → `400` |
| `I365` Statement screen | David | ❌ | ◐ calls `POST /wallets/statements`, which does not exist |
| `I369` Manage card screen | David | ❌ | ◐ freeze ✅; reveal and unfreeze send a step-up token, and the server wants the card PIN (§2.3) |
| `I376` Delete card confirmation | David | ❌ | ◐ calls `DELETE /cards/{id}`; the server has `POST /cards/{id}/terminate` (§2.3) |
| `I364`, `I368`, `I375` | Philip | design | not visible in git |

**Four of sixteen match merged code**, all backend. Two more match endpoints that already existed. Two of the six mobile items now work against the real API on the branch, and none is merged.

### 2.2 `origin/BVA-I353`: today's commit

6 commits by `Davidtariq96`, 23–29 Oct, 76 files, +9,670/−104 against `main`. **No PR.** Today's `a444ec9` *dispute resolution* (26 files, +1,937/−608):

| Client call | Server | Result |
|---|---|---|
| `GET /help/categories`, `/help/categories/{slug}`, `/help/articles/{slug}` | same | ✅ |
| `GET /help/search?q=` | same (`q`, 2–120 chars) | ✅ |
| `POST /help/articles/{slug}/feedback` `{helpful}` | same | ✅ |
| `GET /disputes`, `GET /disputes/{id}` | same; reads both camelCase and snake_case keys | ✅ |
| `POST /upload/image` (multipart `file`), then the returned `url` | same; storage origin checked | ✅ |
| `POST /disputes` `{transactionReference, reason, details, attachments[{url, filename, sizeBytes}]}` | same | ✅ for 6 of 7 reasons |
| reason "I didn't make this transaction" = `didnt_make_transaction` | enum value `not_my_transaction` | **400** |

The client's own comment says only `money_didnt_arrive` was confirmed against Postman. The contract-test allowlist gains eight entries, with a note that the help routes are "not yet in openapi.yaml". They have been in it since 28 Oct. The vendored copy (`suggestions.md` §5.10) is what lacks them. After submit, the app opens the dispute as a read-only "thread" built from the report and the answer. Replying in a dispute (`I343`) needs messaging endpoints that do not exist (`I344`).

### 2.3 Card verification: three models

| | Reveal / unfreeze / terminate authorised by | Biometrics |
|---|---|---|
| **Server** (`card.controller.ts`, since 27 Aug) | The **card's own 4-digit PIN** in the body. Account step-up only for issuing a card and for revealing a forgotten card PIN | no |
| **Board** (`I378`, on 1002 since 22 Oct; `I381` started today) | **Account PIN or device biometrics** → "a short-lived authorization that sensitive card endpoints require". Freeze is exempt | yes, "biometric-backed", enforced by the backend |
| **Client** (`BVA-I353`) | `X-Step-Up-Token` from `/auth/step-up` | the sheet offers it; the server cannot verify it (`suggestions.md` §5.11) |

The client matches the board's intent but not the server. If `I381` builds what `I378` says, the server's card routes change and most of the client's card calls become correct. If the per-card PIN stays, the client changes. **Decide before `I380` and `I381` go further** (`suggestions.md` §5.15).

### 2.4 In progress

| Leaf | Owner | Age | Note |
|---|---|---:|---|
| `I331` Help & Support home | David | 7.2 d | on the branch, FAQ part now wired |
| `I354` Wallet "more options" sheet | David | 7.2 d | `wallet_options_widgets.dart` on the branch |
| `I346` Support chat screen | David | 2.9 d | placeholder; no server surface |
| `I383` Card details screen | David | 2.9 d | on the branch |
| `I386` Card limits screen | David | 2.9 d | calls the unbuilt `GET /wallets/limits` |
| `I343` Dispute history & thread | David | 1.0 d | list wired today; thread replies need `I344` |
| `I380` Verification sheet | David | 0.1 d | — |
| `I332` Open dispute count endpoint | Ayomikun | **7.2 d** | not in #87. `GET /disputes` returns everything, so the client could count, but there is no count route |
| `I347` Support conversation endpoints | Ayomikun | 2.9 d | no server branch |
| `I344` Dispute listing, detail & messaging | Ayomikun | 1.0 d | listing and detail shipped in #87; messaging not |
| `I381` PIN & biometric verification endpoint | Ayomikun | 0.1 d | see §2.3 |
| `I348` Triage flow configuration | **Unassigned** | 2.9 d | — |
| `I379` Verification edge states | Philip | 0.1 d | design |

---

## 3. Code, API surface and spec drift

**Audit: six routes in code and not in the spec, now zero.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-29`), the first run found three consumer routes (`/disputes`) and three admin routes (`/admin/disputes`) undocumented. After this cycle's edits it is clean: 149/149 consumer, 63/63 admin, proposed 37/18, spec health clean, no `x-beevia-*`. The in-repo audit reports phantom lines from the three `diverged` working trees (18 consumer + 29 admin "in spec, not in code"). It also confirms that `api-rfc.md` §3 sums to the new totals. The phantom lines were not acted on.

**Three `main` branches moved, all on 28 Oct after the last edition's cut-off.**

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` | `b49e1be` → `2fbf657` | **#26 transaction disputes** (merged 15:49 UTC) → **v0.0.45** (15:50): migration `0041`, `dispute_reason` (7 values) and `dispute_status` enums, `transaction_disputes` (reference + jsonb snapshot + optional ledger/payment FKs, reviewer `set null`), `dispute_attachments`, partial unique index `disputes_one_open_per_txn_uq`; `admin_module` gains `disputes`. 1 commit, `Phoenixdadhev` |
| `beevia-api` | `1eba51c` → `e2bc950` | **#87 disputes** (16:05 UTC): `src/disputes/` (controller, service, DTO, 10 integration tests), Postman folder, db-schema 0.0.45. 1 commit, `Phoenixdadhev` |
| `beevia-admin-api` | `d8ed60e` → `b8b6a13` | **#24 dispute queue** (16:21 UTC): `src/disputes/`, 12 tests, DTOs in `admin.dto.ts`. 1 commit, `Phoenixdadhev` |

`beevia-mobile` `main` (`ccb4f63`, 22 Oct) and `beevia-admin` (`0b41e35`, 22 Sep) did not move. **No PR is open on any backend repo.** Mobile: `BVA-I353` gained `a444ec9` (§2.2). The highest mobile PR is still Dependabot #53, and #45, #47, #50 and #53 are still open.

### 3.1 Disputes: what shipped

Full detail in `api-rfc.md` §5.18 and `admin-api-rfc.md` §3.16.

| | App (`beevia-api`) | Admin (`beevia-admin-api`) |
|---|---|---|
| Routes | `POST /disputes`, `GET /disputes`, `GET /disputes/{id}` | `GET /admin/disputes` (open queue by default, oldest first), `GET /admin/disputes/{id}`, `PATCH /admin/disputes/{id}` (claim or answer) |
| Subject | Receipt reference, resolved server-side against the caller's ledger, then peer payments | Snapshot as the user saw it, plus reporter name and phone |
| Rules | One open report per transaction; `409` returns the existing id; attachments on own storage only; another user's report is `404` | Answer requires a note; `resolved`/`rejected` are final; **moves no money** |
| Who can call | Any signed-in user | **`disputes` permission, granted to no role** |
| Tests | 10 against real Postgres | 12 against real Postgres |
| Not covered | Card spending; messaging; open count; notifications | Assignment; agent replies (`I350`); a dashboard screen (`I349`) |

`POST /disputes` is the built form of the proposed `POST /payments/{id}/dispute`, keyed by reference instead of payment id. It was moved out of `openapi.proposed.yaml`. `/support/tickets` stays proposed for general support. It also gives the PRD's "90 percent of issues resolved within 72 hours" KPI (§7.4) its first data, with one caveat: the queue's `age_hours` ignores `reviewed_at` (`suggestions.md` §4.11.6).

### 3.2 Mobile

`main` is unchanged since PR #52, with no conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`. **`call.ended` is still unhandled** on `main` and on `BVA-I353`; the only match is a doc comment in `call_provider.dart`. The biometric step-up (`wallet_service.dart:78`) is unchanged.

### 3.3 The standing checks

- **Pipelines:** no workflow change on any backend `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`". db-schema released v0.0.45 1 min after #26 merged and 15 min before #87, which uses it.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` are unchanged. `22P02` is still unmapped, and the three new `/{id}` dispute routes inherit it. `messages.ref_id` still has no index. FAQ search still has no `en-US` fallback (`src/help` unchanged since #86).

### 3.4 Document changes this cycle

- **`openapi.yaml`** (146 → 149): `createDispute`, `listDisputes`, `getDispute` under a new `Disputes` tag, with schemas `DisputeReason`, `DisputeStatus`, `DisputeAttachmentInput`, `CreateDisputeRequest`, `DisputedTransaction` and `Dispute`. The `Support` tag now describes only support chat and escalation.
- **`openapi.admin.yaml`** (60 → 63): `listDisputesAdmin`, `getDisputeAdmin`, `resolveDispute` under `Admin Disputes`, plus the `DisputeId` parameter and schemas `AdminDisputeStatus`, `AdminDisputeReason`, `QueuedDispute`, `DisputeDetail` and `ResolveDisputeRequest`. `disputes` was added to `AdminModule`, the activity-event enum and the module list in `info` (12 → 13). The operations document the anonymous claim, the unconditional update and `age_hours`.
- **`openapi.proposed.yaml`** (38 → 37): `disputePayment` and its orphaned `CreateDisputeRequest` were removed. The `createSupportTicket` text now points to the shipped route.
- **`api-rfc.md`**: header and §3 totals (149 / 34 net-new / 37), a Disputes row, Support row 4 → 3, §6.8 rows, new §5.18, §7.2 (5 → 4) and Phase E.
- **`admin-api-rfc.md`**: totals (63), Module 5 row (6 → 9), module count, new §3.16.
- **`suggestions.md`**: new §4.11 (dispute gaps) and §5.15 (`BVA-I353`'s new calls and the three verification models).

---

## 4. Risks

- **Disputes can be filed and cannot be answered.** `POST /disputes` is live (deploy on push). Until a role holds `disputes`, every complaint about money waits with no reader except direct database access. The PRD's 72-hour KPI starts counting on each one.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content.
- **A fraud report fails.** "I didn't make this transaction" returns `400` from the branch's dispute sheet. It is one line to fix, and it should be fixed before merge.
- **Card spending, probably the most disputed category, has no dispute path.** The schema allows a reference with no local row, so it can be added.
- **Three verification models for card actions.** Building `I380`/`I381` before choosing one means rework on at least one side.
- **The review column still mixes merged work with branch work**, and the first checklist closed unticked. If 1002 is swept the way 0902 was, the mis-wired card screens will be recorded as delivered.
- **Every backend repo still deploys or migrates production on push without a test gate.** Yesterday that was three merges and a schema release. Each carried real-Postgres tests that CI does not gate on.
- **The admin workstream:** 36.9 days without a `beevia-admin` commit and 45.0 days without admin-board activity. Two new admin APIs (FAQ content, dispute queue) have no screen, and both Stories (`I349`, `I351`) are unassigned.
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); blocks do not reach payments (§4.9); FAQ search fallback (§4.10); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points. Disputes close a real PRD commitment ("Beevia handles escalation", §8.3, and the §7.4 KPI), but escalation is not a rubric capability. The PRD's "never tell the user to contact the partner" still needs support chat (`/support/tickets`, `I347`) for anything that is not one transaction.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 22 Oct 14:03 → 29 Oct 14:03 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Cycle times use 0901, 0902 and 1002.

### 6.1 Ayomikun Araoye: backend + admin API

**20 commits in 7 days**: 12 in `beevia-api`, 5 in `beevia-db-schema` and 3 in `beevia-admin-api`. Disputes went from first commit to the last merge in 38 minutes across three repos (15:43 → 16:21 UTC). Each commit explains a design choice and names the guard its tests protect, for example "reverting four guards fails four of them". **7 own submissions** (`I377`, `I370`, `I366`, `I358`, `I335`, `I338`, `I341`), and 9 moves of David's and Philip's items. Median cycle **0.99 d (n=20)**. WIP: `I332` (7.2 d, past their median; #87 did not include it), `I347` (2.9 d), `I344` (1.0 d, half delivered), and `I381` (started today, waiting on the §2.3 decision). `BVA-I8` has been In progress on the closed admin board for 45.0 days. `I350` and `I352` are To do, although #24 and #23 delivered most of each. That is a board-hygiene note, not an output one.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct and has aged out) and **6 on `origin/BVA-I353`**. Today's commit wired the FAQ and dispute screens to the server. It was written against Postman because the vendored spec lacks those routes, and it got all but one value right. **Zero own submissions**: the last was `I286` on 14 Oct, **14.9 days** ago. Their six 7-day "submissions" were moved by Ayomikun. Median cycle **0.99 d (n=40)**. WIP: **7 items**, still the most on the board. `I331` and `I354` are at 7.2 d, both with visible branch work. Seven WIP items and a 76-file branch with no PR is a merge-risk question, not an output one: the longer the branch lives, the larger the eventual review.

### 6.3 Philip Chidera: design

No submissions of their own. Their three REVIEW/QA items were moved by Ayomikun on 23 and 27 Oct. Today they closed `I360` (2.8 d in progress, not through review) and `I392`, and started `I379` and the verification block. The `I392` question in §1.2 is about how the board records review, not about Philip's work: the checklist was written by board administration, and no one has defined who ticks it. Design files are not in git, so the board is the only record.

### 6.4 Promise Udo: admin dashboard

**No commit in the window.** The last was `0b41e35` on 22 Sep, **36.9 days** ago. The admin board has had no activity for 45.0 days, and `BVA-I9` has been In progress for all of it. The backend now offers the dashboard two new modules to build on: FAQ content (`I351`) and the dispute queue (`I349`, the Support Inbox). Both Stories are unassigned. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible. Still, the dispute queue is the first admin feature with users waiting on it, which makes the question more pressing.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (from Mon 26 Oct, to 14:03 UTC Thu) | — | — | **10** | 5 | 5 | 0 |

**Acceptance is still zero.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted by someone other than its submitter since `BVA-I268` on 16 Sep. 1002's three Done leaves were each closed by their own owner. W44 is already the busiest 1002 week for submissions, and nothing has left the review column. The bottleneck is the review step.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Seven WIP items for David and four for Ayomikun are not comparable loads.
- **Unpushed work.** The 27 Oct edition missed a day of card screens for this reason. Today's dispute wiring was visible because it was pushed the same morning.
- **Who moved an item is not whether it is done.** It is not whether it was verified either, as `I392` shows.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The route checks in §2.2 come from reading both sides' code, not from running the app.

---

## 7. Previous recommendations: where they stand

| Recommendation from 28 Oct | Status on 29 Oct |
|---|---|
| **1. Grant `help_center`** | ❌ **Not visible.** No migration or seed. The same gap now applies to `disputes` |
| **2. Correct `BVA-I353` before it merges** | ◐ **Partly.** New FAQ and dispute calls are correct bar one value. The statement and limits calls are unchanged. The card rows are **revised** (correction 1): decide `I381`'s model first |
| **3. Stop vendoring the client spec** | ❌ **Not done.** `a444ec9` added eight more allowlist entries |
| **4. Wire the FAQ screens to `/help/*`** | ✅ **Done on the branch** (`a444ec9`), not merged |
| **5. Add the `en-US` fallback to FAQ search** | ❌ **Not done** |
| **6. Agree a dispute contract before the four dispute leaves go further** | ✅ **Overtaken.** The server shipped the contract that afternoon and the client followed it. It is now in `openapi.yaml`. `I348` (triage) is still unassigned |
| **7. Use `I392` as the pattern for review** | ❌ **No.** It closed with 0 of 63 checks ticked |
| **8. Handle `call.ended` on the client** | ❌ **Not done** |
| **9. Make REVIEW/QA mean merged** | ❌ **No.** `I340` went in 18 h before its code. Nothing was moved back. `I352` is still To do |
| **10. Give the admin dashboard a home** | ❌ **No**, and a second unassigned admin Story (`I349`) now has a live API |
| **11. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done** |
| **12. Generate `openapi.yaml` from the app and diff it in CI** | ❌ **Not done.** Six more routes reached production undocumented |
| **13. Set `ZOHO_SPRINT_FILTER` to `1002`** | ❌ **Not done** |
| **14. Carried items** | ❌ **None moved** |

**Two done (one on a branch, one overtaken), one partly done.** The work that moved was product work.

---

## 8. What I would do this week

1. **Grant `disputes` and `help_center`** to Super Admin and to the support role, in a db-schema seed or migration, so a fresh environment does not depend on a manual click (`suggestions.md` §4.10.1, §4.11.1). Disputes first: users can already file them.
2. **Fix `didnt_make_transaction` → `not_my_transaction`** on `BVA-I353` before merge. Better still, read the enum from the server spec rather than retyping it.
3. **Decide the card verification model before `I380`/`I381` go further** (§2.3, `suggestions.md` §5.15). If it is the board's token model, plan the server card-route change. If it is the card PIN, update `I378` and change the client.
4. **Open a PR for `BVA-I353`**, or split it. At 76 files it is already hard to review. The FAQ and dispute half is ready apart from one value. The card half waits on item 3, and the statement and limits calls still need the §5.14 fixes.
5. **Make checklists mean something.** Agree who ticks `I392`-style checks (not the builder), and reopen `I392` until its boxes reflect what was verified.
6. **Let card spending be disputed.** Resolve the reference against the card partner's transactions, which the schema already allows (`suggestions.md` §4.11.2). Also store the transaction type `I341` asks for.
7. **Notify the user when a dispute is answered**, and make the admin answer conditional on the status read (§4.11.4–5).
8. **Give the admin dashboard a home.** The dispute queue (`I349`) and FAQ content (`I351`) both have APIs and no owner. Assign them to Promise on an admin-board sprint, or say the dashboard is paused.
9. **Make REVIEW/QA mean merged.** Move `I340`, `I365`, `I369` and `I376` back until their code is on `main`. Mark `I352` Done, or merge it into `I335`. Split `I350` into what #24 delivered and what remains.
10. **Handle `call.ended` on the client.**
11. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job.
12. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4), and **stop vendoring the client spec** (§5.10). Together they would have caught every mismatch in §2.2 and §5.14.
13. **Set `ZOHO_SPRINT_FILTER` to `1002`.**
14. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); blocks vs payment requests (§4.9); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 45.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 45 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002, as two unassigned Stories: `I349` Support Inbox, whose dispute API shipped in `beevia-admin-api` #24, and `I351` FAQ CMS, whose API shipped in #23. `beevia-admin` has gone 36.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed fifty-eight days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. Disputes and the dispute queue are real support and compliance work, but neither is a rubric capability. Line 11 (admin oversight) is already at 0.97 and is limited by the dashboard, which did not move. The client's FAQ, dispute and card work is on an unmerged branch, and branch code adds nothing until it is on `main`. `call.ended` is still unhandled, so line 2 stays at 0.92.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No server card change. Client card management on unmerged `BVA-I353`; its auth model is undecided (§2.3) |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | Dispute queue API shipped (#24), no role can use it and no dashboard screen; no `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether any role was granted `disputes` or `help_center` by hand** in production since the migrations ran, and whether any dispute has been filed yet.
- **Whether the `I392` checks were done** somewhere the board cannot see.
- **Whether `BVA-I353`'s screens are reachable** in the built app, or what is still on the author's machine.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went.** The export reads sprints, not the backlog.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel as three background calls and finished by about 14:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0. 0902 and 0901 were not re-exported; both are closed and static.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-29`: exit 1 (3 + 3 undocumented routes) before this cycle's spec edits, exit 0 after. The in-repo audit ran too, for the board section and the RFC-count check (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`q29.py`, `flow29.py`): 1002 day-over-day diff, every transition in the window by actor, cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions. Descriptions of `I332`, `I339`–`I352` and `I378`–`I381` were read, along with `I392`'s checkbox count.
5. Content checks. `git fetch --all --prune` and `for-each-ref` on every repo, `ls-remote` of `refs/pull/*`, and the remote-tracking reflog for `BVA-I353`. In `beevia-db-schema`: migration `0041` and every grant of `help_center` or `disputes` (none). In `beevia-api`: #87's commit message, controller, DTO and service; the upload controller and service; the card controller's auth model; `/auth/step-up`; `release.yml`; and the standing greps. In `beevia-admin-api`: #24's controller, DTOs and service. In `beevia-mobile`: `a444ec9`'s diff, every `support_service.dart` call against the server routes, the reason enum, the attachment JSON, the contract-test allowlist, `call.ended`, and conflict markers on `main`.
6. Spec and RFC updates (§3.4).
7. This report and its web edition.
8. End-of-run recheck at 14:12 UTC. A fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 11:33 UTC. `ls-remote` showed every `main` and `BVA-I353` at the commits read above, and no new branch or PR on any repo.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `reflog`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-29.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `openapi.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 29 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **0902 and 0901 were not re-exported.** Both are closed, and their 27 Oct and 19 Oct copies were reused for cycle times.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **Push times are not visible.** Commit dates show when work was written, not when it reached `origin`. `a444ec9` was authored at 10:18 UTC and first fetched here at 14:01 UTC.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 28 Oct 14:05 UTC → 29 Oct 14:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
