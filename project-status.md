# Beevia — Project Status

**As of 2026-08-05** · Sprint 0702 (21 Jul → **07 Aug**, ends in 2 days)
Source: `sprint-board-exports/beevia-sprint-board-2026-08-05.csv`, cross-checked against the code in `beevia-api`, `beevia-admin-api` and `beevia-db-schema`.

---

## Quick overview

> **Delivery is healthy. Verification is the bottleneck, and the PRD gap is not closing.**

| | |
|---|---|
| **Sprint** | 0702 · ends **07 Aug**, 2 days out |
| **Work items** | 89 real tasks (+31 parent stories that roll up) |
| **Done** | **11** (12%) — all design, all one person |
| **In review** | **72** (81%) |
| **In progress** | 6 (7%) |
| **Shipped to the API this cycle** | 10 new consumer endpoints + a whole new admin service (29 endpoints) |

**The three things worth knowing:**

1. **81% of the sprint is sitting in REVIEW/QA, and 97 of those items arrived there in the last 3 days** — 56 of them today. This is an end-of-sprint pile-up, not a stale queue. Nothing is rotting; everything is waiting. With 2 days left, this queue will not clear without a deliberate plan, and the sprint will close with most work "done but unverified".

2. **Zero engineering items are marked Done.** All 11 completions are design work by one person. Every backend and frontend task is in REVIEW/QA. Either the review step is under-resourced, or "Done" is being reserved for something the board isn't capturing — worth settling, because right now the board cannot tell you what has actually landed.

3. **The build is moving away from the PRD, not toward it.** The 10 new consumer endpoints are chat, profile and onboarding refinements. The four capabilities the PRD calls MVP — **multi-currency/FX, virtual cards, international KYC tier, consent management** — remain at zero code, unchanged for two cycles. FX and cards both need a partner selected before engineering can start, so they are the long-lead items and they are not started.

**Biggest risk right now:** the admin API has **no two-factor authentication**, while the dashboard spec makes it mandatory. It is email + password, with no lockout and no rate limiting, guarding accounts that can read customers' BVNs and suspend accounts. Detail in [`admin-api-rfc.md`](./admin-api-rfc.md) §4.3.

**Recommended this week:** (1) triage the review queue before 07 Aug, (2) fix admin auth before any real staff account exists, (3) make a partner decision on FX and card issuing.

---

## 1. Sprint 0702 in detail

### 1.1 How to read the board

The export has 120 rows, but they are two different things:

| | Count | What it is |
|---|---:|---|
| **Parent stories** | 31 | Umbrella items. All marked "Unassigned" and all have child tasks — this is a hierarchy artifact, **not** unstaffed work. |
| **Leaf work items** | 89 | The real units of work: 66 tasks with a parent, plus 23 standalone stories. |

All figures below use the **89 leaf items**. A typical parent looks like `BVA-I146 "User Account Detail View"`, with a design child and a backend child underneath it.

### 1.2 Status

| Status | Items | Share |
|---|---:|---:|
| REVIEW/QA | 72 | 81% |
| Done | 11 | 12% |
| In progress | 6 | 7% |

### 1.3 The review queue is new, not stale

This is the most important nuance in the whole export, and it changes the diagnosis.

| Moved to REVIEW/QA on | Items |
|---|---:|
| 29 Jul | 1 |
| 03 Aug | 16 |
| 04 Aug | 25 |
| **05 Aug (today)** | **56** |

97 of 98 review-queue transitions happened in the last three days. Median time since last touch is **0 days**; the oldest untouched item is 7 days.

So this is **not** a queue of forgotten work. It is a wave of work completing at once, right before the sprint boundary. That is a healthier problem than a rotting backlog — but it produces the same outcome if unaddressed: the sprint closes on 07 Aug with ~80% of items unverified, and either the definition of done quietly slips or the work rolls forward.

Median age since creation is 15 days, against an 18-day sprint. Items are being worked steadily and landing together.

### 1.4 Who is doing what

| Person | Items | Done | In review | In progress | Apparent role |
|---|---:|---:|---:|---:|---|
| David Samuel | 47 | 0 | 44 | 3 | Engineering (26 tasks + 21 stories) |
| Ayomikun Araoye | 28 | 0 | 25 | 3 | Backend (27 tasks, 1 story) |
| Philip Chidera | 14 | **11** | 3 | 0 | Design (all items are screens, UI, flows) |

Two observations:

- **David carries 53% of the sprint** (47 of 89). That is a concentration risk regardless of throughput — it is a single point of failure for both delivery and review.
- **Only design work reaches Done.** Philip's 11 completions are the entire Done column. Design has a working definition of done; engineering does not appear to, or the reviewer for engineering work is the constraint.

### 1.5 By epic

| Epic | Items | Done | In review | In progress |
|---|---:|---:|---:|---:|
| *(no epic)* | 56 | 5 | 48 | 3 |
| Admin | 14 | 6 | 5 | 3 |
| Banking Path (Nigeria / BVN / Anchor) | 8 | 0 | 8 | 0 |
| Onboarding & Authentication | 7 | 0 | 7 | 0 |
| Path Selection & Chat-Only Path | 3 | 0 | 3 | 0 |
| Onboarding Completion & Chat Entry | 1 | 0 | 1 | 0 |

**63% of items have no epic.** Combined with §1.6, this means the board can report activity but not progress-toward-a-goal — you cannot currently answer "how far through the banking path are we?" from this data.

Admin is the healthiest epic, and it is the newest — consistent with it being the current focus.

### 1.6 The board cannot measure velocity

| Field | State |
|---|---|
| Estimation Points | **0 on all 120 items** |
| Priority | **"None" on all 120 items** |
| Tags | **Empty on all 120 items** |
| Epic | Missing on 63% of leaf items |

