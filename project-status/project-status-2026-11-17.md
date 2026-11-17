# Beevia — Project Status

**As of 2026-11-17** · Sprint **1002** (21 Oct → 5 Nov, **ended twelve days ago, day 28**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-17.csv` + `beevia-activity-2026-11-17.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-17.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 16 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 16 Nov 15:05 UTC → 17 Nov 15:02 UTC, 1.0 day (Mon → Tue).**

---

## Quick overview

> **The app side of yesterday's message editing was written overnight, but on a branch. It has not reached `main`. `beevia-mobile` `feat-forget-pin-fixes` gained one 47-file commit (`d55630e`, 17 Nov 05:51 UTC). It adds editing, reads the catch-up `changes`, and reads `deleted_for` as the string the server sends: all three gaps named yesterday. It also adds forwarding, starred messages and a voice-note waveform. The branch is now 109 files and about 7,400 added lines ahead of `main`, and it has no pull request. Nothing else moved: no commit reached `main` in any repo, and the board has had no action for 6.3 days. Sprint 1002 is twelve days past its end, and none of its 33 review items has been accepted.**

| Metric | 16 Nov | 17 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 16 Nov; last action 11 Nov 06:53 UTC (**6.3 days**) |
| Transitions into REVIEW/QA, last 7 days (leaves) | 1 | **1** | `I362`, by its owner, 11 Nov |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **34.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin) | 1 / 0, added | **0 / 0** | audit clean, exit 0 |
| API surface (consumer / admin) | 166 / 76 | **166 / 76** | no backend commit |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| App side of #112 (edit, catch-up `changes`, `deleted_for`) | none anywhere | **written on a branch; not on `main`** | `d55630e`, no PR |
| `feat-forget-pin-fixes` ahead of `main` | 2 commits | **3 commits, 109 files, +7,443 / −774** | still no PR (pull refs end at #63) |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | `release.yml` re-read; unchanged |
| `beevia-admin` days since a commit | 17.0 | **18.0** | |
| `beevia-mobile` days since a commit on `main` / on any branch | 6.0 / 4.3 | **7.0 / 0.4** | `d55630e` on the branch |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 / 9.1 / 0.1 | **1.1 / 10.1 / 1.1** | |
| Admin board: open sprint / days since any activity | none / 63.0 | **none / 64.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: the rubric scores `main`, and nothing reached it (appendix) |

**No correction to the previous edition.** Its claims about the app were about `main`, and they still hold there. One sentence is out of date: "`feat-forget-pin-fixes` has the same code, and no other branch touches it." Since 05:51 UTC today, that branch does handle edit and delete.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **1 own** (`I362`) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**64.0 d**) | **9** (7 `beevia-api`, 2 `beevia-db-schema`) | #112 and #36 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**26.2 d**), `I361` (14.3 d). Both have code on `main` | **3**, all on `feat-forget-pin-fixes` (`36b03ff`, `3e23414`, `d55630e`) | Branch now 7,400 lines ahead with no PR. Last own submission 34 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 15.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**64.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 18.0 days; possibly unpushed work |

**The three questions for standup:** (1) **When does `feat-forget-pin-fixes` become a pull request, and should it be split first?** It now holds Forgot PIN, the app side of #112, forwarding, starred messages and voice-note work in one branch of 109 files. (2) **Can the edit/delete work go on the board?** The code exists now, and an item would let it be reviewed and accepted like the rest. (3) **Who reviews the 24 REVIEW/QA leaves with merged code?** The board has had no action for 6.3 days.

**The three things worth knowing:**

1. **Yesterday's three client gaps are written, on a branch.** `d55630e` adds an edit action: text only, the sender's own messages, within 15 minutes. It sends `message.edit` with `{requestId, messageId, envelopes}`, which matches the server's `wsEditMessageSchema`, and it handles `message.edited`. The catch-up loop now applies each `changes` entry, and `deleted_for: "everyone"` removes the message. Edit envelopes use the same builder as a send. Read, not run (§3.1).

2. **None of it reaches users until the branch is merged, and the branch keeps growing.** It started as Forgot PIN on 11 Nov. With no pull request, it is now 3 commits, 109 files and about 7,400 added lines ahead of `main`. The longer it stays unmerged, the larger the eventual review becomes. Meanwhile users on `main` still have the PIN lock with no way out, and a phone that was offline still keeps messages deleted for everyone (§3.1, §4).

