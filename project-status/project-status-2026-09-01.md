# Beevia — Project Status

**As of 2026-09-01** · Sprint **08-01** (10 Aug → 28 Aug) — **closed 4 days ago, still no successor sprint**
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-01.csv` + `beevia-activity-2026-09-01.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision. **This edition corrects one claim and one method from 31 Aug — see §0.1.**

---

## Quick overview

> **The backend restarted hard — 49 commits across three repos after three days of silence — and the board went the other way: two items were marked BLOCKED, both card work, and the review queue grew to 28 with still zero forward exits in the sprint's entire history. Separately, a first-time inspection of the mobile wallet found that its bank-transfer and add-money screens make no network calls at all, against endpoints that have been live for days.**

| | 31 Aug | 1 Sep | Δ |
|---|---:|---:|---:|
| To do (leaves) | 0 | 0 | 0 |
| In progress (leaves) | 5 | 2 | **−3** |
| **Blocked (leaves)** | 0 | **2** | **+2** |
| **In review / QA (leaves)** | 27 | **28** | +1 |
| Done (leaves) | 11 | 11 | 0 |
| **Forward review exits, whole sprint** | 0 | **0** | **22 days** |
| API surface (consumer / admin) | 131 / 29 | 131 / 29 | 0 / 0 |
| Commits merged | 1 | **24** | +23 |
| Successor sprint | none | **still none** | — |

**Team, at a glance:**

| Person | Owns | Leaf state | First submissions to review (7d) | Median cycle | Open WIP (age) | Commits (7d) | Flag |
|---|---|---|---:|---:|---|---:|---|
| Ayomikun Araoye | backend + admin API | 1 In prog, **14 Review**, 3 Done, 1 Blocked | 4 | 2.4 d † | 1 item @ 4 d | **49** | Broke the 3-day pause with 12 API fixes; one of his items was blocked by someone else |
| David Samuel | mobile | **9 Review**, 1 Blocked | 4 | 2.0 d † | — | 1 | **Zero open WIP.** Blocked both card items; still performs every review send-back |
| Philip Chidera | design | 1 In prog, 5 Review, **8 Done** | 3 | 0.9 d | 1 item @ 5 d | — | 8 of the sprint's 11 completions; item now 5 d old vs a 0.9 d median |
| Promise Udo | admin dashboard | — (no board presence) | — | — | — | 3 | Build-config fixes only; the mock-backed money modules are unchanged |

† Cycle-time medians are computed differently from the 31 Aug edition and are not comparable to the numbers printed there — see §0.1 and §5.2.

**The two questions for standup:** (1) BVA-I182 and BVA-I197 were both moved to BLOCKED yesterday afternoon — by what, and is it the same blocker? Ayomikun spent this morning fixing Anchor's card endpoints, which suggests it may already be cleared. (2) The mobile bank-transfer and add-money screens display a hard-coded bank list and a hard-coded account number (`0099873456`, "Chatbank_John Doe") while `GET /wallets/banks`, `POST /wallets/resolve-account` and `GET /wallets/payin-details` are all live. Is that a staging placeholder, or has nobody picked up the wiring?

**The three things worth knowing:**

1. **The backend came back at full speed, and all of it is repair work.** Twenty-four commits merged in the last day: 12 in `beevia-api`, 9 in `beevia-db-schema`, 2 in `beevia-admin`, 1 in `beevia-admin-api` — which ends its 24-day silence. Not one adds an endpoint; the consumer surface is still exactly 131 operations. What they add is correctness on the KYC-to-wallet path that every banking user walks: the BVN must now be verified *before* the banking profile is accepted, Anchor customers are matched on BVN and phone rather than email alone, malformed `+2340…` phone numbers are recovered, and `gender` is accepted case-insensitively. Each of these was a live provisioning failure (§2).
2. **Two card items were blocked, and they are the first BLOCKED items of the sprint.** `BVA-I182` (In-Chat Request Flow & Cards) and `BVA-I197` (Card Issuance Integration) both moved In progress → BLOCKED at 15:11 UTC on 31 Aug. Both card work; both blocked by the mobile lead. The board offers no reason. The plausible reading is that the Anchor card integration was broken — and this morning Ayomikun merged exactly that fix: Anchor serves card update as `PATCH`, not `POST`, and returns the reveal token as `data.token` rather than under `data.attributes`. Both defects would make card issuance and card reveal fail outright (§1.3).
3. **A first-time deep check of the mobile wallet found two complete UI flows with zero network calls.** `send_money_bank_transfer.dart` hard-codes a six-bank list, resolves every account number to the literal string `'John Doe'` after a 650 ms fake delay, and ends at a PIN sheet that pops the navigator instead of submitting. `add_money_screen.dart` displays `accountNumber = '0099873456'` as a compiled-in default. Meanwhile the P2P send path *is* genuinely wired to `POST /payments/transfer`, and the wallet home and transaction history read the real API. This is the wired-vs-stub split the rubric exists to catch, and it lowers capability 6 (§6).

