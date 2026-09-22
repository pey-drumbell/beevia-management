# Beevia — Project Status

**As of 2026-09-18** · Sprint **0901** (3 Sep → 22 Sep) — **day 16** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 16** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-18.csv` + `beevia-activity-2026-09-18.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-18.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (35 items) + sidecar; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. Window **17 Sep 14:01 UTC → 18 Sep 14:03 UTC** (~24 hours, Wed→Thu).

---

## Quick overview

> **The project shipped 23 commits after a day with none — and one of them took production down.** The three backend repos went from silent to the busiest day in this record: Trust & Safety moderation built end-to-end on the server, NestJS 12 across all three, Semgrep CI landed. Then the NestJS 12 release **never bound `:3000`, the health check failed and the deploy rolled back** — one optional field (`sentAt: z.coerce.date()`) that the new Swagger version could not render, throwing inside `SwaggerModule.createDocument()` at boot. **CI was green the whole way**, because nothing in the test suite runs `main.ts`. Fixed an hour later, with a regression test that closes the class rather than the instance. Two other things landed that this report has been asking for: **the E2EE question that has blocked admin Module 4 since 5 August is answered in code on both sides**, and **Semgrep is running on every backend PR**. Against all that, the review queue went from 11 items to **15** and still has never lost a single one, with **four days left in the sprint**.

**Yesterday's first recommendation was not taken, and the consequence arrived within 24 hours.** Yesterday's edition asked for one word to be changed in five security-item descriptions — "every *backend* repository" → "every repository" — because as written they excluded `beevia-admin` and `beevia-mobile`, the two repos with the actual gaps. That did not happen, and Semgrep duly landed in exactly the three backend repos and nowhere else. `beevia-admin` still has **no `.github` directory at all** (4.1 days without a commit); `beevia-mobile` is still missing `secrets-scan`, `supply-chain-guard` **and now `semgrep`**, and still carries nine unmerged Dependabot branches, the oldest 38 days.

**A caveat this report has carried for two editions can now be retired, and the board retired it.** Yesterday's appendix said branch protection and secret scanning "could be substantially done" because GitHub settings leave no trace in a clone. They are not done, and the reason is in a board comment: *"this is done on all backend repos but I cannot add it organisation wide yet as I do not have admin access to the organisation."* **Three of the five security items are gated on a GitHub org-admin grant, not on engineering time.** That is why `BVA-I269` is the first `BLOCKED` item this board has ever carried.

| Measure | 17 Sep | 18 Sep | Δ |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 0 | **22** | **+22** |
| Commits on *any* ref, all five repos, in window | 0 | **23** | **+23** |
| **Production deploys rolled back** | 0 | **1** | **+1** |
| Board transitions, all three boards, in window | 6 | **7** (6 distinct + 1 artefact — §1.2) | +1 |
| New board items created | 5 | **0** | −5 |
| API surface (consumer / admin) | 137 / 47 | 137 / **49** | **0 / +2** |
| Proposed operations (consumer / admin) | 38 / 19 | 38 / **18** | 0 / **−1** |
| Spec drift vs `origin/main` found this cycle | 0 | **3 findings — all reconciled** | §3 |
| Sprint 0901 leaves, total | 26 | 26 | 0 |
| Sprint 0901 leaves To do | 4 | **2** | −2 |
| Sprint 0901 leaves In progress | 5 | **2** | **−3** |
| Sprint 0901 leaves REVIEW/QA | 11 | **15** | **+4 — four in, none out** |
| Sprint 0901 leaves **BLOCKED** | 0 | **1** | **+1 — first ever** |
| Sprint 0901 leaves Done | 6 | 6 | **0** |
| Review-queue median age (0901) | 8.9 d | **8.2 d** | **−0.7 — dilution, not review (§1.4)** |
| Oldest item in the queue | 8.9 d | **9.9 d** | +1.0 |
| `beevia-api` days since a commit | 1.1 | **0.1** | −1.0 |
| `beevia-admin-api` days since a commit | 1.1 | **0.2** | −0.9 |
| `beevia-db-schema` days since a commit | 1.1 | **0.4** | −0.7 |
| `beevia-mobile` `main` days since a commit | 1.9 | **2.9** | +1.0 |
| `beevia-admin` `main` days since a commit | 3.1 | **4.1** | +1.0 |
| `origin/BVA-I239` (new mobile branch) | — | **0.9 d** | new |
| `origin/BVA-I242` tip | static 2.0 d | **static 3.0 d** | +1.0 |
| Admin board: days since *any* activity | 3.0 | **4.0** | +1.0 |
| Ayomikun commits (7d, 2 identities, merged, non-merge) | 28 | **32** | +4 |
| David commits (7d, merged to `main`) | 1 | 1 | 0 |
| Promise commits (7d, merged) | 1 | 1 | 0 |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 35 · 0 / 12 | 0 / 35 · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈61% (61.40) | **≈62% (61.52)** | **+0.12** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **15 on 0901** — 12 REVIEW/QA, 1 BLOCKED, 2 To do · 3 on 0901-admin | **4 leaves, all moved by himself** | **1.5 d** (n=3 — §5.1) | **0 on 0901** — nothing In progress at all · 1 on 0901-admin, 4.0 d | **32** (was 28) | **Wrote essentially the entire cycle.** All 22 merged commits are his. Also: he broke production and fixed it in an hour, **12 of the 15 items in review are his**, and he is the one blocked on org-admin access |
| David Samuel | mobile | 7 on 0901 — 2 In progress, 3 REVIEW/QA, 2 Done | 3 leaves — **2 moved by a non-contributor, 1 by Ayomikun** | 8.1 d (n=2 — §5.1) | 2: `BVA-I229` 3.9 d, `BVA-I238` 2.1 d | 1 merged · **1 on a branch in window** | **Opened a new branch** (`BVA-I239`, l10n, 17 Sep 16:09 UTC) — so not idle. But `BVA-I254`, his Trust & Safety item, **was moved to review by someone else with no mobile commit behind it** (§1.3) |
| Philip Chidera | design | 4 on 0901 — **all 4 Done** | 1 (moved by a non-contributor) | — | **0** | — | Second edition with an empty board. The design half of Trust & Safety is done; the build half is what moved today |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, moved for him 14 Sep, 4.0 d) | 1 | **Zero self-attributed board actions across all three boards, all time** — measured, not inferred (§4). No `beevia-admin` commit for **4.1 days**; the repo still has no CI and is covered by none of the five security items |

