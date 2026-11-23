# Beevia — Project Status

**As of 2026-11-23** (code and specs; **board figures are the 20 Nov export, because today's Zoho exports failed**) · Sprint **1002** (21 Oct → 5 Nov, **ended eighteen days ago, day 34**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, 12 of 12 items Done · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: **All board data is the 20 Nov 15:02 UTC export. No export completed today: Zoho's API answered slowly and then timed out on every attempt (appendix), so no board figure in this report is newer than Friday.** `sprint-board-exports/beevia-sprint-board-2026-11-20.csv` + `beevia-activity-2026-11-20.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-20.csv` + its activity sidecar (12 items, sprint 0901-admin); the read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, also dated 20 Nov. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 20 Nov 15:02 UTC → 23 Nov 15:25 UTC, 3.0 days (Fri → Mon, over a weekend).**

---

## Quick overview

> **After three days with nothing on any remote, a whole feature arrived on Monday morning. "Status" (24-hour posts, end to end encrypted, with a report-and-review path) was committed and merged across the database package, the consumer API and the admin API between 08:05 and 10:14 UTC today: 26 new routes (17 + 9), about 7,500 lines of which about 3,300 are tests. It is carefully built, and it is not in the PRD, not on any board as of Friday's export, and not called by either app. The MVP estimate does not move (≈68%), because Status is none of the eleven capabilities and the four gaps that carry 32 points were not touched. No role can review a status report yet. The boards could not be read today: no Zoho export completed, so every board figure below is Friday's export, which showed sprint 1002 untouched since 11 Nov.**

| Metric | 20 Nov | 23 Nov | Δ |
|---|---:|---:|---|
| API surface (consumer / admin) | 166 / 76 | **183 / 85** | **+17 / +9**, all of it Status (§3) |
| Routes in code but not in the spec (consumer / admin) | 0 / 0 | **0 / 0** after today's edits | the audit found 17 / 9 undocumented; all 26 are now in the specs, exit 0 |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | Status was never proposed, so nothing left the proposed files |
| Person-authored commits on any branch in the window | 0 | **16** (non-merge), all backend, all on 23 Nov between 03:04 and 10:06 UTC | first since 17 Nov. 8 `beevia-api`, 5 `beevia-admin-api`, 3 `beevia-db-schema` |
| Pull requests merged in the window | 0 | **8** | `beevia-api` #113, #115, #118 · `beevia-admin-api` #32, #33 · `beevia-db-schema` #37, #38, #39. Three carry Status; five are package updates or stacked on them (§3) |
| `beevia-db-schema` version | v0.0.55 | **v0.0.58** | 0056 adds twelve tables; both APIs now pin 0.0.58 |
| `beevia-admin-api` schema pin | 0.0.50 | **0.0.58** | the five-version gap carried since 7 Nov is closed |
| Roles that can review a status report | n/a | **0** | `statuses` is granted to no role by its migration (§3.2) |
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)\*** | \* **20 Nov export.** Not re-read today |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8\*** | \* 20 Nov export |
| Board actions on 1002 in the window | 0 | **not measured** | export failed. Last known action 11 Nov 06:53 UTC, which is 12.4 days ago if nothing has happened since |
| Board actions on 0901-admin in the window | 0 | **not measured** | export failed. Last known action 18 Nov 15:03 UTC |
| Transitions into REVIEW/QA, last 7 days (leaves) | 0 | **0 known** | none between 16 Nov and the 20 Nov export; the three days since are not covered |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC\* (Ayomikun, `I362`)** | David's last own submission is still 14 Oct, **40.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0\*** | |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | no mobile or dashboard code moved |
| Work merged in the window that is an item on a board | n/a | **0 of 26 routes**\* | \* no item on 1002 or 0901-admin mentioned Status as of the 20 Nov exports |
| `feat-forget-pin-fixes` ahead of `main` | 3 commits, +7,443 / −774 | **unchanged** at `d55630e` | still no PR (non-Dependabot pull refs on `beevia-mobile` end at #58); eighth edition |
| Open Dependabot PRs on `beevia-mobile` | 8 (#60, #62–#68) | **8** | no new branch or commit |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | 5, then a 30-minute lock | **unchanged** | the three gaps in `suggestions.md` §4.19 remain |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no workflow file changed; Status went out this way |
| `beevia-admin` days since a commit | 21.0 | **24.0** | |
| `beevia-mobile` days since a person's commit on `main` / on any branch | 10.0 / 3.4 | **13.0 / 6.4** | |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a person's commit | 4.1 / 13.1 / 4.1 | **0.2 / 0.2 / 0.3** | |
| Admin board: open sprint / days since any activity | none / 2.0 | **none / 5.0 if untouched since 20 Nov** | |
| Estimation points set (1002) | 0/63 | **0/63\*** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: Status is not a rubric line, and no scored capability moved (appendix) |

**Two corrections, one to the previous edition's reading and one to this workspace's own spec.**

1. **Friday's "nothing changed" was true of the remotes and silent about the work.** The 20 Nov edition said so in terms ("it does not say nothing was done") and made unpushed work its first standup question. Today answers it for the backend: sixteen commits are stamped inside seven hours on 23 Nov, and a feature with 5,500 lines of API code and integration tests was not written in that time. The quiet days were this feature being built somewhere this report could not see. The same may be true of the other three workstreams, which are still quiet.
2. **`openapi.yaml` has been wrong about `/users/me/settings` since 30 July.** It listed `messageHistorySyncEnabled` only. `readReceiptsEnabled` shipped in `ae348eb` on 30 Jul and was never added, through every edition that reported the audit as clean. The audit compares routes, not fields, so it could not see it; it surfaced today only because Status added a third field to the same object. All three are in the spec now. "Audit clean" has only ever meant "no route is missing".

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 4, all Done | **0\*** (last own: `I362`, 11 Nov) | 1.48 d (n=22) | none on any board | **16** (8 `beevia-api`, 5 `beevia-admin-api`, 3 `beevia-db-schema`), under `Phoenixdadhev` | Nine are Status and seven are package updates; none is an item on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0\*** | 0.99 d (n=36) | 2: `I331` (**32.2 d**), `I361` (20.3 d). Both have code on `main` | **1**, on `feat-forget-pin-fixes` (17 Nov) | Branch 7,400 lines ahead with no PR. Nothing pushed for 6.4 days. Last own submission 40 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0\* | 0.89 d (n=3) | none | n/a | No board action in 21.0 days. The Status code cites "the designs", so design work exists that no board shows |
| Promise Udo | admin dashboard | 0901-admin: 4, all Done · **1002: 0** | 0 | n/a | none | **0** (`beevia-admin`, last 30 Oct) | No commit in 24.0 days; no item open on any board; nine new admin routes with no screen |

**The three questions for standup:** (1) **Who asked for Status, and where does it sit against the four MVP gaps?** It may well have been asked for; no document or board item says so, and FX, the international tier and consent are still at zero with the provisional target 83 days past. (2) **Who will review status reports, and when is that role granted?** Until then a report hides a status after three reporters and nobody can look at it. (3) **When does `feat-forget-pin-fixes` become a pull request, and what else is unpushed?** Backend work surfaced today after three quiet days; mobile, dashboard and design are still quiet.

**The three things worth knowing:**

1. **Status shipped whole, on the server only.** Schema v0.0.58 (twelve tables), 17 consumer routes and 9 admin routes merged between 08:08 and 10:14 UTC. A status is text, a photo or a video that lives 24 hours and reaches the people the poster has written to. It is end to end encrypted with a key per status. A viewer who reports one hands that key to the server, which checks it against what it stores and keeps the status as evidence for a reviewer. That is a sound answer to moderating content the server cannot read, and stronger than the one built for chat in September. All 26 routes are in the specs as built, and the audit is clean at 183 / 85. Nothing in `beevia-mobile` or `beevia-admin` calls any of them (§3).

2. **It is live code without an operator, and it deploys on push.** The `statuses` permission is granted to no role, so no one can open or close a report. Evidence is deleted 90 days after a case closes, so a case nobody closes keeps a readable copy without limit. The review deadlines (24 and 72 hours) are as long as a status lives (24 hours), so three reporters remove a status in practice. Uploads are size-checked only when completed, and the daily limit of 30 resets when a status is deleted. None of this needs the app: the routes answer any signed-in user. The thirteen points are in `suggestions.md` §4.21, and five of them should be closed before a client exists (§3.2, §8).

3. **The MVP estimate does not move, and that is the point to discuss.** About 7,500 lines landed and the number stays at 68.36, because the rubric scores the PRD's eleven capabilities and Status is not one of them. Changing the rubric to count it would be a methodology change, and this edition does not make one. The four structural gaps (international KYC, multi-currency and FX, consent, and what is left of cards) still carry 32 of 100 points with no code in the window. The grace before the NIN requirement bites ends about 6 Dec, **13 days** from now, with the enforcement question still open. Whether anything moved on a board since Friday is not known (appendix, degraded inputs).

**If you read nothing else:** decide on the record whether Status is in the MVP, grant `statuses` to a role before anyone can file a report from an app, and open the pull request for `feat-forget-pin-fixes`.

---

## 1. Board movement

### 1.1 The boards could not be read today

**No Zoho export completed today, so this section reports the 20 Nov state and says nothing about the three days since.** Nine attempts were made between 15:01 and 15:30 UTC (appendix). The first three ran for ten minutes and were stopped with about 50 of 64 item descriptions fetched; the other six each ended in a read timeout from Zoho's API, three of them on the first data request. No file dated 23 Nov was written to `sprint-board-exports/`, to `sprint-board-exports/admin/` or to the scratch folder. The sprint-name check at 15:01 UTC did succeed: Zoho still lists `['1002', '0902', '0901', '08-01', '0702', '0701']` for Beevia and `['0901-admin']` for the admin project. **No successor to 1002 has appeared on either board.**

| Board | Items | Last known action | Read today? |
|---|---:|---|---|
| 1002 (live, scratch export) | 63 (44 leaves + 19 parents) as of 20 Nov | 11 Nov 06:53 UTC | **No.** 20 Nov export used |
| 0901-admin | 12 (8 leaves + 4 parents), all Done as of 20 Nov | 18 Nov 15:03 UTC | **No.** 20 Nov export used |
| 08-01 (the in-repo main export) | 64, all Done | 3 Sep | **No.** 20 Nov export used |
| 0902, 0901 | closed | 21 Oct, 30 Sep | not re-exported; the scratch copies from 20 Nov were reused for cycle times |

1002's board actions per day, as far as the 20 Nov sidecar goes:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12–20 Nov (to 15:02) | 20 Nov 15:02 → 23 Nov |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 | not measured |

As of 20 Nov there were no comments on 1002, `I392` showed Done with 0 of 63 ticked, and nothing had ever left REVIEW/QA on 1002. The audit's `SINCE` block compared the 19 and 20 Nov exports of 08-01 and reported no change; with no export today, it is not a comparison with today. `ZOHO_SPRINT_FILTER` still points at 08-01.

What can be said without the board: no remote branch or commit in the window names a board item, and the sprint list has no new sprint, so the code side gives no sign of board work. That is weak evidence and is not offered as a finding.

### 1.2 Eighteen days past 1002's end

1002 ended **Thursday 5 Nov**. As of 20 Nov, 36 of its 44 leaves were not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902 was swept six days after its end; 1002 is twelve days beyond that with no successor sprint in Zoho's list today. A sweep would mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** Status in all three backend repos (26 routes, twelve tables); `beevia-api` #112 and `beevia-db-schema` #36 (message edit and delete), #111, #110 and `beevia-db-schema` #35 (Forgot PIN, the PIN lock); `beevia-mobile` `feat-forget-pin-fixes`; eight open Dependabot PRs. That is a gap in the board, not a judgement on the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

From the 20 Nov export, where it was unchanged since 11 Nov. The code column was re-checked today: no client ref moved, and the backend change does not touch these routes.

| REVIEW/QA leaves (33) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | 12 | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391`, `I362` | Routes on `origin/main`. `I387` caps funding, not spending. `I391` lacks the pagination, search and filter it asks for. `I362` reports limits and does not enforce them |
| Mobile, matching merged code | 12 | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, `I386` | On `main` since #58 (10 Nov). `I390` is still unassigned |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Moved to review, no matching code | 2 | `I348`, `I372` | `I348`: the dashboard screen is mock only. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 32.2 d and 20.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part** (the wrong-PIN lock exists since #110; the biometric credential does not).
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.
- **Nothing on 1002 mentioned Status as of 20 Nov.** A search of every item name and description on this board and the admin board finds no reference to it. An item added since Friday would not be seen.

---

## 3. Code, API surface and spec drift

**Audit: 26 routes found undocumented, all added, clean on the re-run.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-23`), the first run reported 183 routes in `beevia-api` against 166 in the spec and 85 in `beevia-admin-api` against 76 (exit 1). After the spec edits it reports 183/183 and 85/85, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). The in-repo audit still reports phantom lines from the three `diverged` working trees (2 / 54 / 51). They were not acted on.

