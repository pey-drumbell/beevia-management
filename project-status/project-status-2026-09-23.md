# Beevia — Project Status

**As of 2026-09-23** · Sprint **0901** (3 Sep → 22 Sep) — **closed yesterday, still being worked in** · Sprint **0901-admin** (3 Sep → 22 Sep) — closed yesterday · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-23.csv` + `beevia-activity-2026-09-23.json` (64 items, sprint 08-01 — frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-23.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**58 items**) + sidecar in `/tmp/beevia-scratch/`; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. **Window 22 Sep 15:20 UTC → 23 Sep 15:05 UTC — about 1.0 day.**

---

## Quick overview

> **Seven weeks of mobile work landed on `main` this morning in a single merge, and the MVP estimate moves more in one day than in the previous month combined: ≈62% → ≈67%.** PR #35 brought the entire wallet feature module — wallet home, balances, transaction history, p2p and external bank transfers, virtual-card request, notifications, localisation in four languages, and the report-sheet client change — onto `beevia-mobile` `origin/main`. Three findings this report has carried for weeks closed at once: the chat money buttons **now call the payments API** (`POST /payments/transfer`, plus `payment.request/accept/decline/cancel` over the socket, matching the server's gateway handler names exactly); `lib/l10n` and `lib/core/language` **exist on `main`**; and `reportConversation` **now sends the disclosed `messages` and `blockContact`**, so a moderator opening Module 4 will see evidence instead of an empty list. **But sprint 0901 ended yesterday and no successor sprint exists on either board** — the team spent today working inside an expired sprint, which grew by another 12 QA bugs this morning to 49 leaves.

**Correction to the 22 Sep edition — one claim of mine was wrong in substance, and it matters.** That edition scored capability #3 (translation) at 0.30 and said "both branches are unmerged", listing `origin/BVA-I239` and `origin/BVA-I242` as the two candidates. **There was a third branch it never named — `origin/BVA-1239`, spelled with the digit `1` rather than the letter `I`** — and that is the one that merged as PR #35 at 14:58 UTC today. The recommendation "pick one of the two l10n branches" was therefore based on an incomplete branch list. The practical consequence is in §1.6 and is not cosmetic: `origin/BVA-I239` (letter I) is still 3 commits ahead of `main`, and **those three commits are the project owner's own** — a CI disk-space fix and "Fix 7 failing wallet tests broken by two independent gaps". They did not come across in the merge.

**Also carried forward and now resolved:** the 22 Sep edition's "what this report cannot tell you" asked whether David had unpushed mobile work. He did — seven weeks of it, on a branch this report was not tracking.

| Measure | 22 Sep | 23 Sep | Δ (1 day) |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 19 | **24** (23 mobile via PR #35, 1 admin) | +5 |
| Board transitions, all three boards, in window | 20 | **35 entries / 14 status changes** | +15 |
| Items added to sprint 0901 | 11 | **12 — 11 QA bugs + 1 branding Story** | +1 |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 0 |
| Sprint 0901 leaves, total | 37 | **49** | **+12** |
| Sprint 0901 leaves To do | 11 | **12** | +1 |
| Sprint 0901 leaves In progress | 0 | **4** | **+4** |
| Sprint 0901 leaves BLOCKED | 0 | **5** | **+5** |
| Sprint 0901 leaves REVIEW/QA | 20 | **22** | +2 |
| Sprint 0901 leaves Done | 6 | 6 | **0 — fifth edition flat** |
| Review-queue median age (0901) | 8.0 d | **7.2 d** | −0.8 — dilution again (§1.3) |
| Oldest item in the queue | 14.0 d | **14.9 d** | +0.9 |
| `beevia-mobile` `main` days since a commit | 7.0 | **0.0** | **−7.0** |
| `beevia-admin` `main` days since a commit | 1.0 | 0.9 | |
| `beevia-admin-api` days since a commit | 1.0 | 2.0 | |
| `beevia-api` / `beevia-db-schema` days since a commit | 3.9 / 3.9 | **4.8 / 4.8** | |
| Admin board: days since *any* activity | 8.0 | **9.0** | +1.0 |
| Ayomikun commits (7d, both identities, merged, non-merge) | 29 | **21** | rolling window |
| David commits (7d, merged to `main`) | 1 | **4** | +3 |
| Promise commits (7d, merged) | 1 | **2** | +1 |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 46 · 0 / 12 · 0 / 64 | **0 / 58 · 0 / 12 · 0 / 64** | 0 |
| **Sprints open on either board** | 2 | **0** | **−2** |
| MVP readiness (estimate) | ≈62% (61.70) | **≈67% (66.72)** | **+5.02** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **15 on 0901 — all 15 REVIEW/QA** · 3 on 0901-admin · co-assigned on 6 new QA bugs | 6 (3 self-moved) | 1.77 d (n=4) | **0** solely-owned · 1 on 0901-admin (`BVA-I8`, 9.0 d) · co-owns 4 of today's blocked/in-progress bugs | **21** | Everything solely his on 0901 is still waiting on review, unchanged for a fifth edition. Four of today's five BLOCKED bugs are co-assigned to him and were blocked *pending backend input* |
| David Samuel | mobile | **23 on 0901** — 7 REVIEW/QA, 9 To do, 3 In progress, 2 BLOCKED, 2 Done | 5 | 6.16 d (n=5) | **3 In progress + 2 BLOCKED**, all opened today | **4** | **Back, and decisively.** PR #35 ended a 7-day `main` silence with seven weeks of work. **First edition in which he self-moved his own items** — 11 self-attributed transitions today vs 0 on 22 Sep |
| Philip Chidera | design | 4 on 0901 — all Done | 0 | — | 0 | — | Fourth edition with an empty board, and now **eight** "doesn't match Figma"-class bugs across the two QA batches. Design sign-off looks like the unstaffed step |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, 9.0 d) | **2** | Shipped the wallets module (`0b41e35`, 939 lines, with tests). Still zero self-attributed board actions anywhere; the admin board has not moved in 9 days |

**The two questions for standup:** (1) **There is no open sprint on either board — what is 0902 and when does it start?** The team worked all of today inside a sprint that ended yesterday; every figure in §1 describes an expired container. (2) **Who merges `origin/BVA-I239`'s three commits?** They are the owner's wallet-test and CI fixes, they are not on `main`, and the near-identical branch name that *did* merge makes them very easy to lose.

**The three things worth knowing:**

1. **The mobile client stopped being a screen inventory and became a wired product.** `lib/features/wallet/` now exists on `main` with 12 screens and a `wallet_service.dart` that calls `GET /wallets`, `GET /wallets/transactions`, `GET /wallets/banks`, `POST /wallets/withdraw`, `GET /payments/recent-recipients`, `POST /payments/transfer` and `GET /cards` through the real `networkService`. The request/accept/decline/cancel half runs over the socket, and the client's constants in `socket_constant.dart:38-42` are the same four strings as `messaging.gateway.ts:428-452`. **The 7 August finding — "Send money / Request money buttons with a local placeholder handler and zero calls to the payments API" — is closed**, forty-seven days after it was first written.

2. **Translation shipped, but not the translation that was specified.** `lib/core/language/on_device_translation_service.dart` uses ML Kit's `OnDeviceTranslator` on the handset; `lib/l10n` carries generated bundles for en/es/fr/zh. Meanwhile `beevia-api` `translate.module.ts:23` still binds `StubTranslateAdapter`, and `openapi.proposed.yaml` still carries `/translate/batch` and `/translate/languages` as proposals. The only server endpoint the client uses is `/translate/preferences`. **This is an architecture decision that has now been made in code without being made on paper** — and it is a good one for latency and for E2EE (no plaintext leaves the device), but §7's "decide what happens to `POST /translate`" is now overdue rather than pending, and two of this morning's bugs (`BVA-I282` re-translating every message on every open, `BVA-I285` static labels not translating) are its first cost.

3. **Both boards are expired and the work has not stopped.** Sprint 0901 ended 22 Sep; 0901-admin ended 22 Sep; the only sprints Zoho reports for the two projects are `0901, 08-01, 0702, 0701` and `0901-admin`. Nothing succeeds them. Today the closed sprint absorbed 12 more items, saw 14 status changes, and ended with 4 In progress and 5 BLOCKED. Whatever the next sprint is called, it does not exist yet, and every item now moving is moving inside a container whose dates are in the past.

**If you read nothing else:** the single biggest product day this project has recorded, and the board it happened on closed yesterday. Done on sprint 0901 is still 6 of 49.

---

## 1. Sprint 0901 — closed 22 Sep, still the working board

### 1.1 State

**58 items — 49 leaves, 9 parent Stories.** Twelve leaves added since yesterday; none removed. **The sprint ended yesterday.**

| Status | Leaves | 22 Sep | Δ |
|---|---:|---:|---:|
| To do | **12** | 11 | +1 |
| In progress | **4** | 0 | **+4** |
| BLOCKED | **5** | 0 | **+5** |
| REVIEW/QA | **22** | 20 | +2 |
| Done | 6 | 6 | **0** |

| Item type | Leaves |
|---|---:|
| Story | 15 |
| Task | 15 |
| **Bug** | **19** |

| Epic | Leaves |
|---|---:|
| `Language` | 10 |
| `Notification` | 7 |
| `security` | 5 |
| (none) | 27 — the 22 QA bugs plus 5 earlier items; genuinely unassigned |

**Bugs are now 39% of the sprint's leaves.** On 18 September there were none. The board has, in five days, gone from a feature sprint to a defect sprint without a sprint boundary in between.

### 1.2 Who moved what — and the flow reversal

Thirty-five activity entries in the window across 20 items. **Eleven of the fourteen status changes were made by the assignee** — the first edition where that is true. On 22 Sep, every one of twenty was made by a board administrator.

| Time (UTC) | Item(s) | Transition | By |
|---|---|---|---|
| 22 Sep 17:16–17:17 | `BVA-I262`, `BVA-I266`, `BVA-I267` | To do → In progress | board administration |
| 22 Sep 17:20 | `BVA-I259` | To do → In progress → REVIEW/QA | board administration |
| 22 Sep 17:20 | `BVA-I257` | To do → REVIEW/QA | board administration |
| 23 Sep 08:23–08:59 | `BVA-I274`–`BVA-I285` (12) | created, Backlog → **0901** | board administration |
| 23 Sep 10:55 | `BVA-I266` | In progress → **BLOCKED** | **David Samuel** |
| 23 Sep 10:58 | `BVA-I263` | To do → In progress | **David Samuel** |
| 23 Sep 10:58 | `BVA-I275` | To do → **BLOCKED** | **David Samuel** |
| 23 Sep 11:05 | `BVA-I279` | To do → **BLOCKED** | **David Samuel** |
| 23 Sep 11:06 | `BVA-I280` | To do → **BLOCKED** | **David Samuel** |
| 23 Sep 11:07 | `BVA-I260` | To do → **BLOCKED** | **David Samuel** |
| 23 Sep 11:10 | `BVA-I261` | To do → In progress | **David Samuel** |

Five comments were also posted, all by David, all substantive: a note that face-verification liveness was descoped on a call (`BVA-I260`), a recollection of the business rule behind the swapped profile pictures (`BVA-I275`), two requests for screenshots (`BVA-I276`, `BVA-I277`), and a routing note that the missing-contacts bug is backend work (`BVA-I279`).

**This is the healthiest single day of board behaviour this report has recorded** — triage, routing, and explicit blocking, by the person doing the work. It is also the day the sprint it happened in was already over.

### 1.3 The review queue — 22 items, still nothing has ever left by review

| Age | Items |
|---|---|
| **14.9 d** | `BVA-I246`–`BVA-I252` — the seven-item Notification block, unchanged since 8 Sep 16:02 |
| 13.2 d | `BVA-I231` Preference Storage & Precedence Logic |
| 9.0 d | `BVA-I245` Backend String Bundles & Selection Logic |
| 8.9 d | `BVA-I233` Build Both Screens · `BVA-I243` String Extraction & Bundle Switching |
| 5.4–5.5 d | `BVA-I254` · `BVA-I255` · `BVA-I270` · `BVA-I271` |
| 4.9 d | `BVA-I269` · `BVA-I272` · `BVA-I273` |
| 1.9 d | `BVA-I229` · `BVA-I238` |
| 0.9 d | `BVA-I257` · `BVA-I259` |

Median **7.2 d** (n=22), down from 8.0 — **for the third consecutive edition, by arrival rather than by review.** The twenty items that were in the queue yesterday are each a day older; on their own their median is 8.9 d. **Fifteen of the twenty-two are Ayomikun's, and he has nothing else solely assigned on the sprint.**

**What changed underneath the queue, though, is real:** `BVA-I229` (Translation Engine Integration), `BVA-I238` (Auto-Translation Display), `BVA-I233`, `BVA-I243` and `BVA-I254` (report sheet) **now have merged code on `main` behind them**. Yesterday's finding — "three of David's five review items have nothing on `main`" — is resolved by the merge, not by a board move. Every item in the queue is now, for the first time, actually reviewable.

### 1.4 What shipped — PR #35

`4b9c00c`, merged 23 Sep 14:58 +0100, brought 23 commits dating back to 6 August onto `beevia-mobile` `origin/main`:

| Landed | Evidence on `main` |
|---|---|
| Wallet feature module | `lib/features/wallet/` — 12 screens, 7 models, `wallet_provider.dart`, `wallet_service.dart` |
| Live wallet + payments wiring | `wallet_service.dart:14,21,30,53,166` → `GET /cards`, `GET /wallets`, `GET /wallets/payin-details`, `GET /payments/recent-recipients`, `POST /payments/transfer` |
| In-chat money, end to end | `chat_details.dart:1630` `_sendMoneyToPeer` → `showChatSendMoneyFlow` → `WalletProvider` → transfer; `payment_events.dart:92` emits `payment.request` with ack and listens on `payment.updated` |
| Socket contract match | `socket_constant.dart:38-42` vs `messaging.gateway.ts:428-452` — `payment.request/accept/decline/cancel`, identical strings |
| Localisation | `lib/l10n/` — `app_en/es/fr/zh.arb` + generated bindings; `lib/core/language/` — provider, settings service, on-device translator |
| Report evidence | `chat_service.dart` `reportConversation` now posts `{reason, messages, blockContact}` — matching `conversations.controller.ts:160-172`, which has accepted all three since it was written |
| Virtual card request flow | `request_virtual_card_screen.dart`, `review_card_request_screen.dart`, `card_request_success_screen.dart`, `virtual_card.dart` |
| Notifications, transfers, history | `notifcations`, `p2p money transfers`, `transaction history`, `external bank transfer screens` commits (6 Aug – 2 Sep) |

Screen inventory: **51 screen files**, up from ~39 at the 7 August baseline.

`beevia-admin` also advanced: `0b41e35` (22 Sep 16:54, Promise Udo) added the wallets dashboard module — `wallets-summary.tsx`, `wallets-table.tsx`, `virtual-account.tsx`, an expanded `src/features/wallet/api.ts`, and **an expanded `wallet-section.test.tsx`**. 939 insertions across 15 files.

### 1.5 The five BLOCKED items — what they are waiting on

| Item | Blocked on | Note |
|---|---|---|
| `BVA-I260` Face verification shows static placeholder | A product decision | David's comment says liveness checking was descoped on a call; the item may be invalid rather than blocked |
| `BVA-I266` Correct PIN triggers error modal | Backend | Co-assigned to Ayomikun |
| `BVA-I275` Sender/receiver profile pictures swapped | A business-rule clarification | David recalls a deliberate rule; needs confirming |
| `BVA-I279` Existing contacts missing from New Chat list | Backend | Explicitly routed: "This is for Backend" |
| `BVA-I280` Conversations list shows empty chats / wrong preview | Backend | Co-assigned to Ayomikun |

**Three of five are waiting on backend work that has no board item of its own.** Ayomikun is co-assigned but every one of his own 15 items is in review, so nothing represents this work in the sprint's In-progress column.

### 1.6 The branch-name collision — `BVA-1239` vs `BVA-I239`

`beevia-mobile` has 15 remote branches. Three are l10n-adjacent, and two of the names differ by one character:

| Branch | Ahead of `main` | Contents |
|---|---:|---|
| `origin/BVA-1239` (digit one) | merged as PR #35 | the seven weeks of work described above |
| `origin/BVA-I239` (letter I) | **3** | `92d86f1` "ci: free runner disk space before Android builds"; `7ed6d1e` "Fix 7 failing wallet tests broken by two independent gaps"; `1f5fffd` merge of PR #33 — **all three authored by Victor Peynado, 22 Sep** |
| `origin/BVA-I242` | 0 | fully contained in `main` — effectively retired by the merge |

`git diff origin/main origin/BVA-I239` is 35 files, +595/−1333. **The owner's own test and CI fixes are the only l10n-branch work that did not land**, and they are sitting behind a name one keystroke away from the branch that did. Nine Dependabot branches and `origin/deps-updates-2026-09-22` (0 ahead of `main`) remain open.

---

## 2. Admin dashboard board — `0901-admin`

**12 items — 8 leaves, 4 parents. No change of any kind since 14 September (9.0 days).**

| Status | Leaves | 22 Sep | Δ |
|---|---:|---:|---:|
| Done | 6 | 6 | 0 |
| In progress | 2 | 2 | 0 |

| Assignee | Leaves |
|---|---:|
| Promise Udo | 4 (3 Done, 1 In progress — `BVA-I9`, 9.0 d) |
| Ayomikun Araoye | 3 (Done) |
| Unassigned | 1 |

Its sprint **also closed on 22 September**, and the project reports no successor. Zero activity entries in the window.

**The board's blind spot has inverted rather than closed.** Promise now has a row, sourced from a real board — but that board has been static for nine days while `beevia-admin` received two commits in the same period, including the 939-line wallets module. The board is no longer *absent*; it is *stale*, which reads identically to a stalled workstream and is not one. Twenty editions of this report asked for a board; the board now needs someone to move items on it.

---

## 3. API surface and spec drift

**Clean.** `beevia-api` 137 routes in code, 137 in `openapi.yaml`. `beevia-admin-api` 49 / 49. All four spec files pass health checks; no `x-beevia-*` markers; no broken `$ref`s, orphaned components or duplicate `operationId`s. Proposed: 38 consumer, 18 admin.

**No spec edit was needed this cycle**, and that is itself the expected result: the day's 24 commits were 23 in `beevia-mobile` (a client, which contributes no routes) and 1 in `beevia-admin` (a Next.js dashboard, likewise). `beevia-api` has not moved since 18 September and `beevia-admin-api` since 21 September. The sync report said as much before the audit ran — "No controller/DTO/schema files touched".

Two contract observations that are *not* drift but are worth recording:

- **`POST /conversations/{id}/report` is now fully exercised.** The server has accepted `messages` (≤20 disclosed plaintexts) and `blockContact` since the operation was written; until today the client sent neither. The spec was right and the client has caught up — no change required.
- **`/translate/batch` and `/translate/languages` remain proposed, and the client has routed around them** (§ Quick overview, item 2). They are not drift today, but they are now proposals that a shipped design has bypassed. A decision is owed; see §7.

---

## 4. PRD gap

Unchanged in structure: the four MVP gaps are **cross-currency FX, international KYC tier, consent management**, and — now materially narrower — **multi-currency wallets**.

`PaymentService.activeNgn()` is still present at `beevia-api/src/payments/payment.service.ts:506` and is still called from three places (lines 70, 128, 288). **While it exists, FX is not started**, regardless of what the client can now display. `/fx/rates`, `/fx/quotes` and `/fx/quotes/{quoteId}` remain in `openapi.proposed.yaml` only. What changed today is the *client* half of capability #6: there is now a wallet home, balance and transaction history beyond onboarding setup. The server still speaks one currency.

Consent management remains at zero: no endpoint, no record, no board item, in any of the three boards.

---

## 5. Team performance — detail

### 5.1 The figures

| Person | Submissions to REVIEW/QA (7d) | Self-moved | Median cycle (In progress → REVIEW/QA) | Open WIP | Commits (7d, merged, non-merge) |
|---|---:|---:|---|---|---:|
| Ayomikun Araoye | 6 | 3 | **1.77 d** (n=4: 1.44, 1.52, 2.01, 4.19) | 0 solely-owned on 0901; `BVA-I8` on 0901-admin, 9.0 d; co-owner of 4 bugs opened today | **21** — `beevia-api` 9, `beevia-admin-api` 7, `beevia-db-schema` 5 |
| David Samuel | 5 | 0 | **6.16 d** (n=5: 0.0, 5.2, 6.16, 7.0, 10.0) | **5** — 3 In progress, 2 BLOCKED, all opened today | **4** (`Davidtariq96`) |
| Philip Chidera | 0 | — | — | 0 | — (no repo) |
| Promise Udo | 0 | — | — | 1 (`BVA-I9`, 9.0 d) | **2** (`beevia-admin`) |

Commit counts sum each person's git identities (§ Git identities in the skill): Ayomikun as `Phoenixdadhev` + `Ayomikun Araoye`, David as `Davidtariq96` + `David Samuel`. Bot and `semgrep.dev` commits are excluded; three `github-actions[bot]` release commits in `beevia-db-schema` and four `semgrep.dev` commits are not attributed to anyone.

### 5.2 Per person

**Ayomikun Araoye.** Twenty-one merged commits across three backend repos in seven days, and a cycle time under two days on everything he moves. All fifteen of his solely-owned sprint items are in REVIEW/QA and have been for between 4.9 and 14.9 days. He is not blocked on himself. **He also became, today, the implicit owner of three of the five newly-blocked mobile bugs** — backend work that arrived via co-assignment, with no item of its own and no place in the sprint's In-progress column. Neither `beevia-api` (4.8 d) nor `beevia-db-schema` (4.8 d) has had a commit since 18 September; `beevia-admin-api` last moved 21 September.

**David Samuel.** The seven-day `main` silence this report flagged on 22 September ended at 14:58 today with seven weeks of work. His 6.16-day median cycle is a direct artefact of that: work sat on a branch while the board tracked it as In progress. **Today is also the first day he moved his own items** — eleven self-attributed transitions, five substantive comments, and five items explicitly triaged into In progress or BLOCKED rather than left in To do. Three of his blocks route to backend; one questions whether the bug is valid at all. This is the behaviour the last six editions have been asking for, and it appeared the day after the sprint ended.

**Philip Chidera.** Four Done items, nothing open, no submissions, no repo, fourth consecutive edition with an empty board. There are now **eight** bugs across the two QA batches of the "doesn't match the approved Figma" kind (`BVA-I284` search-icon size is the clearest example), plus `BVA-I274` "App Logo and Branding", created this morning and **the only unassigned leaf on the sprint**. Design has the most obviously matching skill set and no board presence. This is a question, not a finding: is he working untracked, finished, or waiting?

**Promise Udo.** Two commits in seven days and the wallets dashboard module, complete with a test file. Zero board actions anywhere, on any board, ever. The admin board has been frozen for nine days across the exact window in which he shipped 939 lines. **Absence of board data is not absence of work** — this is the twentieth edition making that statement, and the first in which a board exists that could have carried the evidence and did not.

### 5.3 Weekly submission trend (sprint 0901, transitions into REVIEW/QA)

| Window | Submissions |
|---|---:|
| 8 Sep (the Notification block) | 7 |
| 10–14 Sep | 4 |
| 15–18 Sep | 5 |
| 18–22 Sep | 5 |
| 22–23 Sep | 2 |
| **Accepted / Done in any of them** | **0** |

Steady input, zero acceptance, for three weeks. **The bottleneck is not the developers.** No item has left REVIEW/QA by review on this board in its entire lifetime, and Done has been 6 since before the 15 September edition.

### 5.4 What this does not measure

- **Nothing on any of the three boards is estimated** — 0 of 58, 0 of 12, 0 of 64. There is no workload normalisation, so a raw item count says nothing about who is carrying more. David has 23 leaves and Ayomikun 15; that comparison is meaningless without points.
- **Commit counts reward small commits.** PR #35 is 23 commits and seven weeks; `0b41e35` is one commit and 939 lines. Neither number measures difficulty.
- **Cycle time here measures board hygiene as much as work.** David's 6.16-day median largely reflects long-lived branches, not slow implementation — the code was written continuously and merged once.
- **Correctness and testing are out of scope by standing instruction.** Nothing in this report claims the wallet flow *works*; it claims the screens exist, match the designed flow, and reach the real API. Twenty-two open QA bugs suggest the gap between those two statements is currently wide.
- **No individual is responsible for the review queue.** Fifteen of 22 items belong to one person who cannot review his own work. That is a process gap.

---

## 6. Previous recommendations — where they stand

| Recommendation from 22 Sep | Status on 23 Sep |
|---|---|
| **1. Decide the fate of the 20 review items at the sprint boundary** | ❌ **Not done — and the boundary has now passed.** The sprint closed with the queue intact; it is 22 today, in a sprint that no longer runs. Seventh edition |
| **2. Only move an item to REVIEW/QA when there is a merge to review** | ✅ **Resolved by the merge.** All 22 queue items now have code on `main` behind them (§1.3). Worth keeping as a rule — it was luck of timing, not a policy change |
| **3. Merge one l10n branch, then ship the report-sheet client change** | ✅ **Both done, in one merge** (§1.4). The highest-value engineering on the board, landed |
| **4. Plan the 11 QA bugs into the next sprint; triage `BVA-I260`/`BVA-I267` first** | 🟡 **Triaged, not planned.** Both named items were triaged today — `I267` to In progress, `I260` to BLOCKED with a comment that liveness was descoped. But there is no next sprint to plan them into, and 12 more arrived (§1.1) |
| **5. Confirm branch protection / secret scanning / Dependabot in the GitHub UI** | ❌ Not done, still unobservable from here. `BVA-I269`/`I272`/`I273` sit at 4.9 d in review with no comments |
| **6. Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`** | ❌ Not done. `beevia-mobile` took 23 commits today and none of them was this. Nine Dependabot branches still open, oldest now 43 days |
| **7. Restore or deliberately retire `beevia-api/docs/`** | ❌ Not done. `docs/` is still absent from `origin/main`. Note the mobile side shipped without `mobile-integration-handoff.md` — so it is now demonstrably retirable, but the decision should be explicit |
| **8. Put the Module 4 dashboard on the admin board** | ❌ Not done. The board is now nine days static (§2) |
| **9. Extend `openapi-schema.spec.ts` to diff against the committed spec** | ❌ Not done, untouched since `75ab35b` |
| **10. Fix the report read-scoping gap** (`reports.service.ts`) | ❌ Not done — `beevia-admin-api` has no commit since 21 Sep. Eleventh edition |
| **11. Estimation points, `POST /translate`, Module 4 decision record** | ❌ None done. **`POST /translate` escalates** — the client now translates on-device, bypassing it (§ Quick overview, item 2) |
| **12. Move `ZOHO_SPRINT_FILTER` to the next sprint's name** | ❌ **Not done, and now impossible** — still `08-01`, and no successor sprint exists to point it at (§7.1) |

