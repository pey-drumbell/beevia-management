# Beevia — Project Status

**As of 2026-11-10** · Sprint **1002** (21 Oct → 5 Nov, **ended five days ago, day 21**): **63 items, 44 leaves: 1 To do · 3 In progress · 32 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-10.csv` + `beevia-activity-2026-11-10.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-10.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 9 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 9 Nov 15:03 UTC → 10 Nov 15:03 UTC, 1.0 day (Mon → Tue).**

---

## Quick overview

> **The mobile app has caught up with the server's NIN, limits and Activity contract, but only on a branch: nine minutes after Monday's cut-off David pushed a NIN screen, a deadline banner, a limits screen that reads the shipped response, and the call that clears the Activity badge. Nothing is merged, `main` has not moved in 19 days, and the board has not been touched in 6.0 days. Sprint 1002 is five days over with 36 of 44 leaves unfinished and no successor, and the backend added a test-only route that undoes a verified NIN, with no production guard behind it.**

| Metric | 9 Nov | 10 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 3 / 32 / 0 / 8 | **1 / 3 / 32 / 0 / 8** | none. All three sidecars are byte-identical to 9 Nov |
| Board actions on 1002 in the window | 0 | **0** | last action 4 Nov 16:13 UTC, **6.0 days ago** |
| Transitions into REVIEW/QA, last 7 days (leaves) | 16 | **8** | the window rolled past 3 Nov's morning batch; nothing new entered. 3 by the leaf's owner (Ayomikun), 3 moved by Ayomikun on others' items, 2 by board administration on David's |
| Owners' last submission of their *own* leaf | 3 Nov 16:04 UTC (Ayomikun, `I387`) | **3 Nov 16:04 UTC** (unchanged) | David's last own submission is 14 Oct, **27.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 11 of 32 | **11 of 32** | neither of today's two merges maps to a review item |
| 1002 REVIEW/QA leaves whose code is only on a branch | 11 | **12** | `I386` (card limits screen) gained its client code on `BVA-I353` |
| Routes in code but not in the spec (consumer / admin), before today's edits | 1 / 1 (+1 gone) | **1 / 0** | now **0 / 0**: `DELETE /kyc/nin` added |
| API surface (consumer / admin) | 160 / 76 | **161 / 76** | +1 consumer (`DELETE /kyc/nin`, test only) |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | two more merges went through it; no workflow file changed |
| `beevia-admin` days since a commit | 10.0 | **11.0** | |
| `beevia-mobile` days since a commit on `main` | 18.2 | **19.2** | `BVA-I353` moved: `c04e207`, **1.0 d** ago (was 5.2 d). Three pull refs appeared, #56–#58 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.0 / 2.1 / 0.0 | **0.8 / 3.1 / 1.0** | 2 merges on `beevia-api` (#106, #107) after the 9 Nov cut-off; none elsewhere |
| Admin board: open sprint / days since any activity | none / 56.0 | **none / 57.0** | |
| Client calls to `/kyc/nin`, `/kyc/status`, `/activity/seen` (any ref) | none | **all three, on `BVA-I353` only** | not on `main` |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67%** (67.32) | **0**: see the appendix |

**No correction to the 9 Nov edition is needed, and five of its claims are no longer true.** Each was right at its 15:03 UTC cut-off and changed within the next nine hours:

1. *"`beevia-mobile` has no NIN step on `main` or on `BVA-I353`."* `c04e207` (9 Nov 15:12 UTC) adds `verify_nin.dart`, a `NinBanner` on Home and Wallet that reads `grace_until`, and an `UpgradeTierScreen` that opens it. Still not on `main` (§3.3).
2. *"The limits screen still parses a response that never shipped."* `WalletLimits` now reads `daily.limit`, `daily.used`, `monthly.*`, `single_transfer_limit`, `max_balance` and `next`, which is the shape in `openapi.yaml`. `I361` still reads In progress.
3. *"Nothing on `beevia-mobile` calls `POST /activity/seen`."* The Activity provider calls it on opening and on leaving the tab, which is what the route's text asks for.
4. *"No PR."* Pull refs #56 (head `c04e207`), #57 (head `582d863`) and #58 (head `e0c1647`, which contains the other two) exist on `beevia-mobile`. Their state is not visible from here.
5. *"`I386`: nothing on the branch calls card `/limits`."* `wallet_provider.dart` and `card_limits_form.dart` now call `GET` and `PATCH /cards/{cardId}/limits`.