**The two questions for standup:** (1) **Who holds GitHub org-admin, and will they spend twenty minutes in the org settings today?** Three security items (`BVA-I269`, `BVA-I272`, `BVA-I273`) cannot be finished by the person assigned to them, and one is already `BLOCKED` saying so. This also decides whether Semgrep — which landed today and works — can ever block a bad merge, because a required status check is a branch-protection setting. (2) **Fifteen items in review, four days to 22 September, and nobody has ever reviewed one — is the plan to sweep, to review, or to roll them?** All three are decisions. Five editions of no decision is the only option with no upside, and the queue grew 36% today.

**The three things worth knowing:**

1. **A green pipeline shipped a release that could not boot.** The NestJS 12 upgrade merged at 10:28 UTC with CI passing; `@nestjs/swagger` 12 derives request schemas from Zod and throws on types JSON Schema cannot express, and `sentAt: z.coerce.date()` — added the previous evening for the disclosed-messages feature — is one. `SwaggerModule.createDocument()` runs at boot, so the process died before binding a port, the health check failed, and the deploy rolled back to the previous release. **The failure mode was the dangerous one**: the app stayed up on old code and nothing looked down. The fix (11:29 UTC) went through a converter with `unrepresentable: 'any'` and a `date` override rather than narrowing the Zod type, explicitly to avoid smuggling a wire-contract change into a crash fix — the right call, and the more expensive one. It also added `openapi-schema.spec.ts`, which builds the document the way `main.ts` does. **That is the important artefact**: CI was green because nothing ran `main.ts`, and now something does. Details in `suggestions.md` §5.8; the rollback itself is reported from the commit message, as this workspace cannot see deploy logs.

2. **Admin Module 4's E2EE deadlock is resolved in code, on both sides, and the client is the missing half.** `admin-api-rfc.md` §5.1 has said since 5 August that the dashboard spec's "reported messages" is unbuildable — chat is E2EE and the server holds no key — and offered three options. Last night both halves of **Option B** shipped: `POST /conversations/{id}/report` now accepts up to 20 plaintext messages the *reporter* chose to disclose plus a `blockContact` toggle (one transaction, count frozen at filing, group blocks refused rather than guessed), and `GET /admin/chats/reports/{reportId}` returns them alongside a new `PATCH` that records a review decision. The server still decrypts nothing. **But the Flutter client still posts `{"reason": reason}` and nothing else** — verified on `main` and on the unmerged `BVA-I239` branch alike — so every report reaching the new queue will arrive with `message_count: 0` and an empty `messages` array. The board item for the client half (`BVA-I254`, "Update Report Sheet, Add Message Count, Build Confirmation") is **in REVIEW/QA**, moved there by the backend lead, with zero mobile commits behind it (§1.3).

3. **The review queue grew by four and has still never lost an item — and its median age went *down*, which means nothing.** 11 → 15 items. The median fell 8.9 → 8.2 days purely because four fresh items diluted it; every one of the original eleven is a day older, and the oldest is now **9.9 days**. The seven-item Notification block has not moved since 8 Sep 16:02. Ayomikun now has **zero items In progress** and twelve in review, which means the pipeline is not blocked on him writing code — it is blocked on nobody reviewing. That is a process finding, not a personal one, and it is now the single largest risk to 22 September.

**If you read nothing else:** the team's output today was excellent and the two hardest problems on this list moved — the E2EE deadlock and SAST. What is left is not engineering capacity. It is one permission grant, one client-side commit, and somebody reviewing fifteen items in four days.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

**35 items — 26 leaves, 9 parent Stories.** Unchanged in size; all the movement was internal. Day 16 of 20, **four days remain**.

| Status | Leaves | 17 Sep | Δ |
|---|---:|---:|---:|
| To do | 2 | 4 | −2 |
| In progress | 2 | 5 | **−3** |
| **BLOCKED** | **1** | 0 | **+1 — first ever** |
| REVIEW/QA | **15** | 11 | **+4** |
| Done | 6 | 6 | **0** |

| Epic | Leaves |
|---|---:|
| `Language` | 10 |
| `Notification` | 7 |
| `security` | 5 |
| (none) | 4 |

**Done has not moved in three editions.** Everything that happened today moved work *into* review or *into* blocked. Six of 26 leaves are Done on day 16 of 20.

