# Beevia — Project Status

**As of 2026-08-25** · Sprint **08-01** (10 Aug → 28 Aug, day 16 of 18, 3 days left)
Sources: `sprint-board-exports/beevia-sprint-board-2026-08-25.csv` + `beevia-activity-2026-08-25.json` (67 items), cross-checked against all five repos and every pushed branch.

Scope: current sprint only, per the 12 Aug decision.

---

## Quick overview

> **The step-up fix is written, correct, and sitting on an unmerged branch. Meanwhile the review queue grew to 14 — a third of the sprint — and has still never released a single item in sixteen days.**

| | 24 Aug | 25 Aug | Δ |
|---|---:|---:|---:|
| To do (leaves) | 18 | 17 | −1 |
| In progress (leaves) | 10 | 8 | −2 |
| Blocked (leaves) | 3 | 2 | −1 |
| **In review / QA (leaves)** | 10 | **14** | **+4 — 33% of the sprint** |
| Done (leaves) | 2 | 2 | **0 — unchanged since yesterday** |
| Review exits, all sprint | 0 | **0** | 16 days |
| API surface (consumer / admin) | 108 / 29 | 108 / 29 | 0 / 0 |
| Commits merged to any `main` | 6 | **0** | — |
| Client step-up token | absent | **absent on `main`, done on a branch** | unmerged |

**Team, at a glance:**

| Person | Owns | Current leaf state | Flag |
|---|---|---|---|
| Ayomikun Araoye | backend + admin API | 6 To do, 2 In progress, **9 Review/QA**, 2 Blocked | Holds 9 of the 14 review items; no commits this window |
| David Samuel | mobile | 2 To do, 3 In progress, **5 Review/QA** | **Wrote the step-up fix** (24 Aug 16:31 UTC) — unmerged on `origin/BVA-I187` |
| Philip Chidera | design | 9 To do, 3 In progress, 2 Done | Both of the sprint's completions remain his |
| Promise Udo | admin dashboard | one co-assigned parent Story | `beevia-admin` **19 days** silent, still no branches |

**The question for standup:** the send-money fix is finished and correct on `origin/BVA-I187`. Merging it is the difference between 08-01 delivering its headline capability and not. Three days left — what is stopping the merge?

**The three things worth knowing:**

1. **The step-up gap is solved — on a branch nobody has merged.** David's `p2p money transfers` commit (24 Aug 16:31 UTC) does exactly the three things recommended on Friday: adds `stepUpUrl = "/auth/step-up"`, holds the returned token in `WalletProvider`, and sends `Options(headers: {'X-Step-Up-Token': stepUpToken})` on the transfer. It even reads the response defensively (`step_up_token ?? stepUpToken`), which matches what the API actually returns, and the mock routes were updated to validate the header. It is **not on `main`**, so it does not score and no user can reach it.
2. **The review queue is now a third of the sprint and has never released anything.** Fourteen of 43 leaves, median age 8 days, zero exits in sixteen days. Ayomikun holds 9, David 5. Four more items were pushed in yesterday at 16:08–16:12 UTC by `Fortune Okwu` — six transitions in four minutes, the same bulk pattern as 17 Aug.
3. **The board moved ahead of the code again, by 23 minutes.** BVA-I188 "P2P Transfer" went BLOCKED → REVIEW/QA at 16:08 UTC. The commit that actually fixes it landed at **16:31 UTC** — after the item was already marked ready for review. BVA-I200 "Transaction History Endpoint" also entered review, while the API route count stayed at 108; no new backend endpoint shipped.

**If you read nothing else:** the fix for the sprint's headline capability is written and sitting unmerged, and the queue meant to verify work has not verified anything in sixteen days. Three days remain to act on either.

---

## 1. Sprint 08-01 — three days out

### 1.1 Status, day 16

| Status | Leaves | Share |
|---|---:|---:|
| To do | 17 | 40% |
| In progress | 8 | 19% |
| **Review / QA** | **14** | **33%** |
| Blocked | 2 | 5% |
| Done | 2 | 5% |
| **Total** | **43** | |

