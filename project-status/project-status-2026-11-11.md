# Beevia — Project Status

**As of 2026-11-11** · Sprint **1002** (21 Oct → 5 Nov, **ended six days ago, day 22**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-11.csv` + `beevia-activity-2026-11-11.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-11.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 10 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 10 Nov 15:03 UTC → 11 Nov 15:01 UTC, 1.0 day (Tue → Wed).**

---

## Quick overview

> **Three weeks of mobile work reached `main` four minutes after Tuesday's cut-off. #58 merged whole, bringing #56 and #57 with it, and added the NIN step, limits, card management, Help & Support and the Activity contract. For the first time, 24 of 1002's 33 review items have merged code behind them. None has been accepted. Sprint 1002 is six days past its end with no successor. Overnight the backend shipped call ringing and voice-note limits, and closed a hole that let any signed-in user delete anyone's profile photo.**

| Metric | 10 Nov | 11 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 3 / 32 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | `I362` (limits endpoint) → REVIEW/QA, by its owner, 11 Nov 06:53 UTC |
| Board actions on 1002 in the window | 0 | **1** | the first in 6.6 days |
| Transitions into REVIEW/QA, last 7 days (leaves) | 8 | **3** | 3 Nov's batches rolled out of the window. 1 by the leaf's owner (`I362`), 2 by board administration on David's leaves (4 Nov) |
| Owners' last submission of their *own* leaf | 3 Nov 16:04 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **28.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 11 of 32 | **24 of 33** | +12 mobile leaves whose code reached `main` with #58; +`I362` |
| 1002 REVIEW/QA leaves whose code is only on a branch | 12 | **0** | the branch was merged and deleted |
| Routes in code but not in the spec (consumer / admin), before today's edits | 1 / 0 | **1 / 0** | now **0 / 0**: `POST /calls/{id}/ringing` added |
| API surface (consumer / admin) | 161 / 76 | **162 / 76** | +1 consumer; three contracts changed in place |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | two more merges went through it; no workflow file changed |
| `beevia-admin` days since a commit | 11.0 | **12.0** | |
| `beevia-mobile` days since a commit on `main` | 19.2 | **1.0** | `ccb4f63` → `e40116d`: 335 files, +39,770 −2,067; screen files 53 → 67 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.8 / 3.1 / 1.0 | **0.3 / 4.1 / 2.0** | 2 merges on `beevia-api` (#108, #109); none elsewhere |
| Admin board: open sprint / days since any activity | none / 57.0 | **none / 58.0** | |
| Client calls to `/kyc/nin`, `/kyc/status`, `/activity/seen`, `/cards/{id}/limits` | on `BVA-I353` only | **on `main`** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈68%** (68.36) | **+1.04**: local KYC 0.90 → 0.93, virtual cards 0.80 → 0.88 (appendix) |

**No correction to the 10 Nov edition is needed. Three of its central claims stopped being true four minutes after its 15:03 UTC cut-off:**

1. *"Nothing is merged, `main` has not moved in 19 days."* David merged #58 at 15:07 UTC on 10 Nov (`e40116d`).
2. *"Merging #58 first would take David's work with it."* That is how the stack was merged. #58 contained `BVA-I353` (#56) and the dependency and test work (#57), so all three landed in one merge. The branches `BVA-I353`, `test-coverage-2026-11-09` and `fix/ui-audit-2026-11` are gone from the remote. The 10 Nov recommendation to review #56 separately is moot.
3. *"12 of the 32 REVIEW/QA leaves have their code only on `BVA-I353`."* That code is now on `main`. The leftover `print("MARKED ACTIVITY")` the edition flagged is not on `main`.

**Landed after this edition's cut-off (15:05–15:08 UTC), noted and not analysed:** `beevia-db-schema` #35 (v0.0.54, migration 0054). It adds the `pin_reset` OTP purpose and two columns, `users.pin_failed_attempts` and `users.pin_locked_until`. Its commit message says the purpose is a "Forgot PIN" flow and a wrong-PIN lock, because "today wrong PINs are never limited, so a 4-digit PIN can be guessed by trying all 10,000". This is schema only; no `beevia-api` change uses it yet. It is the first move toward the attempt limit that `I381` was closed without. Tomorrow's edition reads it properly.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **1 own** (`I362`) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**58.0 d**) | **30** (23 `beevia-api`, 3 `beevia-admin-api`, 4 `beevia-db-schema`) | #108 and #109 (ringing, voice notes, the photo fix) are not items on any board |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | 2 (**0 own**, both moved by board administration on 4 Nov) | 0.99 d (n=36) | 2: `I331` (**20.2 d**), `I361` (8.3 d). **Both now have code on `main`** | **1** (`c04e207`) **+ the #58 merge** | His two In-progress items have merged code and are not in review. His last own submission was 28 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | Zero WIP and nothing To do for a second week. The NIN screen and five support screens are now on `main`, and none has a design item |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**58.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 12.0 days, possibly unpushed work. The consumer app's support chat is now on `main`, and the agent side of it has no screen |

**The three questions for standup:** (1) **Who reviews the 24 REVIEW/QA leaves that now have merged code, and when?** The code exists; acceptance is the only step left, and no item has left review on 1002. (2) **Should `I331` and `I361` move to review?** Both of David's In-progress items have screens on `main` since #58. (3) **What happens to 1002?** It is six days over. A sweep now would be more defensible than a week ago, but it would still mark `I348` and `I372` Done with no code behind them.

**The three things worth knowing:**

1. **The client caught up with the server on `main`, all at once.** #58 brought 14 new screen files: the NIN step and upgrade tier, the limits screen, statements, wallet details, card details, funding and management, and six Help & Support screens. It also brought the calls to `POST /kyc/nin`, `GET /kyc/status`, `GET /wallets/limits`, `POST /activity/seen` and `GET`/`PATCH /cards/{id}/limits`. Card history now parses the server's `data.items` and `in`/`out`, a mismatch the 4 Nov edition found. Still open: `verify_nin.dart` does not match `nin_not_found`, `bvn_required` or `verification_unavailable` by name, and there is no sign that any route was called from a real build (§3.3).

2. **Until #108 at 07:18 UTC today, any signed-in user could delete any other user's profile or group photo.** `DELETE /upload` checked only the key's format, and public photo URLs carry the key. Uploads now record their uploader, and deleting someone else's file returns `403 upload_not_yours`. Whether the hole was used cannot be told from here. Files uploaded before today are now undeletable through that route, including by their owners (§3.1).

3. **The board moved once, and the review queue still does not drain.** `I362` went to review 4.7 days after its code merged. 24 of 33 REVIEW/QA leaves now have merged code, and nothing has left review on 1002. Output reached `main`; acceptance stays at zero. The bottleneck is the review step, not the developers (§1.2, §2).

**If you read nothing else:** spend this week's review time on the 24 items whose code is on `main`. Accept or return each one before anyone sweeps 1002.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 10 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. At about 15:05 UTC Zoho listed the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`) and only `0901-admin` for the admin project. **No successor to 1002 exists.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **One action in the window:** at 06:53 UTC on 11 Nov, Ayomikun moved `I362` (*Limits & Usage Endpoint*) from In progress to REVIEW/QA. It is his own leaf, and its code had been merged and working since 6 Nov 15:08 UTC. No other status change, no owner change, no comment and no new item. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5 Nov | 6 Nov | 7–8 Nov | 9 Nov | 10 Nov | 11 Nov (to 15:01) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | 0 | 0 | 0 | 0 | **1** |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 Six days past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`, *Reflect card spending in the app*). The one precedent is 0902, which was swept on 21 Oct, six days past its end. That sweep marked 7 REVIEW/QA leaves Done and removed 15 leaves to a destination the export cannot see. 1002 is now at the same point. The difference from a week ago is that most of the review queue now has merged code (§2). A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** #108 (call ringing; photo removal and the upload ownership fix) and #109 (voice notes); the NIN screen and upgrade-tier screen; the test-coverage and UI-audit work inside #58; Dependabot PRs #59–#63. This is a limit of the board, not a finding about the work.

---

## 2. Sprint 1002: what is in review, and whether the code exists

| REVIEW/QA leaves (33) | Count | Items | Evidence |
|---|---:|---|---|
| Backend, matching merged code | **12** (was 11) | `I366`, `I335`, `I338`, `I341`, `I332`, `I344`, `I347`, `I350`, `I352`, `I387`, `I391`, **`I362`** | Routes on `origin/main`. `I387` caps funding, not spending. `I391` lacks the pagination, search and filter it asks for. `I362` is the limits route, which reports limits and does not enforce them |
| Mobile, matching merged code | **12** (was 0) | `I334`, `I337`, `I340`, `I343`, `I346`, `I354`, `I357`, `I365`, `I369`, `I376`, `I390`, `I386` | On `main` since #58. The item-to-code mapping is the 10 Nov edition's, made on the branch; the branch merged unchanged into `main`. `I390` is still unassigned |
| Backend, already existed or no identifiable change | 3 | `I370`, `I377`, `I358` | Unchanged |
| Moved to review, no matching code | 2 | `I348`, `I372` | `I348`: the dashboard screen is mock only. `I372`: no code, and not buildable as written |
| Design | 4 | `I364`, `I368`, `I375`, `I389` | Design files are not in git |

- **In progress, with merged code:** `I331` (Help & Support home: `help_support_screen.dart` on `main`) and `I361` (limits screen: `transaction_limits_screen.dart`, reading the shipped shape). WIP ages 20.2 d and 8.3 d.
- **Done without matching merged code:** `I380`, `I381` (no attempt limit or lockout on `POST /auth/step-up`, no reopen) and `I384`. **`I383` (card details screen) is no longer on this list**: `card_details_screen.dart` reached `main` with #58.
- **Stories out of step with their children:** `I371` is To do with `I372` in review. `BVA-I349` (Support Inbox) is To do and unassigned with `I350` in review. `BVA-I351` (FAQ CMS) is To do and unassigned with `I352` in review. `I359` (*Transaction Limits & Tier*) is To do and unassigned, with `I360` Done and `I362` now in review. Unchanged apart from `I362`.
- **`I373`** (*Reflect card spending in the app*) is To do. The card history on `main` reads `GET /cards/{id}/activity`, including `spend_included`, which shows spending when the provider returns it. Whether that meets the item is the owner's call.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edit.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-11`), it first reported one consumer route undocumented (`POST /calls/{id}/ringing`), exit 1. After the spec edit it reported 162/162 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). The in-repo audit still reports phantom lines from the three `diverged` working trees. They were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `b836f6b` → `5aa03d8` | #108: photo removal, upload ownership, `call.ringing`. #109: voice-note limits |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged |
| `beevia-db-schema` `main` | `01f677c` (v0.0.53) | Unchanged at the cut-off. **#35 (v0.0.54, PIN reset and a wrong-PIN lock, schema only) merged at 15:05 UTC, after it** |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `ccb4f63` → **`e40116d`** | #58 merged (10 Nov 15:07 UTC), carrying `BVA-I353`, the test-coverage work and the UI audit. Synced by fast-forward, no branch switch |

### 3.1 Ringing, voice notes and the photo fix (`beevia-api` #108, #109)

- **The upload hole (#108, merged 11 Nov 07:18 UTC).** The commit message describes it: `DELETE /upload` "checked only the key's format, not who uploaded it. Public URLs carry the key, so any signed-in user could delete anyone's profile or group photo." Each upload now records its uploader in object metadata (no schema change). Deleting someone else's file returns `403 upload_not_yours`; a key with no file returns `404 upload_not_found`. **Files uploaded before this merge carry no uploader, so nobody can delete them through this route, including their owners.** Whether the hole was used before today cannot be seen from here.
- **Removing a profile photo (#108).** `PATCH /users/me` takes `avatarUrl: null`, which used to fail validation. When a photo is removed or replaced, the old file is deleted from storage if the user uploaded it and no other profile or group still shows it. Account deletion does the same.
- **`POST /calls/{id}/ringing` and the `call.ringing` socket command (#108).** The callee's app reports that it is showing the incoming call. While the call is still `ringing`, the caller's devices get `call.ringing` `{ call_id, conversation_id, user_id, at }`. A late report tells nobody and returns the call's current status. Nothing is stored. **The app on `main` neither sends it nor handles the event.**
- **Voice notes (#109, merged 07:53 UTC).** A `type: audio` message now needs exactly one `audio/*` attachment of at most 10 MB and a whole-millisecond `contentMeta.durationMs` up to 10 minutes; each failure is a distinct `400`. An offline recipient's push reads "🎤 Voice message". **This does not break the app on `main`**: no send path chooses `type: audio`, and there is no recorder. A recorder will have to send `durationMs`.
- **Not touched, and still true.** The tier limits are applied nowhere; `KYC_RESET_ENABLED` has no startup check; `kyc_holds`, Tier 3 and an admin route for the limits have no code; `isSubjectConsent` is a constant; `GET /cards/{id}/transactions` is in kobo, though the app now reads card history from `/activity` instead.

### 3.2 What the change leaves open

- **Photos uploaded before today are undeletable through the API.** A one-off backfill of the uploader from `avatar_url` and the group photo columns would fix it (`suggestions.md` §4.18 item 4).
- **Check whether the photo hole was used.** If storage access logs exist, look for `DELETE` calls on `public/image/*` keys that someone else uploaded.
- **`call.ringing` and `call.ended` both lack a client.** They are a natural pair.
- **The dashboard has no screen for take-over, the article list, the unread counts, the hours or the card-limit default**, and no role holds `disputes`. Unchanged. The consumer side of support chat is now on `main`, so the missing agent side matters more.
- **`beevia-admin-api` pins `beevia-db-schema` 0.0.50**, while the consumer API is on 0.0.53. Unchanged.

### 3.3 The app against the contract, now on `main`

`origin/main` at `e40116d` was read for each call the 10 Nov edition checked on the branch. **Read, not run.**

| Contract | On `main` (11 Nov) |
|---|---|
| `POST /kyc/nin`, returning the KYC status | `verify_nin.dart`, `KycService.verifyNin`. Handles `too_many_attempts`, `nin_mismatch` and `nin_already_used` by name. **`nin_not_found`, `bvn_required` and `verification_unavailable` still are not**; only the mock server returns them by name |
| `GET /kyc/status` and `grace_until` | `KycStatus`; `NinBanner` on Home and Wallet |
| `GET /wallets/limits` | `WalletLimits` reads the shipped shape; `transaction_limits_screen.dart` |
| `POST /activity/seen` | Called on opening and on leaving the tab. The debug `print` is gone |
| `GET` / `PATCH /cards/{cardId}/limits` | `CardLimitsForm`, `wallet_provider.fetchCardLimits` / `updateCardLimits` |
| Card history | `GET /cards/{id}/activity`. **Parses `data.items` and `direction` `in`/`out`**, which fixes the mismatch noted on 4 Nov |
| Help & Support, disputes, support chat | Six screens under `lib/features/support`; support chat over the `support.*` socket commands. The "I didn't make this transaction" reason is sent as `didnt_make_this_transaction`, which is the server's value, so the 29 Oct mismatch is gone |
| `call.ended` push, `call.ringing` | Not handled |
| Biometric option in Chat Send | Still present (`chat_send_money_flow.dart`) |

**One caution stands.** #58's mock server answers the new routes, so the tests and Maestro flows it reports exercise those mocks, not the API. The project's own check from 9 Nov (call each new route once from a real build) is still not shown to have happened.

### 3.4 The standing checks

- **`beevia-api` `release.yml`**: read in full. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. It deploys and runs `pnpm db:migrate` on push to `main`. No workflow file changed in `b836f6b..5aa03d8`. #108 and #109 went through the ungated path. `postman-sync` re-uploads the collection, which both merges edited.
- **`beevia-mobile` CI**: #58 changed `.github/workflows` (`c0f590f`, `783078d`, secrets for the reusable Flutter workflow). Whether Flutter CI is a required check cannot be seen.
- **Branch protection, PR reviews and CI results**: cannot be seen from here. Dependabot opened #59–#63 on `beevia-mobile` at 03:54–03:56 UTC today.

### 3.5 Document changes this cycle

`openapi.yaml`: added `POST /calls/{id}/ringing` (`reportCallRinging`, `200` call, `400 own_call`, `404`). `avatarUrl` is now nullable in `UpdateMeRequest`, and `updateMe` documents removal. `deleteUpload` gains `403 upload_not_yours` and `404 upload_not_found`. `sendMessage` documents the voice-note rules. `openapi.admin.yaml`, `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` are unchanged. `api-rfc.md`: 161 → 162, the Calls row 5 → 6, two inventory rows, and a new §5.25. `admin-api-rfc.md`: unchanged. `suggestions.md`: new §4.18.

---

## 4. Risks

- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves now have merged code. If review does not start, the next sweep will mark them Done without anyone having looked, as on 21 Oct.
- **The photo-deletion hole was open until this morning.** It is closed, its use cannot be checked from here, and old photos are now undeletable through the API.
- **A 335-file merge went to `main` in one step.** It has been merged. What remains is that nothing about it was run here, and its tests run against the app's own mock server.
- **1002 ended six days ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment. Unchanged.
- **The 30-day NIN clock.** The client that can send a NIN is now on `main`. Whether it has shipped to users is not visible, and the limits are still not enforced, so the deadline still has no effect.
- **Every backend repo still deploys or migrates production on push without a test gate.** Two more merges used it.
- **A user can be told a person is coming when none can come.** No role holds `disputes`, and the consumer support chat is now on `main`. Unchanged on the server side.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged.
- **Done and REVIEW/QA hide open work.** `I381`'s lockout does not exist. `I372` is in review with no code.
- Carried, unchanged: `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** 10 Nov's "the client the contract needs is unmerged" and "two reviews in sequence". The stack merged as one.

---

## 5. PRD gap

The four structural gaps are unchanged and carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. #58 moves two lines that were waiting on the client: the local KYC tier, whose NIN step is now on `main`, and virtual cards, whose management screens are now on `main`. It does not touch the four gaps. `activeNgn()` is unchanged, so every new wallet screen is NGN only. Voice notes and call ringing are refinements to lines 1 and 2, with no client yet.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 4 Nov 15:01 → 11 Nov 15:01 UTC. Commit counts are non-merge commits on all remote refs in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (4 on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times:** Ayomikun's rose from 1.44 d to 1.48 d (n=21 → 22), because `I362` took 6.6 days from In progress to review. David's (0.99 d, n=36) and Philip's (0.89 d, n=3) are unchanged.

### 6.1 Ayomikun Araoye: backend + admin API

**30 commits in 7 days**: 23 in `beevia-api`, 3 in `beevia-admin-api` and 4 in `beevia-db-schema`. **One own submission**, `I362`, 6.6 days after it started and 4.7 days after its code merged. **No WIP on 1002.** Since the last cut-off: #108 and #109, neither an item, including the fix for the upload hole. The last commit is 0.3 d old. `I381` remains Done with no lockout. `BVA-I8` has been In progress on the closed admin board for 58.0 days.

### 6.2 David Samuel: mobile

**1 non-merge commit** in 7 days (`c04e207`, 9 Nov), and **the merge of #58 into `main`** (10 Nov 15:07 UTC). It is the first change to `main` since 21 Oct, and it carried ten of his commits. **Zero own submissions**: the last was `I286` on 14 Oct, **28.0 days** ago. Both of his 7-day "submissions" were board administration's, on 4 Nov. **WIP: 2 items, both with code on `main`**: `I331` at 20.2 days (20 times his median of 0.99 d) and `I361` at 8.3 days. This reads as an item left in the wrong column rather than stuck work, but that is for him to say. One leaf is To do (`I373`).

### 6.3 Philip Chidera: design

**No 7-day submission**, since 3 Nov's move of `I389` has rolled out of the window. **Zero WIP and no leaf left To do for a second week**: finished, blocked or working untracked. Worth a question, not an assumption. Fourteen new screen files reached `main`. The NIN step and the support screens have no design item on the board. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is now 12.0 days old. The consumer support chat reached `main` today, while the dashboard's inbox still runs on its mock and the server's take-over, hours, unread counts and card-limit default have no screen. Nothing has been pushed in response. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee, and `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 58.0 days.

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
| 2026-W46 (9 Nov → 11 Nov 15:01 UTC) | — | — | **1** | 1 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by anyone other than its submitter since `BVA-I268` on 16 Sep. Output has stayed steady and has now reached `main` too, while acceptance has stayed at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A migration, a 335-file merge and a one-line fix all count the same.
- **Who moved an item is not whether it is done.** Two of the three 7-day moves into review were made by board administration, not the owner.
- **Untracked work.** #108, #109, the NIN screen and the UI-audit and test work in #58 are not items on any board.
- **Commit counts reward small commits.** David's 7-day count is 1. The merge he made on 10 Nov carried ten of his commits and three weeks of work.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository. #58's commit messages report coverage of 46.0% and passing Maestro flows; #109's reports an end-to-end voice-note test. Those figures were read, not checked.

---

## 7. Previous recommendations: where they stand

| Recommendation from 10 Nov | Status on 11 Nov |
|---|---|
| **1. Close 1002 now, deliberately** | ❌ **Not done, six days late.** One owner move (`I362`); no successor, no sweep, filter still 08-01 |
| **2. Settle the order of #56, #57, #58** | ➖ **Overtaken.** #58 was merged whole at 15:07 UTC on 10 Nov, bringing the other two with it |
| **3. Call each new route from a real build; handle three NIN errors; remove the debug `print`** | 🟡 **The `print` is gone.** The three errors are still not matched by name; no real-build check is visible |
| **4. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No.** `env.ts` changed today for voice notes only |
| **5. NIN step on the board; move `I361` and `I362` to review** | 🟡 **`I362` moved.** `I361` is still In progress with code on `main`; no NIN item or design |
| **6. Decide whether the tier limits are enforced** | ❌ **No** |
| **7. Decide the seeded card default** | ❌ **Not visible** |
| **8. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **9. Decide what a card limit is** | ❌ **No.** The merged form edits funding caps |
| **10. Record the consent behind each lookup** | ❌ **No** |
| **11. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** More pressing now the consumer support chat is on `main` |
| **12. A log line or metric on the take-over fallback** | ❌ **No** |
| **13. Let a merchant payment be disputed; correct the assistant's text** | ❌ **No** |
| **14. Fix the seams** | ❌ **No** |
| **15. Run one real chat and one real dispute through the assistant** | ❌ **Not visible** |
| **16. Decide the assistant on the record** | ❌ **Not visible** |
| **17. Bring the dashboard onto the real contract** | ❌ **No commit in 12.0 days** |
| **18. Reopen `I380`, `I381`, `I383`, `I384`; add an attempt limit** | 🟡 **`I383` now has its code on `main`.** The other three are unchanged. No attempt limit in the API; the schema for a wrong-PIN lock landed just after the cut-off |
| **19. Agree how parent status moves work** | ❌ **No** |
| **20. Assign `I348`, `I349`, `I351`, `I359`, `I390`; give the dashboard a sprint** | ❌ **No** |
| **21. Convert `GET /cards/{id}/transactions` to naira, or retire it** | 🟡 **The app now uses `/activity` for card history.** The kobo route has no caller and still exists |
| **22. `needs: test` on `sync`; verify jobs elsewhere** | ❌ **Not done.** Two more merges went through the ungated path |
| **23. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** One more route was added by hand today |
| **24. Carried items** | ❌ **None moved.** `call.ended` is still unhandled on `main` |

**None of the 24 is fully met. One was overtaken, and four moved in part.** Most of the movement came from the #58 merge rather than from acting on a recommendation.

---

## 8. What I would do this week

1. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (new, replaces "settle the merge order").** Start with the 12 mobile leaves, which have never been looked at against the API. Return `I348` and `I372`, which have no code.
2. **Then close 1002 deliberately (carried, six days late).** Move `I331` and `I361` to review if David agrees they are done. Create the successor sprint, carry `I373` and anything returned, do not sweep, and set `ZOHO_SPRINT_FILTER`.
3. **Call each new route once from a real build against the sandbox (carried, now against `main`).** `POST /kyc/nin`, `GET /kyc/status`, `GET /wallets/limits`, `POST /activity/seen`, `PATCH /cards/{id}/limits`, plus one support chat. Handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
4. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (new).** `suggestions.md` §4.18 items 4–5.
5. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).** Same fix as `OTP_ECHO` (§1.2).
6. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried, now urgent).** The consumer support chat is on `main`.
7. **Send `call.ringing` from the app and handle `call.ended` (new, pairs with a carried item).**
8. **Put the NIN step and the support screens on the board with a design and an owner (carried).** The code exists, so these are review items, not build items.
9. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
10. **Decide the seeded card default and what a card limit is, on the record (carried).** Rewrite `I371`, `I372`, `I385` and `I387` to say "funding cap", or ask the provider about card product configuration.
11. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
12. **Record the consent behind each BVN and NIN lookup (carried).**
13. **Put a log line or metric on the take-over fallback (carried).**
14. **Let a merchant payment be disputed, and correct the assistant's text (carried).**
15. **Fix the seams (carried):** the inbox's transaction type and `or`, the payment lookup, `unreadOnly` before paging, the `timezone` check, the article list's `search` locale and `meta.total`.
16. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
17. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
18. **Reopen `I380`, `I381` and `I384` if those closes were not meant for them (carried)**, and add an attempt limit to `/auth/step-up`.
19. **Agree how parent status moves work, and have board administration move nothing to review without the owner (carried).**
20. **Assign `I348`, `I349`, `I351`, `I359` and `I390`, and give the admin dashboard a sprint (carried).**
21. **Retire `GET /cards/{id}/transactions` now that the app reads `/activity` (carried, narrowed).**
22. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto the current `beevia-db-schema` (carried).
23. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
24. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 58.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 58 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). The consumer half of support chat reached `main` today, and the agent half still has no real screen. `beevia-admin` last moved 12.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, +1.04)

**Target 2026-09-01 (provisional). The target date passed seventy-one days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**Two lines move, both on code that reached `main` in #58 (`e40116d`).**

- **Line 4 (local KYC): 0.90 → 0.93.** Evidence: `verify_nin.dart`, `KycService.verifyNin`, the `KycStatus` model, `NinBanner` and `upgrade_tier_screen.dart` are on `main` and call `POST /kyc/nin` and `GET /kyc/status`. The 10 Nov edition named this as the first line to reconsider once the branch merged. It stops short of 1.0 because Tier 3 and the parked-funds mechanism have no code, the limits are not enforced, and three server errors are not handled by name.
- **Line 9 (virtual cards): 0.80 → 0.88.** Evidence: `card_details_screen.dart`, `card_fund_screen.dart`, `manage_card_screen.dart` and `CardLimitsForm` are on `main`. They call reveal, funding, `GET`/`PATCH /cards/{id}/limits` and `/cards/{id}/activity`, and card history now parses the server's `data.items` and `in`/`out`. Those calls were the condition the score was held on. It stops short because the verification model is undecided and limits cap funding, not spending (the provider's constraint).