| Repo | `origin/main` | What |
|---|---|---|
| `beevia-db-schema` | `92b034b` (v0.0.58) | #37 and #38 (03:33 and 03:50 UTC): package updates, `pnpm` 11 → 12; released as v0.0.56 and v0.0.57. **#39** (08:08 UTC): migration `0056_statuses`, released as v0.0.58 one minute later |
| `beevia-api` | `8ebaf0c` | #113 (03:30 UTC): package update and a lint fix across 18 test files; no major version changed. **#115** (09:09 UTC): posting, uploads, feed, rings, views; it carries #114's commit. **#118** (10:13 UTC): viewers, mutes, reactions and replies, reports; it carries #117's commit. There is no pull ref for #116 |
| `beevia-admin-api` | `e83e86f` | #32 (03:44 UTC): package update, schema 0.0.50 → 0.0.55. **#33** (10:14 UTC): status moderation, schema 0.0.58, and a same-hour fix that makes two request bodies strict |
| `beevia-admin` | `64304ef` (30 Oct) | Unchanged. No branch besides `main`, no pull ref |
| `beevia-mobile` | `e40116d` | Unchanged since 10 Nov. `feat-forget-pin-fixes` at `d55630e`, no PR. The eight Dependabot branches and `App-bundle` unchanged |

