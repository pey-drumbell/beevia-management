# Beevia — Project Status

**As of 2026-11-16** · Sprint **1002** (21 Oct → 5 Nov, **ended eleven days ago, day 27**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-16.csv` + `beevia-activity-2026-11-16.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-16.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 13 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 13 Nov 15:03 UTC → 16 Nov 15:05 UTC, 3.0 days (Fri → Mon).**

---

## Quick overview

> **Message editing and a working "delete" landed on the server this morning, and the app on `main` can use only part of it. `beevia-api` #112 (on `beevia-db-schema` 0.0.55) adds `PATCH /messages/{id}` to edit a sent text, lets a recipient "delete for me", and makes "delete for everyone" reach the other person's phone. Per the commit, until today it reached nobody. The app on `main` handles the live delete. It cannot edit, ignores the catch-up that tells an offline phone about deletes, and misreads `deleted_for`. The board has had no action for 5.3 days, 1002 is eleven days past its end, and none of its 33 review items has been accepted. The Forgot PIN client is still on a branch with no pull request.**

| Metric | 13 Nov | 16 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 13 Nov; last action 11 Nov 06:53 UTC (**5.3 days**) |
| Transitions into REVIEW/QA, last 7 days (leaves) | 1 | **1** | `I362`, by its owner, 11 Nov |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **33.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin), before today's edits | 0 / 0 | **1 / 0** | `PATCH /messages/{id}`; added |
| API surface (consumer / admin) | 165 / 76 | **166 / 76** | +1 edit; `DELETE /messages/{id}` and message history changed in place |
| WebSocket commands (consumer) | 46 | **47** | `message.edit` |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain; no auth file changed |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | migration 0055 rewrote existing message rows through it |
| `beevia-admin` days since a commit | 14.0 | **17.0** | |
| `beevia-mobile` days since a commit on `main` / on any branch | 3.0 / 1.3 | **6.0 / 4.3** | `feat-forget-pin-fixes` unchanged since 12 Nov 06:49 UTC; still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 1.0 / 6.1 / 2.0 | **0.1 / 9.1 / 0.1** | #112 and #36 today |
| Admin board: open sprint / days since any activity | none / 60.0 | **none / 63.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: editing has no client yet; the delete changes fix an existing feature (appendix) |

**Correction to earlier editions and to the workspace spec.** `openapi.yaml` has described `Message.deleted_for` as a list of user ids, "always empty today", since message deletion shipped in August. The server has always sent a single string (`none`, `sender` or `everyone`). `DELETE /messages/{id}` was documented as returning `{ removed }`, but it returns `{ message_id, deleted_for }`. #112's commit says the Postman example had the same list shape and that the app followed it. Both are fixed today. No report had claimed that "delete for everyone" reached the other person. None had checked, either, and per #112's commit it did not.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **1 own** (`I362`) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**63.0 d**) | **12** (10 `beevia-api`, 2 `beevia-db-schema`) | #112 and #36 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**25.2 d**), `I361` (13.3 d). Both have code on `main` | **3** (`c04e207`, `36b03ff`, `3e23414`) | Forgot PIN branch 4.3 days unchanged, no PR. Last own submission 33 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 14.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**63.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 17.0 days; possibly unpushed work |

**The three questions for standup:** (1) **Who builds the app side of #112, and is it on the board?** Edit, catch-up `changes` and the `deleted_for` string are server-ready with no client and no item. (2) **When does `feat-forget-pin-fixes` get a PR?** It has been unchanged for 4.3 days, and the PIN lock it is the way out of has been live since 12 Nov. (3) **Who reviews the 24 REVIEW/QA leaves with merged code?** The board has had no action for 5.3 days.

**The three things worth knowing:**

1. **Deleting a message did not reach the other person. From today it does, on an open socket.** #112's commit says `message.deleted` went to a conversation room the app never joins, so "delete for everyone" changed only the server. It now goes to every member's devices, and the attached files are deleted. The app on `main` deletes by id when the event arrives, so this should work without an app release. A recipient can now "delete for me" too; until today that was a `403`. Read, not run (§3.1).

