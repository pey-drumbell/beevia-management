# Beevia — Project Status

**As of 2026-08-28** · Sprint **08-01** (10 Aug → 28 Aug, **day 18 of 18 — final day**)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-28.csv` + `beevia-activity-2026-08-28.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision. **New this edition:** a second board (Beevia Admin Dashboard) is now part of the pipeline — see §4.

---

## Quick overview

> **Sprint 08-01 closes today with 10 of 43 leaves Done and 27 — 63% — sitting in a review queue that released nothing in 19 days. The engineering behind it was real; the verification never happened.**

| | 27 Aug | 28 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 3 | **0** | −3 |
| In progress (leaves) | 2 | 6 | +4 |
| Blocked (leaves) | 2 | **0** | −2 |
| **In review / QA (leaves)** | 27 | **27** | 0 |
| **Done (leaves)** | 9 | **10** | +1 |
| Review exits, whole sprint | 0 | **0** | **19 days** |
| API surface (consumer / admin) | 131 / 29 | 131 / 29 | 0 / 0 |
| Commits merged | 21 | 1 | `fix(users)` |

**Team, at a glance:**

| Person | Owns | Final leaf state | Note |
|---|---|---|---|
| Ayomikun Araoye | backend + admin API | 3 In progress, **13 Review/QA**, 3 Done | Shipped 131-operation API surface over the sprint |
| David Samuel | mobile | 1 In progress, **9 Review/QA** | Step-up merged 27 Aug; send money reachable |
| Philip Chidera | design | 2 In progress, 5 Review/QA, **7 Done** | 7 of the sprint's 10 completions |
| Promise Udo | admin dashboard | — | `beevia-admin` **22 days** silent; **now has its own project** (§4) |

**The question for the retrospective:** 27 items entered REVIEW/QA and none ever left, across the entire sprint. Before 08-02 is planned, someone has to say what that state is *for* — because as used this sprint it was a holding pen, not a gate.

**The three things worth knowing:**

1. **The sprint's headline number is 10 Done out of 43, and it flatters the picture.** Seven of the ten are Philip's design items. Of the three backend/mobile completions, the 26 August edition established that several were marked Done in a 60-second batch with no corresponding code. Meanwhile the genuinely large delivery — 23 API operations on 27 Aug, cards, top-ups, payouts, the step-up merge — sits almost entirely in the 27-item review queue, counted as *not done*.
2. **Zero review exits in nineteen days.** This is the single most consistent finding of the sprint, raised in eleven consecutive editions. To do and Blocked are now both empty, so the queue is no longer being fed — it is simply the terminal state for everything that was worked on.
3. **The admin dashboard finally has a home.** A second Zoho project, *Beevia Admin Dashboard*, now exists and the refresh pipeline reads it daily. It has no sprint yet, so there is nothing to report from it — but the blind spot that eleven editions have flagged is now a pipeline step rather than a caveat (§4).

**If you read nothing else:** the code shipped, the verification did not, and 08-02 inherits 27 unexamined items unless today's retrospective disposes of them.

---

## 1. Sprint 08-01 — final state

### 1.1 Where the 43 leaves landed

| Status | Leaves | Share |
|---|---:|---:|
| **Review / QA** | **27** | **63%** |
| Done | 10 | 23% |
| In progress | 6 | 14% |
| To do | 0 | 0% |
| Blocked | 0 | 0% |

Owner split of the review queue: Ayomikun 13, David 9, Philip 5.

### 1.2 What moved on the last day

Nine transitions, in two clusters — David at 12:27/12:43 UTC and Ayomikun's 14 at 12:40:

| Item | Transition |
|---|---|
| BVA-I182 In-Chat Request Flow & Cards | BLOCKED → In progress |
| BVA-I196 Virtual Card Issuance (Anchor) | BLOCKED → In progress |
| BVA-I197 Card Issuance Integration | BLOCKED → In progress |
| BVA-I213 App-Wide Language Setting | To do → **Done** |
| BVA-I214 Settings Language Screen | To do → **Done** |
| BVA-I224/I225 Anchor Reconciliation | To do → In progress |
| BVA-I226/I227 Dashboard Home / Activity Feed | To do → In progress |

Both blocked card items were unblocked on the day the cards API shipped, which is consistent. The two new Done items are language screens — design work, like most of this sprint's completions.

### 1.3 The sprint in one table

| Measure | 10 Aug (start) | 28 Aug (close) |
|---|---:|---:|
| Leaf items | 39 → 43 | 43 |
| Done | 0 | **10** |
| In review | 0 | **27** |
| Review exits | — | **0** |
| Consumer API operations | 105 | **131** (+26) |
| Estimation points set | 0/50 | **0/67** |

