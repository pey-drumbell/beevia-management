# Beevia — Project Status

**As of 2026-11-06** · Sprint **1002** (21 Oct → 5 Nov, **ended yesterday, day 17**): **63 items, 44 leaves: 1 To do · 3 In progress · 32 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-06.csv` + `beevia-activity-2026-11-06.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-06.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 5 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. The commit messages of the day's merges were read as the authors' own account, and none of their production claims could be checked.

Scope: five boards, kept separate and never summed. **Window: 5 Nov 15:01 UTC → 6 Nov 15:03 UTC, 1.0 day (Thu → Fri).**

---

## Quick overview

> **The server now requires a NIN before it will open a banking account, and the app has no NIN step, so a new banking user would finish every screen and never get an account. The same two merges publish a limits route that nothing applies and that the only screen built for it cannot read. Meanwhile the sprint ended yesterday and nobody touched the board: 36 of 44 leaves are unfinished, nothing was accepted, and there is no successor sprint.**

| Metric | 5 Nov | 6 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 3 / 32 / 0 / 8 | **1 / 3 / 32 / 0 / 8** | none. The export and the sidecar are byte-identical to 5 Nov |
| Board actions on 1002 in the window | 4 | **0** | none on the sprint's last day. Last action 4 Nov 16:13 UTC, **2.0 days ago** |
| Transitions into REVIEW/QA, last 7 days (leaves) | 16 | **16** | 8 by the leaf's owner (Ayomikun), 6 moved by Ayomikun on others' items, 2 by board administration on David's |
| Owners' last submission of their *own* leaf | 3 Nov 16:04 UTC (Ayomikun, `I387`) | **3 Nov 16:04 UTC** (unchanged) | David's last own submission is 14 Oct, **23.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 11 of 32 | **11 of 32** | none of the day's merges maps to a review item |
| Routes in code but not in the spec (consumer / admin), before today's edits | 0 / 0 | **4 / 0** (+2 documented routes gone) | now **0 / 0**: specs updated |
| API surface (consumer / admin) | 158 / 75 | **160 / 75** | +4 −2 / 0. One in-place contract note (card kobo) |
| Proposed operations (consumer / admin) | 34 / 18 | **32 / 18** | −2: `GET /kyc/status` and `GET /wallets/limits` shipped, both in a different shape |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | two more migrations (0051, 0052) went through it |
| `beevia-admin` days since a commit | 6.0 | **7.0** | |
| `beevia-mobile` days since a commit on `main` | 14.2 | **15.2** | `BVA-I353` unchanged (`f46641f`, 2.2 d ago), still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.0 / 0.0 / 0.0 | **0.1 / 1.0 / 0.1** | 4 merges on `beevia-api` and `beevia-db-schema` (#100, #101, #32, #33) + 2 bot releases; none on `beevia-admin-api` |
| Admin board: open sprint / days since any activity | none / 52.0 | **none / 53.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67%** (67.32) | **0**: see the appendix for why the KYC and limits lines hold |

**One thing in 5 Nov that is no longer true, not a correction.** That edition said, of `I362` (*Limits & Usage Endpoint*), that nothing on `origin/main` serves a tier or `/users/me/limits`. Both `GET /kyc/status` and `GET /wallets/limits` now serve a tier and its limits, and `/users/me/limits` is still proposed. `I362` and its parent `I359` are unchanged on the board: `I362` is still In progress while its code is merged (§1.2, §3.1). **No claim from 5 Nov was withdrawn.**

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (1 In progress, 15 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **8 own** (+6 moves on other items) | 1.44 d (n=21) | `I362` (2.0 d, code merged) · `BVA-I8` on 0901-admin (**53.0 d**) | **37** (23 `beevia-api`, 7 `beevia-admin-api`, 7 `beevia-db-schema`) | `I362` shipped as code and still reads In progress. The NIN change reached `main` with no client, and the tier limits are not enforced anywhere |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | 5 (**0 own**, 3 moved by Ayomikun, 2 by board administration) | 0.99 d (n=36) | 2: `I331` (**15.2 d**), `I361` (3.3 d) | **0 on `main`** · **3 on `BVA-I353`** | The Transaction Limits screen on the branch reads the proposed response, and the app has no NIN step. `I331` is 15 times the median |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (moved by Ayomikun) | 0.89 d (n=3) | none | n/a | Zero WIP and nothing left To do: what is next? A NIN screen is a design gap |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**53.0 d**) | **1** (`beevia-admin`, 30 Oct) | No commit in 7.0 days, and this may be unpushed. The server gained routes for hours, unread counts, the article list and card-limit defaults, and none has a screen |

**The three questions for standup:** (1) **What happens to 1002, which ended yesterday?** 36 leaves are not Done, no one touched the board on the last day, there is no successor sprint, and the one precedent is a sweep that marked unbuilt work Done. (2) **Who builds the NIN step in the app, and should the server change reach users before it does?** Today a new banking user would get a `200` from the profile step and no account. (3) **Is the tier limit meant to be enforced, and what should happen to existing users when their 30-day grace ends around 6 Dec?** Today nothing reads the limits to refuse a send.

**The three things worth knowing:**

1. **The server now needs a verified NIN before it opens a banking account, and the app cannot supply one.** `POST /kyc/nin` and `POST /upgrade/nin` look the NIN up with YouVerify and compare it to the BVN already verified. Provisioning waits for it, `POST /wallets` refuses a new account without it, and the profile step on the upgrade path refuses too. Neither `beevia-mobile` `main` nor `BVA-I353` calls either route, so a new user who finishes the BVN and profile steps gets a `200` and nothing is queued. Existing accounts are untouched, and every user with a verified BVN now has 30 days' grace. The Entrust document check was removed in the same change (§3.2).

2. **`GET /wallets/limits` and `GET /kyc/status` report limits that nothing applies, and the app's screen reads zeros from them.** Only those two routes read the new `kyc_tier_limits` table. No send, payout or card funding checks the daily, monthly, single-transfer or maximum-balance figure, and the parked-funds table and the Tier 3 address flow have no code. The Transaction Limits screen on `BVA-I353` reads `daily_max` and `daily_remaining` from a list, which is the proposal, and the route returns one object with `daily.limit` and `daily.used`. It would show 0 of 0 (§3.3, `suggestions.md` §4.15).

3. **1002 ended yesterday with the board untouched.** No action on the last day, none since 4 Nov 16:13 UTC, no sweep and no successor sprint, so the filter still cannot move. 32 of the 36 unfinished leaves are in review: 11 with merged code, 11 on a branch with no PR, 3 with no matching code, 4 designs whose files are not in git, 3 backend items that already existed. Nothing has ever left review on 1002 (§1.3, §2).

**If you read nothing else:** do not let the NIN requirement reach users before the app can send one, and decide today what 1002's 36 open leaves become. If the sprint is swept as 0902 was, `I372` (no code), `I386` and `I348` (mock only) will read as delivered, along with eleven screens nobody has merged.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were not re-exported. The 08-01 and 0901-admin sidecars are byte-identical to 5 Nov, and the CSVs differ only in the export date. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project, checked at about 15:00 UTC today: **no successor to 1002 exists, and it ended yesterday.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **Nothing moved in the window.** The 1002 sidecar is byte-identical to the one taken on 5 Nov, so there was no status change, no owner change, no comment and no new item. 1002's board actions per day:

| 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov | 4 Nov | 5 Nov | 6 Nov (to 15:03) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 17 | 16 | 6 | 6 | 0 | 0 | 5 | **23** | **4** | **0** | **0** |

**No comments in the window, and none on 1002 ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002.**

**`I362` reads In progress, and its code is merged.** Its text is "endpoint returning the user's tier, its limits (daily, monthly, single transfer), and today's usage", and `GET /wallets/limits` returns exactly that (§3.1). It was last moved on 4 Nov at 16:04 UTC, 2.0 days ago. The route was merged today at 12:58 UTC. Moving it to review is the owner's call, and it should wait for a reader of the response (§3.3). Its parent `I359` (*Transaction Limits & Tier*) is To do and unassigned, with `I360` Done and `I361` (the screen) In progress.

### 1.3 What the day after 1002's end holds

1002 ended **yesterday, Thursday 5 Nov**. 36 of its 44 leaves are not Done: 32 in REVIEW/QA, 3 In progress (`I331`, `I361`, `I362`), 1 To do (`I373`, reflect card spending in the app). The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. The board has not been touched since 4 Nov 16:13 UTC, so neither a sweep nor a carry-over has happened yet. A sweep would mark Done work that has no merged code (§2) and would not say so.

---

## 2. Sprint 1002: what is in review, and whether the code exists

Unchanged from 5 Nov: the day's merges map to no review item.

| REVIEW/QA leaves (32) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **11** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391` | Routes on `origin/main`. `I387` caps funding, not spending, and has no maximum for the user. `I391` asks for pagination, search, filter and the Activity tab's query logic, and has none of them |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | **11** | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390` | Unmerged, no PR. `I390` is unassigned and its list would be empty (4 Nov §3.4) |
| Moved to review, no matching code | 3 | `I348`, `I386`, `I372` | `I348`: mock only, and its server table is gone. `I386`: nothing on the branch calls card `/limits`. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen), `I383` (client on the branch) and `I384`. All unchanged.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review. `I359` (*Transaction Limits & Tier*) is To do and unassigned with `I360` Done and `I362` carrying merged code.
- **`origin/BVA-I353`:** 9 ahead, 4 behind `main`, 91 files. Last commit `f46641f` *card history, dispute events* (4 Nov 10:13 UTC), unchanged for 2.2 days. **No PR.** `refs/pull/53`–`55` are dependabot branches, and `#52` was `BVA-I316`, merged on 22 Oct.
- **WIP ages:** `I331` 15.2 d, `I361` 3.3 d, `I362` 2.0 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edits.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-06`), it first reported 4 consumer routes undocumented, 2 documented routes gone and 2 proposals shipped (exit 1). After the spec changes: 160/160 consumer, 75/75 admin, proposed 32/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 74 phantom lines from the three `diverged` working trees (31 consumer + 41 admin "in spec, not in code", and 2 "in code, not in spec"), and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` `main` | `5b988c1` → `e420d4c` | #32, **v0.0.51**: KYC tier tables and columns, migration 0051. #33, **v0.0.52**: monthly and single-transfer limit columns, migration 0052. Both released within 40 seconds of the merge |
| `beevia-api` `main` | `5bd0b30` → `1033fe8` | #100 card amounts as kobo. #101 Tier 2 needs a NIN, Entrust removed, `GET /wallets/limits`. +2,152/−1,065 across 61 files |
| `beevia-admin-api` `main` | `a7cb08b` | Unchanged |
| `beevia-mobile` `BVA-I353` | `f46641f` | Unchanged. Unmerged (§2) |

