# Beevia — Project Status

**As of 2026-11-02** · Sprint **1002** (21 Oct → 5 Nov, day 13 of 16): **63 items, 44 leaves: 11 To do · 11 In progress · 16 REVIEW/QA · 0 BLOCKED · 6 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-02.csv` + `beevia-activity-2026-11-02.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-02.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 30 Oct file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 30 Oct 14:03 UTC → 2 Nov 15:01 UTC, 3.0 days (Fri → Mon).**

---

## Quick overview

> **The admin dashboard is moving again, and 1002 has three working days left after today. `beevia-admin` took its first commit in 38 days: two support screens, 68 files and 10,750 lines. They run on mock data by default, and the dispute contract they propose conflicts with the API that already shipped. On the board, closing the "Verify it's you" Story marked the mobile and backend items under it Done, although the backend it asks for does not exist. `BVA-I353` fixed the fraud-report bug and its statement route, but still has no PR. Nothing has left REVIEW/QA, no successor sprint exists, and 38 of 44 leaves are not Done.**

| Metric | 30 Oct | 2 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 12 / 13 / 16 / 0 / 3 | **11 / 11 / 16 / 0 / 6** | 3 In progress → Done (`I379`, `I380`, `I381`); `I384` To do → In progress |
| Board actions on 1002 in the window | 0 | **6** | all on 30 Oct, 14:55–16:11 UTC; none since |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **10** | same ten; 5 by the leaf's owner (Ayomikun), 5 moved by Ayomikun on David's and Philip's items |
| Owners' last submission of their *own* leaf | 28 Oct 16:22 UTC (Ayomikun, `I341`) | **unchanged** | David's last own submission is 14 Oct, **18.9 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | Done leaves skipped the queue |
| 1002 REVIEW/QA leaves with matching **merged** code | 4 of 16 | **4 of 16** | |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 | **0 / 0** | no backend `main` moved |
| API surface (consumer / admin) | 149 / 63 | **149 / 63** | |
| Proposed operations (consumer / admin) | 37 / 18 | **37 / 18** | the inbox's 11 are not added yet (§3.3) |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | |
| `beevia-admin` days since a commit | 37.9 | **3.0** | `64304ef`, 30 Oct 15:52 UTC |
| `beevia-mobile` days since a commit on `main` | 8.2 | **11.2** | `BVA-I353` moved: `21fe490`, 3.0 d ago, still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 1.9 / 1.9 | **3.9 / 4.9 / 5.0** | none moved |
| Admin board: open sprint / days since any activity | none / 46.0 | **none / 49.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: the new screens run on mock data, and everything else is on an unmerged branch |

**Two corrections to 30 Oct.**

1. **"The board stopped" was an artefact of the cut-off.** That edition read the board at 14:02 UTC. At 14:55 the same day the board recorded four completions, and by 16:11 two more moves, with two code pushes at 15:52 and 15:54. "No action in the window" was accurate, but the headline read more into it than one early cut-off can support.
2. **`beevia-admin`'s 37.9 days read as a stall, and it was not one.** The detail section said local work would be invisible, but the risk list and the recommendation ("or say the dashboard is paused") treated the silence as the finding. A single 10,750-line commit almost certainly was not written in a day. This is inference, because one commit carries one date. The silence meant "nothing pushed", as this report has already had to learn once for mobile.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (6 To do, 4 In progress, 7 REVIEW/QA, 1 Done) · `I392` shared · 0901-admin: 1 In progress | **5 own** (+5 moves on teammates' items) | 0.99 d (n=20) | `I332` (**11.2 d**), `I347` (**7.0 d**), `I344` (5.1 d), `I384` (3.0 d, moved there by the parent) · `BVA-I8` on 0901-admin (**49.0 d**) | **16** (9 `beevia-api`, 3 `beevia-admin-api`, 4 `beevia-db-schema`) | `I381` shows Done with no matching server code. The inbox contract has 12 backend questions waiting |
| David Samuel | mobile | **1002: 16** (3 To do, 6 In progress, 6 REVIEW/QA, 1 Done) · `I392` shared | 4 (**0 own**, 4 moved by Ayomikun) | 0.99 d (n=40) | 6: `I331`, `I354` (**11.2 d**), `I346`, `I383`, `I386` (7.0 d), `I343` (5.1 d) | **0 on `main`** · **6 on `BVA-I353`** (7 on the branch) | Fraud reason and statement route fixed. Branch still has no PR |
| Philip Chidera | design | **1002: 7** (1 To do, 3 REVIEW/QA, 3 Done) · `I392` shared (Done) | 1 (0 own, 1 moved by Ayomikun) | 0.94 d (n=4) | none | n/a | Zero WIP with `I379` finished: what is next? |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**49.0 d**) | **1** (`beevia-admin`, 68 files) | Inbox and triage screens landed. `I348` and `I349` still show no assignee |

