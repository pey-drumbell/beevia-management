# Beevia — Project Status

**As of 2026-11-12** · Sprint **1002** (21 Oct → 5 Nov, **ended seven days ago, day 23**): **63 items, 44 leaves: 1 To do · 2 In progress · 33 REVIEW/QA · 0 BLOCKED · 8 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-11-12.csv` + `beevia-activity-2026-11-12.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-11-12.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 11 Nov file in the same folder. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`. Commit messages were read as the authors' own account, and none of their claims about tests, production or live environments could be checked.

Scope: five boards, kept separate and never summed. **Window: 11 Nov 15:01 UTC → 12 Nov 15:04 UTC, 1.0 day (Wed → Thu).**

---

## Quick overview

> **Wrong PINs are now limited. Until #110 merged at 10:38 UTC today, nothing stopped a signed-in session from trying all 10,000 PINs on the step-up that moves money. Five wrong PINs now lock PIN entry for 30 minutes, and a three-step Forgot PIN exists. The lock has a gap: requests sent together are all checked before it lands. The app on `main` still says "coming soon" on Forgot PIN; David pushed the client to a new branch this morning. The board did not move at all. 1002 is a week past its end, and none of its 33 review items has been accepted.**

| Metric | 11 Nov | 12 Nov | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 63 (44+19) | **63 (44+19)** | none added or removed |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 1 / 2 / 33 / 0 / 8 | **1 / 2 / 33 / 0 / 8** | no change |
| Board actions on 1002 in the window | 1 | **0** | sidecar byte-identical to 11 Nov; last action 11 Nov 06:53 UTC |
| Transitions into REVIEW/QA, last 7 days (leaves) | 3 | **1** | 4 Nov's two board-administration moves rolled out of the window. The one left is `I362`, by its owner |
| Owners' last submission of their *own* leaf | 11 Nov 06:53 UTC | **11 Nov 06:53 UTC** (Ayomikun, `I362`) | David's last own submission is still 14 Oct, **29.0 days** ago |
| Items that left REVIEW/QA on 1002, ever | 0 | **0** | checked in the sidecar |
| 1002 REVIEW/QA leaves with matching **merged** code | 24 of 33 | **24 of 33** | |
| Routes in code but not in the spec (consumer / admin), before today's edits | 1 / 0 | **3 / 0** | now **0 / 0**: the three Forgot PIN routes added |
| API surface (consumer / admin) | 162 / 76 | **165 / 76** | +3 consumer; four contracts changed in place |
| Proposed operations (consumer / admin) | 32 / 18 | **32 / 18** | none |
| Limit on wrong PINs at `/auth/pin/verify` and `/auth/step-up` | none | **5, then a 30-minute lock** | `beevia-api` #110 on `beevia-db-schema` #35. Parallel requests get past it (§3.2) |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #110 and migration 0054 went through it; no workflow file changed |
| `beevia-admin` days since a commit | 12.0 | **13.0** | |
| `beevia-mobile` days since a commit on `main` / on any branch | 1.0 / 1.0 | **2.0 / 0.3** | new branch `feat-forget-pin-fixes`, 2 commits, 88 files, not merged, no PR |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.3 / 4.1 / 2.0 | **0.2 / 5.1 / 1.0** | #110 on `beevia-api`; #35 (v0.0.54) on `beevia-db-schema` |
| Admin board: open sprint / days since any activity | none / 58.0 | **none / 59.0** | |
| Estimation points set (1002) | 0/63 | **0/63** | |
| MVP readiness (estimate) | ≈68% (68.36) | **≈68%** (68.36) | **no change**: everything new is on the server or on an unmerged branch (appendix) |

**No correction to the 11 Nov edition is needed.** Two of its statements were true at its cut-off and are now out of date. *"No attempt limit in the API"* (recommendation 18): `beevia-api` #110 added one this morning. *"This is schema only; no `beevia-api` change uses it yet"* (about `beevia-db-schema` #35): #110 is that change.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (16 REVIEW/QA, 2 Done) · `I392` shared · 0901-admin: 1 In progress | **1 own** (`I362`) | 1.48 d (n=22) | none on 1002 · `BVA-I8` on 0901-admin (**59.0 d**) | **20** (15 `beevia-api`, 1 `beevia-admin-api`, 4 `beevia-db-schema`) | Forgot PIN and the PIN lock (#35, #110) are not items on any board. They are the attempt limit `I381` was closed without |
| David Samuel | mobile | **1002: 16** (1 To do, 2 In progress, 11 REVIEW/QA, 2 Done) · `I392` shared | **0** | 0.99 d (n=36) | 2: `I331` (**21.2 d**), `I361` (9.3 d). Both have code on `main` | **3** (`c04e207`, `36b03ff`, `3e23414`) | New branch with the client for Forgot PIN, ringing and voice notes, not on the board. Last own submission 29 days ago |
| Philip Chidera | design | **1002: 7** (4 REVIEW/QA, 3 Done) · `I392` shared (Done) | 0 | 0.89 d (n=3) | none | n/a | No board action in 10.0 days. Forgot PIN now has a screen on a branch and no design item |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**59.0 d**) | **0** (`beevia-admin`, last 30 Oct) | No commit in 13.0 days; possibly unpushed work |

**The three questions for standup:** (1) **Who reviews the 24 REVIEW/QA leaves with merged code, and when?** A second day has passed with no board action at all. (2) **Can the PIN check reserve the attempt before comparing the PIN?** It is a small change and it closes the parallel-request gap (§3.2). (3) **When does `feat-forget-pin-fixes` get a PR?** Until it merges, a user who trips the new lock has no way out but to wait 30 minutes.

**The three things worth knowing:**

1. **The step-up PIN finally has an attempt limit, and it can be raced.** Every PIN check (`/auth/pin/verify`, `/auth/step-up`, `currentPin` on `/auth/pin`) shares one count of wrong PINs; the fifth locks PIN entry for 30 minutes with `403 pin_locked`. The counter is atomic, but the lock is checked against the user row read before the PIN is compared. A burst of requests from one session is therefore compared in full before the first lock lands, and the API has no rate limit. Separately, locking resets the count, so a patient guesser gets 5 tries every 30 minutes indefinitely: all 10,000 PINs in about 42 days. Read, not run (§3.2).

2. **Forgot PIN exists on the server, and on a branch in the app.** `POST /auth/pin/reset/request` → `/verify` → `/auth/pin/reset`: an SMS code, a 5-minute reset token, a new PIN, and a "Your PIN was changed" push. On `main` the app's "Forgot PIN?" still shows "coming soon". `feat-forget-pin-fixes` (pushed 06:49 UTC) calls all three routes and handles `pin_locked`, `attempts_remaining` and `pin_reset_invalid`. It also sends `call.ringing`, records voice notes with `durationMs`, and moves Paystack checkout into the app. That is the client for #108, #109 and #110, three days after they shipped (§3.3).

3. **The board stood still for a full day, a week after 1002 ended.** Zero actions on any board. 24 of 33 REVIEW/QA leaves have merged code, and nothing has ever left review on 1002. The bottleneck is still the review step, not the developers (§1, §2).

**If you read nothing else:** make the PIN check reserve its attempt before it compares (§3.2), get `feat-forget-pin-fixes` into review, and spend this week's review time on the 24 items whose code is on `main`.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars are byte-identical to 11 Nov. The audit's `SINCE` block compares two 08-01 exports and correctly reports no change. 0901 and 0902 were not re-exported, because they are closed; the 19 and 27 Oct copies feed the cycle times. `ZOHO_SPRINT_FILTER` still points at 08-01. At 15:00 UTC Zoho listed the same six Beevia sprints (`1002`, `0902`, `0901`, `08-01`, `0702`, `0701`). The admin export found only `0901-admin`. **No successor to 1002 exists.**

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, unchanged. **No action in the window.** The 1002 sidecar is byte-identical to 11 Nov; the CSV differs only in its export-date line. 1002's board actions per day:

| 27 Oct | 28 Oct | 29 Oct | 30 Oct | 31 Oct–1 Nov | 2 Nov | 3 Nov | 4 Nov | 5–10 Nov | 11 Nov | 12 Nov (to 15:04) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 16 | 6 | 6 | 0 | 5 | **23** | **4** | 0 | **1** | 0 |

**There are no comments on 1002, ever.** `I392` still shows Done with 0 of 63 ticked. **Nothing has ever left REVIEW/QA on 1002**, and no sidecar on any board shows a transition out of review since the 21 Oct sweep.

### 1.3 A week past 1002's end

1002 ended **Thursday 5 Nov**. 36 of its 44 leaves are not Done: 33 in REVIEW/QA, 2 In progress (`I331`, `I361`) and 1 To do (`I373`). 0902, the one precedent, was swept six days after its end. 1002 has now gone a day longer with no sweep and no successor. A sweep would still mark `I348` (mock only) and `I372` (no code, not buildable as written) Done, and it would say nothing about review.

**Work that is not on the board:** `beevia-db-schema` #35 and `beevia-api` #110 (Forgot PIN, the PIN lock, attempts left on codes); `beevia-mobile` `feat-forget-pin-fixes` (the client for #108–#110 and in-app Paystack checkout); Dependabot PRs #59–#63. This is a limit of the board, not a finding about the work.

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

- **In progress, with merged code:** `I331` (Help & Support home) and `I361` (limits screen). WIP ages 21.2 d and 9.3 d.
- **Done without matching merged code:** `I380`, `I384`, and **`I381` in part**. `I381` asked for a lockout and a biometric-backed credential. #110 adds a wrong-PIN lock to `POST /auth/step-up`, the first time one has existed. The biometric credential still exists nowhere, and the server still accepts only a PIN.
- **Stories out of step with their children:** `I371` (To do; `I372` in review), `BVA-I349` and `BVA-I351` (To do, unassigned; `I350`/`I352` in review), `I359` (To do, unassigned; `I360` Done, `I362` in review). Unchanged.
- **`I373`** (*Reflect card spending in the app*) is To do. Unchanged.

---

## 3. Code, API surface and spec drift

**Audit: clean after today's edit.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-12`), it first reported three consumer routes undocumented (`POST /auth/pin/reset/request`, `/auth/pin/reset/verify`, `/auth/pin/reset`), exit 1. After the spec edit it reported 165/165 consumer and 76/76 admin, proposed 32/18, clean spec health and no `x-beevia-*` (exit 0). The in-repo audit still reports phantom lines from the three `diverged` working trees. They were not acted on.