**If you read nothing else:** the API is being repaired quickly and well, the board has not accepted a single item in 22 days, and the client's money-in and bank-payout screens are demonstrations rather than features.

---

## 0.1 Corrections to the 31 August edition

**Claim: "`beevia-admin-api` at 24 days silent."**

Correct when written; superseded. `beevia-admin-api` received a commit at 08:53 UTC today (`package update`, a dependency bump), and — more substantially — carries an unmerged branch `BVA-1226` with four commits implementing a full admin activity feed (§3.2). The "both admin repos are silent" framing, carried since 17 Aug, no longer holds for either repo. What does still hold is the specific gap the previous edition named: **none of the four Module 5 money-oversight endpoints the dashboard's mock screens are waiting on has been built.**

**Method: the per-person cycle-time figures.**

The 31 Aug edition printed David Samuel's median cycle time as **4.2 d on 13 measured items**. Recomputing from the same sidecar with the method described in §5.2 gives **2.0 d on the same 13 items**. This is not new data and it is not a factual error about the project — the two editions measured different things, and the earlier one did not record which. Rather than reverse-engineer it, this edition states its method explicitly and will hold to it:

> **A cycle measurement is one pass:** from an item's *most recent* entry into `In progress` to the *next* time it reaches `REVIEW/QA`. An item sent back and resubmitted contributes two measurements, not one, and a send-back loop is never counted as a single long cycle.

On that basis the 31 Aug figures would have read David 2.0 d, Ayomikun 0.9 d, Philip 0.9 d. The Δ against today is computed on those, so the change column in §5 is internally consistent. **Treat the 4.2 d printed on 31 Aug as incomparable, not as a regression that has since improved.**

---

## 1. Sprint 08-01 — four days after close

### 1.1 Where the 43 leaves sit

| Status | Leaves | Share | Δ |
|---|---:|---:|---:|
| **Review / QA** | **28** | **65%** | +1 |
| Done | 11 | 26% | 0 |
| **Blocked** | **2** | 5% | **+2** |
| In progress | 2 | 5% | −3 |
| To do | 0 | 0% | 0 |

Owner split of the review queue: Ayomikun 14, David 9, Philip 5.

67 board rows = 43 leaves + 24 parent stories. All figures above are leaves; parents are excluded to avoid double-counting.

### 1.2 The review queue, measured properly

| Measure | 31 Aug | 1 Sep |
|---|---:|---:|
| Leaves currently in REVIEW/QA | 27 | **28** |
| Distinct leaves that have *ever* entered REVIEW/QA | 27 | **28** |
| Transitions **into** REVIEW/QA (all time) | 48 | **49** |
| Transitions **out of** REVIEW/QA (all time) | 22 | 22 |
| Transitions REVIEW/QA → **Done** | **0** | **0** |
| Median queue age | 5 d | **6 d** |
| Oldest in queue | 17 d | **18 d** (1 item, see note) |
| Oldest backed by a submission | 14 d | **15 d** (7 items) |
| Arrived in the last 2 days | 0 | **1** |

All 22 recorded exits went backwards — 13 to In progress, 8 to To do, 1 to BLOCKED. **The transition REVIEW/QA → Done has never occurred in this sprint.** All 11 completions went In progress → Done, bypassing the queue entirely. Twenty-two days, 49 submissions, zero acceptances.

The one arrival is `BVA-I227` (§1.4). The queue otherwise aged by exactly one day, because nothing entered and nothing left.

Unchanged data gap: `BVA-I185` (Wallet Summary Endpoint, Ayomikun) shows status REVIEW/QA with **no status-change transition into it** — it was completed 13 Aug and reopened 14 Aug, and its current status appears to have been set by that reopen. `audit.py` dates it from the reopen, which makes it the queue's oldest item at 18 days; it is included in the figures above but is the one entry in them not backed by a submission.

