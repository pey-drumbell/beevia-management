# Beevia — Project Status

**As of 2026-09-07** · Sprint **0901** (3 Sep → 22 Sep) — **day 5** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-07.csv` + `beevia-activity-2026-09-07.json` (64 items, sprint 08-01), a read-only scratch export of sprint 0901 (25 items), and all five repos inspected at both local `main` and `origin/main`.

Scope: both sprints, kept separate. Window 4 Sep 14:00 UTC → 7 Sep 14:00 UTC — a three-day window covering a weekend.

> ## ⛔ STOP — read §0 before doing anything else
>
> **`origin/main` of `beevia-api`, `beevia-admin-api` and `beevia-db-schema` was force-pushed on or before 7 September with malware appended to `eslint.config.mjs`.** Do not pull, do not run `npm install`, do not run lint, and do not let CI run on those branches until §0 has been worked through. Nothing was pulled onto this machine — the sync step's `--ff-only` rule refused the merge, which is the only reason this is a warning and not an incident report about local compromise.

---

## 0. Security incident — three repositories were force-pushed with a malicious payload

This is the finding. Everything else in this report is secondary to it, and the routine sections below are written on the assumption that §0 is being handled in parallel.

### 0.1 What was found

Today's sync step refused to fast-forward three repositories, reporting `diverged`. The usual cause is a local commit somebody forgot to push. Here `git reflog` on all three shows `forced-update` instead: **`origin/main` was rewritten upstream**, and the content difference between the last-known-good local `main` and the new `origin/main` is two files:

| File | Change |
|---|---|
| `eslint.config.mjs` | **~8.5 KB of obfuscated JavaScript appended to the last line**, after a long run of tab characters that pushes it off-screen in most editors |
| `.gitignore` | Three entries added: `branch_structure.json`, `temp_auto_push.bat`, `temp_interactive_push.bat` |

There is no other content change in `beevia-api` or `beevia-db-schema`. Their entire diff against the pre-rewrite tip is those two files.

### 0.2 What the payload does

Read statically — it was **not executed**, and nothing in this refresh ran `node`, `npm` or `eslint`:

1. **Resolves its command-and-control address from the Ethereum blockchain.** It hard-codes a wallet address, queries public Ethereum RPC endpoints and a Blockscout indexer for that wallet's most recent transaction, and decodes the transaction's `to` field into **two IPv4 addresses**. This is the "EtherHiding" technique: the C2 address is changed by sending a transaction, so there is no domain to seize and no fixed IP to block.
2. **Downloads a second stage over plain HTTP** from those addresses, XOR-decrypts it with a hard-coded key, and passes it to `eval`.
3. **Spawns detached `node -e` child processes** (`detached: true`, `stdio: 'ignore'`, `windowsHide: true`) so the payload keeps running after the parent exits, and is invisible in a console window.
4. **Carries a campaign identifier** (`global.i = 'A8-4893-2'`), which is how this family tracks victims.

The three `.gitignore` additions are consistent with the same actor: `temp_auto_push.bat` and `temp_interactive_push.bat` are Windows batch files for automated `git push`, and `branch_structure.json` is a repository map. Adding them to `.gitignore` stops the tooling's own artifacts from showing up in `git status` on the machine it is running on.

**The trigger is any invocation of ESLint.** `npm run lint`, a pre-commit hook, an editor's ESLint integration, or a CI lint job all load `eslint.config.mjs` and execute it as a module. Note that the config's own first line is `globalIgnores(['eslint.config.mjs'])` — the file exempts itself from linting, so no lint run will ever report it.

### 0.3 Scope — what is and is not affected

| Repo | Local worktree | `origin/main` | Notes |
|---|---|---|---|
| `beevia-api` | ✅ clean | ⛔ **compromised** | Payload in the tip merge commit only; both its parents are clean |
| `beevia-admin-api` | ✅ clean | ⛔ **compromised** | **Both** parents of the tip carry it — including the 6 Sep dashboard commit |
| `beevia-db-schema` | ✅ clean | ⛔ **compromised** | Payload in the tip, committed as `github-actions[bot]` — the release bot's identity |
| `beevia-admin` | ✅ clean | ✅ clean | Fast-forwarded 6 commits today; scanned, no markers |
| `beevia-mobile` | ✅ clean | ✅ clean | No commits since 26 Aug |

Two details that matter for how this is triaged:

- **The payload sits at the tip, and the history behind it is clean.** Sampling `eslint.config.mjs` down `origin/main` at six depths back to `project init` finds it only in the tip commit; everything before the rewrite point is intact in all three repos. So this is a tip injection carried in on a force-push rather than a wholesale history rewrite, which makes recovery much simpler than it first appeared.
- **In `beevia-api` it rides an "evil merge".** The tip `babb236` is a merge commit whose content differs from both of its parents, which is why `git log -S` finds no commit that introduces the string. A reviewer looking at the PR diff would see nothing; the payload exists only in the merge result.

### 0.4 The part that says this is live, not historical

**In `beevia-admin-api`, the payload is in the 6 September dashboard commit** (`09fda4f`, authored `Phoenixdadhev`, 13:31 −0700 — Sunday), not only in the rewritten merge. That commit is genuine work: it is a well-built dashboard summary endpoint, and §4 documents it.

It carries the payload because **it was authored on a machine whose working copy already contained the malicious `eslint.config.mjs`**. That is a materially different situation from a one-off force-push against the remote:

- At least one developer workstation has the file on disk today, and has almost certainly executed it — anyone working in a NestJS repo runs lint.
- Legitimate work is now being committed on top of poisoned trees, so the payload will keep re-appearing in new commits until that workstation is cleaned. Reverting the remote alone will not hold.
- Whatever credentials that machine holds should be assumed captured: GitHub tokens, npm tokens, `.env` files for both API services, Anchor and Paystack keys, database URLs.

### 0.5 What I did not do

Per this pipeline's guardrails, the sync step is limited to fast-forwarding, and it is the only sanctioned write to the service repos. **No repository was reset, rebased, reverted or cleaned**, and no attempt was made to "fix" the branches. Recovery here needs decisions this report cannot make — chiefly whether to force-push a corrected history or revert forward, and in what order relative to rotating credentials.

Nothing was pulled, and no Node tooling ran in any sub-repo during this refresh.

### 0.6 What needs to happen, in order

1. **Rotate every credential** that the affected workstation or CI could reach: GitHub personal access tokens and deploy keys, npm publish tokens for `@drumbell-technologies/beevia-db-schema`, and the Anchor, Paystack, Entrust and database credentials for both API services. Do this first — it is the only step that gets less effective with delay.
2. **Take the developer workstation offline and image it** before cleaning. The `.bat` filenames say Windows; check for persistence and for the spawned detached `node` processes.
3. **Freeze CI on the three repos.** A lint job on a compromised branch executes the payload with whatever secrets that runner holds.
4. **Audit the GitHub org** — force-push was possible on `main`, so branch protection is either absent or was bypassed with a stolen token. Check the audit log for when the force-push happened and from which token, and check for new deploy keys, new collaborators, changed webhooks and modified Actions workflows.
5. **Rebuild the three branches from the last clean commit.** The pre-rewrite tips still exist in the local clones here (`d9af17b`, `43abc3a`, `5b0592a`) and their history is clean, which makes this tractable. The one piece of genuine work that must be carried across is `09fda4f`, the dashboard endpoint — re-apply it with `eslint.config.mjs` reverted.
6. **Turn on branch protection with force-push disabled** on all five repos, and require signed commits if the org plan allows it.
7. **Then** re-run this refresh, so the audit sees real code again.

### 0.7 Why no audit would have caught this either

For the second cycle running, the most serious finding is invisible to the automation. The 4 September edition made this point about behaviour drift; this is a sharper version of it. **The compromise touches no route, no DTO, no schema and no spec.** `eslint.config.mjs` is not application code and is not in any inventory this pipeline maintains. Today's audit ran clean on the consumer API and would have run clean on all three repos had the sync succeeded.

What *did* catch it was the sync script's `--ff-only` rule — a guardrail written to avoid making merge commits in repos this pipeline is only supposed to read. It refused the merge, printed `diverged`, and that refusal is the entire reason the payload is not on this machine and in this report's own workspace. **The safety property that mattered was one written for an unrelated reason**, which is worth remembering the next time a guardrail looks like friction.

`suggestions.md` gains §7 with the durable version of this.

---

## Quick overview

> **Three of the five repositories have malware on `origin/main`, and it is still spreading — the newest legitimate commit, Sunday's dashboard endpoint, carries the payload because it was written on an already-infected machine. Set against that: the two workstreams this report has spent a fortnight calling blocked both moved. Promise Udo wired four dashboard modules to the live API on Friday afternoon — hours after the endpoints shipped, and 99 minutes after Friday's report went out saying nobody had told him — and sprint 0901 finally started. Friday's edition was wrong about the dashboard, and §0.8 corrects it.**

| | 4 Sep | 7 Sep | Δ |
|---|---:|---:|---:|
| Repos with a compromised `origin/main` | 0 | **3** | **+3** |
| Sprint 0901 leaves in To do | 17 | **14** | **−3** |
| Sprint 0901 leaves In progress | 0 | **3** | **+3** |
| Sprint 0901 board transitions | 0 | 11 | +11 |
| Estimation points set (0901) | 0 / 25 | **0 / 25** | 0 |
| Sprint 08-01 (closed) | 41 leaves, all Done | unchanged | 0 |
| API surface (consumer / admin) | 131 / 34 | **131 / 35** | 0 / **+1** |
| Admin spec modules with something built | 5 of 8 | **5 of 8** | 0 |
| `beevia-admin` modules on the live API | 1 of 9 | **5 of 10** | **+4** |
| `beevia-admin` modules still `MOCK` | 4 | **2** | **−2** |
| MVP readiness (estimate) | ≈55% | **≈56%** | +1 |

**Team, at a glance:**

| Person | Owns | 0901 leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---:|---:|---:|---|---:|---|
| Ayomikun Araoye | backend + admin API | 9, all To do | 4 | 3.0 d | — | 15 | **His workstation is the likely infection source** (§0.4). Untouched 0901 leaves for a 4th day |
| David Samuel | mobile | 6 — **2 In progress** | 3 | 2.6 d | 2, age 3 d | **0 to `main`** | `beevia-mobile` `main` untouched **12 days**; `BVA-I192` still 12 commits unmerged, item Done |
| Philip Chidera | design | 2 — **1 In progress** | 2 | 0.9 d | 1, age 3 d | — | Started 0901 and moved three of David's items into it |
| Promise Udo | admin dashboard | **0** | — | — | — | **6** | **Wired 4 modules to the live API** (§5). 18th edition with no board row |

Flow figures are carried forward from 3 September: the only board movement in this window was 11 status transitions on Friday afternoon, none of them into REVIEW/QA, so no new cycle time or submission has been measured. **Commit counts are for the trailing 7 days and include commits on compromised branches** — the work is real even where the branch is not trustworthy.

**The two questions for standup:** (1) **Who has admin on the GitHub org, and when did the force-push happen?** That is the fastest route to how the token was obtained and what else it touched (§0.6). (2) **Whose machine wrote `09fda4f` on Sunday?** That workstation still has the payload on it, and until it is cleaned every new commit re-infects the branch (§0.4).

**The three things worth knowing:**

1. **Three repositories were force-pushed with a blockchain-addressed malware loader, and the infection is on at least one developer machine, not just the remote** (§0). Nothing reached this workspace, because the sync step refuses non-fast-forward merges. The payload runs on any `eslint` invocation — including CI — so freezing CI and rotating credentials are the first two moves.
2. **The admin dashboard is not blocked and was never as far behind as this report said.** Promise Udo's Friday commit deleted the transactions and wallet mock data outright and pointed transactions, wallet, reconciliation and the activity feed at the real endpoints — the same endpoints that had shipped that morning. Mock modules drop from four to two. Friday's report said "the API is ahead of the dashboard, and nobody has told the dashboard" and recommended telling him; he had already done the work 99 minutes after that report's cut-off (§0.8).
3. **Sprint 0901 started, then stopped.** Three leaves moved to In progress on Friday afternoon, all of them by Philip — including two assigned to David. Since then: nothing across Saturday, Sunday and Monday morning. Still **0 of 25 items estimated**, fourth consecutive edition asking. The one commit in the window was Sunday's dashboard endpoint, which is not on the sprint.

**If you read nothing else:** stop CI and rotate credentials on the three backend repos today; the dashboard workstream is healthier than the last three reports claimed and this one apologises for that; and sprint 0901 has moved 3 of 17 leaves in 5 days with no estimates.

---

## 0.8 Corrections

### Correction 1 — to 4 September's reading of the admin dashboard

**Claim (2026-09-04, §5): "the API is ahead of the dashboard, and nobody has told the dashboard."** Restated in §7 risk 9 ("The admin dashboard is now behind its own API… with no channel to communicate the change") and in §9 recommendation 4 ("Tell Promise the two endpoints he was blocked on exist… Four days of silence in `beevia-admin` while its blockers cleared is the most avoidable thing in this report").

**All of that was already false when it was written.** Commit `6448b59` in `beevia-admin`, at 16:39 BST on 4 September — **15:39 UTC, 99 minutes after that report's 14:00 UTC cut-off** — wired `transactions`, `wallet`, `reconciliation` and the dashboard activity feed to the live API in one pass, deleting `transactions/mock-data.ts` and `wallet/mock-data.ts` entirely. The reconciliation and transaction endpoints had merged that same morning. The gap between endpoint and client was hours, not days.

Worse, the error was structural rather than unlucky. The report inferred a communication failure from **repository silence** — "no commits for four days, therefore he does not know" — which is the same class of mistake as inferring build state from board state, and this pipeline has now made it in three directions in four days: a Done column that overstated delivery, a withdrawal that understated it, and now a quiet repo read as an uninformed developer. **A quiet repository means nothing has been pushed. It does not mean nothing is known and it does not mean nothing is happening.**

There is a fix available and it is cheap: the cut-off is 14:00 UTC, which is early afternoon in Lagos and mid-morning in the US. Work committed in a normal European or African afternoon lands after it and reads as a silent day. **Three of the last four editions have reported a "silence" that a later cut-off would have shown as activity.** §9 item 6 proposes moving it.

### Correction 2 — the audit's admin drift line is an artifact, not drift

Today's audit closes with **`beevia-admin-api code=34 spec=35 — documented, not in code: GET /admin/dashboard`**. That is not real drift. The endpoint exists on `origin/main`; it is absent from the *working tree* because the fast-forward was refused (§0), so the audit read Thursday's code against today's spec. The spec is right and the audit is right about what it can see. It will resolve itself when §0.6 step 7 re-runs. Flagged here so the next reader does not "fix" the spec by deleting a real operation.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State

| Status | Leaves | Share | Δ vs 4 Sep |
|---|---:|---:|---:|
| To do | **14** | 82% | **−3** |
| **In progress** | **3** | **18%** | **+3** |
| Review / QA | 0 | 0% | 0 |
| Done | 0 | 0% | 0 |

25 board rows = 17 leaves + 8 parent stories. Window 3 Sep → 22 Sep (19 days); **5 elapsed, 14 remaining.**

**All movement happened in one 97-minute burst on Friday afternoon**, after the last report's cut-off. The activity sidecar records 11 transitions and then nothing at all across Saturday, Sunday and Monday morning:

| Time (UTC) | Item | Moved by | Transition |
|---|---|---|---|
| 4 Sep 14:23 | `BVA-I234`, `I235`, `I236` | Philip Chidera | To do → In progress → **back to To do**, same minute |
| 4 Sep 15:57 | `BVA-I239`, `I240`, `I241` | Philip Chidera | To do → In progress |
| 4 Sep 16:00 | `BVA-I232`, `I233` | David Samuel | To do → In progress |

The 14:23 block is board hygiene, not work — three items moved and reverted inside the same minute. The real change is the five at 15:57 and 16:00, of which three are still In progress today (`BVA-I233` *Build Both Screens* and `BVA-I241` *Build the Toggle*, both David's; `BVA-I240` *Caption, Icon & Toggle States*, Philip's).

**Philip moved two of David's items.** `BVA-I239`/`I240`/`I241` were transitioned by Philip, and `I241` is assigned to David. Per this report's standing method, per-person figures key to the assignee rather than to whoever clicked — but it is worth knowing that the sprint's start was driven by one person updating the board, not by three people picking up work.

### 1.2 Three days, no movement, and a weekend in the middle

Two of the three intervening days were a weekend, which is the honest read and should be said before anything else. Against that:

- **Monday morning has produced nothing** on the board as of the 14:00 UTC cut-off.
- **Nothing has reached REVIEW/QA on either sprint since 28 August** — ten days. The throughput signal remains entirely blind (§6.1).
- The only commit in the window is Sunday's dashboard endpoint, which belongs to no sprint item.

### 1.3 Still no estimates — fourth consecutive edition

**0 of 25 items carry estimation points.** Asked on 3, 4 and now 7 September. Five of nineteen days are spent. §1.4's finding from Friday still stands unexamined: seven of the nine backend notification stories describe already-merged code, so the sprint is probably smaller than its story count, and there is no estimate anywhere to test that against.

### 1.4 The foundation is still a stub

`POST /translate` still returns its input unchanged — `TranslateModule` binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`, and `beevia-api` has had no commit at all since 4 September, so nothing has changed. The sprint asks the client to integrate a translation engine and render per-message auto-translations on top of it. **There is still no board item for connecting a provider**, and still no statement of whether the engine is meant to be server-side or on-device. Third edition asking.

