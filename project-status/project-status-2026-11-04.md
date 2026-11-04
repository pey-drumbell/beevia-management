# Beevia — Project Status

**As of 2026-11-04** · Sprint **1002** (21 Oct → 5 Nov, day 15 of 16): **63 items, 44 leaves: 2 To do · 4 In progress · 30 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-04.csv` + `beevia-activity-2026-11-04.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-04.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 3 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. The card provider's public docs were read to check one claim (§3.1).

Scope: five boards, kept separate and never summed. **Window: 3 Nov 15:01 UTC → 4 Nov 15:01 UTC, 1.0 day (Tue → Wed).**

---

## Quick overview

> **Both sides of support and cards moved again, and the gaps have narrowed to specific items. The app's real chat client arrived on its branch on the new contract, opening hours are fixed, and the server gained card limits and a single card history. Three things still stop users benefiting: nothing from mobile has reached `main` in 13 days, no admin role can open the inbox, and the card stories ask for spending controls the provider does not appear to offer. 1002 ends tomorrow with 30 of 44 leaves in review, 11 of them with merged code, none accepted, and no successor sprint.**

| Metric | 3 Nov | 4 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 6 / 6 / 24 / 0 / 8 | **2 / 4 / 30 / 0 / 8** | 6 into REVIEW/QA |
| Board actions on 1002 in the window | 20 | **8** | all on 3 Nov at 16:04 UTC, 52 minutes after the last edition's recheck. None today |
| Transitions into REVIEW/QA, last 7 days (leaves) | 14 | **16** | 9 by the leaf's owner (Ayomikun), 7 moved by Ayomikun on David's, Philip's and unassigned items |
| Owners' last submission of their *own* leaf | 3 Nov 13:52 UTC | **3 Nov 16:04 UTC** (Ayomikun, `I387`) | David's last own submission is 14 Oct, **20.9 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 9 of 24 | **11 of 30** | `I387` and `I391` added, each narrower than its description |
| Routes in code but not in the spec (consumer / admin), before today's edits | 6 / 9 | **3 / 3** | now **0 / 0**: specs updated |
| API surface (consumer / admin) | 155 / 69 | **158 / 72** | +3 / +3 |
| Proposed operations (consumer / admin) | 34 / 18 | **34 / 18** | |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | |
| `beevia-admin` days since a commit | 4.0 | **5.0** | |
| `beevia-mobile` days since a commit on `main` | 12.2 | **13.2** | `BVA-I353` moved: `f46641f`, 0.2 d ago, still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.0 / 0.0 / 0.1 | **0.2 / 1.0 / 0.2** | 6 merges since the last edition |
| Admin board: open sprint / days since any activity | none / 50.0 | **none / 51.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: the new card and hours routes have no client on `main` |

**One correction to 3 Nov.**

1. **"The app has no chat client" should have read "nothing pushed".** That edition's headline said so, and `f46641f` arrived about 19 hours later with a working chat client, 3,841 lines across 43 files. Some of that work was very likely under way when the sentence was written. It is the fourth time this report has read silence as absence, after mobile on 27 Oct, `beevia-admin` on 30 Oct and the server on 2 Nov.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (1 To do, 15 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **9 own** (+7 moves on other items) | 1.44 d (n=21) | none on 1002 · `BVA-I8` on 0901-admin (**51.0 d**) | **24** (13 `beevia-api`, 6 `beevia-admin-api`, 5 `beevia-db-schema`) | `I372` shows REVIEW/QA with no code, and #94 says it cannot be built on this provider. It needs a decision, not more work |
| David Samuel | mobile | **1002: 16** (1 To do, 4 In progress, 9 REVIEW/QA, 2 Done) · `I392` shared | 4 (**0 own**, 4 moved by Ayomikun) | 0.98 d (n=34) | 4: `I331`, `I354` (**13.2 d**), `I357`, `I361` (1.3 d) | **0 on `main`** · **4 on `BVA-I353`** | The branch is now 91 files and moving fast, with no PR. Card history would be empty against the real server |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (moved by Ayomikun) | 0.89 d (n=3) | none | n/a | Zero WIP and nothing left To do: what is next? |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**51.0 d**) | **1** (`beevia-admin`, 68 files) | The server has moved further towards the screen, including hours. No commit in 5.0 days, and this may be unpushed |