**The standing claim that is *not* withdrawn:** all of this is unmerged. `origin/main` of `beevia-mobile` is still `ccb4f63` (22 Oct), and the stack in #58 is **335 files, +39,770 −2,067** against it.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (1 In progress, 15 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **3 own** (+3 moves on other items), all on 3 Nov | 1.44 d (n=21) | `I362` (**6.0 d**, code merged and working since 6 Nov) · `BVA-I8` on 0901-admin (**57.0 d**) | **35** (25 `beevia-api`, 4 `beevia-admin-api`, 6 `beevia-db-schema`) | The two merges since Monday's cut-off (a test-only NIN reset and the account name) are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | 3 (**0 own**, 1 moved by Ayomikun, 2 by board administration) | 0.99 d (n=36) | 2: `I331` (**19.2 d**), `I361` (7.3 d) | **0 on `main`** · **2 on `BVA-I353`** | A large push (`c04e207`) with no board movement behind it. `I361` now reads the shipped shape and is still In progress; `I386` has code and sits in review |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (moved by Ayomikun) | 0.89 d (n=3) | none | n/a | Zero WIP and nothing left To do. The NIN screen now exists in code with no design item on the board |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**57.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 11.0 days, and this may be unpushed. The server's take-over route, hours, unread counts and card-limit defaults still have no screen |

**The three questions for standup:** (1) **What happens to 1002, which ended last Thursday?** 36 leaves are not Done, the board has been untouched for 6.0 days, and the only precedent is a sweep that marked unbuilt work Done. (2) **In what order does the mobile stack get reviewed and merged?** #56 is David's branch alone; #58 contains it plus seven commits (and a merge) of tests, dependency bumps and UI fixes under the project owner's identity; 335 files in all. Merging #58 first would take David's work with it. (3) **Where is `KYC_RESET_ENABLED` turned on, and is `main` deployed to that same environment?** The reset route is a `404` by default, and the pipeline that ships `main` is named `production`.

**The three things worth knowing:**

1. **The client half of last week's contract exists, in one commit, on a branch.** `c04e207` closes four items the 9 Nov list carried: the NIN step, the limits shape, the Activity "seen" call and a pull request. It does not close the review: `main` has not moved since 22 Oct, 12 of the 32 REVIEW/QA leaves have their code only on `BVA-I353`, and the commit's own mock server answers the new routes, so what it proves is that the screens match the spec, not that they work against the API (§3.3).

2. **A route that clears a user's NIN now exists, and nothing stops it being switched on in production.** `DELETE /kyc/nin` (#106) takes the NIN off the caller's account and restarts or ends their 30-day grace. It is a `404` unless `KYC_RESET_ENABLED=true`, off by default, which is the only guard: the same pattern as `OTP_ECHO`, with no startup check. The same merge added test BVNs and NINs (`0000…`), whose switch is checked in code and ignored outside the Anchor sandbox. Both signal that KYC is being exercised on a live environment (§3.1).

3. **1002 is five days over with the board untouched, and the newest work is again off the board.** No action since 4 Nov 16:13 UTC, no sweep, no successor sprint, so the filter still cannot move. #106 and #107 map to no item, and neither does the NIN screen. Nothing has ever left review on 1002 (§1.2, §2).

**If you read nothing else:** decide today what 1002's 36 open leaves become, before anyone sweeps it, and decide the order in which #56, #57 and #58 are reviewed before one merge takes the others with it.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01, 0901-admin and 1002 sidecars are byte-identical to 9 Nov, and the CSVs differ only in the export date. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported (closed; the 19 and 27 Oct copies feed the cycle times). `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project, checked at about 14:50 UTC today: **no successor to 1002 exists.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **Nothing moved in the window.** No status change, no owner change, no comment and no new item. 1002's board actions per day:

| 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov | 4 Nov | 5 Nov | 6 Nov | 7–8 Nov | 9 Nov | 10 Nov (to 15:03) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 17 | 16 | 6 | 6 | 0 | 0 | 5 | **23** | **4** | **0** | **0** | **0** | **0** | **0** |

**No comments in the window, and none on 1002 ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

**`I362` and `I361` are both In progress, and the evidence now sits behind both.** `I362` (the limits endpoint) has had merged, working code since 6 Nov 15:08 UTC (6.0 days). `I361` (the limits screen) now has a screen on `BVA-I353` that reads the shipped response. Moving either to review is the owner's call; the screen is still unmerged.

### 1.3 Five days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 32 in REVIEW/QA, 3 In progress (`I331`, `I361`, `I362`), 1 To do (`I373`, reflect card spending in the app). The only precedent is 0902, which ran six days past its end date, then was swept on 21 Oct by board administration (7 REVIEW/QA leaves marked Done, 15 leaves removed to a destination the export cannot see). 1002 is at day five past its end with neither a sweep nor a carry-over. A sweep would mark Done work that has no merged code (§2) and would not say so.

**Work that is not on the board:** #106 (the NIN reset and test identities), #107 (the account name), the NIN screen and banner, the upgrade-tier screen, the NIN's design, and the 335-file stack in #58. This is a limit of the board, not a finding about the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

| REVIEW/QA leaves (32) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **11** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391` | Routes on `origin/main`. `I387` caps funding, not spending, and has no maximum for the user. `I391` asks for pagination, search, filter and the Activity tab's query logic, and has none of them |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | **12** (was 11) | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, **`I386`** | Unmerged. A pull ref now exists (#56). `I390` is unassigned and its list would be empty (4 Nov §3.4). **`I386` is new here**: the branch calls `GET` and `PATCH /cards/{cardId}/limits` through a `CardLimitsForm` |
| Moved to review, no matching code | **2** (was 3) | `I348`, `I372` | `I348`: mock only, and its server table is gone. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen), `I383` (client on the branch) and `I384`. All unchanged.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review. `I359` is To do and unassigned with `I360` Done and `I362` carrying merged code. Unchanged.
- **`origin/BVA-I353`:** 10 ahead, 4 behind `main` (139 files, +18,447 −314 against it). Last commit `c04e207` *kyc implementation* (9 Nov 15:12 UTC), by `Davidtariq96`. It touches 90 files (+5,175 −434; 67 under `lib`, 44 of them in `lib/features`), with a NIN screen, a banner, an upgrade screen, a card-limits form, the Activity provider and models, and iOS and Android manifest changes.
- **The stack above it:** `origin/test-coverage-2026-11-09` (4 commits: CI secrets, "coverage 8.3% → 46.0%", Maestro flows, a Flutter 3.47.1 move) and `origin/fix/ui-audit-2026-11` (18 commits: all of the above, `BVA-I353` merged in, and a UX/UI audit pass), the newest at 9 Nov 21:47 −07:00 (10 Nov 04:47 UTC). `origin/App-bundle` carries one `WIP` commit. Pull refs #57 and #58 are those two heads. None is merged.
- **WIP ages:** `I331` 19.2 d, `I361` 7.3 d, `I362` 6.0 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edit.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-10`), it first reported 1 consumer route undocumented (`DELETE /kyc/nin`), exit 1. After adding it: 161/161 consumer, 76/76 admin, proposed 32/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 76 phantom lines from the three `diverged` working trees (32 consumer and 42 admin "in spec, not in code", 2 "in code, not in spec"), up from 74 only because the two specs gained an operation each since the trees froze, and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `1797949` → `b836f6b` | #106 `DELETE /kyc/nin` (test only) and test BVNs and NINs; #107 the bank account is named as Anchor names it |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged |
| `beevia-db-schema` `main` | `01f677c` (v0.0.53) | Unchanged |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `ccb4f63` (22 Oct) | Unchanged |
| `beevia-mobile` `BVA-I353` | `f46641f` → `c04e207` | NIN, limits, Activity "seen", card limits form (§3.3) |

