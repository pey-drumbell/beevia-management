# Beevia — Project Status

**As of 2026-11-03** · Sprint **1002** (21 Oct → 5 Nov, day 14 of 16): **63 items, 44 leaves: 6 To do · 6 In progress · 24 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-03.csv` + `beevia-activity-2026-11-03.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-03.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 2 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 2 Nov 15:01 UTC → 3 Nov 15:01 UTC, 1.0 day (Mon → Tue).**

---

## Quick overview

> **The support backend shipped today: one queue for disputes and chats, with an AI assistant answering first. It replaced the disputes API and adopted most of Promise's contract, which settles yesterday's main question. Nobody can use it yet. No admin role can open the inbox, the dashboard still runs on its mock, and the app has no chat client and sends two dispute reasons the server now rejects, including the fraud one. 1002 ends Thursday with 24 of 44 leaves in review, 9 of them with merged code, none accepted, and no successor sprint.**

| Metric | 2 Nov | 3 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 11 / 11 / 16 / 0 / 6 | **6 / 6 / 24 / 0 / 8** | 8 into REVIEW/QA, 2 into Done, 3 into In progress |
| Board actions on 1002 in the window | 6 | **20** | 5 on 2 Nov 15:58–15:59 UTC, 15 today |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **14** | 8 by the leaf's owner (Ayomikun), 6 moved by Ayomikun on David's and unassigned items |
| Owners' last submission of their *own* leaf | 28 Oct 16:22 UTC | **3 Nov 13:52 UTC** (Ayomikun, `I344`) | David's last own submission is 14 Oct, **19.9 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 4 of 16 | **9 of 24** | `I332`, `I344`, `I347`, `I350`, `I352` added |
| Routes in code but not in the spec (consumer / admin), before today's edits | 0 / 0 | **6 / 9**, plus 3 admin routes removed | now **0 / 0**: specs updated |
| API surface (consumer / admin) | 149 / 63 | **155 / 69** | +6 / +9 −3 |
| Proposed operations (consumer / admin) | 37 / 18 | **34 / 18** | `/support/tickets` shipped in another shape |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | |
| `beevia-admin` days since a commit | 3.0 | **4.0** | |
| `beevia-mobile` days since a commit on `main` | 11.2 | **12.2** | `BVA-I353` moved: `f6df54e`, 0.2 d ago, still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 3.9 / 4.9 / 5.0 | **0.0 / 0.0 / 0.1** | 8 merges across the three today |
| Admin board: open sprint / days since any activity | none / 49.0 | **none / 50.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: support is not on the rubric, and line 11's screens are still on a mock |

**Three corrections to 2 Nov.**

