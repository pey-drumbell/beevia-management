# Beevia — Project Status

**As of 2026-09-29** · Sprint **0901** (3 Sep → 22 Sep): **closed seven days ago, still the working board** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-29.csv` + `beevia-activity-2026-09-29.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-29.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**77 items**) + sidecar in `/tmp/beevia-scratch/`. All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`. The unmerged branches `beevia-mobile` `origin/update-fixes`, `beevia-admin-api` `origin/ci/node-26-only` and `beevia-db-schema` `origin/ci/pr-only-no-cron` were read too.

Scope: three boards, kept separate and never summed. **Window: 28 Sep 14:05 UTC → 29 Sep 14:05 UTC, one working day.**

---

## Quick overview

> **A quiet day on the board and on every `main`, but not on the branch that matters: the unmerged mobile branch gained a third commit that fixes two more items already sitting in REVIEW/QA, three days after they entered it. That makes four QA items whose fixes are verifiably not on `main`.** The board recorded one move in 24 hours. Nothing left review and nothing was accepted, so the queue now holds 58 of 68 leaves (85%). No product code reached any `main` branch. The only backend merges were CI changes, and one of them means **`beevia-api`'s security scan no longer runs on pushes to `main` or on a daily schedule**. It now runs on pull requests only. Whether `main` requires a pull request has never been verified, and on 28 Sep another backend repo's `main` turned out to be force-pushable.

**Correction to the previous edition: read this first.**

1. **"42 submissions (10 moved by board administration)" (28 Sep, team table and §6.2/§6.6) understated board administration's share by 17.** Ten was **Friday's count only**. Over the full seven days that edition measured, **27 of David's 42 submissions were moved by board administration**, 11 by David and 4 by Ayomikun on co-owned items. In today's window the split is 25 / 11 / 4 of 40. This changes how the number reads: most of the mobile "submission" count records the board being tidied, not David submitting work. It is not a measure of David's output in either direction.

| Metric | 28 Sep | 29 Sep | Δ |
|---|---:|---:|---|
| Sprint 0901 items (leaves + parents) | 77 (68+9) | **77 (68+9)** | 0 |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 0 |
| Socket commands | 38 | 38 | 0 |
| Sprint 0901 leaves To do | 2 | **1** | −1 |
| Sprint 0901 leaves In progress | 1 | 1 | 0 |
| Sprint 0901 leaves BLOCKED | 2 | 2 | 0 |
| Sprint 0901 leaves REVIEW/QA | 57 | **58** | +1 |
| Sprint 0901 leaves Done | 6 | 6 | **0, ninth edition flat** |
| Review queue as a share of the board | 84% | **85%** | +1 pt |
| Review-queue median age (0901) | 3.9 d | **4.9 d** | +1.0 |
| Oldest item in the queue | 19.9 d | **20.9 d** | +1.0 |
| Items that left REVIEW/QA in the window | 0 | **0** | last exit of any kind 24 Sep (5.1 d); last to Done 16 Sep (13.1 d) |
| QA items whose fix is verifiably only on `update-fixes` | ≥2 | **≥4** (`BVA-I287`, `BVA-I303`, **`BVA-I292`, `BVA-I294`**) | +2 |
| `update-fixes` vs `beevia-mobile` `main` | 2 ahead · 68 files | **3 ahead · 90 files, +4,138 / −1,300** | +1 commit |
| `beevia-mobile` days since a commit on `main` / any branch | 3.9 / 1.0 | **4.9 / 0.9** | |
| `beevia-api` days since a product (non-CI) commit | 3.0 | **4.0** | only CI merged (#58, #59) |
| `beevia-admin-api` days since a commit | 4.1 | **5.1** | CI branch pending, unmerged |
| `beevia-db-schema` days since a commit | 3.7 | **0.9** (CI only, #18) | no forced update this window |
| `beevia-admin` days since a commit | 5.9 | **6.9** | +1.0 |
| Admin board: days since *any* activity | 14.0 | **15.0** | +1.0 |
| Backend security scan triggers (`beevia-api`) | PR · push to `main` · daily | **PR only** | **narrowed** (§3.2) |
| Ayomikun commits (7d, both identities, `origin/main`, non-merge) | 27 | **29** | rolling window; 3 new, all CI |
| David commits (7d): merged to `main` / on `update-fixes` | 3 / 2 | **1 / 3** | rolling window |
| Promise commits (7d, merged) | 2 | **1** | rolling window; last 22 Sep |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 77 · 0 / 12 · 0 / 64 | same | 0 |
| **Sprints open on either board** | 0 | **0** | sixth edition |
| MVP readiness (estimate) | ≈66% (65.52) | **≈66% (65.52)** | 0, nothing new on any `main` |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **21 on 0901, all REVIEW/QA** (15 solely) · 3 on 0901-admin | 9 (4 own moves) | 0.98 d (n=10) | **0** on 0901 · 1 on 0901-admin (`BVA-I8`, **15.0 d**) | **29** | Their half of the queue has a median age of **11.5 d** and includes the oldest item (20.9 d). Monday's merges were CI only; one narrowed the security scan to PRs (§3.2) |
| David Samuel | mobile | **48 on 0901**: 42 REVIEW/QA (34 solely), 2 BLOCKED, 1 In progress, 1 To do, 2 Done | 40 (**11** own moves; 25 board administration; 4 Ayomikun) | 0.96 d (n=24) | 3: `BVA-I277` In progress 4.9 d; `BVA-I260`, `BVA-I275` BLOCKED 6.1 d | **1 merged · 3 unmerged** | `update-fixes` gained a third commit fixing two more queued items. The fixes exist but are not on `main` (§1.2) |
| Philip Chidera | design | 7 on 0901: 4 Done, 3 REVIEW/QA | 3 (1 own) | 0.55 d (n=2) | 0 | n/a | Moved `BVA-I298` To do → REVIEW/QA on Monday, the window's only board action. **No design item is open any more** |
| Promise Udo | admin dashboard | 4 on 0901-admin: 3 Done, 1 In progress | 0 | n/a | 1 (`BVA-I9`, **15.0 d**) | 1 | `beevia-admin` **6.9 days** without a commit, the longest gap since the admin board went live. The admin board has been silent for 15 days |

**The two questions for standup:** (1) **What is stopping `update-fixes` from merging?** It now carries the fixes for at least four items QA has had for three to four days, plus the escrowed send. Every day it stays unmerged, a `main` build fails more of the queue. (2) **Does `main` require a pull request on the backend repos?** As of Monday, `beevia-api`'s security scan only sees pull requests. If a direct push to `main` is possible (and a force-push was possible on `beevia-db-schema` three days ago), that push is never scanned.

**The three things worth knowing:**

1. **The gap between the queue and the code grew again.** Monday's `update-fixes` commit (`e109ac0`, 28 Sep 15:59 UTC, 19 files) adds the end-to-end-encryption notice at the top of every conversation (`BVA-I292`). It also adds offline handling for the conversation list, with previews and ordering rebuilt from the local message store, a refetch on reconnect, and a splash screen that stops waiting on a dead network (`BVA-I294`). Both items entered REVIEW/QA on **25 Sep at 16:08–16:10**, roughly **72 hours before their fixes were written**. Board administration moved both. Neither fix is on `main`, which has had no commit for 4.9 days. The same 28 Sep diagnosis still holds and is a process finding, not a personal one: REVIEW/QA is being used for "in hand", and with no reviewer nothing forces a distinction.

2. **The backend's only change was to CI, and one part of it trades coverage for cost.** `beevia-api` #58 and `beevia-db-schema` #18 test and publish on Node 26 only, which is uncontroversial. **`beevia-api` #59 removed the `push` and daily `cron` triggers from `code-scan.yml`.** The commit's reasoning holds for anything that arrives by pull request. It does not hold for a direct push to `main`, and the comment it deleted named exactly that case as the schedule's purpose. The September payload arrived that way. The same change is written, unmerged, for `beevia-admin-api` and `beevia-db-schema`. Recommendation: keep a weekly schedule and the `push` trigger on `main` until branch protection requiring a pull request is confirmed (`suggestions.md` §7.7).

3. **The review queue has not produced a single forward move in 13 days.** The last item to reach Done was `BVA-I268` on 16 Sep, closed by its own owner. The last item to leave REVIEW/QA for any reason was `BVA-I262` → BLOCKED on 24 Sep. Since then 33 transitions have gone in and none have come out. The one move today was a design item going straight from To do to the queue. Eleven editions have now said that the missing piece is a reviewer, not developer output.

**If you read nothing else:** the fixes QA is waiting for are being written, but they are going onto a branch while the items sit in a queue no one reviews. The one backend change narrowed security scanning on the assumption that every change to `main` arrives by pull request, which nobody has verified.

---

## 1. Sprint 0901: closed 22 Sep, still the working board

**77 items: 68 leaves + 9 parent Stories.** All figures below are leaves unless stated. No item was added or removed.

### 1.1 Status distribution and movement

| Status | 28 Sep | 29 Sep | Δ |
|---|---:|---:|---:|
| REVIEW/QA | 57 | **58** | +1 |
| To do | 2 | **1** | −1 |
| In progress | 1 | 1 | 0 |
| BLOCKED | 2 | 2 | 0 |
| Done | 6 | 6 | 0 |
| **Total leaves** | **68** | **68** | 0 |

The audit's `SINCE` section, run against the 28 and 29 Sep scratch exports, shows **1 entered review, 0 left, 0 newly Done.** Its two problems are both real: *58/68 in REVIEW/QA seven days after the sprint's end*, and *nothing left REVIEW/QA*.

**The whole window, in one line:** Mon 28 Sep 15:14 UTC, `BVA-I298` *Message Text and Timestamp Lack Visual Contrast*, To do → REVIEW/QA, moved by its owner Philip Chidera. It was never marked In progress. There were no comments, creations or re-assignments on any board.

### 1.2 The queue is still ahead of the code, now by four verified items

`beevia-mobile` `main` last moved on 24 Sep 16:32 UTC (PR #36). `origin/update-fixes` (`Davidtariq96`) is now **3 ahead of `main` and 2 behind**, and the difference is 90 files, +4,138 / −1,300. The branch was checked by content, not by commit message. The new commit's message is "update from fixes".

| Item | Entered REVIEW/QA | Moved by | Fix | Committed |
|---|---|---|---|---|
| `BVA-I287` Request Money button on profile not working | Sat 26 Sep 09:06 | David | `contact_profile.dart`: `onTap: () {}` → `_requestMoney` | Sun 27 Sep 14:22 (`99c8909`) |
| `BVA-I303` Excessive spacing between wallet title and content | Sat 26 Sep 09:29 | David | `wallet_screen.dart`: `SizedBox(height: 42)` removed | Sun 27 Sep 14:22 (`99c8909`) |
| **`BVA-I292`** E2EE notice missing at start of conversation | Fri 25 Sep 16:10 (from To do) | board administration | New `EncryptionNoticeBanner` as the first row of `chat_details.dart`'s list outside search mode; `encryptionNoticeMessage` string in all four locales. **Absent from `main`** (`git grep` finds nothing) | **Mon 28 Sep 15:59** (`e109ac0`) |
| **`BVA-I294`** Conversations list not available offline, not refreshing after reconnect | Fri 25 Sep 16:08 (3 h after David started it) | board administration | `conversation_provider.dart` rebuilds previews and order from `LocalMessageStore` when offline, because forward secrecy makes a second decryption of the cached ciphertext fail. `user_provider.dart` refetches on reconnect. The splash screen skips the network when there is no connectivity. `NetworkService` gets 15 s timeouts | **Mon 28 Sep 15:59** (`e109ac0`) |

The same commit also changes outgoing voice calls to play ringback through the earpiece and keeps the loudspeaker for video only, which bears on `BVA-I295` (*no ringback tone*, in REVIEW/QA since 25 Sep). The video call's fallback background is now plain black. These were not verified against their board items line by line, so they are not counted above.

The engineering in `e109ac0` is careful. The comment explaining why cached ciphertext cannot be decrypted twice under Signal's forward secrecy is exactly the kind of reasoning that belongs in the code. None of this reflects on effort. It is about **where** the work is. A reviewer testing `main` today would find all four items unfixed.

### 1.3 The review queue: 58 items

Ages are the `actiontime` of each item's last transition into REVIEW/QA, from the activity sidecar, measured to 29 Sep 14:05 UTC.

| | Items | Median age | Oldest |
|---|---:|---:|---:|
| Ayomikun Araoye | 21 | **11.5 d** | **20.9 d** |
| David Samuel | 42 | 4.6 d | 14.9 d |
| Philip Chidera | 3 | 3.9 d | 4.9 d |
| **Whole queue** | **58** | **4.9 d** | **20.9 d** |

The owner rows add up to 66 across 58 items, because eight items are co-assigned. The seven-item Notification block submitted on 8 September is now **20.9 days** old. On sprint 0901, REVIEW/QA has had **four exits in its history**: `BVA-I268` → Done on 16 Sep, closed by its own owner, and three moves to BLOCKED on 23–24 Sep. **No item on any board has ever been accepted by someone other than the person who submitted it.**

### 1.4 What is open

Four leaves.

| Item | Status | Age | Owners |
|---|---|---:|---|
| `BVA-I260` Face verification shows static placeholder | BLOCKED | 6.1 d | David |
| `BVA-I275` Sender/receiver profile pictures swapped | BLOCKED | 6.1 d | David |
| `BVA-I277` New chat shows incorrect phone numbers for invites | In progress | 4.9 d | David |
| `BVA-I297` Inconsistent section divider styling | To do | 5.0 d | David |

`BVA-I260` and `BVA-I275` are **disputed, not blocked**. Each carries a written argument from David (23 Sep) that the reported behaviour is intended. **Neither has had a reply in six days.** `BVA-I277` carries David's request for a screenshot from the same day, also unanswered. It is five times over David's 0.96-day median cycle, and on this evidence the likely reason is the missing information, not the work. All four open items are David's.

---

## 2. Admin dashboard board: `0901-admin`

**12 items: 8 leaves + 4 parent Stories. Unchanged in every respect.**

| Status | Leaves |
|---|---:|
| Done | 6 (`BVA-I5`, `BVA-I11` Ayomikun · `BVA-I6`, `BVA-I12`, `BVA-I15` Promise · `BVA-I14` unassigned) |
| In progress | 2 (`BVA-I8` *Report Data Query*, Ayomikun · `BVA-I9` *Report Content Display*, Promise; both **15.0 d**) |

**The last activity of any kind was on 14 September at 14:53 UTC, fifteen days ago.** `beevia-admin` has had no commit since 22 September (**6.9 days**). `beevia-admin-api`'s `main` has had none since 24 September (5.1 days), and its only newer work is the unmerged CI branch. Both the board and both repos of the admin workstream have now been silent together for a second edition. These counts are never added to the main sprint's.

---

## 3. API surface, spec drift and CI

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. The audit ran against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-29`. The in-repo audit reports its usual 21 "in spec, not in code" lines (6 consumer + 15 admin). These are the known phantom drift from the three `diverged` working trees, and nothing was done about them.

