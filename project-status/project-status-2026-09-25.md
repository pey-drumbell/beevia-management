# Beevia — Project Status

**As of 2026-09-25** · Sprint **0901** (3 Sep → 22 Sep) — **closed three days ago, still the working board** · Sprint **0901-admin** (3 Sep → 22 Sep) — closed, static · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-25.csv` + `beevia-activity-2026-09-25.json` (64 items, sprint 08-01 — frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-25.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**77 items**) + sidecar in `/tmp/beevia-scratch/`; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. **Window 24 Sep 13:30 UTC → 25 Sep 12:58 UTC — about 1.0 day.**

---

## Quick overview

> **A third QA batch of 19 items landed in one hour last night, and the review queue is now 38 of 68 leaf items — 56% of the board is waiting for a reviewer who has never existed.** All 19 were filed by board administration between 14:38 and 15:35 UTC, and 18 of the 19 were assigned to one person. Meanwhile the backend shipped a phone-normalisation fix that closes a real duplicate-account bug, changing the contract of **nine operations without touching a single route** — the third consecutive cycle in which the most consequential change was invisible to the route-level audit. **Three claims in recent editions were wrong and are corrected below**, the most important being that this project has never accepted an item: it has, once, on 16 September.

**Corrections to previous editions — read these first.**

1. **"The project has never accepted an item" is false, and this report said it twice.** `BVA-I268` (*Design the Transaction Receipt Image*) moved **REVIEW/QA → Done on 16 Sep at 11:53 UTC**, closed by its own owner. The 16 and 17 September editions recorded this correctly and in detail. The 23 and 24 September editions then asserted "the acceptance count across all three boards, for the entire life of the project, is still zero" — a restatement that was never re-derived. **The correct standing statement:** on sprint 0901 exactly one item has made the REVIEW/QA → Done transition, and it was closed by its own owner rather than by a reviewer; separately, 46 items were swept REVIEW/QA → Done in 47 seconds at sprint 08-01's close. **No item on any board has ever been accepted by someone other than the person who submitted it.** That is the real finding, and it survives the correction intact.

2. **`GET /translate/languages` is implemented, not proposed.** The 23 and 24 September editions both held capability #3 back partly on the grounds that "`/translate/batch` and `/translate/languages` are still proposed-only". `/translate/languages` shipped and was moved into `openapi.yaml` on **22 September** — by this pipeline, in the same edition that repeated the claim. Only `/translate/batch` remains proposed. The score does not move (§Appendix), because the thing actually holding it back is the stub adapter, not the endpoint list.

3. **Comment bodies are readable after all.** Yesterday's appendix stated that "`Comments` bodies are unavailable from the Zoho API (`commentCount` only)". True of the board export; **not true of the activity sidecar**, which carries the comment text in its `display` field. Sprint 0901 has **nine** comments, and several are substantive engineering pushback that this report has been unable to quote for weeks (§1.4). The export column stays blank; the sidecar is the place to read them.

4. **Yesterday's spec edit left the audit dirty, and yesterday's report said it was clean.** §3.2 of the 24 September edition reported "the audit re-run clean after the edits". Rewriting `LedgerEntry` in `openapi.yaml` diverged it from the duplicate in `openapi.proposed.yaml`; today's first audit run flagged it. Realigned this cycle (§3.3).

| Metric | 24 Sep | 25 Sep | Δ |
|---|---:|---:|---|
| Sprint 0901 items (leaves + parents) | 58 (49+9) | **77 (68+9)** | **+19** |
| Items added to sprint 0901 | 0 | **19** | **+19** |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | **0** |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 0 |
| **Response/request-contract changes needing a hand spec edit** | 2 schemas, 4 ops | **3 schemas, 9 ops** | **+5 ops** |
| Sprint 0901 leaves, total | 49 | **68** | **+19** |
| Sprint 0901 leaves To do | 6 | **17** | **+11** |
| Sprint 0901 leaves In progress | 8 | **5** | −3 |
| Sprint 0901 leaves BLOCKED | 4 | **2** | −2 |
| Sprint 0901 leaves REVIEW/QA | 25 | **38** | **+13** |
| Sprint 0901 leaves Done | 6 | 6 | **0 — seventh edition flat** |
| Review queue as a share of the board | 51% | **56%** | +5 pts |
| Review-queue median age (0901) | 6.4 d | **2.3 d** | −4.1 — dilution, not drainage (§1.3) |
| Oldest item in the queue | 15.9 d | **16.9 d** | +1.0 |
| Items that left REVIEW/QA in the window | 3 (none accepted) | **0** | −3 |
| `beevia-api` / `beevia-admin-api` days since a commit | 0.0 / 0.0 | **0.6 / 1.0** | +0.6 / +1.0 |
| `beevia-db-schema` days since a commit | 0.1 | **0.6** | +0.5 |
| `beevia-mobile` days since a commit | 1.0 | **0.9** | −0.1 |
| `beevia-admin` days since a commit | 1.9 | **2.9** | +1.0 |
| Admin board: days since *any* activity | 9.9 | **10.9** | +1.0 |
| Ayomikun commits (7d, both identities, merged, non-merge) | 25 | **35** | rolling window |
| David commits (7d, merged to `main`) | 3 | 3 | rolling window |
| Promise commits (7d, merged) | 2 | 2 | 0 |
| Unmerged `beevia-mobile` feature branches | 1 (`BVA-I239`, 11 ahead) | **0** — merged as PR #36 | **−1** |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 58 · 0 / 12 · 0 / 64 | 0 / 77 · 0 / 12 · 0 / 64 | 0 |
| **Sprints open on either board** | 0 | **0** | 0 |
| MVP readiness (estimate) | ≈67% (66.72) | **≈67% (66.72)** | **0.00** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **20 on 0901 in REVIEW/QA** (15 solely his) · 3 on 0901-admin · 1 co-owned In progress | 11 | 0.96 d (n=9) | **0** solely-owned on 0901 · 1 on 0901-admin (`BVA-I8`, 10.9 d) | **35** | **Highest count this report has recorded, and still nothing of his has been reviewed.** His half of the queue has a median age of **7.4 d** against David's 0.9. **New: he started triaging** — removed himself as owner from three of the new QA items and pushed back in writing on two (§1.4) |
| David Samuel | mobile | **40 on 0901** — 17 REVIEW/QA solely his (+6 co-owned), 16 To do, 5 In progress, 2 BLOCKED, 2 Done | 23 | 0.96 d (n=18) | **7** — every open item on the board is his | **3** | **18 of the 19 new QA items were assigned to him.** He now holds 40 of 68 leaves. Three mobile commits in seven days against a queue of 23 |
| Philip Chidera | design | 7 on 0901 — 4 Done, 1 To do (`BVA-I298`), 1 co-owned In progress, 1 co-owned REVIEW/QA | 1 | 0.11 d (n=1) | 1 co-owned (`BVA-I296`, 0.9 d) | — | Two design-shaped items from the new batch reached him (`BVA-I298` solely, `BVA-I296` co-owned) — the first time QA work has been routed to design at filing time rather than after a report asked |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, 10.9 d) | 2 | Eleventh day with no admin-board movement; no `beevia-admin` commit since 22 Sep. The board exists; nobody is using it |

**The two questions for standup:** (1) **Nineteen new bugs arrived overnight and eighteen went to one person — is that triage or a queue?** Ayomikun already declined three of them as mis-routed. (2) **Sprint 0902 — fourth edition asking.** 62 of 68 leaves are open inside a container that expired on Tuesday.

**The three things worth knowing:**

1. **The board is now 56% review queue, and the queue's falling median is an illusion.** 38 of 68 leaves are in REVIEW/QA. The median age dropped from 6.4 days to **2.3** — but nothing left the queue, nothing was accepted, and 16 items arrived in the last two days. Split by owner the queue is still two queues: Ayomikun's 20 items have a median of **7.4 days** and an oldest of 16.9; David's 23 have a median of 0.9. The seven-item Notification block submitted on 8 September is now **16.9 days old** and remains the oldest thing on the board. A headline median that falls while the oldest item keeps ageing is measuring arrivals, not throughput.

2. **The backend fixed a duplicate-account bug, and the route-level audit could not see it.** `feat/contact-sync-normalisation` replaced the hand-rolled E.164 regex with `libphonenumber-js`. The old pattern accepted `+23408089421407` — a Nigerian number with its trunk `0` left in after the country code — which E.164 says is the same person as `+2348089421407`, and a unique index stored both happily. **That is where duplicate accounts came from.** Six endpoints now accept locally-typed numbers with an optional `countryCode`, and `GET /conversations` gained ordering rules and three response fields. Nine operations changed contract; **no route was added, removed or renamed**, so the audit reported `beevia-api` clean. Both specs were corrected by hand (§3.1–3.2). Third consecutive cycle for this pattern.

3. **The mobile client is checking its contract against a copy of the spec that is 27 operations stale — and it has already produced a wrong claim in a merged PR.** `beevia-mobile` vendors `api-docs/openapi.yaml`, last touched 21 September. It is missing every `/cards` route, all three `/topups` routes, `/wallets/banks`, `/wallets/resolve-account` and eight more; its `LedgerEntry` has neither `name` nor `counterparty_name`. PR #36 added three of those endpoints to a drift-suppression allowlist on the stated grounds that they "aren't yet declared in `openapi.yaml`" — **all three are declared, and have been for weeks.** This is the direct, mechanical reason `BVA-I262` cannot be finished on the client: the fields its fix needs are not in the contract the client reads (§3.4, `suggestions.md` §5.10).

**If you read nothing else:** nineteen new bugs went to one developer overnight, the queue passed half the board, the backend closed a duplicate-account defect the audit was structurally blind to, and the one thing that has never happened on this project — somebody reviewing somebody else's work — still has not.

---

## 1. Sprint 0901 — closed 22 Sep, still the working board

**77 items: 68 leaves + 9 parent Stories.** All figures below are leaves unless stated. The sprint's dates ended 22 September; nothing succeeds it.

### 1.1 Status distribution

| Status | 24 Sep | 25 Sep | Δ |
|---|---:|---:|---:|
| REVIEW/QA | 25 | **38** | **+13** |
| To do | 6 | **17** | **+11** |
| In progress | 8 | **5** | −3 |
| BLOCKED | 4 | **2** | −2 |
| Done | 6 | **6** | **0** |
| **Total leaves** | **49** | **68** | **+19** |

The nineteen additions are a single QA batch (§1.2). Beneath them the internal movement is real but one-directional: ten items entered REVIEW/QA, **zero left it**, and Done has not moved in seven editions.

### 1.2 The third QA batch — 19 items in 57 minutes

All nineteen were created by board administration on **24 September between 14:38 and 15:35 UTC**, and all nineteen landed directly in sprint 0901 rather than a backlog.

| Assigned to | Items |
|---|---:|
| David Samuel (solely) | **17** |
| David Samuel + Ayomikun Araoye | 1 (`BVA-I289`) |
| Philip Chidera + David Samuel | 1 (`BVA-I296`) |
| Philip Chidera (solely) | 1 (`BVA-I298`) |

By subject they are overwhelmingly client-surface defects: eight are explicit design-mismatch bugs (icon sizes, spacing, label position, divider styling, contrast, contact-name styling), four are conversation-list behaviour (ordering, offline availability, empty chats, date grouping), and the remainder cover calling (`BVA-I295`, no ringback tone), encryption UX (`BVA-I292`, missing E2EE notice), virtual cards (`BVA-I300`, `BVA-I301`) and a packaging oddity (`BVA-I305`, the app downloading an unrelated `cy_en.zip` language package).

**This is the third such batch** — 23 September brought twelve (`BVA-I274`–`BVA-I285`), and the two QA rounds before that supplied most of the current queue. The pattern is consistent and the throughput consequence is arithmetic: QA files faster than one developer can clear, and nothing downstream drains.

**One piece of good news in the routing.** `BVA-I298` (message/timestamp contrast) went to Philip alone and `BVA-I296` (date grouping) to Philip and David jointly. Every previous batch sent design-mismatch work exclusively to the mobile developer, and three consecutive editions recommended changing that. This is the first batch where it happened at filing time.

### 1.3 The review queue — 38 items, and the median is lying

Ages are the `actiontime` of each item's last transition into REVIEW/QA, from the activity sidecar.

| | Items | Median age | Oldest |
|---|---:|---:|---:|
| Ayomikun Araoye | 20 | **7.4 d** | **16.9 d** |
| David Samuel | 23 | **0.9 d** | 10.9 d |
| Philip Chidera | 1 | 0.9 d | 0.9 d |
| **Whole queue** | **38** | **2.3 d** | **16.9 d** |

(44 owner-rows across 38 items — six are co-assigned.)

**The headline median has now fallen for three consecutive editions — 7.2 → 6.4 → 2.3 — and not once because anything drained.** Ten items entered in this window and none left. Ayomikun's half of the queue has a median more than eight times David's, and its oldest item, the seven-item Notification block submitted in one sitting on 8 September, has aged another day to **16.9**. Reporting 2.3 days without that split would be actively misleading, which is why the split is here rather than in an appendix.

**Nothing left REVIEW/QA in this window.** The audit raises that as a problem rather than a note, correctly.

### 1.4 The backend developer started triaging — and pushed back in writing

The newly-readable comment trail (see correction #3) shows something the status columns do not. Within half an hour of the new batch landing, Ayomikun:

- **removed himself as owner** from `BVA-I277`, `BVA-I295` and `BVA-I296`;
- commented on `BVA-I295` (*"not sure I understand this please"*) and moved it To do → BLOCKED;
- commented on `BVA-I296` (*"this should be on mobile if I am not mistaken since they have the full conversation"*) and moved it To do → BLOCKED.

Both were then moved back to In progress by board administration within twenty minutes, and `BVA-I296` was re-assigned to Philip and David.

This is the first recorded instance of a developer declining a mis-routed item on this project, and it worked — the item reached the right person the same evening. It is worth naming because the standing complaint in these reports is that the board records outcomes but never reasoning; here the reasoning is on the item, in writing, and it changed the routing.

The full comment history on sprint 0901 is nine entries, of which six are David asking for screenshots or explaining that a reported bug is intended behaviour (`BVA-I260`: *"we are not doing a liveness check hence it's not a live facial recognition. By extension it's not a bug per se"*). **Several QA items are being disputed on their merits and the board carries no field for that** — the dispute lives in a comment while the status says BLOCKED or In progress.

### 1.5 Everything that moved

Fifty-four audit entries in the window, of which nineteen are the batch creations. The status movement:

| When (UTC) | Item | Move | Actor |
|---|---|---|---|
| 24 Sep 13:30 | `BVA-I281`, `BVA-I262`, `BVA-I274` | BLOCKED → In progress | David Samuel |
| 24 Sep 15:25 | `BVA-I262` | In progress → REVIEW/QA | Ayomikun Araoye |
| 24 Sep 15:26 | `BVA-I279`, `BVA-I280` | BLOCKED → In progress | Ayomikun Araoye |
| 24 Sep 16:03 | `BVA-I281` | In progress → REVIEW/QA | Ayomikun Araoye |
| 24 Sep 16:03 | `BVA-I295` | To do → BLOCKED, with a comment | Ayomikun Araoye |
| 24 Sep 16:04 | `BVA-I289` | To do → REVIEW/QA | Ayomikun Araoye |
| 24 Sep 16:04–16:08 | `BVA-I263`, `BVA-I282`, `BVA-I274`, `BVA-I284`, `BVA-I278`, `BVA-I276`, `BVA-I283` | In progress / To do → REVIEW/QA | board administration |
| 24 Sep 16:05 | `BVA-I296` | To do → BLOCKED, with a comment | Ayomikun Araoye |
| 24 Sep 16:05–16:06 | `BVA-I279` | In progress → BLOCKED → In progress | board administration, then Ayomikun |
| 24 Sep 16:25–16:26 | `BVA-I280` | In progress → BLOCKED → In progress → REVIEW/QA | board administration, then Ayomikun |
| 24 Sep 16:26 | `BVA-I295`, `BVA-I296` | BLOCKED → In progress | board administration |
| **25 Sep 07:44** | `BVA-I301` | To do → REVIEW/QA | **David Samuel** |
| **25 Sep 11:10** | `BVA-I305` | To do → REVIEW/QA | **David Samuel** |
| **25 Sep 12:58** | `BVA-I294` | To do → In progress | **David Samuel** |

**`BVA-I262` reached REVIEW/QA at 15:25 on 24 September** — the item whose server half merged the previous lunchtime. It was moved there by the backend developer, not the mobile one, and **there has been no `beevia-mobile` commit implementing it**: the only mobile commit in the window is PR #36, a dependency and test merge. Combined with §3.4 — the client's vendored contract does not contain `name` or `counterparty_name` — the most likely reading is that the backend marked its own half done and the client half has not started. Yesterday's recommendation #1 asked for one comment on the item to settle this; no comment was added.

### 1.6 What is open

Seven leaves are open (5 In progress, 2 BLOCKED) and **all seven are David's**, two co-assigned.

| Item | Status | Age | Owners |
|---|---|---:|---|
| `BVA-I260` | BLOCKED | 2.1 d | David |
| `BVA-I275` | BLOCKED | 2.1 d | David |
| `BVA-I277` | In progress | 0.9 d | David |
| `BVA-I279` | In progress | 0.9 d | David, **Ayomikun** |
| `BVA-I295` | In progress | 0.9 d | David |
| `BVA-I296` | In progress | 0.9 d | **Philip**, David |
| `BVA-I294` | In progress | 0.0 d | David |

Nothing here exceeds David's 0.96-day median cycle by enough to call it stuck. The two BLOCKED items are both **disputed rather than blocked** — `BVA-I260` and `BVA-I275` each carry a comment from David arguing the reported behaviour is intended (§1.4). They have been in that state for 2.1 days with no reply on the item.

---

## 2. Admin dashboard board — `0901-admin`

**12 items: 8 leaves + 4 parent Stories. Unchanged in every respect, for the eleventh consecutive day.**

| Status | Leaves |
|---|---:|
| Done | 6 |
| In progress | 2 |

| Item | Status | Owner |
|---|---|---|
| `BVA-I5` · `BVA-I11` | Done | Ayomikun Araoye |
| `BVA-I6` · `BVA-I12` · `BVA-I15` | Done | Promise Udo |
| `BVA-I14` | Done | Unassigned |
| `BVA-I8` — Report Data Query | **In progress, 10.9 d** | Ayomikun Araoye |
| `BVA-I9` — Report Content Display | **In progress, 10.9 d** | Promise Udo |

**Last activity of any kind: 14 September 14:53 UTC — 10.9 days ago.** `beevia-admin` itself has had no commit since 22 September (2.9 days). The blind spot this pipeline reported for eleven editions is closed — the board exists, it has items, Promise has a row — and it has been replaced by a simpler problem: the board is not used. Sprint 0901-admin closed 22 September with no successor, like the main board.

Its counts are never added to the main sprint's.

---

## 3. API surface and spec drift

**Audit: route level clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18. Run against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-25`, because three working trees are still `diverged`.

