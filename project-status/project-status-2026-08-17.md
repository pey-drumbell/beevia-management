# Beevia — Project Status

**As of 2026-08-17** · Sprint **08-01** (10 Aug → 28 Aug, day 8 of 18, 11 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-17.csv` + `beevia-activity-2026-08-17.json` (67 items), cross-checked against all five repos re-synced to `origin/main`.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **Code shipped for the first time in a week — 11 commits, three merged PRs, and the direct-transfer API the send-money flow needed — and the blocked P2P item cleared hours later. But the item sitting in REVIEW/QA has no deliverable on `main` to review.**

| | 14 Aug | 17 Aug | Δ |
|---|---:|---:|---:|
| Items (rows / leaves) | 67 / 43 | 67 / 43 | 0 / 0 |
| To do (leaves) | 35 | 33 | −2 |
| In progress (leaves) | 4 | **7** | **+3** |
| Blocked (leaves) | 2 | **1** | **−1** |
| In review / QA (leaves) | 1 | 1 | 0 — *nothing left* |
| Done (leaves) | 1 | 1 | 0 |
| **API surface (consumer / admin)** | 105 / 29 | **108** / 29 | **+3** / 0 |
| **Commits, product repos** | 0 | **11** | **+11** |
| Estimation points set | 0/67 | 0/67 | still zero |

**Team, at a glance:**

| Person | Owns | Current leaf state | Commits since 14 Aug | Flag |
|---|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 16 To do, 2 In progress, 1 Review/QA | **11** | Shipped the whole cycle's code in one day, via 3 reviewed PRs |
| David Samuel | mobile | 6 To do, 3 In progress, **1 Blocked** | 0 | BVA-I170 blocked 4 days; `beevia-mobile` untouched since 6 Aug (his last commit) |
| Philip Chidera | design | 11 To do, 2 In progress, 1 Done | — | Picked up both dark-mode items after midnight on 17 Aug |
| Promise Udo | admin dashboard | one co-assigned parent Story, no owned leaf | 0 | `beevia-admin` now **11 days** silent |

**The question for standup:** BVA-I185 "Wallet Summary Endpoint" has been in REVIEW/QA since 14 Aug, but **no wallet-summary route exists anywhere in `beevia-api`** — the wallets controller has not changed since 22 July. What is being reviewed, and is the work on an unmerged branch? This is very likely the same dependency still blocking David's BVA-I170.

**The three things worth knowing:**

1. **The board/code divergence broke, decisively, in the right direction.** Ayomikun landed 11 commits across `beevia-api` and `beevia-db-schema` today, all through merged PRs (#20, #21, #22): the direct-transfer payments surface, a BVN-lookup cache to shield the YouVerify rate limit, and a fix flipping accounts to banking at provisioning rather than at the email step. This is the first product code since 10 Aug and it answers the 14 Aug recommendation to ask for reviewable PRs — that one worked.
2. **The shipped API unblocked the board within hours.** `POST /payments/transfer` merged at 06:34 UTC; BVA-I188 "P2P Transfer" came off BLOCKED at 12:59 and into In progress at 13:00. The sequence is consistent with the missing backend being the actual blocker, which is the answer the 14 Aug edition asked for and could not get.
3. **One item is in a verification state with nothing to verify.** BVA-I185 was marked Done on 13 Aug, reopened into REVIEW/QA on 14 Aug, and has sat there three days. The wallets controller still exposes the same seven routes it had on 22 July, and the +3 API growth this cycle is entirely payments. Either the endpoint is on an unmerged branch or the item's state does not reflect its deliverable — and until it resolves, BVA-I170 has no endpoint to wire.

**If you read nothing else:** delivery restarted and immediately cleared a blocker, which is the model to repeat. The remaining drag is a review queue of one that has never drained and whose contents cannot be located on `main`.

### MVP readiness — ≈46% (estimate, headline unchanged; one sub-score moved)

**Target 2026-09-01 (provisional) · 15 days out.** Capability **#7 (send / request / receive) moves 0.45 → 0.50** on named evidence: three endpoints shipped that serve the send-money flow directly — `POST /payments/transfer` (non-escrow, idempotent on `idempotencyKey`), `GET /payments/recipients` and `GET /payments/recent-recipients`. The API side of that capability is now close to complete.

The headline does not move (45.5 → 46.1 weighted, still ≈46%) because **the client remains entirely unwired**: `beevia-mobile/lib` contains **zero references to `/payments`**, and its last `lib/` change was 11 Aug. A capability the user cannot reach does not score as built. The BVN cache and upgrade-path fix are hardening on an already-0.9 capability (#4) and do not move it.

---

## 1. Sprint 08-01 — delivery restarts, review does not

### 1.1 Status, day 8

| Status | Leaves | Share |
|---|---:|---:|
| To do | 33 | 77% |
| In progress | 7 | 16% |
| Blocked | 1 | 2% |
| Review / QA | 1 | 2% |
| Done | 1 | 2% |
| **Total** | **43** | |

67 rows: 24 parent Stories grouping 43 leaf Tasks. Leaf counts used throughout.

### 1.2 What moved since 14 Aug

All timings from the activity sidecar, never `Last Modified`. The actor who clicked a transition is not always the item's owner; both are shown.

| Item | Owner | Transition | Actor | When (UTC) |
|---|---|---|---|---|
| BVA-I159 Dark Mode Design — Core Navigation & Home | Philip | To do → In progress | Philip | 17 Aug 00:14 |
| BVA-I160 Core Screens Dark Mode | Philip | To do → In progress | Philip | 17 Aug 00:14 |
| BVA-I187 Send Money to Another Beevia User (P2P) *(parent)* | Philip, David, Ayomikun | BLOCKED → To do → In progress | David | 17 Aug 12:59 → 13:00 |
| BVA-I188 P2P Transfer | Ayomikun | **BLOCKED → To do → In progress** | David | 17 Aug 12:59 → 13:00 |
| BVA-I194 External Transfer Screens | David | To do → In progress | David | 17 Aug 13:57 |

No items were added or removed. WIP rose from 4 to 7 leaves.

### 1.3 The blocked item and the review item are probably the same dependency

| State | Item | Owner | Since | Age |
|---|---|---|---|---:|
| BLOCKED | BVA-I170 Wire Real Response into Wallet Screen | David | 13 Aug 16:06 | **4d** |
| REVIEW/QA | BVA-I185 Wallet Summary Endpoint | Ayomikun | 14 Aug 12:19 | **3d** |

BVA-I170 is the client-side wiring of a wallet response; BVA-I185 is the endpoint that would supply it. The board records no reason field, so the link is inference — but it is the reading the evidence supports, and it is testable at standup with one question.

What the code says about BVA-I185, stated precisely so it can be checked:

- `beevia-api/src/wallets/wallets.controller.ts` was **last modified 22 July** and exposes seven routes: `GET /wallets`, `POST /wallets`, `GET /wallets/payin-details`, `GET /wallets/beneficiaries`, `GET /wallets/transactions`, `GET /wallets/{walletId}/transactions`, `POST /wallets/withdraw`.
- A repo-wide search for a wallet-summary route or handler returns nothing.
- This cycle's +3 operations are all under `/payments`.

So the deliverable is not on `main`. The benign explanation is an unmerged branch; the report cannot distinguish that from an item whose state is ahead of its work.

### 1.4 Review still has an entry and no exit

The audit flags it for the second consecutive edition: **nothing has left REVIEW/QA between snapshots.** Queue depth is 1, median age 3 days. One item is not a crisis, but 0702 ended with 78 items in this state, so the pattern is worth stopping early rather than late. No accept/reject owner has been named — the 14 Aug recommendation on this is unresolved.

### 1.5 What is still missing

- **Estimation points: 0 of 67**, day 8 of 18. Recommended on days 2, 3, 4 and 5. The sprint will end without a velocity baseline.
- **Epics: 8 of 67** (all `Admin`), unchanged since 13 Aug.
- **Tags: 0 of 67.**
- **Blocked-reason field:** still absent from the exported evidence.

---

## 2. What shipped this cycle

**11 commits, all on 17 Aug, all in `beevia-api` and `beevia-db-schema`, all authored by Ayomikun** (as `Phoenixdadhev`, merged under `Ayomikun Araoye`).

| PR | What | Repos |
|---|---|---|
| #21 | `feat(payments)`: direct transfer + recipient search/recent for the Send Money flow | `beevia-api` |
| #22 | `feat(kyc)`: cache BVN lookups to shield the YouVerify rate limit, backed by a new `bvn_lookups` table + `BvnLookupDal` | `beevia-api`, `beevia-db-schema` |
| #20 | `fix(upgrade)`: flag the account as banking at provisioning, not at the email step | `beevia-api` |

`beevia-db-schema` released **v0.0.16 and v0.0.17**.

**API surface: 105 → 108 consumer operations.** The audit found all three undocumented; they are now specified in `openapi.yaml` (see §5):

| Route | Contract |
|---|---|
| `POST /payments/transfer` | Direct, non-escrow move to another banking user. Targets a **user id**, not a phone. Idempotent on `idempotencyKey` (stored as the payment's `reference`). One balanced SERIALIZABLE ledger transaction; lands `completed`. Step-up required. NGN→NGN only. |
| `GET /payments/recipients` | Recipient picker search, banking-enabled users only, ≤20 rows, **never returns a phone**. |
| `GET /payments/recent-recipients` | Distinct recent send counterparties, newest first, ≤15 rows, drawn from the last 60 sends. |

Repo staleness on 17 Aug:

| Repo | Last commit | Days | Note |
|---|---|---:|---|
| `beevia-api` | 17 Aug | **0** | Ayomikun, 3 PRs |
| `beevia-db-schema` | 17 Aug | **0** | Ayomikun + release bot |
| `beevia-mobile` | 11 Aug | 6 | owner's test/pipeline commit; David's last was 6 Aug |
| `beevia-admin-api` | 6 Aug | **11** | |
| `beevia-admin` | 6 Aug | **11** | |

The two admin repos have now been silent for eleven days. This measures visible `main`, not local work.

---

## 3. Product-vs-PRD gap

| PRD capability | State |
|---|---|
| Cross-currency conversion | **Not built.** `PaymentService` still resolves NGN unconditionally via `activeNgn()` — including in the new `transfer()` path. |
| Virtual cards | **Not built.** Board/design work active (BVA-I198, I207, I209); no provider-backed module or table shipped. |
| International KYC tier | **Not built.** Local Nigerian path only, now with a BVN-lookup cache. |
| Consent management | **Not built.** |
| Payments read path | **Still missing, and now more load-bearing.** No `GET /payments`. The new transfer settles immediately and recovers only by replaying the idempotency key, so a client that loses the response cannot confirm the money moved. Recorded in `api-rfc.md` §4.4. |
| Send-money client wiring | **Not built.** The API is nearly complete; `beevia-mobile/lib` has zero `/payments` references. |

---

## 4. Risks

1. **BVA-I185 sits in REVIEW/QA with no locatable deliverable on `main`**, and it plausibly gates BVA-I170. Highest-value question of the day.
2. **The review queue has still never drained** — second consecutive edition with zero exits and no named accept/reject owner.
3. **The client is now the binding constraint on the flagship capability.** The send-money API is essentially done; the mobile side has not been touched since 6 Aug by its owner. Capability #7 cannot progress further from the backend.
4. **Both admin repos are eleven days silent**, and the admin-dashboard workstream still has no owned leaf on the board.
5. **Delivery is concentrated in one person.** All 11 commits this cycle came from Ayomikun, who also holds 19 of 43 leaves, the review item, and both backend gates. This is a bus-factor and sequencing risk, not a performance observation.
6. **Estimation remains 0/67** on day 8; scope-fit for the remaining 11 days cannot be defended numerically.
7. **WIP rose from 4 to 7 leaves while throughput stayed at zero completions.** Starting more work while nothing finishes is how 0702's queue formed.

---

## 5. Spec and document updates made this cycle

The audit found drift and it has been resolved in this repo (no service-repo files were touched):

- **`openapi.yaml`** — added `POST /payments/transfer` with a new `TransferRequest` schema, plus `GET /payments/recipients` and `GET /payments/recent-recipients`, both reusing the existing `PublicProfileListOk` response since `PublicProfile` already matches the code's `ChatUserProfile` projection exactly. Implemented count 105 → **108**. No `x-beevia-*` markers; the file stays client-generation safe.
- **`openapi.proposed.yaml`** — unchanged. None of the three routes had been proposed, so nothing needed moving; still 52 operations.
- **`api-rfc.md`** — §3 Payments row 6 → **9** with the three additions named, total 105 → **108**; §6.7 inventory extended with the three routes; §4.4 extended to record that the immediate-settlement transfer makes the missing read path more load-bearing, not less.

Post-update audit: `code=108 spec=108` for `beevia-api`, `29/29` for `beevia-admin-api`, all four specs valid, **no drift**.

---

## 6. Previous recommendations — where they stand

| Recommendation from 14 Aug | Status on 17 Aug |
|---|---|
| Add a reason, owner and unblock date to BVA-I170 and BVA-I188 | **Half done by delivery, not by process.** BVA-I188 cleared hours after the transfer endpoint merged. BVA-I170 is still blocked at 4 days, and no reason field was added to either. |
| Assign an accept/reject owner for BVA-I185 and define exit evidence | **Not done.** Three days in review, zero exits, and the deliverable is not on `main`. |
| Ask for reviewable branches or small PRs | **Done, and it worked.** Three PRs merged, 11 commits, the API surface moved for the first time since 07 Aug. Repeat this. |
| Confirm the message-translation architecture decision | **No evidence either way.** `POST /translate` unchanged; no board or code movement on the on-device direction. |
| Choose whether 08-01 will be estimated | **Not done.** Still 0/67 on day 8. |

One landed and produced the cycle's only delivery; one was overtaken by events; three are open.

---

## 7. What I would do today

1. **Locate BVA-I185.** One question: is the wallet-summary endpoint on an unmerged branch, or has the item been moved ahead of the work? Either answer unblocks David's BVA-I170; not answering keeps a 4-day block alive.
2. **Repeat this morning's pattern.** Small branch → PR → merge produced the entire week's visible delivery in one day and cleared a blocker. Ask for the same shape for the wallet summary and the mobile work.
3. **Point the mobile work at the API that now exists.** `/payments/recipients`, `/payments/recent-recipients` and `/payments/transfer` are live and are exactly what the Send Money screens need. The client has zero `/payments` calls — that is now the only thing between the API and a demonstrable capability.
4. **Name one person who can accept out of REVIEW/QA**, and cap WIP until something exits. Seven items in progress against zero completions is the shape 0702 ended in.
5. **Ask about the two admin repos** — eleven days silent, and the dashboard still has no owned leaf on the board.
6. **Estimate or stop measuring.** Day 8 of 18. Either size the 33 remaining To do items or drop velocity language from the sprint.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`) → sanctioned fast-forward-only sync of five product repos (**11 commits pulled** across `beevia-api` and `beevia-db-schema`) → deterministic API/spec audit (**drift found: 3 routes**) → spec + RFC updates (§5) → re-audit clean → this report.

