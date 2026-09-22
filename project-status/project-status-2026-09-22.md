# Beevia — Project Status

**As of 2026-09-22** · Sprint **0901** (3 Sep → 22 Sep) — **day 20 of 20, closes today** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 20 of 20** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-22.csv` + `beevia-activity-2026-09-22.json` (64 items, sprint 08-01 — frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-22.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**46 items**) + sidecar in `/tmp/beevia-scratch/`; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`).

Scope: three boards, kept separate and never summed. **Window 18 Sep 14:03 UTC → 22 Sep 15:20 UTC — about 4.1 days (Fri → Tue).** There were no editions on 19 or 21 September, so every "Δ" below covers four days, not one.

---

## Quick overview

> **Sprint 0901 closes today with 6 of 37 leaves Done and 20 in review — and the review queue has still never lost an item.** Over four days the queue grew 15 → **20**. Every one of the five arrivals was moved there by a board administrator, not by its assignee, and **two of them — David's translation items — have no code on `main` behind them**: both l10n branches are still unmerged and `beevia-mobile` has had no commit for **7.0 days**. At the same time **11 new mobile QA bugs were moved into this sprint yesterday afternoon**, all To do, one day before it ends. The good news is real and in the one place this report has worried about longest: **`beevia-admin` shipped Promise's Module 4 dashboard** — conversations, the report queue, report detail with disclosed messages, and a review form, all six screens calling the live API. The admin side of Trust & Safety is now end to end; only the phone is missing.

**Correction to the 18 Sep edition: the org-admin blocker is probably not a blocker any more — and this report cannot confirm it either way.** On 18 Sep at 16:21 UTC, two hours after that edition's window closed, a board administrator moved `BVA-I269` BLOCKED → REVIEW/QA and `BVA-I272`/`BVA-I273` To do → REVIEW/QA. Ninety minutes later, `beevia-api` `6121413` says in its message that "the branch ruleset names the required checks" and must be updated as it merges — which only makes sense if a ruleset with required checks exists. So the 18 Sep headline recommendation ("grant or exercise org-admin today") appears to have happened the same day. **But none of it is observable from here:** the GitHub token in this workspace gets `404` on every repo's rules endpoint. Treat the three security items as *plausibly done, unverified*, not as done.

**Also changed since then:** the 18 Sep edition listed `beevia-mobile` as missing `secrets-scan`, `supply-chain-guard` and `semgrep` "workflows". That remains true, but the backend has since collapsed all three into one four-line caller of an org-level workflow (`code-scan.yml`, `6121413` / `76ce0e5`). Copying security CI into mobile and admin is now one file, not three — the cheapest it will ever be.

| Measure | 18 Sep | 22 Sep | Δ (4 days) |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 22 | **19** | — (4-day window) |
| Commits on *any* ref, all five repos, in window | 23 | **19** | — |
| Board transitions, all three boards, in window | 7 | **20** (7 status, 2 type, 11 sprint moves) | — |
| Items added to sprint 0901 | 0 | **11** — all mobile QA bugs, all To do | **+11** |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 3 — reconciled | **0** | — |
| Contract drift found beyond route level | 1 | **1 — `GET /admin/users`, wrong since 4 Aug, fixed (§3)** | — |
| Sprint 0901 leaves, total | 26 | **37** | **+11** |
| Sprint 0901 leaves To do | 2 | **11** | +9 (−2 moved, +11 new) |
| Sprint 0901 leaves In progress | 2 | **0** | −2 |
| Sprint 0901 leaves BLOCKED | 1 | **0** | −1 |
| Sprint 0901 leaves REVIEW/QA | 15 | **20** | **+5 — five in, none out** |
| Sprint 0901 leaves Done | 6 | 6 | **0 — fourth edition flat** |
| Review-queue median age (0901) | 8.2 d | **8.0 d** | −0.2 — dilution again (§1.3) |
| Oldest item in the queue | 9.9 d | **14.0 d** | +4.1 |
| `beevia-mobile` `main` days since a commit | 2.9 | **7.0** | +4.1 |
| `beevia-admin` `main` days since a commit | 4.1 | **1.0** | **−3.1** |
| `beevia-admin-api` days since a commit | 0.2 | 1.0 | |
| `beevia-api` / `beevia-db-schema` days since a commit | 0.1 / 0.4 | **3.9 / 3.9** | |
| Admin board: days since *any* activity | 4.0 | **8.0** | +4.0 |
| Ayomikun commits (7d, both identities, merged, non-merge) | 32 | **29** | rolling window |
| David commits (7d, merged to `main`) | 1 | 1 (15 Sep, on the edge) | 0 |
| Promise commits (7d, merged) | 1 | **1 — 21 Sep, 2,450 lines** | new commit |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 35 · 0 / 12 · 0 / 64 | **0 / 46 · 0 / 12 · 0 / 64** | 0 |
| MVP readiness (estimate) | ≈62% (61.52) | **≈62% (61.70)** | **+0.18** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **15 on 0901 — all 15 REVIEW/QA** · 3 on 0901-admin | 6 — **3 moved by a board administrator** | 1.75 d (n=4 — §5.1) | **0** on 0901 · 1 on 0901-admin (`BVA-I8`, 8.0 d) | **29** | Everything Ayomikun owns on the sprint is waiting on review. Output since Friday was hardening, not features: Postman docs, CI consolidation, a silent-zero counts bug |
| David Samuel | mobile | **18 on 0901** — 11 To do (new), 5 REVIEW/QA, 2 Done | 3 — **none self-moved** (2 by a board administrator, 1 by Ayomikun) | 6.6 d (n=4) | 0 In progress · **11 To do arrived yesterday** | 1 | **No commit on any ref for 4.97 days; none on `main` for 7.0.** Two of David's items entered review yesterday without a merge behind them. Eleven QA bugs were assigned to David the day before sprint close |
| Philip Chidera | design | 4 on 0901 — all Done | 1 | — | 0 | — | Third edition with an empty board. The 11 QA bugs include four "doesn't match approved Figma" items — design sign-off may be needed |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, 8.0 d) | **1 (21 Sep)** | **Shipped Module 4 end to end, wired to the live API** (§2). Still zero self-attributed board actions on any board, and the admin board has not moved in 8 days, so the board still cannot see this work |