### 3.1 What merged

| Repo | PR | Merged (UTC) | Change |
|---|---|---|---|
| `beevia-api` | #58 `ci/node-26-only` | Mon 28 Sep 16:24 | `test.yml` matrix `[24, 26]` → `[26]` |
| `beevia-api` | #59 `ci/pr-only-no-cron` | Mon 28 Sep 16:39 | `code-scan.yml`: `push` and daily `cron` triggers removed (§3.2) |
| `beevia-db-schema` | #18 `ci/node-26-only` | Mon 28 Sep 16:25 | `ci.yml` and `release.yml` on Node 26 only; `engines` still `>=24` |

No file under `src/` changed in any backend repo. **No spec edit was needed**, and none was made to any of the four OpenAPI files, `api-rfc.md` or `admin-api-rfc.md`.

`beevia-db-schema` is otherwise as the 28 Sep edition left it. `main`'s `package.json` says **0.0.37**, tag `v0.0.38` still points at `e285f10`, which is on no branch, and no release commit followed #18. That fits `ci.yml`'s `paths-ignore: '.github/**'`: a change that only touches workflows starts no CI run, so it starts no release. Whether the next real release re-bumps to 0.0.38 is still the open question from §4.1 of that edition. **The reflog sweep found no forced update in any of the five repos in this window.**