### 1.3 The two blocked items — the sprint's first

Both moved at 15:11 UTC on 31 Aug, both by the mobile lead, both card work:

| Item | Owner | History |
|---|---|---|
| `BVA-I182` *In-Chat Request Flow & Cards* | David Samuel | To do → Review (17 Aug) → To do (18 Aug) → Review (26 Aug) → **BLOCKED** (26 Aug) → In progress (27 Aug) → **BLOCKED** (31 Aug) |
| `BVA-I197` *Card Issuance Integration* | Ayomikun Araoye | To do → In progress (26 Aug) → **BLOCKED** (26 Aug) → In progress (27 Aug) → **BLOCKED** (28 Aug) → In progress (28 Aug) → **BLOCKED** (31 Aug) |

`BVA-I197` has now been blocked and unblocked three times in six days. The board records no reason for any of them, so this report cannot tell you what the blocker is — only that it recurs and that it is card-shaped.

**What the code suggests.** Between 11:31 and 13:43 UTC today, `beevia-api` merged `fix/card-anchor-endpoints`, containing two defects that would break card issuance and card reveal outright:

- `updateCard` was issuing `POST /api/v1/cards/{id}`; Anchor serves that as `PATCH` and rejects the `POST` with *"Request method 'POST' is not supported"*.
- The card reveal token is returned by Anchor at `data.token`, not `data.attributes.token`, so the parser was returning `null` for every reveal.

That is a plausible cause for both blocks and it now appears fixed. **Nobody has moved either item off BLOCKED,** so if it is fixed, the board does not know.

### 1.4 Everything the board recorded since the last report

| When (UTC) | Item | Action |
|---|---|---|
| 31 Aug 15:11 | `BVA-I182` (leaf) | In progress → BLOCKED |
| 31 Aug 15:11 | `BVA-I197` (leaf) | In progress → BLOCKED |
| 31 Aug 15:11 | `BVA-I196` (parent Story) | In progress → BLOCKED |
| 1 Sep 11:11 | `BVA-I227` *Unified Activity Feed Endpoint* (leaf) | In progress → REVIEW/QA |
| 1 Sep 11:11 | `BVA-I226` (parent Story) | In progress → REVIEW/QA |

Five entries, three distinct pieces of work. That is the complete list.

**`BVA-I227` is worth singling out**, because it is the first item this pipeline has seen enter review with visible, matching, *unmerged* code behind it: `beevia-admin-api`'s `BVA-1226` branch implements `GET /admin/activity`, and the `admin_activity` table and DAL it reads merged to `beevia-db-schema` main this morning. That is review being used as "pull request open", which is a coherent meaning for the status — and it is a different meaning from the one the other 27 items carry, most of which are backed by code that merged days or weeks ago. Worth deciding which one the column means before the queue is disposed of.

### 1.5 Still no successor sprint

The Zoho project holds exactly three sprints: `08-01`, `0702`, `0701`. **08-02 has not been created**, four days after 08-01 closed. Twenty-eight items in review, two in progress and two blocked have nowhere to go.

---

## 2. What shipped this cycle

**24 commits across four repos — the largest single-day merge volume this pipeline has recorded — and not one new endpoint.** The consumer API is unchanged at 131 operations, the admin API at 29.

### 2.1 `beevia-api` (12 commits) — the KYC-to-wallet path, repaired

Every functional change lands on the path a banking user walks from BVN to a provisioned NGN account. Four are user-visible corrections:

| Fix | What was wrong |
|---|---|
| **BVN must be verified before the banking profile** (`POST /upgrade/profile`) | The profile step enqueues provisioning. Submitting it on an unverified BVN returned **200 OK** while `maybeProvision()` silently no-opped — so the client showed a completed upgrade, no account was ever opened, and `path` stayed `chat_only`. Now `400 bvn_required`. |
| **Anchor customer matched on BVN and phone, not just email** | Anchor de-dupes customers on email *and* phone, so a blind create threw *"Customer with email/PhoneNumber already exist"*. Worse: a BVN belongs to exactly one Anchor customer, so reusing the wrong one made the account permanently unverifiable. Now matched BVN-first, with an identity guard (`bvn_registered_elsewhere`) so a user is never provisioned onto someone else's customer. |
| **Malformed `+2340…` phone numbers recovered** | Clients sending both the country code and the local leading zero produced a hybrid Anchor rejects. |
| **`gender` accepted case-insensitively** | Clients send `"Male"`; the enum required `"male"`. Fixed on both `POST /kyc/profile` and `POST /upgrade/profile`. |