| Repo | From → to | What |
|---|---|---|
| `beevia-api` `main` | `5aa03d8` → `b5c046f` | #110 (merged 12 Nov 10:38 UTC): Forgot PIN, the wrong-PIN lock, attempts left on codes. Now on `beevia-db-schema` 0.0.54 |
| `beevia-admin-api` `main` | `b4e9744` | Unchanged. Still pins `beevia-db-schema` 0.0.50 |
| `beevia-db-schema` `main` | `01f677c` → `a871f3e` (v0.0.54) | #35 (merged 11 Nov 15:08 UTC): the `pin_reset` OTP purpose, `users.pin_failed_attempts`, `users.pin_locked_until` (migration 0054) |
| `beevia-admin` `main` | `64304ef` (30 Oct) | Unchanged |
| `beevia-mobile` `main` | `e40116d` | Unchanged. **New branch `feat-forget-pin-fixes`** (`36b03ff` 11 Nov 19:09 UTC, `3e23414` 12 Nov 06:49 UTC), no PR |

### 3.1 Forgot PIN and the PIN lock (`beevia-db-schema` #35, `beevia-api` #110)

- **Forgot PIN, for a signed-in user.** `POST /auth/pin/reset/request` sends a `pin_reset` code to the account phone and returns the number masked (`+234 812 *** 6789`). `POST /auth/pin/reset/verify` trades the code for a `reset_token`, a JWT valid 5 minutes (`JWT_PIN_RESET_TTL`) that can only set a PIN. `POST /auth/pin/reset` sets the new PIN with it, with no old PIN, clears any lock and sends a "Your PIN was changed" security push. `pin_reset` is not accepted by the public `/auth/otp/request`, so the code cannot be requested without a session.
- **The wrong-PIN lock.** One count is shared by `/auth/pin/verify`, `/auth/step-up` and `currentPin` on `/auth/pin`, and incremented with a single atomic `UPDATE`. Each wrong PIN is `pin_invalid` with `details.attempts_remaining`. The fifth (`PIN_MAX_ATTEMPTS`) locks PIN entry for 30 minutes (`PIN_LOCK_MINUTES`), returning `403 pin_locked` with `details.locked_until`, even for the right PIN. A right PIN clears the count; a reset unlocks at once.
- **Attempts left on every phone code.** A wrong code is `otp_invalid` with `details.attempts_remaining`, and the last allowed one is `otp_too_many_attempts`. This covers sign-up, login, phone change and Forgot PIN.
- **What it closes.** The commit states the problem: "a 4-digit PIN could be guessed by trying all 10,000, and the step-up it unlocks moves money." That was true from the first step-up route until 10:38 UTC today. It was also the missing half of `I381`, which was marked Done on 30 Oct.
- **Not touched, and still true.** No HTTP rate limit anywhere (`suggestions.md` §4.1). `KYC_RESET_ENABLED` has no startup check. The tier limits are applied nowhere. `isSubjectConsent` is a constant.

