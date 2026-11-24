# Beevia — Project Status

**As of 2026-11-24** · Sprint **1002** (21 Oct → 5 Nov, **ended nineteen days ago, day 35**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, 12 of 12 items Done · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: **All three board exports completed today (15:01 UTC), after failing on 23 Nov.** `sprint-board-exports/beevia-sprint-board-2026-11-24.csv` + `beevia-activity-2026-11-24.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-24.csv` + its activity sidecar (12 items, sprint 0901-admin); the read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`. Each was compared with the 20 Nov export, the last one before it. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Client progress was read from the code, not from commit messages.

Scope: five boards, kept separate and never summed. **Code window: 23 Nov 15:25 UTC → 24 Nov 15:02 UTC, 1.0 day. Board window: 20 Nov 15:02 UTC → 24 Nov 15:01 UTC, 4.0 days, because no export exists for 23 Nov.**

---

## Quick overview

> **The boards could be read again today, and they answer yesterday's open question: nothing happened on any of them. All three exports are byte-identical to Friday's, so sprint 1002 has had no action for 13.3 days and ended nineteen days ago with 36 of 44 leaves open and no successor. The day after Status landed, no backend ref moved and none of its open points was touched: no role can review a report, no app calls it, no board item names it, and no document says whether it is in the MVP. The one new commit is on mobile: `feat-forget-pin-fixes` gained a fourth commit at 21:22 UTC on 23 Nov (a hands-free voice-note recorder, redesigned chat bubbles, tests), still with no pull request. That branch's iOS project is now at build 15 against 10 on `main`, which earlier editions did not report. The MVP estimate is unchanged (≈68%).**

| Metric | 23 Nov | 24 Nov | Δ |
|---|---:|---:|---|
| Board exports completed | 0 of 3 | **3 of 3** | Zoho answered normally; each export took about a minute |
| Board actions on 1002 since the 20 Nov export | not measured | **0** | sidecar byte-identical to 20 Nov. Last action 11 Nov 06:53 UTC, **13.3 days** ago |
| Board actions on 0901-admin since the 20 Nov export | not measured | **0** | sidecar byte-identical. Last action 18 Nov 15:03 UTC, 6.0 days ago |
| Sprint 1002 items (leaves + parents) | 63 (44+19)\* | **63 (44+19)** | \* yesterday's figure was the 20 Nov export; confirmed today |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8\* | **1 / 2 / 33 / 0 / 8** | no change since 11 Nov |
| Transitions into REVIEW/QA, last 7 days (leaves) | 0 known | **0** | measured. ISO week 47 (16 → 22 Nov) is the first full week with none (§6.5) |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC\* | **11 Nov 06:53 UTC (Ayomikun, `I362`)** | David's last own submission is still 14 Oct, **41.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0\* | **0** | |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | no `main` moved in any repo |
| Board items that name Status | none as of 20 Nov | **none** | measured today: 0 of 63 on 1002, 0 of 12 on 0901-admin |
| API surface (consumer / admin) | 183 / 85 | **183 / 85** | no backend commit since 10:14 UTC on 23 Nov |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 after edits | **0 / 0** | audit exit 0 on the first run; no spec or RFC was edited today |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | |
| Roles that can review a status report | 0 | **0** | no migration or seed change |
| Status routes called by an app | 0 of 26 | **0 of 26** | no `/statuses` call on mobile `main`, on the mobile branch or in `beevia-admin` |
| Person-authored commits on any branch in the window | 16 | **1** | `ad2c0ed` on `beevia-mobile` `feat-forget-pin-fixes`, 23 Nov 21:22 UTC (§3.1) |
| Pull requests merged in the window | 8 | **0** | |
| `feat-forget-pin-fixes` ahead of `main` | 3 commits, +7,443 / −774 | **4 commits, +8,896 / −1,093** (111 files) | still no PR (non-Dependabot pull refs on `beevia-mobile` end at #58); ninth edition |
| iOS project version on `main` / on the branch | not reported | **1.1.1 (10) / 1.1.6 (15)** | new to this report, though it has been diverging since 12 Nov (correction 2) |
| Open Dependabot PRs on `beevia-mobile` | 8 | **8** | #60, #62–#68; no new branch or commit |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no workflow file changed |
| `beevia-admin` days since a commit | 24.0 | **25.0** | |
| `beevia-mobile` days since a person's commit on `main` / on any branch | 13.0 / 6.4 | **14.0 / 0.7** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a person's commit | 0.2 / 0.2 / 0.3 | **1.2 / 1.2 / 1.3** | |
| Admin board: open sprint / days since any activity | none / 5.0 if untouched | **none / 6.0** | confirmed untouched |
| Estimation points set (1002) | 0/63\* | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: nothing merged to any `main` (appendix) |

**Two corrections to earlier editions.**

1. **Yesterday's board rows were Friday's figures; today they are measured, and nothing had moved.** The 23 Nov edition could not read Zoho and marked every board figure "20 Nov export" or "not measured". Today's sidecars for 1002, 0901-admin and 08-01 are byte-identical to the 20 Nov ones. So the statements yesterday carried with an "if" are now plain: the last action on 1002 was on 11 Nov; ISO week 47 had no transition into review; and no item for Status was added to either board in the four days around its merge.
2. **The mobile branch has been carrying iOS build numbers since 12 Nov, and no edition said so.** This report has read the branch's Dart code in each edition since 12 Nov and never looked at the Xcode project. `main` is at version 1.1.1, build 10. The branch was at 1.1.2 (11) on 12 Nov, 1.1.5 (14) on 17 Nov and is at 1.1.6 (15) since last night; builds 12 and 13 have no commit of their own. Build numbers are normally raised in order to upload a build, so the plain reading is that iOS builds have been cut from this unreviewed branch five times since #58 merged. That is an inference: whether any build was uploaded, and who received it, is not visible from here. Earlier editions listed "whether #58 has shipped to users, in which build" as unknown; the more useful question is which branch testers are running. `pubspec.yaml` says 1.0.1+2 on every ref, so Android's version has not moved in git.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 4, all Done | **0** (last own: `I362`, 11 Nov) | 1.48 d (n=22) | none on any board | **16**, all on 23 Nov (8 `beevia-api`, 5 `beevia-admin-api`, 3 `beevia-db-schema`), under `Phoenixdadhev` | None since 10:14 UTC on 23 Nov. Status has no board item, so the board shows a quiet week |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**33.2 d**), `I361` (21.3 d). Both have code on `main` | **1**, on `feat-forget-pin-fixes` (23 Nov 21:22 UTC), under `Davidtariq96` | Branch now 8,900 lines ahead with no PR, and iOS build 15 against 10 on `main`. Last own submission 41 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 22.0 days. Last night's commit cites two Figma frames, so design work continues that no board shows |
| Promise Udo | admin dashboard | 0901-admin: 4, all Done · **1002: 0** | 0 | n/a | none | **0** (`beevia-admin`, last 30 Oct) | No commit in 25.0 days; no item open on any board; nine admin routes for Status with no screen |

**The three questions for standup:** (1) **Is anyone testing builds made from `feat-forget-pin-fixes`, and when does it become a pull request?** The branch's iOS build number is five ahead of `main`. If testers have it, the code under test has had no review and is not what `main` holds. (2) **Who closes 1002 and opens the next sprint, and when?** It ended nineteen days ago, nothing has moved on it for thirteen, and 24 leaves with merged code are waiting for someone to accept them. (3) **Has Status been decided?** Yesterday's three questions on it (who asked for it, who reviews reports, where it sits against the MVP gaps) have no answer in any repo or on any board a day later.

**The three things worth knowing:**

1. **The boards were not moving while they could not be read.** Today's exports completed in about a minute each and match Friday's byte for byte. Sprint 1002 has had one action since 4 Nov (`I362` to review on 11 Nov). It ended on 5 Nov with 33 leaves in REVIEW/QA, of which 24 have merged code behind them, and nothing has ever left review on it. No successor sprint exists in Zoho's list, and the admin project still has only its closed `0901-admin`. The week of 16 to 22 Nov is the first in this report's trend table with no item entering review at all. Two things explain that without anyone slowing down: the backend's merged work (Status, Forgot PIN, message edit) has no item to move, and the mobile work is on a branch with no PR (§1, §6.5).

2. **Mobile work surfaced last night, on the same unmerged branch, and that branch is where the iOS builds come from.** `ad2c0ed` (6 files, +1,705 / −571) adds tap-to-record voice notes with pause, listen-back and resume, redraws the chat bubbles and call bubbles to cited Figma frames, moves the sent/delivered/read mark to the latest message only, and adds a 264-line widget test. It is tidy work and it answers part of yesterday's "what else is unpushed". It also makes the branch 8,900 lines and 111 files ahead of `main`, holding the only way out of the PIN lock, the offline-delete fix, message edit, forwarding, stars and now voice notes in two recording modes. Its iOS project says version 1.1.6, build 15; `main` says 1.1.1, build 10 (correction 2, §3.1).

3. **Status is exactly where it was at 10:14 UTC yesterday.** No backend ref moved. The `statuses` permission is still granted to no role, so a report can be filed by any signed-in user against the live routes and nobody can open it; evidence for an unclosed case is still kept without limit; the other eleven points in `suggestions.md` §4.21 stand. Neither app calls any of the 26 routes, no board item names the feature, and nothing in the PRD or any other document here says whether it is in the MVP. The estimate stays at 68.36, the four structural gaps still carry 32 of 100 points, and the grace before the NIN requirement bites ends about 6 Dec, **12 days** from now (§3.2, §5).

**If you read nothing else:** find out which branch the testers' iOS build comes from and open the pull request for it, close 1002 by reviewing the 24 leaves that have code, and write down whether Status is in the MVP.

---

## 1. Board movement

### 1.1 All three boards read; none moved in four days

**Every export completed today.** The 23 Nov edition had none, so this section compares today with the 20 Nov exports, the last ones on disk, and so covers Friday afternoon, the weekend, Monday and today up to 15:01 UTC.

| Board | Items | Last action | Since the 20 Nov export |
|---|---:|---|---|
| 1002 (live, scratch export) | 63 (44 leaves + 19 parents) | 11 Nov 06:53 UTC, 13.3 days ago | **0 actions.** CSV identical apart from its export date; sidecar byte-identical |
| 0901-admin | 12 (8 leaves + 4 parents), all Done | 18 Nov 15:03 UTC, 6.0 days ago | **0 actions.** Sidecar byte-identical |
| 08-01 (the in-repo main export) | 64 (41 leaves + 23 parents), all Done | 3 Sep | **0 actions.** Sidecar byte-identical. The audit's `SINCE` block reports no change, as it must for a closed sprint |
| 0902, 0901 | closed | 21 Oct, 30 Sep | not re-exported; the scratch copies from 20 Nov were reused for cycle times |

1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–24 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | **0** |

There are no comments on 1002, `I392` still shows Done with 0 of 63 ticked, and nothing has ever left REVIEW/QA on it. Zoho's sprint list, checked after the exports at 15:02 UTC, is `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project: **no successor to 1002 on either board.** `ZOHO_SPRINT_FILTER` still points at 08-01.

### 1.2 Nineteen days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902 was swept six days after its end; 1002 is thirteen days beyond that. A sweep would mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** Status in all three backend repos (26 routes, twelve tables); `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111, #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); the whole of `beevia-mobile` `feat-forget-pin-fixes`, now four commits; eight open Dependabot PRs. That is a gap in the board, not a judgement on the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

From today's export, which is unchanged since 11 Nov. The code column was re-checked: no `main` moved in any repo since yesterday's edition.

| REVIEW/QA leaves (33) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | 12 | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391`, `I362` | Routes on `origin/main`. `I387` caps funding, not spending. `I391` lacks the pagination, search and filter it asks for. `I362` reports limits and does not enforce them |
| Mobile, matching merged code | 12 | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, `I386` | On `main` since #58 (10 Nov). `I390` is still unassigned |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Moved to review, no matching code | 2 | `I348`, `I372` | `I348`: the dashboard screen is mock only. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 33.2 d and 21.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do, unassigned; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.
- **Nothing on 1002 or 0901-admin mentions Status.** Searched in today's exports, item names and descriptions. Yesterday this could only be said of Friday's export.

---

## 3. Code, API surface and spec drift

**Audit: clean on the first run, and no document was edited.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-24`) it reports 183/183 routes in `beevia-api` and 85/85 in `beevia-admin-api`, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). The in-repo audit still reports phantom lines from the three `diverged` working trees (2 / 54 / 51, the same as yesterday). They were not acted on. Because the audit compares routes and not fields, the head commits were also compared with yesterday's recorded SHAs: all five `origin/main` heads are equal, so there is no contract change it could have missed.