**The three questions for standup:** (1) **What is a card limit?** Accept funding caps and rewrite `I372`, `I385` and `I387`, or take the requirement to the provider. (2) **Who grants `disputes`, and who goes on duty?** That is now the one thing stopping the inbox, and support reads offline until it happens. (3) **What happens to 1002 tomorrow, and when does `BVA-I353` get a PR?** The whole mobile half of the sprint is on that one branch.

**The three things worth knowing:**

1. **The card stories ask for something the provider does not appear to offer.** `I372` asks to approve or decline card payments in real time, and `I385`/`I387` ask for limits "enforced on card spending" and applied at the provider. #94 says the provider has no spend controls and no authorization hook, so it capped funding instead and labelled it so (`enforced_on: "funding"`). The public docs agree as far as they go: the description is "the only card attribute that can be changed after creation", and `cardPayment.*` events report what has already happened. Card product configuration is not visible there. The engineering here is careful and honestly named. The decision belongs to the product side, and until it is made these items show REVIEW/QA against descriptions they cannot meet (§3.1).

2. **"Card disputes" do not reach a merchant payment.** #92's commit says card disputes were impossible and are now covered, naming `card_transfers` as "spending from a card". The schema defines that table as wallet↔card movements, and `card_topups` as funding the *wallet* by bank card. So "my card was charged twice" still returns `404`, and the assistant is told its lookup covers card spending and that "not found" means the reference is not the user's. That is the case most likely to be a fraud report, and the fix looks small: the schema already allows a reference with no foreign key, and the provider call already exists (§3.2).

3. **Today's new code has seams, and each side's tests cannot show them.** The app's card history expects a list and the server sends `data.items`, so a used card would look unused, and the branch's mock returns the list it expects. On the server, the inbox's `transactionType` filter can match only one of its nine values and that value escapes the status filter, and the transaction view never looks up payments. None of it can reach a user or an admin yet: the app code is unmerged and the inbox routes return `403`. All of it is a normal result of both sides moving this fast, and a real run would surface most of it (§3.2, §3.4).

**If you read nothing else:** the code is converging quickly, but tomorrow's sprint close has nothing planned. A sweep like 0902's would mark `I372`, with no code, as delivered.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were not re-exported, and the 08-01 and 0901-admin sidecars are byte-identical to 3 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project: **no successor to 1002 exists yet, with one day left.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged.

| Time (UTC) | Items | Move | Made by | Reading |
|---|---|---|---|---|
| 3 Nov 16:04:12 | `I372` | To do → REVIEW/QA | Ayomikun | Own. No code on any branch, and its parent `I371` is still To do |
| 3 Nov 16:04:20 | `I388` (parent), `I389`, `I390`, `I391` | To do → REVIEW/QA | Ayomikun | Parent move, within 3 ms. `I391`'s route merged 21 minutes later (#93) |
| 3 Nov 16:04:33 | `I385` (parent), `I386`, `I387` | In progress → REVIEW/QA | Ayomikun | Parent move, within 3 ms. `I387`'s route merged **19 hours later** (#94) |

These moves came 52 minutes after the last edition's recheck. Parent moves are inferred from timing, as no comment records intent. That makes **eight** parent moves since 30 Oct. **No comments in the window, and none on 1002 ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002** (no sidecar entry reads "from REVIEW/QA"). Board administration made no move in the window.

Board actions per day on 1002:

| 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov | 4 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 17 | 16 | 6 | 6 | 0 | 0 | 5 | **23** | **0** |

### 1.3 What the last day of 1002 holds

1002 ends **tomorrow, Thursday 5 Nov**. 36 of its 44 leaves are not Done: 30 in REVIEW/QA, 4 In progress, 2 To do (`I362` limits and usage endpoint, `I373` reflect card spending in the app). The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see.

---

## 2. Sprint 1002: what is in review, and whether the code exists

