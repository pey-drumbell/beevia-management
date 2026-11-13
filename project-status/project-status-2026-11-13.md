# Beevia — Project Status

**As of 2026-11-13** · Sprint **1002** (21 Oct → 5 Nov, **ended eight days ago, day 24**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-13.csv` + `beevia-activity-2026-11-13.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-13.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 12 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 12 Nov 15:04 UTC → 13 Nov 15:03 UTC, 1.0 day (Thu → Fri).**

---

## Quick overview

> **A quiet day. One small server fix landed: `beevia-api` #111 stops the app's "Some messages can't be shown on this device" banner from appearing for calls and payment cards, which have no ciphertext by design. Nothing else moved. The board had no action for a second full day, 1002 is eight days past its end, and none of its 33 review items has been accepted. The Forgot PIN client is still on a branch with no pull request, so a user who trips yesterday's PIN lock on `main` still has no way out but to wait 30 minutes. The lock's race is unchanged.**

| Metric | 12 Nov | 13 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 0 | **0** | sidecar byte-identical to 12 Nov; last action 11 Nov 06:53 UTC |
| Transitions into REVIEW/QA, last 7 days (leaves) | 1 | **1** | `I362`, by its owner, 11 Nov |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **30.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin), before today's edits | 3 / 0 | **0 / 0** | #111 changed one field's meaning; updated in place |
| API surface (consumer / admin) | 165 / 76 | **165 / 76** | one contract changed in place (`unresolved`) |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain; no auth code changed |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #111 went through it; no workflow file changed |
| `beevia-admin` days since a commit | 13.0 | **14.0** | |
| `beevia-mobile` days since a commit on `main` / on any branch | 2.0 / 0.3 | **3.0 / 1.3** | `feat-forget-pin-fixes` unchanged since 12 Nov 06:49 UTC; still no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.2 / 5.1 / 1.0 | **1.0 / 6.1 / 2.0** | #111 on `beevia-api` (12 Nov 15:53 UTC) |
| Admin board: open sprint / days since any activity | none / 59.0 | **none / 60.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: #111 is a correctness fix on an existing capability (appendix) |

**No correction to the 12 Nov edition is needed.** #111 merged at 15:53 UTC on 12 Nov, 49 minutes after that edition's cut-off and after its final 15:08 UTC fetch, so its absence there was correct at the time.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **1 own** (`I362`) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**60.0 d**) | **16** (13 `beevia-api`, 1 `beevia-admin-api`, 2 `beevia-db-schema`) | #110 and #111 are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**22.2 d**), `I361` (10.3 d). Both have code on `main` | **3** (`c04e207`, `36b03ff`, `3e23414`) | Branch with the Forgot PIN client is 1.3 days old with no PR. Last own submission 30 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 11.0 days |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**60.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 14.0 days; possibly unpushed work |

**The three questions for standup:** (1) **Who reviews the 24 REVIEW/QA leaves with merged code, and when?** Two full days have now passed with no board action. (2) **When does `feat-forget-pin-fixes` get a PR?** The lock it is the way out of has been live since yesterday morning. (3) **Has anyone picked up the PIN check's race (§3.2 of 12 Nov, `suggestions.md` §4.19)?** No auth code changed today.

**The three things worth knowing:**

1. **The "can't be shown" banner should stop firing for calls and payments.** The sync route's `unresolved` count used to include every row with no ciphertext for the device, and that includes call entries, payment cards, system notices and deleted messages, which the server writes in the clear on purpose. The app on `main` shows "Some messages can't be shown on this device" whenever the count is above zero, so a chat of calls and payments showed the warning with nothing missing. #111 counts only encrypted types that were not deleted. It is server-only, so it reaches users without an app release. It still counts history sent before a device was registered. That is the real case, and the app's existing `message.backfill` path is what fixes it. Read, not run (§3.1).