**The three questions for standup:** (1) **Was closing `I378` meant to close `I380` and `I381`?** If not, reopen them. The lockout and biometric credential they ask for are not on any remote. (2) **Who settles the inbox contract, and when?** Promise's screen and Ayomikun's `/admin/disputes` disagree on reasons, statuses and whether an answer needs a note. Is there a slot this week for the two of them to go through the 12 backend questions? (3) **How does 1002 close on Thursday?** 16 leaves wait in review, 11 have not started, 11 are In progress, and there is no successor sprint.

**The three things worth knowing:**

1. **The admin inbox is real, on mock data, and disagrees with the server.** `64304ef` adds `/support/inbox` and `/support/triage-config`: queue, thread, claim and assign, reply, availability, socket handlers and a triage editor. Its 11 operations under `/admin/support/*` do not exist on any server, and Promise's documents say so plainly and ask for confirmation. The conflict is with `/admin/disputes`, shipped on 28 Oct, which the screen does not call. Two reason codes differ, the screen has no `rejected` state, and it closes a dispute without the written answer the server requires (§3.1). The mock also stays on unless someone sets a flag to `false`, so a production build without it would show invented conversations (§3.2). This is the moment to reconcile the two, while neither is in use: no role holds `disputes` yet, and `I347`/`I350` have no code.

2. **`I381` says Done, and the server has not changed.** At 14:55:45 UTC on 30 Oct, `I378` and its children `I379`, `I380` and `I381` all went from In progress to Done within 5 milliseconds, by one person. That is what closing a parent Story looks like. It may well have been meant for the design half (`I379`). But `I381` asks for attempt limits, a lockout and a biometric-backed credential, and `assertPin` still just compares and throws. Reveal, unfreeze and terminate still take the card PIN in the body. `I380`'s sheet on the branch is the existing payment sheet with a new title and no lockout message. So the three-way model question from 29 Oct is still open; the board just no longer shows it. **This is a process point, not a personal one: this board lets a parent's status carry its children with it**, and the same thing moved `I384` to In progress an hour later.

3. **`BVA-I353` closed two real bugs, and the deadline is what remains.** `21fe490` changes the fraud reason to `not_my_transaction`, so "I didn't make this transaction" should no longer return `400`, and it moves both statement calls to the real `POST /statements`. Six REVIEW/QA leaves and five In progress ones still depend on a branch nobody can review, because it has no PR. Thursday is three days after today, and the only precedent (0902) ended in a sweep that would mark all of this delivered.

**If you read nothing else:** the admin work was never paused, and it should now be reconciled with the API before either side builds further. Check what the Done labels on verification mean before 1002 closes on Thursday.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 and 0901 were not re-exported, and the 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project: **no successor to 1002 exists yet.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged.