---

## 2. What shipped this cycle

**One commit of application code**, in `beevia-admin-api`, on Sunday. The consumer API stays at 131 operations; **the admin API goes 34 → 35.** Six `beevia-admin` commits were pulled today, four of them predating this window (§5 covers the dashboard workstream, which is where the substantive movement is).

### 2.1 `beevia-admin-api` — `GET /admin/dashboard`

One endpoint backing the whole console landing screen: user counts (total, active, new today / 7 d / 30 d, split by onboarding path and account status), the KYC review queue, transaction counts and volume for today and the last 7 days plus volume by ledger type over 30 days, pending payouts, treasury solvency, and admin-account counts. Gated `dashboard:view` behind both guards.

The construction is right for what it is. A handful of parallel `COUNT`/`SUM` queries in a single `Promise.all`, no schema change and no new table; the treasury tile **reuses `ReconciliationService.reconcilePool()`** rather than reimplementing solvency, so there is exactly one definition of "solvent" in the service. `dashboard` was already a value in `adminModuleEnum`, so the permission is seedable without a migration — a small thing that is usually got wrong.

Three things to note, none a defect:

1. **It inherits Friday's `solvent` trap and puts it on the landing screen.** `treasury.solvent` is `false` whenever the pool is unconfigured, which means *unknown*. Friday's report flagged this as something "a dashboard binding a red/green badge to `solvent`" would get wrong; that dashboard now exists in spec form. The payload does expose `configured` alongside, so the client *can* tell the difference — the risk is entirely that the naming does not steer anyone to check it.
2. **"Volume" is gross value moved, not net position.** It sums the ledger's credit legs. Correct for a dashboard tile, wrong for a balance sheet, and nothing in the field name says which.
3. **Nothing is cached** — every call recomputes, and the 30-day group-by is the query that will need an index first.