**Three of twelve resolved, and all three by the same merge.** Every remaining item is a decision, a review, a sprint, or a board action — none of them is code nobody has written.

---

## 7. What I would do this week

1. **Open sprint 0902 on both boards today, and decide the queue as you do it.** There is no open sprint anywhere; work is accumulating in an expired one. The 22 review items and 22 QA bugs both need a container with dates in the future, and the sprint boundary was the moment this report spent six editions asking you to use for the queue. It passed yesterday; opening the next sprint is the second-best moment.
2. **Merge or cherry-pick `origin/BVA-I239`'s three commits** — the owner's own "Fix 7 failing wallet tests" and the Android CI disk-space fix. The wallet code they test is now on `main`; the tests are not. Then delete `BVA-I239` and `BVA-I242` so the `BVA-1239`/`BVA-I239` collision cannot cost anyone a day.
3. **Review something.** Twenty-two items, every one now backed by merged code, median 7.2 days, oldest 14.9. The seven-item Notification block (`BVA-I246`–`I252`) is the obvious first sitting: one author, one subject, submitted together on 8 September. Nothing has ever left this queue by review, on any board, in the project's history.
4. **Write down the translation decision.** On-device ML Kit translation is shipped and is arguably the right answer under E2EE. Say so, then either retire `/translate/batch` and `/translate/languages` from `openapi.proposed.yaml` and replace `StubTranslateAdapter` with a deletion, or state what server-side translation is still for. `BVA-I282` (re-translates on every open) is a caching decision that belongs in the same note.
5. **Give the three backend-routed bug blocks their own items and an owner.** `BVA-I266`, `BVA-I279`, `BVA-I280` are blocked on backend work that is invisible in the sprint — co-assignment is not a task. Ayomikun currently has zero In-progress items and three implicit ones.
6. **Pull Philip onto the eight Figma-mismatch bugs and `BVA-I274`** (App Logo and Branding — created this morning, still unassigned, and the only unowned leaf). Fourth edition with an empty design board while design-shaped work accumulates.
7. **Put Promise's two commits on the admin board.** Nine days static while the wallets module shipped. The board now exists; the argument that the work is invisible no longer holds, but only if someone moves items on it.
8. **Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`.** One four-line file each. `beevia-mobile` just took seven weeks of unscanned wallet and payments code onto `main` — this is the moment it matters most. Then close or merge the nine Dependabot branches.
9. **Confirm branch protection, secret scanning and Dependabot in the GitHub UI**, and comment on `BVA-I269`/`I272`/`I273` naming the covered repos. Fifth edition; this workspace cannot see it.
10. **Estimation points on sprint 0902 as it is created.** Fifteenth edition. Twenty-two bugs of wildly different sizes have just entered the project and there is no way to size the next sprint against them.
11. **Carried, unchanged:** `openapi-schema.spec.ts` diffing the committed spec; the `reports.service.ts` read-scoping fix; the Module 4 A-then-B decision record; restoring or retiring `beevia-api/docs/`.

---

## Appendix — method and readiness rubric

### MVP readiness — ≈67% (estimate; 66.72, +5.02)

**Target 2026-09-01 (provisional) · the target date passed twenty-two days ago.** Weights frozen — **no methodology change this edition.** Scores measure build, not acceptance: the review queue has accepted nothing, and none of the movement below has been reviewed by anyone.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No change to `beevia-api` crypto, keys or sockets; PR #35 touched the chat UI, not the crypto layer |
| 2 | Voice & video calling | 8 | 0.80 | 0 | `beevia-api` unchanged since 18 Sep; `FCM_SERVICE_ACCOUNT` still optional and blank |
| 3 | Message translation | 7 | **0.60** | **+0.30** | **Named evidence:** `lib/l10n/app_{en,es,fr,zh}.arb` + generated bindings and `lib/core/language/on_device_translation_service.dart` (ML Kit `OnDeviceTranslator`) on `main` via `4b9c00c`; `translate_chat_screen.dart` routed; `/translate/preferences` wired at `api_url.dart:51`. **Held back:** server `translate.module.ts:23` still binds `StubTranslateAdapter`, `/translate/batch` and `/translate/languages` still proposed-only, and the shipped design bypasses both |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No API change. The onboarding flow was already scored; `BVA-I257`/`I260` are correctness findings, explicitly out of scope for scoring |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | **0.85** | **+0.10** | **Named evidence:** `lib/features/wallet/` on `main` — wallet home, balances, `transaction_history.dart`, `add_money_screen.dart`, bank transfer and withdraw screens, all calling `GET /wallets`, `/wallets/transactions`, `/wallets/banks`, `POST /wallets/withdraw` via `networkService`. The rubric's third clause (a wallet surface beyond onboarding setup) is now satisfied. **Held back:** `activeNgn()` re-verified at `payment.service.ts:506`, called from lines 70/128/288 — the server is still single-currency |
| 7 | Send / request / receive in chat | 12 | **0.95** | **+0.05** | **Named evidence:** the 7 Aug wired-vs-stub finding is closed. `chat_details.dart:1630` → `showChatSendMoneyFlow` → `POST /payments/transfer` (`wallet_service.dart:166`); `payment_events.dart:92` emits `payment.request` with ack, and `socket_constant.dart:38-42` matches `messaging.gateway.ts:428-452` exactly for request/accept/decline/cancel/updated. **Held back:** no REST read path for a single payment |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only; `activeNgn()` confirmed present |
| 9 | Virtual cards | 10 | **0.80** | **+0.10** | **Named evidence:** `request_virtual_card_screen.dart`, `review_card_request_screen.dart`, `card_request_success_screen.dart`, `models/virtual_card.dart` on `main`; `GET /cards` wired at `wallet_service.dart:14`. **Held back:** only the list operation is wired — `reveal`, `reveal-pin`, `freeze`, `unfreeze`, `terminate`, `fund`, `withdraw`, `transfers` exist in `openapi.yaml` with no client constant |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | **0.97** | **+0.02** | **Named evidence:** `beevia-admin` `0b41e35` — wallets module (`wallets-summary.tsx`, `wallets-table.tsx`, `virtual-account.tsx`, expanded `features/wallet/api.ts`), 939 lines with an expanded `wallet-section.test.tsx`. **Held back:** no enforcement link, no prior-report counters, still no CI on the dashboard repo |
| | **Weighted total** | **100** | **66.72** | **+5.02** | **≈67%** |

**The largest single-edition move this report has recorded, and it is a merge, not a month of work.** Four capabilities moved because code that had existed on a branch since early August became observable on `main`. Nothing here was reviewed, tested by this pipeline, or run: the score measures that the designed flow exists in merged code and reaches the real API. The 22 open QA bugs are the counterweight, and they are not in this number.

### What this report cannot tell you

- **What the next sprint is called or when it starts.** Zoho lists `0901, 08-01, 0702, 0701` for Beevia and `0901-admin` for Beevia Admin Dashboard. Nothing is open.
- **Whether any of the merged wallet, payments or translation code works.** No `flutter`, `npm` or `node` command was run; nothing was built or executed. Twenty-two open QA bugs are the only functional signal, and they predate the merge.
- **Whether branch protection, secret scanning and Dependabot are actually on**, and on which repos — the `gh` token here gets `404` on every repo's rules endpoint.
- **Whether the three commits on `origin/BVA-I239` were deliberately left behind** or lost to the branch-name collision.
- **Whether `BVA-I260` is a valid bug.** David's comment says liveness was descoped on a call; no written decision exists to check against.
- **Velocity for any of the three sprints** — 0 of 58, 0 of 12, 0 of 64 items estimated.
- **Whether Philip is working untracked**, and whether the eight Figma-mismatch bugs are waiting on him.

### Method

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, exit 0) → admin board export with `--sprint 0901-admin` (12 items, exit 0) → read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/` (58 items, exit 0) → fast-forward sync (**2 repos advanced — `beevia-mobile` +23, `beevia-admin` +1; 3 refused as `diverged`**; exit 0) → audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow` (clean, exit 0) → item-by-item diff of today's 0901 scratch export against the 22 Sep one → activity-sidecar sweep for the window → content reads of the merged mobile wallet, payments, l10n and report paths against the `beevia-api` controller and gateway → this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages are the `actiontime` of each item's last transition into `REVIEW/QA`; cycle times are `In progress` → `REVIEW/QA` pairs; WIP ages are the entry into the current status.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran; no repository was reset, rebased or cleaned; no sub-repo file was edited; the sync's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-23.html`, `web-report/index.html`; new board exports for 23 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`. **All four OpenAPI specs and all three narrative documents needed no change** — the audit was clean and the day's commits touched no controller, DTO or schema.

**Degraded inputs.**

- **No open sprint on either board.** Sprint 0901 and 0901-admin both closed 22 September with no successor. Every sprint figure in this report describes an expired container that is still being worked in.
- **Three repositories remain unsynced** — `beevia-api`, `beevia-admin-api`, `beevia-db-schema` still `diverged` since 8 September (`ahead 1`, behind 38 / 32 / 23). Every backend code claim is made against `origin/main` via the shadow.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, zero activity). All sprint-0901 figures come from the scratch export. The filter cannot be corrected until a new sprint exists.
- **GitHub settings are unobservable.** Branch protection, secret scanning, push protection and Dependabot alerts are reported from the board and commit messages only.
- **Whether any CI run passed is unknowable from a clone.**
- **`Comments` bodies are unavailable** from the Zoho API (`commentCount` only). Today's five comments are visible in the activity sidecar's `display` field, truncated.
- **The export's "no source key" warning fired on `Epic` again** and is the known 50-row sampling artefact. The column resolves on sprint 0901: 22 of 49 leaves carry an epic; the 27 blanks are genuinely unassigned (22 of them QA bugs).
- **Repository integrity was not hash-swept this cycle.**

**Window.** 22 Sep 15:20 UTC → 23 Sep 15:05 UTC. All `actiontime` and board figures are UTC; `git log` was read with local timestamps converted where quoted.