**Sources.**
- Board: `beevia-sprint-board-2026-08-17.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-17.json`
- Code: all five repos at `origin/main`; 11 commits since 14 Aug
- Specs after update: `openapi.yaml` (108), `openapi.proposed.yaml` (52), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — all validated, no drift

**Flow measurement.** Transitions and timings come from the activity sidecar's `actiontime`, never `Last Modified`, which bulk board operations rewrite without producing audit entries.

**Claims about absent code** (no wallet-summary route; zero `/payments` references in the client) are search results over the synced working trees at `origin/main`, and are stated with the file and date so they can be falsified directly. They say nothing about unmerged branches.

### MVP readiness — ≈46%

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live and `translate_chat_screen` present; batch + language list proposed; on-device privacy direction undecided |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding. **This cycle:** BVN-lookup cache + provisioning fix — hardening, not new capability, so unchanged |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.45 | NGN only, `activeNgn()` hard-coded; wallets controller unchanged since 22 July; no wallet home/balance screen in the client |
| 7 | Send / request / receive | 12 | **0.50** ↑ | **Moved this cycle.** API write path now near-complete: escrow send, direct `POST /payments/transfer` (idempotent), plus the recipient picker. Held well below 1.0 because the client has **zero `/payments` calls** |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; the PRD's headline differentiator |
| 9 | Virtual cards | 10 | 0.0 | proposed only; three board items active, no code |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; dashboard Modules 1 & 3 landed; both admin repos 11 days silent |
| | **Weighted total** | **100** | | **46.1 → ≈46%** |