Size, leaving out lockfiles, the Postman collection and the migration snapshot: `beevia-api` 64 files, +5,462 / −81 (2,701 added lines are tests); `beevia-admin-api` 12 files, +1,025 (293 tests); `beevia-db-schema` 12 files, +1,039 (337 tests). The feature branches on `beevia-api` that Friday's edition listed (`feat/message-edit`, `feat/voice-notes`) are gone from the remote; only `main` remains there.

### 3.1 What Status is

Read from the code; nothing was run.

- **A status** is text, a photo (5 MB) or a video (16 MB, 30 seconds) that lives exactly 24 hours. A sweep every minute deletes expired ones with their files. Thirty a day; up to five private mentions.
- **Encryption.** The phone seals the text or caption and the file with a key made for that status (AES-256-GCM), and seals that key once per viewer device through its existing chat sessions. The server stores all of it and can open none of it.
- **Audience.** Everyone who is currently in a 1:1 or group chat the poster has sent a message in, minus blocks either way and accounts that cannot sign in. It is fixed at posting, and only people the phone sealed a key for become recipients.
- **Uploads resume.** A photo or video goes up in 5 MB parts (S3 multipart), and the phone can ask which parts arrived. This is the API's first multipart upload.
- **Feed, rings and Seen by.** `GET /statuses/feed` groups by person. Every 1:1 row of the conversation list now carries a `status` block for the ring around the avatar, which changes two live operations. A view is always recorded privately; the poster sees it only while both people have Seen by and read receipts on. `statusSeenByEnabled` is a new setting.
- **Reactions and replies** are ordinary encrypted chat messages to the poster, marked with the status id.
- **Reports.** The reporter sends a reason and the status's key. The server checks the key opens the stored status, then keeps the sealed status, the key and a copy of the file. One case per status; the third different reporter hides it until review. Compliance reviews the case in the admin API, where the evidence is decrypted, and closes it as action taken or no breach. Posting can be suspended. Evidence is deleted 90 days after the case closes.

