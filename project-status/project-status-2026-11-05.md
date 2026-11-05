# Beevia — Project Status

**As of 2026-11-05** · Sprint **1002** (21 Oct → 5 Nov, **day 16 of 16, its last day**): **63 items, 44 leaves: 1 To do · 3 In progress · 32 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-05.csv` + `beevia-activity-2026-11-05.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-05.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 4 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. The commit messages of the day's merges were read as the authors' own account, and none of their production claims could be checked.

Scope: five boards, kept separate and never summed. **Window: 4 Nov 15:01 UTC → 5 Nov 15:01 UTC, 1.0 day (Wed → Thu).**

---

## Quick overview

> **The server fixed what had been failing against the real card provider, and the day's other change is a default that quietly caps every card. Today's merges fix card funding and card reveal, which the commits say did not work against the real provider, and seed a NGN 500,000 daily and monthly funding cap that applies to every card from deploy. The app still has none of it on `main`: nothing from mobile has merged in 14 days and no PR exists for the branch that holds all of it. 1002 ends today with 32 of 44 leaves in review, 11 of them with merged code, none accepted, and no successor sprint.**

| Metric | 4 Nov | 5 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 2 / 4 / 30 / 0 / 8 | **1 / 3 / 32 / 0 / 8** | 2 into REVIEW/QA, 1 started |
| Board actions on 1002 in the window | 8 | **4** | all on 4 Nov between 16:04 and 16:13 UTC, 1 to 12 minutes after the last edition's cut-off. None today |
| Transitions into REVIEW/QA, last 7 days (leaves) | 16 | **16** | 8 by the leaf's owner (Ayomikun), 6 moved by Ayomikun on others' items, **2 by board administration on David's** |
| Owners' last submission of their *own* leaf | 3 Nov 16:04 UTC (Ayomikun, `I387`) | **3 Nov 16:04 UTC** (unchanged) | David's last own submission is 14 Oct, **22.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 11 of 30 | **11 of 32** | the two new ones are mobile, code only on the branch |
| Routes in code but not in the spec (consumer / admin), before today's edits | 3 / 3 | **0 / 3** | now **0 / 0**: specs updated |
| API surface (consumer / admin) | 158 / 72 | **158 / 75** | +0 / +3. Eight consumer operations changed in place |
| Proposed operations (consumer / admin) | 34 / 18 | **34 / 18** | |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | |
| `beevia-admin` days since a commit | 5.0 | **6.0** | |
| `beevia-mobile` days since a commit on `main` | 13.2 | **14.2** | `BVA-I353` unchanged (`f46641f`, 1.2 d ago), still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.2 / 1.0 / 0.2 | **0.0 / 0.0 / 0.0** | 8 merges + 1 release since the last edition |
| Admin board: open sprint / days since any activity | none / 51.0 | **none / 52.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67%** (67.32) | **0**: the day's card changes have no client on `main` |

**One qualification to 4 Nov, not a correction.** That edition and earlier ones read the card routes from code and scored them on that basis, and said nothing had been run. #97 and #95 now say that funding and reveal were failing against the provider (§3.1). No claim in 4 Nov was contradicted, but the card line's 0.80 was a statement about code that had not yet met the provider, and it should be read that way. **No item from 4 Nov was withdrawn.**

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (1 In progress, 15 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **8 own** (+6 moves on other items) | 1.44 d (n=21) | `I362` (1.0 d) · `BVA-I8` on 0901-admin (**52.0 d**) | **33** (21 `beevia-api`, 7 `beevia-admin-api`, 5 `beevia-db-schema`) | The card stories ask for something the provider does not offer, and `I372` shows REVIEW/QA with no code. Both need a decision |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | 5 (**0 own**, 3 moved by Ayomikun, 2 by board administration) | 0.99 d (n=36) | 2: `I331` (**14.2 d**), `I361` (2.3 d) | **0 on `main`** · **3 on `BVA-I353`** | 11 leaves in review, all on one unmerged branch with no PR. `I331` is 14 times the median |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (moved by Ayomikun) | 0.89 d (n=3) | none | n/a | Zero WIP and nothing left To do: what is next? |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**52.0 d**) | **1** (`beevia-admin`, 68 files) | The server gained a flat article list and a settings route for a screen that has not started. No commit in 6.0 days, and this may be unpushed |

