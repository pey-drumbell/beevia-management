# Beevia — Project Status

**As of 2026-08-24** · Sprint **08-01** (10 Aug → 28 Aug, day 15 of 18, 4 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-24.csv` + `beevia-activity-2026-08-24.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **Four days from the sprint end, 2 of 43 leaves are Done and 10 sit in a review queue that has never released anything. The one-line step-up fix that would make send money work was not made, so the flagship capability still returns 401.**

| | 21 Aug | 24 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 19 | 18 | −1 |
| In progress (leaves) | 10 | 10 | 0 |
| Blocked (leaves) | 3 | 3 | 0 |
| In review / QA (leaves) | 10 | 10 | 0 — *zero exits, 15 days* |
| **Done (leaves)** | 1 | **2** | **+1 — second of the sprint** |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| Commits merged | 4 | **6** | all `beevia-api`, all Friday evening |
| Client step-up token | absent | **absent** | transfer still 401s |
| Estimation points set | 0/67 | 0/67 | still zero |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| Ayomikun Araoye | backend + admin API | 6 To do, 3 In progress, **7 Review/QA**, **3 Blocked** | Shipped all 6 commits — logging, tracing, contacts scale fix |
| David Samuel | mobile | 3 To do, 4 In progress, 3 Review/QA | No commits since PR #27 on Friday; step-up gap unaddressed |
| Philip Chidera | design | 9 To do, 3 In progress, **2 Done** | Both of the sprint's completions are his |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **18 days** silent, still no branches |

**The question for standup:** the sprint ends Friday. With 10 items in review that have never moved, 10 in progress and 3 blocked, what is the plan for the 41 leaves that are not Done — carry them to the next sprint, or cut scope now while there is still time to do it deliberately?

**The three things worth knowing:**

1. **The step-up fix did not happen, and it is the whole capability.** Friday's first recommendation was three small changes: call `/auth/step-up`, keep the token, send `X-Step-Up-Token`. The client still calls `/auth/pin/verify`, still has **zero** step-up references in `lib/`, and the transfer POST still passes no headers. `POST /payments/transfer` is wired and will return 401 on every attempt. Four days left.
2. **Real platform work landed Friday evening — six commits, none of it MVP capability.** Structured `pino` logging with redaction, OpenTelemetry tracing shipped to Axiom (preloaded via pm2), a contacts scalability fix, package updates and a CI runner change. This is genuine engineering maturity and it does not move the readiness number, because none of it is a PRD capability. Worth saying plainly rather than letting it look like idle time.
3. **A shipped contract changed without the spec changing** — caught here, not by the audit. `POST /contacts/sync` went from 500 entries to 25,000, and now returns only the **first 500** resolved inline while queueing the rest to a background worker. The route count never moved, so the drift check stayed green. Fixed in §4, which also proposes the completion endpoint the change now needs.

**If you read nothing else:** the sprint will close with a handful of items Done and a queue nobody has emptied. Decide this week what carries over, and spend the remaining days on the 401 rather than on new work.

---

## 1. Sprint 08-01 — four days out

### 1.1 Status, day 15

| Status | Leaves | Share |
|---|---:|---:|
| To do | 18 | 42% |
| In progress | 10 | 23% |
| Review / QA | 10 | 23% |
| Blocked | 3 | 7% |
| **Done** | **2** | **5%** |
| **Total** | **43** | |

**The arithmetic that matters:** 41 of 43 leaves are not Done. Nothing has ever left REVIEW/QA in this sprint. If the queue behaves for the next four days as it has for the last fifteen, 08-01 closes with **2 accepted items out of 43**.

### 1.2 Everything in the window

Window: **21 Aug 14:12 UTC → 24 Aug 14:55 UTC** (15:12 → 15:55 WAT). Spans the weekend; two board actions, six commits — all of the commits on Friday evening.

| When (UTC) | Who | What |
|---|---|---|
| 21 Aug 15:54 | Ayomikun (`Phoenixdadhev`) | `feat(logging)`: structured pino logging with redaction + Axiom shipping |
| 21 Aug 16:02 | Ayomikun | `feat(tracing)`: OpenTelemetry → Axiom, preloaded via pm2 |
| 21 Aug 16:16 | Ayomikun Araoye | `beevia-api` PR #24 merged (structured logging) |
| 21 Aug 16:50 | Ayomikun | `wip:package update` |
| 21 Aug 17:27 | Ayomikun | **`fix(contacts)`: accept large address books — inline first 500, queue the rest** |
| 21 Aug 17:30 | Ayomikun | `personal runner` |
| 24 Aug 11:04 | Philip Chidera | BVA-I158 Logo Design & Brand Asset Set → **Done** |
| 24 Aug 11:10 | Philip Chidera | BVA-I161 Dark Mode Design — Onboarding & Banking → In progress |

No weekend activity in either stream, which is expected and not a finding.

### 1.3 The step-up gap, unchanged

Friday established that `POST /payments/transfer` is guarded by `StepUpGuard`, requires `X-Step-Up-Token`, and that the client obtains no such token. Re-checked today against `origin/main`:

| Check | Friday | Today |
|---|---|---|
| `verifyPinUrl` | `/auth/pin/verify` | **unchanged** |
| Step-up references in `lib/` | 0 | **0** |
| Headers on the transfer POST | none | **none** |

`/auth/pin/verify` is documented as *"Confirms the PIN … **does not mint a step-up token**"*; `/auth/step-up` is the endpoint that mints one. Until the client switches, the merged send-money flow is unreachable in practice.

This is the third consecutive edition in which the single highest-value action is also one of the smallest.

### 1.4 The review queue, day 15

Ten leaves, **zero exits in fifteen days**. Ayomikun holds 7; David 3.

The queue's composition has not changed since 17 Aug, when eleven items entered in a three-minute bulk operation. The 18 Aug edition established that none of the nine leaves then in review corresponded to code merged during this sprint; nothing since has changed that. BVA-I185 "Wallet Summary Endpoint" is now **10 days** in review with no endpoint on any branch — and PR #27 routed around it entirely, so it may simply be obsolete.

---

## 2. What shipped this cycle

**Six commits, all `beevia-api`, all Friday evening, all Ayomikun.**

| Change | What it is |
|---|---|
| `feat(logging)` + PR #24 | Structured `pino` logging with field redaction, shipped to Axiom over HTTP |
| `feat(tracing)` | OpenTelemetry instrumentation exporting to Axiom, preloaded via pm2 |
| `fix(contacts)` | Address-book sync raised 500 → 25,000 entries; first 500 resolved inline, remainder queued to a `contacts-sync` BullMQ worker |
| `wip:package update`, `personal runner` | Dependency bump and a CI runner change |

**None of this is a PRD capability**, so the MVP number does not move. It is nonetheless the first observability work in the project — until Friday there was no structured logging and no tracing, which is directly relevant to §5: the seven-week KYC failure was invisible partly because nothing was watching.

| Repo | Last commit to `main` | Days |
|---|---|---:|
| `beevia-api` | 21 Aug | 3 |
| `beevia-mobile` | 21 Aug | 3 |
| `beevia-db-schema` | 17 Aug | 7 |
| `beevia-admin-api` | 6 Aug | **18** |
| `beevia-admin` | 6 Aug | **18** |

*Sync note:* `beevia-mobile` was on the `Mock-data` branch locally again and was switched to `main`, then fast-forwarded by one commit (PR #27, which last week's dirty-tree skip had left unpulled). Flagging in case someone was mid-task on that branch.

---

## 3. Product-vs-PRD gap

| PRD capability | State |
|---|---|
| Cross-currency conversion | **Not built.** `PaymentService` resolves NGN unconditionally. |
| Virtual cards | **Not built.** BVA-I198 in review with no code. |
| International KYC tier | **Not built.** |
| Consent management | **Not built.** |
| Payments read path | **Still missing.** No `GET /payments`. |
| Send money, end to end | **Wired but unreachable** — 401 without a step-up token (§1.3). |
| Contact discovery at scale | **Now works to 25,000 entries**, but with no completion signal for the queued remainder (§4). |

---

## 4. Spec and document updates made this cycle

The audit reported no drift — route counts held at 108/29 — but the contacts commit changed a **shipped contract without changing a route**, which the route-count check cannot see. Found by reading Friday's diff against the spec.

**What actually changed in code:** `MAX_SYNC_ENTRIES` 500 → **25,000**; a new `SYNC_INLINE_BATCH = 500` bounds what is resolved synchronously; overflow goes to the `contacts-sync` BullMQ queue and surfaces later via `GET /contacts`.

**What the spec said:** *"Upload up to 500 E.164 phones … returns the entries already registered."* A client following that would have uploaded 500 at a time and treated the response as complete — both now wrong.

Edits made in this repo (no service-repo files touched):

- **`openapi.yaml`** — `POST /contacts/sync` description rewritten: the 25,000 ceiling, the 500-entry inline cap, and an explicit warning that **the response is a first page, not the complete match set**, with `GET /contacts` as the follow-up. `SyncContactsRequest.entries` `maxItems` 500 → **25000**, with the DoS-bound rationale recorded.
- **`openapi.proposed.yaml`** — added **`GET /contacts/sync/status`** with a `ContactSyncStatus` schema. The change created a real gap: a user uploading a large address book gets a partial list and has no way to know when the rest arrives, so the only strategy is to poll and guess. Proposed count 52 → **53**. *This is a proposal I authored, not a team decision — reject it freely if the intended answer is different.*
- **`api-rfc.md`** — the Contacts row read "Complete"; it no longer is. Now 2 implemented / 1 proposed, with the gap named. Proposed total 49 → 50 (53 operations including the three live-endpoint modifications).

Post-edit audit: 108/108 and 29/29, all four specs valid, no drift, no `x-beevia-*` markers.

---

## 5. Risks

1. **The sprint closes Friday with 41 of 43 leaves unfinished** and no decision recorded about what carries over.
2. **The review queue has never drained in fifteen days.** Whatever is agreed for the sprint end, this needs a named owner or it repeats in 08-02.
3. **The flagship capability is unreachable for want of one header** (§1.3), for the third consecutive edition.
4. **Blocked items still carry no reasons** — BVA-I188's four transitions remain unannotated.
5. **Contract drift is invisible to the automated check.** Two instances in four days — the upgrade-path semantics on Friday, contacts today — both found only by reading commits against the spec by hand.
6. **Both admin repos at 18 days**, no commits, no branches, no owned leaves — eighth consecutive edition.
7. **Estimation still 0/67**, so the carry-over conversation will have no size data to work from.

---

## 6. Previous recommendations — where they stand

| Recommendation from 21 Aug | Status on 24 Aug |
|---|---|
| Fix the step-up gap | **Not done.** Client unchanged; transfer still 401s. |
| Then test one real transfer end to end | **Not possible yet** — blocked by the above. |
| Update the board to match the code | **Not done.** BVA-I187 still BLOCKED with PR #27 merged; no comments added. |
| Decide whether BVA-I185 is still needed | **Not done.** Now 10 days in review. |
| `beevia-admin`, fifteen days | **Not done.** Now 18. |

Zero of five. Six commits landed in the same window, all on work not on this list.

---

## 7. What I would do today

1. **Fix the step-up gap this morning.** Three changes, described in Friday's §1.4. With four days left it is the difference between a sprint that delivered its headline capability and one that did not.
2. **Hold a scope conversation today, not Friday.** 41 leaves unfinished, 10 stuck in review. Decide now what is cut, what carries to 08-02, and what must land — while there is time to act on the answer.
3. **Empty the review queue, or admit it is a backlog.** Fifteen days, zero exits. Either someone accepts or rejects these ten this week, or they should be moved out of REVIEW/QA so the next sprint does not inherit a fiction.
4. **Close BVA-I185 if PR #27 made it obsolete** — the client now reads `GET /wallets` and `/wallets/transactions` directly.
5. **Point the new tracing at the money path.** OpenTelemetry landed Friday; a span on `POST /payments/transfer` would have shown the 401 immediately, and would catch the next silent failure of the kind §5 describes.
6. **`beevia-admin`, eighteen days.** Eighth edition.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`, cut-off 14:55 UTC) → fast-forward-only sync (**7 commits pulled across `beevia-api` and `beevia-mobile`; `beevia-mobile` switched from `Mock-data` to `main`**) → deterministic API/spec audit (no route drift) → **manual contract review of the weekend diffs**, which is what found §4 → this report.

**Why the manual review.** The audit compares route inventories. Both contract changes found in the last four days — upgrade-path semantics, contacts sync — kept their routes and changed their meaning, so the check stayed green. Reading each commit's diff against the affected operation is currently the only thing catching this class, and it is manual.

**Window.** 21 Aug 14:12 UTC → 24 Aug 14:55 UTC. Per the 20 Aug correction, CSV header times are the exporting machine's local MDT; `actiontime` values are UTC. WAT (UTC+1) is inferred for the team, not stated in the data.

**Sources.** Board: `beevia-sprint-board-2026-08-24.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-24.json`. Code: five repos at `origin/main`; `beevia-api` +6, `beevia-mobile` +1. Specs after edits: `openapi.yaml` (108), `openapi.proposed.yaml` (**53**), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈50% (estimate, unchanged)

**Target 2026-09-01 (provisional) · 8 days out.** No score moves. Friday's six commits are observability, dependency and scalability work — none is a PRD capability. No client code changed, so #6 and #7 hold.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. Contact discovery now scales to 25,000 entries |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live; provider integration and per-message endpoint BLOCKED; "v2" comment still unrecorded as a decision |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding; face verification fixed 20 Aug after seven weeks broken |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.65 | `GET /wallets` drives the balance, `/wallets/transactions` correct and called, transaction-history screen. Ceiling: server NGN-only, no wallet-summary route |
| 7 | Send / request / receive | 12 | 0.65 | Send wired end to end with a spec-correct body. Ceiling: **step-up token absent, so it 401s** (§1.3); request/receive have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only; BVA-I198 in review with no code |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 18 days silent, no branches |
| | **Weighted total** | **100** | | **50.3 → ≈50%** |

Weights frozen. Scores measure **merged, reachable build evidence**, never board status or items in review.

**Team performance — what these figures do not measure.** Ayomikun shipped all six commits; Philip closed both of the sprint's Done items, which are design deliverables. Neither fact ranks anyone: observability work and brand assets are not comparable units, and with 0/67 estimation points nothing here is normalised. "Zero of five recommendations done" is a statement about where attention went, not about effort — six commits landed in the same window.

**What this report cannot tell you:**
- Whether the transfer works — the step-up gap says 401, read from code, not observed.
- Why BVA-I188 is blocked, or whether PR #27 resolves BVA-I187.
- Whether the new logging and tracing are actually receiving data in Axiom.
- Whether anything else changed contract without changing a route — §4 was found by hand, and only for the commits in this window.
- Velocity or scope-fit for the last 4 days — still 0/67 estimated.