### 1.2 Who actually moved each item

All seven activity entries in the window were **Ayomikun's own** — the first edition where every transition on this board was self-attributed rather than made by a board administrator.

| Time (UTC) | Item | Transition | Assignee |
|---|---|---|---|
| 18 Sep 02:38 | `BVA-I271` | In progress → REVIEW/QA | Ayomikun |
| 18 Sep 02:41 | `BVA-I269` | In progress → **BLOCKED** | Ayomikun |
| 18 Sep 03:01 | `BVA-I253` | To do → REVIEW/QA | *(parent Story)* |
| 18 Sep 03:01 | `BVA-I254` | To do → REVIEW/QA | **David** |
| 18 Sep 03:01 | `BVA-I255` | To do → REVIEW/QA | Ayomikun |
| 18 Sep 03:06 | `BVA-I270` | *comment* — the org-access blocker | Ayomikun |
| 18 Sep 04:34 | `BVA-I270` | In progress → BLOCKED → REVIEW/QA | Ayomikun |

The `BVA-I270` double transition is six seconds apart and is an artefact of a corrected click, not two events. Counted once everywhere in this report.

### 1.3 Trust & Safety shipped — and one of its three items has no code

`BVA-I253` (parent) and its two children went To do → REVIEW/QA together at 03:01 UTC. The parent and one child are genuinely built; the other is not.

| Item | Assignee | Claim | Code found at `origin/main` |
|---|---|---|---|
| `BVA-I255` Report Submission, Storage & Actions | Ayomikun | backend | ✅ **Built.** `beevia-db-schema` migration (moderation state + disclosed-message evidence), `beevia-api` accepts `messages`/`blockContact`, `beevia-admin-api` serves detail + review. Three repos, one night |
| `BVA-I254` Update Report Sheet, Add Message Count, Build Confirmation | **David** | mobile | ❌ **Not found.** `chat_service.dart` still posts `data: {"reason": reason}`. No `messages`, no `blockContact`, no count picker — on `main` or on either open branch |

The only occurrence of `blockContact` anywhere in `beevia-mobile` is a localised UI label (`"blockContact": "Block Contact"`) for the pre-existing standalone block action on `origin/BVA-I239` — not the new report field. `messageCount` appears nowhere in `lib` on any ref.

**Two things follow, and the second is the one that matters.** First, an item was moved to review by someone who does not own it, against a repo that has no commit for it — which is the "wired vs stub" gap this pipeline is explicitly built to catch. Second, and more consequential: **the most valuable part of the new moderation feature has no producer.** A moderator opening the new report detail screen will see an empty evidence list for every report filed by today's app, and will reasonably conclude the feature is broken rather than unfed.

### 1.4 The review queue — 15 items, and the median is now misleading

| Age | Items |
|---|---|
| 9.9 d | `BVA-I246`–`BVA-I252` — the seven-item Notification block, unchanged since 8 Sep 16:02 |
| 8.2 d | `BVA-I231` Preference Storage & Precedence Logic |
| 4.0 d | `BVA-I245` Backend String Bundles & Selection Logic |
| 3.9 d | `BVA-I233` Build Both Screens · `BVA-I243` String Extraction & Bundle Switching |
| 0.5 d | `BVA-I254` · `BVA-I255` · `BVA-I271` |
| 0.4 d | `BVA-I270` |

Median **8.2 d**, down from 8.9. **Do not read that as improvement.** Nothing left the queue; four items entered it. The eleven that were there yesterday are each exactly one day older, and on their own their median is 9.9 d. A queue metric that falls when work is added and nothing is reviewed is measuring arrivals, not throughput — which is why this section lists the ages rather than quoting the median alone.

**Twelve of the fifteen are Ayomikun's**, and he has nothing In progress — so the sprint is now rate-limited by review capacity rather than by anyone's writing speed.

### 1.5 `BVA-I269` — the first BLOCKED item, and it names its own blocker

`BVA-I269` *Enable Branch Protection on Main Branches* went In progress → BLOCKED at 02:41 UTC. The reason is recorded on its sibling `BVA-I270` at 03:06:

> this is done on all backend repos but I cannot add it organisation wide yet as I do not have admin access to the organisation

Branch protection, GitHub secret scanning, push protection and org-wide Dependabot alerts are all **org-level settings**. That places three of the five security items outside the assignee's reach:

| Item | Status | Needs |
|---|---|---|
| `BVA-I269` Branch protection | **BLOCKED** | org admin |
| `BVA-I270` Semgrep on every PR | REVIEW/QA | ✅ done in 3 repos — but *required-check* enforcement needs `BVA-I269` |
| `BVA-I271` Fix vulnerabilities already found | REVIEW/QA | ✅ done for backend; mobile's nine Dependabot PRs untouched |
| `BVA-I272` Dependabot | To do | org admin (or a `dependabot.yml` per repo — 3 of 5 lack one) |
| `BVA-I273` Secret scanning + push protection | To do | org admin |

This is a genuinely useful finding and it came from the board, not the code: yesterday's report said these items "could be substantially done" precisely because a clone cannot see GitHub settings. They are not done, and the blocker is a permission, which no amount of engineering time will clear.

### 1.6 `origin/BVA-I239` — a new mobile branch, and `BVA-I242` is now three days static

David pushed a new branch `origin/BVA-I239` (*translation implementation*) at 17 Sep 16:09 UTC — two hours after yesterday's window closed, hence its absence there. It carries the full `lib/l10n` layer with four locales and generated localisations.