**Considered and held.** **Line 6 (multi-currency wallets) holds at 0.85.** The limits, statement and wallet-details screens are now on `main`, but every one is NGN only and `activeNgn()` is unchanged; the line's ceiling is the missing second currency, not the screens. **Line 7 (send/request/receive) holds at 0.92:** the biometric option is still in Chat Send. **Line 2 (calling) holds at 0.92:** `call.ringing` is server-only and `call.ended` is still unhandled. **Line 1 (E2EE) holds at 0.90:** voice-note limits are server-side and the app has no recorder. **Line 11 (admin oversight) holds at 0.97:** no admin code changed, and the consumer support chat does not count toward it.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Chat surface unchanged; voice-note validation on the server, no recorder in the app; support threads are a separate, plaintext carve-out |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `POST /calls/{id}/ringing` added on the server; neither it nor `call.ended` is handled on `main` |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound |
| 4 | Local KYC tier (BVN) | 8 | **0.93** | **+0.03** | NIN step, status and deadline banner on `main` (#58), wired to `/kyc/nin` and `/kyc/status`. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged. Limits, statement and wallet-details screens on `main`, all NGN |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | **0.88** | **+0.08** | Card details, funding, reveal, limits and activity wired on `main` (#58). Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item. The lookups assert consent as a constant |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed; no role holds `disputes`; the screens still run on a mock |
| | **Weighted total** | **100** | **68.36** | **+1.04** | **≈68%** |

### What this report cannot tell you

- **Whether any of the merged client screens work against the API.** Nothing was executed, and #58's tests run against its own mock server.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the photo-deletion hole was used before #108.**
- **Whether #108 and #109 are live, and where.** Merge times and the workflow are known; results and the target host are not.
- **Whether the pull requests were reviewed or approved**, or who approved #58. The merge commit names David as the merger.
- **Whether `KYC_RESET_ENABLED` or `KYC_TEST_IDS_ENABLED` is on anywhere.**
- **Whether migrations 0051–0053 have run**, and when, which decides the date the grace ends.
- **Whether the seeded card default was a decision**, and whether the assistant runs at all in production.
- **Who decided on the assistant, on funding caps, on the NIN timing, on the reset route or on the consent flag, and whether a privacy or legal review happened.**
- **Whether any role was granted `disputes` or `help_center` by hand.**
- **Whether closing or moving a parent was meant to carry its children.** Same-millisecond timing is inference.
- **What the design items contain.** Design files are not in git.
- **Where 0902's 15 leaves went**, or what will happen to 1002's open items.
- **Whether branch protection requires CI on any `main`.**
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Three background exports starting at about 15:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 10 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, one new action. Sprint lists came from the `__nonexistent__` dry run for both projects: Beevia `['1002', '0902', '0901', '08-01', '0702', '0701']`, admin `['0901-admin']`. 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. **`beevia-mobile` fast-forwarded 19 commits (`ccb4f63` → `e40116d`) on `main`, with no branch switch.** `beevia-admin` was already current. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-11`: exit 1 before the spec edit, exit 0 after. The in-repo audit also ran, for the board section; it produced phantom lines only. Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow11.py`, adapted from 10 Nov's). It diffed 1002 against 10 Nov, listed every action in the window, split 7-day submissions by actor, and computed WIP ages and the weekly trend. It also searched every sidecar for any transition out of REVIEW/QA.
5. Content checks. `git fetch` (by the sync) and `ls-remote` of heads and `refs/pull/*`. In `beevia-api`: the #108 and #109 commit messages and diffs (calls controller and service, gateway, users DTO and controller, upload controller and service, voice-note validator, env). In `beevia-mobile` at `origin/main`: the screen inventory before and after #58, and greps for each contract route. Also the NIN error handling, the card history parser, the card service paths, the dispute reason values, the biometric option, `call.ended`/`call.ringing`, and the send path for `type: audio`. `release.yml` read in full.
6. Spec and narrative updates (§3.5).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity (8 on `beevia-mobile` in the window: 7 inside #58 and 1 on `App-bundle`) are reported as facts about the merge, not as a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`. Nothing was committed, pushed or deployed. A final `fetch` at 15:09 UTC found `beevia-db-schema` #35 (noted in the overview) and no other repo moved; a fast 1002 re-export at the same time found no board action after 06:53 UTC.

**Files changed this cycle:** this report, `web-report/2026-11-11.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md` and `suggestions.md`. New board exports for 11 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov**, when it was made on `BVA-I353`. It was not re-derived item by item today. The branch merged into `main` unchanged, and the files it named are present there.

**Window.** 10 Nov 15:03 UTC → 11 Nov 15:01 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (−07:00).