3. **6.3 days with no board action, twelve days after 1002 ended.** The last action was 11 Nov 06:53 UTC. 24 of 33 REVIEW/QA leaves have merged code, and nothing has ever left review on 1002. Code keeps arriving (#112 yesterday, the branch today) while acceptance stays at zero. The bottleneck is still the review step, not the developers (§1, §2).

**If you read nothing else:** open a pull request for `feat-forget-pin-fixes` (or split it into PIN reset, edit/delete and the chat extras), put that work on the board, and spend this week's review time on the 24 items whose code is on `main`.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 16 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change (0 left review, 0 newly Done, 0 entered review). 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. Zoho lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **No action in the window.** The 1002 sidecar is byte-identical to 16 Nov, and so is the CSV apart from its date line. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–17 Nov (to 15:02) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 Twelve days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902, the one precedent, was swept six days after its end. 1002 is now six days beyond that, with no sweep and no successor. A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111 (the unreadable-message count), #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes`, which now also carries the app side of #112, forwarding and starred messages; Dependabot PRs #59–#63. That is a gap in the board, not a judgement on the work.

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

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 26.2 d and 14.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-17`), it reported 166/166 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). No spec file was edited. The in-repo audit still reports phantom lines from the three `diverged` working trees (2 / 37 / 42). They were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `a5cf9b5` | Unchanged. `feat/message-edit` and `feat/voice-notes` are still on the remote, 0 commits ahead of `main` |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50 |
| `beevia-db-schema` `main` | `bcc45fb` (v0.0.55) | Unchanged |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `e40116d` | Unchanged. **`feat-forget-pin-fixes` `3e23414` → `d55630e`**, no PR (pull refs end at #63) |

### 3.1 The app side of message editing and deletion (`beevia-mobile` `d55630e`, on a branch)

The commit message is a single word ("fixes"). Everything below comes from reading the diff (47 files, +4,037 / −601). The comparison is with the server code merged in #112.

- **Editing.** Long-pressing one of the user's own text messages selects it, and the selection bar offers Edit, which opens an edit composer. `_canEdit` allows it within 15 minutes of sending; after that the user sees an "edit window expired" message. The new text goes through the same envelope builder as a send, which is what `suggestions.md` §4.20 point 4 asked for. It is sent as `message.edit` with `{requestId, messageId, envelopes}`, and that matches `wsEditMessageSchema` field for field. On the ack, the local copy is updated. A server rejection (`edit_window_closed`, `message_not_editable`) is shown in the server's own localized wording; a timeout or a missing socket falls back to the app's own message. Edited bubbles carry an "edited" mark.
- **Receiving an edit.** A `message.edited` handler decrypts the new ciphertext and replaces the stored text. It ignores the device's own edits, edits whose sender does not match the stored message, and edits not newer than the one already applied. The last rule matters: decrypting the same edit twice would fail, because its message key has already been used.
- **Catch-up.** `MessageHistoryResponse` now parses `changes`, and the catch-up loop applies each one after the new messages: `message.edited`, `message.deleted` and `message.updated` (payment cards). So a phone that was offline should now pick up deletes and edits it missed.
- **`deleted_for`.** It is read as the server's single string, and `"everyone"` removes the stored message. The old list-of-user-ids form is still accepted.
- **One mismatch to settle in review.** The client hard-codes 15 minutes. The server reads `MESSAGE_EDIT_WINDOW_MINUTES` (default 15, `0` = no limit). If someone changes that setting, the two will disagree and the app will refuse edits the server would accept.
- **Also in the commit:**
  - Message forwarding: a new 560-line screen. Forwards are sent as new messages with `content_meta.forwarded`, which the server accepts as free-form metadata.
  - Starred messages: a new screen. Stars are stored on the device only (`Prefs`), so they do not follow the user to another device.
  - A recording waveform and a reworked voice-note bubble.
  - Call-direction icons, stepper and settings widget changes, and strings in four languages.
  - One new widget test (`voice_note_layout_test.dart`).
- **Not in the commit:** `call.ended` is still only mentioned in a comment on both `main` and the branch, and Forgot PIN on `main` is still a `TODO` stub.
- **Read, not run.** No build, test or device run took place here.

### 3.2 The standing checks

- **PIN lock (#110):** no `beevia-api` commit since 16 Nov. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists (`ThrottlerModule`, `express-rate-limit`: no match).
- **`beevia-api` `release.yml`**: re-read. `sync` still has no `needs: test` ("Deliberately not `needs: test` — hosted runners cannot start jobs"), and it runs `pnpm db:migrate` on push to `main`. Unchanged.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is on 0.0.55.
- **Branch protection, PR reviews and CI results**: cannot be seen from here.

### 3.3 Document changes this cycle

`suggestions.md` §4.20: a dated update saying that points 1–4 are written on the branch but not on `main`, and noting the edit-window mismatch. No OpenAPI file, `api-rfc.md` or `admin-api-rfc.md` changed: the audit was clean and no route moved.

---

## 4. Risks

- **One large unreviewed branch is now the only path for three user-facing fixes.** These are: a way out of the PIN lock, offline delete, and edit. Bundling them means none ships until all of them are reviewed, and the review gets harder with each commit. *(New.)*
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A locked-out user has no way out on `main`.** The lock is live, and Forgot PIN on `main` is still a stub.
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **A production data migration with no test gate.** 0.0.55 rewrote `deleted_for = 'sender'` rows on push. Whether it ran cleanly is not visible.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended twelve days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **The 30-day NIN clock.** The client is on `main`. Whether it has shipped to users is not visible, and the limits are still not enforced. The grace for existing users ends about 6 Dec.
- **A user can be told a person is coming when none can come.** No role holds `disputes`.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** none.

---

## 5. PRD gap

The four structural gaps are unchanged and carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. Today's branch commit extends E2EE messaging (line 1) and touches none of them. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 10 Nov 15:02 → 17 Nov 15:02 UTC. Commit counts are non-merge commits on all remote refs in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (2 on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**9 commits in 7 days**: 7 in `beevia-api` and 2 in `beevia-db-schema`. The drop from 12 is the window moving past 10 Nov, not a change of pace. **One own submission**, `I362` on 11 Nov. **No WIP on 1002.** No commit since #112 and #36 yesterday; his last is 1.1 d old. Neither is an item on any board. `BVA-I8` has been In progress on the closed admin board for 64.0 days.

### 6.2 David Samuel: mobile

**3 commits** in 7 days, all on `feat-forget-pin-fixes`: 11 Nov 19:09, 12 Nov 06:49 and **17 Nov 05:51 UTC**. Today's commit builds the client half of #112, the server work that landed yesterday, within a day of its merge, plus forwarding and starred messages. **Zero submissions.** His last own submission was `I286` on 14 Oct, **34.0 days** ago. That says more about the board than the work: a branch with no PR cannot be moved to review in any meaningful sense. **WIP: 2 items, both with code on `main`**: `I331` at 26.2 days and `I361` at 14.3 days. As before, this reads as items left in the wrong column rather than stuck work; that is for him to say.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** His last board action was on 2 Nov 15:58 UTC, **15.0 days** ago: he may be finished, blocked or working untracked. Worth a question, not an assumption. Forwarding, starred messages and message editing now exist in the app with no design item on the board, like Forgot PIN before them. Design files are not in git, so whether a design preceded them is not visible.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **18.0 days** old, and `beevia-admin` has no new branch or pull ref. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee; `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 64.0 days.

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
| 2026-W47 (16 → 17 Nov, to 15:02 UTC) | — | — | 0 | 0 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. Output continues in code; acceptance stays at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 4,000-line commit and a one-line fix count the same.
- **Who moved an item is not whether it is done.**
- **Untracked work.** #110, #111, #112, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits.** `d55630e` is one commit.
- **Unpushed work.** A quiet remote says nothing about local work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 16 Nov | Status on 17 Nov |
|---|---|
| **1. Put the app side of #112 on the board, with an owner and a design** | ◐ **In part.** The code was written (`d55630e`, on a branch). It is not on the board, and no design item exists |
| **2. Open a PR for `feat-forget-pin-fixes` and review it** | ❌ **No.** The branch grew by 47 files instead; pull refs still end at #63 |
| **3. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No `beevia-api` commit |
| **4. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No board action at all** |
| **5. Close 1002 deliberately** | ❌ **Not done, twelve days late.** No successor, no sweep, filter still 08-01 |
| **6. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No** |
| **7. Two-device chat on a real build, including delete online and offline** | ❌ **Not visible.** The offline-delete half now has client code on the branch to test |
| **8. Confirm migration 0055 ran cleanly in production** | ❌ **Not visible** |
| **9. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **10. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **11. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **12. Handle `call.ended` in the app** | ❌ **No**, on `main` or the branch |
| **13. NIN step, support screens and Forgot PIN on the board** | ❌ **No** |
| **14. Decide whether the tier limits are enforced** | ❌ **No** |
| **15. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **16. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **17. Record the consent behind each lookup** | ❌ **No** |
| **18. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **19. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **20. Bring the dashboard onto the real contract** | ❌ **No commit in 18.0 days** |
| **21. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **22. Parent status moves; assign `I348`, `I349`, `I351`, `I359`, `I390`; admin sprint** | ❌ **No** |
| **23. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **24. `needs: test` on `sync`; verify jobs; admin-api onto 0.0.55** | ❌ **No.** `release.yml` unchanged; admin-api still on 0.0.50 |
| **25. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No** |
| **26. Carried items** | ❌ **None moved** |

**None of the 26 is fully met. One moved in part:** the client code for #112 now exists, on a branch and off the board.

---

## 8. What I would do this week

1. **Open a PR for `feat-forget-pin-fixes`, or split it first, and review it (carried, now more urgent).** It now holds three separable pieces: Forgot PIN, the app side of #112, and forwarding/starred/voice-note work. Smaller PRs would let the PIN way-out and the offline-delete fix ship without waiting for the rest. Ask whether the in-app Paystack WebView was a decision.
2. **Put that work on the board, with an owner and a design item (carried, narrowed).** The code exists; what is missing is the item that lets it be reviewed and accepted like the rest of 1002.
3. **In that review, settle the edit window (new).** Either the app reads the window from the server, or the setting is documented as fixed at 15 minutes (`suggestions.md` §4.20).
4. **Make the PIN check reserve its attempt before comparing (carried).** Use one conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
5. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
6. **Then close 1002 deliberately (carried, twelve days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and items for #35, #110, #111, #112 and the branch. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
7. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
8. **Run one two-device chat on a build of the branch (carried, now testable).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
9. **Confirm migration 0055 ran cleanly in production (carried).** Look for rows still marked `deleted_for = 'sender'` and for a `message_hides` count that matches.
10. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
11. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
12. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
13. **Handle `call.ended` in the app (carried).**
14. **Put the NIN step and the support screens on the board with a design and an owner (carried).**
15. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
16. **Decide the seeded card default and what a card limit is, on the record (carried).**
17. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
18. **Record the consent behind each BVN and NIN lookup (carried).**
19. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
20. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
21. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
22. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
23. **Agree how parent status moves work; assign `I348`, `I349`, `I351`, `I359` and `I390`; give the admin dashboard a sprint (carried).**
24. **Retire `GET /cards/{id}/transactions` (carried).**
25. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.55 (carried).
26. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
27. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 64.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 64 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 18.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-seven days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** Nothing reached `main` in any repo during the window. Today's branch commit is the client for #112's edit and catch-up, which would let line 1 (E2EE messaging) be reconsidered. It also carries voice-note recorder work, which is what line 1 has been waiting on. But the rubric scores `main`, and the branch has no PR. When it merges, line 1 is the line to revisit.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Edit client, catch-up `changes` and the voice-note recorder are all on an unmerged branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether the branch builds, runs, or edits and deletes correctly against the server.** Nothing was run, and the commit message gives no account of testing beyond one new widget test.
- **Whether #112 is live and whether migration 0055 ran cleanly.** The workflow deploys and migrates on push; its result is not visible.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the pull requests were reviewed or approved.**
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag, on the in-app Paystack checkout, on the 15-minute edit window or on device-only stars, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three background exports starting at about 14:54 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 16 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical and CSV identical apart from its date line. Then a sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects). 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-17`: exit 0. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow17.py`, a date-shifted copy of 16 Nov's). It diffed 1002 against 16 Nov, listed every action in the window (none), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `fetch` and `ls-remote` of heads and `refs/pull/*` in all five repos. In `beevia-mobile`: the full stat of `d55630e`; its edit, `message.edited`, `applyChange`, catch-up and `deleted_for` code; the edit-envelope builder; `call.ended` and the Forgot PIN stub on `main` and the branch; the branch's base (`e0c1647`, whose tree is identical to `main`'s). In `beevia-api`: `wsEditMessageSchema`, `editBodyFields` and the `message.edit` gateway handler, to compare with the client; `release.yml`; both services' schema pins; the absence of any HTTP rate limiter.
6. Document update (§3.3).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch` (including the existing `refs/pull/*` mirror), `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`merge-base`. Nothing was committed, pushed or deployed. A final `fetch` of all five repos at 15:07 UTC found nothing new.

**Files changed this cycle:** this report, `web-report/2026-11-17.html`, `web-report/index.html` and `suggestions.md`. New board exports for 17 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 16 Nov 15:05 UTC → 17 Nov 15:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