**The two questions for standup:** (1) **Sprint 0901 ends today with 20 items in review and no review ever done — what happens to them tonight?** Roll, sweep or review; this is the sixth edition asking, and the sprint boundary is the natural moment to decide. If they roll, say so in the next sprint's name rather than letting the queue silently cross over. (2) **David — which l10n branch lands, and what is the plan for the 11 QA bugs?** Two of David's items were moved to review yesterday against code that is not on `main`, and eleven bugs arrived on the last day of the sprint. The question is sequencing, not effort.

**The three things worth knowing:**

1. **Module 4 is built on both admin sides; the missing piece is one mobile commit.** `c1b0aeb` added 28 files to `beevia-admin` — conversations list and detail, per-user chat activity, the report queue, report detail with a `reported-messages` panel, and a review form — and every one of the six chat calls goes through `liveClient`, not fixtures. The same day `b4c545e` fixed the admin API reporting **every** conversation as 0 participants, 0 messages, 0 reports (a correlated subquery bound to its own `id`; Postgres raised nothing), so the dashboard landed onto correct data. What a moderator will still see is an empty evidence list for every report, because `chat_service.dart:258` on `beevia-mobile` `origin/main` still posts `{"reason": reason}`. `BVA-I254`, the item for that, has been in REVIEW/QA for 4.5 days with no mobile code behind it.

2. **The board is now moving items into review that the code has not reached.** Yesterday at 16:07 UTC a board administrator moved four translation items (`BVA-I229`, `BVA-I238` and their parents `BVA-I228`, `BVA-I237`) In progress → REVIEW/QA. `lib/l10n` and `lib/core/language` still do not exist on `main`; the work is on `origin/BVA-I239` (static 4.97 d) and `origin/BVA-I242` (static 7.0 d), each roughly 18,000 lines ahead of `main`. Items in review without a merged change are not reviewable in any useful sense — and together with `BVA-I254` that is **three of David's five review items with nothing on `main`**. This is a board-hygiene finding, not a personal one: none of the three moves was his.

3. **Sprint 0901's scope grew 42% on its penultimate day.** Eleven mobile QA bugs (`BVA-I257`–`BVA-I267`) — created 15 Sep, moved from Backlog into 0901 on 21 Sep at 16:17 UTC, all assigned to David, all To do. Several are substantive (face verification shows a static placeholder instead of a live camera; biometric auth not functional; correct PIN triggers the error modal) and four are "doesn't match the approved Figma". Nothing on this board is estimated, so it is impossible to say whether they were meant to be finished today or are simply being queued for the next sprint via this one. Either way they belong to the next sprint's plan, and they are the first QA output this project has recorded on any board.

**If you read nothing else:** the admin dashboard — the workstream this report called invisible for nineteen editions — shipped its biggest commit yet, wired to real data. What is between Trust & Safety and a working feature is one change on the phone. And sprint 0901 ends tonight with its review queue at an all-time high of 20 and its Done count unchanged for a week.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

**46 items — 37 leaves, 9 parent Stories.** Eleven leaves added since 18 Sep; none removed. **Day 20 of 20 — the sprint ends today.**