`beevia-admin` (`64304ef`, 30 Oct) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. The day's merges landed between 12:12 UTC on 5 Nov and 12:58 UTC today, so this edition covers more than the window's hours.

### 3.1 Tiers, the NIN, and what was removed

- **Banking now starts at Tier 2.** There is no Tier 1. Tier 2 is a verified BVN plus a NIN whose record names the same person: the same date of birth, and the BVN's first and last names among the NIN's names (any order; case and accents ignored). Tier 3 adds an address confirmed by a YouVerify field agent. `tier` is 0, 2 or 3.
- **`POST /kyc/nin` and `POST /upgrade/nin`.** Five attempts an hour per user, counted from the verification log; a provider outage is `503 verification_unavailable` and alerts Slack (`kyc_nin_unavailable`). `409 nin_already_used` if the NIN belongs to another account. On success it stores the NIN whole, sets `kyc_level` 2 and clears the grace.
- **Provisioning waits for the NIN.** Onboarding and upgrade only queue an NGN account when BVN, NIN, email and address are all on file. `POST /upgrade/profile` refuses without a NIN (`nin_required`), and `POST /wallets` refuses a **new** NGN account without one. Existing wallets are untouched.
- **Existing users get 30 days.** Migration 0051 puts every user with a verified BVN at `kyc_level` 1 with `kyc_grace_until` thirty days out (about 6 Dec, if it ran at the release). That includes anyone who had reached a higher level, and users whose account was never provisioned. During the grace `tier` is 0 and `limits_tier` is 2.
- **The Entrust (Onfido) document check is gone.** `POST /kyc/id/start` and `POST /kyc/entrust/webhook` were removed, with the service, the env vars, the Postman requests and the `kyc_id_rejected` alert. The Entrust columns remain. No client called either route. It was the only document check, and `POST /kyc/international/start` (still proposed) described itself as mirroring it.
- **`GET /kyc/status`** shipped, narrower than proposed: the local ladder only, with no international tier and no unlocked currencies.
- **`GET /wallets/limits`** shipped in a different shape from its proposal: one NGN object with `daily` and `monthly` as `{ limit, used, remaining, percent_used }`, plus `single_transfer_limit`, `max_balance`, `tier`, `limits_tier`, `grace_until` and `next`. "Used" is money that left the wallet: P2P sends, requests the user paid, bank payouts without the fee, and card fundings whose wallet debit went through, per Lagos day and month. The monthly limit is not seeded, so it reads as no limit; the single-transfer limit is seeded at each tier's daily limit (Tier 2 NGN 200,000, Tier 3 NGN 5,000,000).
- **#100, card amounts.** The commit says Anchor reports every amount in kobo and the card balance was read as naira: three NGN 100 fundings left NGN 300 on a card the app showed as NGN 30,000, and the withdrawal pre-check passed NGN 2,000 and NGN 10,000 on to Anchor, which refused them. Balance, activity rows and statement lines now divide by 100. `GET /cards/{id}/transactions` still passes the partner's payments through, so **its `amount` is in kobo**, the only such field in the API. This is the first evidence in the repos that funding reached a card after yesterday's pool fix, though the message does not say in which environment.