One stale comment for whoever builds the tile: `dashboard.types.ts` documents `configured` as "null when `ANCHOR_POOL_ACCOUNT_ID` is unset", but the field is a `boolean` set from `pool.status !== 'not_configured'`. The comment describes `pool_balance_ngn`. The implementation is correct.

### 2.2 It is on a compromised branch

`09fda4f` is legitimate work and this report documents it as shipped, because it is merged to `origin/main` and the endpoint is real. It also **carries the malicious `eslint.config.mjs`** (§0.4). Those are both true and neither cancels the other: the dashboard endpoint will survive the cleanup, the config file must not, and the commit will need re-applying on a clean base (§0.6 step 5).

### 2.3 Repo staleness

| Repo | Last commit to `origin/main` | Days silent | Δ |
|---|---|---:|---:|
| `beevia-admin-api` | **6 Sep** | **1** | −1 |
| `beevia-admin` | 4 Sep | 3 | −1 |
| `beevia-api` | 4 Sep | 3 | +3 |
| `beevia-db-schema` | 1 Sep | 6 | +3 |
| `beevia-mobile` | 26 Aug | **12** | +3 |

`beevia-mobile` has now had no commit to `main` for twelve days while `origin/BVA-I192` sits **12 commits ahead**, unchanged since 2 September, with its board item marked Done. Nine dependabot branches, `Deps-updates-2026-08-20` and `self-hosted-runners` also remain. Unmerged work is not scored.