| Repo | `origin/main` | What |
|---|---|---|
| `beevia-api` | `8ebaf0c` | Unchanged since #118 (23 Nov 10:13 UTC). No branch besides `main`; pull refs end at #118 |
| `beevia-admin-api` | `e83e86f` | Unchanged since #33 (23 Nov 10:14 UTC). No other branch |
| `beevia-db-schema` | `92b034b` (v0.0.58) | Unchanged |
| `beevia-admin` | `64304ef` (30 Oct) | Unchanged. No branch besides `main`, no pull ref |
| `beevia-mobile` | `e40116d` | `main` unchanged since 10 Nov. **`feat-forget-pin-fixes` moved `d55630e` → `ad2c0ed`** (23 Nov 21:22 UTC). No PR. The eight Dependabot branches and `App-bundle` unchanged |

### 3.1 The mobile commit (`ad2c0ed`, branch only)

Read from the code; nothing was built or run. Six files, +1,705 / −571, under `Davidtariq96`.

- **Tap to record a voice note hands-free.** Holding the mic still records and sends on release. A tap now opens a composer in place of the message bar: a timer and live waveform, then pause, listen back to the note so far, continue, delete or send. A call or backgrounding the app pauses a tapped note instead of sending it, and the 10-minute cap pauses it too.
- **Two audio formats now leave the app.** A held note is an `.m4a` file sent as `audio/mp4`, as before. A tapped note is raw AAC frames written to an `.aac` file and sent as `audio/aac`, because that is what makes pause and resume possible. The server accepts it: its only type check on a voice note is that the type starts with `audio/` (`voice-note.ts`). Whether the other phone plays that file, on both platforms, and can scrub within it, was not tested here; the bubble's length comes from `durationMs`, which the app still sends.
- **Read marks moved.** Sent, delivered and read now show under this user's most recent message only (ticks, then the other person's photo once read), not in groups, and stop at "delivered" when either side has read receipts off.
- **Bubbles redrawn to the design.** Outgoing messages take an inverted fill, call bubbles read "Missed", "Declined" or "Call back", and the header's call button opens a voice or video menu. The code cites Figma frames `4762:14925` and `4773:45785`.
- **Tests.** A new 264-line widget test covers the receipt rule, the bubbles, the call bubbles and the composer's two states. The branch has 132 files under `test/` against 129 on `main`.
- **iOS version 1.1.5 (14) → 1.1.6 (15).** See correction 2.