**The three questions for standup:** (1) **What happens to 1002 today?** 36 leaves are not Done, there is no successor sprint, and the one precedent is a sweep that marked unbuilt work Done. (2) **Is a NGN 500,000 default funding cap on every card what you meant, and is `ANCHOR_POOL_ACCOUNT_ID` set in production?** One is a behaviour change on deploy, the other decides whether the funding fix works at all. (3) **When does `BVA-I353` get a PR?** Eleven reviewed leaves, the whole mobile half of the sprint, depend on that one branch.

**The three things worth knowing:**

1. **Card funding and reveal were failing against the provider, and the fixes landed today.** #97 says all three production fundings so far failed with "Insufficient balance", because the transfer drew on the user's own account when customer money sits in the organisation's pool. It now draws on `ANCHOR_POOL_ACCOUNT_ID`, and when that is unset it falls back to the old account, which restores the failure silently. #95 says every card reveal failed with a `401`, because the code called a path that is not a provider route, and moves it to the documented one. Both commits report a sandbox check. Nothing here could check production, and the app on `main` has no card code to use any of it (§3.1).

2. **Every card now has a funding cap nobody was told about.** Migration 0050 seeds NGN 500,000 a day and a month, and funding now applies the card's own limit, else that default. A card that had no cap yesterday has one on deploy, and a single funding between 500,000 and 1,000,000 that was allowed is now refused. Sending `null` to `PATCH /cards/{id}/limits` used to remove the limit and now brings the default back, so the user can no longer choose "no limit". The app on the branch does not read `source` or `default_limit`, and does not read `/limits` at all. The default is editable through two new admin routes that have no screen (§3.2, `suggestions.md` §4.14).

3. **The board is being moved to review ahead of the code, again, one day before the sprint ends.** Board administration moved `I354` and `I357`, and their parent `I353`, to REVIEW/QA 1 to 12 minutes after yesterday's cut-off. Their code is on `origin/BVA-I353` and nowhere else, and that branch has no PR. That is 32 of 44 leaves in review, 11 with merged code, 11 on the branch, 3 with no matching code, and 4 design items whose files are not in git. Nothing has ever left review on 1002 (§1.3, §2).

**If you read nothing else:** today is the sprint's last day, and the review column is the only thing standing between 36 unfinished leaves and a sweep. If it is swept as 0902 was, `I372` (no code), `I386` and `I348` (mock only) will read as delivered, along with eleven screens nobody has merged.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were not re-exported. The 08-01 and 0901-admin sidecars are byte-identical to 4 Nov, and the CSVs differ only in the export date. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project, checked at about 15:00 UTC today: **no successor to 1002 exists, and it ends today.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged.