### 3.2 The security scan now sees pull requests only

`e8377de`'s message: *"The daily scan re-checked code that had already been scanned on its pull request, and the push trigger re-ran the whole suite on merge against the same tree the pull request had just passed."* For work that arrives by pull request, that is correct, and the saving is real.

It gives up two things:

- **A direct push to `main` is no longer scanned at all.** The deleted comment gave the reason for the schedule: *"so a payload or a credential committed to a quiet branch surfaces within a day."* Whether a direct push is possible depends on branch protection requiring a pull request (`suggestions.md` §7.1). That has never been verifiable from here, and on 28 Sep it was shown **not** to stop a force-push to `beevia-db-schema`'s `main`. The September incident's payload reached `main` by push, not by pull request.
- **A quiet repo is never re-evaluated.** Scanner rules and advisory data change while code sits still. A weekly run is what catches a newly disclosed problem in an unchanged lockfile.

The same change is written and waiting for **both other backends**: `beevia-admin-api` `origin/ci/node-26-only` (`66737d7`, "check on pull requests only") and `beevia-db-schema` `origin/ci/pr-only-no-cron`, which also removes the schedule from its three standalone scan workflows. Recommendation (`suggestions.md` §7.7, updated today): **keep a weekly schedule, and keep the `push` trigger on `main` until a pull request to `main` is confirmed to be mandatory.** Neither step needs org access.