Plus the two Anchor card fixes in §1.3, and CI changes (rollback to `ubuntu-latest`).

This is good work on a real failure mode — a 200 that means nothing is the hardest class of bug for a client team to diagnose. It also carries an uncomfortable implication: **these paths were shipped and moved to review without anyone completing a live provisioning run**, or the failures would have surfaced then. See §6.

### 2.2 `beevia-db-schema` (9 commits) — the admin activity table

`admin_activity` lands as an append-only table (module, action, actor, target type/id, summary, metadata, timestamp) with `AdminActivityDal`, new enums, migration `0032`, and indexes for the paginated per-module feed query. A follow-up fix makes `actor_admin_id` `ON DELETE SET NULL` so deleting an admin does not delete the history of what they did — the right call for an audit surface. Released as v0.0.25 → v0.0.27.

### 2.3 `beevia-admin-api` (1 commit) and `beevia-admin` (2 commits)

Dependency and build-config housekeeping only. The admin API's silence is broken in the trivial sense; the substantive work sits unmerged (§3.2).

### 2.4 Repo staleness

| Repo | Last commit to `main` | Days silent | Δ |
|---|---|---:|---:|
| `beevia-api` | **1 Sep** | 0 | −3 |
| `beevia-db-schema` | **1 Sep** | 0 | −4 |
| `beevia-admin-api` | **1 Sep** | 0 | **−24** |
| `beevia-admin` | 31 Aug | 1 | −1 |
| `beevia-mobile` | 26 Aug | **6** | +1 |

**`beevia-mobile` is now the only stale repo**, and it is the one whose gaps §6 identifies as load-bearing.

Unmerged remote branches: `beevia-admin-api` carries `origin/BVA-1226` (§3.2); `beevia-mobile` carries `origin/BVA-I192` and four dependabot branches; `beevia-api` carries `origin/victor` and four merged-feature branches. Unmerged work does not count toward readiness scoring.

---

## 3. Spec updates made this cycle

Three edits, all driven by code read this cycle. The audit reports `code=131 spec=131` consumer and `29/29` admin, all four specs valid, no `x-beevia-*` markers, no broken refs, no orphaned components.

### 3.1 `openapi.yaml` — two contract changes to existing operations

No route was added or removed, so the drift check saw nothing. Two operations nevertheless changed contract:

1. **`POST /upgrade/profile` gained a precondition.** Documented the `400 bvn_required` response and the reason for it, matching the house style already used by `POST /kyc/id/start`.
2. **`gender` is now case-insensitive** on `KycProfileRequest` and `UpgradeProfileRequest`. The enum stays `[male, female]` — those remain the canonical values a generated client should send — with a description recording that input is trimmed and lower-cased before validation. Widening the enum to include `Male`/`MALE` would have been the wrong fix: it would push four dead variants into every generated SDK.

`api-rfc.md` §6.3a and §5.1 updated to match. **The §5.1 finding is worth reading:** the BVN-ordering guard was added to `POST /upgrade/profile` only. `POST /kyc/profile` has no equivalent — it still accepts a profile with an unverified BVN and still returns 200 while `maybeProvision()` no-ops. **The same bug the team just fixed is still live on the other ladder**, because the two ladders are near-duplicates and the fix was applied to one of them. This is the third time this RFC has recommended converging them.

### 3.2 `openapi.admin.proposed.yaml` — `GET /admin/activity` added (23 → 24)

The admin activity feed exists as written code on `beevia-admin-api`'s unmerged `BVA-1226` branch, and the table it reads is on `beevia-db-schema` main. It returns 404 against `beevia-admin-api` main, so it does **not** belong in `openapi.admin.yaml` — putting it there would create false drift on the next run and would let someone generate a client for a route that does not answer. It has been added to the proposed file instead, transcribed from the branch rather than designed, with a header comment saying exactly that and instructing the next editor to *move* it on merge. `admin-api-rfc.md` §5.4a records the same, and its counts are updated.

Two things about that contract deserve a reviewer's attention, and are written into §5.4a rather than left in a spec comment:

- **Its permission model is unlike every other admin operation.** Each of the other 52 declares one required permission and 403s without it. The feed declares none: any authenticated admin may call it and the service filters rows in SQL to the modules that admin can view, returning an empty list — not a 403 — to an admin entitled to nothing. That is the right shape for a feed, but it moves access control off the route decorator and into the service, where a reviewer has to go looking for it.
- **Pagination is cursor-based** (`before` / `nextCursor`) where every other list operation in the service is page-based.

Also: the feed's five actions are admin-console events only (user status change, role assignment, admin invite, admin deactivate/reactivate). Nothing from the money, KYC or chat modules appends to it, so "cross-module" currently means four of eleven modules.

### 3.3 The audit-trail endpoint from 31 Aug §3.1 — still open, now with a third option

`beevia-admin` still calls `GET /users/{id}/audit-trail` (`src/features/users/api.ts:229`), still without the `/admin` prefix every other admin route carries, still routed through a mock adapter, and still matching no operation in either admin spec. The new activity feed does **not** resolve it: `GET /admin/activity` is a global stream, not a per-user trail.

There are now three ways to close it, and it remains a decision for the two owners rather than an inference this report should bake into a spec:

1. Point the client at the existing `GET /admin/users/{id}/actions`, which is live and documented as exactly this.
2. Design a broader per-user trail and add it to the proposed spec.
3. **New:** derive it from `admin_activity` filtered on `target_type = 'user'`, which would make it a query parameter on the feed rather than a fourth endpoint.

**This is the sixth contract-level finding in twelve days that the automated check could not see** — the audit compares route inventories between API code and spec, and a client calling an undesigned endpoint is invisible to it.

---

## 4. Admin dashboard board

The second Zoho project, *Beevia Admin Dashboard* (`187554000000127002`), **still has no sprints**; step 1b returned exit 3 again, for the **thirteenth consecutive edition**. The board contributes nothing, so Promise Udo's row remains sourced from commits.

This cycle: two commits, both `fix: allow dependency build scripts`. The nine feature modules, four of them explicitly `MOCK IMPLEMENTATION — no network calls`, are unchanged from 31 Aug. The four Module 5 endpoints those mocks are waiting on (`/admin/transactions/{id}/flag`, `/admin/reconciliation`, `/admin/users/{id}/wallets`, `/admin/users/{id}/transactions`) remain proposed-only.

**Pipeline note, unchanged:** the two boards are never summed; admin exports land in `sprint-board-exports/admin/` because `beevia-audit` globs the main folder non-recursively; when the admin board gets a sprint its name will not match `ZOHO_SPRINT_FILTER`, so step 1b will keep skipping until `--sprint` is passed.

---

## 5. Team performance — detail

All figures come from the activity sidecar and git. None comes from the `Last Modified` column, which bulk board operations rewrite without producing per-item audit entries.

**Ayomikun Araoye — backend + admin API.** 14 items in review, 3 Done, 1 in progress (4 days), 1 blocked. **49 commits in 7 days** across `beevia-api` (26), `beevia-db-schema` (22) and `beevia-admin-api` (1), summing the `Ayomikun Araoye` and `Phoenixdadhev` identities and excluding the release bot. The three-day silence the last edition flagged as ambiguous resolved into the busiest single day in the project's history. Four first submissions to review in 7 days, including `BVA-I227` today. His one blocked item was moved there by someone else.

**David Samuel — mobile.** 9 items in review, 1 blocked, **zero in progress and zero Done for the sprint**. One commit in 7 days; `beevia-mobile` has not received a commit in 6 days and is now the only stale repo. He remains **the only person who has ever moved an item out of REVIEW/QA** — all 22 leaf exits are his, and all are send-backs — and he moved both card items to BLOCKED yesterday. That is review and triage work the board records as nothing at all, while his own delivery column reads zero. Two readings fit the data equally well: he is absorbed in reviewing everyone else's work, or he is stuck on the card blocker. The board cannot distinguish them; a question at standup can.

**Philip Chidera — design.** 8 of the sprint's 11 completions, 5 in review, 1 in progress. His open item (`BVA-I171`, Correct Bank Name Display) is now **5 days old against a 0.9 d median** — by the standing heuristic, probably stuck, and mildly ironic given §6's finding that the bank list is hard-coded.

**Promise Udo — admin dashboard.** No board presence, thirteenth consecutive edition. Three commits, all build configuration. No feature change since the 28 Aug commit.

### 5.1 Weekly submission trend