| Time (UTC) | Items | Move | Made by | Reading |
|---|---|---|---|---|
| 4 Nov 16:04:30 | `I362` | To do → In progress | Ayomikun | Own. The limits-and-usage endpoint (tier, limits, today's usage). Nothing on `origin/main` serves a tier or `/users/me/limits`, which is still proposed only |
| 4 Nov 16:10:43 | `I357` | In progress → REVIEW/QA | Board administration | David's leaf. Wallet Details screen. Code only on `origin/BVA-I353` |
| 4 Nov 16:13:13 | `I353` (parent), `I354` | In progress → REVIEW/QA | Board administration | Parent and child within 3 ms. `I354` is the More Options sheet and navigation, code only on the branch. It had been In progress for 13.3 days |

These came 1 to 12 minutes after the last edition's cut-off, the same pattern as 6 and 15 Oct, when board administration moved items to review at about 16:00 UTC, after the edition's cut-off. The parent move is inferred from timing, as no comment records intent, and makes **nine** parent moves since 30 Oct. **No comments in the window, and none on 1002 ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002.**

Board actions per day on 1002:

| 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov | 4 Nov | 5 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 17 | 16 | 6 | 6 | 0 | 0 | 5 | **23** | **4** | **0** |

4 Nov's row read 0 in yesterday's edition, which stopped at 15:01 that day.

### 1.3 What the last day of 1002 holds

1002 ends **today, Thursday 5 Nov**. 36 of its 44 leaves are not Done: 32 in REVIEW/QA, 3 In progress (`I331`, `I361`, `I362`), 1 To do (`I373`, reflect card spending in the app). The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. A sweep today would mark Done work that has no merged code (§2) and would not say so.

---

## 2. Sprint 1002: what is in review, and whether the code exists

| REVIEW/QA leaves (32) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **11** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391` | Routes on `origin/main`. `I387` caps funding, not spending, and has no maximum for the user (the new default is a default, not a maximum). `I391` asks for pagination, search, filter and the Activity tab's query logic, and has none of them |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | **11** | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390` | Unmerged, no PR. `I354` and `I357` are new today. `I390` is unassigned and its list would be empty (4 Nov §3.4) |
| Moved to review, no matching code | 3 | `I348`, `I386`, `I372` | `I348`: mock only, and its server table is gone. `I386`: nothing on the branch calls `/limits`. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen), `I383` (client on the branch) and `I384`. All unchanged.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review. The server gained a flat article list today for that dashboard (§3.3), and the dashboard still has no screen.
- **`origin/BVA-I353`:** 9 ahead, 4 behind `main`, 91 files, +13,526/−134. Last commit `f46641f` *card history, dispute events* (4 Nov 10:13 UTC), unchanged since the last edition. **No PR.** `refs/pull/53`–`55` are dependabot branches, and `#52` was `BVA-I316`, merged on 22 Oct.
- **WIP ages:** `I331` 14.2 d, `I361` 2.3 d, `I362` 1.0 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edits.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-05`), it first reported 3 admin routes undocumented (exit 1). After the spec changes: 158/158 consumer, 75/75 admin, proposed 34/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 68 phantom lines from the three `diverged` working trees (27 consumer + 41 admin "in spec, not in code"), and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` `main` | `6c69dbc` → `5b988c1` | #31, **v0.0.50**: `card_settings` table, seeded NGN 500,000 / 500,000 |
| `beevia-api` `main` | `bc7da11` → `5bd0b30` | #95 missing message keys, reveal route, statement start day. #96 statement redesign. #97 fund from the pool, cardholder name. #98 top-up reconciliation. #99 default limits. +1,795/−247 across 36 files |
| `beevia-admin-api` `main` | `59e03f9` → `a7cb08b` | #29 flat article list. #30 default card limits. +1,270/−17 |
| `beevia-mobile` `BVA-I353` | `f46641f` | Unchanged. Unmerged (§2) |

`beevia-admin` (`64304ef`, 30 Oct) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. All eight merges landed between 03:59 and 14:57 UTC today, so this edition covers more than the window's hours.

### 3.1 Funding, reveal and the pool

- **Funding drew on the wrong account.** #97 says each deposit is swept into the organisation account, so the user's own Anchor account is empty by design. Card transfers used it, Anchor accepted each as `PENDING` and then failed it with "Insufficient balance", and the wallet debit was reversed. The commit says all three fundings so far failed this way in production while the wallet held NGN 25,600, and that NGN 100 each way worked in sandbox. Transfers now use `ANCHOR_POOL_ACCOUNT_ID`, falling back to the user's account if unset, **and that covers withdrawals too, so a withdrawal's money now returns to the pool.** The variable is already used by payouts. Whether it is set in the production env file cannot be seen.
- **The response now waits for the verdict.** Up to 5 s, polled every 250 ms, then `status` is `completed`, or `400 card_transfer_failed` with a refund, or `pending`. Anchor settles in about a second, per the commit.
- **Reveal called a route that does not exist.** `fetchCardDetails` took a card id and called `/cards/{id}/details`. The commit says that is not a provider route, that **every reveal came back `401`** and reached the app as a bare "Internal server error", and that it checked sandbox with a real token (old route `401`, new route `200`). It now calls `/cards/details` with the token, which is how the provider identifies the card. A partner failure is `503 card_reveal_unavailable`.
- **`cardholder_name`** is now on every card view and on reveal. `BVA-I353`'s `virtual_card.dart` already reads `cardholder_name`, so the client was ahead of the server on this one field.
- **Not changed:** the funding check can still be raced (`suggestions.md` §4.13.8), and the new default adds a read to it.

### 3.2 Default card limits

`GET /cards/{id}/limits` now reports each window's `limit` as the one in force, plus `source` (`card`, `default`, `none`) and `default_limit`. `assertFundingAllowed` applies `card.dailyLimit ?? default`.