**And, for the third cycle running, the clean result is the finding.** Yesterday it was four response bodies; today it is nine operations across two subsystems.

### 3.1 `feat/contact-sync-normalisation` — phones are parsed now, not pattern-matched

Merged 24 September (`beevia-api` #56, with the address-book re-linking half in `beevia-db-schema`, released as v0.0.37/v0.0.38).

Six operations — `POST /auth/register`, `/auth/otp/request`, `/auth/otp/verify`, `/auth/login`, `/users/lookup` and `/contacts/sync` — previously demanded strict E.164. They now accept a number as typed (`08089421407`) alongside `+2348012345678`, each with an optional `countryCode` region hint; where it is omitted the caller's own account country is used. Normalisation happens in the schema at object level, so no handler ever sees an unnormalised number.

**The reason this matters is a data-integrity bug, not ergonomics.** The retired regex `^\+[1-9]\d{6,14}$` asks whether a string is a plus followed by 7–15 digits. It says nothing about whether those digits are dialable, and in particular it accepts `+234` with a Nigerian number pasted on in *national* format — `+23408089421407` — because the trunk `0` is just another digit to a regex. E.164 requires that `0` to be dropped, so the same person typing their own number the two obvious ways produced two different strings and the unique index stored both as separate accounts. The code comment says so in as many words, and `phone.util.ts` now repairs that specific shape explicitly before falling back to a parse failure.

**The one subsystem left behind is the one that moves money.** `payments.dto.ts` still declares its own `z.string().trim().min(6).max(20)` and imports nothing from `phone.util.ts`. `POST /payments/send` and `POST /payments/request` are now the **only** phone inputs in the service that are neither validated nor normalised — so a payer who types a local number there gets no resolution, where every other screen in the app now would. This is `suggestions.md` §3.6, escalated today; both fields carry the looseness as a `description` in `openapi.yaml` so no client is misled in the meantime.

### 3.2 The inbox gained ordering rules that were never written down

Two further merges (#53, #54) changed `GET /conversations`:

- **A direct conversation is listed only once a message has been sent in it.** Creating one does not put it in the inbox; groups are listed from the moment you are added. A client must navigate off the create response rather than waiting for the list to catch up — a behaviour no client author could have known from the old spec.
- **Rows are ordered by a new `last_message_at`**, which is deliberately *not* cleared when the previewed message is deleted, so a row keeps its place instead of falling to the bottom.
- **`last_message` is `null` in three distinct cases**: deleted for everyone, deleted by the caller for themselves, or at/below the caller's `cleared_seq` watermark.

While documenting that, two further fields turned up that the server has **always** sent and the spec never listed: `hidden_at` (the per-user hide) and `cleared_seq` (the clear-chat watermark). A client generating models from `openapi.yaml` has never had access to a watermark the API was already returning on every conversation row.

Four of the new QA items — `BVA-I289` (list not sorted by recent activity), `BVA-I294` (list not available offline), `BVA-I280` (empty chats and wrong last message) and `BVA-I296` (missing date grouping) — are all in this exact area, and three of them were filed *after* these fixes merged.

### 3.3 Spec and document changes this cycle

| File | Change |
|---|---|
| `openapi.yaml` | New `TypedPhone` schema; `phone` switched to it on six request bodies, each gaining an optional `countryCode`. `Conversation` gains `last_message_at`, `hidden_at`, `cleared_seq`. `GET /conversations` description rewritten with the listing and null-preview rules. A malformed `RegisterRequest.countryCode` description repaired — an unquoted comma in a flow mapping had been silently truncating it and creating a junk key. `payerPhone` now carries the same looseness note as `recipientPhone`. |
| `openapi.proposed.yaml` | `LedgerEntry` realigned to the implemented definition (correction #4); `Phone` description realigned. |
| `api-rfc.md` | New §5.10 recording both contract changes and the payments exception. |
| `suggestions.md` | **§5.2 marked resolved** — the E.164 regex now exists in exactly one file. **§3.6 escalated** — payments is the last unparsed phone input. **New §5.10** — the vendored client spec (§3.4), promoted to item 3d in §8. |

No route was added, moved or deleted; `openapi.admin.yaml` needed no change (`beevia-admin-api` has had no commit since yesterday's HEAD); no `x-beevia-*` marker was introduced. The audit re-ran clean after the edits — and this time that was verified rather than asserted.

### 3.4 The client is reading a different contract

`beevia-mobile` vendors its own copy of the consumer spec at `api-docs/openapi.yaml`, and `test/mock/spec_contract_test.dart` validates the mock server against **that file**. It was last updated on 21 September.

Diffed against `openapi.yaml` at `origin/main` today, the vendored copy is **missing 27 of 137 operations**: all thirteen `/cards/*` routes, all three `/topups` routes, `/wallets/banks`, `/wallets/resolve-account`, both `/wallets/transfers` reads, `GET /translate/languages`, the three per-conversation translation-preference routes, two beneficiary routes and `POST /webhooks/paystack`. Its `LedgerEntry` predates the transaction-naming work and has neither `name` nor `counterparty_name`.

Two consequences:

1. **The contract test passes while the client codes against a week-old API.** It is not a weak test — it has a `nowDeclared` guard that fails when an allowlisted entry reappears in the spec — but every comparison it makes is against a file that no longer describes the service.

2. **It produced a false statement in a merged PR.** PR #36 added `/wallets/banks`, `/wallets/resolve-account` and `/cards` to a `knownSpecDrift` allowlist because they "aren't yet declared in `openapi.yaml`". All three **are** declared in the canonical spec and have been for weeks; they are absent only from the vendored copy. Three endpoints the API documents are now on a list that suppresses drift warnings about them.

**This is the mechanical answer to why `BVA-I262` is stuck.** The mobile fix needs `name` and `counterparty_name` on a statement row. The contract the mobile repo reads does not contain them, and its own test will not complain. Recorded as `suggestions.md` §5.10.

---

## 4. PRD gap

No change. The four MVP gaps — international KYC tier, multi-currency/FX settlement, virtual cards beyond listing, and consent management — are where they were.

`PaymentService.activeNgn()` is re-verified present at `payment.service.ts:506`, called from lines 70, 128 and 288. While it exists, FX has not started, whatever else ships. `StubTranslateAdapter` is still bound at `translate.module.ts:23`.

One correction carried down from the overview: **`GET /translate/languages` is implemented** and has been since 22 September. It lists the languages the service supports; it does not translate anything. `/translate/batch` remains the only proposed `/translate` operation. The capability gap is unchanged — it was never the endpoint inventory, it is that the server-side port is a stub and the shipped client design translates on-device and bypasses it.

---

## 5. Team performance — detail

All flow figures are from the activity sidecars (`actiontime` of the relevant transition), never from `Last Modified`. Commit counts are non-merge commits on `origin/main` in the last 7 days, summing each person's git identities.

### 5.1 Ayomikun Araoye — backend + admin API

**35 commits in 7 days** (`beevia-api` 15 across both identities, `beevia-db-schema` 14, `beevia-admin-api` 6) — the highest figure this report has recorded for anyone, up from 25 yesterday. The window's work is the phone-normalisation feature across two repos, two inbox correctness fixes, and a migration of all three backend repos onto self-hosted CI runners.

**Twenty of his items are in REVIEW/QA, fifteen solely his.** Their median age is 7.4 days and the oldest is 16.9. He has zero solely-owned items in progress on the main board and one on the admin board (`BVA-I8`, In progress for 10.9 days). Median cycle time In progress → REVIEW/QA is 0.96 days (n=9).

**New this cycle: he is triaging.** He moved six items himself, declined three mis-routed QA items by removing his own ownership, and left the first two explanatory comments a backend developer has put on a QA item (§1.4). One of them re-routed `BVA-I296` to design the same evening.

**The queue profile remains a process finding, not a personal one**: a developer submitting at this rate into a queue with no reviewer accumulates exactly this shape, and nothing he can do changes it.

### 5.2 David Samuel — mobile

**23 submissions to REVIEW/QA in 7 days, median cycle 0.96 days (n=18)** — the highest submission count on the board, though many are To do → In progress → REVIEW/QA inside one triage session, which compresses the figure.

**He now owns 40 of the 68 leaves**, including all seven open items and 17 of the 38 queue entries solely. Eighteen of the nineteen new QA items were assigned to him. Against that: **three mobile commits in seven days**, and the only one in this window is a dependency and test merge authored by the project owner.

The gap between 40 owned items and 3 commits is the single most important number in this report, and it is not a statement about effort. It is what happens when one QA pipeline files into one developer with no second implementer and no reviewer. **`BVA-I262` is the concrete case**: its server half shipped, the item sits in REVIEW/QA, no client commit implements it, and the contract the client reads does not contain the fields it needs (§3.4).

### 5.3 Philip Chidera — design

**Two items from the new batch reached him at filing time** — `BVA-I298` (message/timestamp contrast) solely, and `BVA-I296` (date grouping) jointly with David after Ayomikun re-routed it. `BVA-I274` (App Logo and Branding), picked up two days ago, reached REVIEW/QA yesterday.

This is the first batch in which design-shaped work was routed to design as it was filed rather than after a report asked for it — the narrow half of a recommendation carried for four editions. The broader half is still open: the eight design-mismatch bugs from the earlier batches remain David's alone, and the new batch added six more of the same kind to his name.

No commits; design work does not land in these repositories.

### 5.4 Promise Udo — admin dashboard

2 commits in 7 days, both on 22 September (wallets summary/detail integration). No commit since — `beevia-admin` is 2.9 days stale. Four items on the admin board, one In progress for 10.9 days, and **no board action by him anywhere, ever**; every transition on the admin board was made by someone else.

The reporting gap is closed — the board exists, he has a row, his work is visible in `beevia-admin`. What remains is that the board's 10.9-day silence carries no information either way about whether the work is progressing.

### 5.5 Weekly submission trend (sprint 0901, transitions into REVIEW/QA)

| ISO week | Submissions |
|---|---:|
| 2026-W37 | 9 |
| 2026-W38 | 15 |
| 2026-W39 (partial) | **25** |

Input is accelerating sharply — W39 is already 67% above W38 with days to run. **Acceptances over the same three weeks: one** (`BVA-I268`, 16 September, closed by its own owner). When submission triples and acceptance is one self-closure, the bottleneck is not the developers; no reviewing role is staffed, and this report has now said so in nine consecutive editions.

### 5.6 What this does not measure

- **No estimation points on any of 77 items** (nor on 12, nor on 64). There is no workload normalisation, so item counts say nothing about who is carrying more. Sixteenth edition.
- **Commit counts reward small commits; cycle times reward small items.** Neither measures difficulty or quality, and 35 backend commits against 3 mobile ones is not a statement about relative output — this cycle's mobile work was a merge of someone else's branch.
- **Co-assignment is counted for both owners**, so per-person board counts sum to more than the board.
- **Nothing here measures correctness.** No build, test or lint was run by this pipeline in any repository.

---

## 6. Previous recommendations — where they stand

| Recommendation from 24 Sep | Status on 25 Sep |
|---|---|
| **1. Tell David that `BVA-I262`'s server half is on `main`** | ❌ **Not done, and the gap is now measurable.** No comment was added. The item was moved to REVIEW/QA by the *backend* developer at 15:25; no mobile commit implements it; and the vendored client spec does not carry the two fields the fix added (§3.4) |
| **2. Decide `origin/BVA-I239` — it is live work, not lost work** | ✅ **Done.** Merged as PR #36 on 24 Sep at 16:32 UTC and the branch deleted. `beevia-mobile` now has **zero** unmerged feature branches and the nine Dependabot branches are gone. First outright resolution in four editions |
| **3. Open sprint 0902 on both boards** | ❌ **Not done.** Zoho still lists only `0901, 08-01, 0702, 0701` and `0901-admin`. Fourth edition; 62 of 68 leaves are open in an expired container |
| **4. Review Ayomikun's sixteen** | ❌ **Not done.** It is now twenty, median 7.4 d, oldest 16.9 d. Nothing left the queue in this window |
| **5. Generate the OpenAPI document in CI and diff it** | ❌ **Not done, and it escalates for the third consecutive day.** Today it would have caught nine operations' worth of request/response change. §5.10 adds the client-side twin of the same argument |
| **6. Give the three backend-blocked bugs their own items** | ❌ **Not done** — and the ownership moved the other way. `BVA-I279` and `BVA-I280` are still co-assignments; Ayomikun additionally *removed* himself from three new items rather than acquiring schedulable ones |
| **7. Pull Philip onto the eight Figma-mismatch bugs** | 🟡 **Partially, and structurally for the first time.** Two of the nineteen new items were routed to design at filing time (§5.3). The original eight remain David's, and six more of the same kind were added to him |
| **8. Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`; bring `beevia-db-schema` onto it** | ❌ **None of the three done.** `beevia-admin` still has no `.github` directory at all; `beevia-mobile` has three workflows and no security scan; `beevia-db-schema` still carries the three standalone copies |
| **9. Confirm branch protection / secret scanning / Dependabot in the GitHub UI** | ❌ Not done, still unobservable from here. Seventh edition |
| **10. Estimation points on sprint 0902 as it is created** | ❌ Not done — there is still no sprint 0902, and the board grew by 19 unpriced items |
| **11. Carried: `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; the translation decision** | ❌ **None done.** `docs/` is still absent from `origin/main`; `beevia-admin-api` has had no commit at all since yesterday, so §4.7 is unchanged by definition; no decision record exists and `StubTranslateAdapter` is still bound |

**One of eleven resolved outright** — and it is the one that had been open longest.

---

## 7. What I would do this week

1. **Stop the mobile repo reading a stale spec — today.** This is new, it is cheap, and it is currently blocking a bug fix. Either delete `beevia-mobile/api-docs/openapi.yaml` and fetch the canonical file in CI, or add a job that fails when the two differ. While it stands, the client's contract test certifies conformance to a document that is 27 operations out of date, and PR #36 has already recorded a false claim because of it (§3.4). Then re-check the three entries added to `knownSpecDrift`: all three are declared and should come straight back off the list.
2. **Say out loud who reviews.** 38 of 68 leaves are in REVIEW/QA; one item in the project's history has left that column forward, and its own owner closed it. This is the ninth consecutive edition making this point and the queue has grown every time. It does not need a process — it needs one name against the word "reviewer", or an explicit decision that REVIEW/QA means "done" and the column is renamed.
3. **Open sprint 0902 on both boards, and decide what carries over as you do it.** Fourth edition. Nineteen new items just landed in a container that expired on Tuesday, and there is nowhere else to put the next nineteen.
4. **Decide whether nineteen bugs to one person is the plan.** Eighteen of the new batch went to David, who already owned 21 items and has three commits this week. Ayomikun has 35 commits and no schedulable work of his own. If the mobile client is genuinely one-person, the batch size is the thing to change; if it is not, some of these have a second owner.
5. **Reply to the two disputed items.** `BVA-I260` and `BVA-I275` have been BLOCKED for 2.1 days carrying written arguments from David that the reported behaviour is intended. Nobody has answered on the item. A QA disagreement that sits in a comment while the status says BLOCKED is invisible to every count in this report.
6. **Bring `payments.dto.ts` onto `phone.util.ts`.** One import and one deleted line. After yesterday's merge the two money-moving endpoints are the only phone inputs in the service that are not parsed or normalised, which is precisely backwards (§3.1, `suggestions.md` §3.6).
7. **Generate both services' OpenAPI documents in CI and diff them against the committed files.** Unchanged from yesterday and the day before, and now three-for-three on cycles where it would have caught the day's most serious change. `openapi-schema.spec.ts` already builds the document; the diff is a few more lines in a file that exists.
8. **Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`, and bring `beevia-db-schema` onto it.** Unchanged. `beevia-admin` still has no CI of any kind, which also blocks the branch-protection work.
9. **Estimation points on sprint 0902 as it is created.** Seventeenth edition. The board is now 68 unpriced leaves, most of them QA bugs of wildly varying size.
10. **Carried, unchanged:** the `reports.service.ts` read-scoping fix (twelfth edition); the Module 4 A-then-B decision record; restoring or retiring `beevia-api/docs/`; and writing the translation decision down.

---

## Appendix — method and readiness rubric

### MVP readiness — ≈67% (estimate; 66.72, unchanged)

**Target 2026-09-01 (provisional) · the target date passed twenty-four days ago.** Weights frozen — **no methodology change this edition.** Scores measure build, not acceptance.

**No score moved, and two evidence lines were corrected rather than re-scored.** The window's engineering was substantial — a duplicate-account defect closed, inbox ordering fixed, a seven-week dependency branch merged — but the rubric asks whether a *capability* exists, and none of it adds one.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Inbox ordering, deleted-preview and clear-chat-watermark fixes merged (§3.2) — correctness on an existing surface, not new capability. No change to crypto, keys or sockets |
| 2 | Voice & video calling | 8 | 0.80 | 0 | No `/calls` change. `BVA-I295` (no ringback tone) is a new QA bug; **board status does not score** |
| 3 | Message translation | 7 | 0.60 | **0 — held, evidence corrected** | **Correction:** `GET /translate/languages` is **implemented**, not proposed — it shipped 22 Sep and the 23/24 Sep editions were wrong to list it as a blocker. Only `/translate/batch` is proposed. The score is unchanged because neither endpoint was ever the blocker: `translate.module.ts:23` still binds `StubTranslateAdapter`, and the shipped client design translates on-device via ML Kit and bypasses the server entirely |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change. Registration now accepts locally-typed phones, which improves onboarding input handling without altering the verification ladder |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` re-verified at `payment.service.ts:506`, called from 70/128/288. The server remains single-currency — the clause holding this line back |
| 7 | Send / request / receive in chat | 12 | 0.95 | 0 | Re-verified: `payment_events.dart` emits `payment.request`/`accept`/`decline`/`cancel` over the socket, matching `messaging.gateway.ts`; the send path posts `/payments/transfer` from `wallet_service.dart:167`. The REST `/payments/send` and `/payments/request` being unused by the client is expected — they are the HTTP mirror of the socket commands (`api-rfc.md` §2.8), not a second flow. **Held back:** still no REST read path for a single payment |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only; `activeNgn()` confirmed present |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card endpoint wired since yesterday. `api_url.dart:26` still carries only `cardsUrl = "/cards"`; `reveal`, `freeze`, `fund` and the rest have no client constant — and all thirteen `/cards` routes are absent from the spec the client reads (§3.4) |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | The rubric line scores **dashboard modules landed in `beevia-admin/src`**, and `beevia-admin` has had no commit since 22 Sep |
| | **Weighted total** | **100** | **66.72** | **0.00** | **≈67%** |

Mobile screen inventory re-counted at **53** (51 under `lib/features/*/screens/` plus two call screens), against ~39 when the rubric was written on 2026-08-07.

### What this report cannot tell you

- **What the next sprint is called or when it starts.** Nothing is open on either project.
- **Whether the nineteen new QA items are reproducible or duplicates.** Several overlap with fixes that merged the same day (§3.2), and this pipeline runs no build.
- **Whether `BVA-I262`'s client half has been started.** No mobile commit references it; the item is in REVIEW/QA; no comment records what was done.
- **Whether the disputed items (`BVA-I260`, `BVA-I275`) are bugs.** Two written arguments, no reply, and the report cannot adjudicate a design question.
- **Whether any of the phone-normalisation or inbox code works.** No `npm`, `node` or `flutter` command was run; nothing was built or executed, including the substantial new test code that came with both merges.
- **Whether branch protection, secret scanning and Dependabot are on**, and on which repos — the `gh` token here gets `404` on every repo's rules endpoint. Seventh edition.
- **Velocity for any of the three sprints** — 0 of 77, 0 of 12, 0 of 64 items estimated.
- **What `origin/update-fixes` is for.** A new `beevia-mobile` branch, one commit ahead of `main` and two behind, created 24 September. Not yet a divergence worth flagging; noted so the next edition can compare.

### Method

**Pipeline.** `beevia-refresh`: sprint-name discovery on both projects (confirming no successor sprint) → main board export (64 items, sprint 08-01, exit 0) → admin board export with `--sprint 0901-admin` (12 items, exit 0) → read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/` (77 items, exit 0) → fast-forward sync (**1 repo advanced — `beevia-mobile` +1 commit; 1 already current; 3 refused as `diverged`**; exit 0) → audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-25`, with the two 0901 scratch exports copied in so the deterministic `SINCE` delta covers the *active* sprint rather than the frozen one → item-by-item diff of today's 0901 export against the 24 Sep one → activity-sidecar sweep for the window → content reads of the phone-normalisation, contacts and inbox paths, and of the vendored client spec → spec and document edits → audit re-run (clean, verified) → this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages are the `actiontime` of each item's last transition into `REVIEW/QA`; cycle times are `In progress` → `REVIEW/QA` pairs; WIP ages are the entry into the current status. Completions are matched on all three of Zoho's action names (`Updated the status`, `Item Completed`, `Item Reopened`) — filtering on the substring `status` alone silently drops every completion the project has recorded, which is how correction #1's error was originally introduced.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is performed by a non-contributor whose transitions are reported without naming the actor; thirty-one of this window's fifty-four audit entries are theirs, including all nineteen item creations.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran; no repository was reset, rebased or cleaned; no sub-repo file was edited; the sync's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-25.html`, `web-report/index.html`, `openapi.yaml`, `openapi.proposed.yaml`, `api-rfc.md`, `suggestions.md`; new board exports for 25 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`. **`openapi.admin.yaml`, `openapi.admin.proposed.yaml` and `admin-api-rfc.md` needed no change** — `beevia-admin-api` has had no commit since yesterday's HEAD.

**Degraded inputs.**

- **No open sprint on either board.** Sprint 0901 and 0901-admin both closed 22 September with no successor. Every sprint figure describes an expired container that is still being worked in. Fourth edition.
- **Three repositories remain unsynced** — `beevia-api`, `beevia-admin-api`, `beevia-db-schema` still `diverged` (`ahead 1`, behind 55 / 34 / 43, up from 40 / 34 / 27 yesterday). Every backend code claim is made against `origin/main` via the shadow, never the working tree. `beevia-api` and `beevia-db-schema` are drifting further each day.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, zero activity). All sprint-0901 figures come from the scratch export, and the audit's board section was run against that export rather than the in-repo one.
- **GitHub settings are unobservable.** Branch protection, secret scanning, push protection and Dependabot alerts are reported from the board and commit messages only.
- **Whether any CI run passed is unknowable from a clone.**
- **The export's "no source key" warning fired on `Epic` again** and is the known 50-row sampling artefact, not an OAuth scope gap.
- **Repository integrity was not hash-swept this cycle.**

**Window.** 24 Sep 13:30 UTC → 25 Sep 12:58 UTC. All `actiontime` and board figures are UTC; `git log` was read with local timestamps converted where quoted.