---

## 3. Sprint 08-01 — closed and frozen

Unchanged: 64 rows = 41 leaves + 23 parent stories, all 41 leaves Done, no activity since the closing sweep of 3 September. The audit's period-over-period section confirms it — **no net status change, 0 items left review, 0 newly Done, 0 entered.**

**The export still targets this closed sprint.** `ZOHO_SPRINT_FILTER` in `.env` remains `08-01`, so today's in-repo export is 64 rows of frozen data and the audit again reports "sprint ends 2026-08-28 (−10d left)". Sprint 0901 reaches this report only through a read-only scratch export written outside the repository. Friday's edition called itself "the last edition for which that workaround is appropriate"; this is the second. §9 item 5 explains why the cutover was not done today and what it needs.

---

## 4. Spec updates made this cycle

The audit opened at 131/131 consumer and 34/34 admin, and all four specs valid. The admin API is nevertheless **35 operations** as of Sunday; the audit could not see the new one because the fast-forward was refused (§0.8, Correction 2).

### 4.1 `openapi.admin.yaml` — one operation added

`GET /admin/dashboard` is documented from its controller, service, types file and the response interceptor, in wire shape rather than handler shape — `ResponseInterceptor` wraps every payload as `data` and snake_cases keys recursively, so the spec carries `generated_at`, `new_this_week`, `by_path`, `volume_ngn`, `by_type_this_month`, `pending_amount_ngn`, `ledger_liability_ngn` and `pool_balance_ngn`. New schemas: `DashboardSummary` and `DashboardTxnWindow`. A `Dashboard` tag joins the tag list.