This follows the same line as chat reports (`admin-api-rfc.md` §5.1), one step further. In September a reporter could attach plaintext they typed in, which could be made up. Here the server can check the evidence against what it already holds. The cost is that, for a reported status, Beevia holds the key. The PRD's statements about moderation were written for chat, and Status is not in the PRD, so nothing on the record says whether that is acceptable (`admin-api-rfc.md` §5.1c).

### 3.2 What stands between this code and a safe launch

All from reading; `suggestions.md` §4.21 has the thirteen points with file references. The ones that matter first:

- **No role can review.** Migration 0056 adds the `statuses` permission and grants it to nobody, as happened with `help_center` and `disputes`. The seed script would grant it to Super Admin if someone ran it; no workflow does.
- **An unreviewed case keeps its evidence without limit.** Retention counts from the day a case closes. With no reviewer, nothing closes.
- **Three reports are a removal.** Review is due in 24 or 72 hours and a status lives 24, so a "no breach" decision made on time usually has nothing left to restore. Three members of any group the poster has written in are enough.
- **A deleted status cannot be reported.** The report route needs the status to still exist. A poster can delete after it has been seen.
- **The evidence key is stored as received,** next to the ciphertext, and reading evidence in the admin API leaves no log line. The KYC unmask route logs the admin id for the same kind of access.
- **The evidence file is served with a content type the poster chose,** unchecked, and neither API sends `nosniff`.
- **Upload size is enforced only at complete,** with no cap on open uploads per user and no rate limiter anywhere (`suggestions.md` §4.1).
- **The daily limit of 30 counts statuses that still exist,** so deleting resets it, and every post notifies the whole audience.

The API deploys on push, so these routes are presumably answering now, to any signed-in user, whether or not an app screen exists. Whether the deploy and migration 0056 completed is not visible from here.

### 3.3 The standing checks