**`origin/BVA-I242`, the older l10n branch, has not moved for 3.0 days**, and its two related items (`BVA-I229`, `BVA-I238`) are still In progress. There are now **two** unmerged branches carrying overlapping translation work and neither is on `main`, which is why capability #3 does not move (§ appendix). Third edition asking what happens to `BVA-I242`.

### 1.7 Still no estimates — thirteenth consecutive edition

0 of 35 items on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01 carry estimation points. Velocity is not derivable for any sprint, so "four days left" cannot be turned into "enough time for fifteen reviews or not".

---

## 2. What shipped this cycle

**23 commits on any ref; 22 merged to `main`.** After a window with zero, this is the largest single-day figure in this record.

| Repo | In window | Merged to `main` | Last commit on `origin/main` | Days stale |
|---|---:|---:|---|---:|
| `beevia-api` | 10 | 10 | `60ed6cd` 18 Sep 11:29 UTC | 0.1 |
| `beevia-db-schema` | 7 | 7 | `b9bfa7a` 18 Sep 04:43 UTC | 0.4 |
| `beevia-admin-api` | 5 | 5 | `36b840a` 18 Sep 10:27 UTC | 0.2 |
| `beevia-mobile` | 1 (branch) | 0 | `874697a` 15 Sep 16:07 UTC | **2.9** |
| `beevia-admin` | 0 | 0 | `f12135b` 14 Sep 11:36 UTC | **4.1** |

Four things landed, in descending order of consequence.

**1. Trust & Safety, end to end on the server.** `beevia-db-schema` gained moderation state and a disclosed-message evidence table (`72d71d3`, `9f60b32`, releases v0.0.32 and v0.0.33); `beevia-api` widened reporting (`dc53f63`); `beevia-admin-api` gained report detail and review decisions (`09cdcc8`). Three repos, one coherent feature, with a schema release in between — and it resolves a design deadlock this project has carried for six weeks (§3, `admin-api-rfc.md` §5.1b).

**2. NestJS 12 across all three backend repos** (`531a367`, `8e8d9ea`, `ccead88`), with validation moved onto Nest 12's Standard Schema support (`6ee6ac8`). This is the change that broke production, and it also surfaced two real behaviour differences: Nest 12 runs global guards for gateway handlers, so `JwtAuthGuard` threw a `TypeError` on every WebSocket message until it was taught to stand aside for non-HTTP contexts (`bfd8b7e`), and the response envelope had to be kept off websocket ACKs (`22b1690`).

**The guard change is not a security regression, and that was checked rather than assumed.** A socket authenticates once on its handshake: `handleConnection` runs `WsPrincipalService` and calls `socket.disconnect(true)` on failure — verified at `messaging.gateway.ts:156`. Per-message re-authentication was not happening on Nest 11 either, because the guard never ran in that context. Standing aside restores prior behaviour; it does not relax anything.

**3. Semgrep CI in the three backend repos** (`BVA-I270`), running `semgrep ci` on `pull_request`, on `push` to `main`, and on a daily cron. It works, and it is **advisory**: a workflow cannot prevent a merge unless it is a required status check, which is the branch-protection setting that is blocked (§1.5).

**4. The boot-crash fix** (`75ab35b`), covered in the overview and in `suggestions.md` §5.8.

**`beevia-admin` shipped nothing for the fourth day.** Its board item `BVA-I9` has been In progress since 14 Sep with no commit behind it, and the repo still has no `.github` directory.

---

## 3. Spec updates made this cycle

**Three findings, all reconciled.** The audit against the `origin/main` shadow reported:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 49  spec= 47  proposed= 19  [DRIFT]
    + in code, undocumented : GET    /admin/chats/reports/{}
    + in code, undocumented : PATCH  /admin/chats/reports/{}
    * PROPOSAL SHIPPED      : GET    /admin/chats/reports/{}