The API grew by 26 operations and the board completed 10 items. Those two numbers describe the same sprint and disagree about it, because the work that produced the endpoints is sitting in review.

---

## 2. What shipped this cycle

**One commit.** `fix(users): expose account path on the contact profile` (Ayomikun, 27 Aug 13:10 UTC) — adds `path` to the contact profile so the client can gate money actions: you can only send to a `chat_banking` peer.

| Repo | Last commit to `main` | Days |
|---|---|---:|
| `beevia-api` | **28 Aug** | **0** |
| `beevia-mobile` | 27 Aug | 1 |
| `beevia-db-schema` | 26 Aug | 2 |
| `beevia-admin-api` | 6 Aug | **22** |
| `beevia-admin` | 6 Aug | **22** |

---

## 3. Spec updates made this cycle

The route count did not move (131), so the audit reported no drift — but the commit changed a **response shape**, and chasing it surfaced a larger pre-existing gap.

**What the spec said:** `GET /users/{id}` and `GET /users/by-username/{username}` return `PublicProfileOk` — the lean six-field chat profile.

**What the code returns:** `ContactProfile`, which extends that with `phone`, `joined_at`, `conversation_id`, `media_count`, `payment_count` — and now `path`. A client generated from the spec would have been missing six fields on both routes, five of them for longer than this sprint.

Edits to `openapi.yaml`:

- New **`ContactProfile`** schema (`allOf` on `PublicProfile` plus the six extras), with `path` documented as the money-gating field added 27 Aug.
- New **`ContactProfileOk`** response; both single-user routes repointed to it, and their summaries corrected from "public profile" to "contact profile".
- The **phone-visibility rule is now in the spec**: `phone` is relationship-scoped, non-null only when a 1:1 conversation exists or you are viewing yourself. Any authenticated caller can pass an arbitrary id, so returning it unconditionally would make this a number-harvesting endpoint. That reasoning existed only as a controller comment.
- `PublicProfile`'s description now says what it is *not* used for, and the same text was applied to the proposed copy so the two do not diverge.

Post-edit audit: `code=131 spec=131`, `29/29` admin, all four specs valid, no drift.

