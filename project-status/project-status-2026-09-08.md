# Beevia — Project Status

**As of 2026-09-08** · Sprint **0901** (3 Sep → 22 Sep) — **day 6** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-08.csv` + `beevia-activity-2026-09-08.json` (64 items, sprint 08-01), a read-only scratch export of sprint 0901 (25 items), and all five repos inspected at both local `main` and `origin/main`.

Scope: both sprints, kept separate. Window 7 Sep 14:00 UTC → 8 Sep 14:00 UTC — one working day, the first clean 24-hour window in a week.

---

## Quick overview

> **The compromise has been remediated on `main`, and it was done properly — all three repositories now carry a byte-identical clean `eslint.config.mjs`, and a full history sweep finds the payload nowhere on `origin/main` in any of the five repos. It is not finished. Eight `beevia-admin-api` feature branches still carry the malware, one of them touched by an automated Copilot agent yesterday, and merging any of them puts it straight back on the branch that was just cleaned. Separately, two of this pipeline's standing claims turned out to be wrong: sprint 0901 is not blocked on a translation provider, and David has not stopped working.**

| | 7 Sep | 8 Sep | Δ |
|---|---:|---:|---:|
| Repos with a compromised `origin/main` | **3** | **0** | **−3** |
| `beevia-admin-api` branches still carrying the payload | not measured | **8** | new |
| Sprint 0901 leaves To do | 14 | **13** | −1 |
| Sprint 0901 leaves In progress | 3 | **4** | +1 |
| Sprint 0901 board transitions (window) | 11 | 2 | −9 |
| Days since anything entered REVIEW/QA | 10 | **11** | +1 |
| Estimation points set (0901) | 0 / 25 | **0 / 25** | 0 |
| Sprint 08-01 (closed) | 41 leaves, all Done | unchanged | 0 |
| API surface (consumer / admin) | 131 / 35 | 131 / **37** | 0 / **+2** |
| Admin spec modules with something built | 5 of 8 | 5 of 8 | 0 |
| `beevia-admin` modules on the live API | 5 of 10 | **6 of 10** | **+1** |
| `beevia-admin` modules still mock-only | 2 | 2 | 0 |
| MVP readiness (estimate) | ≈56% | **≈56%** | +0.4 pt |

**Team, at a glance:**

| Person | Owns | 0901 leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---:|---:|---:|---|---:|---|
| Ayomikun Araoye | backend + admin API | 9, **all To do** | 4 | 3.0 d | — | **20** | Rebuilt the three poisoned branches this morning (§0). Nine 0901 leaves untouched for a 5th day |
| David Samuel | mobile | 6 — **3 In progress** | 3 | 2.6 d | 3; ages 3.9 d ×2, 0.1 d | 0 to `main`, **3 on `BVA-I192`** | Started two items himself today. `beevia-mobile` `main` untouched **13 days**; `BVA-I192` now **14 commits** unmerged under a Done item |
| Philip Chidera | design | 2 — 1 In progress | 2 | 0.9 d | 1, age **3.9 d** | — | WIP is 4× his own median. No board action since Friday |
| Promise Udo | admin dashboard | **0** | — | — | — | **5** | Wired the dashboard module to `GET /admin/dashboard` and deleted its last two mock files. 19th edition with no board row |

Flow figures (submissions, median cycle) are unchanged since 3 September — **nothing has entered REVIEW/QA on either board for eleven days**, so there is no new throughput to measure. Commit counts are trailing-7-day, merged to the default branch except where stated, summing each person's git identities.

**The two questions for standup:** (1) **Can the eight infected `beevia-admin-api` branches be deleted, or does someone need them?** Three are already merged and are pure liability; the rest need a rebase before any of them can be merged (§0.3). (2) **Is `BVA-I192` waiting on review, or on a decision?** Fourteen commits, two of them yesterday, under a board item that has been Done for eleven days.

**The three things worth knowing:**

1. **The cleanup worked, and it is half-finished.** `main` is clean on all three repositories — verified by blob hash across the full history of every branch's default ref, not by reading a diff. But `beevia-admin-api` has eight other remote branches with the payload intact, `feat/admin-chats` among them, which a **Copilot agent merged `origin/main` into yesterday**. The exposure did not end when `main` was fixed (§0.3, §0.4).
2. **Sprint 0901 is not blocked on a translation provider, and this pipeline said it was.** `BVA-I228`'s acceptance criteria put translation **on-device** — iOS Translation framework and Android ML Kit — explicitly so message content never leaves the phone. That is the correct architecture for an E2EE product, it makes the server-side stub irrelevant to chat, and `api-rfc.md` §5.5 had concluded the exact opposite five days ago. §0.6 corrects it.
3. **Module 4 has been built, correctly, and nobody has said so.** `admin-api-rfc.md` §5.1 has argued since 5 August that Trust & Safety cannot be built as specified, because the spec wants "reported messages" and chat is E2EE — and it recommended metadata-only moderation as the honest alternative. An unmerged branch contains exactly that: four `/admin/chats` endpoints whose controller docstring reads *"serves metadata + moderation only — never message content"*, including the first reader the `conversation_reports` table has ever had. It sits on `feat/admin-chats`, which is one of the eight infected branches, which is why it must be rebased rather than deleted (§2.4). Separately, `GET /admin/wallets` and its per-user drill-down shipped Saturday, taking Module 5 to six of seven operations (§2.1).

**If you read nothing else:** delete seven of the eight infected branches and rebase the eighth today, because one merge undoes this morning's cleanup and that eighth branch is the only copy of an entire module; sprint 0901 has moved 4 of 17 leaves in 6 days with zero estimates and zero submissions; and both of this week's genuinely good architectural calls — on-device translation and metadata-only moderation — were made silently and found by reading code, which is a reporting problem rather than an engineering one.

---

## 0. Security — remediation status

### 0.1 What happened since yesterday

Yesterday's edition reported that `origin/main` of `beevia-api`, `beevia-admin-api` and `beevia-db-schema` had been force-pushed with an EtherHiding malware loader appended to `eslint.config.mjs`, and that at least one developer workstation was infected because the payload rode in on legitimate work.

**All three branches were rebuilt this morning.** The commit metadata records it precisely: the three surviving `beevia-admin-api` commits carry author dates of 6 September and **committer dates of 8 September 13:36–13:45 UTC**, by `phoenixdahdev <ayomikuntemitope.araoye@gmail.com>`. Three `rescue/*` branches were pushed alongside, which is the shape of someone taking snapshots before rewriting. This was a deliberate, careful recovery, not an accident.

### 0.2 What is verified clean

| Check | Result |
|---|---|
| `eslint.config.mjs` blob on `origin/main`, all three repos | `09fc5b23…`, **1485 bytes** — byte-identical to the last-known-good blob still held in this workspace |
| Same file on local `main` (the pre-compromise tip) | `09fc5b23…` — **the same object**, so the clean file is provably the original, not a retyped approximation |
| Every `eslint.config.mjs` blob reachable from `origin/main` history, all five repos | Only `09fc5b23…` (1485 B) and its older `4e9f8271…` (899 B) predecessor. **The 9167-byte payload appears nowhere** |
| `.gitignore` markers (`branch_structure.json`, `temp_auto_push.bat`, `temp_interactive_push.bat`) | **Gone** from all three |
| Tree of `origin/main` vs the last-known-good local tip (`beevia-api`, `beevia-db-schema`) | **Identical.** Nothing but the payload was removed, and nothing else was changed |
| `beevia-api`, `beevia-db-schema` remote branches | Only `main` remains — the feature branches were deleted |

The verification was done by comparing **object hashes across every ref**, not by reading diffs. That matters: the payload was appended after a long run of tabs and is invisible in a diff view, which is how it survived review in the first place.

### 0.3 What is not clean — eight branches in `beevia-admin-api`

| Branch | `eslint.config.mjs` | Last commit |
|---|---|---|
| `feat/admin-chats` | ⛔ `d394c08e…` **9167 B** | 2026-09-07 — **`copilot-swe-agent[bot]` merged `origin/main` into it** |
| `feat/admin-dashboard` | ⛔ 9167 B | 2026-09-06 |
| `feat/admin-wallets` | ⛔ 9167 B | 2026-09-06 |
| `feat/admin-user-transactions` | ⛔ 9167 B | 2026-09-04 |
| `feat/ledger-anchor-reconciliation` | ⛔ 9167 B | 2026-09-04 |
| `feat/reconciliation-aggregate` | ⛔ 9167 B | 2026-09-04 |
| `BVA-1226` | ⛔ 9167 B | 2026-09-04 |
| `rescue/3b188c9` | ⛔ 9167 B | 2026-09-06 |
| `rescue/43abc3a`, `rescue/e6b8436` | ✅ 1485 B | clean snapshots |

Spot-checked content: the blob still ends in `spawn("node",["-e",env+code],{detached:!0,stdio:"ignore",windowsHide:!0}).unref()` with the same `http://${ip1}:443/0x/cls` loader. It is the same payload, unmodified.

Three consequences, in order of how soon they bite:

1. **CI is not safe yet.** A push to, or a pull request from, any of these branches runs a lint job that loads the malicious config. Freezing CI on `beevia-admin-api` alone is not enough if the freeze was lifted after `main` was fixed.
2. **One merge re-infects `main`.** `feat/admin-chats`, `feat/admin-dashboard` and `feat/admin-wallets` are live feature branches. Merging any of them without rebasing onto the clean history puts the file straight back where it was yesterday.
3. **An automated agent is operating on an infected branch.** `copilot-swe-agent[bot]` merged `origin/main` into `feat/admin-chats` yesterday. Whatever environment that agent runs in checked out a tree containing the payload. That is also the one branch of the eight that cannot simply be deleted, because it holds a module nobody has reported (§2.4).

**The remedy is cheaper than it looks, because six of the eight carry nothing worth keeping.** Note first that *none* of them is an ancestor of the rebuilt `main` — the rewrite gave every commit a new SHA, so `git branch --merged` will report all eight as unmerged and is the wrong instrument here. Compare content instead:

| Branch | Unique content vs `main` | Action |
|---|---|---|
| `BVA-1226`, `feat/admin-user-transactions`, `feat/ledger-anchor-reconciliation`, `feat/reconciliation-aggregate` | **None.** All four point at the same old poisoned merge `d83687c` and are *behind* `main` by 13 files | **Delete** |
| `feat/admin-wallets`, `feat/admin-dashboard` | **None.** Content-identical to `main` except `eslint.config.mjs` and `.gitignore` — i.e. the payload and its cover | **Delete** |
| `rescue/3b188c9` | None; a pre-rewrite snapshot, behind `main` | **Delete** once §0.2's verification is accepted |
| **`feat/admin-chats`** | **Yes — an entire unmerged module** (§2.4) | **Rebase onto `origin/main`.** Do not delete |

So seven deletions and one rebase, and the one rebase is the branch that matters most (§2.4).

### 0.4 The workstation question is still open

Yesterday's §0.4 argued the infection is on a developer machine, because the payload arrived inside genuine application work. **Nothing observable from here says that has been dealt with.** The remote is clean; the machine that authored `09fda4f` is not visible to this pipeline. If it has not been imaged and cleaned, the next legitimate commit re-introduces the file and this section repeats itself.

The same applies to credential rotation. Rotation is invisible from a git clone. It is listed as done or not done nowhere, so this report cannot say — it can only note that **§0.6's first two steps are the two that cannot be verified from the outside**, and that they are also the two that get less effective with delay.

### 0.5 Branch protection could not be checked

Yesterday's top recommendation was branch protection with force-push disabled. **This workspace cannot verify it.** The GitHub credential available here has no access to the `Drumbell-Technologies` organisation — `repos/Drumbell-Technologies/beevia-api` returns `404` for the repository itself, not just for its protection settings, so "not found" carries no information either way. Git access is over SSH with a different key.

That has to be confirmed in the GitHub UI by someone with org admin. It is not a finding that it is missing; it is a finding that **this report has no instrument for the control it keeps recommending**, and will not have one until someone checks by hand or grants a token read access.

### 0.6 Two corrections

#### Correction 1 — `api-rfc.md` §5.5 was wrong about the translation sprint

**Claim (2026-09-03, restated 2026-09-04 and 2026-09-07): "connecting a real provider is a prerequisite for the translation sprint, and it is not on the board."**

It is not a prerequisite, and the answer was on the board the whole time. Sprint 0901's foundation story `BVA-I228` — *On-Device Translation Engine Integration* — states its own design in its acceptance criteria:

> *"a working on-device translation capability, so chat messages can be translated without any message content leaving the user's phone"* — integrating **iOS's native Translation framework and Android's ML Kit Translation behind one unified internal translation service**, for English (UK), English (US), French, Spanish and Mandarin, handling the on-device model download and offline fallback.

Server-side translation of chat requires plaintext at the server. That is exactly what E2EE forbids, and it is the same constraint that makes the admin console's content-moderation module unbuildable (`admin-api-rfc.md` §5.1). **The team chose the architecture that preserves the product's central privacy claim, and this pipeline spent three editions calling it blocked on the architecture that would have broken it.**

The failure mode is worth naming, because it is not the same one as last time. This was not inferring build state from board state; it was **reading the board's status column and not its descriptions**. `BVA-I228`'s title alone ("On-Device Translation Engine Integration") contained the correction. `api-rfc.md` gains §5.5a with the full version, and the two now-probably-obsolete proposed operations (`/translate/batch`, `/translate/languages`) are annotated rather than deleted — see §4.2.

#### Correction 2 — yesterday's audit drift line, again, and it grew

Today's audit closes with `beevia-admin-api code=34 spec=37 — documented, not in code: GET /admin/dashboard, GET /admin/wallets, GET /admin/wallets/users/{}`. **None of that is drift.** All three exist on `origin/main`; they are absent from the *working tree* because the fast-forward is still refused (§0.7). Running the same extractor against `origin/main` gives **code=37, spec=37, zero difference in either direction** — and `beevia-api` likewise, 131 = 131.

Flagged for the second consecutive edition so that nobody "fixes" the spec by deleting three real operations.

### 0.7 What this refresh did and did not do

The three repositories are **still not synced**, and deliberately so. `sync_repos.py` is limited to `--ff-only` merges; `origin/main` is a rewritten history, so the merge is correctly refused. Resolving it needs `git reset --hard origin/main` or equivalent, which is outside this pipeline's sanctioned exception and is a decision for whoever owns those clones.

**The evidence now says it is safe to do.** `origin/main` is verifiably clean (§0.2) and its trees for `beevia-api` and `beevia-db-schema` are byte-identical to the local tips. Adopting it discards nothing. But the local clones hold the last-known-good pre-rewrite tips (`d9af17b`, `43abc3a`, `5b0592a`), which have been useful twice this week, so **capture those SHAs before resetting** — they are the only offline copy of the pre-incident history.

Nothing was executed from any sub-repo during this refresh. No `npm`, `node`, `eslint` or build step ran. All code claims about the three unsynced repositories were made against `origin/main` read through `git show` and `git archive` into a temp directory outside the workspace.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

25 items — **17 leaves, 8 parent Stories**. Sprint 3 Sep → 22 Sep, day 6 of 20.

| Status | Leaves |
|---|---:|
| To do | 13 |
| In progress | **4** |
| REVIEW/QA | 0 |
| Done | 0 |

| Owner | Leaves | To do | In progress |
|---|---:|---:|---:|
| Ayomikun Araoye | 9 | 9 | 0 |
| David Samuel | 6 | 3 | 3 |
| Philip Chidera | 2 | 1 | 1 |

### 1.2 The window's movement, and who made it

Two transitions, both today at **12:16 UTC**, both by **David Samuel**: `BVA-I242` *Static App UI Text Localization* and its leaf `BVA-I243` *String Extraction & Bundle Switching*, To do → In progress.

Small, but it is the first time in this sprint that **David started his own items**. Every previous start was made by Philip, including three on items David owns. Board hygiene performed by one person on another's behalf is not the same signal as an owner picking up work, and this is the better one.

Against that: **Ayomikun has not touched any of his nine leaves for a fifth consecutive day**, and all nine are the sprint's backend half — the seven notification stories, preference storage, and the backend string bundles. He has been shipping continuously (§2), just not on this sprint.

### 1.3 What the sprint actually is

Worth stating plainly, because three editions have discussed "the translation sprint" without reading it. 0901 is **two workstreams**:

| Workstream | Items | Owner |
|---|---|---|
| **Translation** — on-device engine, language preference storage, per-conversation override, per-message toggle, app-text localization, backend string bundles | 10 leaves | David (client), Philip (design), Ayomikun (2 backend) |
| **Push notifications** — Firebase Admin SDK, device-token storage, payload routing, four trigger families, per-category preferences | 7 leaves | Ayomikun, all |

The notification half is entirely Ayomikun's and entirely untouched. `BVA-I246` is the foundation (server-side FCM credential and device-token registration) and everything else in that half depends on it.

### 1.4 Still no estimates — fifth consecutive edition

**0 of 25 items carry estimation points**, and none carries a tag. Velocity, burn-down and any workload comparison between people remain underivable. This report has now asked five times; either answer — "here are the points" or "this project does not estimate" — closes it.

---

## 2. What shipped this cycle

### 2.1 `beevia-admin-api` — the Wallets screen (2 operations)

Merged 6 September, first seen by this pipeline today because the branch was unsyncable yesterday.

| Method | Path | Permission |
|---|---|---|
| GET | `/admin/wallets` | `wallets:view` |
| GET | `/admin/wallets/users/{userId}` | `wallets:view` |

A platform-wide summary (total held per currency, counts by status) over a filterable, paginated list of customer wallets — user, currency, balance, status, provider and pay-in virtual account — plus a per-user drill-down. `search` matches the owner by name, username, email or phone; ordering is balance descending. System and escrow wallets are excluded via `wallet_type = 'user'`, so the totals are customer liability rather than the platform's balance sheet.

**It is well-built.** Guards and permissions are present (`AdminAuthGuard`, `PermissionGuard`, `@RequirePermission`), the query is Zod-validated, the summary is four parallel aggregates rather than a scan, `wallets` was already in `adminModuleEnum` so no migration was needed, and it ships with two spec files. It is also the first admin operation to arrive with a `.spec.ts` beside it in the same commit.

Four contract facts for whoever builds the screen:

- **The summary ignores the filters.** `total_wallets`, `by_currency` and `by_status` are computed over every user wallet regardless of `currency`, `status` or `search`. Deliberate — a "total held" tile should not move as the operator pages — but it is the single most likely thing to be read as a bug when it sits above a filtered table.
- **`by_status` is sparse.** A status with no wallets is absent, not zero.
- **`search` matches the owner, not the wallet.** There is no lookup by wallet id or by account number, which is where a support call actually starts ("a transfer went to 9901234567").
- **Balances are presentation values**, rounded from the ledger's scale-8 figure. Summing the column will not reproduce `total_balance`.

**What did not ship is the reason the proposal existed.** The retired `GET /admin/users/{id}/wallets` proposal asked for the **partner-reported balance beside the ledger balance with an `in_sync` flag**, so a per-wallet mismatch was visible at a glance. The shipped row carries the ledger balance only. Answering "is this one wallet in sync" still means leaving the Wallets screen for `GET /admin/reconciliation/users/{userId}`, which runs an unbounded full-history comparison for the whole account. That is now the substantive gap in Module 5 (`admin-api-rfc.md` §6.3).

One cosmetic artifact of the rebuild: **the tip of `beevia-admin-api` `main` is an empty commit.** `4981c70` and `ec32008` share a message and an author date; `ec32008` carries all 8 files, `4981c70` carries none. Harmless, and worth knowing before someone reads the tip as the wallets change.

### 2.2 `beevia-admin` — the dashboard stopped being a mock

`d0faf19`, 7 September, Promise Udo. The dashboard module now calls `GET /admin/dashboard`: `src/features/dashboard/api.ts` gains 161 lines with the response shape and a comment reading *"confirmed live"*, `overview.tsx` (423 lines) replaces `summary-cards.tsx` and `financial-section.tsx`, and **`mock/summary.ts`, `mock/financial.ts` and `use-mock-resource.ts` are deleted outright** rather than left as fallbacks.

That is the same pattern as his 4 September commit and the same speed: the endpoint merged on Sunday, the client was on it Monday. **Six of ten admin modules now call the live API**; `reports` and `pending-transfers` are the two still mock-only.

### 2.3 `beevia-mobile` — activity is on a branch, not on `main`

`main` is unchanged since 26 August — **13 days**. `origin/BVA-I192` is now **14 commits ahead** (was 12), with two commits yesterday: *"unsaved local changes"* and *"resolved conflicts"*.

**David is working; the default branch cannot see it.** Yesterday's edition reported "zero commits" with a caveat; today the caveat is the finding. A branch that has been rebasing against a moving `main` for eleven days, under a board item that is already Done, is the definition of work at risk — and "resolved conflicts" is what that costs.

### 2.4 Unmerged, and the most interesting thing in the repository: Module 4 exists

`origin/feat/admin-chats` — the branch a Copilot agent merged into yesterday, and one of the eight still carrying the payload — contains an entire `src/chats/` module that has never been mentioned in any status report, because it has never been on `main` and the branch was unreadable until today.

`feat(chats): admin chats screen (E2EE-safe metadata + moderation)`, 6 September, four endpoints:

| Method | Path | Summary |
|---|---|---|
| GET | `/admin/chats` | Conversations list — participant / message / report counts, last activity |
| GET | `/admin/chats/reports` | **The moderation queue** — reporter, reason, conversation |
| GET | `/admin/chats/users/{userId}` | A user's conversations plus their block graph |
| GET | `/admin/chats/{conversationId}` | Conversation detail — metadata, participants, reports |

**This is spec Module 4, the one `admin-api-rfc.md` §5.1 says cannot be built as specified — and it is built the right way.** §5.1 laid out three options and recommended **Option A, metadata-only moderation**, because the spec's demand for "reported messages" is unsatisfiable against E2EE. The controller's own docstring is that recommendation in one line: *"Chat is end-to-end encrypted, so these endpoints serve metadata + moderation only — never message content."* Every operation says "no message content" in its description. Nobody asked this report whether it was buildable; someone read the constraint and built the version that respects it.

It also closes a finding that has been open since 5 August. §5.1 noted that `conversation_reports` is populated by the consumer app's `POST /conversations/{id}/report` and **nothing reads it** — "reports are piling up unreviewed today". `GET /admin/chats/reports` is the reader.

Three things follow:

1. **It is not in `openapi.admin.yaml`, and should not be.** The implemented spec documents what is on `main`. This is on a feature branch. It will be documented the day it merges, and §4 records the decision rather than pre-empting it.
2. **It sharpens the branch problem rather than softening it.** The only branch of the eight with unique work is the only one that cannot be deleted, so it is the one that must be rebased onto the clean history — and it is the one an automated agent has been merging into.
3. **Module 4 goes from "blocked on a product decision" to "awaiting a merge"**, if the metadata-only reading is accepted. That is a question for the owner, not a conclusion this report can draw: §5.1 offered three options and someone chose one without recording it. The same shape as the translation decision in §0.6 — a good call, made silently, that this pipeline could only discover by reading code.

### 2.5 `beevia-api` — nothing

No commit since 4 September. Every consumer-API capability in the MVP rubric is unchanged for a fourth day, including the translate stub, `PaymentService.activeNgn()`, the unset `ANCHOR_POOL_ACCOUNT_ID`, and the `POST /kyc/profile` silent-200.

---

## 3. Sprint 08-01 — closed and frozen

64 items, 41 leaves, **all Done**. No transitions since it closed on 3 September, and none are possible. It remains the sprint the daily export targets (§7, §9).

---

## 4. Spec updates made this cycle

### 4.1 `openapi.admin.yaml` — two operations added, 35 → 37

`GET /admin/wallets` and `GET /admin/wallets/users/{userId}`, documented from the controller, DTO, service and response types read at `origin/main`. New `Wallets` tag; new `WalletUserId` parameter; new `AdminWalletRow`, `WalletVba`, `WalletsSummary` and `WalletsCurrencyTotal` schemas. `TransactionsPagination` is reused rather than duplicated — the shape is identical, and its description now says so, including that the name is historical and renaming it would churn every generated client.

The four contract traps in §2.1 are written onto the operations, not left for the reader to discover.

### 4.2 `openapi.admin.proposed.yaml` — one proposal retired, 21 → 20

`GET /admin/users/{id}/wallets` shipped, at a different path. Replaced with a `NOTE` comment in the house style, which records **what did not ship** (`partner_balance`, `in_sync`) rather than just marking it done — that is the part someone will otherwise re-propose from scratch. The orphaned `AdminWallet` schema is removed.

### 4.3 `openapi.proposed.yaml` — two translation operations annotated, not deleted

`POST /translate/batch` and `GET /translate/languages` both exist to serve a server-side engine: the language list is the provider's, and batching exists to avoid one round trip per visible message. On-device translation (§0.6) has neither. **Both are annotated as probably obsolete and left in place.** Nothing is built either way, no decision is recorded anywhere in writing, and retiring a proposal on inference is how a spec starts lying in the opposite direction. This is an open question for the owner (§9 item 4), not a finding.

`/users/me/translation` and `/conversations/{id}/translation` are **unaffected and now board-backed** — `BVA-I230`/`BVA-I231` is exactly that proposal. A client-side engine still needs a server-side preference that survives reinstall.

### 4.4 Narrative documents

- `admin-api-rfc.md` — counts 35 → 37 and 21 → 20; new §3.12 (Wallets); Module 5 coverage 4 → 6 ops; §5.2 rewritten (one operation left proposed, not two); §6.3 grows a fourth gap, the missing per-wallet partner balance.
- `api-rfc.md` — new §5.5a correcting §5.5's sequencing conclusion (§0.6).
- `suggestions.md` — new §7.6, *"Cleaning `main` is not cleaning the repository"*, with the ref-sweep command; §8's order re-headed by the branch cleanup.

### 4.5 Spec health

All four files parse; **131 / 42 / 37 / 20** operations. No `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s. Drift against `origin/main`: **zero, both services, both directions.**

---

## 5. Admin dashboard board

**The Beevia Admin Dashboard project still has no sprint.** Step 1b exits 3 and writes nothing — nineteenth consecutive edition. The project exists (id `187554000000127002`, project no. 8) with no sprints and no start/end dates.

That is the status, and it is unchanged since the project was created on 28 August. Until it carries items, Promise Udo's row in the team table is sourced from commits, and the standing caveat holds: **board totals understate delivery, because the entire admin dashboard workstream — 37 endpoints' worth of client, six of ten modules now live — happens outside them.**

When it is populated, the export step will need `--sprint <name>` explicitly; the main `ZOHO_SPRINT_FILTER` (`08-01`) will not match, and a silent exit 3 after the board goes live means exactly that.

---

## 6. Team performance — detail

All figures come from the activity sidecar and git, never from `Last Modified`. **No item reached REVIEW/QA on either sprint in this window**, so submission and cycle-time figures are carried forward from 3 September; commit counts, WIP ages and staleness are current.

**Ayomikun Araoye — backend + admin API.** 20 commits in the trailing 7 days across `beevia-api`, `beevia-admin-api` and `beevia-db-schema`, summing the `Ayomikun Araoye`, `Phoenixdadhev` and `phoenixdahdev` identities and excluding bots. Up from 15 yesterday, and the increase is almost entirely **this morning's history rebuild** (§0.1) rather than new features — the three rebuilt commits are re-committed 6 September work. His last genuine feature commit is Saturday's wallets endpoint. He owns nine of sprint 0901's seventeen leaves, all in To do, untouched for a fifth day, and the notification half of the sprint cannot start without `BVA-I246`, which is his. **The remediation was his work and it was done well** — clean blob restored to the original object, `.gitignore` markers removed, rescue snapshots taken first. It is also, in this window, the thing he did instead of the sprint, which is the correct trade and worth recording as such rather than reading his flat feature output as a slowdown.

**David Samuel — mobile.** Three genuine submissions in the trailing 7 days, last on 28 August; median cycle 2.6 d over 14 passes. **Zero commits to `main`, three to `origin/BVA-I192`** including two yesterday. He now holds three 0901 leaves In progress: `BVA-I233` and `BVA-I241` at **3.9 days** against his own 2.6-day median, and `BVA-I243` started today. Two items past his median and a fourteen-commit branch that has been merging conflicts for eleven days is one situation, not two — the branch is where his attention has been. He also started his own board items today for the first time this sprint, which is a small positive signal in a column that otherwise reads as silence.

**Philip Chidera — design.** Two genuine submissions in 7 days; median cycle 0.9 d over 7 passes. One leaf In progress, `BVA-I240`, age **3.9 days against a 0.9-day median** — over four times his own pace and the most overdue WIP on either board relative to its owner. No board action since Friday, after a Friday in which he made nine of eleven transitions including three on items he does not own.

**Promise Udo — admin dashboard.** No board presence, nineteenth consecutive edition. **5 commits in the trailing 7 days**, and yesterday's took the dashboard module from mock to live within a day of the endpoint existing (§2.2). His workstream continues to have the cleanest endpoint-to-client latency in the project and the least visibility in its tracking.

### 6.1 Weekly submission trend

Genuine submissions into REVIEW/QA, by ISO week: **W34 (17–23 Aug) — 17 · W35 (24–30 Aug) — 10 · W36 (31 Aug – 6 Sep) — 1 · W37 (7–8 Sep) — 0.**

**Eleven days since anything entered review.** The closed sprint cannot produce more; the open sprint has produced starts only. The throughput signal has been blind for three consecutive editions, and at some point the honest reading is not "the queue is empty" but "this board is not being used to track completion."

### 6.2 Cycle times

Unchanged from 3 September; no new passes measured. Method: one measurement per pass, from an item's most recent entry into `In progress` to the next time it reaches `REVIEW/QA`.

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

### 6.3 What these figures do not measure

- **They do not see branches.** David reads zero commits while fourteen sit on `origin/BVA-I192`, two of them yesterday. Every "commits" figure means *merged to the default branch*.
- **They count a security rebuild as feature output.** Ayomikun's 20 includes three re-committed 6 September commits from this morning's history rewrite. The work was real and necessary; it was not new product.
- **They do not see the largest client change of the week.** Promise's dashboard wiring appears in exactly one column, because his workstream has no board.
- **No estimation points exist on any item, either sprint** — 0/64 and 0/25. Nothing is normalised for size.
- **Board actions are not evenly attributable.** Figures key to the item's assignee, not to whoever clicked.
- **Review and triage work is invisible**, and there was again none to record.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **Absence of board data is not absence of work**, and absence of commits *to `main`* is not absence of commits.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction. Noted anyway because it is new: the wallets endpoint shipped with tests in the same commit.

---

## 7. Risks

1. **Eight `beevia-admin-api` branches still carry the malware payload** (§0.3). A merge from any of the three live feature branches re-infects the `main` that was cleaned this morning.
2. **CI on `beevia-admin-api` is not safe** while those branches exist and can trigger lint jobs.
3. **An automated Copilot agent merged into an infected branch yesterday** (§0.3). Its execution environment held the payload.
4. **An entire unmerged module exists only on an infected branch** (§2.4). `feat/admin-chats` is the sole copy of the `/admin/chats` work; deleting the infected branches carelessly destroys it, and merging it carelessly re-infects `main`.
5. **The infected workstation's status is unknown** (§0.4). Until it is cleaned, the next legitimate commit re-introduces the file.
6. **Credential rotation cannot be verified from here** and is the step that decays fastest.
7. **Branch protection cannot be verified from here** (§0.5) — the available GitHub token has no org access. The control this report keeps recommending has no instrument behind it.
8. **Three repositories remain unsynced locally** (§0.7), so the deterministic audit reads Thursday's code for them. Every claim here about them was made against `origin/main` by hand.
9. **Nothing has entered REVIEW/QA for eleven days** on either board (§6.1) — throughput blind for a third edition.
10. **Sprint 0901 has moved 4 of 17 leaves in 6 days**, with 0 of 25 estimated (§1.1, §1.4).
11. **The notification half of 0901 has not started**, and all seven items depend on one untouched foundation story (§1.3).
12. **A fourteen-commit mobile branch has been unmerged for eleven days** under a Done board item, and is now resolving conflicts (§2.3).
13. **The Wallets screen cannot show a per-wallet ledger-vs-partner mismatch** (§2.1) — the one thing the proposal existed to provide.
14. **The per-user reconciliation balance check will report false discrepancies for every user the moment the treasury pool is enabled.** `ANCHOR_POOL_ACCOUNT_ID` is still unset, so the window is still open.
15. **`treasury.solvent` is on the landing screen and reads `false` for "unknown"** — the dashboard module went live yesterday, so this is now rendered, not hypothetical.
16. **The money-oversight surface still has no second reviewer** — PRs #1–#6 were self-merged.
17. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows; exceeding the caps produces wrong output, not visible truncation.
18. **The Anchor webhook backfill is still unscoped** — 67 days of dropped events, unmeasured, seven days after the fix.
19. **The daily export still targets a closed sprint** (§3), third consecutive edition.
20. **The 14:00 UTC cut-off is still producing false "silence" findings** — today's David finding was a near miss of the same kind.
21. **The same silent-200 is still live on `POST /kyc/profile`** — sixth consecutive edition.
22. **A hard-coded account number still reaches a money screen on `main`** — sixth consecutive edition, under a Done item.
23. **`POST /translate` still returns its input unchanged.** Less urgent than it looked yesterday (§0.6), but it is a live route that lies to any caller that is not the chat client.

---

## 8. Previous recommendations — where they stand

| Recommendation from 7 Sep | Status on 8 Sep |
|---|---|
| Work §0.6 in order, today | **Partly, and the visible half was done well.** The three branches were rebuilt from clean history this morning and verified clean (§0.2). Not done or not verifiable: the eight infected branches (§0.3), the workstation (§0.4), credential rotation, the org audit. |
| Turn on branch protection with force-push disabled | **Unknown.** Cannot be checked from this workspace (§0.5). Needs a manual confirmation. |
| Decide the sprint 0901 question properly | **No decision recorded.** Two leaves started today, by their owner rather than by proxy, which is movement but not a decision. Nine leaves still untouched for a fifth day. |
| Confirm the filter contract for `GET /admin/transactions` | **Not done.** No commit either side. The dashboard still sends five undocumented filter params. |
| Move the daily export to sprint 0901 | **Not done.** Third edition. Still the right change and still not blocked by anything except that nobody has made it. |
| Move the report cut-off to ~20:00 UTC | **Not done.** |
| Put estimation points on 0901 | **Not done.** 0/25, fifth edition asking. |
| Scope the Anchor webhook backfill | **Not done.** No reconciliation run, no commit, no board item. |
| Apply the BVN-ordering guard to `POST /kyc/profile` | **Not done.** Re-checked at `origin/main`; unchanged. |

One of nine substantially actioned, and it is the one that mattered most.

---

## 9. What I would do this week

1. **Clear the eight infected `beevia-admin-api` branches — today. Seven deletions and one rebase.** Six carry no unique content and `rescue/3b188c9` is a superseded snapshot; all seven can be deleted outright. `feat/admin-chats` is the exception and must be rebased onto `origin/main`, because it is the only copy of the chats module (§2.4). Do not use `git branch --merged` to decide which is which — the rewrite changed every SHA, so it reports all eight as unmerged; compare content, per the table in §0.3. `main` is clean; the repository is not, and one merge undoes this morning's work.
2. **Sweep every ref, in every repo, and verify by blob hash.** The command is in `suggestions.md` §7.6. "Is `main` clean" and "is the repository clean" are different questions, and only the second one is the one that matters.
3. **Confirm the two things this report cannot see**: whether the workstation that authored `09fda4f` has been imaged and cleaned, and whether credentials were rotated. Both are invisible from a git clone, and both are on the critical path for §0 being genuinely closed rather than apparently closed.
4. **Rebase `feat/admin-chats` and decide whether to merge it** (§2.4). It is Module 4 built as `admin-api-rfc.md` §5.1 recommended — metadata-only, no message content — and it is the first thing that will ever read the `conversation_reports` table, which has been accumulating unread reports since the consumer app shipped reporting. The engineering question is a rebase; the product question is whether metadata-only moderation is accepted as the answer to Module 4, which §5.1 raised as needing a decision and which appears to have been made in code without being recorded.
5. **Decide the translation API question** (§4.3). On-device translation makes `POST /translate/batch` and `GET /translate/languages` obsolete, and probably makes `POST /translate` itself a route to retire rather than to connect a provider to. Say so in writing and the spec follows in ten minutes; leave it unsaid and someone eventually builds a provider adapter nobody needs.
6. **Start `BVA-I246`, or move the notification half out of 0901.** Seven of nine of Ayomikun's leaves depend on it, none has moved in five days, and the sprint has fourteen days left. This is the concrete version of "decide the 0901 question" that the last two editions asked in the abstract.
7. **Merge `BVA-I192` or say why not.** Fourteen commits, eleven days, an already-Done board item, and now conflict resolution. Whatever the reason is, it is cheaper to state than to keep rebasing.
8. **Move the daily export to sprint 0901.** Third edition asking, and the only thing standing in the way is that it means relocating twelve tracked CSVs into `sprint-board-exports/08-01/` and changing `ZOHO_SPRINT_FILTER`. It is a half-hour of file moves, and it is currently costing a scratch export and a caveat in every edition.
9. **Put estimation points on 0901, or state that this project does not estimate.** Fifth consecutive edition.
10. **Get a token with org read access, or check branch protection by hand.** Recommending a control for three editions with no way to observe it is not a useful loop (§0.5).
11. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Unchanged from the last six editions; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:00 UTC) → admin board (exit 3, no sprints, 19th edition) → fast-forward sync (**1 commit into `beevia-admin`; 3 repos refused as `diverged`**, §0.7) → repository-wide integrity sweep across every remote ref by blob hash (§0.2, §0.3) → deterministic audit → static contract review of the wallets endpoint from `origin/main` → spec and RFC updates → re-audit, plus a second drift check run against `origin/main` extracted to a temp directory → read-only scratch export of sprint 0901 → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran during this refresh. The three unsynced repositories were read with `git show`, `git grep`, `git cat-file` and `git archive` only. No repository was reset, rebased, reverted or cleaned, and the sync step's `--ff-only` limit was not overridden.

**Sprint 0901 was exported to `/tmp/beevia-scratch/`, outside the repository**, for the fourth consecutive edition and for the same reason: `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest files as snapshots of one board, so a second CSV covering a different sprint would make tomorrow's delta compare 08-01 against 0901 and report invented movement. §9 item 7 is the fix.

**Degraded inputs.**
- **Three repositories could not be synced** (§0.7) — `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are diverged because `origin/main` was rewritten, twice this week. Their *working trees* are 4 September code. Every code claim about them here was made against `origin/main`; the audit script, which reads working trees, was not, which is why it reports three phantom drift lines (§0.6).
- **Branch protection is unverifiable** — the GitHub credential in this environment has no access to the `Drumbell-Technologies` org (§0.5).
- **Credential rotation and workstation remediation are unverifiable** from a git clone (§0.4).
- **The `Epic` column is blank** across the main board — the OAuth refresh token lacks `ZohoSprints.epic.READ`. Known scope gap, not "no epic assigned". 38 of 41 leaves affected.
- **`Comments` bodies are unavailable** from the API.
- **The admin board produced no export** because the project has no sprints (expected, exit 3, not a failure).
- **`ZOHO_SPRINT_FILTER` is stale** — still `08-01`, so the in-repo export covers a sprint that closed on 28 August.
- **No estimation points on any item**, either sprint, so velocity is not derivable and no per-person figure is normalised for size.

**Window.** 7 Sep 14:00 UTC → 8 Sep 14:00 UTC — one working day. All `actiontime` values and board times are UTC. Git author dates are as recorded; note that this morning's rebuild reset committer dates on three `beevia-admin-api` commits, so committer and author dates diverge by two days there — §0.1 uses that divergence deliberately, as the timestamp of the remediation.

**Sources.** Board: `beevia-sprint-board-2026-09-08.csv` (64 rows, 41 leaves, sprint 08-01), `beevia-activity-2026-09-08.json`. Active sprint: scratch export of `0901` (25 rows, 17 leaves) with its own activity sidecar. Admin board: none. Code: `beevia-admin` and `beevia-mobile` at `origin/main` in the working tree; `beevia-api`, `beevia-admin-api` and `beevia-db-schema` read from `origin/main` refs without checkout. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (**37**), `openapi.admin.proposed.yaml` (**20**) — all validated, no markers, no broken refs, no orphaned components.

**A note on who appears here.** Only people whose work is tracked have rows. Board transitions performed by non-contributors are reported without attribution, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈56% (estimate; 56.33, from 55.97)

**Target 2026-09-01 (provisional) · the target date passed seven days ago.** On merged build evidence the product is roughly 56% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. No `beevia-api` commit since 4 Sep. Unchanged |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present; incoming-call push wired. Unchanged |
| 3 | Message translation | 7 | 0.15 | **Unchanged score, corrected basis.** `TranslateModule` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`. The sprint's design is now known to be **on-device** (`BVA-I228`), so the server stub is no longer the blocker — but nothing is merged: 0 commits to `beevia-mobile` `main` in 13 days, and the two engine items are To do. A design decision is not build evidence |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged. KYC/upgrade endpoints + provider webhook live; full onboarding flow wired in the client. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged; no consumer-API commit in the window. Client has a full wallet section (6 screens: home, add money, transaction history, three send flows). Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` unset), so not scored. Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. P2P send wired end to end via `/payments/transfer`. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; `PaymentService.activeNgn()` still present at `origin/main` |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. Card lifecycle events processed since 3 Sep. Ceiling still low: the client has **zero** `/cards` references and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | **0.78** ↑ | **+0.06, both halves moved in the same 48 hours.** Admin API 35 → **37** (`/admin/wallets`, `/admin/wallets/users/{userId}`, §2.1), taking Module 5 from 4 of 7 operations to **6 of 7** — flagging is all that remains. On the client, `beevia-admin` goes from **5 of 10** feature modules on the live API to **6 of 10**: the dashboard module now calls `GET /admin/dashboard` and its three mock files were deleted, not disabled (§2.2). Ceiling: `reports` and `pending-transfers` still mock-only, Modules 4, 6 and 8 have no endpoints at all, no per-wallet partner-balance comparison, and the transaction filter contract is still unconfirmed |
| | **Weighted total** | **100** | | **56.33 → ≈56%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, never merged-but-disabled code, and never a design decision on its own.

**On the single movement, and on the one that did not happen.** Capability 11 moved because two endpoints merged and a client module stopped being a mock — both nameable, both merged. Capability 3 did *not* move despite this edition's largest new piece of information, because knowing the right architecture is not the same as having built it, and the rubric would stop meaning anything the first time a plan scored points. The correction in §0.6 changes what the remaining 0.85 of that capability costs; it does not change how much of it exists.