First-ever submissions into REVIEW/QA, by week: 17–23 Aug — 17 items; 24–30 Aug — 10 items; 31 Aug onward — **1 item**. Against an acceptance rate of **zero for the whole sprint**.

Output is falling and acceptance has never been non-zero. That combination is not a developer-throughput problem: the queue has absorbed 49 submissions and released none forward, so the constraint is downstream of everyone in the table above.

### 5.2 Cycle times, and why the median is a poor summary here

Method, restated from §0.1: one measurement per pass, from the most recent entry into `In progress` to the next arrival at `REVIEW/QA`.

| Person | n | Distribution (days) | Median |
|---|---:|---|---:|
| Philip Chidera | 7 | 0, 0, 0, 0.9, 0.9, 8.2, 13.0 | **0.9** |
| David Samuel | 13 | 0, 0, 0, 0.9, 0.9, 0.9, 2.0, 3.1, 4.1, 4.2, 6.0, 8.2, 9.3 | **2.0** |
| Ayomikun Araoye | 10 | 0, 0, 0.9, 0.9, 0.9, 3.9, 4.1, 6.2, 7.1, 13.0 | **2.4** |

Ayomikun's median moved 0.9 → 2.4 on the addition of a single 3.9-day measurement (`BVA-I227`). That is a small-sample artifact, not a slowdown: with n=9 the median was the fifth value; with n=10 it is the mean of the fifth and sixth, and his distribution is bimodal — five passes at ≤0.9 days and five at ≥3.9. **Do not read a 2.7× change into it.** Every distribution here is bimodal in the same way, which is what you would expect from a mix of same-day board hygiene and multi-day builds. The medians are reported because the format asks for them; the distributions are what to actually look at.

### 5.3 What these figures do not measure

- **No estimation points exist on any of the 67 items.** Nothing is normalised for size; an item count says nothing about who is carrying more.
- **Board actions are not evenly attributable.** Of the 49 submissions into review, 40 were performed by one person, 7 by board administration and 2 by the item's own assignee. Per-person figures above are keyed to the item's **assignee**, not to whoever clicked.
- **Cycle time rewards small items; commit counts reward small commits.** Ayomikun's 49 commits are largely incremental fixes with their own tests; Promise's 3 are build config. Neither number measures difficulty or quality.
- **The zero-acceptance rate is a process finding, not a personal one.** It is not attributable to any individual in the table.
- **Review and triage work is invisible.** All 22 send-backs and both blocks are one person's work, and none of it appears in any delivery column.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction. Nothing here claims the code works — though §2.1 and §6 are both evidence that some of it did not.

---

## 6. The mobile wallet — screens that are not yet features

This section is new, and it is the result of applying the rubric's wired-vs-stub check to `beevia-mobile`'s wallet flows for the first time at file level. `beevia-mobile` has 45 screen files across six features and has not changed in 6 days, so none of this is new code — it is newly *examined* code.

| Flow | Screen | State |
|---|---|---|
| Wallet home / balances | `wallet_screen.dart` | **Wired** — `GET /wallets` via `WalletProvider` → `WalletService` |
| Transaction history | `transaction_history.dart` | **Wired** — `GET /wallets/transactions` |
| P2P send | `send_money_screen_p2p.dart` → `send_money_amount_screen.dart` | **Wired** — `GET /payments/recent-recipients`, `POST /auth/step-up`, `POST /payments/transfer` |
| **Bank transfer out** | `send_money_bank_transfer.dart` | **Stub — no network calls** |
| **Add money (in)** | `add_money_screen.dart` | **Stub — no network calls** |

The two stubs in detail:

- **`send_money_bank_transfer.dart`** carries `const walletBanks = [...]` — six banks hard-coded with names, sort codes and brand colours — while `GET /wallets/banks` is live. Account-name lookup calls `widget.accountVerifier ?? _previewAccountVerifier`; nothing anywhere in `lib` supplies an `accountVerifier`, and the fallback waits 650 ms and returns the literal string `'John Doe'`. `POST /wallets/resolve-account` is live and never called. The review step ends at `showBankTransferPinSheet(...)` followed by `Navigator.of(context).pop(true)` — **the transfer is never submitted.** `POST /wallets/withdraw` has zero references in the repo.
- **`add_money_screen.dart`** routes to `AddMoneyBankTransferDetailsScreen`, whose constructor defaults are `accountNumber = '0099873456'`, `accountName = 'Chatbank_John Doe'`, `bankName = 'Paystack Titan'`. The caller passes no arguments, so those defaults are what renders. `GET /wallets/payin-details` is live and *is* called — but only from the onboarding KYC provider, never from this screen. The screen offers copy-to-clipboard and share on that hard-coded number.