Two contract facts are written into the operation description rather than left implicit, both because a client will otherwise get them wrong: that `by_type_this_month` is an **open map** keyed by ledger type — new types appear as new keys, so a client must not exhaustively switch on them — and that `solvent: false` with `configured: false` means *unknown*.

**Nothing was retired from `openapi.admin.proposed.yaml`.** It stays at 21. The proposed analytics operations (signups over time, onboarding funnel, Chat-Only vs Chat+Banking split) are time-series queries; this is a point-in-time summary and does not supersede any of them.

`admin-api-rfc.md` gains **§3.11** for the implemented contract, its header count and §1 move to 35 operations and eight controllers, and the Module 7 coverage row moves from "the activity feed only" (1 op) to activity feed + landing summary (2 ops).

### 4.2 No consumer-API change

`beevia-api` has had no commit since 4 September. `openapi.yaml` stays at 131 operations, `openapi.proposed.yaml` at 42, and neither needed an edit.

### 4.3 Spec health

All four files validate: no `x-beevia-*`, no broken `$ref`s, no duplicate or missing `operationId`s, no orphaned components. The only non-clean line is the code-vs-spec count for the admin API, which is the stale-worktree artifact explained above.

---

## 5. Admin dashboard — the workstream this report has been wrong about

### 5.1 The board

The second Zoho project, *Beevia Admin Dashboard* (`187554000000127002`), **still has no sprints**; step 1b returned exit 3 again, for the **seventeenth consecutive edition**. Promise Udo's row is still sourced from commits.

### 5.2 The code, which is a different story

Six commits pulled today, spanning 31 August to 4 September, and one of them changes the picture this report has been painting for a fortnight. **`6448b59`, "transactions list update", 4 September 16:39 BST** — 37 files, +1,937/−1,095:

| Module | Before | After |
|---|---|---|
| `transactions` | `MOCK IMPLEMENTATION` | **Live** — `GET /admin/transactions`; `mock-data.ts` **deleted** (140 lines) |
| `wallet` | `MOCK IMPLEMENTATION` | **Live**; `mock-data.ts` and its test **deleted** (238 lines) |
| `reconciliation` | `MOCK IMPLEMENTATION` | **Live** — `/admin/reconciliation/pool` and `/admin/reconciliation/users/{id}` |
| `dashboard` | activity feed | **Live** — `GET /admin/activity` |
| `reports` | — | **new module**, mock-backed |

All four go through `liveClient` with no mock fallback path. `MOCK IMPLEMENTATION` markers across `src/features` drop from **four to two** — only `reports` (new) and `pending-transfers` remain — and the feature module count goes 9 → 10.

The endpoints it consumes had merged **that same morning**. This is the fastest endpoint-to-client turnaround this project has produced, and three consecutive editions of this report described it as a blocked, uninformed workstream (§0.8).

**It also independently hit the gap the RFC predicted.** `admin-api-rfc.md` §6.3 warned that the shipped transaction statement lost the proposed `direction`/`from`/`to` filters. Promise's `transactions/api.ts` sends `user`, `types`, `statuses`, `dateFrom`, `dateTo` anyway, with a comment stating plainly that only `page` and `limit` are confirmed, that the rest follow the codebase's existing convention, that unrecognised params mean results stop narrowing but pagination stays correct, and to "revisit once the backend documents its actual filter params". That is the right engineering call and it is documented at the call site — but it is also **two people solving the same problem from opposite ends without talking**, and the cost is a filter UI that may silently not filter.

### 5.3 Pipeline note

Unchanged: the two boards are never summed; admin exports would land in `sprint-board-exports/admin/` because `beevia-audit` globs the main folder non-recursively; when the admin board gets a sprint its name will not match `ZOHO_SPRINT_FILTER`, so step 1b keeps skipping until `--sprint` is passed.

---

## 6. Team performance — detail

All figures come from the activity sidecar and git, never from `Last Modified`. **No item reached REVIEW/QA on either sprint in this window**, so submission and cycle-time figures are carried forward from 3 September; only commit counts, WIP and staleness are new.