No estimates means no velocity, no burndown, and no forecast. No priority means the review queue has no triage order — with 72 items and 2 days, something has to decide what gets looked at first, and the board offers nothing.

This is cheap to fix and would pay for itself immediately: even coarse T-shirt sizing on the *remaining* work would tell you whether 07 Aug is achievable.

---

## 2. What actually shipped

Verified against the code, not the board.

### 2.1 Consumer API: 90 → 100 endpoints

| Area | Endpoints | Notes |
|---|---|---|
| **Upgrade ladder** | 6 | `chat_only` → `chat_banking`. Duplicates `/kyc/*` closely — see `api-rfc.md` §5.1 |
| **Clear chat** | 1 | Per-user watermark; survives new messages |
| **Delete message** | 1 | Was a proposal in the last review — now shipped. Sender-only in both modes |
| **Contact change** | 2 | Phone/email change, step-up gated |
| **Contact profile** | — | `GET /users/{id}` now returns relationship-scoped `phone` and shared counts |

The contact-profile work is worth calling out as *good*: `phone` is returned only when the two users already share a conversation, specifically to stop the endpoint becoming a number-harvesting tool. That instinct is what the security findings elsewhere are asking for.

### 2.2 New service: `beevia-admin-api` (29 endpoints)

Three of the dashboard spec's eight modules are built: Authentication (partial), Admin Account Management, and User Management & Support Tools.

The KYC review surface is the strongest part — values masked by default, reveals logged with the admin id, and permissions escalating with how destructive the action is.

### 2.3 Database extracted to a package

Schema and migrations now ship as `@drumbell-technologies/beevia-db-schema`, consumed by both services. This is the structural change that makes a separate admin service defensible rather than risky.

---

## 3. Product-vs-PRD gap

The board shows steady delivery. Measured against the PRD, the gap has not moved.

| PRD MVP capability | State | Change since last cycle |
|---|---|---|
| Multi-currency / FX | **No code.** `PaymentService.activeNgn()` hard-codes NGN | None |
| Virtual cards | **No code.** No module, table, or provider capability | None |
| International KYC tier | **Local (BVN/Nigeria) only** | None |
| Consent management | **No endpoint or record** | None |

**Why this matters now rather than later:** FX and card issuance both require a *partner* to be selected before engineering can begin. They are the longest-lead items in the plan and neither is started. Every other gap on the list is work the team can do unblocked.

There is a legitimate strategic answer here — that multi-currency and cards move to post-launch and the PRD gets re-scoped. What is expensive is the current position: documented as core, treated as later, which leaves the money-handling API shape unsettled for every client that touches it.

---

## 4. Risks

| # | Risk | Severity | Action |
|---|---|---|---|
| 1 | **Admin API has no 2FA**, no lockout, no login rate limiting — guarding BVN access and account suspension | **High** | Fix before any production staff account exists. `admin-api-rfc.md` §4.3 |
| 2 | **Admin guards are per-controller**; a new controller with no decorator is fully unauthenticated | **High** | Register as `APP_GUARD`, make permissions fail-closed. §4.2 |
| 3 | **72 items unverified with 2 days left** | **High** | Triage now; decide what ships vs rolls |
| 4 | **Trust & Safety module is unbuildable as specified** — it asks for "reported messages" but chat is E2EE | **Blocking** | Product decision needed. Three options in `admin-api-rfc.md` §5.1 |
| 5 | **Reports accumulate unread today** — `conversation_reports` is populated by the app; nothing reads it | Medium | Ships with the moderation queue |
| 6 | **Fees and provider routing edited by hand in production** — both documented "admin-managed", no route in either service | Medium | Highest-value item in dashboard Module 6 |
| 7 | **53% of the sprint on one person** | Medium | Spread load; it is a review bottleneck as well as a delivery one |
| 8 | **No estimates, priorities or epics on most items** | Medium | Cheap to fix; currently no forecast is possible |
| 9 | **Admin/consumer tokens share a signing secret** | Low–Medium | Mitigated by a `type` check today. Separate the secrets. §4.1 |

---

## 5. What I would do this week

**Before 07 Aug**
1. **Triage the review queue.** 72 items, 2 days. Decide explicitly what gets verified and what rolls into the next sprint, rather than letting the boundary decide.
2. **Settle what "Done" means for engineering.** Zero engineering items have reached it across an 18-day sprint. Either the gate is unclear or the reviewer is the constraint — both are fixable, but not by accident.

**Before any staff uses the admin dashboard**
3. **2FA, fail-closed guards, separate admin JWT secret, Swagger off in production.** None are features; all are cheaper now than after the first real admin account exists.

**Before the next sprint is planned**
4. **Decide on FX and card-issuing partners** — or formally re-scope them out of MVP. They cannot start without this, and they are the longest lead items in the plan.
5. **Resolve the Trust & Safety / E2EE conflict.** Module 4 is specified in a way the architecture cannot satisfy. Metadata-only moderation is a day's work; reporter-attached excerpts need a consumer-app change and a consent flow.
6. **Add estimates and epics.** Even coarse ones. Without them the next status report will be as unable to forecast as this one.

---

## Appendix — method

- Figures derive from the 89 **leaf** items; the 31 parent stories are excluded to avoid double-counting. Both totals are stated in §1.1 so either can be reconstructed.
- "Unassigned" is a literal value in the export, not an empty field. All 31 such items are parent stories.
- Endpoint counts are derived from controller decorators in each service and cross-checked against `openapi.yaml` (100) and `openapi.admin.yaml` (29), which validate against the code with zero drift.
- Sprint window and status transition dates come from `Sprint Start/End Date` and `Last Modified`.
- The board export was filtered to `Sprints Contains 0702`, so this reflects one sprint, not the whole project history.