| Status | Leaves | 18 Sep | Δ |
|---|---:|---:|---:|
| To do | **11** | 2 | +9 |
| In progress | **0** | 2 | −2 |
| BLOCKED | **0** | 1 | −1 |
| REVIEW/QA | **20** | 15 | **+5** |
| Done | 6 | 6 | **0** |

| Epic | Leaves |
|---|---:|
| `Language` | 10 |
| `Notification` | 7 |
| `security` | 5 |
| (none) | 15 — the 11 new QA bugs plus 4 earlier items; genuinely unassigned |

**Nobody on the sprint has anything In progress.** Every leaf is either waiting to start (the 11 new bugs), waiting on review (20), or Done (6). Done has not moved since before the 15 September edition; six of 37 leaves (16%) are Done on the sprint's last day. No completion (`Item Completed`) was recorded in the window on any board.

### 1.2 Who moved what

All twenty activity entries in the window were made by a **board administrator** — none by an assignee. This reverses the 18 Sep edition, where every transition was self-attributed.

| Time (UTC) | Item | Transition | Assignee |
|---|---|---|---|
| 18 Sep 16:21 | `BVA-I269` Branch protection | **BLOCKED → REVIEW/QA** | Ayomikun |
| 18 Sep 16:21 | `BVA-I272` Dependabot | To do → REVIEW/QA | Ayomikun |
| 18 Sep 16:21 | `BVA-I273` Secret scanning + push protection | To do → REVIEW/QA | Ayomikun |
| 21 Sep 16:07 | `BVA-I228`, `BVA-I237` *(parents)* · `BVA-I229`, `BVA-I238` | In progress → REVIEW/QA | David |
| 21 Sep 16:15–16 | `BVA-I261`, `BVA-I263` | type Bug → Task | David |
| 21 Sep 16:17 | `BVA-I257`–`BVA-I267` (11) | Backlog → **0901** | David |

**Leaves moved into review: five** (`I269`, `I272`, `I273`, `I229`, `I238`); the two parents move with their children and are not counted.

### 1.3 The review queue — 20 items, nothing has ever left by review

| Age | Items |
|---|---|
| **14.0 d** | `BVA-I246`–`BVA-I252` — the seven-item Notification block, unchanged since 8 Sep 16:02 |
| 12.2 d | `BVA-I231` Preference Storage & Precedence Logic |
| 8.0 d | `BVA-I233` Build Both Screens · `BVA-I243` String Extraction & Bundle Switching · `BVA-I245` Backend String Bundles |
| 4.4–4.5 d | `BVA-I254` · `BVA-I255` · `BVA-I270` · `BVA-I271` |
| 4.0 d | `BVA-I269` · `BVA-I272` · `BVA-I273` |
| 1.0 d | `BVA-I229` · `BVA-I238` |

Median **8.0 d** (n=20), down from 8.2 — **for the same reason as last time: arrivals, not reviews.** The fifteen items that were in the queue on 18 Sep are each 4.1 days older, and on their own their median is now 12.2 d. **Fifteen of the twenty are Ayomikun's**, and Ayomikun has nothing else on the sprint. The pipeline is rate-limited by review, and has been for two weeks; that is a process finding.

### 1.4 Three review items with nothing on `main`

| Item | Assignee | Moved by | Code at `beevia-mobile` `origin/main` |
|---|---|---|---|
| `BVA-I254` Update Report Sheet, Add Message Count | David | Ayomikun, 18 Sep | ❌ `chat_service.dart:258` posts `{"reason": reason}` only |
| `BVA-I229` Translation Engine Integration | David | board administrator, 21 Sep | ❌ no `lib/l10n`, no `lib/core/language` on `main` |
| `BVA-I238` Auto-Translation Display | David | board administrator, 21 Sep | ❌ same |

The translation work does exist — on `origin/BVA-I239` (`a398106` *translation implementation*, 17 Sep 16:09 UTC) and on `origin/BVA-I242` (15 Sep). Both are about 115 files and ~18,000 inserted lines ahead of `main`; neither has merged, and nothing says which one will. **Review should be of a merge request, and there isn't one on `main` to review.**

### 1.5 The security items — board says review, code says partial, settings are invisible