### 3.3 Spec and document changes this cycle

| File | Change |
|---|---|
| `suggestions.md` | **§7.7:** new 2026-09-29 update on the scan-trigger narrowing and its two costs. **§8 item 3b:** keep the weekly schedule and the `push` trigger before the pending CI branches merge. |

No OpenAPI file, `api-rfc.md` or `admin-api-rfc.md` changed. No route, DTO, socket command or proposed operation moved.

---

## 4. Risks

- **Review queue.** 85% of the board, with nothing out in 5.1 days and nothing to Done in 13.1 (§1.3).
- **Queue ahead of code.** At least four queued items are fixed only on an unmerged branch that is now 90 files wide. The longer it stays unmerged, the bigger and riskier the merge (§1.2).
- **Security scanning narrowed on an unverified assumption** (§3.2). This is new today.
- **The biometric step-up on `update-fixes` is unchanged.** `wallet_service.dart:78` still posts `{ method: biometric }`, and `stepUpSchema` on `origin/main` is still `z.object({ pin })` at `auth.dto.ts:77`. If the branch merges as it is, every biometric confirmation fails against the real API (`suggestions.md` §5.11).
- **`payments.dto.ts` phone field.** It is still `z.string().trim().min(6).max(20)` at line 5, and it becomes the input to every chat send once `update-fixes` merges.
- **`beevia-db-schema` release state.** The tag is orphaned and `main` sits one version behind the registry. Nothing has changed since 28 Sep.
- **No sprint open** on either project, for the sixth edition.
- **Three diverged local working trees.** `beevia-api` is behind by 61, `beevia-admin-api` by 34 and `beevia-db-schema` by 44, each 1 ahead.