### 3.2 Three gaps in the lock (read, not run)

From `AuthService.checkPin` on `origin/main`. Nothing was executed.

1. **Requests sent together are all compared.** `checkPin` tests `pin_locked_until` on the user row it loaded at the start of the request, then runs scrypt. Only a *wrong* answer touches the counter. Every request that loaded the row before the fifth wrong answer was written gets its PIN compared, and a right one among them succeeds. The commit says "parallel guesses cannot slip past". That holds for the count, not for the guesses. With no rate limit, a single stolen session can send a burst far larger than five. **Fix:** reserve the attempt with a conditional `UPDATE … WHERE not locked AND count < max RETURNING`, compare only if a row came back, and give the attempt back on a right PIN.
2. **The lock does not escalate.** Locking sets the count back to zero, which allows 5 guesses per 30 minutes, indefinitely. That is about 240 a day: half the PIN space in about 21 days, all of it in about 42.
3. **A `reset_token` is reusable for its 5 minutes**, and a reset leaves the account's other sessions open. A session thief who also controls the phone number would reset the PIN next. The security push is the only signal.

All three are in `suggestions.md` §4.19.

### 3.3 The new mobile branch, `feat-forget-pin-fixes`

Two commits by `Davidtariq96` (11 Nov 19:09 and 12 Nov 06:49 UTC): 88 files, +3,531 −298, of which 62 under `lib`. **Not merged, no pull request.** Read, not run.