### 3.2 What does not exist behind the new tiers

- **Nothing applies the limits.** On `origin/main` only `GET /kyc/status` and `GET /wallets/limits` read `kyc_tier_limits`. The commit message says the usage calculation is shared "so limit enforcement can reuse it". A user shown "NGN 200,000 a day" can send more.
- **Parked funds and Tier 3 have no code.** `kyc_holds` ("money received above a Tier 2 user's cap, parked until they upgrade") is unused, and `address_verifications` has no route or webhook that fills it.
- **No admin can change the limits.** The migration says an admin can, and `beevia-admin-api` has no route for `kyc_tier_limits`, so a change is a SQL update.
- **The consent flag is a constant.** Both the BVN and the NIN lookup send `isSubjectConsent: true` with no consent step and no record (`suggestions.md` §4.15).

### 3.3 The app against the new contract

- **No NIN step.** Neither `main` nor `BVA-I353` calls `POST /kyc/nin` or `POST /upgrade/nin`, or reads `nin_verified` or the new `nin` value of `next_step`. The client only reads `GET /wallets`, so there is no `400` for it to display. A new user finishes BVN and profile with a `200`, and no account is queued.
- **The limits screen reads the old proposal.** `wallet_limits.dart` reads `per_transaction_max`, `daily_max`, `daily_remaining`, `monthly_max` and `monthly_remaining` and takes the first item of a list. Against the shipped object every one is absent, so it returns zeros and the usage card would read 0 of 0. The screen's header cites `openapi.proposed.yaml`. Nothing on the branch reads `tier`, `limits_tier` or `grace_until`, and the "Upgrade Tier" entry (`I359`) leads to a flow that now needs a step the app does not have.
- **Unchanged from 5 Nov:** the branch does not read `source`, `default_limit` or `card_transfer_failed`, its card history takes rows only when `data` is a list, and `call.ended` is unhandled on `main` and on the branch.