```

After the edits, both services are clean: `137/137` and `49/49`, proposed `38` and `18`.

| # | Finding | Action taken |
|---|---|---|
| 1 | `GET /admin/chats/reports/{reportId}` — a standing proposal, now shipped | **Moved** proposed → implemented, written **as built** rather than as proposed. Deleted from `openapi.admin.proposed.yaml`; the orphaned proposed `ChatReportDetail` component removed with it |
| 2 | `PATCH /admin/chats/reports/{reportId}` — in code, never proposed | **Added** to `openapi.admin.yaml` with `ReviewChatReportRequest`, `ChatReportReview`, `ChatReportedMessage`, `ChatReportDetail` |
| 3 | `POST /conversations/{id}/report` — contract widened, no route change | **Updated in place** in `openapi.yaml`: `messages` (≤20) and `blockContact` on `ReportConversationRequest`, new `ReportedMessage` schema, `400` for `block_requires_direct` |

**Finding 3 is the one the route-level audit could not see**, and it is the fourth instance of that class recorded in `suggestions.md` §5.4. The surface stayed at 137 operations while the request body of a live endpoint gained an array of message plaintext. It was found by reading the commit, not by the inventory diff.

**Two operations shipped as proposed and one did not, and the difference is worth stating.** The shipped `GET` matched the proposed *path* but not the proposed *shape*: it returns the whole participant list rather than a single `reported_user` (the only well-defined answer for a group), and it does **not** carry the proposed prior-report counters on either party. The shipped `PATCH` replaced the proposed `POST .../resolve` for the bookkeeping half only — it records `reviewed` / `actioned` / `dismissed`, but does not enforce anything, so suspension is still an unlinked separate call. `POST .../resolve` therefore **stays proposed**, annotated, for the enforcement half alone.

Two implementation details are better than the proposal asked for and are now documented as such: `pending` cannot be set back (so "someone already looked" is not erasable), and `review` is `null` rather than an object of nulls until someone has looked.

**Narrative documents updated:**

- `admin-api-rfc.md` — 47 → **49 operations**, 19 → **18 proposed**; §3.13 Chats 4 → 6 ops with the two new rows and six contract facts; Module 4 coverage `NOT BUILT` → **PARTIAL**; **new §5.1b** recording that Option B shipped on both sides and that C was never built; §6 "Blocked on a decision — Module 4" struck; §6.3's Module 4 gap row marked mostly closed, with the prior-report counters and the enforcement link as what remains.
- `api-rfc.md` — **new §5.9** on the widened report contract, the four load-bearing implementation choices, and the client gap; §6.8 inventory row updated; §6.9 records that REST and WS were widened together in one commit by sharing a Zod field object.
- `suggestions.md` — **new §5.8** on the green-pipeline-unbootable-release incident and the CI blind spot it exposed; §7.7 updated with Semgrep coverage, the advisory-vs-required distinction and the org-permission wall; §8 order re-prioritised (org admin escalated, mobile workflows and the openapi drift check promoted).

### 3.1 Standing code findings, re-verified at `origin/main`

All five re-checked against today's shadow, not carried forward:

| Finding | Location | State today |
|---|---|---|
| Report read-scoping gap | `beevia-admin-api/src/reports/reports.service.ts:133` | Unchanged — resolved once at generation, never re-applied at read. **Ninth edition** |
| `POST /translate` bound to a stub | `beevia-api/src/translate/translate.module.ts:23` | Unchanged — `TRANSLATE_PORT` → `StubTranslateAdapter` |
| FX not started | `beevia-api/src/payments/payment.service.ts:506` | Unchanged — `activeNgn()`, call sites 70, 128, 288 |
| Push falls back to a stub | `beevia-api/src/common/env.ts:111`, `.env.example:79` | Unchanged — `FCM_SERVICE_ACCOUNT` still `.optional()` and blank |
| `beevia-admin` has no CI | `beevia-admin/` | Unchanged — no `.github` directory exists |

### 3.2 The working-tree audit still reports 19 phantom drift lines

6 in `beevia-api`, 13 in `beevia-admin-api`, because the three backend repos remain `diverged` from the 8 September incident and their working trees are still 4 September code. **Eleventh consecutive edition flagging it**, so that nobody "fixes" the spec by deleting operations that exist at `origin/main`. The divergence widened today: each is `ahead 1`, now behind **32 / 23 / 20** (was 22 / 18 / 13). Every code claim in this report is made against the shadow.

---

## 4. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 16.** 12 items — **8 leaves, 4 parent Stories**. **Zero activity of any kind in the window**; the board's newest audit entry is 14 Sep 14:53 UTC, so it has now been **4.0 days silent**.

| Status | Leaves | 17 Sep | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 2 | 2 | 0 |
| Done | 6 | 6 | 0 |

| Owner | Leaves | In progress | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 | 3 |
| Ayomikun Araoye | 3 | 1 | 2 |
| Unassigned | 1 | 0 | 1 |

Both In-progress items — `BVA-I8` *Report Data Query* (Ayomikun) and `BVA-I9` *Report Content Display* (Promise) — were moved there on 14 September and have sat **4.0 days** with no `beevia-admin` commit behind them for **4.1 days**.

**Promise has zero self-attributed actions on any board, ever — and that is now measured rather than inferred.** Across all 67 audit entries on this board the actors are a board administrator (43) and Ayomikun (24); across the sprint-0901 and 08-01 sidecars the count is likewise zero. Seventh consecutive edition raising it, and it has not been answered in any framing. It compounds: the admin dashboard is the one workstream with no board self-activity, no CI, the longest commit gap, and no coverage from any of the five security items.

### 4.1 Never summed with the main board

8 leaves here and 26 on sprint 0901 are different projects and different backlogs. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards and report invented movement.

---

## 5. Team performance — detail

**Ayomikun Araoye** — backend and admin API. **All 22 merged commits in the window are his**, across three repos, comprising a three-repo feature, a major-version framework upgrade, a SAST rollout and an incident fix. His 7-day merged non-merge total across both git identities is **32** (19 `beevia-api`, 6 `beevia-admin-api`, 7 `beevia-db-schema`, all as `Phoenixdadhev`), plus three `semgrep.dev on behalf of` commits and three release-bot commits counted separately. His median cycle time improved to **1.5 d** (n=3) as `BVA-I270` and `BVA-I271` went In progress → REVIEW/QA in under two days each. Two things need naming alongside that: **he has nothing In progress and twelve items in review**, so his throughput is now gated entirely on someone else; and **he is the one blocked on org-admin access**, which he reported himself on the board rather than leaving it to be discovered.

**David Samuel** — mobile. Pushed `origin/BVA-I239` at 17 Sep 16:09 UTC with the full l10n layer, so yesterday's "no activity of any kind" does not carry forward. But **nothing merged to `main` for 2.9 days**, two branches now hold overlapping translation work, and `BVA-I254` — his Trust & Safety item — is in REVIEW/QA with no mobile code behind it, moved there by the backend lead. Median cycle 8.1 d (n=2). The question for him is not effort; it is which of two branches is the one that lands.

**Philip Chidera** — design. Four leaves, all Done, board empty for the second edition. The design half of Trust & Safety was complete before the build half started today, which is the right order and worth noting given the previous edition asked whether he had queued work. He still may not.

**Promise Udo** — admin dashboard. One commit in 7 days, none in 4.1 days, zero self-attributed board actions across every board and every edition. **This is reported as absence of data, not as absence of work**: the admin dashboard is a real workstream with a real repo, and nothing in this workspace can see whether work is happening off-repo. What can be said is that neither the board nor git has observed any for four days.

### 5.1 What these figures do not measure

- **No estimation points on any of the three boards**, so a raw item count says nothing about who is carrying more. Twelve items in review may be less work than two.
- **Cycle time is barely computable here.** Most items skip `In progress` entirely; only five leaves in the sprint have both transitions recorded, so n=3 and n=2 are the whole sample. Neither median should be compared between people.
- **Commit counts reward small commits.** Today's 22 include a framework bump, a generated CI file and three release-bot tags alongside a genuine three-repo feature.
- **Neither correctness nor quality is measured.** No build, lint, test or `flutter` command was run from any sub-repo, by design. "Shipped" here means merged and reachable, nothing more.
- **Absence of data is not absence of work**, specifically for `beevia-admin`.
- **Whether any CI run passed is unknowable from a clone**, including today's new Semgrep workflows.

---

## 6. Previous recommendations — where they stand

| Recommendation from 17 Sep | Status on 18 Sep |
|---|---|
| **1. Fix the scope line on the five security items before work starts** | ❌ **Not done — and it cost exactly what was predicted.** Semgrep landed in the three backend repos; `beevia-admin` and `beevia-mobile` got nothing. One word, 24 hours ago (§1.5, §2) |
| **2. Get a decision on the review queue** | ❌ **Not done, and worse.** 11 → **15** items, nothing has ever left, four days remain. Fifth edition (§1.4) |
| **3. Land `BVA-I270` as a file this week** | ✅ **Done, in one day.** `semgrep.yml` in all three backend repos, running on every PR. **The first code-shaped recommendation in this document to become a merged file.** Caveat: advisory until branch protection makes it required |
| **4. Merge or close `beevia-mobile`'s nine Dependabot PRs** | ❌ Not done. Still nine, oldest now **38 days** |
| **5. Decide the fate of the l10n half of `BVA-I242`** | ❌ **Not done, and now more tangled.** `BVA-I242` static 3.0 d; a *second* branch `BVA-I239` now carries l10n too (§1.6) |
| **6. Price the two remaining Trust & Safety items or move them out of 0901** | ✅ **Overtaken by events, and in the better direction.** Not priced — but built: both moved to REVIEW/QA and the backend half is real (§1.3). The mobile half is not |
| **7. Fix the report read-scoping gap** | ❌ Not done. `reports.service.ts:133` re-verified unchanged. Ninth edition |
| **8. Decide what happens to `POST /translate`** | ❌ Not done. `translate.module.ts:23` still binds `StubTranslateAdapter` |
| **9. Put estimation points on the boards** | ❌ Not done. Thirteenth edition |
| **10. Move `ZOHO_SPRINT_FILTER` to `0901` and the cut-off to ~20:00 UTC** | ❌ **Not done, and it cost a third day.** Still `08-01`. David's branch push at 17 Sep 16:09 UTC fell two hours past yesterday's close, which is why yesterday reported him at zero activity. Twelfth edition working around this |
| **11. Ask whether Philip has queued work** | ❌ Not asked, as far as this report can see. His board is empty for a second edition |

**Three of eleven resolved or overtaken — the best ratio this section has recorded**, and two of the three (Semgrep, Trust & Safety) are the two hardest items on the list. The pattern in what did *not* move is now sharp enough to name: **every unresolved item is a decision, a permission or a review — none of them is a coding task.**

---

## 7. What I would do this week

**Four days left in sprint 0901.**

1. **Grant or exercise GitHub org-admin access today.** Three security items cannot be completed by their assignee, one is formally `BLOCKED`, and it also decides whether today's Semgrep work can ever block a bad merge. This is the highest-leverage twenty minutes available to this project, and it is not available to the person assigned the work (§1.5).
2. **Decide the review queue, in any direction.** Fifteen items, four days, nothing has ever left. Sweep, review individually, or roll to the next sprint — all three are answers. Fifth consecutive edition; the queue grew 36% today while the question went unanswered (§1.4).
3. **Ship the mobile half of the report sheet, or move `BVA-I254` back out of review.** The server accepts disclosed messages, the admin queue is built to show them, and the client sends a bare `reason`. Right now the feature's most valuable field will be empty for every report, and the board says it is done (§1.3).
4. **Pick one of the two l10n branches.** `BVA-I242` (static 3.0 d) and `BVA-I239` (0.9 d) both carry translation work and neither is on `main`. Two branches is worse than one stale branch, and capability #3 cannot move until something merges (§1.6).
5. **Copy `secrets-scan.yml`, `supply-chain-guard.yml` and `semgrep.yml` into `beevia-mobile`, and give `beevia-admin` any CI workflow at all.** This is the security work that needs **no** permission from anybody, in the two repos the security items exclude. Then merge or close mobile's nine Dependabot branches — automated, queued, and the oldest is 38 days.
6. **Extend `openapi-schema.spec.ts` to diff the generated document against the committed `openapi.yaml`.** Today's incident paid for the expensive half: the document is already built in a test. A few more lines closes the contract-drift class that `suggestions.md` §5.4 has argued for since 3 September — and that this cycle demonstrated again, since finding 3 in §3 was invisible to the route-level audit.
7. **Write down that Module 4 is A-then-B.** The E2EE decision asked for on 5 August has now been made twice in code and recorded in no document but this pipeline's own. `Beevia Admin Dashboard.md` still says "reported messages" without saying whose (`admin-api-rfc.md` §5.1b).
8. **Fix the report read-scoping gap** (`reports.service.ts:133`). Ninth edition; a live access-control gap behind a client that consumes it.
9. **Decide what happens to `POST /translate`.** One sentence. The client is building on-device translation; the server binds a stub.
10. **Put estimation points on the boards, or state that the project does not estimate.** Thirteenth edition. With four days left and fifteen items in review, there is no way to say whether that is feasible.
11. **Move `ZOHO_SPRINT_FILTER` to `0901` and the daily cut-off to ~20:00 UTC.** Three consecutive editions have now mis-stated something because of the 14:00 boundary. Twelfth edition of this workaround.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync (**0 repos advanced — `beevia-admin` and `beevia-mobile` already current; 3 refused as `diverged`**) → deterministic audit against the working tree → a second audit against a read-only `origin/main` shadow built with `git archive` → read-only scratch export of sprint 0901 (35 items) + sidecar → `git log --all --since` sweep of every ref across all five repositories after a pruning fetch → content reads of the two new controllers, their DTOs and services → spec and RFC edits → a third audit confirming both services clean → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter`, `eslint` or build step ran. No repository was reset, rebased, reverted or cleaned; no sub-repo file was edited; the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed, or deployed.