| Time (30 Oct, UTC) | Item | Move | Made by | Owner |
|---|---|---|---|---|
| 14:55:45.643 | `I379` *Verification Edge States* | In progress → Done | Philip | Philip |
| 14:55:45.647 | `I380` *Build Verification Sheet* | In progress → Done | Philip | David |
| 14:55:45.648 | `I378` *"Verify It's You"* (parent) | In progress → Done | Philip | shared |
| 14:55:45.648 | `I381` *PIN & Biometric Verification Endpoint* | In progress → Done | Philip | Ayomikun |
| 16:11:41.684 | `I384` *Card Details Endpoint* | To do → In progress | David | Ayomikun |
| 16:11:41.686 | `I382` *Card Details* (parent) | To do → In progress | David | shared |

Nothing has happened on the board since. Board actions per day on 1002:

| 23 Oct | 26 Oct | 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct | 1 Nov | 2 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | 15 | 17 | 16 | 6 | **6** | 0 | 0 | **0** |

No comments in the window, and no description edits on `I378`–`I381` recording why they closed. `I392` still shows 63 × ☐ and 0 ticked. None of the three new Done leaves passed through REVIEW/QA, and **nothing has ever left REVIEW/QA on 1002**. No new transition entered it either, so the 7-day count holds at 10 only because all ten are from 27–28 Oct. They age out from tomorrow.

### 1.3 What the last days of 1002 hold

1002 ends **Thursday 5 Nov**. 38 of its 44 leaves are not Done: 16 in REVIEW/QA (4 with merged code), 11 In progress, 11 To do. The only precedent is 0902. It ran six days past its end date, then a 21 Oct sweep by board administration marked its 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. A repeat would record six mobile items as delivered from an unmerged branch.

---

## 2. Sprint 1002: what is in review, and whether the code exists

- **REVIEW/QA (16), unchanged:** 4 backend leaves match merged code (`I366`, `I335`, `I338`, `I341`), 3 match endpoints that already existed or show no identifiable change (`I370`, `I377`, `I358`), 6 mobile leaves have code only on `origin/BVA-I353`, and 3 are design.
- **The Verification block, now Done on the board:**

| Item | What it asks for | What exists at this report's cut-off |
|---|---|---|
| `I379` (design) | wrong PIN, lockout, no PIN, no biometrics, forgot PIN | Design files are not in git, so this cannot be checked |
| `I380` (mobile) | reusable sheet, custom keypad, biometric option, error and lockout messages | On `BVA-I353` only: `showConfirmPaymentSheet` retitled "Verify it's you". No lockout message. Its biometric path calls a route the server cannot verify (§5.11) |
| `I381` (backend) | verify PIN or biometric-backed credential, limit failed attempts with a lockout, short-lived authorization required by sensitive card endpoints | `POST /auth/step-up` from before this sprint, PIN only, no attempt limit. Reveal, unfreeze and terminate do not require its token. **No backend commit since 29 Oct** |