| REVIEW/QA leaves (30) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **11** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391` | Routes on `origin/main`. `I387` caps funding, not spending, and has no maximum. `I391` asks for pagination, search, filter and the Activity tab's query logic, and has none of them |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | 9 | `I334`, `I337`, `I340`, `I343`, `I346`, `I365`, `I369`, `I376`, `I390` | Unmerged. `I343` and `I346` moved here from the row below today, with a real client. `I390` is unassigned and its list would be empty (§3.4) |
| Moved to review, no matching code | 3 | `I348`, `I386`, `I372` | `I348`: mock only, and its server table is gone. `I386`: nothing pushed calls `/limits`. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen), `I383` (client on the branch) and `I384`. All unchanged.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review and no dashboard screen.
- **`origin/BVA-I353`:** 9 ahead, 4 behind `main`, 91 files, +13,526/−134. Last commit `f46641f` *card history, dispute events* (4 Nov 10:13 UTC, 43 files, +3,841/−878). **No PR.**
- **WIP ages:** `I331` and `I354` at 13.2 d; `I357` and `I361` at 1.3 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edits.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-04`), it first reported 3 consumer and 3 admin routes undocumented (exit 1). After the spec changes: 158/158 consumer, 72/72 admin, proposed 34/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 65 phantom lines from the three `diverged` working trees (27 consumer + 38 admin "in spec, not in code"), and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` `main` | `167ad39` → `6c69dbc` | #29, #30; **v0.0.48, v0.0.49**. Seeds `support_hours`, adds `support_settings` and per-agent reads, drops `support_flows` and `flow_state`, adds card limit columns |
| `beevia-api` `main` | `bdb616c` → `bc7da11` | #92 card disputes, assistant topics, hours copy (3 Nov 15:47 UTC). #93 card activity (3 Nov 16:25). #94 card limits (4 Nov 11:16). +2,288/−59 |
| `beevia-admin-api` `main` | `1523591` → `59e03f9` | #28 hours, unread counts, transaction filter and view (3 Nov 15:50). +827/−20 |
| `beevia-mobile` `BVA-I353` | `f6df54e` → `f46641f` | Unmerged (§2, §3.4) |

`beevia-admin` (`64304ef`) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. Four of the six merges came within about 75 minutes after the last edition's recheck, so this edition covers more than today's commits.

### 3.1 Card limits

`GET`/`PATCH /cards/{cardId}/limits`. The change is behind account step-up. `used` counts settled and in-flight fundings in Africa/Lagos days and months, and `assertFundingAllowed` runs before the wallet is touched. #94's commit says the provider has no spend controls or authorization hook. **Checked against the provider's public docs, which agree as far as they go:** Manage Cards says the description "is the only card attribute that can be changed after creation", Create Card takes no limit fields, and Card Payment Events describes after-the-fact notifications. Card product configuration is not visible there, so this does not prove that no limit can exist.

- **The stories cannot be met as written.** See overview item 1. `I385` also requires a maximum "allowed for the user", and #94 deliberately has none yet, with KYC-tier limits to come.
- **The funding check can be raced.** It reads the total and then writes the transfer with no lock, so two simultaneous fundings can both pass (`suggestions.md` §4.13.8).

### 3.2 Card activity and card disputes

`GET /cards/{cardId}/activity` merges `card_transfers` with a live partner read and reports `spend_included: false` if the partner fails, which is a careful touch. From reading the code (`suggestions.md` §4.13):

- **Merchant payments still cannot be disputed**, as above, and **the assistant's tool description says otherwise**. A withdrawal is also typed `card_payment` for the model.
- **`transactionType` on the inbox list is faulty.** Only `payment` can match, because no snapshot has a `type` key. That value escapes the other filters, because the raw `or` is unparenthesised and Drizzle's `and()` does not wrap its items (checked in 0.45.2), so resolved threads would appear in the working queue. #28's tests do not cover this filter.
- **The new transaction view never reads payments.** The last branch returns `null` either way, so a payment dispute says "Transaction no longer found".
- **`unreadOnly` filters after paging**, so `meta.total` overstates and pages run short.

### 3.3 The inbox: what is left

- **`support_hours`: closed.** Seeded weekdays 09:00–18:00 Africa/Lagos, and writable through `/admin/support/hours`.
- **No role holds `disputes`: open, and now the only blocker.** All twelve routes return `403`. `online` needs an on-duty admin, and going on duty needs that permission, so **the app still reads "offline" during open hours.**
- **The dashboard is unchanged.** The mock is on by default, and the `suggestions.md` §5.16 table still stands. `/support/triage-config` is now only half alive: the server built hours and dropped the rest.
- **The assistant's gaps are unchanged:** no dispute reason, reference or snapshot reaches the model, the fraud reason alone does not force a person, a dispute with no `details` calls the model with no messages, and one real chat has still not been recorded. #92 widened what it is asked to handle to five topics.
- **New:** `PUT /admin/support/hours` accepts any `timezone`, and an unknown zone would make `GET /support/availability` throw for every app user.

### 3.4 The app against the new contract

On `BVA-I353`, unmerged. **Closed since yesterday:** the two rejected reasons (`amount_wrong`, `didnt_make_this_transaction`, with old values still read), chat placeholders (real client over the socket with a REST fallback, and all seven `support.*` command names match the gateway), a composer on open dispute threads, `with_assistant` and `quick_replies`. Two `TODO(support-api)` remain, both about the support email address. **Open:**

- **Card history would come back empty.** The parser takes rows only when `data` is a list, and the server returns `data.items`. The mock returns a list, so its tests pass.
- **Then every row would read as money out**, since the server sends `in`/`out` and `isCredit` tests for `credit`.
- **`spend_included` is not read anywhere**, and "load more" stops at 200.
- **Reveal, unfreeze and terminate still send no card PIN**, so each returns `400`. `GET /wallets/limits` is still proposed only. The statement screen still does not mention the PDF password.
- **Send and request on the card screen were replaced by fund and withdraw**, which match the server. This reverses part of 3 Nov's `f6df54e`, and its comment says the design may bring them back.

### 3.5 Document changes this cycle

- **`openapi.yaml`:** +3 (`GET`/`PATCH /cards/{cardId}/limits`, `GET /cards/{cardId}/activity`), 5 new schemas, limit errors on fund, and rewritten `POST /disputes` and `/support/availability` text. **`openapi.admin.yaml`:** +3 (`GET`/`PUT /admin/support/hours`, `/admin/support/conversations/{id}/transaction`), `transactionType`, `unreadOnly` and `unread_count`, with the misbehaviour stated in the parameter descriptions. Proposed files: no change.
- **`api-rfc.md`:** counts, new §5.20. **`admin-api-rfc.md`:** counts, §3.16 to twelve routes.
- **`suggestions.md`:** new §4.13; updates to §4.12, §5.15, §5.16 and §5.17, including the correction above.

### 3.6 The standing checks

- **Pipelines:** whole `release.yml`/`sync.yml`/`deploy.yml` read at `origin/main`, and no workflow changed. All three repos still deploy or migrate on push with no test gate. `beevia-api`'s comment still says "Deliberately not `needs: test`". #29's Release dropped `flow_state` about 20 minutes before the APIs that stopped reading it merged, so support reads probably failed in between (inferred from merge times).
- `PaymentService.activeNgn()`, `StubTranslateAdapter`, unmapped `22P02`, unindexed `messages.ref_id`, FAQ search's missing `en-US` fallback, and no grant of `help_center` or `disputes`: all unchanged.
- `POST /auth/step-up`: no attempt limit, and no throttler anywhere in `src`. `PATCH /cards/{id}/limits` now sits behind it too.
- **Mobile:** `main` unchanged. **`call.ended` is still unhandled** on `main` and on `BVA-I353`. The biometric step-up is unchanged.

---

## 4. Risks

- **1002 ends tomorrow with nothing accepted and no successor sprint.** A sweep like 0902's would mark no-code and mock-only work as delivered, including `I372`.
- **A real charge could be answered with "that isn't yours".** Merchant payments have no dispute path, and the assistant's instructions say otherwise (§3.2). It takes effect once a client ships and the assistant is switched on.
- **All of mobile's sprint work is on one unreviewed branch**, now 91 files, with `main` 13 days behind it. The longer it runs, the more server contract it has to chase, as today's card history shows.
- **A user can be told a person is coming when none can come** (§3.3).
- **Account data going to a third party without a recorded decision or consent.** #92 widened the topics, not the data flow.
- **Done and REVIEW/QA on the board now hide open work.** `I381`'s lockout does not exist, so **guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code**. That token now guards raising a card limit too.
- **The inbox's mock is on by default**, and switching it off naively would show an unfiltered queue or an error.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **The FAQ is still empty in production** until someone grants `help_center` and enters content. It still has no admin screen.
- **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.
- **Withdrawn:** "the fraud reason returns `400` from the branch" and "support hours are permanently empty". Both are fixed, the first on the branch only.

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. PRD §3.2 says users "want to set limits", and today's limits meet that for funding only. The PRD does not say a limit must stop a purchase, so the funding cap may be acceptable. The stories are what say so. The AI assistant is still outside the PRD. `pending_partner`, `partner_reference` and `sla_due_at` are still unbuilt.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 28 Oct 15:01 → 4 Nov 15:01 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are recomputed at the same reduced base as 3 Nov** (the 20 Oct 0902 file is still gone): 0.98 d (n=34), 1.44 d (n=21), 0.89 d (n=3). Each new cycle is a parent move, so read these with care.

### 6.1 Ayomikun Araoye: backend + admin API

**24 commits in 7 days**: 13 in `beevia-api`, 6 in `beevia-admin-api`, 5 in `beevia-db-schema`. **9 own submissions** and 7 moves on other items, 3 of them in this window through parent moves. **No WIP on 1002**, and `I362` is the only To do. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 51.0 days. `I387` went to review 19 hours before its code merged, through its parent. This is a board process point, as with the others below.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct). **4 on `origin/BVA-I353`** in the window, 9 ahead of `main` in all, the latest today at 10:13 UTC. **Zero own submissions**: the last was `I286` on 14 Oct, **20.9 days** ago. All four 7-day "submissions" were moved by Ayomikun, so that count says little about mobile work: today's commit alone is the largest client change in the sprint, and it has no PR to submit against. It caught up with a contract that changed the day before. `I386` and `I390` went to review without David moving them. WIP: **4 items**, with `I331` and `I354` at 13.2 days.

### 6.3 Philip Chidera: design

**One 7-day submission**, `I389`, moved by its parent. **Zero WIP and no leaf left To do**: finished, blocked or working untracked. Worth a question, not an assumption. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**1 commit**, `64304ef` on 30 Oct, now 5.0 days old. The server has moved further towards the screen: hours, unread counts and the transaction beside its snapshot, all to Promise's documents. Nothing has been pushed in response, which after four corrections this report does not read as nothing having been done. The board still shows none of this: `I348` is in REVIEW/QA with no assignee, and `I349` is To do. `BVA-I9` has been In progress on the closed admin board for 51.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (from Mon 2 Nov, to 4 Nov 15:01 UTC) | — | — | **14** | 8 | 6 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a provider investigation and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Seven of this window's eight actions belong to two parent moves, and the routes behind `I387` and `I391` had not merged when those moves happened.
- **Unpushed and untracked work.** Yesterday's "no chat client" is today's evidence of that.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The commits report test counts (1,090 in `beevia-api`, 342 in `beevia-admin-api`), and those were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 3 Nov | Status on 4 Nov |
|---|---|
| **1. Plan 1002's close before Thursday** | ❌ **Not visible.** No successor sprint; nothing left review; 6 more went in; filter still 08-01 |
| **2. Make the inbox reachable** | 🟡 **Half.** `support_hours` seeded and writable. No role granted `disputes` or `help_center` |
| **3. Decide the assistant on the record** | ❌ **Not visible** |
| **4. Run one real chat; pass the dispute's context; force handoff on fraud; skip the empty turn** | ❌ **Not visible.** Code unchanged on all three |
| **5. Bring the dashboard onto the real contract** | ❌ **No commit.** The server closed some of the distance (§3.3) |
| **6. Open a PR for `BVA-I353`, fix the two reasons first** | 🟡 **Half.** Reasons fixed. No PR |
| **7. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | ❌ **No** |
| **8. Agree how parent status moves work; reset `I343`, `I346`, `I348`** | ❌ **No.** Two more parent moves. `I343` and `I346` now at least have code on the branch |
| **9. Assign `I348` and `I349` to Promise** | ❌ **No** |
| **10. Push on an agent's reply; move "logged" to the activity log** | ❌ **No** |
| **11. Reopen `I392`** | ❌ **No** |
| **12. Close the payments half of blocking; let card spending be disputed** | 🟡 **Partly.** Wallet↔card movements are disputable. Merchant payments are not, and blocking is unchanged |
| **13. `needs: test` on `beevia-api`'s `sync`, verify jobs elsewhere** | ❌ **Not done** |
| **14. Generate `openapi.yaml`; stop vendoring the client spec** | ❌ **Not done** |
| **15. Handle `call.ended` on the client** | ❌ **Not done** |
| **16. Carried items** | ❌ **None moved** |

**Three of sixteen moved, all partly.** All three came from the team's own plan rather than this list, and the list's other items may still be on someone's.

---

## 8. What I would do this week

1. **Close 1002 deliberately tomorrow (carried, now urgent).** Accept or return the eleven REVIEW/QA leaves with merged code. Move `I372`, `I386`, `I348` and the nine branch-only mobile leaves back to In progress. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Decide what a card limit is (new).** Accept funding caps and rewrite `I371`, `I372`, `I385` and `I387`, or ask the provider whether card product configuration can hold limits. Either way, the screen must not say "spending limit" while it caps funding.
3. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried, changed).** It is the last server-side step before anyone can answer a thread.
4. **Let a merchant payment be disputed, and correct the assistant's text (new).** Resolve the reference against the partner's list, and until then remove "card spending" from `getTransaction`'s description and hand over.
5. **Open a PR for `BVA-I353` (carried, changed).** Fix the `data.items` parsing and `in`/`out` first, read `spend_included`, and test against a response taken from the server. Split it if that gets it merged sooner, with support first.
6. **Fix the inbox's seams (new):** store the transaction type and parenthesise the `or`, look up payments in the transaction view, and filter `unreadOnly` before paging. Validate `timezone`.
7. **Run one real chat and one real dispute through the assistant (carried)**, then pass the dispute's reason, reference and snapshot, force handoff on `didnt_make_this_transaction`, and skip the empty turn.
8. **Decide the assistant on the record (carried).** Who approved it, what the privacy notice says, and whether users are told it is an AI. Add it to the PRD.
9. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and cut `/support/triage-config` down to hours.
10. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up` whatever the model is.
11. **Agree how parent status moves work on this board (carried).** Move children first, or do not let a parent's move carry them.
12. **Assign `I348`, `I349` and `I390` (carried, extended)**, and give the admin dashboard a sprint or say the consumer board is its home.
13. **Send a push when an agent replies, and move "logged" to the admin activity log (carried).**
14. **Reopen `I392`** until its boxes reflect what was verified (carried).
15. **Close the payments half of blocking** (`suggestions.md` §4.9) (carried).
16. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried). Order schema drops after the code that stops reading them.
17. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried). Today's card history bug is the case for it.
18. **Handle `call.ended` on the client** (carried).
19. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 51.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 51 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, and the server now serves only its hours half) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 5.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-four days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. Line 9 is the one to explain: the server gained limits and activity, but no client on `main` calls them, and the limits are not the spending limits the stories describe. It takes the same treatment as line 11 on 3 Nov, and should move when `BVA-I353` merges with those calls working. Line 11 holds at 0.97: three more admin routes, still no role and no wired screen.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound; no translate change |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | 3 server routes shipped (limits on funding only, activity). Client card management on unmerged `BVA-I353`; auth model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | 3 more support routes. No role holds `disputes`; the screens still run on a mock |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the provider could offer card limits through card product configuration or a commercial agreement.** Only its public docs were read, and they do not cover that.
- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, and whether a real model call succeeds.
- **Who decided on the assistant, or on funding caps, and whether a privacy or legal review happened.** No record is visible here.
- **Whether the migrations have run in production, and whether support reads failed during #29's gap.** Merge times are known, and workflow results are not.
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **Whether the commit-reported tests pass, or whether anything renders.** Nothing was executed. The client findings come from reading the parser beside the server's code and its Postman samples.
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **Whether a server-side attempt limit exists at a proxy** in front of the API.
- **Whether a production build of `beevia-admin` exists**, and with which flag.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items on 5 Nov.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel as three background calls, starting at about 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 3 Nov. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-04`: exit 1 before spec edits, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`q04.py`, `flow04.py`, `win04.py`, `items04.py`): a diff of 1002 against 3 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA. The sprint lists came from the `__nonexistent__` dry run.
5. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`: card controller, DTO, limits, activity and funding services, support service, agent and tools, availability, gateway. In `beevia-admin-api`: support controller, DTO, service, hours. In `beevia-db-schema`: migrations 0047–0049, `cards.ts`, `card-topups.ts`, `support.ts`. In `beevia-mobile`: `f46641f`'s wallet and support code, its mock routes. Drizzle's `and()` was read in the 0.45.2 copy already installed in `beevia-api/node_modules`; nothing was run from it.
6. Provider docs, read only: [Manage Cards](https://docs.getanchor.co/docs/manage-cards), [Create Card](https://docs.getanchor.co/docs/create-card), [Card Payment Events](https://docs.getanchor.co/docs/card-payment-events).
7. Spec and narrative updates (§3.5).
8. This report and its web edition.
9. End-of-run recheck: see the note under Window.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`reflog`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-04.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 4 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The 20 Oct 0902 scratch file is gone from `/tmp`**, so median cycle times have lower n and are not comparable with editions before 3 Nov. The older rows of the weekly table are carried.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **Provider documentation is partial.** One guessed page returned `404` (Card Payments Lifecycle), and card product configuration is not described.

**Window.** 3 Nov 15:01 UTC → 4 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets. **End-of-run recheck at 15:12 UTC:** a fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 3 Nov 16:04 UTC, and `ls-remote` showed every `main` and `BVA-I353` at the commits read above, with no new PR on any repo.