41 of 43 leaves are still not Done, unchanged from yesterday. What changed is where they sit: four moved from In progress/BLOCKED into a queue that has never had an exit.

### 1.2 Everything in the window

Window: **24 Aug 14:55 UTC → 25 Aug 15:24 UTC** (15:55 → 16:24 WAT). Seven board actions, zero merges to any `main`, one commit on a branch.

| When (UTC) | Who | What |
|---|---|---|
| 24 Aug 15:32 | David Samuel | BVA-I208 Secure Card Entry UI → In progress |
| 24 Aug 16:08 | `Fortune Okwu` | BVA-I187, BVA-I188 BLOCKED → **REVIEW/QA** |
| 24 Aug 16:08 | `Fortune Okwu` | BVA-I199, BVA-I200, BVA-I201 In progress → **REVIEW/QA** |
| 24 Aug 16:12 | `Fortune Okwu` | BVA-I178 Send Flow In progress → **REVIEW/QA** |
| **24 Aug 16:31** | **Davidtariq96** | **`p2p money transfers` — the step-up fix, committed to `origin/BVA-I187`** |

Six of the seven board transitions were made by `Fortune Okwu` inside four minutes — an identity whose role has never been confirmed across ten editions, and which has now performed two bulk review-queue operations (17 Aug, 24 Aug).

### 1.3 The step-up fix, verified on the branch

Read directly from `origin/BVA-I187`, not from the commit message:

| Requirement (from Friday's §1.4) | State on the branch |
|---|---|
| Call `/auth/step-up`, not `/auth/pin/verify` | ✅ `const stepUpUrl = "/auth/step-up";` |
| Retain the returned token | ✅ `_stepUpToken` held in `WalletProvider`; cleared on failure |
| Send `X-Step-Up-Token` on the transfer | ✅ `options: Options(headers: {'X-Step-Up-Token': stepUpToken})` |
| Guard the call when no token is held | ✅ bails if `stepUpToken == null \|\| isEmpty` |

Two details worth crediting, because both are the class of thing that has bitten this project before:

- **The response field is read defensively** — `data['step_up_token'] ?? data['stepUpToken']`. The API returns `{ stepUpToken }` in code, which the response interceptor snake-cases to `step_up_token` over the wire, matching the spec. Either spelling works, so this cannot fail the way the `/payments/transactions` URL did.
- **The mock backend was updated too** — `lib/mock/http/routes/wallet_routes.dart` now reads `options.headers['X-Step-Up-Token']`, so the mock enforces the same contract as the real guard.

**But `main` is unchanged.** `verifyPinUrl = "/auth/pin/verify"` is still what ships, there are still zero step-up references in `main`'s `lib/`, and `POST /payments/transfer` still returns 401 for every real user. Per the rubric, branch work does not score.

Scope note: `origin/BVA-I187` reads as 9 commits ahead because PR #27 was squash-merged on 21 Aug, so the pre-squash commits still count as divergent. Only **one** commit is genuinely new since that merge — the 24 Aug step-up work. The branch is also 1 commit behind `main` and will want a rebase or merge first.

### 1.4 The review queue, day 16

**Fourteen leaves. Zero exits in sixteen days. Median age 8 days.**

| Owner | Items |
|---|---:|
| Ayomikun Araoye | 9 |
| David Samuel | 5 |

Full queue: BVA-I165, I169, I170, I173, I178, I185, I188, I189, I198, I200, I201, I203, I221, I223.

Two observations that have held across editions and still hold:

- **BVA-I185 "Wallet Summary Endpoint"** is now **11 days** in review, and `wallets.controller.ts` remains unchanged since 22 July. PR #27 routed around it; it is very likely obsolete.
- **BVA-I200 "Transaction History Endpoint"** entered review yesterday while the consumer API stayed at 108 routes. Wallet transactions are served by the pre-existing `GET /wallets/transactions`, so either the item is satisfied by code that shipped long ago, or its deliverable does not exist — the same ambiguity the 18 Aug edition documented for nine other items, still unresolved.

---

## 2. What shipped this cycle

**Nothing merged to any `main`.** All five repos were already current on sync.

| Repo | Last commit to `main` | Days |
|---|---|---:|
| `beevia-api` | 21 Aug | 4 |
| `beevia-mobile` | 21 Aug | 4 |
| `beevia-db-schema` | 17 Aug | 8 |
| `beevia-admin-api` | 6 Aug | **19** |
| `beevia-admin` | 6 Aug | **19** |

**Unmerged branch work across the estate:**

| Repo | Branch | Ahead | Tip | Contents |
|---|---|---:|---|---|
| `beevia-mobile` | **`BVA-I187`** | 9 (1 genuinely new) | 24 Aug | **The step-up fix** (§1.3) |
| `beevia-mobile` | `Mock-data` | 7 | 24 Aug | Owner's mock-backend work |
| `beevia-mobile` | `Deps-updates-2026-08-20` | 4 | 21 Aug | Dependency bumps |
| `beevia-api` | `victor` | 1 | 20 Jul | Stale |

**Specs: no change required.** Audit clean at 108 consumer / 29 admin, no drift — unsurprising, since nothing merged that could have moved a contract. Yesterday's contacts and proposed-endpoint edits stand.

*Sync note:* `beevia-mobile` was on the `Mock-data` branch locally for the third consecutive run and was switched to `main`. If someone is working there routinely, the sync will keep moving them off it — worth knowing.

---

## 3. Risks

1. **The sprint ends in three days with 2 of 43 leaves Done** and no recorded decision on what carries to 08-02.
2. **A finished, verified fix for the headline capability is sitting unmerged** with three days left (§1.3).
3. **The review queue is now 33% of the sprint and has never released an item.** Fourteen items with no exit path in sixteen days will function as backlog once the sprint closes, whatever the column is called.
4. **The board continues to run ahead of the code** — yesterday by 23 minutes on BVA-I188, and BVA-I200 entered review with no new endpoint.
5. **`Fortune Okwu` performed a second bulk review-queue operation** (six transitions in four minutes) and the identity is still unconfirmed after ten editions.
6. **Both admin repos at 19 days**, no commits, no branches, no owned leaves — ninth consecutive edition.
7. **Estimation still 0/67**, so Friday's carry-over conversation has no size data.

---

## 4. Previous recommendations — where they stand

| Recommendation from 24 Aug | Status on 25 Aug |
|---|---|
| Fix the step-up gap this morning | **Done in code, not in `main`.** Written 24 Aug 16:31 UTC on `origin/BVA-I187`; unmerged. |
| Hold a scope conversation today | **No evidence either way.** No board or commit signal; may have happened off-record. |
| Empty the review queue, or admit it is a backlog | **Went the other way.** 10 → 14, still zero exits. |
| Close BVA-I185 if PR #27 made it obsolete | **Not done.** Now 11 days in review. |
| Point the new tracing at the money path | **No evidence either way** — `beevia-api` received no commits during this window. |
| `beevia-admin`, eighteen days | **Not done.** Now 19. |

One done-but-unmerged, one went backwards, four open.

---

## 5. What I would do today

1. **Merge `BVA-I187`.** Rebase it onto `main` (it is 1 behind), run the pipeline, merge. The fix is written and verified correct — the only thing between it and a working send-money flow is a merge, and there are three days left.
2. **Then run one real transfer** and record the result. It would be the first money moved through the app and the only unambiguous evidence this sprint could produce.
3. **Triage the 14 review items into three piles today**: accepted, rejected-with-a-reason, and "was never actually built". §1.4 gives two concrete candidates for the third pile. Carrying 14 unexamined items into 08-02 guarantees the next sprint starts with the same problem.
4. **Confirm who `Fortune Okwu` is.** Two bulk operations on the review queue, ten editions unconfirmed. This identity is shaping the sprint's recorded state more than anyone else.
5. **`beevia-admin`, nineteen days.** Ninth edition.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: Zoho export (67 items, `--modified --activity`, cut-off 15:24 UTC) → fast-forward-only sync (all five already current; `beevia-mobile` switched from `Mock-data` to `main`) → deterministic API/spec audit (clean, no drift, no spec edits) → this report.

**Branch verification.** Because `main` did not move, the substantive check was of unmerged work: `git rev-list --count origin/main..<branch>` across every pushed branch in all five repos, then `git show <branch>:<path>` and `git grep <branch>` to read the step-up implementation directly. The §1.3 table is quoted from `api_url.dart`, `wallet_provider.dart`, `wallet_service.dart` and `mock/http/routes/wallet_routes.dart` on `origin/BVA-I187`. The API-side field name was confirmed from `auth.service.ts` (`{ stepUpToken }`) plus the snake-casing interceptor, and against the documented `step_up_token` in `openapi.yaml`.

**Window.** 24 Aug 14:55 UTC → 25 Aug 15:24 UTC. Per the 20 Aug correction, CSV header times are the exporting machine's local MDT; `actiontime` values are UTC. WAT (UTC+1) is inferred for the team, not stated in the data.

**Sources.** Board: `beevia-sprint-board-2026-08-25.csv` (67 rows, 43 leaves), `beevia-activity-2026-08-25.json`. Code: five repos at `origin/main`, no merges; all pushed branches enumerated. Specs: `openapi.yaml` (108), `openapi.proposed.yaml` (53), `openapi.admin.yaml` (29), `openapi.admin.proposed.yaml` (23) — validated, no drift.

### MVP readiness — ≈50% (estimate, unchanged)

**Target 2026-09-01 (provisional) · 7 days out.** No score moves: nothing merged to any `main`. Capability #7 stays at 0.65 — the fix that would lift it is written and verified but unmerged, exactly the leading-indicator situation the 18 Aug edition described for the client wiring. If `BVA-I187` merges, #7 moves next edition.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present; contact discovery scales to 25,000 |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; call screens present |
| 3 | Message translation | 7 | 0.7 | `POST /translate` live; provider integration and per-message endpoint BLOCKED; "v2" comment still unrecorded as a decision |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | KYC/upgrade endpoints + provider webhook live; full client onboarding; face verification fixed 20 Aug |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.65 | `GET /wallets` drives the balance, `/wallets/transactions` correct and called, transaction-history screen. Ceiling: server NGN-only, no wallet-summary route |
| 7 | Send / request / receive | 12 | 0.65 | Send wired end to end with a spec-correct body. Ceiling: **step-up token still absent from `main`, so it 401s** — the fix exists on `origin/BVA-I187`, unmerged (§1.3); request/receive have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only |
| 9 | Virtual cards | 10 | 0.0 | proposed only; BVA-I198 in review with no code; BVA-I208 now in progress |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | 0.45 | 29/52 admin ops; both admin repos 19 days silent, no branches |
| | **Weighted total** | **100** | | **50.3 → ≈50%** |

Weights frozen. Scores measure **merged, reachable build evidence** — never board status, items in review, or unmerged branches.

**Team performance — what these figures do not measure.** David wrote the fix and holds 5 review items; Ayomikun holds 9 and shipped nothing this window, having shipped all six commits in the last one. Neither is a productivity statement: work lands in bursts, and review items sitting against someone's name represent verification they are expected to perform, which is a different thing from their own outstanding work. `Fortune Okwu`'s six transitions are board administration, which the standing guidance says never to read as delivery. With 0/67 estimation points nothing here is normalised.

**What this report cannot tell you:**
- Why `BVA-I187` has not been merged — no PR state is visible to this pipeline (the `gh` CLI cannot resolve this org).
- Whether the step-up fix works against the real API; it is verified as correct by reading, not by running.
- Why BVA-I188 was marked ready for review 23 minutes before its fix was committed.
- Whether any of the 14 review items has an owner who intends to accept or reject it.
- Velocity or scope-fit for the last 3 days — still 0/67 estimated.