- **`origin/BVA-I353`:** 7 commits, last `21fe490` at 30 Oct 15:54 UTC, 4 behind `main`, **no PR**. Fixed: the fraud reason and both statement routes. The body now matches `statements.dto.ts`, and `email` is gone because delivery goes to the profile's address. **Still open:** `GET /wallets/limits` (proposed only), the three card calls (table above), and the statement screen still does not tell the user that the PDF's password is their phone number (`suggestions.md` §4.8). Support chat is still placeholder data (`TODO(support-api)`, 5 left).
- **WIP ages:** `I331`, `I354` and `I332` at 11.2 d; `I346`, `I347`, `I348` (unassigned), `I383` and `I386` at 7.0 d; `I343` and `I344` at 5.1 d; `I384` at 3.0 d.

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-02`): 149/149 consumer, 63/63 admin, proposed 37/18, spec health clean, no `x-beevia-*`. The in-repo audit still reports the 47 phantom lines from the three `diverged` working trees (18 consumer + 29 admin "in spec, not in code"), and they were not acted on.

**One `main` moved, and one tracked branch.**

| Repo | From → to | What |
|---|---|---|
| `beevia-admin` `main` | `0b41e35` → `64304ef` | *admin chat and inbox ui setup* (30 Oct 15:52 UTC, `Promise Udo`, pushed directly; this repo has no `refs/pull`). 68 files, +10,750/−11 |
| `beevia-mobile` `BVA-I353` | `a444ec9` → `21fe490` | *account statement* (30 Oct 15:54 UTC, `Davidtariq96`). 19 files, +515/−145. Unmerged |

`beevia-api` (`4c57305`), `beevia-admin-api` (`b8b6a13`), `beevia-db-schema` (`2fbf657`, v0.0.45) and `beevia-mobile` `main` (`ccb4f63`, 22 Oct) did not move. **No new PR on any repo.**

### 3.1 The inbox contract against the API that exists

`/support/inbox` lists disputes and support chats in one queue. `docs/hs7-support-inbox-api-contract.md` is explicitly a proposal. The dispute half collides with #24:

| | Inbox proposal | Server today |
|---|---|---|
| Route | `/admin/support/conversations*` (9 operations) | `/admin/disputes*` (3 operations) |
| Reasons | `amount_wrong`, `didnt_make_this_transaction` | `wrong_amount`, `not_my_transaction` (the other five match) |
| Status | `in_progress`, `resolved` | `submitted`, `under_review`, `resolved`, `rejected` |
| Closing | `{status}` only | `resolved` or `rejected` **requires a `note`** |
| Claiming | atomic, named holder, `409 already_claimed` | anonymous and unguarded (`suggestions.md` §4.11.5) |
| Search | user's full name | transaction reference |
| Replies | `POST …/messages` | none (`I344`, In progress) |

`BVA-I350` (To do) describes something close to the proposal, so the right answer may well be to build it, with disputes adapted behind it. That is a decision for Promise and Ayomikun, not this report. Whichever route wins, the reason codes and `rejected` need to agree. The contract's premise that support threads are not end-to-end encrypted **is** on the board (`BVA-I342`'s acceptance criteria). It is a deliberate carve-out from PRD §"End-to-end encryption on every conversation", and worth keeping visible as one.

### 3.2 The mock's default

`USE_MOCK_SUPPORT_API` is `NEXT_PUBLIC_USE_MOCK_SUPPORT_API !== "false"`. The older flag is `NEXT_PUBLIC_USE_MOCKS === "true"`, the opposite default. Dev panels check `NODE_ENV`; the adapter and its seed data do not. So a production build that does not set the flag ships a convincing inbox of invented users. No deploy config is in this repo, so whether that build exists cannot be seen here.

### 3.3 Document changes this cycle

- **`suggestions.md`**: new §5.16 (the inbox contract, the mock default, the missing server half); updates to §4.11, §5.14 (statement row closed) and §5.15 (fraud reason fixed, Verification block closed without the backend).
- **`admin-api-rfc.md`**: §3.15 and §3.16 no longer say the dashboard has no dispute screen or no recent commit.
- **The four OpenAPI specs: no change.** Route drift is clean and no backend moved. **The inbox's 11 operations were deliberately not added to `openapi.admin.proposed.yaml`:** the contract says nothing in it is confirmed, and writing it into the spec would pre-empt the choice in §3.1. Add it once that is made.
- `api-rfc.md` needed no change.

### 3.4 The standing checks

- **Pipelines:** no workflow change; `beevia-api`, `beevia-admin-api` and `beevia-db-schema` have the same SHAs as 30 Oct, so all three still deploy or migrate on push with no test gate.
- `PaymentService.activeNgn()`, `StubTranslateAdapter`, unmapped `22P02`, unindexed `messages.ref_id`, FAQ search's missing `en-US` fallback, and no grant of `help_center` or `disputes`: all unchanged (same SHAs).
- **Mobile:** `main` is unchanged. **`call.ended` is still unhandled** on `main` and on `BVA-I353`. The biometric step-up (`wallet_service.dart`) is unchanged.

---

## 4. Risks

- **1002 ends Thursday with nothing accepted and no successor sprint.** A sweep like 0902's would mark unmerged and mis-wired work as delivered (§1.3).
- **Done on the board now hides open work.** `I381`'s lockout does not exist, so **guessing a 4-digit PIN against `/auth/step-up` has no limit visible in the code** (no throttler anywhere in `src`). That token guards card creation and PIN reveal.
- **Two contracts for one queue.** Each week both sides build on their own version, reconciling costs more (§3.1).
- **The inbox's mock is on by default** (§3.2).
- **Disputes can be filed and cannot be answered.** Five days now. Every complaint about money waits with no reader except direct database access, and the PRD's 72-hour KPI is counting.
- **The FAQ is still empty in production** until someone grants `help_center` and enters content. It still has no admin screen.
- **Blocking does not reach payments.**
- **Every backend repo still deploys or migrates production on push without a test gate.**
- Carried, unchanged: `call.ended` unconsumed; statement PDF password (§4.8); FAQ search fallback (§4.10); card spending not disputable (§4.11); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points. The new support screens serve the PRD's dispute handling and support needs. They do not touch these four.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 26 Oct 15:01 → 2 Nov 15:01 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Median cycle times are carried from 30 Oct: no item entered REVIEW/QA since, so they cannot have changed, and the 20 Oct 0902 scratch file that fed them has been cleared from `/tmp`.

### 6.1 Ayomikun Araoye: backend + admin API

**16 commits in 7 days**: 9 in `beevia-api`, 4 in `beevia-db-schema` and 3 in `beevia-admin-api`, all from 27–29 Oct. None since #88. **5 own submissions** (`I366`, `I358`, `I335`, `I338`, `I341`) and 5 moves on David's and Philip's items. Median cycle **0.99 d (n=20)**. WIP: `I332` (11.2 d, past their median; the open-dispute count still has no route), `I347` (7.0 d), `I344` (5.1 d), `I384` (3.0 d, moved there with its parent, so not evidence that work began). `I381` left their WIP through the parent's close, not through a move of their own. Three days without a backend commit, after a run of daily merges and across a weekend, is not a signal by itself. `BVA-I8` has been In progress on the closed admin board for 49.0 days.

### 6.2 David Samuel: mobile

**0 commits on `main`** in the window (the last, `8039bd7`, was 21 Oct). **6 on `origin/BVA-I353`** in the window, 7 on the branch in all, the latest at 30 Oct 15:54 UTC. It closes the fraud-reason and statement mismatches this report has been raising, and its commit moves the mock and contract test in step. **Zero own submissions**: the last was `I286` on 14 Oct, **18.9 days** ago. Their four 7-day "submissions" were moved by Ayomikun, and `I380`'s Done was made by Philip. Median cycle **0.99 d (n=40)**. WIP: **6 items**, still the most on the board, with `I331` and `I354` at 11.2 d. The branch holds the code for six REVIEW/QA leaves and five In progress ones (`I331`, `I354`, `I383`, `I386`, `I343`), and none of it is reviewable until it has a PR.

### 6.3 Philip Chidera: design

Closed `I378` and its children on 30 Oct. One 7-day submission, moved by Ayomikun on 27 Oct. **Zero WIP** with one leaf To do: finished, blocked or working untracked. Worth a question, not an assumption. `I392` remains Done with no ticks, which is still a question about how the board records review. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**1 commit**, `64304ef` on 30 Oct: two features under `src/features/support-inbox` and `src/features/support-triage`, two API contract documents, and a README section that names its own open assumptions. The screens match `BVA-I349` and `I348` by content, although both still show no assignee and `I349` still says To do, so **the board shows none of this**. The mapping from Promise's `HS6-AD`/`HS7-AD` labels to those items is inferred. FAQ content (`I351`) still has no screen. `BVA-I9` has been In progress on the closed admin board for 49.0 days.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (26 Oct → 1 Nov) | — | — | **10** | 5 | 5 | 0 |
| 2026-W45 (from Mon 2 Nov, to 15:01 UTC) | — | — | **0** | 0 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by someone other than its submitter since `BVA-I268` on 16 Sep. `I380` and `I381` were closed by someone other than their owner, but they skipped review, so they are not exceptions. Output was steady through W44, and acceptance stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Six WIP items for David and four for Ayomikun are not comparable loads. Nor does one commit of 10,750 lines compare with sixteen smaller ones.
- **Unpushed and untracked work.** Today's lead finding is the proof: 38 quiet days produced this commit.
- **Who moved an item is not whether it is done**, or whether it was verified.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The new test files were read, not run.

---

## 7. Previous recommendations: where they stand

| Recommendation from 30 Oct | Status on 2 Nov |
|---|---|
| **1. Plan 1002's close before Thursday** | ❌ **Not visible.** No successor sprint; nothing moved out of review; `ZOHO_SPRINT_FILTER` still 08-01 |
| **2. Grant `disputes` and `help_center`** | ❌ **Not visible.** No db-schema or admin-api change |
| **3. Fix `didnt_make_transaction` and open a PR** | 🟡 **Half.** Fixed on the branch (`21fe490`), with both statement routes too. **No PR** |
| **4. Decide the card verification model** | ❌ **Not visible, and now harder to see.** The Story closed without it (§2) |
| **5. Reopen `I392`** | ❌ **No.** Still Done, 0 of 63 ticked |
| **6. Close the payments half of blocking** | ❌ **Not done** |
| **7. Disputes follow-ups** | ❌ **Not done** |
| **8. Give the admin dashboard a home** | 🟡 **Half.** The work is plainly not paused and the inbox screen exists. `I349`/`I348` are still unassigned, FAQ has no screen, no admin sprint |
| **9. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done** |
| **10. Generate `openapi.yaml` from the app; stop vendoring the client spec** | ❌ **Not done** |
| **11. Handle `call.ended` on the client** | ❌ **Not done** |
| **12. Carried items** | ❌ **None moved** |

**Two of twelve moved, both partly**, and both by people working from their own list rather than this one. That is fine. The window also included a weekend.

---

## 8. What I would do this week

1. **Plan 1002's close before Thursday (carried).** Review the four REVIEW/QA leaves with merged code and accept or return them. Move the six branch-only mobile leaves back to In progress until `BVA-I353` merges. Create the successor sprint, carry the remainder into it explicitly, and do not sweep. Then set `ZOHO_SPRINT_FILTER` to the new sprint.
2. **Reopen `I380` and `I381` if the close was not meant for them (new)**, and decide the card verification model before they restart. Whatever else is decided, add an attempt limit to `/auth/step-up`.
3. **Have Promise and Ayomikun go through `hs7` and `hs6` together (new).** Settle the route, reason codes, `rejected` and the required note before `I347`/`I350` go further, then add the agreed routes to `openapi.admin.proposed.yaml`.
4. **Assign `I348` and `I349` to Promise (new)**, so the board shows the work, and add an admin-board sprint or say the consumer board is the home.
5. **Default the support mock off in production builds, or show a banner while it is on (new).**
6. **Open a PR for `BVA-I353`**, splitting it if needed: the FAQ, dispute, block and statement half looks ready, and the card half waits on item 2.
7. **Grant `disputes` and `help_center`** to Super Admin and the support role (`suggestions.md` §4.10.1, §4.11.1). Disputes first.
8. **Reopen `I392`** until its boxes reflect what was verified, and agree who ticks such checklists (not the builder).
9. **Close the payments half of blocking** (`suggestions.md` §4.9).
10. **Disputes follow-ups:** let card spending be disputed, store the transaction type, notify the user on an answer, and make the admin answer conditional (§4.11).
11. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job.
12. **Generate `openapi.yaml` from the running app and diff it in CI** (§5.4), and stop vendoring the client spec (§5.10).
13. **Handle `call.ended` on the client.**
14. **Carried:** add the `en-US` fallback to FAQ search; decide the statement password and delivery model (§4.8); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 49.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 49 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002, as unassigned Stories: `I349` Support Inbox (To do, screen on mock data), `I348` Triage Flow Configuration (In progress, screen on mock data) and `I351` FAQ CMS (To do, API only). `beevia-admin` last moved 3.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed sixty-two days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. Line 11 is the one to explain: `64304ef` is a large, real addition to the dashboard, but the rubric gives screens that do not reach an API at most ~0.1 over nothing, and every call in it is answered by a mock unless a flag is changed. Line 11 scores the admin surface already wired, stays at 0.97, and does not fall either, because nothing regressed. Line 9's client work is still unmerged.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No backend or mobile `main` change |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No server card change. Client card management on unmerged `BVA-I353`; auth model undecided |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | `64304ef`'s support screens run on mock data and reach no server route; dispute queue and FAQ admin still have no role |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether closing `I378` was meant to close `I380` and `I381`.** No comment or description edit explains it. Same-millisecond timing is what suggests a parent's close, and that is inference.
- **Whether a server-side attempt limit exists outside `assertPin`**, such as at a proxy or rate limiter in front of the API.
- **Whether a production build of `beevia-admin` exists**, and with which flag. No deploy config is in the repo.
- **Whether any role was granted `disputes` or `help_center` by hand**, and whether any dispute has been filed.
- **When `64304ef` was written.** One commit, one date; everything before it is invisible.
- **Whether the new tests pass, or whether the new screens render.** Nothing was executed.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items on 5 Nov.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel as three background calls, starting at 15:01 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical to 30 Oct. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` fast-forwarded +1 commit, `beevia-mobile` was already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-02`: exit 0. The in-repo audit ran too, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`q02.py`, `flow02.py`): a diff of 1002 against 30 Oct, every action since 29 Oct 11:00 UTC, 7-day submissions split by actor, WIP ages, the weekly trend, and a search for any transition out of REVIEW/QA. The sprint lists came from the `__nonexistent__` dry run.
5. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` of `refs/pull/*` on every repo, and the remote-tracking reflogs. In `beevia-admin`: `64304ef`'s file list, both contract documents, README, `constants.ts`, `api.ts`, the role and socket changes. In `beevia-admin-api`/`beevia-api`: the dispute controllers and DTOs, `assertPin`, `stepUp`, card guards, statement DTO, and a search for support tables and controllers. In `beevia-mobile`: `21fe490`'s diff and the verification sheet's call sites. Sidecar and CSV: `I342`, `I345`–`I351`, `I378`–`I384`.
6. `suggestions.md` and `admin-api-rfc.md` updates (§3.3). No OpenAPI change.
7. This report and its web edition.
8. End-of-run recheck at 15:08 UTC. A fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 30 Oct 16:11 UTC. `ls-remote` showed every `main` and `BVA-I353` at the commits read above, and no new PR on any repo.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `reflog`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-02.html`, `web-report/index.html`, `suggestions.md`, `admin-api-rfc.md`, plus new board exports for 2 Nov in `sprint-board-exports/` and `sprint-board-exports/admin/`. The `beevia-admin` working tree fast-forwarded to `64304ef`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The 20 Oct 0902 scratch file has been cleared from `/tmp`**, so median cycle times were carried from 30 Oct rather than recomputed (without it the script gives n=31 and n=16). No item entered review since, so the medians cannot have changed. The older rows of the weekly table are carried too.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 30 Oct 14:03 UTC → 2 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