**Ayomikun Araoye — backend + admin API.** 15 commits in the trailing 7 days across `beevia-api` (2 in window, 14 in the trailing week), `beevia-admin-api` and `beevia-db-schema`, summing the `Ayomikun Araoye` and `Phoenixdadhev` identities and excluding bots — down from 41 on Friday, which reflects Friday's exceptional day dropping out of a window that now includes a weekend. His one commit in this window is Sunday's dashboard endpoint (§2.1). He still owns 9 of sprint 0901's 17 leaves and has touched none of them for a fourth day, and §1.4's finding that seven of them describe merged code is still unconfirmed with him. **Separately and more urgently: `09fda4f` carries the malware payload, which makes his workstation the most likely infection source** (§0.4). That is a security finding about a machine, not about a person or their work — the commit itself is clean, well-structured code.

**David Samuel — mobile.** Three genuine submissions in the trailing 7 days, last on 28 August; median cycle 2.6 d over 14 passes. **Zero commits to `main` in 7 days** — `beevia-mobile` `main` static for **12 days** — and nothing new on `origin/BVA-I192`, still 12 commits ahead with its board item Done. He now has **2 leaves In progress** (`BVA-I232`, `BVA-I233`), started Friday 16:00, age 3 days against a 2.6-day median, so they are at the edge of where his own history says they should have moved. Twelve days without a merge to `main` and a finished-but-unmerged branch is the pattern worth a question.

**Philip Chidera — design.** Two genuine submissions in 7 days; median cycle 0.9 d over 7 passes. One leaf In progress (`BVA-I240`), age 3 days against a 0.9-day median — the most overdue WIP on the board relative to its owner's own pace. He drove all 9 of Friday's board transitions including three on items he does not own, which is board administration as much as design work and is not separable in this data.

**Promise Udo — admin dashboard.** No board presence, eighteenth consecutive edition. **6 commits in the trailing 7 days** and the single largest client-side change this project has seen (§5.2). His workstream is now the one with the cleanest endpoint-to-client story, and this report has misread it three editions running.

### 6.1 Weekly submission trend

First-ever genuine submissions into REVIEW/QA, by ISO week: **W34 (17–23 Aug) — 17 · W35 (24–30 Aug) — 10 · W36 (31 Aug – 6 Sep) — 1 · W37 (7 Sep) — 0.**

No submission has been made on either board since 28 August — **ten days**. The closed sprint cannot produce more transitions and the open sprint has produced none beyond starts. The throughput signal has now been blind for two consecutive editions.

### 6.2 Cycle times

Unchanged from 3 September; no new passes measured. Method: one measurement per pass, from an item's most recent entry into `In progress` to the next time it reaches `REVIEW/QA`.

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

Every distribution is bimodal — same-day board hygiene at one end, multi-day builds at the other.

### 6.3 What these figures do not measure

- **They do not see the largest change in this window.** Promise's four-module wiring is 37 files and shows up in exactly one column, "commits", because his workstream has no board.
- **They do not see branches.** `beevia-mobile` reads zero while twelve commits sit on `origin/BVA-I192`. Every "commits" figure means *merged to the default branch*.
- **They now include commits on compromised branches.** The work is real; the branch is not trustworthy. No figure here is adjusted for that.
- **No estimation points exist on any item, either sprint** — 0/64 and 0/25. Nothing is normalised for size.
- **Board actions are not evenly attributable.** Figures key to the item's assignee, not to whoever clicked — and this window is a clear case, with one person making 9 of 11 transitions.
- **A weekend sits in the middle of a three-day window.** Every "days silent" figure here is inflated relative to working days.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **Review and triage work is invisible**, and there was again none to record: PR #5 was authored and merged by the same person.
- **Absence of board data is not absence of work** — and absence of *commits* is not absence of knowledge, which is this edition's correction (§0.8).
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction.

---

## 7. Risks

1. **Three repositories have a malware loader on `origin/main`, and at least one developer workstation is infected** (§0). Credentials for both API services, the database, Anchor, Paystack and npm publishing should be treated as captured until rotated.
2. **CI on those three repos will execute the payload** on any lint job (§0.2). It should be frozen before anything else is merged.
3. **`main` was force-pushable**, so branch protection is absent or was bypassed with a stolen token (§0.6 item 4).
4. **New legitimate work is re-infecting the branches** (§0.4). The workstation has to be cleaned before any remote fix can survive the next push.
5. **Sprint 0901 has moved 3 of 17 leaves in 5 days** and has no estimates (§1.1, §1.3).
6. **Sprint 0901's foundation is still a stub and still not on the board** (§1.4).
7. **Nothing has entered REVIEW/QA for ten days** on either board (§6.1) — the throughput signal is blind for the second consecutive edition.
8. **The dashboard's transaction filter UI may silently not filter** (§5.2) — the client sends filter params the backend never documented.
9. **The per-user reconciliation balance check will report false discrepancies for every user the moment the treasury pool is enabled** (§2.1 of 4 Sep). Unchanged; `ANCHOR_POOL_ACCOUNT_ID` is still unset, so there is still time.
10. **`treasury.solvent` is now on the landing screen** and reads `false` for "unknown" (§2.1).
11. **The money-oversight surface still has no second reviewer** — PR #5 was self-merged like the four before it.
12. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows; exceeding the caps produces wrong output, not visible truncation.
13. **The Anchor webhook backfill is still unscoped** — 67 days of dropped events, unmeasured, six days after the fix.
14. **A finished mobile payout feature has been unmerged for ten days** with its board item closed (§2.3).
15. **The daily export still targets a closed sprint** (§3), for the second consecutive edition.
16. **The report's 14:00 UTC cut-off is producing false "silence" findings** (§0.8) — three of the last four editions.
17. **The same silent-200 is still live on `POST /kyc/profile`** — fifth consecutive edition; a five-line guard already written on the other ladder.
18. **A hard-coded account number still reaches a money screen on `main`** — fifth consecutive edition, under a Done item.