**This is the fourth contract-without-route change in eight days** (upgrade semantics 21 Aug, contacts sync 24 Aug, cards' security model 27 Aug, contact profile today). Every one was found by reading a diff against the spec by hand; the automated check cannot see any of them.

---

## 4. Admin dashboard board — *new section*

Per the owner's decision, the refresh pipeline now reads a **second Zoho project** and reports it here, separately from the main sprint.

| | |
|---|---|
| Project | **Beevia Admin Dashboard** (`187554000000127002`, project no. 8) |
| Status | Active, **no sprints, no start/end dates** |
| Board export | Step 1b returns *nothing to export* (exit 3) |

**There is nothing to report from it yet, and that is the status.** It answers a question these reports have raised in eleven consecutive editions: the admin dashboard workstream had no board presence, so Promise Udo has never had a row anyone could read and `beevia-admin` silence could only be inferred from commits.

Once it carries a sprint, this section fills in and Promise gets a real row sourced from that board. Until then the standing rule holds: report the responsibility, judge the work from commits — and `beevia-admin` is at **22 days** with no commits, no branches.

Pipeline notes, for whoever runs this next:

- The two boards are **never summed**. Different projects, different sprints; a combined leaf count would be meaningless.
- Admin exports land in `sprint-board-exports/admin/`, deliberately. `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and treats every match as a snapshot of *one* board — a second project's CSV in the main folder would make it diff two unrelated boards and report invented movement.
- When the board gets a sprint, its name will not match the main `ZOHO_SPRINT_FILTER`, so step 1b keeps skipping until `--sprint` is passed. A silent exit 3 after the board is live means exactly that.

---

## 5. Risks carried into 08-02

1. **27 unexamined items.** If they carry over untouched, 08-02 starts two-thirds full of work nobody has verified.
2. **A review state with no demonstrated exit path.** Nineteen days, zero exits; no accept/reject owner was ever named.
3. **A large money-handling surface is unverified.** Cards, top-ups and payouts all shipped in the last two days and went straight into that queue.
4. **The client is ~23 endpoints behind the API.** No `/cards`, `/topups`, `/wallets/banks` or `/wallets/transfers` references in `beevia-mobile`.
5. **Contract drift is invisible to automation** — four instances in eight days, all caught by hand.
6. **Both admin repos at 22 days.** The new project gives the workstream a home; it does not give it commits.
7. **The sprint closes with 0/67 estimated**, so the carry-over conversation has no size data — as every edition since 11 Aug has noted.

---

## 6. Previous recommendations — where they stand

| Recommendation from 27 Aug | Status on 28 Aug |
|---|---|
| Spend the last day on the review queue | **Not done.** Queue unchanged at 27; six items moved *into* In progress instead. |
| Exercise one real card end to end | **No evidence.** No demonstration recorded anywhere this pipeline can see. |
| Decide `reveal_ttl_seconds` | **Not done.** Still absent from `CardSecrets`. |
| Point the mobile work at the new surface | **Not done.** Client still has zero references to the 23 new endpoints. |
| `beevia-admin`, twenty-one days | **Not done.** Now 22 — though the workstream now has its own project (§4). |

Zero of five, on the sprint's final day.

---

## 7. What I would do at the retrospective

1. **Dispose of the 27 review items explicitly, item by item, before planning 08-02.** Three buckets: accepted, send back with a reason, or "was never built". The 18 August edition showed several in this queue have no code behind them; carrying those forward silently would put fiction into the next sprint's backlog.
2. **Name one person who can accept out of REVIEW/QA, and require a one-line reason on every exit.** The queue never drained because nobody owned draining it.
3. **Demonstrate the money paths.** One real transfer and one real card lifecycle. Twenty-six operations shipped this sprint and not one has been shown working; the readiness number measures built surface, and the gap between that and *working* is exactly what a demo closes.
4. **Decide whether 08-02 gets estimates.** Two sprints have now closed with no velocity baseline. Either size the items or stop treating sprint capacity as a measurable thing.
5. **Set up the Admin Dashboard board** if the workstream is to be tracked. The project exists and the pipeline reads it; it needs a sprint and items.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`, now with a second export step: main board (67 items, cut-off 14:06 UTC) → **admin board (exit 3, no sprints)** → fast-forward sync (**+1 commit, `beevia-api`**) → deterministic audit (no route drift) → **manual contract review**, which found §3 → this report.

**Why the manual review keeps mattering.** The audit compares route inventories. Today's commit added a field to a response and changed no route, so the check stayed green while two endpoints were documented as returning the wrong object. That is the fourth such case in eight days.

**Window.** 27 Aug 13:01 UTC → 28 Aug 14:06 UTC. CSV header times are the exporting machine's local MDT; `actiontime` values are UTC (per the 20 Aug correction).

**Sources.** Board: `beevia-sprint-board-2026-08-28.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-28.json`. Admin board: none — project has no sprints. Code: five repos at `origin/main`. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈58% (estimate, unchanged)

**Target 2026-09-01 (provisional) · 4 days out.** No score moves: one commit, adding a field to an existing response. The sprint's large delivery was scored yesterday.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live since 10 July, unchanged; batch/languages/preference still proposed |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; NGN wallet auto-provisioned after BVN + profile |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.75 | Bank payouts observable end to end; card top-ups added. Ceiling: server NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | Reachable since the 27 Aug step-up merge. **This edition:** `path` on the contact profile lets the client gate sends on a `chat_banking` peer. Ceiling: request/receive have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.45 | 13 operations live. Ceiling: client has zero `/cards` references, no issuer webhook, no `reveal_ttl_seconds` |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 22 days silent. The new Zoho project changes visibility, not build state |
| | **Weighted total** | **100** | | **57.8 → ≈58%** |

Weights frozen. Scores measure **merged, reachable build evidence** — never board status, items in review, or unmerged branches. Across this sprint the number moved 46% → 58%, driven entirely by code, while the board's Done count moved 0 → 10.

**Team performance — what these figures do not measure.** Philip holds 7 of 10 completions because design items were the ones being closed, not because design outran engineering — Ayomikun's sprint output is a 26-operation API surface that the board records as "in review". With 0/67 estimation points nothing here is normalised, and the review-queue split (13/9/5) measures where work stopped, not who stopped it.

**What this report cannot tell you:**
- **What the 27 review items are worth** — whether they represent finished work, work shipped earlier, or scope that was never built.
- Whether any of the sprint's 26 new operations function; none has been demonstrated and testing stays out of scope for scoring.
- What was decided at the retrospective, which happens after this cut-off.
- Anything about the Admin Dashboard board beyond its existence — it has no sprint.
- Velocity or scope-fit for 08-02 — the sprint closed at 0/67 estimated.