### 3.4 The standing checks

- **Pipelines:** no workflow file changed in any of the three repos since 5 Nov. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`" and `sync` still migrates before `deploy`; `beevia-admin-api`'s `sync.yml` still triggers on push; db-schema's Release published v0.0.51 and v0.0.52 within 40 seconds of each merge. All three still deploy or migrate on push with no test gate. **Migrations 0051 and 0052 shipped on that path**, and 0051 rewrites `kyc_level` for every user with a verified BVN.
- **Admin API:** unchanged. The inbox routes still return `403` for every role: **no role holds `disputes`**. The mock is still the dashboard's default.
- `PaymentService.activeNgn()`, `StubTranslateAdapter`, unmapped `22P02`, unindexed `messages.ref_id`, FAQ search's missing `en-US` fallback: all unchanged.
- `POST /auth/step-up`: no attempt limit, and no throttler anywhere in `src`. It still guards `PATCH /cards/{id}/limits`.

### 3.5 Document changes this cycle

- **`openapi.yaml`:** +4 (`POST /kyc/nin`, `GET /kyc/status`, `POST /upgrade/nin`, `GET /wallets/limits`), −2 (`POST /kyc/id/start`, `POST /kyc/entrust/webhook`). In place: `POST /upgrade/profile` and `POST /wallets` (the NIN gate and `nin_required`), `UpgradeStatus` (`nin_verified`, `nin` next step), `GET /cards/{cardId}/transactions` (kobo). New schemas `NinRequest`, `KycStep`, `KycNext`, `KycStatus`, `LimitWindow`, `WalletLimits`; `IdVerificationStart` removed here.
- **`openapi.proposed.yaml`:** `GET /kyc/status` and `GET /wallets/limits` removed (shipped), `KycStatus` removed; `POST /kyc/international/start` no longer says it mirrors a route that exists. Admin spec files: no change.
- **`api-rfc.md`:** counts to 160 and 32 (29 net-new + 3), §3 table, §4.3, new §5.22, §6.3, §6.3a, §6.6, §7.4, §7.5, §8. **`suggestions.md`:** new §4.15. **`admin-api-rfc.md`:** no change.

---

## 4. Risks

- **The NIN requirement can reach users before the app can send one.** New banking signups would stall without an error, and a support ticket is the only signal. Existing users are protected for 30 days.
- **1002 ended with nothing accepted and no successor sprint.** A sweep like 0902's would mark no-code, mock-only and unmerged work as delivered, and the 36 unfinished leaves have no destination.
- **A limit that is shown and not applied.** The routes report a daily cap, a monthly cap and a maximum balance that nothing enforces. A user, or a regulator reading the screen, would assume they hold. Switching enforcement on later also decides what happens at the end of the grace.
- **A migration rewrote `kyc_level` for every user with a verified BVN**, through an ungated deploy path, and put them all on a 30-day clock.
- **All of mobile's sprint work is on one unreviewed branch**, 91 files, with `main` 15 days behind it. Each day the server moves, the branch has more contract to catch up with. Today's additions are the NIN, the tier and a different limits shape.
- **The funding fix still depends on one environment variable that cannot be seen** (`ANCHOR_POOL_ACCOUNT_ID`), though #100's message is some evidence that funding ran.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Account data going to a third party without a recorded decision or consent is carried and unchanged otherwise.
- **A real charge could be answered with "that isn't yours".** Merchant payments have no dispute path, and the assistant's instructions say otherwise (4 Nov §3.2). Unchanged.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **Done and REVIEW/QA on the board hide open work.** `I381`'s lockout does not exist, so **guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code**, and that token also guards raising a card limit.
- **Every backend repo still deploys or migrates production on push without a test gate**, and two more migrations used it today.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content.
- **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); 0902's 15 removed leaves (not visible); the inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.
- **Withdrawn:** nothing today.

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. Today's change is on the local tier only, and it makes the international gap slightly wider: the proposed `GET /kyc/status` was meant to say which currencies a tier unlocks, and the route that shipped does not, while the only document check the international start was modelled on was deleted. PRD §3.2's "set limits" is still met for card funding only; the tier limits are reported and not applied. The NIN, the Tier 2 and Tier 3 ladder, the seeded CBN figures and the YouVerify field-agent address check are not in the PRD. The consent flag sent with each lookup is the line-10 gap in a new place.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 30 Oct 15:03 → 6 Nov 15:03 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Only `Phoenixdadhev` appears on the backend repos' non-merge commits in this window. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are recomputed on the same reduced file set as 3 to 5 Nov** (the 20 Oct 0902 file is still gone): 0.99 d (n=36), 1.44 d (n=21), 0.89 d (n=3). They did not change, because no item entered review.

### 6.1 Ayomikun Araoye: backend + admin API

**37 commits in 7 days**: 23 in `beevia-api`, 7 in `beevia-admin-api`, 7 in `beevia-db-schema`. **8 own submissions** and 6 moves on other items, all of them on 3 Nov. **One WIP item on 1002**, `I362`, started 2.0 days ago, and its code is merged. Yesterday's and today's merges are a NIN and tier model, a limits route, a card unit fix and two migrations, and none of it is on the board as its own item except `I362`, which is a limit of the board and not a finding about the work. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 53.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct, 16 days ago). **3 on `origin/BVA-I353`** in the window, 9 ahead of `main` in all, the latest 2.2 days ago. **Zero own submissions**: the last was `I286` on 14 Oct, **23.0 days** ago. Two of this window's five "submissions" were board administration's, both on 4 Nov and both on leaves whose code is on the branch. WIP: **2 items**, `I331` at 15.2 days and `I361` at 3.3. One leaf is To do (`I373`). Nothing has been pushed since the card history commit, 52 hours ago. The server contract for his two open items (limits, onboarding) changed under them in the window.

### 6.3 Philip Chidera: design

**One 7-day submission**, `I389`, moved by its parent. **Zero WIP and no leaf left To do**: finished, blocked or working untracked. Worth a question, not an assumption. A NIN screen and its error states (`nin_not_found`, `nin_mismatch`, `nin_already_used`, the attempt limit) are not on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**1 commit**, `64304ef` on 30 Oct, now 7.0 days old. The server has moved further towards the screen: hours, unread counts, the transaction view, a flat article list and a card-limits settings route, none of which the dashboard calls. Nothing has been pushed in response, which after four corrections this report does not read as nothing having been done. The board still shows none of this: `I348` is in REVIEW/QA with no assignee, and `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 53.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (2 Nov → 6 Nov 15:03 UTC) | — | — | **16** | 8 | 6 | 2 |