| Item | Board | What the code shows at `origin/main` |
|---|---|---|
| `BVA-I269` Branch protection | REVIEW/QA (was BLOCKED) | `6121413`'s message refers to a branch ruleset with required checks on `beevia-api`. **Unverifiable here** — rules endpoint returns 404 for this token |
| `BVA-I270` Semgrep on every PR | REVIEW/QA | ✅ backend. `beevia-api` and `beevia-admin-api` now call the org workflow (`code-scan.yml`: quality + typecheck, Semgrep, secrets, supply-chain). **`beevia-db-schema` was not migrated** — it still carries its three separate files. Mobile and admin: none |
| `BVA-I271` Fix known vulnerabilities | REVIEW/QA | Backend `package update` commits on 18 Sep. **Mobile: nine Dependabot branches still open, oldest 42 days** |
| `BVA-I272` Dependabot | REVIEW/QA (was To do) | `dependabot.yml` present in `beevia-api` and `beevia-mobile` only; absent from `beevia-admin-api`, `beevia-db-schema`, `beevia-admin`. Org-level alerts: invisible here |
| `BVA-I273` Secret scanning + push protection | REVIEW/QA (was To do) | GitHub setting — invisible here |

The scope problem the 17 and 18 Sep editions raised is unchanged: **`beevia-admin` has no `.github` directory at all**, and `beevia-mobile`'s workflows do not include any of the security scans.

### 1.6 Eleven QA bugs, added on day 19

| Item | Title |
|---|---|
| `BVA-I257` | BVN Input Field Not Visible |
| `BVA-I258` | Font Sizes Smaller Than Design Across the App |
| `BVA-I259` | Grammar Error on Facial Verification Screen |
| `BVA-I260` | Face Verification Shows Static Placeholder Instead of Live Camera |
| `BVA-I261` | Virtual Card Shows Incorrect Logo and Provider *(retyped Bug → Task)* |
| `BVA-I262` | Recipient Name Missing From Transactions List |
| `BVA-I263` | Share Transaction Receipt Shares Plain Text Instead of Image *(retyped Bug → Task)* |
| `BVA-I264` | In-Chat Money Request Card Doesn't Match Approved Figma Design |
| `BVA-I265` | Send Money Screen and Receiver Details Don't Match Approved Design |
| `BVA-I266` | Correct PIN Incorrectly Triggers Error Modal |
| `BVA-I267` | Biometric Authentication Not Functional |

**This is the first QA pass visible on any board**, and it is useful evidence in its own right: it says the KYC, wallet and send-money flows are in a testable state on a device, and names where they fall short of the design. It does **not** move the MVP estimate either way — correctness is out of scope for the rubric by the owner's standing instruction — but `BVA-I260` and `BVA-I267` are worth a look before anyone calls local KYC "0.9 built": a static placeholder where facial verification should be is a wired-vs-stub question, not a polish one. Flagged for the next edition to verify in code rather than scored from a bug title.

### 1.7 Still no estimates — fourteenth consecutive edition

0 of 46 items on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01 carry estimation points. Velocity is not derivable for any sprint, so there is no way to say whether 11 new bugs on the last day was a plan or a parking decision.

---

## 2. What shipped this cycle

**19 commits on any ref, all merged to `main`** (including PR merge commits and one release-bot commit), across four days.

| Repo | In window | Last commit on `origin/main` | Days stale |
|---|---:|---|---:|
| `beevia-api` | 6 | `b752b9e` 18 Sep 18:07 UTC | 3.9 |
| `beevia-db-schema` | 3 | `1e1ccec` 18 Sep 18:12 UTC | 3.9 |
| `beevia-admin-api` | 9 | `99c26ea` 21 Sep 14:44 UTC | 1.0 |
| `beevia-admin` | **1** | `c1b0aeb` 21 Sep 15:47 UTC | **1.0** |
| `beevia-mobile` | **0** | `874697a` 15 Sep 16:07 UTC | **7.0** |

In descending order of consequence:

**1. The Module 4 dashboard** (`beevia-admin` `c1b0aeb`, Promise, 21 Sep — 28 files, +2,450 lines). New routes `/chats/[id]`, `/chats/reports`, `/chats/reports/[id]`; a `features/chats` module with the conversations table, conversation detail and participants, per-user chat activity and block list, the reports queue, report detail, a `reported-messages` panel and a review form. **Wired, not stubbed:** `features/chats/api.ts` calls `GET /admin/chats`, `GET /admin/chats/{id}`, `GET /admin/chats/users/{userId}`, `GET /admin/chats/reports`, `GET /admin/chats/reports/{id}` and `PATCH /admin/chats/reports/{id}` through `liveClient`, which bypasses the mock adapter. The review form sends `note: ""` explicitly because the API treats an omitted note as "clear" — a detail that shows the author read the contract. One small leftover: a `TODO(backend)` fallback unwraps a list envelope from the detail route, written against a Postman sample that has since been corrected (§3).