**Why this matters beyond scoring.** A user who reaches the add-money screen on `main` is shown a plausible-looking account number and invited to copy or share it. That is a demo behaviour sitting on the default branch of a money application. Whether the risk is real depends on how the app is distributed, which this pipeline cannot see — but it should be a deliberate decision rather than an artifact of a screen built before its API existed.

Domains with **zero** references anywhere in `beevia-mobile/lib`: `/cards` (13 live operations), `/topups` (3), `/translate` (1) — the last despite `translate_chat_screen.dart` existing. The client's endpoint constants file lists 47 paths against the API's 131 operations.

---

## 7. Risks

1. **No sprint 08-02 exists**, four days after 08-01 closed. 28 review items, 2 in progress and 2 blocked have no destination.
2. **The forward path out of REVIEW/QA has never been exercised** — 0 of 28 accepted in 22 days, across 49 submissions. This is a demonstrated property of the process, not a backlog.
3. **Two card items are blocked with no recorded reason**, one of them for the third time in six days, while a plausible fix for both merged this morning and nobody has moved them.
4. **The same silent-200 provisioning bug fixed on `/upgrade/profile` is still live on `/kyc/profile`** (§3.1). The duplicated KYC ladder means every fix has to be applied twice, and this one was not.
5. **A large money-handling surface remains unverified** — cards, top-ups, payouts and bank transfers all sit in the review queue, and §2.1 shows the provisioning path was shipped with defects that a single live run would have caught.
6. **The client's money-in and bank-payout flows are stubs** against live endpoints, including a hard-coded account number on `main` (§6).
7. **`beevia-mobile` is the only stale repo** at 6 days, and it is where the largest capability gap sits.
8. **The admin dashboard's money modules remain mock-backed** against four endpoints that have not been built.
9. **Contract drift stays invisible to automation** — sixth instance in twelve days (§3.3).
10. **0/67 estimation points**, so any carry-over conversation still has no size data.

---

## 8. Previous recommendations — where they stand

| Recommendation from 31 Aug | Status on 1 Sep |
|---|---|
| Create 08-02, or say explicitly the project is not running sprints | **Not done.** Still three sprints: `08-01`, `0702`, `0701`. |
| Dispose of the 28 review items into accepted / sent back / never built | **Not done.** Queue grew to 28; median age 6 d. |
| Exercise the accept path once, on anything | **Not done.** Zero forward exits, 22 days. |
| Decide the admin API sequencing | **Partially.** `admin_activity` merged and `GET /admin/activity` written on a branch — but that is the feed, not the four Module 5 money endpoints the dashboard is waiting on. |
| Resolve the audit-trail endpoint (§3.1) | **Not done**, and now has a third option (§3.3). |

One of five partially addressed. The four unaddressed are the same four, still blocked behind the same missing decision.

---

## 9. What I would do this week

1. **Create 08-02, or state that the project is not running sprints.** Fourth consecutive edition making this recommendation; four days of drift is now a decision made by default.
2. **Unblock or annotate the two card items today.** The fix that most likely clears them merged this morning. Either move them and note why, or record what the actual blocker is — a third silent block/unblock cycle teaches everyone that BLOCKED means nothing.
3. **Apply the BVN-ordering guard to `POST /kyc/profile`.** It is a five-line change already written for the other ladder, and until it lands the banking-path signup cohort still gets a 200 that means nothing.
4. **Run one live provisioning end to end and one card issuance end to end.** Four of today's twelve fixes were defects a single real run would have surfaced; two more are sitting behind a BLOCKED flag for want of one. This is the cheapest available check on the largest unverified surface.
5. **Decide what the mobile bank-transfer and add-money screens are.** Either schedule the wiring — `GET /wallets/banks`, `POST /wallets/resolve-account`, `POST /wallets/withdraw`, `GET /wallets/payin-details` are all live and documented — or mark them clearly as previews so the hard-coded account number cannot reach a user.
6. **Exercise the accept path once, on anything.** Unchanged from the last three editions and still the single most informative thing anyone could do. `BVA-I227` is a good candidate: it is the one item whose review has an obvious, checkable meaning.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (67 items, cut-off 11:11 UTC) → admin board (exit 3, no sprints, 13th edition) → fast-forward sync (**24 commits pulled across 4 repos; all five repos clean, none dirty, none diverged, none switched branch**) → deterministic audit (exit 1: board findings, no route drift) → manual contract review, which produced §3.1, §3.2 and §6 → this report.