### 3.1 The reset route, test identities and the account name (`beevia-api` #106, #107)

- **`DELETE /kyc/nin` (#106, merged 9 Nov 17:24 UTC).** Clears the caller's `nin` and `nin_verified_at`, puts `kyc_level` at most 1, and, for an account that is open, either restarts the 30 days (`grace=running`, default) or ends them now (`grace=expired`, every limit to zero). Returns the KYC status. A `404 not_found` unless `KYC_RESET_ENABLED` is true; the flag defaults to false. **Nothing fails startup if the flag is on in production**, and the route is open to any signed-in user, not an admin role. Its commit message says why it exists: once a NIN is verified it is unique to the account and the grace is cleared, so the no-NIN states could not be re-run on live data. The spec, the RFC (§5.24) and `suggestions.md` §4.17 carry it.
- **Test BVNs and NINs (`KYC_TEST_IDS_ENABLED`, same merge).** A number beginning `0000`, then an outcome digit (1 found, 2 not found, 3 found but no selfie matches), is answered by the YouVerify adapter without a paid lookup; everything after the lookup runs as usual. Unlike the reset, this switch **is** checked in code: `testIdsAllowed` ignores it unless `ANCHOR_BASE_URL` is the sandbox. No route changed.
- **The bank account carries Anchor's name (#107, merged 9 Nov 19:59 UTC).** Opening an account and the `virtualNuban.created` webhook now store the deposit account's name from Anchor, falling back to the BVN name, never the display name typed at signup. The commit message reports a live KYC test in which Anchor opened the account as "TEST ADA" while the app showed another name, and says three live accounts on `api.dev` already show their BVN names. No route or schema changed.
- **What these three imply, without proving it:** KYC is being exercised end to end against the Anchor sandbox on a live-data server. Whether that server is the one the `Release` workflow deploys to cannot be seen from here.
- **Not touched, and still true from 9 Nov.** The tier limits are applied nowhere; `kyc_holds`, Tier 3 and any admin route for the limits have no code; `isSubjectConsent` is a constant; `GET /cards/{id}/transactions` is in kobo.

### 3.2 What the change leaves open

- **A switch with no production guard, on a route any user can call.** `suggestions.md` §4.17 item 1.
- **`grace=expired` on a real account zeroes every limit for it.** A useful test, and a quick way to lock a tester out. Say which environment the flag is on.
- **The 30-day clock still runs for every new banking user**, and the client that can stop it is unmerged.
- **The dashboard has no screen for take-over, the article list, the unread counts, the hours or the card-limit default**, and no role holds `disputes`. Unchanged.
- **`beevia-admin-api` pins `beevia-db-schema` 0.0.50**, while the consumer API is on 0.0.53. Unchanged.

### 3.3 The app against the contract

`origin/BVA-I353` at `c04e207` was read for each call the 9 Nov edition said was missing. **Read, not run.**

| Contract | On `BVA-I353` | On `main` |
|---|---|---|
| `POST /kyc/nin`, returning the KYC status | `verify_nin.dart` (344 lines), `KycService.verifyNin`, `KycProvider`. The screen handles `too_many_attempts`, `nin_mismatch` and `nin_already_used`; **`nin_not_found`, `bvn_required` and `verification_unavailable` are not matched by name** | not called |
| `GET /kyc/status` and `grace_until` | `KycStatus` model; `NinBanner` on Home and Wallet shows the deadline and switches to a danger style once the grace has lapsed | not called |
| `GET /wallets/limits` | `WalletLimits.fromJson` reads `daily.limit`, `daily.used`, `monthly.*`, `single_transfer_limit`, `max_balance` and `next`; accepts one object or a list | called only on the branch, old shape |
| `POST /activity/seen` | `markSeen()`, called on opening and on leaving the tab; the provider ignores its own echo | not called |
| `GET` / `PATCH /cards/{cardId}/limits` | `CardLimitsForm`, `wallet_provider.fetchCardLimits` / `updateCardLimits` | not called |

Two cautions. The branch's own mock server answers `/kyc/nin`, `/kyc/status`, `/activity/seen` and `/wallets/limits`, so its tests and Maestro flows exercise those mocks; and **the project's own checklist from 9 Nov (call each new route once against a real account) is not shown to have happened for any of them.** A leftover `print("MARKED ACTIVITY")` sits in `_markSeen`. None of this has been merged, so against `main` the app still has no NIN step.

### 3.4 The standing checks

- **Seams in the support inbox, the article list and the card list**: not touched by #106 or #107 (KYC and wallets only).
- **`beevia-api` `release.yml`**: read in full. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. It rsyncs, installs and runs `pnpm db:migrate` on push to `main`, then `deploy` builds and reloads pm2 with a health check and a rollback. No workflow file changed in the range (last change 1 Oct, in `beevia-api`; 28 Sep in `beevia-admin-api`; 1 Oct in `beevia-db-schema`). The `postman-sync` job runs on every push and re-uploads the collection when it changed, and #106's two commits edited it.
- **Branch protection and CI results**: cannot be seen from here.

### 3.5 Document changes this cycle

`openapi.yaml`: added `DELETE /kyc/nin` (`removeNin`, query `grace`, `200` KYC status, `400`, `404`), described as test only. `openapi.admin.yaml`, `openapi.proposed.yaml`, `openapi.admin.proposed.yaml`: unchanged. `api-rfc.md`: 160 → 161, the KYC row 7 → 8, an inventory row, and a new §5.24. `admin-api-rfc.md`: unchanged. `suggestions.md`: new §4.17.

---

## 4. Risks

- **A reset route with no production guard.** `KYC_RESET_ENABLED` is a default and a comment. If it is on where real users are, any of them can clear their own NIN and restart their own grace, and `grace=expired` zeroes their limits.
- **The client the contract needs is unmerged, and the stack above it is 335 files.** Two reviews in sequence (#56 then #58) is a different job from one, and merging #58 first takes David's branch with it. `main` is 19 days behind.
- **1002 ended five days ago with nothing accepted and no successor sprint.** A sweep like 0902's would mark no-code, mock-only and unmerged work as delivered, and the 36 unfinished leaves have no destination.
- **The 30-day NIN clock.** Every new banking user has 30 days to add a NIN. The client that can send one is unmerged, so the effect is hidden only because the limits are not enforced.
- **A limit that is shown and not applied.** Unchanged.
- **A route that was published, announced in a report, and failed for most users.** The 9 Nov edition's own correction. Any route with only mocked specs is unproven, and the new client's mock server is an instance of that.
- **Every backend repo still deploys or migrates production on push without a test gate.** Two more merges used it.
- **A user can be told a person is coming when none can come.** No role holds `disputes`, and take-over makes that sentence more likely to be true while the agent has no screen. Unchanged.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged. The test identities skip the lookup and do not change it.
- **A real charge could be answered with "that isn't yours".** Unchanged.
- **Done and REVIEW/QA on the board hide open work.** `I381`'s lockout does not exist, and that token also guards raising a card limit. Unchanged.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content. **The funding fix still depends on one environment variable that cannot be seen** (`ANCHOR_POOL_ACCOUNT_ID`). **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees.
- **Withdrawn:** 9 Nov's "no pull request for `BVA-I353`" and "the app cannot send a NIN" (as a statement about the branch; both stand for `main`).

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. Today's server changes are test tooling and a naming fix and are outside the four. The client changes on `BVA-I353` sit on the local KYC tier, the wallet screens and cards; none is merged, so none moves a line (appendix). PRD §3.2's "set limits" is still met for card funding only: the branch's card-limits form edits funding caps, and the tier limits are reported and not applied.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 3 Nov 15:03 → 10 Nov 15:03 UTC. Commit counts are non-merge commits on all remote refs in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded (6 on `beevia-db-schema`). Only `Phoenixdadhev` appears on the backend repos' non-merge commits in this window. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are the same as 9 Nov** (0.99 d n=36, 1.44 d n=21, 0.89 d n=3), because no item entered review.

### 6.1 Ayomikun Araoye: backend + admin API

**35 commits in 7 days**: 25 in `beevia-api`, 4 in `beevia-admin-api`, 6 in `beevia-db-schema`. **3 own submissions** and 3 moves on other items, all on 3 Nov (the 13:52 batch rolled out of the window). **One WIP item on 1002**, `I362`, started 6.0 days ago, with its code merged. Since the 9 Nov cut-off: #106 and #107, neither an item. The last commit is 0.8 d old. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 57.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** (the last, `8039bd7`, was 21 Oct, 20 days ago). **2 on `origin/BVA-I353`**, the latest 1.0 d ago and by far the larger. **Zero own submissions**: the last was `I286` on 14 Oct, **27.0 days** ago. Two of this window's three "submissions" were board administration's, both on 4 Nov. WIP: **2 items**, `I331` at 19.2 days (19 times his median of 0.99 d) and `I361` at 7.3. One leaf is To do (`I373`). The server contract for his two open items has not changed since the weekend, and the branch now meets it. The board does not show any of that.

### 6.3 Philip Chidera: design

**One 7-day submission**, `I389`, moved by its parent. **Zero WIP and no leaf left To do**: finished, blocked or working untracked. Worth a question, not an assumption. The NIN screen and its states now exist in code, and no design item for them is on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window**; the last, `64304ef`, was 30 Oct, now 11.0 days old. The server has moved further towards the screen: hours, unread counts, the transaction view, a flat article list, a card-limits settings route and take-over, none of which the dashboard calls. Nothing has been pushed in response, which this report does not read as nothing having been done. `I348` is in REVIEW/QA with no assignee, and `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 57.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (2 → 8 Nov) | — | — | **16** | 8 | 6 | 2 |
| 2026-W46 (9 Nov → 10 Nov 15:03 UTC) | — | — | 0 | 0 | 0 | 0 |

W45 is complete and unchanged. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep, re-derived from the sidecars today. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers, and this week the client work that would fill the review queue is arriving as one very large branch.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a provider investigation and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Five of the eight moves into review in the 7-day window were not made by the owner, and for the mobile ones the code is unmerged.
- **Unpushed and untracked work.** The backend's last two merges, the NIN screen and the 335-file stack are not items on any board.
- **Commit counts reward small commits.** `c04e207` is one commit; the weekend's backend work was many. Neither is a measure of effort.
- **A quiet board is not a quiet day.** The server had two merges, and the mobile refs gained 10 non-merge commits in the 7 days (8 under the project owner's identity, 2 David's), most on 9 Nov.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository. The mobile commit messages report coverage of 46.0% and 26 passing Maestro flows, and those figures were read, not checked.

---

## 7. Previous recommendations: where they stand

| Recommendation from 9 Nov | Status on 10 Nov |
|---|---|
| **1. Close 1002 now, deliberately** | ❌ **Not done, and five days late.** No board action, no successor sprint, filter still 08-01 |
| **2. Put the NIN step on the board with a design and an owner** | 🟡 **The code exists; the board item and the design still do not.** `verify_nin.dart`, `NinBanner` and `UpgradeTierScreen` are on `BVA-I353`, unmerged |
| **3. Decide whether the tier limits are enforced, and what the grace's end does** | ❌ **No.** Still reported, not applied |
| **4. Fix the limits screen to the shipped shape; move `I362` to review** | 🟡 **Screen fixed on the branch.** `I361` and `I362` both still In progress |
| **5. Open a PR for `BVA-I353`** | ✅ **A pull ref exists (#56, head `c04e207`).** Not merged, and its state is not visible |
| **6. Call `POST /activity/seen` from the Activity tab** | ✅ **Done on the branch**, on opening and on leaving |
| **7. Call every new route once against a real account** | 🟡 **Partly, on the backend side.** #106 and #107 describe a live KYC test on a dev server. No sign for the limits routes or the client's calls |
| **8. Decide the seeded card default** | ❌ **Not visible** |
| **9. Confirm `ANCHOR_POOL_ACCOUNT_ID`; run a real funding and reveal** | ❌ **Not visible** |
| **10. Decide what a card limit is** | ❌ **No.** The branch's form edits funding caps, which is the answer the server gives |
| **11. Record the consent behind each lookup** | ❌ **No** |
| **12. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible** |
| **13. A metric or log line on the take-over fallback** | ❌ **No** |
| **14. Let a merchant payment be disputed; correct the assistant's text** | ❌ **No** |
| **15. Fix the seams** | ❌ **No** |
| **16. Run one real chat and one real dispute through the assistant** | ❌ **Not visible** |
| **17. Decide the assistant on the record** | ❌ **Not visible** |
| **18. Bring the dashboard onto the real contract** | ❌ **No commit in 11.0 days** |
| **19. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | ❌ **No** |
| **20. Agree how parent status moves work** | ❌ **No board action at all** |
| **21. Assign `I348`, `I349`, `I351`, `I359`, `I390`; give the dashboard a sprint** | ❌ **No** |
| **22. Convert `GET /cards/{id}/transactions` to naira** | ❌ **No.** The cards code was not touched |
| **23. `needs: test` on `sync`; verify jobs elsewhere** | ❌ **Not done.** Two more merges used the ungated path |
| **24. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** One more route was added by hand today |
| **25. Carried items** | ❌ **None moved** |

**Two of twenty-five are met (a pull ref, the seen call), and three more have half their evidence.** All five moved because of one client commit.

---

## 8. What I would do this week

1. **Close 1002 now, deliberately (carried, now five days late).** Accept or return the eleven REVIEW/QA leaves with merged code. Move `I372`, `I348` and the twelve branch-only mobile leaves according to what merges. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Settle the order of #56, #57 and #58 before anyone merges one (new).** #58 contains the other two. Review David's branch (#56) on its own against the API first, merge it, and let the test and UI-audit work rebase onto it, or the 90 files of David's last commit arrive buried in a 335-file change.
3. **Call each new route once from a real build against the sandbox before merging the client (carried, now sharper).** `POST /kyc/nin`, `GET /kyc/status`, `GET /wallets/limits`, `POST /activity/seen`, and `PATCH /cards/{id}/limits`. Handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name in `verify_nin.dart`, and remove the debug `print`.
4. **Add a startup check that `KYC_RESET_ENABLED` is off when `NODE_ENV` is `production` (new).** Same fix `suggestions.md` §1.2 asks for `OTP_ECHO`. Say which environment the flag is on today, and whether `main` deploys there.
5. **Put the NIN step on the board with a design and an owner (carried).** The code exists, so the item is review, not build. `I361` and `I362` can move to review now.
6. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
7. **Decide the seeded card default on the record (carried).** Is NGN 500,000 a day and a month what you want on every card?
8. **Confirm `ANCHOR_POOL_ACCOUNT_ID` is set in production and run one real funding and one reveal (carried).**
9. **Decide what a card limit is (carried).** The branch edits funding caps, so rewrite `I371`, `I372`, `I385` and `I387` to say so, or ask the provider whether card product configuration can hold limits.
10. **Record the consent behind each BVN and NIN lookup (carried).**
11. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
12. **Put a log line or a metric on the take-over fallback (carried).**
13. **Let a merchant payment be disputed, and correct the assistant's text (carried).**
14. **Fix the seams (carried):** the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, the article list's `search` locale and `meta.total`.
15. **Run one real chat and one real dispute through the assistant (carried)**, then pass the dispute's context, force handoff on `didnt_make_this_transaction`, and skip the empty turn.
16. **Decide the assistant on the record (carried).** Who approved it, what the privacy notice says, and whether users are told it is an AI. Add it to the PRD.
17. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add screens for take-over, the card-limit default, the article list and, when a route exists, the tier limits.
18. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up`.
19. **Agree how parent status moves work on this board (carried)**, and have board administration move nothing to review without the owner.
20. **Assign `I348`, `I349`, `I351`, `I359` and `I390` (carried)**, and give the admin dashboard a sprint or say the consumer board is its home.
21. **Convert `GET /cards/{id}/transactions` to naira, or retire it for `/activity` (carried)** before a client renders it.
22. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried). Order schema changes after the code that stops reading the old ones, and bring `beevia-admin-api` onto the current `beevia-db-schema`.
23. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried).
24. **Carried:** send a push when an agent replies; reopen `I392`; close the payments half of blocking; handle `call.ended` on the client; add the `en-US` fallback to FAQ search; decide the statement password and delivery model; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 57.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 57 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, and the server now serves only its hours half) and `I351` FAQ CMS (To do, unassigned; API only). The server has a take-over route for the inbox with no item and no screen. No admin route for the tier limits exists, and the dashboard's `/settings` page is still a one-line placeholder. `beevia-admin` last moved 11.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed seventy days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves, and four were considered. **Line 4 (local KYC) holds at 0.90.** The NIN screen, the status model and the deadline banner exist, which is the client half the line has been waiting for, but on `BVA-I353` and not on `main`; and Tier 3 and the parked-funds mechanism still have no code. When the branch merges, the client half is met for the NIN and this line is the first to consider a rise. **Line 6 (multi-currency wallets) holds at 0.85:** the limits screen now reads the shipped shape on the branch, the route is NGN only and reports without enforcing. **Line 9 (virtual cards) holds at 0.80:** the card limits form is on the same unmerged branch, and the rubric scores the merged client. **Line 11 (admin oversight) holds at 0.97:** nothing in the dashboard changed. The `DELETE /kyc/nin` route and #107's naming fix are test tooling and a correction, and neither is evidence for any line.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound; no translate change |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | NIN optional at opening, 30-day grace, `POST /kyc/nin` returns the status. Client NIN step now exists on `BVA-I353` only. Tier 3 and holds unbuilt |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only. The route it was modelled on was deleted |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` works, NGN only, unenforced; its client reads the shipped shape on the branch only |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | Funding, reveal, limits, activity and a default limit on the server. Client card management, including the limits form, on unmerged `BVA-I353`; verification model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item. The lookups assert consent as a constant |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed; no role holds `disputes`; the screens still run on a mock |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether #106 and #107 are live, and where.** Merge times and the workflow are known; results and the target host are not. Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere cannot be seen.
- **Whether the pull refs #56–#58 are open, reviewed or approved.** The refs and their heads are visible; the pull requests are not.
- **Whether any of the client's new screens work against the API.** Nothing was executed, and the branch's mock server answers the same routes.
- **Whether migrations 0051–0053 have run**, and when, which decides the date the grace ends.
- **Whether the funding and reveal fixes work in production.** Their commits report sandbox checks.
- **Whether the seeded default was a decision.**
- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, whether Redis takes the take-over job.
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route or on the consent flag, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **Whether the commit-reported tests pass, or whether anything renders.**
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three background exports starting at about 14:45 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 9 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical. Sprint lists from the `__nonexistent__` dry run for both projects: Beevia `['1002', '0902', '0901', '08-01', '0702', '0701']`, admin `['0901-admin']`. 0901 and 0902 not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-10`: exit 1 before the spec edit, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow10.py`, adapted from 9 Nov's): a diff of 1002 against 9 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA in every sidecar.
5. Content checks. `git fetch` (by the sync), `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`: the #106 and #107 commit messages, the KYC controller, DTO, services and env schema. In `beevia-mobile`: `c04e207`'s file list and the NIN, status, limits, Activity and card-limits code on `origin/BVA-I353`, plus the commit messages on the two branches above it. `release.yml` read in full.
6. Spec and narrative updates (§3.5).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor. Commits under the project owner's identity are reported as facts about the branches they are on, not as a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`merge-base`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-10.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 10 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 9 Nov 15:03 UTC → 10 Nov 15:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (−07:00).