- **PIN lock (#110):** `src/auth` changed only in a test file. The three gaps in `suggestions.md` §4.19 stand. No HTTP rate limiter exists.
- **`beevia-api` `release.yml`:** unchanged. `sync` still has no `needs: test` and still runs `pnpm db:migrate` on push to `main`. Migration 0056 went out through it.
- **`beevia-admin-api`** is on `beevia-db-schema` 0.0.58, the same as the consumer API. This closes the pin gap carried since 7 Nov.
- **`call.ended`** is still unhandled, and Forgot PIN on the app's `main` is still a stub (no mobile ref moved).
- **`activeNgn()`** is unchanged at three call sites in `payment.service.ts`.
- **Dependabot:** #64–#68 unchanged since 18 Nov.
- **Branch protection, PR reviews and CI results:** cannot be seen from here.

### 3.4 Document changes this cycle

- **`openapi.yaml`** (166 → 183 operations): a `Statuses` tag; 12 paths with 17 operations; 16 schemas; `status` on `Conversation`; the `contentMeta.kind` rules for reactions and replies on `SendMessageRequest`; `read_receipts_enabled` and `status_seen_by_enabled` on the chat settings, with the request no longer marking one field required.
- **`openapi.admin.yaml`** (76 → 85): a `Status Moderation` tag; 6 paths with 9 operations; 9 schemas and one parameter; `statuses` in the module list (13 → 14); the activity feed's action list brought in line with the schema (`chat_report_reviewed`, missing until today, and the five status actions) and `report` as a target type.
- **`api-rfc.md`:** totals, a Statuses row in the §3 inventory, new §5.29 and new §6.8a.
- **`admin-api-rfc.md`:** totals (85 operations, sixteen controllers), new §3.18 and new §5.1c.
- **`suggestions.md`:** new §4.21 (thirteen points) and item 17 in §8.
- `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` are unchanged: Status was never proposed.

---

## 4. Risks

Two are new today and are listed first. The rest are carried, in the order they bite.

- **New: a moderation path that accepts reports and has no reviewer.** Three reporters hide a status; no role can open the case; the evidence, which Beevia can read, is kept until someone closes it. This applies from deploy, with or without an app screen (§3.2).
- **New: the largest piece of work this month is outside the PRD, and the record does not say why.** If Status is wanted for launch, the plan and the rubric should say so. If it is not, three workstreams will be asked to build a client and a moderation screen for it ahead of FX, the international tier and consent.
- **A locked-out user has no way out on `main`.** The wrong-PIN lock has been on the API's `main` since 12 Nov and Forgot PIN on the app's `main` is still a stub. The fix is on the unmerged branch.
- **One large unreviewed branch is the only path for three user-facing fixes:** a way out of the PIN lock, offline delete, and edit. Unchanged since 17 Nov, no PR.
- **The 30-day NIN clock.** The limits are still not enforced. The grace for existing users ends about 6 Dec, **13 days from now**.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended eighteen days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **Work may still be sitting unpushed** in mobile, the dashboard and design. Backend work surfaced today after three quiet days.
- **Two production data migrations in eight days with no test gate** (0055 on 16 Nov, 0056 today). Whether either ran cleanly is not visible.
- **The PIN lock can be raced, and there is no rate limit behind it.** Unchanged since 12 Nov (`suggestions.md` §4.19). Status adds 17 more routes with no limiter in front.
- **A deleted message survives on a phone that was offline,** on `main`. The fix exists on the branch (`suggestions.md` §4.20).
- **Major dependency bumps waiting on a reviewer.** #66/#67 (ML Kit) and #68 (notifications) are unchanged.
- **Done on the admin board means "closed by the story's owner", never "reviewed".** None of its 12 items passed through REVIEW/QA. The same mechanism closed `I381` on 1002 without its code.
- **The admin dashboard has no open board item anywhere** and no commit for 24 days, while three admin items on 1002 have no assignee and nine new admin routes have no screen.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment.
- **A user can be told a person is coming when none can come.** No role holds `disputes`. `statuses` is now the third module in that state.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.

---

## 5. PRD gap

**Status moves sideways.** It closes none of the four structural gaps and is not in the PRD (a search of `Beevia_PRD.md` finds no status, stories or 24-hour post feature). The gaps still carry 32 of the rubric's 100 points: international KYC, multi-currency and FX settlement, consent management, and virtual cards beyond what is wired. `activeNgn()` is unchanged, so FX is not started.

Whether Status belongs in the MVP is the owner's call, and this report takes no side on it. What it can say is that the call is not written down anywhere it can read, and that the estimate cannot reflect work the rubric has no line for.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 16 Nov 15:25 → 23 Nov 15:25 UTC. Commit counts are non-merge commits on all remote branches in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (3 release commits on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** were recomputed from the 20 Nov exports of 0901, 0902 and 1002 and are unchanged: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3). An item entering review since Friday would change them and would not be seen.

### 6.1 Ayomikun Araoye: backend + admin API

**16 commits in 7 days**, all under `Phoenixdadhev` and all on 23 Nov between 03:04 and 10:06 UTC: 8 in `beevia-api`, 5 in `beevia-admin-api`, 3 in `beevia-db-schema`. Seven are package updates and lint fixes; nine are Status, its tests and its Postman examples. The eight merges were made under `Ayomikun Araoye`. **Board submissions and actions since Friday could not be read**; there were none between 16 Nov and the 20 Nov export. Ayomikun has **no WIP on any board**, and none of this work is a board item, so the board shows a quiet week for the person who merged the month's largest feature. That is a board gap, not a judgement.

Commit counts say little here in either direction. Sixteen commits in seven hours describe when the work was committed, not when it was done; the feature was plainly written over more than a morning.

### 6.2 David Samuel: mobile

**1 commit** in 7 days, `d55630e` on `feat-forget-pin-fixes` (17 Nov 05:51 UTC), 6.4 days ago. None in the window. **Board submissions since Friday could not be read**; there were none between 16 Nov and the 20 Nov export. The last own submission was `I286` on 14 Oct, **40.0 days** ago. A branch with no PR cannot meaningfully be moved to review, so this reads as a board gap rather than idle time. **WIP: 2 items, both with code on `main`**: `I331` at 32.2 days and `I361` at 20.3 days. This still reads as items left in the wrong column rather than stuck work; that is for David to say. Status now adds a client nobody has scoped: a Status tab, a composer with resumable upload, per-device key sealing, a viewer list and a report sheet.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** The last board action by Philip was on 2 Nov 15:58 UTC, **21.0 days** ago. The Status code refers to "the designs" (a Hidden section, a report sheet with six reasons in a set order), so designs for Status exist and are not an item on any board. Whose they are is not visible. Philip may be finished, blocked or working untracked; worth a question, not an assumption. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **24.0 days** old, and `beevia-admin` has no other branch or pull ref. **Promise has no open item on any board**, and the admin items on 1002 (`I348` in REVIEW/QA, `I349` and `I351` To do) are unassigned. Today the admin API gained nine routes with no screen, on top of the support inbox that still runs on its mock. This report does not read a quiet remote as nothing having been done, and today is the reason why; the question is what the current work is and where it is tracked.

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
| 2026-W47 (16 → 22 Nov) | — | — | **0\*** | 0\* | 0\* | 0\* | |
| 2026-W48 (23 Nov, to 15:25 UTC) | — | — | **not measured** | — | — | — | |

The 1002 rows were recomputed today. The W39–W42 rows are carried from earlier editions: 15 of 0902's leaves were removed from that sprint on 21 Oct and their history is no longer in any export.

\* W47 is complete only to Friday 20 Nov 15:02 UTC; the weekend is not covered. If nothing moved over it, W47 is the first week in this table with no transition into review. Two things would produce that even with nobody slowing down: the merged backend work has no board item to move, and the mobile work is on a branch with no PR. **Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), nobody but its submitter has accepted an item from review since `BVA-I268` on 16 Sep. **The bottleneck is the board and review process, not the developers.** Today makes the point from the other side: the week's largest delivery produced no board movement at all, because it has no item to move.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A 5,000-line feature and a one-line fix count the same.
- **Unpushed work.** A quiet remote says nothing about local work. Friday's three quiet backend days turned out to be Status.
- **Untracked work.** Status, #110–#112, #35, #36 and the whole of `feat-forget-pin-fixes` are not items on any board.
- **When work was done.** Commit timestamps record when it was committed.
- **Who moved an item is not whether it is done.** `I9` was moved by its parent's close, not by its owner.
- **Commit counts reward small commits,** and sixteen in a morning are not a measure of a week.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository. The Status commits describe unit, integration and storage tests; none was run here.