Rows before W43 are carried from earlier editions, because the 0902 file they came from is gone. W45 is unchanged since yesterday: nothing entered review. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a provider investigation and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Eight of the 16 moves into review in the 7-day window were not made by the owner, and for the mobile ones the code is unmerged.
- **Unpushed and untracked work.** The backend's fixes and the whole tier model are not items on any board.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The commits report test counts, and those were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 5 Nov | Status on 6 Nov |
|---|---|
| **1. Close 1002 deliberately, not by sweep** | ❌ **Not done, and it is now a day late.** No board action on the last day, no successor sprint, filter still 08-01 |
| **2. Decide the seeded card default on the record** | ❌ **Not visible.** Migration 0050 unchanged |
| **3. Confirm `ANCHOR_POOL_ACCOUNT_ID` and run one real funding and reveal** | 🟡 **Some evidence.** #100's message describes three NGN 100 fundings that reached a card, and says nothing about reveal or which environment |
| **4. Decide what a card limit is** | ❌ **No.** `I371`, `I372`, `I385`, `I387` not rewritten |
| **5. Open a PR for `BVA-I353`; fix `data.items` and `in`/`out`** | ❌ **No PR, no commit in 52 hours.** Two more items now belong on it: the NIN step and the limits parser |
| **6. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** No seed or migration touched either |
| **7. Let a merchant payment be disputed; correct the assistant's text** | ❌ **No.** No support code changed |
| **8. Fix the seams (inbox, article list)** | ❌ **No** |
| **9. Run one real chat and one real dispute through the assistant** | ❌ **Not visible** |
| **10. Decide the assistant on the record** | ❌ **Not visible** |
| **11. Bring the dashboard onto the real contract** | ❌ **No commit** (7.0 days) |
| **12. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | ❌ **No** |
| **13. Agree how parent status moves work** | ❌ **No.** No board action at all |
| **14. Assign `I348`, `I349`, `I351`, `I390`; give the admin dashboard a sprint** | ❌ **No** |
| **15. Push on an agent's reply; move "logged" to the activity log** | ❌ **No** |
| **16. Reopen `I392`** | ❌ **No** |
| **17. Close the payments half of blocking** | ❌ **No** |
| **18. `needs: test` on `beevia-api`'s `sync`, verify jobs elsewhere** | ❌ **Not done.** Migrations 0051 and 0052 shipped on the ungated path |
| **19. Generate `openapi.yaml`; stop vendoring the client spec** | ❌ **Not done.** Four additions, two removals and a unit note were made by hand today |
| **20. Handle `call.ended` on the client** | ❌ **Not done** |
| **21. Carried items** | ❌ **None moved** |