What it does not touch: Forgot PIN, `call.ended` (still unhandled), any money, card or KYC screen, and Status. Nothing in it names a board item.

**The branch as a whole** is now 4 commits and 111 files ahead of `main` (+8,896 / −1,093; 76 of the files are under `lib`). First recommended for a pull request on 12 Nov. Each commit since has made it harder to review in one sitting, and the build numbers suggest it is already what is being run.

### 3.2 Status, one day on

No backend commit since the merges, so every point of `suggestions.md` §4.21 stands as written yesterday. The checks this report will repeat each edition until they change:

| Check | 24 Nov |
|---|---|
| A role holds `statuses` | **No.** Migration 0056 grants it to nobody; no later migration; the seed script is unchanged and no workflow runs it. A grant made by hand in production would not be visible |
| Unreviewed cases are swept or auto-closed | **No.** Evidence is deleted 90 days after a case closes, and nothing closes a case without a reviewer |
| Evidence media is served with a checked content type and `nosniff` | **No** |
| Open uploads are capped per user | **No** |
| The daily limit survives deletion | **No.** It counts statuses that still exist |
| `beevia-mobile` calls `/statuses` | **No**, on `main` or on the branch (including last night's commit) |
| `beevia-admin` has a moderation screen | **No.** No commit since 30 Oct |
| A board item exists | **No**, measured today on both boards |
| The owner's decision is written down | **Not in this workspace.** `Beevia_PRD.md`, `PRODUCT.md` and the board are unchanged |

The API deploys on push, so the routes are presumably answering since yesterday morning. Whether the deploy and migration 0056 completed is not visible from here.

### 3.3 The standing checks

- **PIN lock (#110):** no change. The three gaps in `suggestions.md` §4.19 stand, and no HTTP rate limiter exists.
- **`release.yml` in all three backend repos:** unchanged. `beevia-api`'s `sync` still has no `needs: test` and runs `pnpm db:migrate` on push to `main`.
- **Schema pin:** both APIs on `beevia-db-schema` 0.0.58.
- **`call.ended`** is still unhandled on `main` and on the branch. Forgot PIN on the app's `main` is still a stub.
- **`activeNgn()`** is unchanged at three call sites in `payment.service.ts`.
- **Dependabot:** #60 and #62–#68 unchanged since 18 Nov.
- **Branch protection, PR reviews and CI results:** cannot be seen from here.

### 3.4 Document changes this cycle

**None.** `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin.yaml`, `openapi.admin.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md` and `suggestions.md` are as committed yesterday. The audit was clean and no merged contract changed. The observations on the mobile branch are in §3.1 and will go into `suggestions.md` when the branch merges or a decision is asked for there.

---

## 4. Risks

One is new today and is listed first. The rest are carried, in the order they bite.

- **New: the build people are testing may not be the code anyone has reviewed.** The iOS project on `feat-forget-pin-fixes` is five build numbers ahead of `main`. If builds 11 to 15 went to testers, then feedback, bug reports and any sign-off refer to 8,900 lines that are not on `main`, have no pull request and have had no visible review. It also means a release cut from `main` would be older than what was tested. This rests on an inference from build numbers (correction 2).
- **A moderation path that accepts reports and has no reviewer.** Three reporters hide a status; no role can open the case; the evidence, which Beevia can read, is kept until someone closes it. Live since yesterday, with or without an app screen (§3.2).
- **The largest piece of work this month is outside the PRD, and the record does not say why.** If Status is wanted for launch, the plan and the rubric should say so. If it is not, three workstreams will be asked to build a client and a moderation screen for it ahead of FX, the international tier and consent.
- **A locked-out user has no way out on `main`.** The wrong-PIN lock has been on the API's `main` since 12 Nov and Forgot PIN on the app's `main` is still a stub. The fix is on the unmerged branch.
- **One large unreviewed branch is the only path for three user-facing fixes:** a way out of the PIN lock, offline delete, and edit. It grew again last night.
- **The 30-day NIN clock.** The limits are still not enforced. The grace for existing users ends about 6 Dec, **12 days from now**.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended nineteen days ago with no successor sprint, and the board has been still for thirteen.** A board nobody updates stops being a source for anything, including this report's flow figures.
- **Work may still be sitting unpushed** in the dashboard and design. Backend work surfaced on Monday morning and mobile work on Monday night, both after days of quiet.
- **Two production data migrations in nine days with no test gate** (0055 on 16 Nov, 0056 on 23 Nov). Whether either ran cleanly is not visible.
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19). Status added 17 routes with no limiter in front.
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **Two voice-note formats, one of them new and untested across platforms.** Branch only; a note that does not play on the other phone would look sent to its sender (§3.1).
- **Major dependency bumps waiting on a reviewer.** #66/#67 (ML Kit) and #68 (notifications) are unchanged.
- **Done on the admin board means "closed by the story's owner", never "reviewed".** None of its 12 items passed through REVIEW/QA. The same mechanism closed `I381` on 1002 without its code.
- **The admin dashboard has no open board item anywhere** and no commit for 25 days, while three admin items on 1002 have no assignee and nine admin routes for Status have no screen.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **A user can be told a person is coming when none can come.** No role holds `disputes`, `help_center` or `statuses`.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.

---

## 5. PRD gap

**Nothing moved toward or away from the PRD today.** No `main` changed. Last night's mobile commit is polish and one new interaction inside E2EE messaging (line 1), on a branch, so it closes no gap and scores nothing until it merges.

The four structural gaps still carry 32 of the rubric's 100 points: international KYC, multi-currency and FX settlement, consent management, and virtual cards beyond what is wired. `activeNgn()` is unchanged, so FX is not started. Status still sits outside the PRD (no status, stories or 24-hour post feature in `Beevia_PRD.md`), and whether it belongs in the MVP is the owner's call. This report takes no side on it; it notes that a day has passed and the call is still not written anywhere it can read.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 17 Nov 15:02 → 24 Nov 15:02 UTC. Commit counts are non-merge commits on all remote branches in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded. The two identity mappings are inferred, not confirmed. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** were recomputed from today's 1002 export and the scratch copies of 0901 and 0902, and are unchanged: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3). No item has entered review since 11 Nov, so there is nothing new for them to include.

### 6.1 Ayomikun Araoye: backend + admin API

**16 commits in 7 days**, all under `Phoenixdadhev` and all on 23 Nov between 03:04 and 10:06 UTC: 8 in `beevia-api`, 5 in `beevia-admin-api`, 3 in `beevia-db-schema`. **None since.** No board submission in 7 days (measured today); the last was `I362` on 11 Nov. Ayomikun has **no WIP on any board**, and 16 leaves waiting in REVIEW/QA that nobody has accepted or returned. The board therefore shows two quiet weeks for the person who merged the month's largest feature. That is a board gap, not a judgement. One quiet day after a large merge says nothing either way; Friday's three quiet days turned out to be Status.

### 6.2 David Samuel: mobile

**1 commit** in 7 days, `ad2c0ed` on `feat-forget-pin-fixes` (23 Nov 21:22 UTC), six hours after yesterday's edition and the first push in 6.6 days. The commit before it (`d55630e`, 17 Nov 05:51 UTC) has just left the 7-day window. **No board submission in 7 days.** The last own submission was `I286` on 14 Oct, **41.0 days** ago. A branch with no PR cannot meaningfully be moved to review, so this still reads as a board gap rather than idle time: the branch holds four commits made between 11 and 23 Nov. **WIP: 2 items, both with code on `main`**: `I331` at 33.2 days and `I361` at 21.3 days, against a median cycle of 0.99 days. These read as items left in the wrong column rather than stuck work; that is for David to say. The question worth asking is not about pace. It is which code the current test builds contain, and what stands in the way of a pull request.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** The last board action by Philip was on 2 Nov 15:58 UTC, **22.0 days** ago. Design work is plainly continuing somewhere: last night's mobile commit builds to two named Figma frames (chat bubbles and the voice-note composer), and the Status code refers to "the designs". None of it is an item on any board, and whose it is cannot be seen. Philip may be finished with what the board holds, blocked, or working untracked; worth a question, not an assumption. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **25.0 days** old, and `beevia-admin` has no other branch or pull ref. **Promise has no open item on any board** (measured today), and the admin items on 1002 (`I348` in REVIEW/QA, `I349` and `I351` To do) are unassigned. The admin API has nine Status routes with no screen, on top of the support inbox that still runs on its mock. This report does not read a quiet remote as nothing having been done; both the backend and mobile showed this week that work can sit unpushed for days. The question is what the current work is and where it is tracked.

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
| 2026-W47 (16 → 22 Nov) | — | — | **0** | 0 | 0 | 0 |
| 2026-W48 (23 Nov, to 24 Nov 15:01 UTC) | — | — | **0** | 0 | 0 | 0 |

The 1002 rows were recomputed today. The W39–W42 rows are carried from earlier editions: 15 of 0902's leaves were removed from that sprint on 21 Oct and their history is no longer in any export.

**W47 is now confirmed as the first week in this table with no transition into review.** It was not a week without work: Status was being written during it and the mobile branch grew before and after it. The work had no item to move (backend) or no pull request to point an item at (mobile). **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. **The bottleneck is the board and review process, not the developers.**

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 5,000-line feature and a one-line fix count the same.
- **Unpushed work.** A quiet remote says nothing about local work. This week showed it twice.
- **Untracked work.** Status, #110–#112, #35, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **When work was done.** Commit timestamps record when it was committed.
- **Who moved an item is not whether it is done.** `I9` was moved by its parent's close, not by its owner.
- **Commit counts reward small commits.** One commit of 1,700 lines and sixteen in a morning are not comparable, and neither measures a week.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository. The new widget tests were read by name, not run.

---

## 7. Previous recommendations: where they stand

Boards were readable today, so the rows marked "not measured" yesterday have an answer.

| Recommendation from 23 Nov | Status on 24 Nov |
|---|---|
| **1. Decide on the record whether Status is in the MVP** | ❌ **No record.** No document changed and no board item exists |
| **2. Grant `statuses` to a role, name a reviewer, close the four server points** | ❌ **No.** No backend commit since the merges. A grant made by hand would not be visible |
| **3. Take the Status product decisions in one sitting** | ❌ **Not visible** |
| **4. Open a PR for `feat-forget-pin-fixes`, or split it, and review it** | ❌ **No, and the branch grew** by a fourth commit (+1,705 / −571). First recommended 12 Nov, ninth edition |
| **5. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No.** Nothing has left REVIEW/QA; no board action since 11 Nov |
| **6. Close 1002 deliberately** | ❌ **No.** Nineteen days late; no successor sprint; not swept either |
| **7. Put the untracked work on the board with an owner and a design item** | ❌ **No.** 1002 still has 63 items and none was added; the untracked list grew by last night's commit |
| **8. Push what is local to a branch, as a habit** | 🟡 **In part.** Mobile pushed one commit last night after 6.6 days. Nothing from the dashboard |
| **9. Give the admin dashboard current work on a board, with Promise as owner** | ❌ **No.** No admin sprint; `I348`, `I349` and `I351` still unassigned |
| **10. Decide whether the tier limits are enforced** | ❌ **No.** 12 days left |
| **11. Give the Dependabot queue an owner** | ❌ **Not visible.** All eight PRs still open |
| **12. Make the PIN check reserve its attempt before comparing** | ❌ **No** |
| **13. HTTP rate limiting on PIN, OTP and lookup routes, then Status** | ❌ **No** |
| **14. Two-device chat on a build of the branch** | ❌ **Not visible.** The branch's build numbers suggest builds exist; whether this test was run on one is not known |
| **15. Confirm migrations 0055 and 0056 ran cleanly in production** | ❌ **Not visible** |
| **16. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **17. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **18. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible** |
| **19. Handle `call.ended` in the app** | ❌ **No**, on `main` or on the branch |
| **20. NIN step and support screens on the board** | ❌ **No** |
| **21. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **22. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **23. Record the consent behind each lookup** | ❌ **No** |
| **24. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No** |
| **25. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **26. Bring the dashboard onto the real contract** | ❌ **No commit in 25.0 days** |
| **27. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❌ **No.** All three still Done |
| **28. Assign `I359` and `I390`** | ❌ **No.** Both still unassigned |
| **29. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **30. `needs: test` on `sync`; verify jobs on the other two** | ❌ **No.** No workflow file changed |
| **31. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No** |
| **32. Carried items** | ❌ **None moved** |

**One of the 32 moved in part (8); none was met in full.** That is one working day after they were written, so it is not a verdict. What is worth noticing is the age of the oldest: the pull request (first asked for on 12 Nov), the review of the queue, and the close of 1002 (which ended on 5 Nov) are the three that everything else waits on. "Not visible" marks the ones that could have happened without leaving a trace in git or on a board; the rest would have.

---

## 8. What I would do this week

No new point is added. Point 1 is promoted and sharpened by the build numbers; the order otherwise follows yesterday. Thirty-two items is too many to act on, so the first six are the ones that unblock the rest.

1. **Open a PR for `feat-forget-pin-fixes` today, as it stands, and say which build testers have (carried from 12 Nov, ninth edition; was point 4).** If builds 11 to 15 came from this branch, the fastest honest fix is to get the branch reviewed and merged so that `main` is again what is tested. Splitting it into Forgot PIN, the app side of #112, and the voice-note and bubble work would make review easier, but a single open PR is better than a fifth week without one. In that review, settle the 15-minute edit window (`suggestions.md` §4.20), ask whether the in-app Paystack WebView was a decision, and play a tapped voice note on the other platform.
2. **Decide on the record whether Status is in the MVP (carried).** One paragraph in the PRD or the plan: who it is for, whether it ships at launch, and where it sits against FX, the international tier and consent. If it is in, it needs board items, an owner on mobile and on the dashboard, and a line in the readiness rubric (a methodology change this report would then make and call out). If it is not, say so before a client is started.
3. **Before any app can file a report: grant `statuses` to a role and name who reviews (carried).** Then close the four server points that do not need a product decision: sweep or auto-close unreviewed cases so evidence is not kept without limit; allow only image and video types on the evidence route and send `nosniff`; cap open uploads per user; count the daily limit from something deletion does not lower (`suggestions.md` §4.21, points 1, 2, 7, 8, 9).
4. **Take the Status product decisions in one sitting (carried):** what three reports should do given a 24-hour life; whether a deleted status can be reported; whether storing the report key as received is acceptable; and log every evidence view (`suggestions.md` §4.21, points 3 to 6). Write the answer where `admin-api-rfc.md` §5.1c asks for it.
5. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
6. **Then close 1002 deliberately (carried, nineteen days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and the items from point 7. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
7. **Put the untracked work on the board with an owner and a design item (carried):** Status, the branch's pieces (Forgot PIN, edit and delete, forwarding and stars, voice notes, the bubble redesign), and #110–#112, #35 and #36.
8. **Push what is local to a branch, as a habit (carried).** It worked for the backend on Monday morning and for mobile on Monday night. Unfinished work on a pushed branch can be backed up, seen and reviewed.
9. **Give the admin dashboard current work on a board, with Promise as owner (carried).** Either open an admin sprint, or assign `I348`, `I349` and `I351` on 1002 to Promise. Then agree that a child owned by someone else is not closed by its parent's close.
10. **Decide whether the tier limits are enforced, and what the end of the grace does (carried, 12 days left).** About 6 Dec is the date for existing users.
11. **Give the Dependabot queue an owner (carried).** Merge #64 and #65 after a build. Merge #66 and #67 together, after one on-device translation run. Merge #68 after a push test on a device. Close #60, #62 and #63 or merge them with the rest.
12. **Make the PIN check reserve its attempt before comparing (carried).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
13. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes, then the Status uploads and posts (carried, `suggestions.md` §4.1).**
14. **Run one two-device chat on a build of the branch (carried).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Send a held voice note and a tapped one each way between an iPhone and an Android phone. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
15. **Confirm migrations 0055 and 0056 ran cleanly in production (carried).**
16. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
17. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
18. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).** Do it in the same change as `statuses`.
19. **Handle `call.ended` in the app (carried).**
20. **Put the NIN step and the support screens on the board with a design and an owner (carried).**
21. **Decide the seeded card default and what a card limit is, on the record (carried).**
22. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
23. **Record the consent behind each BVN and NIN lookup (carried).**
24. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
25. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
26. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
27. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried).**
28. **Assign `I359` and `I390` (carried).**
29. **Retire `GET /cards/{id}/transactions` (carried).**
30. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried).
31. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
32. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

