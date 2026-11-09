# Beevia — Project Status

**As of 2026-11-09** · Sprint **1002** (21 Oct → 5 Nov, **ended four days ago, day 20**): **63 items, 44 leaves: 1 To do · 3 In progress · 32 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-09.csv` + `beevia-activity-2026-11-09.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-09.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 6 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. The commit messages of the weekend's merges were read as the authors' own account, and none of their production claims could be checked.

Scope: five boards, kept separate and never summed. **Window: 6 Nov 15:03 UTC → 9 Nov 15:03 UTC, 3.0 days (Fri → Mon), including a weekend.**

---

## Quick overview

> **The server stopped requiring a NIN to open a banking account this morning, so Friday's headline risk is gone and a smaller one replaced it: every new account now starts a 30-day clock that the app has no way to stop. Separately, Friday's edition described two limits routes from their code, and they were returning `500` for most users until 6 Nov 15:08 UTC. Meanwhile sprint 1002 has been over for four days: the board has not been touched in 5.0 days, 36 of 44 leaves are unfinished, nothing was accepted, and there is still no successor sprint.**

| Metric | 6 Nov | 9 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 3 / 32 / 0 / 8 | **1 / 3 / 32 / 0 / 8** | none. All four sidecars are byte-identical to 6 Nov |
| Board actions on 1002 in the window | 0 | **0** | last action 4 Nov 16:13 UTC, **5.0 days ago** |
| Transitions into REVIEW/QA, last 7 days (leaves) | 16 | **16** | all on 3–4 Nov: 8 by the leaf's owner (Ayomikun), 6 moved by Ayomikun on others' items, 2 by board administration on David's |
| Owners' last submission of their *own* leaf | 3 Nov 16:04 UTC (Ayomikun, `I387`) | **3 Nov 16:04 UTC** (unchanged) | David's last own submission is 14 Oct, **26.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 11 of 32 | **11 of 32** | none of the weekend's merges maps to a review item |
| Routes in code but not in the spec (consumer / admin), before today's edits | 4 / 0 | **1 / 1** (+1 documented route gone) | now **0 / 0**: specs updated |
| API surface (consumer / admin) | 160 / 75 | **160 / 76** | +1 −1 / +1 (`POST /activity/seen` in, `POST /upgrade/nin` out; admin `take-over`) |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | five merges and migration 0053 went through it |
| `beevia-admin` days since a commit | 7.0 | **10.0** | |
| `beevia-mobile` days since a commit on `main` | 15.2 | **18.2** | `BVA-I353` unchanged (`f46641f`, **5.2 d** ago), still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 / 1.0 / 0.1 | **0.0 / 2.1 / 0.0** | 5 merges on `beevia-api` and `beevia-db-schema` (#102–#105, #34) + 1 bot release, 1 on `beevia-admin-api` (#31) |
| Admin board: open sprint / days since any activity | none / 53.0 | **none / 56.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67%** (67.32) | **0**: see the appendix |

**Two corrections to the 6 Nov edition, and one claim that is no longer true.**

1. **Correction: `GET /wallets/limits` and `GET /kyc/status` did not work for most users.** The 6 Nov edition described both from their code and commit messages ("both now serve a tier and its limits"; `I362`'s text is "exactly what the route returns") and did not catch a defect that `beevia-api` #102 fixed at 15:08 UTC that day, five minutes after the cut-off. Both routes read the tier's row with `findById`, but `kyc_tier_limits` is keyed by `tier` and has no `id` column, so the data layer threw before any query ran and the filter returned `500 database_error` for every user on Tier 2 or 3 and every BVN-only user in grace, which is every existing banking user. The merge was at 12:58 UTC, so they were exposed for about 2 hours, if the deploy followed at once. The unit specs mocked the lookup that threw. This edition also withdraws a smaller claim from the same section: the branch's limits screen would not have read zeros against the published code, it would have met a `500`. The route now works (§3.1), and **the screen still parses the old proposal**.
2. **Not an error, but no longer true: "a new banking user would finish every screen and never get an account."** It was right for the code as of 6 Nov. `beevia-api` #104 (9 Nov, 09:47 UTC) removed the NIN from signup and from the upgrade, so provisioning no longer waits for it (§3.1). Nothing else in the 6 Nov headline changed: the limits are still applied nowhere.
3. **Recommendation 2 of the 6 Nov list (hold the NIN requirement back until the app can send one) was met**, by moving the NIN after account opening instead of behind a switch. It is the only one of the 22 that moved (§7).

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (1 In progress, 15 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **8 own** (+6 moves on other items), all 3–4 Nov | 1.44 d (n=21) | `I362` (**5.0 d**, code merged, route fixed 6 Nov) · `BVA-I8` on 0901-admin (**56.0 d**) | **43** (27 `beevia-api`, 8 `beevia-admin-api`, 8 `beevia-db-schema`) | Four of the five weekend features are not items on any board. The tier limits are still applied nowhere |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | 5 (**0 own**, 3 moved by Ayomikun, 2 by board administration) | 0.99 d (n=36) | 2: `I331` (**18.2 d**), `I361` (6.3 d) | **0 on `main`** · **2 on `BVA-I353`** | No push in 5.2 days. The limits screen still parses a response that never shipped, and there is no NIN step to build against the 30-day clock |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (moved by Ayomikun) | 0.89 d (n=3) | none | n/a | Zero WIP and nothing left To do. A NIN screen is now a design gap with a deadline |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**56.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 10.0 days, and this may be unpushed. The server gained a take-over route over the weekend, on top of hours, unread counts, the article list and card-limit defaults, and none has a screen |

**The three questions for standup:** (1) **What happens to 1002, which ended on Thursday?** 36 leaves are not Done, nobody has touched the board for 5 days, and the only precedent is a sweep that marked unbuilt work Done. (2) **Who builds the NIN step, and who owns the 30-day clock?** From today every new banking user has 30 days to add a NIN the app cannot send, then drops to Tier 0. Nothing enforces the limits yet, so nothing visible happens until it does. (3) **Has anyone called `GET /wallets/limits` on a real account since Friday afternoon, and should the Activity tab call `POST /activity/seen`?** The server clears the badge when asked and the app never asks.

**The three things worth knowing:**

1. **A banking account no longer needs a NIN, and the app still cannot send one.** Signup and the upgrade stop asking; the account opens after BVN and profile; a new account without a NIN is held to Tier 2 limits for 30 days (`grace_until`) and then to Tier 0 until `POST /kyc/nin` succeeds. That route now returns the KYC status instead of the user. Existing users keep the 30 days migration 0051 gave them, ending about 6 Dec. `beevia-mobile` has no NIN step on `main` or on `BVA-I353`, and none is on the board (§3.1).

2. **The limits routes now work, and the limits are still applied nowhere.** `GET /wallets/limits` and `GET /kyc/status` read the table; no send, payout or card funding does. The only client for the first reads the proposal's field names. The honest state is a screen that would show a correct number for a cap the server does not hold (§3.1, §3.3).

3. **1002 is four days over with the board untouched, and the weekend's backend work is not on it.** No board action since 4 Nov 16:13 UTC, no sweep, no successor sprint, so the filter still cannot move. 32 of the 36 unfinished leaves are in review: 11 with merged code, 11 on a branch with no PR, 3 with no matching code, 4 designs whose files are not in git, 3 backend items that already existed. The weekend's four features (NIN change, limits fix, support take-over, Activity badge) map to no item. Nothing has ever left review on 1002 (§1.3, §2).

**If you read nothing else:** decide today what 1002's 36 open leaves become, before anyone sweeps it, and put the NIN step on the board with a design and an owner, because the clock it stops has been running for new users since this morning.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were re-exported for cycle times only (`--no-descriptions`) and are unchanged. The 08-01 and 0901-admin sidecars are byte-identical to 6 Nov, and the CSVs differ only in the export date. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project, checked at about 14:50 UTC today: **no successor to 1002 exists.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **Nothing moved in the window.** The 1002 sidecar is byte-identical to the one taken on 6 Nov, so there was no status change, no owner change, no comment and no new item. 1002's board actions per day:

| 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov | 4 Nov | 5 Nov | 6 Nov | 7–8 Nov (weekend) | 9 Nov (to 15:03) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 17 | 16 | 6 | 6 | 0 | 0 | 5 | **23** | **4** | **0** | **0** | **0** | **0** |

**No comments in the window, and none on 1002 ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002.**

**`I362` reads In progress, and its code is merged and now works.** Its text is "endpoint returning the user's tier, its limits (daily, monthly, single transfer), and today's usage". `GET /wallets/limits` returns that, and since 6 Nov 15:08 UTC it returns it for real users (§3.1). It has been In progress for 5.0 days. Moving it to review is the owner's call. Its parent `I359` (*Transaction Limits & Tier*) is To do and unassigned, with `I360` Done and `I361` (the screen) In progress.

### 1.3 Four days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 32 in REVIEW/QA, 3 In progress (`I331`, `I361`, `I362`), 1 To do (`I373`, reflect card spending in the app). The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. 1002 is now at day four past its end, with neither a sweep nor a carry-over. A sweep would mark Done work that has no merged code (§2) and would not say so.

**The weekend's backend work was not on the board.** #102 (the limits fix), #103 and admin-api #31 (support take-over), #104 (the NIN change) and #105 with schema #34 (the Activity badge) are not items. `I362` covers the limits route but not its fix. The closest parents are `I349` (Support Inbox, To do, unassigned) and the Activity items under the closed `I392`. This is a limit of the board, not a finding about the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

Unchanged from 6 Nov: the weekend's merges map to no review item.

| REVIEW/QA leaves (32) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **11** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391` | Routes on `origin/main`. `I387` caps funding, not spending, and has no maximum for the user. `I391` asks for pagination, search, filter and the Activity tab's query logic, and has none of them |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | **11** | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390` | Unmerged, no PR. `I390` is unassigned and its list would be empty (4 Nov §3.4) |
| Moved to review, no matching code | 3 | `I348`, `I386`, `I372` | `I348`: mock only, and its server table is gone. `I386`: nothing on the branch calls card `/limits`. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen), `I383` (client on the branch) and `I384`. All unchanged.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review, and the inbox now has a take-over route no item mentions. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review. `I359` is To do and unassigned with `I360` Done and `I362` carrying merged code.
- **`origin/BVA-I353`:** 9 ahead, 4 behind `main`, 91 files. Last commit `f46641f` *card history, dispute events* (4 Nov 10:13 UTC), unchanged for **5.2 days**. **No PR.** `refs/pull/54` and `55` are dependabot branches; the newest pull ref on `beevia-mobile` is `55`.
- **WIP ages:** `I331` 18.2 d, `I361` 6.3 d, `I362` 5.0 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edits.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-09`), it first reported 1 consumer route undocumented (`POST /activity/seen`), 1 documented route gone (`POST /upgrade/nin`) and 1 admin route undocumented (`POST /admin/support/conversations/{id}/take-over`), exit 1. After the spec changes: 160/160 consumer, 76/76 admin, proposed 32/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 74 phantom lines from the three `diverged` working trees (31 consumer and 41 admin "in spec, not in code", and 2 "in code, not in spec"), the same as 6 Nov, and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` `main` | `e420d4c` → `01f677c` | #34, **v0.0.53**: `users.activity_seen_at`, migration 0053, released 1 minute after the merge |
| `beevia-api` `main` | `1033fe8` → `1797949` | #102 limits lookup fix. #103 support take-over worker. #104 the NIN moves after account opening. #105 `POST /activity/seen` |
| `beevia-admin-api` `main` | `a7cb08b` → `b4e9744` | #31 `POST /admin/support/conversations/{id}/take-over`; BullMQ added |
| `beevia-mobile` `BVA-I353` | `f46641f` | Unchanged. Unmerged (§2) |

`beevia-admin` (`64304ef`, 30 Oct) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. #105's package pin and #34 landed in the right order by merge time (schema 14:04 UTC, release 14:05 UTC, API 14:13 UTC); whether the migration had run in production by then cannot be seen.

### 3.1 The NIN, the limits routes and the Activity badge

- **A banking account no longer waits for a NIN (#104).** Signup and the chat-to-banking upgrade stop asking for it. The account opens once BVN and profile are in, and **opening it without a NIN sets `kyc_grace_until` 30 days out**, held to Tier 2 limits. A grace already set (the 6 Dec one from migration 0051, or one that has lapsed) is never moved. After the 30 days without a NIN, limits drop to Tier 0 until the user adds one. `POST /wallets` no longer refuses with `nin_required`; `POST /upgrade/profile` needs only a verified BVN.
- **`POST /upgrade/nin` is removed, and `POST /kyc/nin` changed.** It is now NIN only: it checks the NIN against the BVN record, sets Tier 2, clears the grace, moves no onboarding step, provisions nothing and works after the 30 days. **It returns the KYC status (the body of `GET /kyc/status`) instead of the user.** The spec was updated in place; both specs, the RFC and `suggestions.md` §4.16 carry the change.
- **The limits routes were failing, and are fixed (#102).** See correction 1. The new database-backed spec runs both services through the real data layer against the seeded rows, and fails before the fix. Both routes also return correctly for a user in grace and at Tier 2 and 3.
- **`POST /activity/seen` (#105, schema 0.0.53).** Sets `users.activity_seen_at` from the database clock and returns `{ count: 0, seen_at }`. From then on `unattended_count` counts only what arrived after the mark: messages, missed calls and money awaiting the user. Rows that still need action keep `requires_attention`. Every device of the user receives `activity.updated` with `changed_type: seen` and `unattended_count: 0`. **Nothing on `beevia-mobile` calls it**, but `ActivityProvider` already copies `unattended_count` from that event into the badge, so the app side needs only the call.
- **Support take-over (#103 and admin-api #31).** A person takes a thread the assistant still holds. The admin API moves the thread and queues a handover job (BullMQ `support-takeover`, on the Redis both services share). A worker in `beevia-api` asks the assistant for a note, or posts a plain one if the assistant is off or fails, and logs the turn as `takeover`. The assistant's reply is now applied under a row lock and only while the thread is `with_assistant`, so a reply that lands after the takeover is dropped (`superseded`) instead of reaching the user or re-queuing the thread. `claim` and `status → in_progress` on an assistant-held thread now return `409 with_assistant`; `assign` runs the takeover.
- **Not touched:** the tier limits are applied nowhere; `kyc_holds`, Tier 3 and any admin route for the limits have no code; `isSubjectConsent` is a constant; `GET /cards/{id}/transactions` is in kobo.

### 3.2 What the change leaves open

- **The 30-day clock now runs for every new banking user, and the app cannot stop it.** The consequence is invisible today only because the limits are not enforced.
- **The dashboard has no screen for take-over, the article list, the unread counts, the hours or the card-limit default.** No role holds `disputes`, so even a finished screen would meet a `403` (4 Nov §3.2).
- **The queue between the two services has one fallback and no signal.** If the worker is down, every take-over posts the plain note and the agent gets no summary. `suggestions.md` §4.16.
- **`beevia-admin-api` pins `beevia-db-schema` 0.0.50, while the consumer API is on 0.0.53 and the database has migration 0053.** Harmless until the admin API writes to a table a later migration changed (`suggestions.md` §4.16).

### 3.3 The app against the new contract

`beevia-mobile` `main` and `BVA-I353` were searched for `/kyc/nin`, `/upgrade/nin`, `/kyc/status`, `/activity/seen`, `nin_verified` and the `nin` next step. None is called. `/wallets/limits` is called only on the branch, by `wallet_limits.dart`, which reads `per_transaction_max`, `daily_max`, `daily_remaining`, `monthly_max` and `monthly_remaining` from a list. The route returns one object with `daily.limit`, `daily.used` and so on, so the usage card would read 0 of 0. The screen's header cites `openapi.proposed.yaml`, which no longer holds the operation. **Nothing here changed since 6 Nov.**

### 3.4 The standing checks

- **Seams in the support inbox, the article list and the card list**: not touched by the weekend's diff (the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, `search` locale, `meta.total`, the kobo field).
- **`beevia-api` `release.yml`**: read in full. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. No workflow file changed in the range.
- **Branch protection and CI results**: cannot be seen from here.

### 3.5 Document changes this cycle

`openapi.yaml`: added `POST /activity/seen`; removed `POST /upgrade/nin`; `POST /kyc/nin` now returns `KycStatus` and says it is not part of signup; `GET /kyc/status`, `POST /wallets`, `POST /upgrade/profile`, `UpgradeStatus.next_step` (the `nin` step removed), `KycStatus.grace_until`, `limits_tier`, `GET /activity`, `GET /activity/unattended-count` and the `activity.updated` text all updated to the new behaviour. `openapi.admin.yaml`: added `take-over`; `claim`, `assign` and `status` describe the `with_assistant` rule. `openapi.proposed.yaml` and `openapi.admin.proposed.yaml`: unchanged. `api-rfc.md`: inventory rows, a supersession note on §5.22 and a new §5.23. `admin-api-rfc.md`: 75 → 76 operations and a take-over row in §3.16. `suggestions.md`: new §4.16, and item 1 of §4.15 marked resolved on the server.

---

## 4. Risks

- **The 30-day NIN clock.** New banking users have 30 days to add a NIN through an app that cannot send one. The effect is invisible while limits are unenforced, and sharp the day they are. Existing users reach the same cliff about 6 Dec.
- **1002 ended four days ago with nothing accepted and no successor sprint.** A sweep like 0902's would mark no-code, mock-only and unmerged work as delivered, and the 36 unfinished leaves have no destination.
- **A limit that is shown and not applied.** The routes report a daily cap, a monthly cap and a maximum balance that nothing enforces. Switching enforcement on later also decides what happens at the end of the grace.
- **A route that was published, announced in a report, and failed for most users, and nothing noticed for two hours.** The only automated check was a mock. Any route that has only mocked specs is unproven.
- **All of mobile's sprint work is on one unreviewed branch**, 91 files, with `main` 18 days behind it. Each day the server moves, the branch has more contract to catch up with.
- **Every backend repo still deploys or migrates production on push without a test gate**, and one more migration (0053) used it.
- **A user can be told a person is coming when none can come.** No role holds `disputes`, and take-over makes that sentence more likely to be true to the user while the agent still has no screen.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged.
- **A real charge could be answered with "that isn't yours".** Merchant payments have no dispute path and the assistant's instructions say otherwise. Unchanged.
- **Done and REVIEW/QA on the board hide open work.** `I381`'s lockout does not exist, so guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code, and that token also guards raising a card limit.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content.
- **The funding fix still depends on one environment variable that cannot be seen** (`ANCHOR_POOL_ACCOUNT_ID`). **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees.
- **Withdrawn:** the 6 Nov risk that a new banking user would get no account (the server no longer requires the NIN, §3.1). Also withdrawn: the claim that the limits routes were working when published (correction 1).

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. This weekend's changes are on the local tier and on support and are outside the four. Moving the NIN after account opening makes the local ladder easier to start and does not change the international gap: the proposed `GET /kyc/status` was meant to say which currencies a tier unlocks, and the route that shipped does not. PRD §3.2's "set limits" is still met for card funding only; the tier limits are reported and not applied. The NIN, the Tier 2 and Tier 3 ladder, the 30-day grace, the take-over of an AI-assisted support thread, and the Activity badge's seen mark are not in the PRD.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 2 Nov 15:03 → 9 Nov 15:03 UTC. Commit counts are non-merge commits on all refs in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Only `Phoenixdadhev` appears on the backend repos' non-merge commits in this window. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are the same as 6 Nov** (0.99 d n=36, 1.44 d n=21, 0.89 d n=3), because no item entered review. The 0901 and 0902 files were re-exported for this, so the inputs match 6 Nov's reduced set.

### 6.1 Ayomikun Araoye: backend + admin API

**43 commits in 7 days**: 27 in `beevia-api`, 8 in `beevia-admin-api`, 8 in `beevia-db-schema`. **8 own submissions** and 6 moves on other items, all of them on 3–4 Nov. **One WIP item on 1002**, `I362`, started 5.0 days ago, with its code merged. The weekend (Fri 15:08 UTC to Mon 14:13 UTC) held four features and a fix on the server, none of them an item, which is a limit of the board and not a finding about the work. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 56.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct, 19 days ago). **2 on `origin/BVA-I353`**, the latest 5.2 days ago. **Zero own submissions**: the last was `I286` on 14 Oct, **26.0 days** ago. Two of this window's five "submissions" were board administration's, both on 4 Nov and both on leaves whose code is on the branch. WIP: **2 items**, `I331` at 18.2 days (18 times his median of 0.99 d) and `I361` at 6.3. One leaf is To do (`I373`). The server contract for his two open items (limits, onboarding) changed again over the weekend.

### 6.3 Philip Chidera: design

**One 7-day submission**, `I389`, moved by its parent. **Zero WIP and no leaf left To do**: finished, blocked or working untracked. Worth a question, not an assumption. A NIN screen and its error states (`nin_not_found`, `nin_mismatch`, `nin_already_used`, the attempt limit, and the 30-day banner) are not on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window**; the last, `64304ef`, was 30 Oct, now 10.0 days old. The server has moved further towards the screen: hours, unread counts, the transaction view, a flat article list, a card-limits settings route and now take-over, none of which the dashboard calls. Nothing has been pushed in response, which after four corrections this report does not read as nothing having been done. The board still shows none of this: `I348` is in REVIEW/QA with no assignee, and `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 56.0 days.

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
| 2026-W46 (9 Nov → 15:03 UTC) | — | — | 0 | 0 | 0 | 0 |

W45 is complete and unchanged since 6 Nov. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep, re-derived from the sidecars today. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a provider investigation and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Eight of the 16 moves into review in the 7-day window were not made by the owner, and for the mobile ones the code is unmerged.
- **Unpushed and untracked work.** The backend's fixes, the tier model and this weekend's features are not items on any board.
- **A quiet weekend on the board is not a quiet weekend.** The server had five merges.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The commits report test counts, and those were read, not run. The limits routes show why.

---

## 7. Previous recommendations: where they stand

| Recommendation from 6 Nov | Status on 9 Nov |
|---|---|
| **1. Close 1002 now, deliberately** | ❌ **Not done, and it is now four days late.** No board action, no successor sprint, filter still 08-01 |
| **2. Hold the NIN requirement back until the app can send one** | ✅ **Done on the server, by a different route.** #104 moved the NIN after account opening. The app still cannot send one, so this becomes recommendation 2 below |
| **3. Decide whether the tier limits are enforced, and what the end of the grace does** | ❌ **No.** Still reported, not applied. #104 adds a grace for every new account |
| **4. Fix the limits screen; move `I362` to review with a real response** | 🟡 **The server half moved.** #102 made the route work, so a real response exists. No client commit, `I362` still In progress |
| **5. Open a PR for `BVA-I353`** | ❌ **No PR, no commit in 5.2 days** |
| **6. Decide the seeded card default** | ❌ **Not visible** |
| **7. Confirm `ANCHOR_POOL_ACCOUNT_ID`; run a real funding and reveal** | ❌ **Not visible** |
| **8. Decide what a card limit is** | ❌ **No** |
| **9. Record the consent behind each lookup** | ❌ **No** |
| **10. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** Migration 0053 touches neither |
| **11. Let a merchant payment be disputed; correct the assistant's text** | ❌ **No** |
| **12. Fix the seams** | ❌ **No.** The weekend's support diff touched none of them |
| **13. Run one real chat and one real dispute through the assistant** | ❌ **Not visible** |
| **14. Decide the assistant on the record** | ❌ **Not visible**, and take-over leans on the assistant for the handover note |
| **15. Bring the dashboard onto the real contract** | ❌ **No commit in 10.0 days.** One more route without a screen |
| **16. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | ❌ **No** |
| **17. Agree how parent status moves work** | ❌ **No.** No board action at all |
| **18. Assign `I348`, `I349`, `I351`, `I359`, `I390`; give the dashboard a sprint** | ❌ **No** |
| **19. Convert `GET /cards/{id}/transactions` to naira** | ❌ **No.** The cards code was not touched |
| **20. `needs: test` on `sync`; verify jobs elsewhere** | ❌ **Not done.** Five merges and one migration used the ungated path |
| **21. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** Three spec changes and two contract changes were made by hand today |
| **22. Carried items** | ❌ **None moved** |

**One of twenty-two moved, and one more has half its evidence.** The backend's work was real and large and, again, almost none of it was on the list.

---

## 8. What I would do this week

1. **Close 1002 now, deliberately (carried, now four days late).** Accept or return the eleven REVIEW/QA leaves with merged code. Move `I372`, `I386`, `I348` and the eleven branch-only mobile leaves back to In progress. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Put the NIN step on the board with a design and an owner (new, replaces 6 Nov's 2).** From 9 Nov every new banking account has 30 days. The screen, its four error states and a "add your NIN" banner reading `grace_until` from `GET /kyc/status` are the minimum. Call `POST /kyc/nin`, and read the new response body.
3. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** Say where (send, payout, card funding, inflow above the cap into `kyc_holds`) and what a user whose grace has ended sees. About 6 Dec is the date for existing users.
4. **Fix the limits screen to the shipped shape and read `limits_tier` and `grace_until` (carried).** The route works now. Then move `I362` to review.
5. **Open a PR for `BVA-I353` (carried).** Fix the `data.items` parsing and `in`/`out`, read `source`, `default_limit` and `spend_included`, handle `card_transfer_failed` and `card_reveal_unavailable`, and test against a response taken from the server. Split it if that gets it merged sooner, with support first.
6. **Call `POST /activity/seen` from the Activity tab (new).** On entering and on leaving, as the route's text asks. The badge handler already clears on the event.
7. **Call every new route once against a real account before a report says it works (new).** The limits routes failed on the first call. Add the one-call check to the merge routine, or at least to the backend's release steps.
8. **Decide the seeded card default on the record (carried).** Is NGN 500,000 a day and a month what you want on every card?
9. **Confirm `ANCHOR_POOL_ACCOUNT_ID` is set in production and run one real funding and one reveal (carried).**
10. **Decide what a card limit is (carried).** Accept funding caps and rewrite `I371`, `I372`, `I385` and `I387`, or ask the provider whether card product configuration can hold limits.
11. **Record the consent behind each BVN and NIN lookup (carried).**
12. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).** Take-over makes this more urgent: the assistant now signs off to the user with "someone from the Beevia team is taking over".
13. **Put a log line or a metric on the take-over fallback (new).** Without it, a worker that is down reads as a quiet inbox.
14. **Let a merchant payment be disputed, and correct the assistant's text (carried).**
15. **Fix the seams (carried):** the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, the article list's `search` locale and `meta.total`.
16. **Run one real chat and one real dispute through the assistant (carried)**, then pass the dispute's context, force handoff on `didnt_make_this_transaction`, and skip the empty turn.
17. **Decide the assistant on the record (carried).** Who approved it, what the privacy notice says, and whether users are told it is an AI. Add it to the PRD.
18. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add screens for take-over, the card-limit default, the article list and, when a route exists, the tier limits.
19. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up`.
20. **Agree how parent status moves work on this board (carried)**, and have board administration move nothing to review without the owner.
21. **Assign `I348`, `I349`, `I351`, `I359` and `I390` (carried)**, and give the admin dashboard a sprint or say the consumer board is its home.
22. **Convert `GET /cards/{id}/transactions` to naira, or retire it for `/activity` (carried)** before a client renders it.
23. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried). Order schema changes after the code that stops reading the old ones, and bring `beevia-admin-api` onto the current `beevia-db-schema`.
24. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried).
25. **Carried:** send a push when an agent replies; reopen `I392`; close the payments half of blocking; handle `call.ended` on the client; add the `en-US` fallback to FAQ search; decide the statement password and delivery model; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 56.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 56 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, and the server now serves only its hours half) and `I351` FAQ CMS (To do, unassigned; API only). The server gained a take-over route for the inbox over the weekend, with no item and no screen. No admin route for the tier limits exists, and the dashboard's `/settings` page is still a one-line placeholder. `beevia-admin` last moved 10.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-nine days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves, and three of them were considered. **Line 4 (local KYC) holds at 0.90.** The NIN is optional at account opening, so the server no longer blocks the app's onboarding, which is the half of 6 Nov's hold that has been removed. But Tier 2 still cannot be reached from the app (no NIN step), the Tier 3 and parked-funds mechanism have no code, and the rubric's client half, "the full onboarding/wallet flow", is not met for the NIN. Nothing here is evidence for a rise. **Line 6 (multi-currency wallets) holds at 0.85:** the limits route works now, and it is NGN only, reports and does not enforce, and its client reads another shape. **Line 11 (admin oversight) holds at 0.97:** take-over adds a server operation and no screen.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound; no translate change |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | NIN now optional at opening, with a 30-day grace; `POST /kyc/nin` returns the status; Tier 3 and holds unbuilt; the app has no NIN step |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only. The route it was modelled on was deleted |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` works since 6 Nov, NGN only, unenforced, and its client reads another shape |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | Funding, reveal, limits, activity and a default limit on the server. Client card management on unmerged `BVA-I353`; verification model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item. The lookups assert consent as a constant |
| 11 | Admin oversight | 6 | 0.97 | 0 | Take-over added to the support inbox; no role holds `disputes`; the screens still run on a mock |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the NIN change, the limits fix and the Activity route are live in production.** Merge times and release tags are known, and workflow results are not. It also cannot tell whether `YOU_VERIFY` is configured for the NIN endpoint.
- **How many users called the limits routes while they failed**, or whether anyone saw the `500`. Production logs are not visible.
- **Whether migrations 0051–0053 have run**, and when, which decides the date the grace ends.
- **Whether the funding and reveal fixes work in production.** Their commits report sandbox checks.
- **Whether the seeded default was a decision.** No ticket or comment on the board mentions it.
- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, whether Redis takes the take-over job, and whether a real model call succeeds.
- **Who decided on the assistant, on funding caps, on the NIN timing, or on the consent flag, and whether a privacy or legal review happened.** No record is visible here.
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **Whether the commit-reported tests pass, or whether anything renders.** Nothing was executed.
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three background exports starting at about 14:45 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 6 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 6 Nov. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical to 6 Nov. Sprint lists from the `__nonexistent__` dry run for both projects: Beevia `['1002', '0902', '0901', '08-01', '0702', '0701']`, admin `['0901-admin']`. 0901 and 0902 re-exported with `--no-descriptions` for cycle times.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep), and the dry run showed them 168, 60 and 92 commits behind `origin/main`.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-09`: exit 1 before spec edits, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow09.py`, adapted from 6 Nov's): a diff of 1002 against 6 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA in every sidecar.
5. Content checks. `git fetch` (by the sync), `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`: the #102–#105 commit messages and the KYC, upgrade, wallet, activity and support diffs. In `beevia-admin-api`: #31. In `beevia-db-schema`: migration 0053. In `beevia-mobile`: `origin/main` and `origin/BVA-I353` searched for the NIN, status, limits and seen routes, and the Activity socket handler read. `grep` over `origin/main` for the callers of `kyc_tier_limits` and `OutflowService`.
6. Spec and narrative updates (§3.5).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-09.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 9 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 6 Nov 15:03 UTC → 9 Nov 15:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