**Files changed this cycle:** `openapi.yaml`, `openapi.admin.yaml`, `openapi.admin.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, this report and the web edition (`web-report/2026-09-18.html`, `web-report/index.html`). `openapi.proposed.yaml` needed no change.

**Degraded inputs.**

- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are still `diverged` from the 8 September incident (each `ahead 1`, now behind 32/23/20 — the gap widened by today's 22 commits); `sync_repos.py` correctly refuses to force a merge. Their working trees remain 4 September code, the sole cause of the working-tree audit's 19 phantom drift lines. Every code claim here is made against `origin/main` via a `git archive` shadow.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, a sprint that closed 28 August. The in-repo main export therefore reads a closed, frozen sprint — confirmed zero activity, all 41 leaves Done. All sprint-0901 figures come from a read-only scratch export to `/tmp/beevia-scratch/`, diffed item-by-item against the 17 September scratch export rather than read off the previous report. Twelfth consecutive edition working around this.
- **The window cut-off mis-stated a third day.** David's `BVA-I239` push landed 17 Sep 16:09 UTC, two hours after yesterday's 14:01 close, so yesterday's "zero commits on any ref" was true for its window and misleading about the day. A ~20:00 UTC cut-off would have caught it, the `BVA-I242` merge and the five security items.
- **The production rollback is reported from a commit message, not observed.** `75ab35b` states that the NestJS 12 deploy never bound `:3000`, failed its health check and was rolled back. This workspace has no access to deploy logs, hosting dashboards or CI run history, so the *fact* of the rollback is second-hand. The *cause* is verifiable and was verified: `z.coerce.date()` on the new `sentAt` field, and `createDocument` at boot.
- **Whether any CI workflow has run or passed is unknowable here**, including the three Semgrep workflows added today. Their presence and triggers were read from `origin/main`; their outcomes live on GitHub.
- **Settings-shaped work remains partly invisible**, but less so than yesterday: branch protection, secret scanning, push protection and Dependabot *alerts* still leave no trace in a clone, yet the board comment on `BVA-I270` now tells us directly that they are not configured and why. `BVA-I272` and `BVA-I273` are reported from the board, and neither is scored.
- **`Comments` bodies are unavailable** from the Zoho API — `commentCount` only. The `BVA-I270` comment quoted in §1.5 came from the **activity sidecar**, which does carry comment text, not from the CSV.
- **Cycle time is not reliably computable on this board** — see §5.1. Only five leaves have both transitions recorded.
- **Repository integrity was not hash-swept this cycle.** Credential rotation and workstation remediation remain unverifiable from this workspace.
- **No estimation points exist on any of the three boards**, confirmed at the raw CSV value level.
- **The activity sidecars only carry history for items currently on their board.**
- **The window ends at 14:03 UTC**, so anything after that today is unobserved.

**The `Epic` column works** — the correction made in the 17 September edition holds. Today's sprint-0901 export resolves 22 of 26 leaves (`Language` 10, `Notification` 7, `security` 5); the four blanks are genuinely unassigned. The export script's "no source key" warning fired again on both in-repo exports and is a **sampling artefact** — it inspects only the first 50 rows, which on the frozen 08-01 board are blank. Do not reinstate the retired OAuth-scope claim on the strength of that warning.

**Window.** 17 Sep 14:01 UTC → 18 Sep 14:03 UTC — a normal ~24-hour cadence. All `actiontime` and board figures are UTC; the local export host runs UTC−6, so raw `git log` output needs `TZ=UTC` to be read correctly.

**Sources.** Boards: `beevia-sprint-board-2026-09-18.csv` (64 rows, 41 leaves, sprint 08-01, unchanged, zero activity) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-18.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (35 rows, 26 leaves) + activity sidecar. Code: all five repositories at `origin/main` — `beevia-admin`, `beevia-mobile` from the synced working tree; the other three from a `/tmp` `git archive` shadow at `60ed6cd` / `36b840a` / `b9bfa7a`. Specs after this cycle's edits: `openapi.yaml` (137), `openapi.proposed.yaml` (38), `openapi.admin.yaml` (49), `openapi.admin.proposed.yaml` (18) — all validated, zero route-level drift against `origin/main`, no `x-beevia-*` markers, no broken `$ref`s, no orphaned components.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is performed by a non-contributor whose transitions are reported without naming the actor.

<a id="mvp-method"></a>

### MVP readiness — ≈62% (estimate; 61.52, +0.12)

**Target 2026-09-01 (provisional) · the target date passed seventeen days ago.** Weights frozen — **no methodology change this edition.**

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | 0 | The socket layer *was* touched, but only to repair what the Nest 12 upgrade broke — the JWT guard standing aside for gateway handlers, the envelope kept off WS ACKs. Restoring prior behaviour is not new capability. No change to crypto or keys |
| 2 | Voice & video calling | 8 | 0.8 | 0 | `FCM_SERVICE_ACCOUNT` still `.optional()` (`env.ts:111`) and blank in `.env.example:79` — push transport still falls back to a stub |
| 3 | Message translation | 7 | 0.30 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter`. `lib/l10n/` and `lib/core/language/` still do not exist on `main` — and there are now **two** unmerged branches carrying them (`BVA-I242` static 3.0 d, `BVA-I239` 0.9 d). Unmerged does not score |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | 0 | Unchanged; nothing touched `/kyc` or `/upgrade` |
| 5 | International KYC tier | 6 | 0.0 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.75 | 0 | `PaymentService.activeNgn()` re-verified at `payment.service.ts:506`, call sites 70/128/288 — every wallet is still NGN |
| 7 | Send / request / receive in chat | 12 | 0.90 | 0 | Unchanged. Still held back from 1.0 by the missing payments read path and the unused `POST /payments/send` and `/payments/{id}/pay` |
| 8 | Cross-currency FX | 12 | 0.0 | 0 | Proposed only. `activeNgn()` still hard-codes the currency |
| 9 | Virtual cards | 10 | 0.70 | 0 | Unchanged. The client still uses 2 of the 13 card operations the server exposes |
| 10 | Consent management | 4 | 0.0 | 0 | No endpoint or record anywhere. The new report flow is *adjacent* — it freezes what a reporter consented to disclose — but it is per-report evidence, not a consent record, and it is not scored here |
| 11 | Admin oversight | 6 | **0.92** | **+0.02** | **Named evidence:** two operations shipped (`GET` and `PATCH /admin/chats/reports/{reportId}`), a proposal retired (19 → 18), a schema migration merged (moderation state + evidence table, v0.0.32/33), and spec **Module 4 moved `NOT BUILT` → `PARTIAL`** — a workable queue with status, filter, detail and review decision. Held back: no enforcement link, no prior-report counters, and **no `beevia-admin` commit for 4.1 days**, so none of it is reachable in a dashboard yet |
| | **Weighted total** | **100** | **61.52** | **+0.12** | **≈62%** |

