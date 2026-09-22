# Beevia — Project Status

**As of 2026-09-16** · Sprint **0901** (3 Sep → 22 Sep) — **day 14** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 14** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-16.csv` + `beevia-activity-2026-09-16.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-16.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (30 items) + sidecar; all five repos at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` read via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. Window **15 Sep 14:04 UTC → 16 Sep 14:04 UTC** (~24 hours, Mon→Tue).

---

## Quick overview

> **The branch merged.** After 40 days, `origin/BVA-I242` landed on `beevia-mobile`'s `main` as a single squash commit — and it landed **split**, exactly as the previous edition asked. The money half is in: the in-chat send-money flow, the socket commands that make payment request / accept / decline / cancel real, the virtual-card issuance flow, bank transfers, withdrawals, and seven new test files. The localisation half is not: the entire `lib/l10n` layer, four locales, and the on-device translation engine are still only on the branch. This is the largest genuine build event this report has recorded — **MVP readiness moves for the first time in nine editions, +3.30 to ≈61%** — and it is also the first time the previous edition's top recommendation was acted on. Two smaller firsts came with it: **David moved his own board items**, at 11:25 this morning, ending four editions of his board being transcribed by someone else; and **an item left REVIEW/QA** — though that one is a design Story that was created, reviewed and closed inside 46 hours without ever queueing, and the eleven engineering items behind it did not move at all and are now a day older.

| Measure | 15 Sep | 16 Sep | Δ |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 12 | **14** (13 excl. release bot) | **+2** |
| Commits on *any* ref, all five repos, in window | 12 | **17** (14 excl. bots) | **+5** |
| Board transitions, all three boards, in window | 11 | **4** | **−7** |
| API surface (consumer / admin) | 137 / 47 | 137 / 47 | 0 |
| Proposed operations (consumer / admin) | 38 / 19 | 38 / 19 | 0 |
| Spec drift vs `origin/main`, both services | 0 | 0 | 0 |
| Sprint 0901 leaves, total | 21 | 21 | 0 |
| Sprint 0901 leaves To do | 5 | **3** | **−2** |
| Sprint 0901 leaves In progress | 1 | **2** | **+1** |
| Sprint 0901 leaves REVIEW/QA | 11 | 11 | 0 (one in, one out — §1.3) |
| Sprint 0901 leaves Done | 4 | **5** | **+1** |
| Admin board leaves In progress / Done | 2 / 6 | 2 / 6 | 0 |
| Review-queue median age (0901) | 6.9 d | **7.9 d** | **+1.0** |
| Oldest open WIP (0901) | 0.9 d | **1.9 d** | +1.0 |
| **Unmerged on `origin/BVA-I242`** | **15 commits · 40 d** | **the l10n layer only — §1.5** | **the money half merged** |
| `beevia-mobile` `main` days since a commit | 19.4 | **0.9** | **−18.5** |
| `beevia-admin` `main` days since a commit | 1.1 | **2.1** | +1.0 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.8 each | **0.1 each** | −0.7 each |
| Ayomikun commits (7d, 2 identities, merged) | 31 | **36** | **+5** |
| David commits (7d, merged to `main`) | 0 | **1** (the squash merge) | **+1** |
| Promise commits (7d, merged) | 4 | **1** | −3 (window moved past 8 Sep) |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 30 · 0 / 12 | 0 / 30 · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈58% (58.10) | **≈61% (61.40)** | **+3.30** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---:|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 10 on 0901 · 3 on 0901-admin | 2 leaves (`BVA-I231`, `BVA-I245`), both self-reported | 6.2 d | **0** | **36** (was 31) | Five merged commits: an `email` field on the self view, a Node 24/26 CI matrix across all three backend repos, and a commit labelled `otp fix` that changes no behaviour and deletes four safety rationales (§2.3). Nine of the eleven items in review are his |
| David Samuel | mobile | 7 on 0901 — 1 To do, **2 In progress**, 2 REVIEW/QA, 2 Done | 2 leaves (`BVA-I233`, `BVA-I243`), both moved **on 14 Sep by a non-contributor** | 2.6 d | 2: `BVA-I229` 1.9 d, `BVA-I238` 0.1 d | **1 merged** — the squash of 40 days of work | **Two firsts.** His branch merged at 16:07 UTC yesterday, and at **11:25 this morning he moved `BVA-I237`/`BVA-I238` to In progress himself** — the first self-attributed board transition of his this report has recorded |
| Philip Chidera | design | 4 on 0901 — 3 Done, 1 To do | 1 (`BVA-I268`, moved to review by a non-contributor) | 0.9 d | 0 | — | **Completed `BVA-I268` himself** at 11:53 UTC — the first item ever recorded leaving REVIEW/QA on this sprint. It was created 15 Sep 13:58 and never aged in the queue (§1.3) |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 — zero self-made transitions, still | — | 1 (`BVA-I9`, moved for him on 14 Sep) | **1** (was 4 — three commits aged out of the window, nothing was lost) | Fifth consecutive edition of zero self-attributed board activity, and no `beevia-admin` commit for 2.1 days. Separately: that repo has **no CI of any kind** — see §3.2 |

**The two questions for standup:** (1) **Now that the money half has merged, what is the plan for the l10n half?** `origin/BVA-I242` still holds the entire localisation layer and the on-device translation engine, and `BVA-I229` *Translation Engine Integration* went back to In progress this morning — so the branch is being worked, not abandoned. Is the intent a second squash, or does the 41-day lineage start over? (2) **Will the eleven-item review queue get the same treatment the branch just did?** One design item went in and out in a day; the seven notification items have now been in review for **7.9 days** with six days left in the sprint. The branch proved a decision can be made — this queue is the next one.

**The three things worth knowing:**

1. **The merge is real, verified by content, and it is only half the branch.** `874697a` is a squash merge, so the branch's 17 commits do not appear in `main`'s history — the content is what was checked. Diffing the merged `main` against the branch tip shows **112 files and ~18,200 insertions still outstanding**, and they are almost entirely one thing: `lib/l10n/` (four locales plus generated Dart), `l10n.yaml`, `lib/core/language/` — including `on_device_translation_service.dart` — the `select_language` onboarding screen, and the string-substitution churn that touches roughly eighty screens. **What merged is the money. What did not is the language.** That split is the single most consequential fact in this report and it is why capability #3 does not move while #6, #7 and #9 do.
2. **"Send / request / receive in chat" stopped being a facade.** The 2026-08-07 finding on this project was that chat had Send money and Request money buttons with a local placeholder handler and zero calls to the payments API. That is now false. `chat_send_money_flow.dart` reads the real `WalletProvider`, fetches the wallet and refreshes transactions; `payment_events.dart` emits `payment.request`, `payment.accept`, `payment.decline` and `payment.cancel` over the socket with acknowledgements and listens for `payment.updated`. All four command names match `@SubscribeMessage` handlers in `beevia-api`'s `messaging.gateway.ts` exactly — checked name by name, not assumed.
3. **The queue's first-ever exit does not mean the queue is moving.** `BVA-I268` is real movement and it was self-completed by its owner, which is the pattern this report has been asking for. It is also a design Story created 15 Sep 13:58, pushed to REVIEW/QA by a non-contributor two hours later, and closed by Philip this morning — it was never in the queue anyone is worried about. **The eleven engineering items in REVIEW/QA are the same eleven items as yesterday**, item for item, and the seven-item notification block is now 7.9 days old.

**If you read nothing else:** the thing this report has flagged in every edition since 6 August — a mobile branch accumulating real product work without landing — resolved today, partially and in the right direction. The MVP estimate moves to ≈61% on merged evidence alone. The two things that did not change are the review queue and `beevia-admin`, and the second of those turns out to be worse than previously reported: it has no CI at all.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

30 items — **21 leaves, 9 parent Stories** (unchanged). Day 14 of 20, 6 days remain.

| Status | Leaves | 15 Sep | Δ |
|---|---:|---:|---:|
| To do | **3** | 5 | **−2** |
| In progress | **2** | 1 | **+1** |
| REVIEW/QA | 11 | 11 | 0 |
| Done | **5** | 4 | **+1** |
| BLOCKED | 0 | 0 | 0 |

| Owner | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Ayomikun Araoye | 10 | 1 | 0 | **9** | 0 |
| David Samuel | 7 | 1 | **2** | 2 | 2 |
| Philip Chidera | 4 | 1 | 0 | 0 | **3** |

### 1.2 Who actually moved each item

Four transitions in the window, from the activity sidecar's exact `actiontime`:

| Item | Owner | Change | When (UTC) | Moved by |
|---|---|---|---|---|
| `BVA-I268` | Philip Chidera | To do → REVIEW/QA | 15 Sep 16:09:27 | *non-contributor* |
| `BVA-I237` (parent Story) | David Samuel | To do → In progress | 16 Sep 11:25:24 | **David Samuel** (self) |
| `BVA-I238` | David Samuel | To do → In progress | 16 Sep 11:25:24 | **David Samuel** (self) |
| `BVA-I268` | Philip Chidera | REVIEW/QA → Done | 16 Sep 11:53:48 | **Philip Chidera** (self) |

**Three of the four were made by the person who owns the item.** That is a change worth stating plainly: the previous four editions recorded David's items moving without him, twice by two different non-tracked actors, and this report asked directly whether he was making those moves. This morning he made two, fourteen hours after his branch merged. The question is answered for today; it does not retroactively explain the 14 September moves.

Only `BVA-I238` is a leaf — `BVA-I237` is its parent Story — which is why the leaf-level In progress count rises by one rather than two.

### 1.3 The review queue — the same eleven items, now 7.9 days median

| Item(s) | Owner | Entered REVIEW/QA | Age |
|---|---|---|---:|
| `BVA-I246`–`BVA-I252` (7 items) | Ayomikun Araoye | 8 Sep 16:02–16:04 UTC | **7.9 d** |
| `BVA-I231` | Ayomikun Araoye | 10 Sep 10:25 UTC | 6.2 d |
| `BVA-I245` | Ayomikun Araoye | 14 Sep 14:53 UTC | 2.0 d |
| `BVA-I233` | David Samuel | 14 Sep 16:04 UTC | 1.9 d |
| `BVA-I243` | David Samuel | 14 Sep 16:04 UTC | 1.9 d |

**Median age 7.9 days** (was 6.9). The count is unchanged at eleven because `BVA-I268` entered and left within the window — it is not in the table above, and it never appeared in any snapshot of this queue.

This is the distinction the headline number hides. **Something left REVIEW/QA for the first time in nine editions, and the queue is not one item smaller.** An item created on Monday afternoon, pushed to review two hours later and closed on Tuesday morning tells you the process *can* complete; it tells you nothing about a block of notification work that has been waiting eight days. Six days remain before 22 September.

`FCM_SERVICE_ACCOUNT` is still blank in `beevia-api/.env.example` (line 79) and still `.optional()` in `common/env.ts` (line 111), re-verified at `origin/main` today. Accepting `BVA-I246` without checking the deployed value still accepts a `StubPushAdapter`.

### 1.4 WIP is David's, and both items are the language work

Both In-progress leaves belong to David: `BVA-I229` *Translation Engine Integration* (1.9 d) and `BVA-I238` *Auto-Translation Display* (0.1 d). Both sit precisely on the half of the branch that did **not** merge, which is coherent: the money work went to review and to `main`, and the language work went back to In progress. Neither is older than his 2.6-day median cycle time, so neither reads as stuck yet.

### 1.5 `origin/BVA-I242` — merged, in half

**What merged.** `874697a "Bva i192 (#33)"`, authored by David Samuel, merged to `beevia-mobile` `main` at **15 Sep 16:07 UTC** — three minutes after the previous edition's window closed, which is why that edition could not see it. It is a squash, so the branch's individual commits are not ancestors of `main`; the comparison below is by content, not by history.

76 files changed, **+7,244 / −1,171**. New on `main`:

| Area | Files |
|---|---|
| Money in chat | `chat/screens/chat_send_money_flow.dart` |
| Payment commands | `wallet/services/payment_events.dart` — socket `payment.request` / `accept` / `decline` / `cancel` + `payment.updated` listener |
| Virtual cards | `wallet/models/virtual_card.dart`, `request_virtual_card_screen`, `review_card_request_screen`, `card_request_success_screen`, `widgets/card_request_widgets.dart` |
| Bank transfers | `bank_transfer_amount_screen`, `bank_transfer_review_screen`, `widgets/bank_transfer_widgets.dart` |
| Requests | `wallet/screens/request_money_screen.dart` |
| Funding | `wallet/services/paystack_payment_service.dart`, `models/wallet_funding.dart`, `models/wallet_bank.dart`, `models/payment_update.dart` |
| Tests | 7 new files under `test/features/wallet/` and `test/features/user/`, 2 modified |

**What did not merge.** Diffing `origin/main` against the branch tip (`92982c5`, "translation engine", 15 Sep 15:48 UTC) leaves **112 files, ~18,200 insertions**:

- `lib/l10n/app_en.arb`, `app_es.arb`, `app_fr.arb`, `app_zh.arb` (517 lines each) and ~9,600 lines of generated `app_localizations*.dart`;
- `l10n.yaml`, `lib/l10n/l10n.dart`;
- `lib/core/language/` — `app_language.dart`, `language_provider.dart`, `language_settings_service.dart`, **`on_device_translation_service.dart`**;
- `lib/features/onboarding/screens/select_language.dart` and four flag assets;
- localisation string-substitution churn across roughly eighty existing screens (`chat_details.dart` alone shows 1,110 changed lines).

**Lineage age.** The first commit on this lineage (`origin/BVA-I192`, 6 Aug) is now **41 days** old. The branch has not been deleted and is still being committed to, so "the branch merged" and "the branch is still open" are both true; what changed is that the money work is no longer trapped behind the language work.

### 1.6 Trust & Safety scope — unchanged, unpriced, fourth edition

`BVA-I254`, `BVA-I255`, `BVA-I256` (leaves; `BVA-I253` is their parent Story) are all still **To do** with **0 estimation points**, and no code exists for any of them. With six days left in the sprint, this scope will not ship in 0901 on any reading.

### 1.7 Still no estimates — eleventh consecutive edition

**0 of 30 on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01.** Confirmed at the raw field level — every value is the literal string `0`, not a blank. Velocity remains underivable, including for the merge that just landed.

---

## 2. What shipped this cycle

**14 commits merged to `origin/main` across four repositories** (13 excluding a release bot); zero to `beevia-admin`.

| Repo | Commits | What |
|---|---:|---|
| `beevia-api` | **6** | `feat(auth): return the user's email when they have one` (a real contract change — §3.1); `ci: test on Node 24 and 26, drop 22`; `ci: bump checkout and setup-node to v7`; `otp fix` (no behaviour change — §2.3); 2 merge commits (PRs #44, #45) |
| `beevia-mobile` | **1** | `874697a Bva i192 (#33)` — the squash merge, §1.5 |
| `beevia-admin-api` | 3 | Node 24/26 CI matrix + action bumps (PR #11) |
| `beevia-db-schema` | 4 | Node 24/26 CI matrix + action bumps (PR #10); `chore(release): v0.0.31` by the release bot |
| `beevia-admin` | 0 | No change since `f12135b` (14 Sep) — 2.1 days |

Two dependabot branches also appeared on `beevia-mobile` (`gradle-minor-and-patch`, `actions/setup-java`), unmerged.

### 2.1 The client's wallet surface doubled, and it is wired to the real API

`wallet_service.dart` went from five methods to ten. Before the merge it called `/wallets`, `/wallets/transactions`, `/payments/recent-recipients`, the step-up endpoint and `/payments/transfer`. It now also calls `/wallets/payin-details`, `/wallets/banks`, `/wallets/resolve-account`, `/wallets/withdraw`, `/topups/initialize`, `GET /cards` and `POST /cards`. Withdrawal and card issuance both send an `X-Step-Up-Token` header; the transfer path carries an `idempotencyKey`.

**These are real calls, not mock routes.** Every one of the ten endpoint constants in `lib/core/constants/api_url.dart` resolves to a caller in `lib/features/`, checked constant by constant. `lib/mock/` exists but is reachable only from `lib/main_dev.dart`; `lib/main.dart` passes no installers, so the mock is not in the production build's import graph at all. That is a deliberate design — the entrypoint comment says so — and it is why the mock layer does not undermine the wired-vs-stub judgement the way an in-process feature flag would.

### 2.2 Chat payments are socket commands, and they match the server

The reason `/payments/request` does not appear in the client's HTTP constants is that request, accept, decline and cancel are not HTTP calls — they are Socket.IO commands with acknowledgements:

| Client (`socket_constant.dart`) | Server (`messaging.gateway.ts`) |
|---|---|
| `payment.request` | `@SubscribeMessage('payment.request')` — line 427 |
| `payment.accept` | `@SubscribeMessage('payment.accept')` — line 435 |
| `payment.decline` | `@SubscribeMessage('payment.decline')` — line 443 |
| `payment.cancel` | `@SubscribeMessage('payment.cancel')` — line 451 |
| `payment.updated` (listener) | server → client event |

Four commands, four handlers, names identical. The client falls back cleanly when the socket is down (`_emitWithAck` returns `error: 'socket not connected'` rather than hanging).

**Not wired:** `POST /payments/send` and the `/payments/{id}/pay` HTTP path are unused by the client, and there is still no payments read path — history comes from `/wallets/transactions`. Of the thirteen `/cards` operations the server exposes, the client uses **two** (list and issue); freeze, unfreeze, terminate, reveal, reveal-pin, fund, withdraw, transactions and transfers have no client consumer. Both gaps are priced into the scores in the appendix.

### 2.3 A commit called `otp fix` fixes nothing

`5843ccf` touches `auth.service.ts` and `otp.service.ts`. Diffed with `-w` and with comment lines removed, everything that remains is line-wrapping — multi-line import braces, a wrapped exception literal, a wrapped method signature. **No behaviour changed.**

What it did remove is four comment blocks, each documenting why the surrounding code is safe: that `login()` returns an identical response whether or not the account exists, to prevent phone-number enumeration; that `assertCanSignIn` is the real gate because a code may have been issued before an account was stopped; and that the Slack OTP echo is gated on `OTP_ECHO` and must never fire unconditionally, because it would post live codes for real users into Slack in production. That last one is the only in-code marker on a flag that is still item §1.2 of `suggestions.md`.

Recorded in `suggestions.md` §5.7. It is a small thing, but a formatting pass labelled as a fix to the OTP path is exactly the commit a future reader will open when looking for an OTP behaviour change and misread.

### 2.4 The backend repos moved to a Node 24/26 CI matrix

All three backend repos now test on Node 24 and 26 and dropped 22, with `actions/checkout` and `actions/setup-node` at v7. Routine maintenance, noted because it landed simultaneously in three repos and accounts for six of the fourteen commits.

---

## 3. Spec updates made this cycle

**One contract change, one spec edit.** The deterministic audit run against a read-only `origin/main` shadow reports:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 47  spec= 47  proposed= 19  [OK]
```

**Route-level drift: zero, both services, both directions** — before and after the edit. All four spec files parse; no `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s.

### 3.1 `email` added to the `User` schema — the kind of change the audit cannot see

`feat(auth): return the user's email when they have one` adds an optional `email` to `PublicUser`, the shape behind `GET /auth/me`, `POST /auth/otp/verify` and `POST /auth/pin`. No operation was added or removed, so the route-level audit is silent on it; it is a field-level change and had to be caught by reading the diff.

Updated in place:

- **`openapi.yaml`** — `email` added to `components.schemas.User`, documented as **absent rather than `null`** when there is none.
- **`api-rfc.md`** — new §5.8, and the `/auth/me` row in §6.2.

The behaviour is deliberate and the commit message argues it well: an absent key is one less state than `null` versus empty, and chat-only accounts routinely have no email. It is also the **only** field on that schema with this rule — `first_name`, `last_name` and `path` are all nullable — so a client doing `user.email !== null` gets a different answer from `'email' in user`. Flagged in §5.8 rather than "fixed", because consistency is the project's call, not the spec's.

> **A limit worth stating:** the `User` schema also omits `username`, `dob`, `avatar_url` and `display_name`, all of which `toPublicUser` returns. Those are pre-existing gaps, not introduced this cycle, and reconciling them needs a check of whether the response interceptor strips them — which was not done today. Named here so it is not rediscovered as new.

### 3.2 The access-control gap is unchanged, and `beevia-admin` has no CI at all

Re-verified at `origin/main`: `reports.service.ts` still resolves `viewableModules` once at generation (line 133) and never re-applies it at read. No commit touched the file.

Separately, the carried recommendation "add the two org security workflows to `beevia-admin` and `beevia-mobile`" turns out to have understated one half of itself. Checked properly today:

| Repo | `.github/workflows` |
|---|---|
| `beevia-api` | `pr` · `release` · `secrets-scan` · `supply-chain-guard` · `test` |
| `beevia-admin-api` | `ci` · `deploy` · `postman-sync` · `secrets-scan` · `supply-chain-guard` · `sync` |
| `beevia-db-schema` | `ci` · `release` · `secrets-scan` · `supply-chain-guard` · `sync` |
| `beevia-mobile` | `flutter-ci` · `main` · `pr` — missing the two org security workflows |
| **`beevia-admin`** | **no `.github` directory exists** |

`beevia-mobile` is two file copies from parity. **`beevia-admin` has never had CI of any kind** — nothing lints, builds, tests or scans it, and no status check can be required on a pull request because none exists. It is also the repo whose only contributor has no board presence, so neither CI nor the board observes that work. Written up as `suggestions.md` §7.7 and inserted near the top of the suggested order, because "add the two security workflows" cannot be done until there is a `.github/` to put them in.

### 3.3 The working-tree audit still reports 19 phantom drift lines

6 in `beevia-api`, 13 in `beevia-admin-api`, because three repositories remain `diverged` from the 8 September incident and their working trees are still 4 September code. **Ninth consecutive edition flagging it**, so nobody "fixes" the spec by deleting operations that exist at `origin/main`. Every code claim in this report is made against the shadow.

---

## 4. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 14.** 12 items — **8 leaves, 4 parent Stories**. **Zero transitions in the window.**

| Status | Leaves | 15 Sep | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 2 | 2 | 0 |
| Done | 6 | 6 | 0 |

| Owner | Leaves | In progress | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 | 3 |
| Ayomikun Araoye | 3 | 1 | 2 |
| Unassigned | 1 | 0 | 1 |

Nothing moved and no commit landed in `beevia-admin` (2.1 days since `f12135b`). `BVA-I9` — moved to In progress *for* Promise by Ayomikun on 14 September — has sat there since, with no code behind it in the window.

**Promise still has zero self-attributed transitions on this board, across every edition it has existed.** The framing has now cycled through three states: nobody touched his board; then someone else did; now nobody does again. The underlying question — who owns his board state — has not been answered, and §3.2 adds a second reason to care about this repo specifically.

### 4.1 Never summed with the main board

8 leaves here and 21 on sprint 0901 are different projects and different backlogs. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards.

---

## 5. Team performance — detail

All figures from the activity sidecars and git, never `Last Modified`. Commits are trailing-7-day (since 9 Sep 14:04 UTC), merged to the default branch except where stated, summing each person's git identities, excluding bots.

**Ayomikun Araoye — backend + admin API.** **36 commits** in the trailing 7 days across `beevia-api` (20), `beevia-admin-api` (10) and `beevia-db-schema` (6), counting `Phoenixdadhev` and `Ayomikun Araoye` together. Five of those are this window: the `email` field, the Node 24/26 matrix in three repos, and `otp fix`. Zero open WIP. **Nine of the eleven items in REVIEW/QA are his**, including the entire seven-item notification block that is now 7.9 days old — which is a queue problem, not a throughput problem: his submissions are self-reported and land close to the code they describe.

**David Samuel — mobile.** **One merged commit**, and it is the one that mattered: the squash of 40 days of branch work, merged 15 Sep 16:07 UTC (§1.5). Four commits on any ref in the window. **He moved his own board items this morning** — `BVA-I237` and `BVA-I238` to In progress at 11:25:24 UTC — the first self-attributed transitions of his this report has recorded, after four editions of asking. Two open WIP, both on the language work still sitting on the branch; neither exceeds his 2.6-day median cycle.

> The standing concern — *is the mobile board being transcribed by someone other than its owner* — has a positive data point today rather than another negative one. It does not retroactively explain the 14 September bulk move, and the two items that non-contributor sent to REVIEW/QA are still sitting there.

**Philip Chidera — design.** **Completed `BVA-I268` himself** at 11:53:48 UTC — *Design the Transaction Receipt Image*, created 15 Sep 13:58, moved to REVIEW/QA by a non-contributor at 16:09 the same day. It is the first item recorded leaving REVIEW/QA on sprint 0901 and the first thing Philip has closed since 28 August. Its cycle was under 46 hours end to end, which is why it does not tell us anything about the eleven items that have been waiting days (§1.3). One To do item remains (`BVA-I256`, Trust & Safety, unpriced).

**Promise Udo — admin dashboard.** **1 merged commit** in the trailing window, down from 4 purely because the window moved past his 8 September commits — nothing was lost or reverted. Zero board transitions by him, again. No `beevia-admin` commit for 2.1 days, in a repo with no CI (§3.2).

### 5.1 What these figures do not measure

- **They cannot price the merge.** The single most significant commit of the last six weeks counts as "1 commit" and carries 0 estimation points.
- **They say nothing about review quality.** One item has now left REVIEW/QA item-by-item, and it never queued. The eleven that did queue still have no recorded exit route other than a 47-second bulk sweep.
- **They cannot tell who did a board update** except through the sidecar, which is the only place assignee and actor are distinguishable.
- **No estimation points exist on any item, on any of three boards** — 0/64, 0/30, 0/12, confirmed at the raw-field level.
- **Correctness and testing remain out of scope for scoring**, per the owner's 2026-08-07 instruction. Noted anyway, since it cuts the other way for once: the merge brought seven new test files with it.
- **Commit-identity mapping is inference.** `Phoenixdadhev` → Ayomikun and `Davidtariq96` → David are consistent and near-certain, but unconfirmed.

---

## 6. Previous recommendations — where they stand

| Recommendation from 15 Sep | Status on 16 Sep |
|---|---|
| **Merge `origin/BVA-I242`, or explicitly split it** | ✅ **Done — and split, which was the better of the two options offered.** The money half merged as `874697a`; the l10n half remains on the branch (§1.5) |
| Get a human decision on the REVIEW/QA queue before 22 September | ❌ **Not done, and worse.** Same eleven items, median age up to 7.9 d, six days left |
| Ask David whether he made the board moves | ✅ **Effectively answered.** He made two himself this morning (§1.2). The 14 September moves are still unexplained |
| Fix the report read-scoping | ❌ **Not done.** `reports.service.ts` untouched, re-verified |
| Decide what happens to `POST /translate` | ❌ **Not done.** `translate.module.ts:23` still binds `TRANSLATE_PORT` to `StubTranslateAdapter` |
| Add both CI security controls to `beevia-admin` and `beevia-mobile` | ❌ **Not done — and the ask was under-specified.** `beevia-admin` has no CI at all (§3.2) |
| Have Promise make at least one board transition himself | ❌ **Not done.** Zero activity on the admin board this window |
| Price or defer the Trust & Safety scope | ❌ **Not done.** All still To do, 0 points, fourth edition |
| Put estimation points on all three boards | ❌ **Not done.** Eleventh edition asking |
| Move the daily export's sprint filter and cut-off | ❌ **Not done.** `ZOHO_SPRINT_FILTER` re-verified still `08-01`; tenth edition working around it |
| Add the `enabled` flag to the translation preference | ❌ **Not done** |
| Add the route-collision check to CI, on push | ❌ **Not done**, re-verified — no workflow in either backend repo references it |
| Apply the BVN-ordering guard to `POST /kyc/profile` | ❌ **Not done.** The `bvn_required` guard exists, but on `startIdVerification`, not on the profile submission |
| Adopt the Reports truncation pattern in reconciliation | ⚠️ **Not verified this cycle** — no commit touched either file, so presumed unchanged |

**Two of fourteen resolved, and one of them is the one that had been open longest.** This is the first edition in which the top recommendation moved. It is worth noting *how* it moved: not by anyone working through this list, but because the work reached a point where merging was the obvious next step. The list's code-shaped asks — a flag, a CI check, a scope re-apply, several of them a few minutes each — remain untouched for the fifth consecutive edition, which continues to suggest this document is not reaching whoever sequences the day.

---

## 7. What I would do this week

Reordered by remaining time. **Six days left in sprint 0901.**

1. **Decide the fate of the l10n half of `BVA-I242`.** The precedent is set and it worked: split, squash, merge. ~18,200 lines and the on-device translation engine are still on the branch, and `BVA-I229` went back to In progress this morning, so someone is actively working in there. A second squash this week would close the 41-day lineage entirely.
2. **Do for the review queue what was just done for the branch.** Eleven items, 7.9-day median, nine of them Ayomikun's notification block. If the plan is a bulk sweep, say so before 22 September rather than after; if it is item-by-item, `BVA-I268` just showed it takes minutes.
3. **Give `beevia-admin` a CI workflow.** Not the security workflows first — *any* workflow. It is the prerequisite for branch protection, for required checks, and for the two org controls that have been recommended for five editions and are currently impossible to add.
4. **Copy `secrets-scan.yml` and `supply-chain-guard.yml` into `beevia-mobile`.** Two file copies, and that repo just absorbed 7,200 lines in one squash.
5. **Fix the report read-scoping gap** (§3.2). Unchanged for three editions, still a live access-control gap behind a client that consumes it.
6. **Settle the `email`-shaped inconsistency now, while it is one field.** Either make the other optional fields absent-when-empty or make `email` nullable like its neighbours. Doing it before a client ships against the current shape costs nothing.
7. **Decide what happens to `POST /translate`.** The client answered this in practice weeks ago by building on-device translation; the server still binds a stub. One sentence.
8. **Price or defer the Trust & Safety scope.** It cannot ship in 0901 with six days left and no code, so the honest move is to move it out.
9. **Have Promise make one board transition himself**, or agree explicitly that someone else owns his board state. Third distinct variant of this finding.
10. **Put estimation points on all three boards, or state that the project does not estimate.** The merge that just landed is unpriced, which means nobody can say whether 0901 is on track.
11. **Move the daily export's sprint filter to `0901` and the cut-off to ~20:00 UTC.** The 16:07 merge missed yesterday's window by three minutes and was reported a day late as a result — a concrete cost, not a hypothetical one, and the tenth edition of this workaround.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync (**1 repo advanced — `beevia-mobile`, +1 commit; `beevia-admin` already current; 3 refused as `diverged`**) → deterministic audit against the working tree → a second audit against a read-only `origin/main` shadow built with `git archive` → read-only scratch export of sprint 0901 (30 items) → `git log` sweep of every ref across all five repositories for the window → content diff of `origin/main` against `origin/BVA-I242` → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter`, `eslint` or build step ran. No repository was reset, rebased, reverted or cleaned; no sub-repo file was edited; the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed, or deployed.

**Files changed this cycle** (all at the workspace root, none in a sub-repo): `openapi.yaml` (§3.1), `api-rfc.md` (§5.8, §6.2), `suggestions.md` (§5.7, §7.7, §8).

**Degraded inputs.**

- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are still `diverged` from the 8 September incident (each `ahead 1, behind 15/16/9`); `sync_repos.py` correctly refuses to force a merge. Their working trees remain 4 September code, the sole cause of the working-tree audit's 19 phantom drift lines. Every code claim here is made against `origin/main` via a `git archive` shadow.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, a sprint that closed 28 August. The in-repo main export therefore reads a closed, frozen sprint — confirmed zero activity in the window, as expected. All sprint-0901 figures come from a read-only scratch export to `/tmp/beevia-scratch/`. Tenth consecutive edition working around this.
- **The previous edition's window closed three minutes before the merge.** `874697a` landed at 15 Sep 16:07 UTC; the 15 September report's cut-off was 14:04 UTC. That is why the single largest event in six weeks is reported a day after it happened, and it is the concrete cost of recommendation 11.
- **The `Epic` column is blank** on both in-repo boards — a known OAuth scope gap (`ZohoSprints.epic.READ` not granted), not "no epic assigned".
- **`Comments` bodies are unavailable** from the API.
- **The window ends at 14:04 UTC**, so anything after that today is unobserved.
- **The merge was verified by content, not by build.** The squash's file list, the endpoint-constant-to-caller mapping and the socket-command-to-handler mapping were all checked by reading the merged tree. Nothing was compiled or run.
- **Repository integrity was not hash-swept this cycle.**
- **Branch protection, credential rotation and workstation remediation remain unverifiable** from this workspace.
- **No estimation points exist on any of the three boards**, confirmed at the raw CSV value level.
- **The activity sidecars only carry history for items currently on their board.**

**Window.** 15 Sep 14:04 UTC → 16 Sep 14:04 UTC — a normal ~24-hour cadence. All `actiontime` and board figures are UTC; the local export host runs UTC−6.

**Sources.** Boards: `beevia-sprint-board-2026-09-16.csv` (64 rows, 41 leaves, sprint 08-01, unchanged) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-16.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (30 rows, 21 leaves) + activity sidecar. Code: all five repositories at `origin/main` — `beevia-admin`, `beevia-mobile` from the synced working tree; the other three from a `/tmp` `git archive` shadow. Specs: `openapi.yaml` (137), `openapi.proposed.yaml` (38), `openapi.admin.yaml` (47), `openapi.admin.proposed.yaml` (19) — all validated, zero route-level drift against `origin/main`.

**A note on who appears here.** Only people whose work is tracked have rows. Two board actions this edition were made by a non-contributor (`BVA-I268` to REVIEW/QA; and, from the previous window, David's two items) and are reported without naming the actor.

<a id="mvp-method"></a>

### MVP readiness — ≈61% (estimate; 61.40, +3.30)

**Target 2026-09-01 (provisional) · the target date passed fifteen days ago.** On merged build evidence the product moves from **58.10 to 61.40 of 100** — **the first movement in nine editions and the largest single-cycle change this rubric has recorded.** All of it comes from one merge.

Three scores move. Each names the specific evidence, per the rule that a score never rises on "probably done, sitting in review":

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | 0 | Unchanged. The merge touched chat screens and the local message store; no crypto or key-exchange file changed |
| 2 | Voice & video calling | 8 | 0.8 | 0 | Unchanged. Push transport still falls back to a stub without `FCM_SERVICE_ACCOUNT` |
| 3 | Message translation | 7 | 0.30 | 0 | **Unchanged, and this is the half that did not merge.** `translate.module.ts:23` still binds `TRANSLATE_PORT` to `StubTranslateAdapter`; `lib/core/language/on_device_translation_service.dart` exists only on `origin/BVA-I242`; `lib/core/language/` does not exist on `main` |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | 0 | Unchanged |
| 5 | International KYC tier | 6 | 0.0 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | **0.75** | **+0.05** | `wallet_service.dart` doubled its surface: `/wallets/payin-details`, `/wallets/banks`, `/wallets/resolve-account`, `/wallets/withdraw` and `/topups/initialize` are now called from merged client code, with step-up on withdrawal, plus bank-transfer amount/review screens. **Small rise only: the currency dimension did not move** — `PaymentService.activeNgn()` re-verified at four call sites, so every wallet is still NGN |
| 7 | Send / request / receive in chat | 12 | **0.90** | **+0.10** | `chat_send_money_flow.dart` merged and reads the real `WalletProvider`; `payment_events.dart` merged with `payment.request`/`accept`/`decline`/`cancel` matched name-for-name to `messaging.gateway.ts` handlers. **The 2026-08-07 "buttons with a placeholder handler" finding is retired.** Held back from 1.0: no payments read path, `POST /payments/send` and `/payments/{id}/pay` unused by the client |
| 8 | Cross-currency FX | 12 | 0.0 | 0 | Proposed only. `activeNgn()` still hard-codes the currency |
| 9 | Virtual cards | 10 | **0.70** | **+0.15** | Was 0.55 on server-only evidence with **zero client `/cards` references on `main`** — that is now false. `virtual_card.dart`, three card screens and `fetchCards`/issue-card (step-up gated) merged. Held well below 0.9: the client uses **2 of 13** card operations — no freeze, unfreeze, terminate, reveal, fund, withdraw or transactions |
| 10 | Consent management | 4 | 0.0 | 0 | No endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.90 | 0 | Unchanged. No `beevia-admin` or `beevia-admin-api` commit touched a scored module; `beevia-admin` had no commit at all |
| | **Weighted total** | **100** | **61.40** | **+3.30** | **≈61%** |

Weights frozen — **no methodology change this edition**, which matters here: the number rose because merged code changed, not because the rubric did.

Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches. The clearest illustration is in this table — capability #3 sits at 0.30 while a complete four-locale translation layer exists and compiles on a branch, because it is on a branch.

### What this report cannot tell you

- **Whether the l10n half of `BVA-I242` will merge, or be rebuilt.** Now the largest single uncertainty in the estimate, inherited directly from the half that did merge.
- **Whether the merged wallet and card flows work.** They are wired to the right endpoints with the right headers; nothing was built, run or exercised against a server.
- **Whether the eleven items in REVIEW/QA will be reviewed individually, swept, or left.** `BVA-I268` set a precedent for an item that never queued, which is not the same question.
- **Why the 14 September bulk move on David's items was made by someone else**, given that he moved his own items today.
- **Whether `FCM_SERVICE_ACCOUNT` is set in any deployed environment.**
- **Whether any CI workflow has actually run or passed** — run history lives on GitHub, not in the clone. For `beevia-admin` the question does not arise: there are none.
- **Whether the `User` schema's other four undocumented fields are intentional** (§3.1) — that needs a read of the response interceptor that was not done today.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 30, 0 of 12 items estimated.