---

## 5. PRD gap

Nothing changed. No product code landed on any `main`. The four structural gaps are where they were: international KYC tier, multi-currency/FX settlement, virtual cards beyond what is wired, and consent management.

Re-verified at `origin/main`: `PaymentService.activeNgn()` is at `payment.service.ts:506` and is called from lines 70, 128 and 288. `StubTranslateAdapter` is still bound at `translate.module.ts:23`. The client's chat Send on `main` still posts `/payments/transfer`, so escrow is still bypassed. The escrowed `payment.send` path is still only on `update-fixes`.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. Commit counts are non-merge commits on `origin/main` from 22 Sep 14:05 to 29 Sep 14:05 UTC, summing each person's git identities. Bot commits are excluded. David's unmerged branch commits are shown separately.

### 6.1 Ayomikun Araoye: backend + admin API

**29 commits in 7 days**: `beevia-api` 15 (`Phoenixdadhev` 13, `Ayomikun Araoye` 2), `beevia-db-schema` 13 (12 + 1), and `beevia-admin-api` 1. Monday added three, all CI (§3.1). Their last product commit is Friday's #57, 4.0 days ago. Two CI branches of theirs are also waiting, one on `beevia-admin-api` and one on `beevia-db-schema`.

**All 21 of their 0901 items are in REVIEW/QA**. Fifteen are theirs alone. Their median age is 11.5 days and the oldest is 20.9. Their nine submissions in seven days break down as four moves of their own and five by board administration. Median cycle time is 0.98 days (n=10). They have no open work on the main board and one admin-board item, `BVA-I8`, In progress for 15.0 days. **Their queue profile is a process finding, not a personal one**: nothing they do can move items out of a column that nobody reviews.