---

## 8. Previous recommendations — where they stand

| Recommendation from 4 Sep | Status on 7 Sep |
|---|---|
| Decide whether sprint 0901 is running | **Partly.** Five leaves were started on Friday afternoon, three still In progress. No decision was recorded, and nothing has moved since (§1.1). |
| Scope the Anchor webhook backfill | **Not done.** No reconciliation run, no commit, no board item. |
| Fix the per-user balance check before enabling the pool | **Not done.** `reconciliation.service.ts` unchanged; the pool is still unconfigured, so the window is still open. |
| Tell Promise the two endpoints he were blocked on exist | **Was never needed.** He wired four modules to them 99 minutes after that report's cut-off (§0.8, §5.2). |
| Move the daily export to sprint 0901 | **Not done**, deliberately — see §9 item 5. |
| Add the "webhook received, no handler matched" alert | **Not done.** No `beevia-api` commit since 4 Sep. |
| Put estimation points on 0901 | **Not done.** 0/25, fourth edition asking. |
| Get a second pair of eyes on the money-oversight code | **Not done**, and PR #5 was self-merged the same way. |
| Apply the BVN-ordering guard to `POST /kyc/profile` | **Not done.** Re-checked; unchanged. |

One of nine resolved, and it was resolved before it was recommended.

---

## 9. What I would do this week

1. **Work §0.6 in order, today.** Rotate credentials, image the infected workstation, freeze CI, audit the GitHub org, then rebuild the three branches from the clean tips this workspace still holds. Items 2–4 of §7 all collapse into this one.
2. **Turn on branch protection with force-push disabled** on all five repositories. This is a five-minute settings change and it is the control whose absence made §0 possible at scale.
3. **Decide the sprint 0901 question properly** — it was asked on Friday, five leaves moved that afternoon, and no decision was recorded. Nine of seventeen leaves belong to someone who has not touched them in four days, and §1.4 says seven of them may already be built. Either re-scope it against what is actually being built, or state that the money and oversight surfaces are the priority and 0901 waits.
4. **Confirm the filter contract for `GET /admin/transactions`** (§5.2). The client already sends five filter params the endpoint never documented; either implement them or tell the dashboard to drop the UI. This is one message between two people who demonstrably ship fast when they are pointed at the same thing.
5. **Move the daily export to sprint 0901.** Not done today on purpose: it means relocating eleven tracked CSVs and sidecars into `sprint-board-exports/08-01/` and changing `ZOHO_SPRINT_FILTER`, which would put a large unrelated file move in the working tree in the same session as a live security incident. It should be its own change, on a normal day, and it is now blocking honest reporting on the active sprint for a second edition.
6. **Move the report cut-off from 14:00 UTC to ~20:00 UTC** (§0.8). Three of the last four editions have reported a "silence" that a later cut-off would have shown as delivery, and each one cost a correction in the next edition. This is a one-line change to when the refresh runs.
7. **Put estimation points on 0901, or state that this project does not estimate.** Fourth consecutive edition asking. Either answer is workable; asking daily and getting silence is not.
8. **Scope the Anchor webhook backfill** (§7 item 13). The reconciliation endpoint that can measure it has now been live for three days and is wired into the dashboard. Running it across the active users turns an unbounded worry into a number.
9. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Unchanged from the last five editions; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:00 UTC) → admin board (exit 3, no sprints, 17th edition) → fast-forward sync (**6 commits pulled into `beevia-admin`; 3 repos refused as `diverged`, which is §0**) → static inspection of the diverged branches, read-only, via `git show`/`git grep` against `origin/main` → deterministic audit (exit 0 on what it could see) → manual contract review of `09fda4f` from `origin/main` → spec update → re-audit → read-only scratch export of sprint 0901 → this report.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran during this refresh. The three compromised branches were read with `git show` and `git grep` only, and no repository was reset, rebased, reverted or cleaned (§0.5).

**Sprint 0901 was exported to `/tmp/beevia-scratch/`, outside the repository**, for the third consecutive edition and for the same reason: `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest files as snapshots of one board, so a second CSV covering a different sprint would make tomorrow's delta compare 08-01 against 0901 and report invented movement. No file for it was written into the workspace. §9 item 5 explains why the cutover was deferred again.

**Degraded inputs.**
- **Three repositories could not be synced** (§0) — `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are diverged by upstream force-push. Their *working trees* are Thursday's code. Every code claim about them in this report was made against `origin/main` read directly, not against the working tree; the audit script, which reads working trees, was not.
- **The `Epic` column is blank** across the board — the OAuth refresh token lacks `ZohoSprints.epic.READ`. Known scope gap, not "no epic assigned".
- **`Comments` bodies are unavailable** from the API.
- **The admin board produced no export** because the project has no sprints (expected, exit 3, not a failure).
- **`ZOHO_SPRINT_FILTER` is stale** — still `08-01`, so the in-repo export covers a sprint that closed on 28 August.
- **The window contains a weekend**, which inflates every staleness figure relative to working days.