| Contract | On the branch |
|---|---|
| Forgot PIN (`/auth/pin/reset/*`) | `reset_pin_code.dart` (new) and `wallet_provider`. Reads `reset_token`; handles `pin_reset_invalid`, `otp_invalid`, `otp_too_many_attempts`, `otp_expired`, `otp_cooldown` |
| The PIN lock | The PIN sheet shows `attempts_remaining` and hides PIN entry after `pin_locked` |
| `POST /calls/{id}/ringing`, `call.ringing` | `call_api.dart` (new) reports ringing from the foreground, CallKit and the background push; `call_events.dart` handles the event |
| Voice notes | `voice_recorder.dart`, `voice_note_bubble.dart` (new). Sends `type: audio` with `contentMeta.durationMs`, as #109 requires |
| Profile photo removal | `profile_photo.dart` and `user_service` changed (+132/+18 lines) |
| Paystack top-up | `paystack_checkout_screen.dart` (new): hosted checkout from `POST /topups/initialize` in an in-app WebView instead of the browser |
| `call.ended` push | Still not handled |
| Biometric option in Chat Send | Still present, and the server still rejects it |
| `nin_not_found`, `bvn_required`, `verification_unavailable` | Still not matched by name |

This branch is what the 11 Nov edition asked for in recommendation 7 (send `call.ringing`), and it is the client #109 needs before any voice note can be sent. Until it merges, the score does not move.

### 3.4 The standing checks

- **`beevia-api` `release.yml`**: read in full. `sync` still has no `needs: test`, and its comment still says hosted runners cannot start jobs. It deploys and runs `pnpm db:migrate` on push to `main`. No workflow file changed in `5aa03d8..b5c046f` or in `beevia-db-schema` `01f677c..a871f3e`. #110 and migration 0054 went through the ungated path. `postman-sync` re-uploads the collection, which #110 edited.
- **`beevia-admin-api`** still pins `beevia-db-schema` 0.0.50. The consumer API is now on 0.0.54.
- **Branch protection, PR reviews and CI results**: cannot be seen from here.