Weights are frozen, so the number stays comparable across editions. Scores measure **build evidence** — a shipped endpoint, a landed module, a wired screen — never board status, design completion, commit-message claims, or items in review. A proposed-only area scores 0.

**Team performance — what these figures do not measure.** With 0/67 estimation points there is no workload normalisation: Ayomikun's 19 leaves and David's 10 are not comparable and neither reflects difficulty. Commit counts reward small commits — today's 11 include merge commits and a package bump. One person shipping the whole cycle is a sequencing and bus-factor fact, not a statement about anyone else's effort; where an item cannot proceed because a dependency is unmerged, that is a process finding.

**What this report cannot tell you:**
- Whether BVA-I185's endpoint exists on an unmerged branch. The search only covers `origin/main`.
- Why BVA-I170 is blocked — the board carries no reason field; §1.3's link is inference.
- Whether unpushed local work exists in `beevia-mobile`, `beevia-admin` or `beevia-admin-api`.
- Whether the three new payment endpoints function correctly or are covered by tests — testing remains out of scope for scoring, per the owner. Draft testing rules are staged in `agent-rules/`, unapplied.
- Who `Fortune Okwu` is — unresolved since 11 Aug, though the identity took no action this cycle.
- Velocity or scope-fit for the remaining 11 days — still 0/67 estimated.