**None of twenty-one moved, and one has a little evidence behind it.** The backend's work was real and large, and none of it was on the list: it is the NIN tier model and the card unit fix. Recommendation 1 is the only one that is overdue.

---

## 8. What I would do this week

1. **Close 1002 now, deliberately (carried, overdue).** Accept or return the eleven REVIEW/QA leaves with merged code. Move `I372`, `I386`, `I348` and the eleven branch-only mobile leaves back to In progress. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Hold the NIN requirement back from new users until the app can send one (new).** Either build the NIN step into the onboarding and upgrade flows first, or put the gate behind a switch. Ask design for the screen and its four error states. Decide the order before more users sign up.
3. **Decide whether the tier limits are enforced, and what the end of the grace does (new).** Today they are reported and not applied. If they are to be enforced, say where (send, payout, card funding, inflow above the cap into `kyc_holds`) and what a user whose grace has ended sees. About 6 Dec is the date.
4. **Fix the limits screen to the shipped shape, and read `limits_tier` and `grace_until` (new).** Then move `I362` to review with a real response in hand.
5. **Open a PR for `BVA-I353` (carried).** Fix the `data.items` parsing and `in`/`out`, read `source`, `default_limit` and `spend_included`, handle `card_transfer_failed` and `card_reveal_unavailable`, and test against a response taken from the server. Split it if that gets it merged sooner, with support first.
6. **Decide the seeded card default on the record (carried).** Is NGN 500,000 a day and a month what you want on every card, and should the app say so when a funding is refused?
7. **Confirm `ANCHOR_POOL_ACCOUNT_ID` is set in production and run one real funding and one reveal (carried).** #100's message is a start.
8. **Decide what a card limit is (carried).** Accept funding caps and rewrite `I371`, `I372`, `I385` and `I387`, or ask the provider whether card product configuration can hold limits. The screen must not say "spending limit" while it caps funding.
9. **Record the consent behind each BVN and NIN lookup (new).** The flag is sent as `true` and nothing records it. That is also the first concrete use for the consent line of the rubric.
10. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
11. **Let a merchant payment be disputed, and correct the assistant's text (carried).**
12. **Fix the seams (carried):** the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, the article list's `search` locale and `meta.total`.
13. **Run one real chat and one real dispute through the assistant (carried)**, then pass the dispute's context, force handoff on `didnt_make_this_transaction`, and skip the empty turn.
14. **Decide the assistant on the record (carried).** Who approved it, what the privacy notice says, and whether users are told it is an AI. Add it to the PRD.
15. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add screens for the card-limit default, the article list and, when a route exists, the tier limits.
16. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up`.
17. **Agree how parent status moves work on this board (carried)**, and have board administration move nothing to review without the owner.
18. **Assign `I348`, `I349`, `I351`, `I359` and `I390` (carried, extended)**, and give the admin dashboard a sprint or say the consumer board is its home.
19. **Convert `GET /cards/{id}/transactions` to naira, or retire it for `/activity` (new)** before a client renders it.
20. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried). Order schema changes after the code that stops reading the old ones.
21. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried).
22. **Carried:** send a push when an agent replies; reopen `I392`; close the payments half of blocking; handle `call.ended` on the client; add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 53.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 53 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, and the server now serves only its hours half) and `I351` FAQ CMS (To do, unassigned; API only). No admin route for the tier limits exists, and the dashboard's `/settings` page is still a one-line placeholder. `beevia-admin` last moved 7.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-six days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves, and two of them were considered. **Line 4 (local KYC) holds at 0.90.** The server gained a NIN step, a tier model and a status route, and lost the document check; Tier 3 and the parked-funds mechanism have no code; and the rubric's client half, "the full onboarding/wallet flow", is now worse, because the app cannot complete a banking onboarding against the new contract. Added and removed capability roughly cancel, so the score stays. **Line 6 (multi-currency wallets) holds at 0.85.** `GET /wallets/limits` is a real addition to the wallet surface, but it is NGN only, reports and does not enforce, and the only client for it reads a different shape. It should move when enforcement lands or the branch merges with a matching parser. Line 9 holds at 0.80: the unit fix corrects code that already counted.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound; no translate change |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | NIN step, tier model and `GET /kyc/status` added; document check removed; Tier 3 and holds unbuilt; the app has no NIN step |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only. The route it was modelled on was deleted |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` shipped, NGN only, unenforced, and its client reads another shape |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | Funding, reveal, limits, activity and a default limit on the server; card amounts now read in the right unit. Client card management on unmerged `BVA-I353`; verification model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item. The lookups assert consent as a constant |
| 11 | Admin oversight | 6 | 0.97 | 0 | No change. No role holds `disputes`; the screens still run on a mock; no admin route for the tier limits |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the NIN and tier changes are live in production**, and whether `YOU_VERIFY` is configured for the NIN endpoint. Merge times and release tags are known, and workflow results are not.
- **Whether new banking users are stalling today.** That follows from the code and the client's missing calls; nothing was run, and no signup data is visible.
- **Whether migration 0051 has run**, and when, which decides the date the grace ends.
- **Whether the funding and reveal fixes work in production.** Their commits report sandbox checks, and #100's message suggests a funding ran somewhere.
- **Whether the seeded default was a decision.** No ticket or comment on the board mentions it, and the same holds for the seeded Tier 2 figures.
- **Whether the provider could offer card limits through card product configuration or a commercial agreement.**
- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, and whether a real model call succeeds.
- **Who decided on the assistant, on funding caps, or on the consent flag, and whether a privacy or legal review happened.** No record is visible here.
- **Whether any role was granted `disputes` or `help_center` by hand**, or whether the Super Admin role in production has `system_settings`.
- **Whether the commit-reported tests pass, or whether anything renders.** Nothing was executed.
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **Whether a server-side attempt limit exists at a proxy** in front of the API.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint lists from the `__nonexistent__` dry run for both projects, run first: Beevia `['1002', '0902', '0901', '08-01', '0702', '0701']`, admin `['0901-admin']`. Then three background exports starting at about 14:50 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 5 Nov. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical to 5 Nov.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-06`: exit 1 before spec edits, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow06.py`, adapted from 5 Nov's): a diff of 1002 against 5 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA.
5. Content checks. `git fetch` (by the sync), `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`: the KYC, upgrade, wallet-limits and card diffs, in full, and the file list of the whole range. In `beevia-db-schema`: migrations 0051 and 0052. In `beevia-mobile`: `origin/main` and `origin/BVA-I353` searched for the NIN routes, the status and limits routes and the Entrust routes, and `wallet_limits.dart` read. `grep` over the shadow for `kyc_tier_limits`, `kyc_holds`, `OutflowService` and `isSubjectConsent`.
6. Spec and narrative updates (§3.5).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-06.html`, `web-report/index.html`, `openapi.yaml`, `openapi.proposed.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 6 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The 20 Oct 0902 scratch file is gone from `/tmp`**, so median cycle times have lower n and are not comparable with editions before 3 Nov. The older rows of the weekly table are carried.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 5 Nov 15:01 UTC → 6 Nov 15:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (the machine's clock is MDT).