### 3.5 Document changes this cycle

`openapi.yaml`: added `requestPinReset`, `verifyPinReset` and `resetPin`, and the `PinResetVerifyRequest` and `PinResetRequest` schemas. `verifyPin`, `stepUp` and `setPin` gain `403 pin_locked` and describe `attempts_remaining`. `verifyOtp`'s `400` names `attempts_remaining`. `openapi.admin.yaml`, `openapi.proposed.yaml` and `openapi.admin.proposed.yaml` are unchanged. `api-rfc.md`: 162 → 165, the Auth row 13 → 16, four inventory rows, and a new §5.26. `admin-api-rfc.md`: unchanged. `suggestions.md`: an update to §4.1 and a new §4.19.

---

## 4. Risks

- **The PIN lock can be raced, and there is no rate limit behind it.** It is better than nothing, which is what existed yesterday. It is not yet the limit the commit describes (§3.2).
- **A locked-out user has no way out on `main`.** The lock is live (it deployed on push), while the app's Forgot PIN on `main` says "coming soon". For 30 minutes such a user cannot verify a PIN or step up.
- **A review queue with code behind it and nobody accepting.** 24 REVIEW/QA leaves have merged code. If review does not start, the next sweep will mark them Done unseen, as on 21 Oct.
- **1002 ended a week ago with no successor sprint.** The filter cannot move, and `I348`/`I372` would be swept Done with no code.
- **A 62-file client branch with no PR.** The longer it waits, the more it looks like #58: one large merge, tested against its own mock server.
- **Every backend repo still deploys or migrates production on push without a test gate.** A schema migration went through it today.
- **A reset route with no production guard.** `KYC_RESET_ENABLED` is still a default and a comment. Unchanged.
- **The 30-day NIN clock.** The client is on `main`; whether it has shipped to users is not visible, and the limits are still not enforced.
- **A user can be told a person is coming when none can come.** No role holds `disputes`. Unchanged.
- **`isSubjectConsent: true` is sent to a third party for every BVN and NIN lookup** with no consent record. Unchanged.
- Carried, unchanged: the photo-hole check and the undeletable old photos; `call.ended` unconsumed; statement PDF password; FAQ search fallback; 0902's 15 removed leaves (not visible); the dashboard inbox's mock on by default; wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500`; production SSH (unverified); biometric step-up on `main`; Firebase keys in history; three diverged local working trees; `ANCHOR_POOL_ACCOUNT_ID` unseen; blocking does not reach payments; merchant payments cannot be disputed.
- **Withdrawn:** "no attempt limit on step-up". It is replaced by the narrower risk above.

---

## 5. PRD gap

The four structural gaps are unchanged and carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. #110 is account security. It hardens step-up, which lines 7 and 9 depend on, but it adds no capability the rubric counts. `activeNgn()` is unchanged.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 5 Nov 15:04 → 12 Nov 15:04 UTC. Commit counts are non-merge commits on all remote refs in that window. Each person's git identities are summed (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), and bots are excluded (4 on `beevia-db-schema`, 5 Dependabot on `beevia-mobile`). WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.**

**Median cycle times** are unchanged, because no item entered review: Ayomikun 1.48 d (n=22), David 0.99 d (n=36), Philip 0.89 d (n=3).

### 6.1 Ayomikun Araoye: backend + admin API

**20 commits in 7 days**: 15 in `beevia-api`, 1 in `beevia-admin-api` and 4 in `beevia-db-schema`. **One own submission**, `I362` on 11 Nov. **No WIP on 1002.** Since the last cut-off: `beevia-db-schema` #35 and `beevia-api` #110, neither an item on any board. Last commit 0.2 d old. #110 gives `I381` the lock it was closed without. `BVA-I8` has been In progress on the closed admin board for 59.0 days.

### 6.2 David Samuel: mobile

**3 commits** in 7 days: `c04e207` (9 Nov, now on `main` via #58) and the two on `feat-forget-pin-fixes` (11 Nov 19:09, 12 Nov 06:49 UTC). That branch is the client for three backend changes from the past two days. **Zero submissions** in the window; 4 Nov's two moves by board administration rolled out of it. His last own submission was `I286` on 14 Oct, **29.0 days** ago. **WIP: 2 items, both with code on `main`**: `I331` at 21.2 days and `I361` at 9.3 days. As on 11 Nov, this reads as items left in the wrong column rather than stuck work; that is for him to say. None of the new branch's work has an item.

### 6.3 Philip Chidera: design

**No submission, no WIP, nothing To do.** His last board action was on 2 Nov 15:58 UTC, **10.0 days** ago: finished, blocked or working untracked. Worth a question, not an assumption. Forgot PIN, the PIN lock message and voice-note recording now have screens on a branch, and none has a design item. Design files are not in git.

### 6.4 Promise Udo: admin dashboard

**No commits in the window.** The last, `64304ef` on 30 Oct, is **13.0 days** old, with no new branch or pull ref on `beevia-admin`. This report does not read that as nothing having been done. `I348` is in REVIEW/QA with no assignee; `I349` and `I351` are To do and unassigned. `BVA-I9` has been In progress on the closed admin board for 59.0 days.

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
| 2026-W46 (9 Nov → 12 Nov 15:04 UTC) | — | — | **1** | 1 | 0 | 0 |

**Nothing has left REVIEW/QA on 1002.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted from review by anyone other than its submitter since `BVA-I268` on 16 Sep. Output continues, in code if not on the board: two backend merges and a client branch in two days. Acceptance stays at zero. The bottleneck is the review step, not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** A security fix, a schema migration and an 88-file branch all count the same.
- **Who moved an item is not whether it is done.**
- **Untracked work.** #35, #110 and `feat-forget-pin-fixes` are not items on any board.
- **Commit counts reward small commits.** David's 3 commits carry 88 files.
- **Nothing here measures correctness.** No build, test, lint or app run took place in any repository. #110's commit reports an end-to-end test of the whole reset flow. That was read, not checked.

---

## 7. Previous recommendations: where they stand

| Recommendation from 11 Nov | Status on 12 Nov |
|---|---|
| **1. Review the 24 REVIEW/QA leaves with merged code** | ❌ **No board action at all** |
| **2. Close 1002 deliberately** | ❌ **Not done, a week late.** No successor, no sweep, filter still 08-01 |
| **3. Call each new route from a real build; handle three NIN errors** | ❌ **Not visible.** The three errors are not matched by name on `main` or on the new branch |
| **4. Check storage logs for the photo hole; backfill uploader metadata** | ❌ **Not visible.** No backfill commit |
| **5. Startup check for `KYC_RESET_ENABLED` in production** | ❌ **No.** `env.ts` changed today for the PIN settings only |
| **6. Grant `disputes` and `help_center`; name who goes on duty** | ❌ **Not visible.** `beevia-admin-api` unchanged |
| **7. Send `call.ringing` from the app; handle `call.ended`** | 🟡 **Ringing is on a branch** (`feat-forget-pin-fixes`). `call.ended` still not handled |
| **8. NIN step and support screens on the board** | ❌ **No** |
| **9. Decide whether the tier limits are enforced** | ❌ **No** |
| **10. Decide the seeded card default and what a card limit is** | ❌ **No** |
| **11. Confirm `ANCHOR_POOL_ACCOUNT_ID`; one real funding and reveal** | ❌ **Not visible** |
| **12. Record the consent behind each lookup** | ❌ **No** |
| **13. A log line or metric on the take-over fallback** | ❌ **No** |
| **14. Let a merchant payment be disputed** | ❌ **No** |
| **15. Fix the seams** | ❌ **No** |
| **16. Run one real chat and dispute through the assistant; decide it on the record** | ❌ **Not visible** |
| **17. Bring the dashboard onto the real contract** | ❌ **No commit in 13.0 days** |
| **18. Reopen `I380`, `I381`, `I384`; add an attempt limit to `/auth/step-up`** | 🟡 **The attempt limit shipped** (#110), with the gaps in §3.2. No item was reopened |
| **19. Agree how parent status moves work** | ❌ **No** |
| **20. Assign `I348`, `I349`, `I351`, `I359`, `I390`; give the dashboard a sprint** | ❌ **No** |
| **21. Retire `GET /cards/{id}/transactions`** | ❌ **No** |
| **22. `needs: test` on `sync`; current schema on `beevia-admin-api`** | ❌ **Not done.** A migration went through the ungated path today |
| **23. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** Three routes were added by hand today |
| **24. Carried items** | ❌ **None moved.** The biometric option is still in Chat Send, on `main` and on the branch |

**None of the 24 is fully met; two moved in part.** Both moves came from developers' own work (#110, the branch), not from the review or decision items.

---

## 8. What I would do this week

1. **Make the PIN check reserve its attempt before comparing (new).** One conditional `UPDATE … RETURNING`, before scrypt. Then lengthen repeated locks, make `reset_token` single-use and consider ending other sessions on reset (`suggestions.md` §4.19).
2. **Open a PR for `feat-forget-pin-fixes` and review it before it grows (new).** It is the only way out of the lock for users on `main`. Ask whether the in-app Paystack WebView was a decision.
3. **Review the 24 REVIEW/QA leaves that have merged code, and accept or return each one (carried).** Return `I348` and `I372`, which have no code.
4. **Then close 1002 deliberately (carried, a week late).** Move `I331` and `I361` to review if David agrees. Create the successor, carry `I373`, anything returned and items for #35/#110 and the branch. Do not sweep. Set `ZOHO_SPRINT_FILTER`.
5. **Add HTTP rate limiting, starting with the PIN, OTP and lookup routes (carried from `suggestions.md` §4.1, now pressing).** The lock depends on it.
6. **Call each new route once from a real build against the sandbox (carried).** Add the Forgot PIN flow and the lock once the branch merges. Handle `nin_not_found`, `bvn_required` and `verification_unavailable` by name.
7. **Check the storage logs for the photo hole, and backfill uploader metadata for old photos (carried).**
8. **Add a startup check that `KYC_RESET_ENABLED` is off in production (carried).**
9. **Grant `disputes` and `help_center` to the support role and Super Admin, and name who goes on duty (carried).**
10. **Handle `call.ended` in the app (carried, narrowed: ringing is on the branch).**
11. **Put the NIN step, the support screens and Forgot PIN on the board with a design and an owner (carried, extended).**
12. **Decide whether the tier limits are enforced, and what the end of the grace does (carried).** About 6 Dec is the date for existing users.
13. **Decide the seeded card default and what a card limit is, on the record (carried).**
14. **Confirm `ANCHOR_POOL_ACCOUNT_ID` in production and run one real funding and one reveal (carried).**
15. **Record the consent behind each BVN and NIN lookup (carried).**
16. **Put a log line or metric on the take-over fallback; let a merchant payment be disputed; fix the seams (carried).**
17. **Run one real chat and one real dispute through the assistant, and decide the assistant on the record (carried).**
18. **Bring the dashboard onto the real contract (carried)**, default the mock off in production builds, and add the agent side of support chat, take-over and the card-limit default.
19. **Reopen `I380` and `I384` if those closes were not meant for them, and narrow `I381` to the biometric credential (carried, narrowed).**
20. **Agree how parent status moves work; assign `I348`, `I349`, `I351`, `I359` and `I390`; give the admin dashboard a sprint (carried).**
21. **Retire `GET /cards/{id}/transactions` (carried).**
22. **Put `needs: test` back on `beevia-api`'s `sync`**, give db-schema's Release and admin-api's Sync a verify job, and bring `beevia-admin-api` onto `beevia-db-schema` 0.0.54 (carried).
23. **Generate `openapi.yaml` from the running app and diff it in CI (carried).**
24. **Carried:** remove the biometric option in Chat Send; send a push when an agent replies; reopen `I392`; close the payments half of blocking; add the `en-US` fallback to FAQ search; decide the statement password; account for 0902's 15 leaves; test the iOS ring on a device; add the `messages.ref_id` index; restrict the Firebase API keys; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; prune the §7 tables in `api-rfc.md`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 59.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 59 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work sits on the consumer board's 1002 instead: `I349` Support Inbox (To do, unassigned; screen on mock; API child `I350` in review), `I348` Triage Flow Configuration (REVIEW/QA, unassigned; screen on mock) and `I351` FAQ CMS (To do, unassigned; API only). `beevia-admin` last moved 13.0 days ago and has no new branch or pull ref. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈68% (estimate; 68.36, no change)

**Target 2026-09-01 (provisional). The target date passed seventy-two days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No line moves.** Everything new is either on the server and outside the rubric's capabilities, or on an unmerged branch.

- **Line 7 (send/request/receive) holds at 0.92.** #110 puts a lock on the step-up that chat Send uses, but the line is held for the biometric option, which is still in Chat Send on `main` and on the new branch.
- **Lines 1 (E2EE, 0.90) and 2 (calling, 0.92) hold.** The voice-note recorder and the ringing report are on `feat-forget-pin-fixes`, not `main`. They are the first candidates to reconsider once it merges. `call.ended` remains unhandled either way.
- **Line 9 (virtual cards) holds at 0.88; line 6 (multi-currency) at 0.85; line 4 (local KYC) at 0.93; line 11 (admin) at 0.97.** No code in those areas changed.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | Unchanged on `main`; the voice-note recorder is on a branch |
| 2 | Voice & video calling | 8 | 0.92 | 0 | Ringing client on a branch; `call.ended` unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `StubTranslateAdapter` still bound |
| 4 | Local KYC tier (BVN) | 8 | 0.93 | 0 | Unchanged. Tier 3 and holds unbuilt; limits unenforced |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Step-up now has a lock (#110); biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.88 | 0 | Unchanged. Verification model undecided; limits cap funding only |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No admin code changed |
| | **Weighted total** | **100** | **68.36** | **0** | **≈68%** |

### What this report cannot tell you

- **Whether the PIN lock can be raced in practice.** §3.2 is a reading of the code. Whether a proxy in front of the API limits request rates is not visible.
- **Whether #110 and migration 0054 are live.** The workflow deploys on push; its result and target host are not visible.
- **Whether any of the merged or branched client screens work against the API.** Nothing was executed.
- **Whether #58 has shipped to users**, in which build, and to which stores.
- **Whether the photo-deletion hole was used before #108.**
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

1. Three background exports starting at about 15:01 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0, sidecar byte-identical to 11 Nov. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0, sidecar byte-identical. A read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0, sidecar byte-identical. The Beevia sprint list came from the `__nonexistent__` dry run: `['1002', '0902', '0901', '08-01', '0702', '0701']`. 0901 and 0902 were not re-exported.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current on `main`, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged`, unchanged since 8 Sep.
3. Audit (step 3) against a `git archive` shadow at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-11-12`: exit 1 before the spec edit, exit 0 after. The in-repo audit also ran, for the board section; it produced phantom lines only. Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`flow12.py`, a date-shifted copy of 11 Nov's). It diffed 1002 against 11 Nov, listed every action in the window (none), split 7-day submissions by actor, and computed WIP ages and the weekly trend.
5. Content checks. `ls-remote` of heads and `refs/pull/*`. In `beevia-api`: #110's commit message and its controller, DTO, service, token, OTP, env, phone and locale diffs; the public OTP purpose enum; the absence of any HTTP rate limiter. In `beevia-db-schema`: #35's log. In `beevia-mobile`: `main`'s Forgot PIN handler, and on `feat-forget-pin-fixes` the file list, the new constants and socket events, the PIN reset and lock handling, the ringing calls, the voice-note send path, the Paystack checkout, the NIN error names, the biometric option and `call.ended`. `release.yml` read in full.
6. Spec and narrative updates (§3.5).
7. This report and its web edition.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, and their actions are reported without naming the actor. Commits under the project owner's identity on `beevia-mobile` (8 in the window: 7 carried by #58 and 1 on `App-bundle`) are not a row.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed. A final `fetch` of all five repos at 15:08 UTC found nothing new, and a fast 1002 re-export at the same time found no board action.

**Files changed this cycle:** this report, `web-report/2026-11-12.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md` and `suggestions.md`. New board exports for 12 Nov were written to `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`.** The in-repo main export is therefore a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.
- **The mobile item-to-code mapping for the 12 REVIEW/QA leaves was carried from 10 Nov.** It was not re-derived item by item.

**Window.** 11 Nov 15:01 UTC → 12 Nov 15:04 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets (−07:00).