### 6.2 David Samuel: mobile

**40 submissions to REVIEW/QA in 7 days** (owner rows). **Of these, 11 were their own moves, 25 were board administration's and 4 were Ayomikun's on co-owned items** (see correction 1). Median cycle time is 0.96 days (n=24). David owns 48 of 68 leaves, including 42 of the 58 queue entries (34 of them solely) and all four open items.

**Commits: 1 on `main` in the window** (`d827ca2`, 22 Sep 17:12, landed with PR #35) **plus 3 on `update-fixes`**, the latest on Monday afternoon. The branch holds real, board-requested work: the escrowed send, the E2EE notice, offline conversations, the profile request-money button, call-audio routing, and several design fixes. The ask is the one from yesterday. Merge it, or agree that an item enters REVIEW/QA only once its fix is on `main`. It is not an ask about effort, which is clearly there.

### 6.3 Philip Chidera: design

On Monday Philip moved `BVA-I298` (message/timestamp contrast) from To do straight to REVIEW/QA. It was the window's only board action and Philip's last open item. There are now three of their items in REVIEW/QA (`BVA-I274` and `BVA-I296` are co-owned) and four Done. **No design item remains open on the board.** There are no commits, because design work does not land in these repositories.

### 6.4 Promise Udo: admin dashboard

Promise has 1 commit in the 7-day window (`0b41e35`, 22 Sep, *wallet summary and wallet detail integration*). **`beevia-admin` has now gone 6.9 days without a commit**, and the admin board has gone 15.0 days without activity. `BVA-I9` has been In progress all that time. Promise has never made a board action themselves. **Absence of data is not absence of work.** `beevia-admin` has no remote branch except `main`, so local work would be invisible here. But the question from 28 Sep is still unanswered, and it is still worth one line at standup.

### 6.5 Weekly submission trend (sprint 0901, transitions into REVIEW/QA)

| ISO week | Submissions |
|---|---:|
| 2026-W37 | 9 |
| 2026-W38 | 15 |
| 2026-W39 | **44** |
| 2026-W40 (from Mon 28 Sep) | 1 |

Across the same three and a bit weeks, acceptances by anyone other than the submitter numbered **zero**. The one move to Done (`BVA-I268`, 16 Sep) was a self-closure. With submissions rising and acceptance at zero, the bottleneck is not the developers. This is the eleventh consecutive edition to say that no reviewing role is staffed.

### 6.6 What this does not measure

- **No estimation points on any of 77 items**, nor on the 12 or the 64. Item counts say nothing about who is carrying more. This is the eighteenth edition to note it.
- **"Submitted" counts any transition into REVIEW/QA, by anyone**, and attributes it to the item's owner. **For David, 25 of 40 were board administration's moves** (correction 1). The figure measures board activity more than individual output.
- **Commit counts reward small commits, and cycle times reward small items.** Twenty-nine backend commits against 1 + 3 mobile ones is not a comparison of output. `e109ac0` alone is 19 files.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 28 Sep | Status on 29 Sep |
|---|---|
| **1. Merge `update-fixes`, or say why not, and agree what REVIEW/QA means** | ❌ **Not merged. The branch grew instead**: 3 ahead, 90 files. Two more queued items were verified fixed only there (§1.2). No convention was written on the board |
| **2. Take the biometric option out before merging** | ❌ **Not done.** It is still at `wallet_service.dart:78` on the branch, and the server still accepts `{ pin }` only |
| **3. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** Line 5 is unchanged. No `src/` change in any backend |
| **4. Find out who force-pushed `beevia-db-schema` `main`, and turn force-push off** | ❔ **Unknown from here.** No further forced update. The tag is still orphaned. Monday's CI change makes it matter more (§3.2) |
| **5. Name a reviewer** | ❌ **Not done.** 58 of 68. Eleventh edition |
| **6. Open sprint 0902 on both boards** | ❌ **Not done.** Zoho still lists `0901, 08-01, 0702, 0701` and `0901-admin`. Sixth edition |
| **7. Reply on `BVA-I260`, `BVA-I275` and `BVA-I277`** | ❌ **Not done.** No comment has been added anywhere since 24 Sep |
| **8. Stop vendoring the spec in `beevia-mobile`** | ❌ **Not done.** |
| **9. Ask about the admin workstream** | ❔ **No visible answer.** Repo silent for 6.9 d, board for 15.0 d |
| **10. Carried: OpenAPI generation in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; estimation points on 0902** | ❌ **None done.** The one CI change in the window went the other way for the scanner (§3.2). `beevia-admin` still has no `.github/` |

**None of the ten was resolved.** Monday was a working day. Items 5, 6 and 7 each need one decision or one comment.

---

## 8. What I would do this week

1. **Merge `update-fixes` today, after taking out the biometric option.** It fixes at least four queued items, and it makes the chat Send use escrow. Every day it waits, it grows (68 → 90 files in one day) and the queue means less. The biometric button fails against the real API, so hide it outside mock mode until the design in `suggestions.md` §5.11 is decided.
2. **Before the other two CI branches merge, keep a weekly scan and the `push` trigger on `main`**, and put both back in `beevia-api`, until someone confirms that `main` requires a pull request on all three backends (§3.2; `suggestions.md` §7.7).
3. **Write down what REVIEW/QA means.** Either an item enters it when its fix is on `main`, or a "fixed on branch" status is added.
4. **Name a reviewer.** 58 of 68 leaves, with nothing out for five days. Eleventh edition.
5. **Bring `payments.dto.ts` onto `phone.util.ts`** before item 1 lands, because every chat send will then depend on that field.
6. **Reply on `BVA-I260`, `BVA-I275` and `BVA-I277`.** That is three comments, each six days overdue. All four of the board's open items are waiting on them or on David.
7. **Open sprint 0902 on both boards.** Sixth edition.
8. **Ask about the admin workstream.** The repo has been silent for seven days and the board for fifteen, with two items In progress throughout.
9. **Decide what `beevia-db-schema`'s `v0.0.38` tag should point at** before the next release run.
10. **Carried, unchanged:** OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec; estimation points on 0902.

---

## Admin dashboard board

See §2. `0901-admin` exists, is closed, holds 12 items, and has not changed in fifteen days. Its figures are kept separate from sprint 0901's throughout.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈66% (estimate; 65.52, unchanged)

**Target 2026-09-01 (provisional). The target date passed twenty-eight days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance.

**No score moved.** No product code reached any `main`. `update-fixes` would move #7 back toward 0.95, because it routes the chat Send through escrowed `payment.send`, and it would add the E2EE notice to #1. It is unmerged, so it does not score.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No change on `main`. The in-thread E2EE notice (`BVA-I292`) exists only on `update-fixes` |
| 2 | Voice & video calling | 8 | 0.80 | 0 | No `/calls` change. Call-audio routing changes are on `update-fixes` only |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` at `payment.service.ts:506`, called from 70/128/288 |
| 7 | Send / request / receive in chat | 12 | 0.85 | 0 | Chat Send on `main` still posts `/payments/transfer` (instant, no escrow). The escrowed socket send is on unmerged `update-fixes`, and the score returns toward 0.95 only when that is on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change on `main` |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | `beevia-admin` has had no commit since 22 Sep. `beevia-admin-api` `main` has had none since 24 Sep |
| | **Weighted total** | **100** | **65.52** | **0** | **≈66%** |

### What this report cannot tell you

- **Whether the other 54 queued items are fixed on `main`.** Four are verifiably not. The rest were not checked line by line, and no build ran.
- **Whether a direct push to any backend `main` is possible.** Branch-protection settings cannot be seen from a clone, which is why §3.2 is a risk and not a finding of exposure.
- **Whether any CI run passed**, or whether `beevia-db-schema`'s release workflow ran after #18. There is no release commit, which fits the `paths-ignore` rule, but a run cannot be seen from here.
- **Whether `update-fixes` builds or passes its tests**, or when it will merge.
- **What the admin dashboard work looks like this week.** There have been no commits and no board activity.
- **Velocity for any of the three sprints.** No item on any of them is estimated (0 of 77, 0 of 12, 0 of 64).

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects. Neither has a successor sprint.
2. Main board export: 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin`: 12 items, exit 0.
4. Read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/`: 77 items, exit 0.
5. Fast-forward sync: 0 repos advanced, 2 already current, 3 refused as `diverged`, exit 1.
6. Reflog sweep of all five repos for forced updates. None were found.
7. Audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-29`: route level and spec health clean. It was re-run with the 28 and 29 Sep 0901 scratch exports copied in, so that the `SINCE` delta covers the active sprint.
8. Activity-sidecar sweep of the window: status transitions, comments, and completions matched on all three Zoho action names.
9. Re-derivation of the seven-day submission split by actor, which produced correction 1.
10. Content reads of `update-fixes` `e109ac0` (diffed, not judged by message), of the three backend CI merges, and of the two unmerged CI branches.
11. `suggestions.md` edit.
12. This report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages are the `actiontime` of each item's last transition into `REVIEW/QA`, measured to 29 Sep 14:05 UTC. Cycle times are `In progress` → `REVIEW/QA` pairs. WIP ages run from the entry into the current status.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose transitions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync, the only git operations were `git archive` and read-only `log`/`diff`/`grep`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-29.html`, `web-report/index.html` and `suggestions.md`, plus new board exports for 29 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **No open sprint on either board.** Both closed on 22 September with no successor. Sixth edition.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged` (ahead 1, behind 61 / 34 / 44). Every backend claim is made against `origin/main` through the shadow. The in-repo audit's 21 drift lines are artefacts of this and were ignored.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, last activity 3 Sep). All sprint-0901 figures come from the scratch export.
- **GitHub settings and CI results cannot be seen from here**, except where a forced update shows in a reflog.
- **The export's "no source key" warning fired on `Epic` again.** This is the known 50-row sampling artefact. On sprint 0901 the column resolves to real values (`Language` 18, `Notification` 7, `security` 5; 47 blank, which means no epic is assigned).

**Window.** 28 Sep 14:05 UTC → 29 Sep 14:05 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