**Read today, and unchanged.** `0901-admin` has 12 of 12 items Done (8 leaves + 4 parents). Its export and activity sidecar are identical to 20 Nov; the last action is still the close of the story `BVA-I7` and its children `I8` and `I9` on 18 Nov at 15:03 UTC.

| Status | 20 Nov | 24 Nov |
|---|---:|---:|
| Leaves In progress | 0 | **0** |
| Leaves Done | 8 | **8** |
| Parents Done | 4 of 4 | **4 of 4** |
| Board actions since the previous export | 0 | **0** |
| Days since any activity | 2.0 | **6.0** |

The sprint ended 22 Sep, and Zoho's sprint list still shows only `0901-admin` for this project, so **the admin dashboard has no open sprint and no open item on its own board.** None of its 12 items passed through REVIEW/QA; Done here means closed by the story's owner. Admin-dashboard work that is tracked at all sits on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). The nine status-moderation routes have no item on this board or on 1002. `beevia-admin` last moved 25.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed 84 days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves, because no `main` moved.** All five `origin/main` heads equal the SHAs recorded yesterday. The one new commit is on an unmerged mobile branch. The rubric scores merged code, so the tap-to-record composer, the bubble redesign and the receipt change do not raise line 1, in the same way the edit client and Forgot PIN on that branch have not since 12 Nov. When the branch merges, lines 1, 2 and 4 are the ones to re-score. Status still has no line (see the 23 Nov edition's appendix); nothing about that changed.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No change on `main`. Edit client, catch-up `changes` and the voice-note recorder are on an unmerged branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound. ML Kit bumps (#66, #67) unmerged |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | Unchanged. Status moderation is outside the spec's modules and has no screen |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether any iOS build was made or distributed from the branch, to whom, and whether Android builds exist.** The build numbers are in git; uploads and testers are not.
- **Whether a tapped voice note plays on the other phone.** Nothing was run, and no device was used.
- **Who asked for Status, when, and whether it is meant for launch.** No document, board item or PR description readable from here says.
- **Whether Status is deployed, and whether migration 0056 ran cleanly.** The workflow deploys and migrates on push; its result is not visible.
- **Whether Status works.** Nothing was run.
- **Whether any role was granted `statuses`, `disputes` or `help_center` by hand,** or whether the seed script was run in production.
- **Whether the admin API has the `S3_*` settings in production**, without which reported photos and videos cannot be reviewed.
- **Whether anyone else has unpushed work, and how much.** Only remotes are visible.
- **Whether the mobile branch builds, passes its tests, runs, or edits and deletes correctly against the server.**
- **Whether the app builds against the Dependabot bumps**, and whether GitHub shows #59 and #61 as closed.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether any pull request was reviewed or approved by a second person.**
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag, on the in-app Paystack checkout, on the 15-minute edit window or on device-only stars, and whether a privacy or legal review happened**, for those or for Status reports.
- **What the design items contain,** and where the Status, chat-bubble and voice-note designs are tracked. Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Exports (step 1), started 15:00 UTC as three separate background runs, **all exit 0**: the main board (step 1a, 64 items, sprint 08-01, with `--modified --activity`); the admin board (step 1b, with `--sprint 0901-admin`, 12 items); and a read-only scratch export of 1002 (63 items) to `/tmp/beevia-scratch/1002/`. All three were written by 15:02 UTC. Each CSV was diffed and each sidecar byte-compared against its 20 Nov counterpart. A sprint-name check on both projects followed at 15:02 UTC, and a last `ls-remote` of all five repos at 15:08 UTC found no ref changed since the sync.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep. Nothing was fast-forwarded today; the sync's `fetch` brought in the new mobile branch commit.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-24`: exit 0. The in-repo audit also ran, for the board section and its `SINCE` block (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Spec reconciliation (step 4): nothing to reconcile. The audit was clean and all five `origin/main` heads equal yesterday's recorded SHAs, so no document was edited.
5. Code reading. The full diff of `ad2c0ed` for `chat_details.dart` and `voice_recorder.dart`; the new composer's and the bubble file's structure and comments; the test names; the Xcode project version on `main` and on each of the branch's commits; and the server's voice-note check on `origin/main`. `chat_widgets.dart` (1,114 changed lines) was read for its new classes and comments, not line by line.
6. Board analysis (`flow24.py`, a date-shifted copy of the script used since October), on today's exports: every action since the 20 Nov export (none), submissions split by actor, cycle medians, WIP ages and the 1002 rows of the weekly trend.
7. Content checks. `ls-remote` of heads and `refs/pull/*` in all five repos; a `git log` of every remote ref since 22 Nov; item states for the carried recommendations read from today's 1002 export.
8. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`diff`/`show`/`grep`/`ls-tree`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-11-24.html`, `web-report/index.html`, and four new export files (`sprint-board-exports/beevia-sprint-board-2026-11-24.csv`, `beevia-activity-2026-11-24.json`, and the two `admin/` counterparts). No spec, RFC or `suggestions.md` change.

**Degraded inputs.**

- **There is no 23 Nov board export, and there never will be.** Today's exports were compared with 20 Nov. Since all three sidecars are byte-identical, the gap hides nothing: an action on 21, 22 or 23 Nov would be in today's audit trail.
- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export, which is outside the repository and is not kept.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **The export's "Epic … FIELD_MAP gap" warning appeared on all three runs.** It is a sampling artefact recorded on 17 Sep, not a missing column.
- **GitHub PR metadata, reviews, settings, CI results, build uploads and deploy state cannot be seen from here.** PR numbers and merge times come from merge commits and pull refs.
- **The W39–W42 rows of the weekly trend are carried, not recomputed.** A fresh 0902 export holds 8 items; the 15 leaves removed on 21 Oct are gone from it.
- **The item-to-code mapping for the 24 REVIEW/QA leaves was carried** (backend from 11 Nov, mobile from 10 Nov). No `main` has changed those routes or screens since.

**Window.** Code: 23 Nov 15:25 UTC → 24 Nov 15:02 UTC. Boards: 20 Nov 15:02 UTC → 24 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