2. **Editing and offline catch-up are server-only.** `PATCH /messages/{id}` and `message.edit` let a sender change a text within 15 minutes, and history with `afterSeq` now returns `changes`, which tells a phone that was offline what was edited or deleted. The app on `main` has no edit action and no `message.edited` handler, and it reads only `messages` on catch-up. It also reads `deleted_for` as a list of user ids, so history rows deleted for everyone are not removed. None of this has a board item (§3.1, `suggestions.md` §4.20).

3. **5.3 days with no board action, eleven days after 1002 ended.** The last action was 11 Nov 06:53 UTC. 24 of 33 REVIEW/QA leaves have merged code, and nothing has ever left review on 1002. Output continues in code (#110, #111, #112, the client branch) while acceptance stays at zero. The bottleneck is still the review step, not the developers (§1, §2).

**If you read nothing else:** put the app side of #112 on the board with an owner, get `feat-forget-pin-fixes` into review, and spend this week's review time on the 24 items whose code is on `main`.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 13 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **No action in the window.** The 1002 sidecar is byte-identical to 13 Nov, and so is the CSV apart from its date line. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–13 Nov | 14–16 Nov (to 15:05) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 Eleven days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902, the one precedent, was swept six days after its end. 1002 is now five days beyond that, with no sweep and no successor. A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111 (the unreadable-message count), #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes`; Dependabot PRs #59–#63. That is a gap in the board, not a judgement on the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

Unchanged since 11 Nov.

| REVIEW/QA leaves (33) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | 12 | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391`, `I362` | Routes on `origin/main`. `I387` caps funding, not spending. `I391` lacks the pagination, search and filter it asks for. `I362` reports limits and does not enforce them |
| Mobile, matching merged code | 12 | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, `I386` | On `main` since #58 (10 Nov). `I390` is still unassigned |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Moved to review, no matching code | 2 | `I348`, `I372` | `I348`: the dashboard screen is mock only. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 25.2 d and 13.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: one drift line, fixed.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-16`), the first run reported `beevia-api` code=166, spec=165, with `PATCH /messages/{}` undocumented (exit 1). After today's edit it reported 166/166 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). The in-repo audit still reports phantom lines from the three `diverged` working trees. They were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `a4b11cb` → `a5cf9b5` | #112 (merged 16 Nov 13:35 UTC): edit messages; delete for me for any member; deletes and edits reach every device and catch-up |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50 |
| `beevia-db-schema` `main` | `a871f3e` (v0.0.54) → `bcc45fb` (**v0.0.55**) | #36 (merged 11:47 UTC): `message_hides`, `messages.changed_seq`, and a data migration |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `e40116d` | Unchanged. `feat-forget-pin-fixes` unchanged at `3e23414`, no PR (pull refs end at #63) |

### 3.1 Message editing and deletion (`beevia-api` #112, `beevia-db-schema` #36)

