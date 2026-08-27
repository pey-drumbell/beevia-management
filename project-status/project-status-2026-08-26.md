# Beevia — Project Status

**As of 2026-08-26** · Sprint **08-01** (10 Aug → 28 Aug, day 17 of 18, 2 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-26.csv` + `beevia-activity-2026-08-26.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **Done jumped from 2 to 8 this morning. Nine items were marked complete in a single minute at 07:09 UTC — including the translation stack that was BLOCKED and annotated "moved to version 2" nine days ago — and no code shipped for any of them.**

| | 25 Aug | 26 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 17 | 6 | −11 |
| In progress (leaves) | 8 | 14 | +6 |
| Blocked (leaves) | 2 | 2 | 0 |
| In review / QA (leaves) | 14 | 13 | −1 |
| **Done (leaves)** | 2 | **8** | **+6** |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| Commits merged to `beevia-api` | 0 | **0** | last commit 21 Aug |
| Commits merged to `beevia-db-schema` | 0 | **16** | card top-ups + CI churn |
| Client step-up token on `main` | absent | **absent** | still unmerged, day 17 |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| Ayomikun Araoye | backend + admin API | 2 To do, 4 In progress, **9 Review/QA**, 1 Blocked, 3 Done | Ran the 07:09 bulk completion; shipped the `card_topups` schema |
| David Samuel | mobile | 5 In progress, 4 Review/QA, 1 Blocked | Reversed part of the bulk change at 13:57 and 15:10 |
| Philip Chidera | design | 4 To do, 5 In progress, **5 Done** | Closed BVA-I161 individually at 15:05 |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **20 days** silent, still no branches |

**The question for standup:** BVA-I163 "Translation Provider Integration" and BVA-I167 "Translate Endpoint" were marked Done this morning. `beevia-api` has not been committed to since 21 Aug, and `src/translate/` has not changed since **10 July**. What was completed — and if the answer is "nothing, we are closing them out", is that a descope decision that should be recorded before the sprint closes?

**The three things worth knowing:**

1. **Nine items were completed in one minute, with no code behind them.** At 07:09 UTC Ayomikun moved BVA-I162, I163, I166, I167, I215, I216, I217, I218 and I219 to Done — most straight from BLOCKED or To do, skipping In progress and REVIEW/QA entirely. Six of them are the translation stack. The last `beevia-api` commit was 21 Aug; the translate controller is unchanged since 10 July; the mobile client has one `/translate` reference and its `main` has not moved since 21 Aug. Whatever these completions record, it is not code written this sprint.
2. **BVA-I218 was explicitly deferred nine days ago and is now Done.** On 17 Aug it carried the comment *"we moved this to version 2 we cannot have this currently."* It is now marked complete. If "Done" is being used to mean "removed from scope", that reading needs saying out loud — the MVP rubric has been holding translation at 0.7 partly on the strength of that deferral being unresolved.
3. **Two people are again moving the board in opposite directions.** After the 07:09 batch, David sent BVA-I196 and BVA-I197 back to BLOCKED at 13:57, and at 15:10–15:11 pulled BVA-I179, BVA-I182 and BVA-I176 back out of REVIEW/QA. This is the third occurrence of the pattern (17 Aug, 24 Aug, today) and no transition in any of them carries a comment.

**If you read nothing else:** the sprint is being closed on the board rather than in the codebase. Two days remain to decide which of the eight completions are real, and to merge the one fix that would make the headline capability work.

---

## 1. Sprint 08-01 — two days out

### 1.1 Status, day 17

| Status | Leaves | Share |
|---|---:|---:|
| To do | 6 | 14% |
| In progress | 14 | 33% |
| Review / QA | 13 | 30% |
| Blocked | 2 | 5% |
| **Done** | **8** | **19%** |
| **Total** | **43** | |

### 1.2 The 07:09 completion batch

Twelve transitions inside sixty seconds, from the activity sidecar:

| Item | Transition | Type |
|---|---|---|
| BVA-I162 Translation Service Integration | BLOCKED → **Done** | parent |
| BVA-I163 Translation Provider Integration | BLOCKED → **Done** | leaf |
| BVA-I166 Translate-Message Endpoint | BLOCKED → **Done** | parent |
| BVA-I167 Translate Endpoint | BLOCKED → **Done** | leaf |
| BVA-I215 / BVA-I216 Translate Action & Picker | To do → BLOCKED → **Done** | both, same minute |
| BVA-I217, BVA-I218, BVA-I219 | To do → **Done** | leaves |
| BVA-I196, BVA-I197 Virtual Card Issuance | To do → In progress | |

Note BVA-I215 and BVA-I216 were moved to BLOCKED and then to Done inside the same minute.

**What the code says.** All eight newly-Done leaves are translation or design items. Against them:

| Evidence | State |
|---|---|
| `beevia-api` last commit | 21 Aug 17:30 UTC — five days ago |
| `src/translate/` last changed | **10 July** — one `@Post()` route, unchanged for seven weeks |
| Implemented translate operations | **1** (`POST /translate`) — unchanged all sprint |
| Proposed translate operations | 4, still proposed: `/translate/batch`, `/translate/languages`, `/users/me/translation`, `/conversations/{id}/translation` |
| `beevia-mobile` `main` last commit | 21 Aug 14:10 UTC; one `/translate` reference in `lib/` |

So the endpoints these items describe either shipped seven weeks before the sprint began, or remain unbuilt and proposed-only. Neither reading supports "completed this sprint".

This is not an accusation of anything. Items can legitimately be closed because the work was already done, or because scope was cut. But the board records neither, and with two days left the distinction determines what 08-01 actually delivered.

### 1.3 The reversals

| When (UTC) | Who | What |
|---|---|---|
| 07:09–07:10 | Ayomikun Araoye | 9 items → Done; 7 items To do → REVIEW/QA; 2 → In progress |
| 13:57 | David Samuel | BVA-I196, BVA-I197 In progress → **BLOCKED** |
| 15:05 | Philip Chidera | BVA-I161 In progress → Done *(individual, not part of a batch)* |
| 15:06 | David Samuel | BVA-I202, I204, I205 To do → In progress |
| 15:10–15:11 | David Samuel | BVA-I182 REVIEW/QA → BLOCKED; BVA-I179, BVA-I176 REVIEW/QA → In progress |

The review queue's net movement (14 → 13) hides the churn: seven items were pushed in at 07:10 and several pulled back out at 15:10. As on 17 and 24 August, one person advances a batch and another reverses part of it within hours, with no comment on either side.

### 1.4 The step-up fix, day 17 and still unmerged

`origin/BVA-I187` is now **10 commits ahead** of `main` and gained a `resolved conflicts` commit today at 13:28 UTC, so it is being prepared for merge. It has not merged.

`main` still carries `verifyPinUrl = "/auth/pin/verify"` and **zero** `X-Step-Up-Token` references. `POST /payments/transfer` still returns 401 for every real user, as it has since the endpoint shipped on 17 August.

This is the fourth consecutive edition in which merging one verified branch is the highest-value available action.

---

## 2. What shipped this cycle

**16 commits, all `beevia-db-schema`** — and none of it is consumed yet.

| Change | Detail |
|---|---|
| `feat(schema): add card_topups table + CardTopupDal` | Paystack card top-up funding. `card_topup_status` enum (`pending`/`succeeded`/`failed`/`abandoned`), a pass-on fee model (user picks `fund_amount`, grossed up to `charge_amount`), and `reference` as the idempotency key seeding a `dep_paystack_{reference}` ledger credit |
| Releases v0.0.18, v0.0.19, v0.0.20 | Three releases in one morning |
| 11 × "previous runner" / "self hosted runner" | CI runner migration churn, 07:07–14:45 UTC |

**The consumer has not caught up.** `beevia-db-schema` is at **v0.0.20**; `beevia-api` pins **0.0.17** and `beevia-admin-api` pins **0.0.14**. There is no cards module in `beevia-api`, so `card_topups` is schema-only groundwork — real, but not reachable and not scoring.

| Repo | Last commit to `main` | Days |
|---|---|---:|
| `beevia-db-schema` | **26 Aug** | **0** |
| `beevia-api` | 21 Aug | 5 |
| `beevia-mobile` | 21 Aug | 5 |
| `beevia-admin-api` | 6 Aug | **20** |
| `beevia-admin` | 6 Aug | **20** |

**Specs: no change required.** Audit clean at 108 consumer / 29 admin, no drift. The db-schema change adds a table but no API route, and no consumer imports it yet.

*Sync note:* `beevia-mobile` was skipped as dirty again (`analysis_options.yaml`, `pubspec.lock`). As last week, this did **not** make its analysis stale — local `HEAD` equals `origin/main`, and every client claim here is read from `origin/main` directly.

---

## 3. Risks

1. **The sprint's completion count is not backed by code** (§1.2). With two days left, eight Done items include six whose deliverables predate the sprint or remain proposed-only.
2. **A deferred item is now marked Done** (BVA-I218) without the deferral being resolved or recorded.
3. **The step-up fix remains unmerged on day 17**, so the flagship capability still 401s.
4. **Board contradiction is now a repeating pattern** — three bulk-advance-then-reverse cycles in ten days, none annotated.
5. **The schema is three versions ahead of its consumer** (0.0.20 vs 0.0.17), so `card_topups` cannot be used and the gap will need a coordinated bump.
6. **Both admin repos at 20 days**, no commits, no branches, no owned leaves — tenth consecutive edition.
7. **Estimation still 0/67**, so tomorrow's close has no size data for the carry-over decision.

---

## 4. Previous recommendations — where they stand

| Recommendation from 25 Aug | Status on 26 Aug |
|---|---|
| Merge `BVA-I187` | **Not done.** Conflicts resolved on the branch today; still unmerged, now 10 ahead. |
| Then run one real transfer | **Not possible** — blocked by the above. |
| Triage the 14 review items into accepted / rejected / never-built | **Partly, and not as triage.** Nine items were moved to Done in a batch and several review items reversed; no accept/reject reasoning is recorded anywhere. |
| Confirm who `Fortune Okwu` is | **Not done.** That identity took no action this window. |
| `beevia-admin`, nineteen days | **Not done.** Now 20. |

One partly addressed by a mechanism that raises more questions than it answers; four open.

---

## 5. What I would do today

1. **Merge `BVA-I187` before the sprint closes.** Conflicts are resolved; it is one merge away from making send money work. Two days left.
2. **Take fifteen minutes on the eight Done items and label each one**: shipped earlier, cut from scope, or genuinely completed this sprint. Whatever 08-01's retrospective says about "8 done" will be wrong unless this is settled first.
3. **Record the translation decision explicitly.** BVA-I218's "version 2" comment and its Done status cannot both be current. If translation is descoped, say so — it also unblocks the rubric question flagged on 18 August.
4. **Agree who may move an item to Done, and require a one-line reason.** Three reverse-cycles in ten days points at an unsettled definition rather than at anyone's conduct, and settling it costs one conversation.
5. **Bump `beevia-api` to db-schema v0.0.20** when the cards work starts, or the `card_topups` table stays unreachable.
6. **`beevia-admin`, twenty days.** Tenth edition.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`, cut-off 15:27 UTC) → fast-forward-only sync (**16 commits pulled into `beevia-db-schema`**; `beevia-mobile` skipped as dirty but at the same commit as `origin/main`) → deterministic API/spec audit (clean, no drift, no spec edits) → this report.

**Evidence for §1.2.** The claim that the newly-Done items have no code behind them is four independent checks, not an inference: `git log -1 origin/main` on `beevia-api` (21 Aug) and `beevia-mobile` (21 Aug); `git log -1 -- src/translate/` (10 July); the implemented-vs-proposed translate operation counts in `openapi.yaml` and `openapi.proposed.yaml`; and a `git grep` for `/translate` in the client (1 reference).

**Flow measurement.** All transitions and timings from the activity sidecar's `actiontime`. The 07:09 batch is identifiable as a batch precisely because twelve transitions share one minute — a snapshot diff alone would have reported it as six items of progress, which is the error this pipeline made on 05 August and has guarded against since.

**Window.** 25 Aug 15:24 UTC → 26 Aug 15:27 UTC. Per the 20 Aug correction, CSV header times are the exporting machine's local MDT; `actiontime` values are UTC. WAT (UTC+1) is inferred for the team, not stated in the data.

**Sources.** Board: `beevia-sprint-board-2026-08-26.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-26.json`. Code: five repos at `origin/main`; `beevia-db-schema` +16. Specs: `openapi.yaml` (108), `openapi.proposed.yaml` (53), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈50% (estimate, unchanged)

**Target 2026-09-01 (provisional) · 6 days out.** No score moves. The only merged code is a database table no service imports, and the rubric scores reachable capability. Capability **#3 Message translation holds at 0.7** despite six translation items being marked Done, because the implemented surface is still the single `POST /translate` route that has existed since 10 July — the board's completion signal and the code disagree, and the rubric follows the code. **#9 Virtual cards holds at 0.0**: `card_topups` is card *funding* groundwork, not card issuance, and no service consumes it.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present; contact discovery scales to 25,000 |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live since 10 July, unchanged. Batch, languages, preference and per-conversation operations remain **proposed only**. Six board items marked Done 26 Aug with no corresponding code (§1.2) |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding; face verification fixed 20 Aug |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.65 | `GET /wallets` drives the balance, `/wallets/transactions` correct and called, transaction-history screen. Ceiling: server NGN-only, no wallet-summary route |
| 7 | Send / request / receive | 12 | 0.65 | Send wired end to end with a spec-correct body. Ceiling: **step-up token still absent from `main`, so it 401s** — fix verified on `origin/BVA-I187`, unmerged for a fourth day (§1.4) |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only. `card_topups` table shipped 26 Aug is card *funding*, not issuance, and no service imports it; BVA-I196/I197 (Anchor issuance) went to BLOCKED today |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 20 days silent, no branches |
| | **Weighted total** | **100** | | **50.3 → ≈50%** |

Weights frozen. Scores measure **merged, reachable build evidence** — never board status, items in review, or unmerged branches. That policy is doing visible work this edition: the board's Done count tripled and the number did not move.

**Team performance — what these figures do not measure.** Ayomikun ran the 07:09 batch and shipped the schema work; David reversed part of the batch and opened new items; Philip closed one item individually. The batch is board administration, which the standing guidance says never to read as delivery — and equally, it is not evidence of anything improper. It is a recorded action with no recorded reason, which is the actual finding. With 0/67 estimation points nothing here is normalised.

**What this report cannot tell you:**
- **What the eight Done items represent** — completed work, work that shipped earlier, or scope removed. No comment accompanies any of them.
- Whether translation is descoped, after nine days of the "version 2" comment standing unresolved.
- Why `BVA-I187` has not merged now that its conflicts are resolved; no PR state is visible to this pipeline.
- Whether the step-up fix works against the real API — verified by reading, not by running.
- Velocity or scope-fit for the final 2 days — still 0/67 estimated.