**The integer headline moved from 61% to 62% by rounding, not by a point of progress.** The change is +0.12 on a 100-point scale — 61.52 rounds up where 61.40 rounded down, so the decimal is the figure to compare between editions.

Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches. Two illustrations from today, pulling opposite ways. The day's largest visible event — twenty-two commits including a framework upgrade and a SAST rollout — moves the estimate **not at all**, because none of it is product capability. And the day's most significant *capability* work, the Trust & Safety feature, moves it by 0.12 rather than more, because the server half shipped while the client half did not exist and the dashboard that would surface it has had no commit in four days. A feature that is real on one side of the wire is not a capability yet.

### What this report cannot tell you

- **Whether the production rollback is fully resolved.** The fix merged at 11:29 UTC; whether a subsequent deploy succeeded and bound a port is not visible from a clone. Worth confirming before anyone relies on `main` being deployable.
- **Whether the Semgrep workflows have run, passed, or found anything.** Three files exist and their triggers are correct; run history and findings live on GitHub, as does whether `SEMGREP_APP_TOKEN` is set.
- **Whether `BVA-I254` is genuinely complete somewhere this workspace cannot see.** The claim is that the mobile report sheet is in review; the searched evidence says `chat_service.dart` posts a bare `reason` on `main` and both open branches. An unpushed local branch would be invisible here.
- **Which of the two l10n branches is intended to land**, or whether they conflict. Both carry `lib/l10n`; neither is merged.
- **Whether the fifteen items in REVIEW/QA will be reviewed, swept, or rolled.** Five editions of asking; the queue has never lost an item to review.
- **Why `beevia-admin` has gone 4.1 days without a commit**, or whether work is happening there off-repo.
- **Whether granting org-admin access is blocked by policy, availability or nobody having asked.** The board records that it is missing, not why.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 35, 0 of 12 items estimated.