---

## 7. Previous recommendations: where they stand

| Recommendation from 20 Nov | Status on 23 Nov |
|---|---|
| **1. Push what is local, today, to a branch** | 🟡 **In part.** The backend pushed and merged Status. Nothing from mobile, the dashboard or design |
| **2. Open a PR for `feat-forget-pin-fixes`, or split it, and review it** | ❌ **No.** Non-Dependabot pull refs still end at #58; the branch is unchanged. First recommended 12 Nov, eighth edition |
| **3. Review the 24 REVIEW/QA leaves with merged code** | ❓ **Not measured.** The boards could not be read today. As of the 20 Nov export: no |
| **4. Close 1002 deliberately** | ❌ **Not done as of the sprint list today:** no successor exists, eighteen days late. Whether 1002 was swept could not be read |
| **5. Put the untracked work on the board with an owner and a design item** | ❌ **No, and the list grew** by Status: 26 routes, twelve tables |
| **6. Give the admin dashboard current work on a board, with Promise as owner** | ❌ **No admin sprint** in Zoho's list today. Assignments could not be read |
| **7. Decide whether the tier limits are enforced** | ❌ **No.** 13 days left |
| **8. Give the Dependabot queue an owner** | ❌ **Not visible.** All eight PRs still open |
| **9. Make the PIN check reserve its attempt before comparing** | ❌ **No.** `src/auth` changed only in a test file |
| **10. HTTP rate limiting on PIN, OTP and lookup routes** | ❌ **No.** Status adds 17 routes with none |
| **11. Two-device chat on a build of the branch** | ❌ **Not visible** |
| **12. Confirm migration 0055 ran cleanly in production** | ❌ **Not visible.** 0056 has now followed it through the same path |
| **13. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible** |
| **14. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No** |
| **15. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `statuses` is now a third ungranted module |
| **16. Handle `call.ended` in the app** | ❌ **No** |
| **17. NIN step and support screens on the board** | ❓ **Not measured.** The boards could not be read today. As of the 20 Nov export: no |
| **18. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **19. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **20. Record the consent behind each lookup** | ❌ **No** |
| **21. Take-over fallback metric; merchant payment disputes; the seams** | ❌ **No.** `src/support` changed by one lint comment |
| **22. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **23. Bring the dashboard onto the real contract** | ❌ **No commit in 24.0 days** |
| **24. Reopen `I380`/`I384`; narrow `I381` to the biometric credential** | ❓ **Not measured.** The boards could not be read today. As of the 20 Nov export: no |
| **25. Assign `I359` and `I390`** | ❓ **Not measured.** The boards could not be read today. As of the 20 Nov export: no |
| **26. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **27. `needs: test` on `sync`; verify jobs; admin-api onto 0.0.55** | 🟡 **In part.** `beevia-admin-api` is on 0.0.58 (#32, #33). No workflow file changed, so the three ungated paths stand |
| **28. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **No.** Today's settings correction is a case it would have caught in July |
| **29. Carried items** | ❌ **None moved** |

**Two of the 29 moved in part (1 and 27); none was met in full.** "Not visible" marks the ones that could have happened without leaving a trace in git or on a board; the rest would have.

---

## 8. What I would do this week

Three points are new and lead the list. The rest are carried from 20 Nov in the same order. Thirty-two items is too many to act on, so the first six are the ones that unblock the rest.

1. **Decide on the record whether Status is in the MVP (new).** One paragraph in the PRD or the plan: who it is for, whether it ships at launch, and where it sits against FX, the international tier and consent. If it is in, it needs board items, an owner on mobile and on the dashboard, and a line in the readiness rubric (a methodology change this report would then make and call out). If it is not, say so before a client is started.
2. **Before any app can file a report: grant `statuses` to a role and name who reviews (new).** Then close the four server points that do not need a product decision: sweep or auto-close unreviewed cases so evidence is not kept without limit; allow only image and video types on the evidence route and send `nosniff`; cap open uploads per user; count the daily limit from something deletion does not lower (`suggestions.md` §4.21, points 1, 2, 7, 8, 9).
3. **Take the Status product decisions in one sitting (new):** what three reports should do given a 24-hour life; whether a deleted status can be reported; whether storing the report key as received is acceptable; and log every evidence view (`suggestions.md` §4.21, points 3 to 6). Write the answer where `admin-api-rfc.md` §5.1c asks for it.
4. **Open a PR for `feat-forget-pin-fixes`, or split it first, and review it (carried, eighth edition).** It holds three separable pieces: Forgot PIN, the app side of #112, and forwarding, starred and voice-note work. Smaller PRs would let the PIN way-out and the offline-delete fix ship without waiting for the rest. In that review, settle the 15-minute edit window (`suggestions.md` §4.20) and ask whether the in-app Paystack WebView was a decision.
5. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
6. **Then close 1002 deliberately (carried, eighteen days late).** Move `I331` and `I361` to review if David agrees. Create the successor and carry over `I373`, anything returned, and the items from point 7. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
7. **Put the untracked work on the board with an owner and a design item (carried, larger today):** Status, the branch's three pieces, and #110–#112, #35 and #36.
8. **Push what is local to a branch, as a habit (carried).** It worked for the backend today. Unfinished work on a pushed branch can be backed up, seen and reviewed.
9. **Give the admin dashboard current work on a board, with Promise as owner (carried).** Either open an admin sprint, or assign `I348`, `I349` and `I351` on 1002 to Promise. Then agree that a child owned by someone else is not closed by its parent's close.
10. **Decide whether the tier limits are enforced, and what the end of the grace does (carried, 13 days left).** About 6 Dec is the date for existing users.
11. **Give the Dependabot queue an owner (carried).** Merge #64 and #65 after a build. Merge #66 and #67 together, after one on-device translation run. Merge #68 after a push test on a device. Close #60, #62 and #63 or merge them with the rest.
12. **Make the PIN check reserve its attempt before comparing (carried).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
13. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes, then the Status uploads and posts (carried, `suggestions.md` §4.1).**
14. **Run one two-device chat on a build of the branch (carried).** Delete a message for everyone with the other phone online, then offline, then edit one, and check both phones. Then call each new route once against the sandbox, and handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
15. **Confirm migrations 0055 and 0056 ran cleanly in production (carried, now two).**
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
30. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (carried; the schema pin half is done).
31. **Generate `openapi.yaml` from the running app and diff it in CI (carried).** It would have caught the settings fields in July.
32. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

**Not read today.** The admin board export did not complete, like the others, so this is the 20 Nov state: `0901-admin` had 12 of 12 items Done (8 leaves + 4 parents), with its last action the close of the story `BVA-I7` and its children `I8` and `I9` on 18 Nov at 15:03 UTC.

| Status | 20 Nov | 23 Nov |
|---|---:|---:|
| Leaves In progress | 0 | **not measured** |
| Leaves Done | 8 | **not measured** (8 as of 20 Nov) |
| Parents Done | 4 of 4 | **not measured** |
| Days since any activity | 2.0 | **5.0** if untouched since |

The sprint ended 22 Sep. **Zoho's sprint list, which did answer today, still shows only `0901-admin` for this project**, so the admin dashboard has no open sprint. Admin-dashboard work that is tracked at all sits on the consumer board's 1002: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only), all as of 20 Nov. Today's nine status-moderation routes have no item on this board or on 1002. `beevia-admin` last moved 24.0 days ago. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed 83 days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves, on a day when about 7,500 lines merged.** Status is not one of the eleven capabilities, which come from PRD §1.2 and §11, so it has no line to score on. Each line was checked against today's diff for an indirect effect and none was found:

- **Line 1 (E2EE messaging)** is scored on the conversations, messages, keys and attachments surface and the chat client. Status reuses the device sessions and sends reactions as chat messages, but adds nothing to chat itself. The `status` block on the conversation list is a ring for a feature with no client.
- **Line 11 (Admin oversight)** is scored on admin endpoints against the dashboard spec's eight modules and on dashboard screens. Status moderation is outside those modules and has no screen. It stays at 0.97.
- **No line goes down.** Nothing was removed, and the rubric does not discount for the gaps in §3.2.

Adding a Status line, or counting it under an existing one, would change what the number means between editions. If the owner decides Status is part of the MVP, the next edition will add the line, reweight in the open and restate earlier totals on the new basis.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No chat change. Edit client, catch-up `changes` and the voice-note recorder are still on an unmerged branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound. ML Kit bumps (#66, #67) unmerged |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | Status moderation is outside the spec's modules and has no screen |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Who asked for Status, when, and whether it is meant for launch.** No document, board item or PR description readable from here says.
- **When Status was written.** Only when it was committed.
- **Whether Status is deployed, and whether migration 0056 ran cleanly.** The workflow deploys and migrates on push; its result is not visible.
- **Whether Status works.** Nothing was run. In particular the encryption format was read from the server's checks and the Postman description, not exercised with a client.
- **Whether any role was granted `statuses`, `disputes` or `help_center` by hand,** or whether the seed script was run in production.
- **Whether the admin API has the `S3_*` settings in production**, without which reported photos and videos cannot be reviewed.
- **Whether anyone else has unpushed work, and how much.** Only remotes are visible.
- **Whether the mobile branch builds, runs, or edits and deletes correctly against the server.**
- **Whether the app builds against the Dependabot bumps**, and whether GitHub shows #59 and #61 as closed.
- **Whether the PIN lock can be raced in practice**, or whether a proxy in front of the API limits request rates.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the pull requests were reviewed or approved.** Each of today's Status PRs was merged under `Ayomikun Araoye` between 3 and 39 minutes after its last commit under `Phoenixdadhev`, which this report treats as one person (an inference, not confirmed). Whether anyone else looked is not visible.
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route, on the consent flag, on the in-app Paystack checkout, on the 15-minute edit window or on device-only stars, and whether a privacy or legal review happened**, for those or for Status reports.
- **What the design items contain,** and where the Status designs are. Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. A sprint-name check (`--sprint __nonexistent__ --dry-run` on both projects) at 15:01 UTC, which succeeded. Then the exports, **all of which failed**:

    - Three parallel background exports from 15:01 UTC (main board, step 1a; admin board with `--sprint 0901-admin`, step 1b; a scratch export of 1002). All three were stopped at this session's ten-minute background limit, having fetched about 50 of 64 descriptions. Zoho was answering slowly: an unauthenticated request to the API host took five seconds in the TLS handshake on two of three tries.
    - A 1002 export with `--no-descriptions`: uncaught `TimeoutError` (60 s read timeout) in the `--modified` sweep after about nine minutes.
    - Steps 1a and 1b again, with a 45-minute limit: `TimeoutError`, one on the item list and one in a description fetch.
    - A 1002 export with `--activity --no-descriptions` only: `TimeoutError` on the item list. One more attempt of the same at 15:25 UTC: `TimeoutError` in the audit-trail fetch, after the item list had answered.
    - A statuses-only export of 1002 (no descriptions, no audit trail, about six requests) at 15:27 UTC: `TimeoutError`.

    Nine attempts in all, each a different or smaller request than the one before; no retry loop was run beyond these. The token cache was used throughout, so the token-refresh limit was not involved. Per the skill, the most recent exports on disk (20 Nov) were used instead.

2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep. The sync's `fetch` brought in today's backend commits.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-23`: exit 1 (17 + 9 undocumented routes), then exit 0 after the spec edits. The in-repo audit also ran, for the board section (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Code reading. Every non-test file under `beevia-api/src/statuses`, `beevia-admin-api/src/statuses` and `beevia-db-schema/src/schema/statuses.ts` was read in full, with the migration, the permission guard, the admin seed, the storage adapter diff, the messaging and conversation diffs, every commit body and the Postman folder description. Test files were not read beyond their names.
5. Spec and document updates (step 4, §3.4), each applied by a script with exact-match assertions, then re-audited.
6. Board analysis (`flow23.py`, a date-shifted copy of 20 Nov's). It ran on the 20 Nov exports with today's clock, so ages are current and events after Friday 15:02 UTC are absent. It listed every action in the 7-day window up to that point (none), split submissions by actor, and computed cycle medians, WIP ages and the 1002 rows of the weekly trend.
7. Content checks. `ls-remote` of heads and `refs/pull/*` in all five repos; a `git log` of every remote ref since 20 Nov 15:00 UTC; `origin/main` and branch heads compared with the SHAs recorded in the 20 Nov edition (three backend heads moved, two client heads equal).
8. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `ls-remote`, `git archive`, and read-only `log`/`diff`/`show`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** `openapi.yaml`, `openapi.admin.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, this report, `web-report/2026-11-23.html` and `web-report/index.html`. **No board export was written today**; `sprint-board-exports/` and `sprint-board-exports/admin/` still end at 20 Nov.

**Degraded inputs.**

- **No board export for today. This is the main degraded input.** No export completed: Zoho's Sprints API was slow and then timed out (method, step 1). All board figures are the 20 Nov 15:02 UTC exports, marked with an asterisk or "not measured" where they appear. Board actions between Friday 15:02 UTC and now are unknown. The next edition should diff its sidecars against 20 Nov, not against today.
- **The export script exits with a traceback on a read timeout.** `try_get` documents status 0 for a request that never completed, but a timeout while reading the response is not caught, so one slow response ends a twelve-minute export with nothing written. Worth a fix in the script; it was not edited here.
- **The first 1002 attempt printed "cannot read epics (HTTP 0)" and blamed a missing OAuth scope.** HTTP 0 was a timeout. The scope explanation in that message is wrong, as recorded on 17 Sep.
- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.** PR numbers and merge times come from merge commits and pull refs.
- **The W39–W42 rows of the weekly trend are carried, not recomputed.** A fresh 0902 export holds 8 items; the 15 leaves removed on 21 Oct are gone from it.
- **The item-to-code mapping for the 24 REVIEW/QA leaves was carried** (backend from 11 Nov, mobile from 10 Nov). No client code changed since, and today's backend change touches none of those routes except the conversation list, which gained a field.

**Window.** 20 Nov 15:02 UTC → 23 Nov 15:25 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