**2. The admin chat counts were always zero, and now aren't** (`b4c545e`, 21 Sep). The three count subqueries on `GET /admin/chats` referenced `${conversations.id}`, which Drizzle renders as a bare `"id"` in a single-table select — so each subquery correlated with its own row and returned 0. Against production the same conversation now reports 2 participants, 7 messages, 1 report. The fix adds an assertion on the rendered SQL, which is the only cheap way to catch a bug that fails silently. It landed the same morning the dashboard that displays those counts was committed.

**3. CI consolidated onto an org workflow** (`6121413` in `beevia-api`, `76ce0e5` in `beevia-admin-api`, 18 Sep). Three copied workflow files became one caller of `Drumbell-Technologies/.github`'s `code-scan.yml`, which also adds a **`tsc --noEmit` typecheck** — something no CI job ran before. `beevia-db-schema` was not migrated.

**4. Documentation, both good and bad.** Good: `5eaaecb` + `e128cc6` document every one of the admin API's 51 Postman requests field by field, and correct the collection's own pagination claim by probing the running service — which is how §3's spec error surfaced. Bad: `081441c chore: package update` in `beevia-api` **deleted the whole `docs/` directory** — five files, 1,719 lines, including `mobile-integration-handoff.md` and `encryption-model.md` — with no mention in the message and no replacement at `origin/main` (`suggestions.md` §5.9).

**5. Dependency and release hygiene.** Package updates in all three backend repos; a lint fix for the stricter `no-unused-expressions` rule (`8762c36`); `beevia-db-schema` release automation repaired and v0.0.34 recovered (`b360e05`, v0.0.35).

**`beevia-mobile` shipped nothing on any ref.** Its last branch push was `BVA-I239` on 17 Sep 16:09 UTC.

---

## 3. Spec updates made this cycle