- **Editing (new).** `PATCH /messages/{id}` and the `message.edit` socket command. The sender re-encrypts the new text exactly as for a send. It replaces the stored blob and every envelope, sets `edited_at`, and `message.edited` goes to each recipient device with its own ciphertext. Text only, the sender's own messages, within `MESSAGE_EDIT_WINDOW_MINUTES` (default 15; `0` means no limit). The errors are `403 not_message_sender`, plus `400 message_not_editable`, `message_deleted` and `edit_window_closed`. A blocked conversation refuses it. The server still sees no plaintext, only that an edit happened and when.
- **"Delete for me" for anyone.** It was a `403` for anyone but the sender, because `deleted_for` was one scope on the message row (`api-rfc.md` §5.2 had suggested a per-user table). It is now a row in `message_hides`: any member, any message, hidden on the caller's own devices only. The migration moved every old `sender`-scoped deletion into that table and reset the message rows to `none`.
- **"Delete for everyone" reaches the other person.** According to the commit, `message.deleted` went to the conversation room, which the app never joins. Payment cards' `message.updated` had the same problem. Both now go to every member's devices. A message deleted for everyone also loses its attached files. Calls, payment cards and notices cannot be deleted for everyone (`400 message_not_deletable`).
- **Catch-up.** History and `sync.messages` with `afterSeq` now return `changes`, the live event for each older message edited or deleted since the cursor. Before this, a phone that was offline learned of neither.
- **Smaller fixes in the same PR:** hidden messages are left out of the viewer's pages and inbox preview; deleted and hidden messages no longer count as unread; the media gallery skips them; socket errors arrive as text in the user's language rather than as catalogue keys.
- **The client on `main`, read and not run.** `_handleMessageDeleted` removes a message by id when the live event arrives, whatever its scope. Delete for everyone should therefore now reach a recipient whose app is connected, with no release needed. There is no edit action, no `message.edit` call and no `message.edited` handler. The catch-up loop (`fetchPendingMessages(afterSeq: …)`) reads `messages` and ignores `changes`. `deleted_for` is parsed as a list of user ids or a `deleted_for_everyone` flag, and the server sends neither: it sends the string `everyone`. A phone that was offline when a message was deleted therefore keeps it. `feat-forget-pin-fixes` has the same code, and no other branch touches it.
- **Read, not run.** The commit reports a new end-to-end test (`test/message-changes.e2e-spec.ts`, two users, four devices, one offline throughout). It was not executed here.

### 3.2 The standing checks