2. **The Forgot PIN client is still not on `main`, a day after the lock went live.** `feat-forget-pin-fixes` has not changed since 12 Nov 06:49 UTC and has no pull request (`beevia-mobile` pull refs end at Dependabot's #63). On `main`, "Forgot PIN?" still says "coming soon". The lock's three gaps from 12 Nov are unchanged: parallel requests are all compared, the lock does not escalate, and a `reset_token` is reusable within its 5 minutes. There is still no HTTP rate limiter.

3. **Two days with no board action, eight days after 1002 ended.** Zero actions on any board since 11 Nov 06:53 UTC. 24 of 33 REVIEW/QA leaves have merged code, and nothing has ever left review on 1002. Output continues in code (#110, #111, the client branch); acceptance stays at zero. The bottleneck is still the review step, not the developers (§1, §2).

**If you read nothing else:** get `feat-forget-pin-fixes` into review, make the PIN check reserve its attempt before it compares, and spend this week's review time on the 24 items whose code is on `main`.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 12 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. The admin export found only `0901-admin`. **No successor to 1002 has appeared on either board.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **No action in the window.** The 1002 sidecar is byte-identical to 12 Nov, and the CSV body is identical too. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12 Nov | 13 Nov (to 15:03) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 Eight days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902, the one precedent, was swept six days after its end; 1002 is now two days beyond that with no sweep and no successor. A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-api` #111 (the unreadable-message count), #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes`; Dependabot PRs #59–#63. This is a limit of the board, not a finding about the work.

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

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 22.2 d and 10.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean, before and after today's edit.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-13`) it reported 165/165 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). #111 adds no route; it changes what one response field means, which a route-level audit cannot see, so the spec was updated by hand. The in-repo audit still reports phantom lines from the three `diverged` working trees. They were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `b5c046f` → `a4b11cb` | #111 (merged 12 Nov 15:53 UTC): only encrypted, undeleted messages count as `unresolved` |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50 |
| `beevia-db-schema` `main` | `a871f3e` (v0.0.54) | Unchanged |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `e40116d` | Unchanged. `feat-forget-pin-fixes` unchanged at `3e23414`, no PR |

### 3.1 The unreadable-message count (`beevia-api` #111)

- **What changed.** `GET /conversations/{id}/messages` and the `sync.messages` socket call return `unresolved`: how many of the returned messages this device cannot decrypt. It counted every row whose ciphertext for the device was `null`. Calls, payment cards and system notices are written in the clear by the server and render from `content_meta`, and messages deleted for everyone have no content; all of them counted. It now counts only `text`, `image`, `audio`, `file`, `location`, `contact` and `key_exchange` messages not deleted for everyone.
- **Why it matters to users.** The app on `main` reads `unresolved` in `conversation_provider.dart` and shows "Some messages can't be shown on this device" (`someMessagesUnavailableOnDevice`) when it is above zero. The commit cites a dev chat where 34 of 112 counted rows were calls and payment cards. Any chat with a call or a payment showed the warning. The fix is server-only.
- **What it leaves.** Messages sent before a device was registered still count, correctly. The commit calls that history backfill and separate work. The app already has a backfill path on `main` (an existing device answers `device.backfill_requested` in `BackfillService` by re-encrypting its local history to the new device and sending it with `message.backfill`), so whether that case recovers in practice is a question for a real two-device test, not a missing feature.
- **Read, not run.** The commit reports a new end-to-end test (`test/sync-unresolved.e2e-spec.ts`) that fails on the old code. That was not executed here.

### 3.2 The standing checks

- **PIN lock (#110):** no auth file changed in `b5c046f..a4b11cb`. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists (`ThrottlerModule`, `express-rate-limit`: no match).
- **`beevia-api` `release.yml`**: read in full. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. It deploys and runs `pnpm db:migrate` on push to `main`. No workflow file changed in `b5c046f..a4b11cb`; #111 went through the ungated path. No commit on `beevia-db-schema` or `beevia-admin-api`.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50; the consumer API is on 0.0.54.
- **Branch protection, PR reviews and CI results**: cannot be seen from here.

### 3.3 Document changes this cycle

`openapi.yaml`: `getMessageHistory`'s description and `MessageHistory.unresolved` now say which message types count. No operation added, removed or moved. `openapi.admin.yaml`, `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` are unchanged. `api-rfc.md`: a new §5.27; totals unchanged at 165. `admin-api-rfc.md` and `suggestions.md`: unchanged.

---

## 4. Risks

- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19).
- **A locked-out user has no way out on `main`.** The lock is live; the app's Forgot PIN on `main` still says "coming soon". The client branch has no PR.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended eight days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **A 62-file client branch with no PR**, now 1.3 days without a commit.
- **Every backend repo still deploys or migrates production on push without a test gate.** #111 went through it today.
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment. Unchanged.
- **The 30-day NIN clock.** The client is on `main`; whether it has shipped to users is not visible, and the limits are still not enforced.
- **A user can be told a person is coming when none can come.** No role holds `disputes`. Unchanged.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** none.

---

## 5. PRD gap

The four structural gaps are unchanged and carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. #111 corrects a count on existing E2EE messaging and adds no capability. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 6 Nov 15:04 → 13 Nov 15:04 UTC. Commit counts are non-merge commits on all remote refs in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (2 on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**16 commits in 7 days**: 13 in `beevia-api`, 1 in `beevia-admin-api` and 2 in `beevia-db-schema`. The drop from 20 is the window moving past 5–6 Nov, not a slowdown. **One own submission**, `I362` on 11 Nov. **No WIP on 1002.** Since the last cut-off: `beevia-api` #111, not an item on any board. Last commit 1.0 d old. `BVA-I8` has been In progress on the closed admin board for 60.0 days.

### 6.2 David Samuel: mobile

**3 commits** in 7 days: `c04e207` (9 Nov, on `main` via #58) and the two on `feat-forget-pin-fixes` (11 Nov 19:09, 12 Nov 06:49 UTC). Nothing pushed in the window. **Zero submissions.** His last own submission was `I286` on 14 Oct, **30.0 days** ago. **WIP: 2 items, both with code on `main`**: `I331` at 22.2 days and `I361` at 10.3 days. As before, this reads as items left in the wrong column rather than stuck work; that is for him to say. The branch's work has no item. A quiet day on the remote is not a quiet day: local commits are invisible here.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** His last board action was on 2 Nov 15:58 UTC, **11.0 days** ago: finished, blocked or working untracked. Worth a question, not an assumption. Forgot PIN, the PIN lock message and voice-note recording have screens on a branch and no design item. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **14.0 days** old, with no new branch or pull ref on `beevia-admin`. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee; `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 60.0 days.

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
| 2026-W46 (9 Nov → 13 Nov 15:03 UTC) | — | — | **1** | 1 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by anyone other than its submitter since `BVA-I268` on 16 Sep. Output continues in code; acceptance stays at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A one-line count fix and an 88-file branch count the same.
- **Who moved an item is not whether it is done.**
- **Untracked work.** #110, #111 and `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits.** David's 3 commits carry 88 files; #111 is one commit of 179 lines, most of them a test.
- **Unpushed work.** A day with no remote commit says nothing about local work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 12 Nov | Status on 13 Nov |
|---|---|
| **1. Make the PIN check reserve its attempt before comparing** | ❌ **No.** No auth file changed |
| **2. Open a PR for `feat-forget-pin-fixes` and review it** | ❌ **No.** Branch unchanged, no PR |
| **3. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No board action at all** |
| **4. Close 1002 deliberately** | ❌ **Not done, eight days late.** No successor, no sweep, filter still 08-01 |
| **5. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No.** No limiter in `beevia-api` |
| **6. Call each new route from a real build; handle three NIN errors** | ❌ **Not visible** |
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
| **18. Bring the dashboard onto the real contract** | ❌ **No commit in 14.0 days** |
| **19. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No** |
| **20. Parent status moves; assign `I348`, `I349`, `I351`, `I359`, `I390`; admin sprint** | ❌ **No** |
| **21. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **22. `needs: test` on `sync`; current schema on `beevia-admin-api`** | ❌ **Not done.** #111 went through the ungated path |
| **23. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** Today's contract change was found by reading the commit, not by any check |
| **24. Carried items** | ❌ **None moved** |

**None of the 24 is met, and none moved in part.** #111 was not on the list: it fixes a problem the reports had not raised.

---

## 8. What I would do this week

1. **Open a PR for `feat-forget-pin-fixes` and review it (carried, now first).** It is the only way out of the lock for users on `main`. Ask whether the in-app Paystack WebView was a decision.
2. **Make the PIN check reserve its attempt before comparing (carried).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
3. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
4. **Then close 1002 deliberately (carried, eight days late).** Move `I331` and `I361` to review if David agrees. Create the successor, carry `I373`, anything returned and items for #35/#110/#111 and the branch. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
5. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried, `suggestions.md` §4.1).**
6. **Run one two-device chat on a real build (new).** Open a chat with calls and payment cards on a fresh device: the banner should now appear only for history sent before that device existed, and backfill from the other device should clear it. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name (carried).
7. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
8. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
9. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
10. **Handle `call.ended` in the app (carried).**
11. **Put the NIN step, the support screens and Forgot PIN on the board with a design and an owner (carried).**
12. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
13. **Decide the seeded card default and what a card limit is, on the record (carried).**
14. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
15. **Record the consent behind each BVN and NIN lookup (carried).**
16. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
17. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
18. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
19. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
20. **Agree how parent status moves work; assign `I348`, `I349`, `I351`, `I359` and `I390`; give the admin dashboard a sprint (carried).**
21. **Retire `GET /cards/{id}/transactions` (carried).**
22. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.54 (carried).
23. **Generate `openapi.yaml` from the running app and diff it in CI (carried).** It would not have caught today's change either, since a field's meaning moved, not its shape; the commit's own docs and Postman edits did.
24. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 60.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 60 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 14.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-three days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** #111 corrects a count on line 1 (E2EE messaging). The rubric scores whether the design is implemented and wired, not whether it is correct, so a correctness fix does not raise it. Line 1 is held at 0.90 for the voice-note recorder, which is still on the unmerged branch.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | #111 fixes the unreadable count; the voice-note recorder is on a branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Step-up has a lock (#110); biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether #111 is live, and whether the banner is gone in practice.** The workflow deploys on push; its result is not visible, and nothing was run.
- **Whether history backfill recovers a new device's chats.** The code path exists on both ends; it was not exercised.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether any of the merged or branched client screens work against the API.**
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the pull requests were reviewed or approved.**
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag or on the in-app Paystack checkout, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three background exports starting at about 14:57 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 12 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar and CSV body byte-identical. 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-13`: exit 0 before and after the spec edit. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow13.py`, a date-shifted copy of 12 Nov's). It diffed 1002 against 12 Nov, listed every action in the window (none), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `fetch` and `ls-remote` of heads and `refs/pull/*` in all five repos. In `beevia-api`: #111's commit message and its service, docs and Postman diffs; that no auth, env or workflow file changed; the absence of any HTTP rate limiter; `release.yml` in full; both services' schema pins. In `beevia-mobile`: where `main` and `feat-forget-pin-fixes` read `unresolved` and show the banner, and the backfill path (`BackfillService`, `message.backfill`).
6. Spec and narrative updates (§3.3).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed. A final `fetch` of all five repos at 15:05 UTC found nothing new, and a fast 1002 re-export at the same time found no board action (last `actiontime` still 11 Nov 06:53 UTC).

**Files changed this cycle:** this report, `web-report/2026-11-13.html`, `web-report/index.html`, `openapi.yaml` and `api-rfc.md`. New board exports for 13 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 12 Nov 15:04 UTC → 13 Nov 15:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (−07:00).