1. **"Every complaint about money waits with no reader" described nobody.** That edition listed disputes that could not be answered as a live risk, with the 72-hour KPI "counting". The schema commit `4ab65b5` records that `transaction_disputes` had zero rows, and no client on any `main` called it. That is the commit's claim, and production cannot be seen from here, but on that record nobody was waiting.
2. **"`BVA-I353` closed the fraud-report bug" did not last a day.** It was accurate against the 2 Nov server. #89 then renamed the enum, so the branch's `not_my_transaction` and `wrong_amount` are rejected again (§3.3).
3. **"The server half has not started in any visible way" (`suggestions.md` §5.16) was a claim about what had been pushed.** It shipped the next day. This is the third time this report has read silence as absence, after mobile on 27 Oct and `beevia-admin` on 30 Oct.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (3 To do, 1 In progress, 12 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **8 own** (+6 moves on other items) | 1.48 d (n=20) | `I387` (1.0 d, moved there by its parent) · `BVA-I8` on 0901-admin (**50.0 d**) | **23** (11 `beevia-api`, 7 `beevia-admin-api`, 5 `beevia-db-schema`) | The role grant and `support_hours` decide whether today's work can be used |
| David Samuel | mobile | **1002: 16** (1 To do, 5 In progress, 8 REVIEW/QA, 2 Done) · `I392` shared | 5 (**0 own**, 5 moved by Ayomikun) | 0.98 d (n=33) | 5: `I331`, `I354` (**12.2 d**), `I386` (8.0 d), `I357`, `I361` (0.3 d) | **0 on `main`** · **4 on `BVA-I353`** | The server contract changed under the branch today. Still no PR |
| Philip Chidera | design | **1002: 7** (1 To do, 3 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | Zero WIP: what is next? |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**50.0 d**) | **1** (`beevia-admin`, 68 files) | The server now exists, and the screen needs to follow its differences. `I348` and `I349` still show no assignee |

**The three questions for standup:** (1) **Who grants `disputes` and fills `support_hours`, and when?** Until both happen, handed-over threads have no reader and support shows offline permanently. (2) **Was the AI assistant decided, and by whom?** It sends account data to a model provider, the PRD does not mention it, and the only record is commit messages. (3) **How does 1002 close on Thursday?** Two working days remain after today, 24 leaves wait in review, and there is no successor sprint.

**The three things worth knowing:**

1. **The server settled the contract, and now both clients have to move.** #25 builds nine of the eleven routes in Promise's `hs7`/`hs6` documents and adopts their reason codes. It departs from them on purpose in three places and says so. `/admin/disputes` is gone. But the dashboard cannot simply switch off its mock: the response shape, status names and filter names all differ. The filter case is the dangerous one, because unknown query keys are ignored, so `assigned_to` returns `200` with no filter applied (§3.2). The app's reasons, chat screen and dispute thread are on the old contract too (§3.3). None of this is a mistake by anyone. The server was built last and made its choices clear, so this is the expected next step.

2. **The assistant is built carefully, and it has gaps a real chat would show.** It can only read, the model cannot choose whose account to read, and sensitive wording goes straight to a person. However, from reading the code, it is never told a dispute's reason, reference or snapshot. A dispute with the fraud reason still goes to the model unless the note contains certain words. And every chat opens with an assistant turn, which the stubbed tests cannot exercise, so one real chat should be run (§3.1). Separately, balances, transactions and masked card numbers now go to a third party, and no consent record exists. That needs a decision, not a code change.

3. **The board now says more than the code does.** Two parent moves carried David's `I343` and `I346` and the unassigned `I348` into REVIEW/QA today: `I346`'s chat screen is placeholder data, and `I348`'s screen runs on a mock and configures a triage the assistant has just replaced. Closing `I382` yesterday marked `I383` and `I384` Done with the client code unmerged. **This is a process point, not a personal one: on this board a parent's status carries its children**, and that has happened six times since 30 Oct. A sweep would record all 32 leaves now in REVIEW/QA or Done as delivered, while only 9 of the 24 in review have merged code.

**If you read nothing else:** today's backend is real progress and removes yesterday's contract question. It needs one role grant, one table filled, one real chat and a decision on the assistant before it does anything for a user.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were not re-exported, and the 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project: **no successor to 1002 exists yet.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged.

| Time (UTC) | Items | Move | Made by | Reading |
|---|---|---|---|---|
| 2 Nov 15:58:58 | `I382` (parent), `I383`, `I384` | In progress → Done | Philip | Parent close, within 2 ms |
| 2 Nov 15:59:12 | `I385` (parent), `I387` | To do → In progress | Philip | Parent move, within 1 ms |
| 3 Nov 08:04, 08:08 | `I357`, `I361` | To do → In progress | David | Own moves |
| 3 Nov 11:11 | `I330` | Ayomikun removed as owner | Ayomikun | |
| 3 Nov 11:15 | `I352` | To do → BLOCKED → REVIEW/QA | Ayomikun | The board's usual 6-second route to review. Not a real block. API shipped 28 Oct |
| 3 Nov 11:15, 13:52 | `I350` | To do → In progress → REVIEW/QA | Ayomikun | Own |
| 3 Nov 13:52:46 | `I332` | In progress → REVIEW/QA | Ayomikun | Own |
| 3 Nov 13:52:50 | `I345` (parent), `I346`, `I347`, `I348` | In progress → REVIEW/QA | Ayomikun | Parent move, within 3 ms |
| 3 Nov 13:52:58 | `I342` (parent), `I343`, `I344` | In progress → REVIEW/QA | Ayomikun | Parent move, within 2 ms |

That 2 Nov 15:58 batch came 57 minutes after the last edition's cut-off. Parent moves are inferred from timing, as no comment records intent. **No comments in the window.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002** (no sidecar entry reads "from REVIEW/QA"). Board administration made no move in the window.

Board actions per day on 1002:

| 23 Oct | 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov | 3 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | 15 | 17 | 16 | 6 | 6 | 0 | 0 | **5** | **15** |

### 1.3 What the last days of 1002 hold

1002 ends **Thursday 5 Nov**, two working days after today. 36 of its 44 leaves are not Done: 24 in REVIEW/QA, 6 In progress, 6 To do. The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see.

---

## 2. Sprint 1002: what is in review, and whether the code exists

| REVIEW/QA leaves (24) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **9** | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352` | Routes on `origin/main`. `I347` was built differently from its description: it asks for a rules engine, and the assistant replaced that. `I350` matches its route list |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Mobile, code only on `origin/BVA-I353` | 6 | `I334`, `I337`, `I340`, `I365`, `I369`, `I376` | Unmerged. `I340` (report sheet) now sends two reasons the server rejects |
| Carried in by a parent today, code does not match | 3 | `I343`, `I346`, `I348` | `I343`: list works on the branch, thread is read-only. `I346`: placeholder data. `I348`: mock only, no server route |
| Design | 3 | `I364`, `I368`, `I375` | Design files are not in git |

- **Done without matching merged code:** `I380`, `I381` (unchanged since 2 Nov: no attempt limit or lockout on `POST /auth/step-up`, no reopen) and now `I383` (client on the branch) and `I384`. `I384` asks for full card details behind a valid authorization, and `POST /cards/{id}/reveal` predates the sprint and takes the card PIN, so whether it meets the item depends on the still-open verification model.
- **Admin Stories:** `BVA-I349` (Support Inbox) is To do and unassigned while its API child `I350` is in review. `BVA-I351` (FAQ CMS) is the same, with `I352` in review and no dashboard screen.
- **`origin/BVA-I353`:** 8 ahead, 4 behind `main`, last commit `f6df54e` *card details flow* (3 Nov 10:00 UTC, 26 files, +571/−78). **No PR.** New: card transactions via `GET /cards/{id}/transactions` (matches), terminate as `POST`, send and request from the card screen. **Still open:** reveal, unfreeze and terminate send `X-Step-Up-Token` and no card PIN, so each returns `400`; `GET /wallets/limits` is proposed only; the statement screen still does not mention the PDF password.
- **WIP ages:** `I331` and `I354` at 12.2 d; `I386` at 8.0 d; `I387` at 1.0 d; `I357` and `I361` at 0.3 d.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edits.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-03`), it first reported 6 consumer and 9 admin routes undocumented and 3 admin routes removed (exit 1). After the spec changes: 155/155 consumer, 69/69 admin, proposed 34/18, spec health clean, no `x-beevia-*` (exit 0). The in-repo audit still reports 59 phantom lines from the three `diverged` working trees (24 consumer + 35 admin "in spec, not in code", up from 47 because the specs gained routes the frozen trees lack), and they were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-db-schema` `main` | `2fbf657` → `167ad39` | #27, #28; **v0.0.46, v0.0.47**. `support_threads`, messages, attachments, flows, hours, `support_agent_turns`. Drops `transaction_disputes` |
| `beevia-api` `main` | `4c57305` → `bdb616c` | #89 threads and assistant, #90 inbox events, #91 `500` on a non-UUID reference. +3,237/−710 |
| `beevia-admin-api` `main` | `b8b6a13` → `1523591` | #25 inbox and socket, #27 event shape, #26 Postman filters. +2,902/−726 |
| `beevia-mobile` `BVA-I353` | `21fe490` → `f6df54e` | Unmerged (§2) |

`beevia-admin` (`64304ef`) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move.

### 3.1 The assistant

`SupportAgentService` uses `@ai-sdk/anthropic` (`SUPPORT_AI_MODEL`, default `claude-sonnet-5-5`), with six read-only tools and a handoff signal. Each turn is logged to `support_agent_turns`. Without an API key it hands every message to a person. No workflow or example file names the key, so whether it runs in production cannot be seen here. Open points (`suggestions.md` §4.12), all from reading the code:

- **It is not told what a dispute is about.** Only message bodies reach the model. Reason, reference and snapshot do not.
- **A fraud reason alone does not force a person.** The regex tests text only.
- **A dispute with no `details` calls the model with no messages.** That should fail and hand over, logged as an error.
- **Every chat opens with an assistant turn**, the greeting. The specs stub the model, and the API docs checked do not settle whether the provider accepts this. If it does not, every chat would hand over at once. One real chat answers it.
- **Account data leaves for a third party, and no consent record exists.** The PRD's consent list covers location, biometrics and translation. Whether a user is told they are talking to an AI is also undecided in the code: `support.views.ts` has the client showing both as Beevia Support.
- **The decision is in commit messages only.** `4ab65b5` called triage "rule-based by requirement" at 11:27 UTC, and `63ec19f` replaced it 56 minutes later. The owner may well have decided this elsewhere; it just cannot be seen here. `I347`'s description still asks for the rules engine.

### 3.2 The inbox: what stops it working today

- **No role holds `disputes`.** No migration or seed grants it, and `PermissionGuard` has no super-admin bypass, so all nine routes return `403`.
- **`support_hours` is empty, and nothing writes it.** No migration, seed or route. `GET /support/availability` therefore reports offline permanently.
- **The dashboard fails if the mock is switched off:**

| | `beevia-admin` | `beevia-admin-api` |
|---|---|---|
| List | `data.conversations`, `data.pagination` | `data` array + `meta`; the screen throws |
| Filters | `assigned_to`, `reason_code`, `transaction_type` | `assignedTo`, `reasonCode`; **unknown keys are ignored** |
| Statuses | `waiting`, `active`, `closed`, `in_progress`, `resolved` | `with_assistant`, `queued`, `in_progress`, `resolved` |
| Closing | `{status}` only | `resolved` needs `resolutionNote`, else `422` |
| Triage panel | `triage_context` | `assistant_summary` |

The mock's default is still on (`NEXT_PUBLIC_USE_MOCK_SUPPORT_API !== "false"`), so a production build without the flag still shows invented conversations. `/support/triage-config` has no route, and `support_flows` is now unused. Also: no push on an agent's reply (`support_replies` is read by nothing), and "opening is logged" is an application log line, not an audit record.

### 3.3 The app against the new contract

`BVA-I353`'s `IssueReason` sends `wrong_amount` and `not_my_transaction`; the server takes `amount_wrong` and `didnt_make_this_transaction`, so those two of seven return `400`. Its mock still accepts them, so its tests cannot show it. History rows now show the server's English `title` where the screen used a localized reason. `support_service.dart` still says chat has no endpoints, with 5 `TODO(support-api)` left. The dispute thread is read-only, although the server now accepts replies.

### 3.4 Document changes this cycle

- **`openapi.yaml`:** +6 (`/disputes/open-count`, `/support/availability`, `GET`/`POST /support/chats`, `/support/threads/{id}`, `/support/threads/{id}/messages`); `/disputes*` rewritten to the thread shape and renamed reasons. **`openapi.admin.yaml`:** +9 `/admin/support/*`, −3 `/admin/disputes*`. **`openapi.proposed.yaml`:** −3 `/support/tickets`, with a comment on what stays unbuilt. `openapi.admin.proposed.yaml`: no change. The inbox's 9 routes went straight to the implemented file, and the two triage routes are not added, since the assistant replaced what they configure.
- **`api-rfc.md`:** counts, new §5.19, §6.8, §7.8, Phase E. **Found, not fixed:** the §7 tables list 11 operations that have since shipped, and the intro said 35/38. The intro now gives 31 + 3 and says so.
- **`admin-api-rfc.md`:** counts, Module 5, §3.16 rewritten as the inbox.
- **`suggestions.md`:** new §4.12 and §5.17; updates to §4.11, §5.15 and §5.16, including corrections.

### 3.5 The standing checks

- **Pipelines:** whole `release.yml`/`sync.yml`/`deploy.yml` read at `origin/main`, and no workflow changed. All three repos still deploy or migrate on push with no test gate. #27's commit states that the table drop lands before the new API, so dispute routes return `500` in between: about 2 h 10 min by merge times (11:27 → 13:38 UTC). It cost nothing today, as the table was empty, and nothing would have stopped it otherwise.
- `PaymentService.activeNgn()`, `StubTranslateAdapter`, unmapped `22P02` (#91 guards the reference path only), unindexed `messages.ref_id`, FAQ search's missing `en-US` fallback, and no grant of `help_center` or `disputes`: all unchanged.
- `POST /auth/step-up`: no attempt limit, and no throttler anywhere in `src`.
- **Mobile:** `main` unchanged. **`call.ended` is still unhandled** on `main` and on `BVA-I353`. The biometric step-up is unchanged.

---

## 4. Risks

- **A user can be told a person is coming when none can come.** Once a client ships, handover says "Someone from the team will pick this up here", and no role can open the queue (§3.2).
- **Account data going to a third party without a recorded decision or consent** (§3.1).
- **1002 ends Thursday with nothing accepted and no successor sprint.** A sweep like 0902's would mark unmerged, mock-only and replaced work as delivered.
- **Done and REVIEW/QA on the board now hide open work.** `I381`'s lockout does not exist, so **guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code**. That token guards card creation and PIN reveal.
- **The inbox's mock is on by default**, and switching it off naively would show an unfiltered queue or an error.
- **The fraud reason returns `400` from the branch**, if it merged as it stands.
- **Every backend repo still deploys or migrates production on push without a test gate.** Today put 8 merges, five migrations and a new external dependency through that path in about three hours.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content. It still has no admin screen.
- **Blocking does not reach payments.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); card spending not disputable; 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.
- **Withdrawn:** "disputes can be filed and cannot be answered", on the record in correction 1.

---

## 5. PRD gap

The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) are unchanged and carry 32 of the rubric's 100 points. Today's work serves PRD §7.4's dispute KPI and §8.3's escalation promise, neither of which is a rubric line. `pending_partner`, `partner_reference` and `sla_due_at` from the removed proposal are still unbuilt. The AI assistant is outside the PRD (§3.1), and support threads are a deliberate carve-out from its "end-to-end encryption on every conversation".

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 27 Oct 15:01 → 3 Nov 15:01 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times are recomputed and not comparable with 2 Nov.** New items entered review, so they could not be carried again, and the 20 Oct 0902 file that fed the older figures is gone: 0.98 d (n=33, was 0.99, n=40), 1.48 d (n=20, was 0.99, n=20), 0.89 d (n=3, was 0.94, n=4). Ayomikun's rise comes from losing old short cycles and adding `I332` and `I347`, which were open for days, and does not mean anything slowed.

### 6.1 Ayomikun Araoye: backend + admin API

**23 commits in 7 days**: 11 in `beevia-api`, 7 in `beevia-admin-api`, 5 in `beevia-db-schema`. All of today's backend work is under this identity. **8 own submissions**, 5 of them today, and 6 moves on other items, 3 of them today through parent moves. WIP: `I387` (1.0 d, moved there by its parent, so not evidence that work began). `I362`, `I372` and `I391` are To do. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 50.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct). **4 on `origin/BVA-I353`** in the window, 8 ahead of `main` in all, the latest today at 10:00 UTC. **Zero own submissions**: the last was `I286` on 14 Oct, **19.9 days** ago. All five 7-day "submissions" were moved by Ayomikun. This is why that count says little about mobile work: the branch has moved steadily and has no PR to submit against. WIP: **5 items**, with two started this morning. The server contract changed under the branch today through no action of David's.

### 6.3 Philip Chidera: design

Closed `I382` and its children, and moved `I385` and `I387` to In progress, on 2 Nov. **Zero 7-day submissions** (the 27 Oct move aged out) and **zero WIP**, with `I389` To do: finished, blocked or working untracked. Worth a question, not an assumption. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**1 commit**, `64304ef` on 30 Oct, now 4.0 days old. The server was built to Promise's documents, a real result for that work, and its three differences plus the mechanical ones in §3.2 are the next step. Whether the two spoke cannot be seen here. The board still shows none of this: `I348` moved to REVIEW/QA with no assignee, and `I349` is To do. `BVA-I9` has been In progress on the closed admin board for 50.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (from Mon 2 Nov, to 3 Nov 15:01 UTC) | — | — | **8** | 5 | 3 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep. Output stayed steady and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A five-migration feature and a one-line fix count the same, and so do 23 commits against one of 10,750 lines.
- **Who moved an item is not whether it is done.** Today's three moves on others' leaves are parent moves.
- **Unpushed and untracked work.** Today's backend was invisible yesterday.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The commits report test counts (1,020 in `beevia-api`, 321 in `beevia-admin-api`), and those were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 2 Nov | Status on 3 Nov |
|---|---|
| **1. Plan 1002's close before Thursday** | ❌ **Not visible.** No successor sprint; nothing left review; filter still 08-01 |
| **2. Reopen `I380` and `I381`** | ❌ **No.** Still Done, and `I383`/`I384` closed the same way |
| **3. Promise and Ayomikun settle `hs7`/`hs6`** | ✅ **Settled in code.** Route, reason codes, `rejected` and the note are all decided. Whether they spoke cannot be seen. The routes went to the implemented spec |
| **4. Assign `I348` and `I349` to Promise** | ❌ **No.** Both still unassigned |
| **5. Default the support mock off in production** | ❌ **No** |
| **6. Open a PR for `BVA-I353`** | ❌ **No.** One more commit, no PR |
| **7. Grant `disputes` and `help_center`** | ❌ **No**, and now it blocks the whole inbox |
| **8. Reopen `I392`** | ❌ **No** |
| **9. Close the payments half of blocking** | ❌ **Not done** |
| **10. Disputes follow-ups** | 🟡 **Partly, by replacement.** Atomic, named claim: yes. Answer notifies the user: over the socket, no push. Conditional admin answer: yes. Card spending and transaction type: no |
| **11. `needs: test` on `beevia-api`'s `sync`** | ❌ **Not done** |
| **12. Generate `openapi.yaml`; stop vendoring the client spec** | ❌ **Not done** |
| **13. Handle `call.ended` on the client** | ❌ **Not done** |
| **14. Carried items** | ❌ **None moved** |

**Two of fourteen moved, one fully.** Both came from the backend's own plan rather than this list, and the list's other items may still be on someone's.

---

## 8. What I would do this week

1. **Plan 1002's close before Thursday (carried).** Review the nine REVIEW/QA leaves with merged code and accept or return them. Move the nine mobile and mock-only ones back to In progress. Create the successor sprint, carry the remainder explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER`.
2. **Make the inbox reachable (new).** Grant `disputes` and `help_center` to the support role and Super Admin, and fill `support_hours`, with an admin route or a seed.
3. **Decide the assistant on the record (new).** Who approved it, what the privacy notice says about account data going to the model provider, and whether users are told it is an AI. Add it to the PRD.
4. **Run one real chat and one real dispute through the assistant (new).** Then pass the dispute's reason, reference and snapshot to the model, force handoff on `didnt_make_this_transaction`, and skip the turn when there is no message.
5. **Bring the dashboard onto the real contract (new)**: shape, statuses, camelCase filters, `resolutionNote`, `assistant_summary`. Default the mock off in production builds at the same time. Decide whether `/support/triage-config` and `I348` still have a purpose.
6. **Open a PR for `BVA-I353`, and fix the two reasons first (carried, changed).** Split it if needed. Chat, socket commands and dispute replies can follow on a second branch.
7. **Reopen `I380`, `I381`, `I383` and `I384` if those closes were not meant for them (carried)**, decide the card verification model, and add an attempt limit to `/auth/step-up` whatever the model is.
8. **Agree how parent status moves work on this board (new).** Move children first, or do not let a parent's move carry them. Reset `I343`, `I346` and `I348`.
9. **Assign `I348` and `I349` to Promise (carried)**, and give the admin dashboard a sprint or say the consumer board is its home.
10. **Send a push when an agent replies, and move "logged" to the admin activity log (new)** (`suggestions.md` §4.12).
11. **Reopen `I392`** until its boxes reflect what was verified (carried).
12. **Close the payments half of blocking** (`suggestions.md` §4.9), and let card spending be disputed (carried).
13. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried).
14. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10) (carried).
15. **Handle `call.ended` on the client** (carried).
16. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; prune the §7 tables in `api-rfc.md`; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 50.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 50 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock, no route) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 4.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-three days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves, on a day with the largest backend change in weeks. Support and disputes are not rubric capabilities, so most of it scores nothing here. Line 11 is the one to explain: the admin API grew, but its new routes have no role and no wired screen, and line 11 scores what is wired, so it holds at 0.97. Line 1 stays at 0.90: support threads are plaintext by design, and they are separate from the E2EE chat surface. Line 9's client work is still unmerged.

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
| 9 | Virtual cards | 10 | 0.80 | 0 | No server card change. Client card management on unmerged `BVA-I353`; auth model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | 9 inbox routes shipped, 3 dispute routes removed. No role holds `disputes`; the screens still run on a mock |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the assistant runs at all in production**: whether the key is set, whether `SUPPORT_AI_ENABLED` is on, and whether a real model call succeeds.
- **Who decided on the assistant, and whether a privacy or legal review happened.** No record is visible here.
- **Whether production has any disputes.** "Zero rows" is the commit's statement, made before the drop.
- **Whether the migrations have run in production.** Merge times are known, and workflow results are not.
- **Whether any role was granted `disputes` or `help_center`, or `support_hours` filled, by hand.**
- **Whether the commit-reported tests pass, or whether anything renders.** Nothing was executed.
- **Whether closing `I382` was meant to close its children**, or the same for `I378`. Same-millisecond timing is inference.
- **Whether a server-side attempt limit exists at a proxy** in front of the API.
- **Whether a production build of `beevia-admin` exists**, and with which flag.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items on 5 Nov.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel as three background calls, starting at about 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 2 Nov. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-03`: exit 1 before spec edits, exit 0 after. The in-repo audit ran too, for the board section (phantom lines only). All through `uv run --no-project --with pyyaml`.
4. Board analysis (`q03.py`, `flow03.py`, `win03.py`, `items03.py`): a diff of 1002 against 2 Nov, every action in the window, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA. The sprint lists came from the `__nonexistent__` dry run.
5. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` of `refs/pull/*` on every repo. In `beevia-api`/`beevia-admin-api`: support controllers, DTOs, services, views, tools, gateway, realtime, `PermissionGuard`, card controller and `env.ts`. In `beevia-db-schema`: migrations 0042–0046, `support.ts` and the seeds. In `beevia-mobile`: `f6df54e`'s diff, support models, service and screens. In `beevia-admin`: `api.ts`, `constants.ts`, `types.ts`, the contract documents. Provider docs were checked for the first-turn question and did not settle it.
6. Spec and narrative updates (§3.4).
7. This report and its web edition.
8. End-of-run recheck: see the note under Window.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-03.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `openapi.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 3 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The 20 Oct 0902 scratch file is gone from `/tmp`**, so median cycle times have lower n and are not comparable with earlier editions. The older rows of the weekly table are carried.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 2 Nov 15:01 UTC → 3 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets. **End-of-run recheck at 15:12 UTC:** a fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 3 Nov 13:52 UTC, and `ls-remote` showed every `main` and `BVA-I353` at the commits read above, with no new PR on any repo.