**Window.** 4 Sep 14:00 UTC → 7 Sep 14:00 UTC. All `actiontime` values and every board time quoted are UTC; git timestamps are as recorded and converted where compared against board times. Note that the force-push rewrote committer timezones on the three affected repos, so their commit dates shifted by an hour without the underlying instant changing — commit *ordering* is unaffected and no figure here depends on the shift.

**Sources.** Board: `beevia-sprint-board-2026-09-07.csv` (64 rows, 41 leaves, sprint 08-01), `beevia-activity-2026-09-07.json`. Active sprint: scratch export of `0901` (25 rows, 17 leaves) with its own activity sidecar. Admin board: none. Code: `beevia-admin` and `beevia-mobile` at `origin/main` in the working tree; `beevia-api`, `beevia-admin-api` and `beevia-db-schema` read from `origin/main` refs without checkout. Specs: `openapi.yaml` (131), `openapi.proposed.yaml` (42), `openapi.admin.yaml` (**35**), `openapi.admin.proposed.yaml` (21) — all validated, no markers, no broken refs, no orphaned components.

**A note on who appears here.** Only people whose work is tracked have rows. Board transitions performed by non-contributors are reported without attribution, per the standing instruction.

<a id="mvp-method"></a>

### MVP readiness — ≈56% (estimate; 55.97, from 55.37)

**Target 2026-09-01 (provisional) · the target date passed six days ago.** On merged build evidence the product is roughly 56% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. Unchanged |
| 2 | Voice & video calling | 8 | 0.8 | 4 call endpoints live; `audio_call_screen` / `video_call_screen` present; incoming-call push wired. Unchanged |
| 3 | Message translation | 7 | 0.15 | Unchanged. `TranslateModule` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`; no commit to `beevia-api` since 4 Sep. A translation sprint is open and still contains nothing that addresses this |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged. KYC/upgrade endpoints + provider webhook live; full onboarding flow wired in the client. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged; no consumer-API commit in the window. Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` unset), so still not scored. Bank payout still unmerged on `origin/BVA-I192`. Ceiling unchanged: server is NGN-only |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. P2P send wired end to end. Ceiling: request/receive still have no client flow |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only; `PaymentService.activeNgn()` still present |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. Card lifecycle events processed since 3 Sep. Ceiling still low: the client has **zero** `/cards` references and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | no endpoint or record anywhere |
| 11 | Admin oversight | 6 | **0.72** ↑ | **+0.10, and the movement is on the client side for the first time.** Admin API 34 → 35 (`GET /admin/dashboard`, §2.1), so 5 of 8 spec modules have something behind them and Module 7 now has two operations. The larger change is the dashboard: `beevia-admin` goes from **1 of 9** feature modules on the live API to **5 of 10** — transactions, wallet, reconciliation and the activity feed all wired through `liveClient` with the mock data files deleted outright, not left as fallbacks (§5.2). Mock modules drop 4 → 2. Ceiling: `reports` and `pending-transfers` are still mock, Modules 4, 6 and 8 have no endpoints at all, and the transaction filter contract is unconfirmed |
| | **Weighted total** | **100** | | **55.97 → ≈56%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, never merged-but-disabled code.

**On the single movement.** Capability 11 is the only line that changed, and it moved for a reason this rubric is designed to catch and this report's prose had been missing: a client stopped being a mock and started calling a real API. The endpoint half of admin oversight has been running ahead of the dashboard half for weeks; that gap closed substantially on Friday, and it closed without anyone reporting it.

**The security incident does not change any score, and that is deliberate.** The rubric measures how much of the PRD's MVP has been built. A compromised branch does not un-build an endpoint. What it does is put the *trustworthiness* of every artifact in doubt, and that belongs in the risk register — where it sits as risks 1–4. If the cleanup ends up discarding merged work, that will show up as a score movement in a later edition, honestly, as a reduction.

**What this report cannot tell you:**
- **How long the three repositories have been compromised, or what the payload did.** The force-push was observed today; the GitHub audit log will date it, and this report has no access to it. No second stage was retrieved and no C2 address was resolved.
- **Which machines are infected, or what credentials were taken.** §0.4 identifies one workstation by inference from commit authorship, not by inspection.
- **Whether anything else was tampered with in the same push.** The content diff is two files per repo, but a rewritten history means the *only* trustworthy comparison is against the local pre-rewrite tips, and those exist here for exactly three repos.
- **Whether sprint 0901 is deliberately paused.** Five leaves were started on Friday and nothing has moved since; no comment or note distinguishes a weekend from a stall.
- **Whether the new dashboard endpoint works.** No HTTP-level tests, no second reviewer, and testing is out of scope for scoring per the owner's 2026-08-07 instruction.
- **Whether the dashboard's transaction filters actually filter.** The client sends them; nobody has confirmed the endpoint reads them (§5.2).
- **What the 67 days of dropped Anchor events cost.** Still unmeasured, six days after the fix.
- **Whether the seven already-built notification stories are known to be already built.** Still a code reading, not a conversation.
- **Why `BVA-I192` has not merged**, now twelve days after its last commit and with its board item closed.
- **Anything about the Admin Dashboard board** beyond its existence — seventeenth edition with no sprint.
- **Velocity for either sprint** — 0 of 64 and 0 of 25 items estimated, and nothing has reached REVIEW/QA in ten days.