**Degraded inputs.** The `Epic` column is blank across all 67 items — the OAuth refresh token lacks `ZohoSprints.epic.READ`. This is a known scope gap, not "no epic assigned". `Comments` bodies are unavailable from the API. The admin board produced no export because the project has no sprints (expected, not a failure). No other input degraded; no step was skipped or run against stale code.

**Window.** 31 Aug 13:15 UTC → 1 Sep 14:00 UTC. `actiontime` values are UTC; git timestamps normalised to UTC where quoted; CSV header times are the exporting machine's local MDT.

**Sources.** Board: `beevia-sprint-board-2026-09-01.csv` (67 rows, 43 leaves), `beevia-activity-2026-09-01.json`. Admin board: none. Code: five repos at `origin/main`, plus read-only inspection of `origin/BVA-1226` on `beevia-admin-api`. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (**24**, +1 this edition) — all validated, no drift, no markers, no broken refs.

**A note on who appears here.** Only people whose work is tracked have rows. Board-administration actions performed by a non-contributor are reported as transitions without attribution, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈58% (estimate; 57.5, from 58.1)

**Target 2026-09-01 (provisional) · the target date is today.** On merged build evidence the product is roughly 58% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points have not been started at all. The date has arrived and is not met; this report has said so at every edition since the estimate began.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live since 10 July; `translate_chat_screen.dart` exists but **`/translate` has zero references in `lib`** — the screen is not wired. Batch/languages/preference still proposed |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full onboarding flow (BVN, facial verification) wired in the client. **Materially hardened today** (§2.1) — four provisioning defects fixed. Ceiling: the same silent-200 bug remains live on `/kyc/profile` |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | **0.70** ↓ | **Moved −0.05.** Wallet home and transaction history are wired to `GET /wallets` and `/wallets/transactions`. But the bank-payout and add-money flows make **zero network calls** — hard-coded bank list, a fake `'John Doe'` account resolver, a hard-coded pay-in account number, and no call to `/wallets/withdraw` (§6). Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | P2P send confirmed wired end to end: `send_money_amount_screen` → `WalletProvider.transferMoney` → `POST /payments/transfer`, with `/auth/step-up`. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; `PaymentService.activeNgn()` still present |
| 9 | Virtual cards | 10 | 0.45 | 13 operations live, and two that were broken were fixed today (§1.3). Not moved: the fixes restore intended behaviour rather than adding capability, the client still has zero `/cards` references, there is no issuer webhook, and both card board items are BLOCKED |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.50 | `GET /admin/activity` is written but **unmerged**, so it does not score (§3.2). `admin_activity` merged to `beevia-db-schema`, which is infrastructure, not surface. 3 of 8 dashboard modules wired; admin API unchanged at 29/52 |
| | **Weighted total** | **100** | | **57.5 → ≈58%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches.

**On the two movements.** Capability 6 comes down 0.05 on evidence that is new to this report but not new to the code: §6 is the first file-level wired-vs-stub check of the mobile wallet's payout flows, and two of the five flows turn out to make no network calls. Capability 9 does *not* move despite real card fixes merging, because restoring an endpoint to its intended behaviour is not new capability — and the rubric's standing rule is that a score moves only when the evidence names something that now exists and did not before. The headline is unchanged at ≈58% because 58.1 and 57.5 round to the same number, not because nothing happened.

**What this report cannot tell you:**
- **What blocked the two card items.** The board records no reason for any of the five block/unblock transitions on them.
- **What the 28 review items are worth.** Twenty-two days of zero acceptances means nobody has recorded an opinion — and §1.4 shows the column now carries at least two different meanings.
- **Whether today's twelve fixes work.** They ship with tests; none has been demonstrated against live Anchor. Testing is out of scope for scoring.
- **Whether the mobile stubs are deliberate staging or abandoned scaffolding.** The code is honest about being a preview; nothing says when it stops being one.
- **Why there is no 08-02** — deliberate pause, unheld planning session, or oversight.
- **Anything about the Admin Dashboard board** beyond its existence — thirteenth edition with no sprint.
- **Velocity or scope-fit for any future sprint** — the board remains at 0/67 estimated.