**Route level: clean.** The audit against the `origin/main` shadow:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 49  spec= 49  proposed= 18  [OK]
```

No operation was added, removed or shipped from proposal. The four commits that touched `beevia-admin-api/src` changed no route and no request or response field.

**Contract level: one error found and fixed — and it had been wrong since 4 August.**

| # | Finding | Action taken |
|---|---|---|
| 1 | `GET /admin/users` documented as `data: AdminUserSummary[]` + `meta: PaginationMeta`. At `origin/main`, `users.service.ts:94` calls `buildResponse({ items, page, limit, total, totalPages }, 'Users')` with no `meta` — so the wire shape is `data.items`, `data.page`, `data.limit`, `data.total`, `data.total_pages`, and **no `meta`** | **Corrected in place** in `openapi.admin.yaml`, with a description noting it is the one list that differs from Roles / Admin Accounts / Reports. Re-audited clean afterwards |

**Found by the backend team, not by this pipeline** — `e128cc6` probed every list route on a running service and reported four pagination envelopes. The other three conventions were checked against the spec and are correctly documented (`meta` on roles, accounts, reports; `data.pagination` on transactions, wallets, chats, report queue; cursor on activity). The dashboard was never misled: `beevia-admin` reads `data.data.items`, having been written against the service. This is the fifth contract-level drift that the route-level audit could not see (`suggestions.md` §5.4, §5.9).

**Narrative documents updated:**

- `admin-api-rfc.md` — §6.3 pagination row: **four** conventions, not three, with the users shape named; §5.1b gains a 22 Sep update recording that the dashboard half of Option B landed and is wired to the live API, the counts fix, and that the mobile half still has not; §1 Module 4 row notes the dashboard.
- `suggestions.md` — **new §5.9**: the users-list drift, and the undocumented deletion of `beevia-api/docs/`.
- `api-rfc.md` — no change needed; the consumer surface and contracts did not move.

### 3.1 Standing code findings, re-verified at `origin/main`

| Finding | Location | State today |
|---|---|---|
| Report read-scoping gap | `beevia-admin-api/src/reports/reports.service.ts:133` | Unchanged — scoped at generation only. **Tenth edition** |
| `POST /translate` bound to a stub | `beevia-api/src/translate/translate.module.ts:23` | Unchanged — `StubTranslateAdapter` |
| FX not started | `beevia-api/src/payments/payment.service.ts:506` | Unchanged — `activeNgn()`, call sites 70, 128, 288 |
| Push falls back to a stub | `beevia-api/src/common/env.ts:111`, `.env.example:79` | Unchanged — `FCM_SERVICE_ACCOUNT` optional and blank |
| `beevia-admin` has no CI | `beevia-admin/` | Unchanged — no `.github` directory |
| Report flow's client half | `beevia-mobile/lib/.../chat_service.dart:258` | Unchanged — posts `{"reason": reason}` only |

### 3.2 The working-tree audit now reports 21 phantom drift lines

6 in `beevia-api`, **15** in `beevia-admin-api` (was 13 — the two report operations added on 17 Sep are now also missing from the stale working tree). The three backend repos remain `diverged`, each `ahead 1`, now behind **38 / 32 / 23**. **Twelfth consecutive edition flagging it**, so that nobody "fixes" the spec by deleting operations that exist at `origin/main`. Every code claim here is made against the shadow.

---

## 4. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep — closes today.** 12 items, **8 leaves, 4 parent Stories**. **Zero activity in the window**; the newest audit entry anywhere on this board is 14 Sep 14:53 UTC — **8.0 days silent**.

| Status | Leaves | 18 Sep | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 2 | 2 | 0 |
| Done | 6 | 6 | 0 |

| Owner | Leaves | In progress | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 (`BVA-I9` Report Content Display) | 3 |
| Ayomikun Araoye | 3 | 1 (`BVA-I8` Report Data Query) | 2 |
| Unassigned | 1 | 0 | 1 |

**The board and the repo now disagree in the good direction.** Promise's biggest commit to date — the Module 4 dashboard — has **no item on this board at all**; every item here is about Module 7 (Reports). So the board shows Promise idle for 8 days while `beevia-admin` shows a 2,450-line feature merged yesterday. The standing rule applies in reverse: absence of board data is not absence of work, and this edition has the commit to prove it. Promise still has **zero self-attributed actions on any board, ever**.

Never summed with the main board: 8 leaves here and 37 on sprint 0901 are different projects and different backlogs, and the export stays in `sprint-board-exports/admin/` so `beevia-audit`'s flat glob cannot diff the two.

---

## 5. Team performance — detail

**Ayomikun Araoye** — backend and admin API. 29 merged non-merge commits in 7 days (12 `beevia-api`, 9 `beevia-admin-api`, 7 `beevia-db-schema` as `Phoenixdadhev`, 1 `beevia-api` as `Ayomikun Araoye`), plus Semgrep- and release-bot commits counted separately. The four days since Friday were hardening rather than features — dependency updates, CI consolidation with a new typecheck, full Postman response docs, and the silent-zero counts fix — and the counts fix is the kind of bug that only gets found by someone reading their own output against production. **All fifteen of Ayomikun's sprint leaves are in REVIEW/QA**, three of them moved there by a board administrator rather than by the assignee. That throughput is gated entirely on review; that is a process finding.

**David Samuel** — mobile. **No commit on any ref for 4.97 days, none on `main` for 7.0.** Median cycle 6.6 d (n=4). Two of David's items entered review yesterday without a merge (moved by a board administrator), one has been in review since Friday without mobile code (moved by Ayomikun), and **eleven QA bugs were assigned to David yesterday**, making David the owner of 16 of the sprint's 31 unfinished leaves. None of this is evidence about effort — there may well be local work not yet pushed — but the two unmerged l10n branches are the thing to resolve first, because they hold three sprint items and capability #3 hostage.

**Philip Chidera** — design. Four leaves, all Done; board empty for the third edition. Four of the new QA bugs are "does not match the approved Figma", which may need Philip to confirm what "approved" means before David can close them.

**Promise Udo** — admin dashboard. **One commit in 7 days, and it is the most consequential front-end commit of the week**: Module 4 end to end, wired to the live API. Invisible to the admin board, which has no item for it and has not moved in 8 days.

### 5.1 What these figures do not measure

- **No estimation points on any of the three boards**, so item counts say nothing about workload. Eleven small UI bugs may be less work than one l10n merge.
- **Cycle time is barely computable.** Only eight leaves in the sprint have both an In progress and a REVIEW/QA transition; n=4 each. Do not compare the medians between people.
- **"Submitted to review" is no longer a measure of the assignee's action** — at least 6 of the 10 review transitions in the last 7 days were made by someone other than the assignee. The column counts arrivals, not submissions.
- **Commit counts reward small commits** and include documentation and dependency bumps.
- **Neither correctness nor quality is measured.** No build, lint, test or `flutter` command was run from any sub-repo.
- **Absence of data is not absence of work** — demonstrated this edition by `beevia-admin`.

---

## 6. Previous recommendations — where they stand

| Recommendation from 18 Sep | Status on 22 Sep |
|---|---|
| **1. Grant or exercise GitHub org-admin access** | 🟡 **Apparently done the same day — unverified.** `BVA-I269` left BLOCKED at 16:21 UTC; `6121413` refers to an existing branch ruleset with required checks. This workspace cannot read GitHub rules (404), so confirm in the org settings (§1.5) |
| **2. Decide the review queue, in any direction** | ❌ **Not done — sixth edition, and the sprint ends today.** 15 → **20**, nothing has ever left by review (§1.3) |
| **3. Ship the mobile half of the report sheet, or move `BVA-I254` out of review** | ❌ Not done. No mobile commit; `BVA-I254` still in REVIEW/QA (§1.4) |
| **4. Pick one of the two l10n branches** | ❌ **Not done, and the board moved ahead of it** — two translation items went to REVIEW/QA with neither branch merged (§1.4) |
| **5. Copy the security workflows into `beevia-mobile`; give `beevia-admin` any CI** | ❌ Not done. But cheaper now: the backend's scans are one four-line caller of an org workflow (§1.5) |
| **6. Extend `openapi-schema.spec.ts` to diff against the committed spec** | ❌ Not done — the file is untouched since `75ab35b`. **And this cycle produced another instance of what it would catch** (§3) |
| **7. Write down that Module 4 is A-then-B** | ❌ Not done. More pressing now the dashboard shows disclosed messages to moderators |
| **8. Fix the report read-scoping gap** | ❌ Not done. `reports.service.ts:133` unchanged. Tenth edition |
| **9. Decide what happens to `POST /translate`** | ❌ Not done. Still `StubTranslateAdapter` |
| **10. Put estimation points on the boards** | ❌ Not done. Fourteenth edition — and the 11-bug scope change shows why it matters |
| **11. Move `ZOHO_SPRINT_FILTER` to `0901` and the cut-off to ~20:00 UTC** | ❌ Not done. Still `08-01`. Cost again this edition: the 18 Sep report missed the security items' move by two hours. With 0901 ending today, the filter should move straight to the next sprint's name |

**One of eleven plausibly resolved, and it was the one this report called highest-leverage.** Every other open item is, again, a decision, a review or a merge — not code that nobody has written.

---

## 7. What I would do this week

**Sprint 0901 closes today; these are for the sprint boundary and the next sprint's first days.**

1. **Decide the fate of the 20 review items at the sprint boundary, explicitly.** Review, sweep, or roll — and if rolled, carry the age with them. Fourteen days for the Notification block is the longest wait this project has recorded. Sixth edition.
2. **Only move an item to REVIEW/QA when there is a merge to review.** Three of David's five review items have nothing on `main`. A review queue of items with no reviewable change is noise, and it makes the queue impossible to act on even when someone does sit down to review it.
3. **Merge one l10n branch, then ship the report-sheet client change.** Those two mobile merges unlock three sprint items, capability #3, and the whole moderator-facing value of Module 4. They are the highest-value engineering on the board.
4. **Plan the 11 QA bugs into the next sprint deliberately, and triage `BVA-I260` / `BVA-I267` first** — a static placeholder instead of a face-verification camera, and biometric auth not working, are capability questions rather than polish. Pull Philip in on the four "doesn't match approved Figma" items.
5. **Confirm branch protection, secret scanning and Dependabot in the GitHub UI** and add a comment to each of `BVA-I269`/`I272`/`I273` saying which repos are covered. This workspace cannot see it, and the board move alone does not say whether `beevia-admin` and `beevia-mobile` are included.
6. **Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`, and migrate `beevia-db-schema` to it.** One file each now. Then merge or close mobile's nine Dependabot branches (oldest 42 days).
7. **Restore or deliberately retire `beevia-api/docs/`** — especially `encryption-model.md` and `mobile-integration-handoff.md`, which the mobile half of the report flow needs (`suggestions.md` §5.9).
8. **Put the Module 4 dashboard on the admin board**, so Promise's work appears where the team looks. The board currently shows Promise idle for eight days in the week the dashboard shipped the most.
9. **Extend `openapi-schema.spec.ts` to diff against the committed `openapi.yaml`** — a few lines; would have caught this cycle's `GET /admin/users` error on 4 August.
10. **Fix the report read-scoping gap** (`reports.service.ts:133`). Tenth edition.
11. **Estimation points, `POST /translate`, and the Module 4 decision record** — carried, unchanged.
12. **Move `ZOHO_SPRINT_FILTER` to the next sprint's name** when it is created — 0901 ends today, so moving it to `0901` now would buy one day.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, exit 0) → admin board export with `--sprint 0901-admin` (12 items, exit 0) → read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/` (46 items, exit 0) → fast-forward sync (**1 repo advanced — `beevia-admin` +1; `beevia-mobile` already current; 3 refused as `diverged`**; exit 1) → pruning fetch and `git log --all --since` sweep of every ref in all five repos → audit against a `git archive` shadow of `origin/main` (clean) → working-tree audit for the board delta (21 phantom drift lines, §3.2) → content reads of the new `beevia-admin` module, the admin-API counts fix, the Postman diff and the users service → one spec edit and a re-audit (clean) → RFC and suggestions edits → this report and its web edition.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran; no repository was reset, rebased or cleaned; no sub-repo file was edited; the sync's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Files changed this cycle:** `openapi.admin.yaml`, `admin-api-rfc.md`, `suggestions.md`, this report, `web-report/2026-09-22.html`, `web-report/index.html`; new board exports for 22 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`. `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin.proposed.yaml` and `api-rfc.md` needed no change.

**Degraded inputs.**

- **Three repositories remain unsynced** — `beevia-api`, `beevia-admin-api`, `beevia-db-schema` still `diverged` since 8 September (`ahead 1`, behind 38 / 32 / 23). Every code claim is made against `origin/main` via the shadow.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, zero activity). All sprint-0901 figures come from the scratch export, diffed item by item against the 18 Sep scratch export.
- **Four-day window.** No editions ran on 19 or 21 September; figures marked Δ cover 18 Sep 14:03 → 22 Sep 15:20 UTC.
- **GitHub settings are unobservable.** The `gh` token here gets `404` on every repo's branch-rules endpoint, so branch protection, secret scanning, push protection and Dependabot alerts are reported from the board and from commit messages only.
- **Whether any CI run passed is unknowable from a clone**, including the new org `code-scan` workflow.
- **`Comments` bodies are unavailable** from the Zoho API (`commentCount` only); the activity sidecar carries none for this window.
- **The export's "no source key" warning fired on `Epic` again** and is the known 50-row sampling artefact. The column resolves on sprint 0901: 22 of 37 leaves carry an epic; the 15 blanks are genuinely unassigned (11 of them the new QA bugs).
- **Repository integrity was not hash-swept this cycle.**

**Window.** 18 Sep 14:03 UTC → 22 Sep 15:20 UTC. All `actiontime` and board figures are UTC; `git log` was read with `TZ=UTC`.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is performed by a non-contributor whose transitions are reported without naming the actor.

<a id="mvp-method"></a>

### MVP readiness — ≈62% (estimate; 61.70, +0.18)

**Target 2026-09-01 (provisional) · the target date passed twenty-one days ago.** Weights frozen — **no methodology change this edition.** Scores measure build, not acceptance.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | 0 | No change to crypto, keys or sockets in the window |
| 2 | Voice & video calling | 8 | 0.8 | 0 | `FCM_SERVICE_ACCOUNT` still optional and blank — push falls back to a stub |
| 3 | Message translation | 7 | 0.30 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter`; `lib/l10n` still not on `main`. Two items moved to REVIEW/QA — **board status does not score**, and both branches are unmerged |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | 0 | No code change. **Watch:** QA bugs `BVA-I260` (static face-verification placeholder) and `BVA-I257` (BVN field not visible) — to be verified in code next edition, not scored from a title |
| 5 | International KYC tier | 6 | 0.0 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.75 | 0 | `activeNgn()` re-verified at `payment.service.ts:506` |
| 7 | Send / request / receive in chat | 12 | 0.90 | 0 | Unchanged |
| 8 | Cross-currency FX | 12 | 0.0 | 0 | Proposed only |
| 9 | Virtual cards | 10 | 0.70 | 0 | Unchanged |
| 10 | Consent management | 4 | 0.0 | 0 | No endpoint or record |
| 11 | Admin oversight | 6 | **0.95** | **+0.03** | **Named evidence:** `beevia-admin` `c1b0aeb` — Module 4 screens (conversations, per-user activity, report queue, report detail with disclosed messages, review form) **calling all six `/admin/chats` operations through `liveClient`**, so the 18 Sep hold-back "none of it is reachable in a dashboard" no longer applies; plus `b4c545e` making the counts those screens show correct. Still held back: no enforcement link, no prior-report counters, no CI on the dashboard repo |
| | **Weighted total** | **100** | **61.70** | **+0.18** | **≈62%** |

The day's most consequential product work moves the estimate by 0.18, because it completes a capability that was already mostly scored on the server side. The two translation items entering review move it by nothing: unmerged work does not score, however the board describes it.

### What this report cannot tell you

- **Whether branch protection, secret scanning and Dependabot are actually on**, and on which repos. The board says review; a commit message implies a ruleset; GitHub itself is not visible from here.
- **Whether David has unpushed mobile work** for the l10n merge, the report sheet or the QA bugs. Nothing is on any remote ref since 17 Sep.
- **Whether the 20 review items will be reviewed, swept or rolled at tonight's sprint boundary.**
- **Whether the 11 QA bugs were meant to be finished in 0901** or were routed through it into the next sprint.
- **Whether deleting `beevia-api/docs/` was intentional.**
- **Whether the new dashboard works in a browser** — it is wired to the live API in code; nothing was run.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 46, 0 of 12 items estimated.