- **PIN lock (#110):** no auth file changed in `a4b11cb..a5cf9b5`. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists (`ThrottlerModule`, `express-rate-limit`: no match).
- **`beevia-api` `release.yml`**: read. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. It deploys and runs `pnpm db:migrate` on push to `main`. No workflow file changed in `a4b11cb..a5cf9b5`. #112 bumped the schema pin to 0.0.55, so **migration 0055, which rewrites existing message rows, ran through the ungated path.** `beevia-db-schema`'s Release published 0.0.55 on the merge, as before.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is now on 0.0.55. Five versions apart.
- **Branch protection, PR reviews and CI results**: cannot be seen from here.

### 3.3 Document changes this cycle

`openapi.yaml`: new `editMessage` (`PATCH /messages/{messageId}`) with an `EditMessageRequest` schema. `deleteMessage` rewritten: new semantics, `400 message_not_deletable`, `403 not_message_sender` and the real response shape. `Message.deleted_for` corrected from an array to a string enum. `MessageHistory.changes` added, with a `MessageChange` schema. `getMessageHistory` describes hidden messages and `changes`. `openapi.admin.yaml`, `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` are unchanged. `api-rfc.md`: totals 165 → 166, a new §5.28, an update under §5.2, the §6.8 rows, and the §6.9 command count, re-counted at 47. The count of 38 there dated from 28 Sep. `suggestions.md`: new §4.20. `admin-api-rfc.md`: unchanged.

---

## 4. Risks

- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A locked-out user has no way out on `main`.** The lock is live, and the app's Forgot PIN on `main` still says "coming soon". The client branch has no PR and has not changed for 4.3 days.
- **New: a deleted message survives on a phone that was offline.** The server now sends what is needed (`changes`, and `deleted_for: "everyone"` in history). The app reads neither (`suggestions.md` §4.20).
- **New: a production data migration with no test gate.** 0.0.55 rewrote `deleted_for = 'sender'` rows into a new table on push. Whether it ran cleanly is not visible.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended eleven days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment. Unchanged.
- **The 30-day NIN clock.** The client is on `main`. Whether it has shipped to users is not visible, and the limits are still not enforced. The grace for existing users ends about 6 Dec.
- **A user can be told a person is coming when none can come.** No role holds `disputes`. Unchanged.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** none.

---

## 5. PRD gap

The four structural gaps are unchanged and carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. #112 extends E2EE messaging (line 1) and does not touch any of them. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 9 Nov 15:04 → 16 Nov 15:04 UTC. Commit counts are non-merge commits on all remote refs in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (2 on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**12 commits in 7 days**: 10 in `beevia-api` and 2 in `beevia-db-schema`. The drop from 16 is the window moving past 6–9 Nov. **One own submission**, `I362` on 11 Nov. **No WIP on 1002.** Since the last cut-off he has shipped `beevia-api` #112 and `beevia-db-schema` #36, and neither is an item on any board. His last commit is 0.1 d old. `BVA-I8` has been In progress on the closed admin board for 63.0 days.

### 6.2 David Samuel: mobile

**3 commits** in 7 days: `c04e207` (9 Nov, on `main` via #58) and the two on `feat-forget-pin-fixes` (11 Nov 19:09, 12 Nov 06:49 UTC). Nothing was pushed in the window, which included a weekend. **Zero submissions.** His last own submission was `I286` on 14 Oct, **33.0 days** ago. **WIP: 2 items, both with code on `main`**: `I331` at 25.2 days and `I361` at 13.3 days. As before, this reads as items left in the wrong column rather than stuck work; that is for him to say. Today's server change gives the app three new pieces of work (§3.1), none of which is on the board. Local commits are invisible here.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** His last board action was on 2 Nov 15:58 UTC, **14.0 days** ago: he may be finished, blocked or working untracked. Worth a question, not an assumption. Message editing now has a server and no design item, like Forgot PIN, the PIN lock message and voice-note recording before it. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **17.0 days** old, and `beevia-admin` has no new branch or pull ref. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee; `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 63.0 days.

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
| 2026-W46 (9 → 15 Nov) | — | — | **1** | 1 | 0 | 0 |
| 2026-W47 (16 Nov, to 15:05 UTC) | — | — | 0 | 0 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. Output continues in code; acceptance stays at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** #112's 1,476-line change and a one-line fix count the same.
- **Who moved an item is not whether it is done.**
- **Untracked work.** #110, #111, #112, #36 and `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits.** #112 is a single commit.
- **Unpushed work.** A weekend with no remote commit says nothing about local work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 13 Nov | Status on 16 Nov |
|---|---|
| **1. Open a PR for `feat-forget-pin-fixes` and review it** | ❌ **No.** Branch unchanged since 12 Nov, no PR |
| **2. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No auth file changed |
| **3. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No board action at all** |
| **4. Close 1002 deliberately** | ❌ **Not done, eleven days late.** No successor, no sweep, filter still 08-01 |
| **5. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No.** No limiter in `beevia-api` |
| **6. Two-device chat on a real build; call each new route; handle three NIN errors** | ❌ **Not visible.** #112's commit reports a two-user, four-device e2e test on the server; the app was not shown to have run |
| **7. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **8. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **9. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **10. Handle `call.ended` in the app** | ❌ **No** |
| **11. NIN step, support screens and Forgot PIN on the board** | ❌ **No** |
| **12. Decide whether the tier limits are enforced** | ❌ **No** |
| **13. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **14. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **15. Record the consent behind each lookup** | ❌ **No** |
| **16. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **17. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **18. Bring the dashboard onto the real contract** | ❌ **No commit in 17.0 days** |
| **19. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **20. Parent status moves; assign `I348`, `I349`, `I351`, `I359`, `I390`; admin sprint** | ❌ **No** |
| **21. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **22. `needs: test` on `sync`; current schema on `beevia-admin-api`** | ❌ **Not done.** #112 and its data migration went through the ungated path; admin-api is now five schema versions behind |
| **23. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** Today's route was caught by the audit. The `deleted_for` shape error had gone unnoticed since August, and a generated spec would have caught it |
| **24. Carried items** | ❌ **None moved.** #112 does close an old point from `api-rfc.md` §5.2 (recipient "delete for me") that was not on this list |

**None of the 24 is met, and none moved in part.** #112 was not on the list. It fixes two problems the reports had not raised and one they had (§5.2).

---

## 8. What I would do this week

1. **Put the app side of #112 on the board, with an owner and a design (new).** Three pieces: read `changes` on catch-up, read `deleted_for` as the string the server sends, and add edit (`message.edit`, `message.edited`). The first two are what make delete work for a phone that was offline. Encrypt an edit to the current device list, as for a send (`suggestions.md` §4.20).
2. **Open a PR for `feat-forget-pin-fixes` and review it (carried).** It is the only way out of the lock for users on `main`. Ask whether the in-app Paystack WebView was a decision.
3. **Make the PIN check reserve its attempt before comparing (carried).** Use one conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
4. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
5. **Then close 1002 deliberately (carried, eleven days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and items for #35, #110, #111, #112 and the branch. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
6. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
7. **Run one two-device chat on a real build (carried, widened).** Delete a message for everyone with the other phone online, then again with it offline, and check both phones. Check also that the "can't be shown" banner appears only for history sent before a device existed. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
8. **Confirm migration 0055 ran cleanly in production (new).** Look for rows still marked `deleted_for = 'sender'` and for a `message_hides` count that matches.
9. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
10. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
11. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
12. **Handle `call.ended` in the app (carried).**
13. **Put the NIN step, the support screens and Forgot PIN on the board with a design and an owner (carried).**
14. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
15. **Decide the seeded card default and what a card limit is, on the record (carried).**
16. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
17. **Record the consent behind each BVN and NIN lookup (carried).**
18. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
19. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
20. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
21. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
22. **Agree how parent status moves work; assign `I348`, `I349`, `I351`, `I359` and `I390`; give the admin dashboard a sprint (carried).**
23. **Retire `GET /cards/{id}/transactions` (carried).**
24. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.55 (carried).
25. **Generate `openapi.yaml` from the running app and diff it in CI (carried).** It would have caught the `deleted_for` shape error three months ago.
26. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 63.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 63 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 17.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-six days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** #112 touches line 1 (E2EE messaging) in two ways, and neither moves it. Editing is new, but it has no client: the rubric scores a flow that is wired from screen to API, and a server route alone is not one. The delete changes make an existing feature work across devices. That is a correctness fix, which the rubric does not score. Line 1 stays at 0.90 for the voice-note recorder, still on an unmerged branch. When the app can edit and reads `changes`, line 1 can be reconsidered.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | #112: edit (server only) and cross-device delete; the voice-note recorder is on a branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Payment-card updates now reach every device (#112); biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether #112 is live, whether migration 0055 ran cleanly, and whether delete now reaches the other phone in practice.** The workflow deploys and migrates on push; its result is not visible, and nothing was run.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether any of the merged or branched client screens work against the API.**
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the pull requests were reviewed or approved.**
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag, on the in-app Paystack checkout or on the 15-minute edit window, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. A sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects), then three background exports starting at about 14:57 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 13 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical and CSV identical apart from its date line. 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-16`: exit 1 before the spec edit (one undocumented route), exit 0 after. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow16.py`, a date-shifted copy of 13 Nov's). It diffed 1002 against 13 Nov, listed every action in the window (none), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `fetch` and `ls-remote` of heads and `refs/pull/*` in all five repos. In `beevia-api`: #112's commit message, controller, DTO, service (`edit`, `remove`, `sync`), `visible-to.ts` and `env.ts`; that no auth or workflow file changed; the absence of any HTTP rate limiter; `release.yml`; both services' schema pins; the `@SubscribeMessage` count before and after. In `beevia-db-schema`: migration 0055 and the schema. In `beevia-mobile` (`main` and `feat-forget-pin-fixes`): how `deleted_for`, `message.deleted`, `message.edited` and catch-up are handled.
6. Spec and narrative updates (§3.3).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`merge-base`. Nothing was committed, pushed or deployed. A final `fetch` of all five repos at 15:08 UTC found nothing new, and a fast 1002 re-export at the same time found no board action (last `actiontime` still 11 Nov 06:53 UTC).

**Files changed this cycle:** this report, `web-report/2026-11-16.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md` and `suggestions.md`. New board exports for 16 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 13 Nov 15:03 UTC → 16 Nov 15:05 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (−07:00).