- **It is a change on deploy.** The seed row is 500,000 / 500,000, and per-transfer maximum is 1,000,000. Every card with no limit of its own is capped now, with no notice and no message the app can show, since the branch's limits code is absent.
- **`null` changed meaning.** It clears the card's own limit so the default applies. Nobody can opt out of the default, only exceed it with a larger limit of their own.
- **The admin routes are unaudited.** `PUT /admin/settings/card-limits` records the last editor and nothing before it, and the dashboard has no screen for it (§3.3).
- **Still funding caps.** The routes' text says so, as before. The stories (`I371`, `I372`, `I385`, `I387`) still ask for spending control and still cannot be met on this provider as written. Today's change moves nothing on the decision 4 Nov asked for.

### 3.3 Admin API

- **`GET /admin/help/articles`** (#29): every article across categories, paged, with votes, search, filters and four sorts. `most_unhelpful` is the one the help centre is run on. Two seams from reading it: `search` matches any translation's title, not the title in `locale` as documented, so a match on another language reads as `title: null`; and `meta.total` ignores `untranslated`, so those pages run short (`suggestions.md` §4.14).
- **`GET`/`PUT /admin/settings/card-limits`** (#30). Replaces both in one save, daily not above monthly, `system_settings:view` / `:edit`. **That module has existed since v0.0.20, and the seed script grants every module to Super Admin**, so unlike `help_center` and `disputes` this one is probably reachable today. Whether production's role was seeded before or after is not visible. `beevia-admin`'s `/settings` page is a one-line placeholder.

### 3.4 Top-ups and statements

- **Top-ups (#98).** Paystack reports `abandoned` for any unpaid checkout, so the old code closed a top-up as unpaid at its first look and then ignored a later payment. Now the close waits 30 minutes, a late payment is still credited, and a sweep every 10 minutes (BullMQ, `topup-reconcile`) settles ones nobody returned to. A user who walks away now sees `pending` for up to half an hour.
- **Statements (#96).** Rows are titled as the app's history titles them, the sender's note sits on its own line, there is an opening and closing balance, and a wallet statement carries the virtual account number. The opening day is a valid start. The PDF is still encrypted with the account's phone number (4 Nov §4.8 and the delivery model are unchanged).
- **#95** adds 26 i18n keys that reached users as raw keys, in four languages, and a test.

### 3.5 The inbox: what is left

Unchanged. The diff touched no support, guard or auth file in either API. **No role holds `disputes`**, and every inbox route still returns `403`. The mock is still the dashboard's default. The assistant's gaps, the `transactionType` filter, the missing payment lookup, `unreadOnly` and the unvalidated `timezone` all stand as 4 Nov described them (§4.13 items 5 to 9 of `suggestions.md`).

### 3.6 The app against the new contract

`BVA-I353` did not move. Of the day's server changes it handles `cardholder_name` and nothing else: it does not read `source`, `default_limit` or `card_transfer_failed`, and it never calls `/cards/{id}/limits`. Its card history still takes rows only when `data` is a list, and the server still sends `data.items`. Reveal, unfreeze and terminate still send no card PIN. **The limits screen (`I361`, `I386`) is therefore not wired to anything.** `call.ended` is still unhandled on `main` and on the branch.

### 3.7 Document changes this cycle

- **`openapi.yaml`:** no operations added. In place: `GET`/`PATCH /cards/{cardId}/limits` (the limit in force, `source`, `default_limit`, the meaning of `null`), `fund` and `withdraw` (5 s wait, `card_transfer_failed`, the pool), `reveal` (`503 card_reveal_unavailable`), `GET /topups/{reference}` (30-minute window), `POST /statements` (opening day, titles, note), `Card` and `CardSecrets` (`cardholder_name`), `CardLimitWindow`.
- **`openapi.admin.yaml`:** +3 (`GET /admin/help/articles`, `GET`/`PUT /admin/settings/card-limits`), a new `Admin Settings` tag, and three schemas. Proposed files: no change.
- **`api-rfc.md`:** new §5.21. **`admin-api-rfc.md`:** counts to 75 and fifteen controllers, §3.15 to twelve routes, new §3.17. **`suggestions.md`:** new §4.14.

### 3.8 The standing checks

- **Pipelines:** no workflow file changed in any of the three repos since 4 Nov. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`" and `sync` still migrates before `deploy`; `beevia-admin-api`'s `sync.yml` still triggers on push; db-schema's release published v0.0.50 within a minute of the merge. All three still deploy or migrate on push with no test gate. **Migration 0050 shipped on that path today.**
- `PaymentService.activeNgn()`, `StubTranslateAdapter`, unmapped `22P02`, unindexed `messages.ref_id`, FAQ search's missing `en-US` fallback, and no grant of `help_center` or `disputes`: all unchanged.
- `POST /auth/step-up`: no attempt limit, and no throttler anywhere in `src`. It still guards `PATCH /cards/{id}/limits`.
- **Mobile:** `main` unchanged. **`call.ended` is still unhandled.** The biometric step-up is unchanged.

---

## 4. Risks

- **1002 ends today with nothing accepted and no successor sprint.** A sweep like 0902's would mark no-code, mock-only and unmerged work as delivered, and the 36 unfinished leaves have no destination.
- **A behaviour change reached production's deploy path without an announcement.** Every card is now capped at NGN 500,000 a day and a month on deploy, and the app cannot say why a funding is refused (§3.2).
- **The funding fix depends on one environment variable that cannot be seen.** If `ANCHOR_POOL_ACCOUNT_ID` is unset, funding falls back to the account that the commit says always fails.
- **All of mobile's sprint work is on one unreviewed branch**, 91 files, with `main` 14 days behind it. Each day the server moves, the branch has more contract to catch up with, and today's `source` and `default_limit` are the latest.
- **A real charge could be answered with "that isn't yours".** Merchant payments have no dispute path, and the assistant's instructions say otherwise (4 Nov §3.2). Unchanged.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **Account data going to a third party without a recorded decision or consent.** Unchanged.
- **Done and REVIEW/QA on the board hide open work.** `I381`'s lockout does not exist, so **guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code**, and that token also guards raising a card limit.
- **The inbox's mock is on by default**, and switching it off naively would show an unfiltered queue or an error.
- **Every backend repo still deploys or migrates production on push without a test gate**, and today's migration used it.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content. The server now has the list and search the dashboard will need, and the dashboard has no screen.
- **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.
- **Withdrawn:** nothing today.

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. PRD §3.2 says users "want to set limits", and today's default and the card's own limits meet that for funding only. The PRD does not say a limit must stop a purchase, so the funding cap may be acceptable. The stories are what say so. A configurable platform default is not in the PRD, and the seeded 500,000 has no source in it. The AI assistant is still outside the PRD. `pending_partner`, `partner_reference` and `sla_due_at` are still unbuilt.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 29 Oct 15:01 → 5 Nov 15:01 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Only `Phoenixdadhev` appears on the backend repos' non-merge commits in this window. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are recomputed on the same reduced file set as 3 and 4 Nov** (the 20 Oct 0902 file is still gone): 0.99 d (n=36), 1.44 d (n=21), 0.89 d (n=3). Each new cycle is a parent move or a board-administration move, so read these with care.

### 6.1 Ayomikun Araoye: backend + admin API

**33 commits in 7 days**: 21 in `beevia-api`, 7 in `beevia-admin-api`, 5 in `beevia-db-schema`. **8 own submissions** and 6 moves on other items, all of them on 3 Nov. **One WIP item on 1002** (`I362`, started yesterday). The day's merges are mostly fixes against the real provider and real users: funding, reveal, raw message keys, abandoned top-ups, statements. None of them is on the board as an item, which is a limit of the board and not a finding about the work. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 52.0 days. `I387` went to review 19 hours before its code merged, through its parent, as 4 Nov said.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct, 15 days ago). **3 on `origin/BVA-I353`** in the window, 9 ahead of `main` in all, the latest yesterday at 10:13 UTC. **Zero own submissions**: the last was `I286` on 14 Oct, **22.0 days** ago. Two of this window's five "submissions" were board administration's, both yesterday and both on leaves whose code is on the branch. WIP: **2 items**, `I331` at 14.2 days and `I361` at 2.3. One leaf is To do (`I373`). Nothing has been pushed to the branch since the card history commit, 29 hours ago.

### 6.3 Philip Chidera: design

**One 7-day submission**, `I389`, moved by its parent. **Zero WIP and no leaf left To do**: finished, blocked or working untracked. Worth a question, not an assumption. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**1 commit**, `64304ef` on 30 Oct, now 6.0 days old. The server has moved further towards the screen: hours, unread counts, the transaction view, and today a flat article list and a settings route, none of which the dashboard calls. Nothing has been pushed in response, which after four corrections this report does not read as nothing having been done. The board still shows none of this: `I348` is in REVIEW/QA with no assignee, and `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 52.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (from Mon 2 Nov, to 5 Nov 15:01 UTC) | — | — | **16** | 8 | 6 | 2 |

Rows before W43 are carried from earlier editions, because the 0902 file they came from is gone. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a provider investigation and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Eight of the 16 moves into review in the 7-day window were not made by the owner, and for the mobile ones the code is unmerged.
- **Unpushed and untracked work.** The day's fixes are the largest example: they are not items on any board.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The commits report test counts, and those were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 4 Nov | Status on 5 Nov |
|---|---|
| **1. Close 1002 deliberately, not by sweep** | ⏳ **Due today.** No successor sprint, nothing has left review, and two more leaves went in. The filter is still 08-01 |
| **2. Decide what a card limit is** | 🟡 **Moved the other way.** #99 extends the funding cap with a platform default. The stories `I371`, `I372`, `I385`, `I387` were not rewritten, and no one has taken the question to the provider on the record |
| **3. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** No migration or seed granted either |
| **4. Let a merchant payment be disputed; correct the assistant's text** | ❌ **No.** No support code changed |
| **5. Open a PR for `BVA-I353`; fix `data.items` and `in`/`out`** | ❌ **No PR, no commit in 29 hours** |
| **6. Fix the inbox's seams** | ❌ **No.** Nothing in `support/` changed |
| **7. Run one real chat; pass the dispute's context** | ❌ **Not visible** |
| **8. Decide the assistant on the record** | ❌ **Not visible** |
| **9. Bring the dashboard onto the real contract** | ❌ **No commit** (6.0 days) |
| **10. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | ❌ **No** |
| **11. Agree how parent status moves work** | ❌ **No.** A ninth parent move, this time by board administration |
| **12. Assign `I348`, `I349`, `I390`; give the admin dashboard a sprint** | ❌ **No** |
| **13. Push on an agent's reply; move "logged" to the activity log** | ❌ **No** |
| **14. Reopen `I392`** | ❌ **No** |
| **15. Close the payments half of blocking** | ❌ **No** |
| **16. `needs: test` on `beevia-api`'s `sync`, verify jobs elsewhere** | ❌ **Not done.** A migration shipped on the ungated path today |
| **17. Generate `openapi.yaml`; stop vendoring the client spec** | ❌ **Not done.** Today's contract changes are the next case for it |
| **18. Handle `call.ended` on the client** | ❌ **Not done** |
| **19. Carried items** | ❌ **None moved** |

**None of nineteen moved, and one went the other way.** The day's work was real and large, and none of it was on the list: it was the team fixing what broke against the provider. Moving recommendation 1 to today is the only change in the table.

---

## 8. What I would do this week

1. **Close 1002 deliberately today (carried, due).** Accept or return the eleven REVIEW/QA leaves with merged code. Move `I372`, `I386`, `I348` and the eleven branch-only mobile leaves back to In progress. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Decide the seeded default on the record (new).** Is NGN 500,000 a day and a month what you want on every card from deploy, and should the app say so when a funding is refused? If not, change the seed in a follow-up migration before more cards are funded.
3. **Confirm `ANCHOR_POOL_ACCOUNT_ID` is set in production and run one real funding and one reveal (new).** The commits say sandbox only. A real funding is the only evidence that the first fix works, and an unset variable would put funding back where it was.
4. **Decide what a card limit is (carried, changed).** Accept funding caps and rewrite `I371`, `I372`, `I385` and `I387`, or ask the provider whether card product configuration can hold limits. The screen must not say "spending limit" while it caps funding.
5. **Open a PR for `BVA-I353` (carried).** Fix the `data.items` parsing and `in`/`out` first, read `source`, `default_limit` and `spend_included`, handle `card_transfer_failed` and `card_reveal_unavailable`, and test against a response taken from the server. Split it if that gets it merged sooner, with support first.
6. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).** It is the last server-side step before anyone can answer a thread.
7. **Let a merchant payment be disputed, and correct the assistant's text (carried).**
8. **Fix the seams (carried, extended):** the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, the article list's `search` locale and `meta.total`.
9. **Run one real chat and one real dispute through the assistant (carried)**, then pass the dispute's reason, reference and snapshot, force handoff on `didnt_make_this_transaction`, and skip the empty turn.
10. **Decide the assistant on the record (carried).** Who approved it, what the privacy notice says, and whether users are told it is an AI. Add it to the PRD.
11. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, cut `/support/triage-config` down to hours, and add a screen for the card-limit default and the article list.
12. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up`.
13. **Agree how parent status moves work on this board (carried).** Move children first, or do not let a parent's move carry them, and have board administration move nothing to review without the owner.
14. **Assign `I348`, `I349`, `I351` and `I390` (carried, extended)**, and give the admin dashboard a sprint or say the consumer board is its home.
15. **Send a push when an agent replies, and move "logged" to the admin activity log (carried).**
16. **Reopen `I392`** until its boxes reflect what was verified (carried).
17. **Close the payments half of blocking** (`suggestions.md` §4.9) (carried).
18. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried). Order schema drops after the code that stops reading them.
19. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried).
20. **Handle `call.ended` on the client** (carried).
21. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 52.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 52 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, and the server now serves only its hours half) and `I351` FAQ CMS (To do, unassigned; API only, with a flat list added today). `beevia-admin` last moved 6.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-five days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. Line 9 is the one to explain: the server fixed funding and reveal against the provider, added `cardholder_name` and a default limit, but no client on `main` calls any card route, and the limits are not the spending limits the stories describe. Fixes to code that already counted do not add capability, and its 0.80 stays. It should move when `BVA-I353` merges with those calls working. Line 11 holds at 0.97: three more admin routes, still no role that can open the inbox and no wired screen.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound; no translate change |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed; top-up and statement fixes add no capability |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | Funding, reveal, limits, activity and a default limit on the server; the commits say funding and reveal did not work against the provider until today. Client card management on unmerged `BVA-I353`; verification model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | 3 more routes (article list, card-limit defaults). No role holds `disputes`; the screens still run on a mock; no screen for the new routes |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the funding and reveal fixes work in production.** Their commits report sandbox checks. Whether `ANCHOR_POOL_ACCOUNT_ID` is set, and whether any real funding has since succeeded, is not visible here.
- **Whether the seeded default was a decision.** The migration comment says "until per-KYC-tier defaults replace it", and no ticket or comment on the board mentions it.
- **Whether the provider could offer card limits through card product configuration or a commercial agreement.** Only its public docs were read on 4 Nov, and they do not cover that.
- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, and whether a real model call succeeds.
- **Who decided on the assistant, or on funding caps, and whether a privacy or legal review happened.** No record is visible here.
- **Whether the migrations have run in production.** Merge times and a release tag are known, and workflow results are not.
- **Whether any role was granted `disputes` or `help_center` by hand**, or whether the Super Admin role in production has `system_settings`.
- **Whether the commit-reported tests pass, or whether anything renders.** Nothing was executed.
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **Whether a server-side attempt limit exists at a proxy** in front of the API.
- **Whether a production build of `beevia-admin` exists**, and with which flag.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items today.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run as three background calls starting at about 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 4 Nov. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0. The sprint lists came from the `__nonexistent__` dry run, run first.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-05`: exit 1 before spec edits, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`q05.py`, `flow05.py`, `win05.py`): a diff of 1002 against 4 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA.
5. Content checks. `git fetch` (by the sync), `for-each-ref` and `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`: the card, funding, limits, topup, anchor and statement diffs, in full. In `beevia-admin-api`: the settings, card-limit defaults and help-center diffs. In `beevia-db-schema`: migration 0050 and `cards.ts`. In `beevia-mobile`: `origin/BVA-I353` searched for the card and limits contract, and for the files behind `I354` and `I357`. The commit messages of #97 were read for the production account.
6. Spec and narrative updates (§3.7).
7. This report and its web edition.
8. End-of-run recheck: see the note under Window.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-05.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 5 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The 20 Oct 0902 scratch file is gone from `/tmp`**, so median cycle times have lower n and are not comparable with editions before 3 Nov. The older rows of the weekly table are carried.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The Anchor documentation was not re-read today.** The production account of funding and reveal is the commit author's.

**Window.** 4 Nov 15:01 UTC → 5 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (the machine's clock is MDT). **End-of-run recheck:** at 15:08 UTC a fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 4 Nov 16:13 UTC, and `ls-remote` showed every `main` and `BVA-I353` at the commits read above, with no new PR on any repo.
