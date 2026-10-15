# Beevia — Project Status

**As of 2026-10-15** · Sprint **0902** (30 Sep → 15 Oct): **last day, 25 items, 0 leaves To do · 3 In progress · 16 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-15.csv` + `beevia-activity-2026-10-15.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-15.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 14 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`, and `beevia-mobile`'s unmerged `origin/BVA-I316` and its new Dependabot branches too. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 14 Oct 14:02 UTC → 15 Oct 14:03 UTC, 1.0 day.**

---

## Quick overview

> **Sprint 0902 ends today with 16 of its 21 leaves in REVIEW/QA, none reviewed, and still no sprint after it.** One item moved: `BVA-I286` went to review after 14 days in progress, and the one visible part of its fix that is still undone (the "Transactions History" label) is not on any branch. The day's real work went into `beevia-mobile`'s unmerged `BVA-I316` branch. It now routes push taps to the right screen (`BVA-I307`), and on Android it reads the incoming-call push in the server's own format. The iPhone token clash recorded on 13 Oct is unchanged, so the branch is still not safe to merge as it is.

| Metric | 14 Oct | 15 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 0 / 4 / 15 / 1 / 1 | **0 / 3 / 16 / 1 / 1** | `BVA-I286` In progress → REVIEW/QA |
| Board actions in the window (all boards) | 0 | **1** | David, 14 Oct 16:01 UTC |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **10** | 6 by the leaf's owner, 1 by another team member, 3 by board administration |
| Owners' last submission of their *own* leaf | 12 Oct 16:03 UTC (Ayomikun, `I325`) | **14 Oct 16:01 UTC (David, `I286`)** | |
| Items that left REVIEW/QA in the window | 0 | **0** | none, apart from the two bulk sweeps |
| 0902 leaves in REVIEW/QA whose code is not (fully) on `main` | 3 | **4** | `I316`, `I324` unmerged; `I325` nowhere; **`I286` partly** |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | no workflow change |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | |
| `beevia-mobile` days since a commit on `main` | 6.1 | **7.1** | branch `origin/BVA-I316` pushed 14 Oct 16:10 UTC |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.8 / 6.3 / 5.1 | **1.8 / 7.3 / 6.1** | db-schema's last is the bot's v0.0.40 bump |
| `beevia-admin` days since a commit | 21.9 | **22.9** | |
| Admin board: open sprint / days since any activity | none / 30.0 | **none / 31.0** | |
| Successor sprint to 0902 in Zoho | none | **none** | 0902 ends today |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: all new code is on a branch |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | 4 (**all own**) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**31.0 d**) | **13** (all `beevia-api`) | No push or board action since #71 (13 Oct 17:43 UTC) |
| David Samuel | mobile | **0902: 15** (11 REVIEW/QA, 3 In progress, 1 BLOCKED) | 8 (**2 own**, 3 by Ayomikun, 3 by board administration) | 0.98 d (n=34) | `I313` (**7.9 d**) · `I309` (3.0 d) · `I307` (2.2 d) | **0 on `main`** + **4 on `origin/BVA-I316`** | `I286` submitted after 14.0 d; its label rename is not on any branch. `I307`'s routing exists, branch only |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 0 | 0.99 d (n=3) | none | n/a | No board action since 2 Oct |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**31.0 d**) | **0** | `beevia-admin` **22.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **What happens to 0902 tonight?** 16 leaves sit in review and 4 are open, with no 0903 to receive them. If 0902 is closed by a sweep, as 0901 was on 30 Sep, four review items without their code on `main` will be marked Done. (2) **What is the merge plan for `BVA-I316`?** It now carries four tickets (`I307`, `I309`, `I316`, `I324`). It cannot merge safely until the VoIP token registration is removed or the server keeps a second token. (3) **Is `BVA-I286` finished?** The board says it is ready for review, but the profile screen still says "Payment History" on every branch.

**The three things worth knowing:**

1. **`BVA-I286` went to review with part of its fix missing.** David moved it on 14 Oct at 16:01 UTC, after 14.0 days in progress (their median is 0.98 d). The ticket lists five fixes to the contact-profile screen. Two of them, the phone number and the joined date, have been on `main` since `99c8909` (27 Sep). The rename of "Payment History" to "Transactions History" is not done: the label is `paymentHistory` → "Payment History" on `main`, on `BVA-I316` and in all four locales. Whether the message button, username and counts now match the design cannot be judged from code. This is the fourth 0902 review item whose code is not fully on `main`.

2. **The `BVA-I316` branch now does `BVA-I307`'s job, and half of `BVA-I309`'s contract fix.** `d507fe4` (14 Oct 16:10 UTC) replaces "every tap opens Home" with routing by the server's `data.kind`: chat pushes open the conversation, payment and wallet pushes open the Wallet tab, security alerts open Settings. On Android, the call handler now reads `kind`, `callId`, `conversationId` and `callKind`, which is exactly what `notifyIncomingCall()` sends. That closes the Android half of the mismatch recorded on 13 Oct. Two gaps remain. The native call screen will show "Beevia" rather than the caller, because the server puts the caller's name only in the banner text (a two-line server fix). And `I307` is still In progress on the board while its code sits on an unmerged branch. On `main`, every tap still opens Home.

3. **The iPhone push risk is unchanged, and the branch keeps growing around it.** `call_kit_manager.dart:80` still registers the PushKit token with `pushProvider: 'voip'` for the same device id. The server still keeps one push token per device and has no APNs sender. Merged as it stands, the branch would make iPhones lose message, payment and security pushes whenever the VoIP token holds the slot (`api-rfc.md` §5.15). The branch is now 4 commits ahead and 2 behind `main` and covers four tickets, so the longer it waits, the more the fix and the merge depend on each other.

**If you read nothing else:** 0902 ends today with no reviewer and no successor sprint. One leaf moved, into review, and part of its fix is missing. The new mobile work is real and lines up with the server's push format, but it is all on one unmerged branch that still carries the iPhone token clash.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. Against the 14 Oct scratch export, one row changed: `BVA-I286`, status and `Last Modified`. The activity sidecar has exactly one new entry in the window.

| Status | 14 Oct | 15 Oct | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 4 | **3** | −1 |
| REVIEW/QA | 15 | **16** | +1 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

| Time (UTC) | Item | Move | By |
|---|---|---|---|
| 14 Oct 16:01:21 | `BVA-I286` *Mismatched UI element on User Profile screen* | In progress → REVIEW/QA | David Samuel (owner) |

No comment, reopen, completion or re-assignment on any board. The move came nine minutes before David pushed `d507fe4` to `BVA-I316`, but that commit does not touch the profile screen (§2).

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static, and their sidecars are byte-identical to 14 Oct's. 0901's last entry is still the 30 Sep sweep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 on its last day

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **4 REVIEW/QA** (`I306`, `I308`, `I310`, `I312`), 3 In progress (`I307`, `I309`, `I313`), **1 BLOCKED** (`I311`) | `I306`, `I312` on `main` (PR #44). `I308`/`I310` server halves on `main` (#64, #65). **`I307`: tap routing now on `origin/BVA-I316`** (`d507fe4`). **`I309`: Android contract aligned on the branch, iOS token clash open.** `I313`: screen and wiring on `main` since July. `I311`: the server sends neither push it displays |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, screen `I316` REVIEW/QA | Feed on `main` (#66). Screen on `origin/BVA-I316` only |
| Appearance (`BVA-I318`–`I329`) | 9 | all 9 REVIEW/QA | On `main` (PR #43) except `I324`'s chat-background application (branch only). `I319`, `I325`, `I328` have no server code |
| Carried bug `BVA-I286` | 1 | **REVIEW/QA since 14 Oct** (14.0 d in progress) | **Partly on `main`** (below) |

**`BVA-I286`, checked against the ticket.** The ticket (from the UI audit, section 1.3) lists five fixes for the contact-profile screen (`lib/features/chat/screens/contact_profile.dart`):

| Ticket asks | Code |
|---|---|
| Phone number and joined date not displayed | **Done on `main`** since `99c8909` (27 Sep): both rows now read `profile.phone` and `profile.joinedAt`, where they had been hard-coded `""` |
| Rename "Payment History" to "Transactions History" | **Not done anywhere.** `context.l10n.paymentHistory` → "Payment History" (and its es/fr/zh strings) on `main`, `BVA-I316`, `BVA-I306` and `BVA-I317` |
| Message button does not match the design; username not displayed as designed | Cannot be judged from code |
| Media count and transaction count not accurate | Not checked. The screen shows the server's `media_count`/`payment_count`, so an inaccuracy may be server-side |

No commit on any remote branch has touched the profile screen since 5 Oct (`6f38116`, theming). So whatever moved `I286` on 14 Oct is not in a pushed commit, unless the remaining items are judged out of scope. A comment on the item would settle it.

**The sprint ends today** with 3 leaves in progress, 1 blocked and 16 in review. Zoho still lists only `0902, 0901, 08-01, 0702, 0701` for Beevia.

---

## 3. Code, API surface and spec drift

**Audit: clean at route level.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-15`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin), identical to 14 Oct. They were not acted on.

**No `main` moved in any repository.** `beevia-api` is still at `f836b91` (#71, 13 Oct), `beevia-admin-api` at `c59460a` (8 Oct), `beevia-db-schema` at `40ecf69` (v0.0.40, 9 Oct), `beevia-admin` at `0b41e35` (22 Sep), `beevia-mobile` at `4f9c29f` (8 Oct). No spec change was needed.

### 3.1 `beevia-mobile` `origin/BVA-I316`: `d507fe4`

One commit, `call kit implementation`, by `Davidtariq96` at 14 Oct 16:10 UTC: 6 files, +265/−58. The branch is now **4 ahead, 2 behind** `main`.

| Area | Change | Against the server |
|---|---|---|
| Push tap routing (`BVA-I307`) | `_routeToPushTarget` switches on `data.kind`. `chat.message` opens the conversation (refetching the list once if needed). `payment.update`/`wallet.update` open Home on the Wallet tab (new `HomeScreen.initialTabIndex`). `security.alert` opens Settings, and the rest open Home. Foreground pushes now carry `data` as the local notification's payload, so those taps route too | Keys match §5.13 exactly. `paymentId`, `event` and `reference` are not used, so a payment push lands on the wallet, not on the payment |
| Android incoming call (`BVA-I309`) | Matches `data.kind == 'call.incoming'` and reads `callId`, `conversationId`, `callKind`. `CallProvider` derives the initiator from the conversation | **Now matches `notifyIncomingCall()`**. The caller name falls back to "Beevia", because the server sends `initiatorName` only in the banner body |
| iOS incoming call | Unchanged: PushKit token registered as `pushProvider: 'voip'` (`call_kit_manager.dart:80`) | **Still overwrites the device's FCM token server-side** (§3.2) |
| Chat screen | Replaces in place when the same text or attachment message id arrives twice (socket delivery racing the catch-up fetch after a notification-tap cold start) | Client-only |

Two minor points. The foreground handler now `print`s each push's full `data` map. For chat pushes that is metadata only (conversation, message and sender ids), but it reaches device logs in release builds. And the server's visible `notification` block on `call.incoming` is still there, so on Android the user may see a banner as well as, or instead of, the ringing screen, depending on app state. That cannot be told from the code (`api-rfc.md` §5.15, updated today).

### 3.2 The standing checks

- **VoIP token clash** (`api-rfc.md` §5.15): **open.** The client still registers the VoIP token for the FCM device id, and the server still has one token slot per device and no APNs sender. The branch has not merged, so the risk has not materialised.
- **Pipelines:** no workflow file changed. `beevia-api`'s `release.yml` `sync` job still has no `needs: test`. `beevia-db-schema` Release/Sync and `beevia-admin-api` Sync/Deploy still run on push to `main` with no verify job. Latest db-schema tag is still `v0.0.40`.
- **Mobile `main`** is the same commit as yesterday (`4f9c29f`), so yesterday's checks stand: no conflict markers, `ios/GoogleService-Info.plist` still tracked, biometric step-up still on `main` against a PIN-only `stepUpSchema`.
- **Dependabot opened its weekly `beevia-mobile` branches** on 14 Oct, 19:42–19:51 UTC: `local_auth` 2.3.0 → **3.0.2** (major; the biometric plugin), `cupertino_icons` 1 → 2, a Gradle group, and a "minor-and-patch" pub group. That group includes **`flutter_local_notifications` 19.5.0 → 22.3.2**, three majors, inside a batch the config describes as "routine and low-risk". The push code on `BVA-I316` depends on that plugin's callback API (`onDidReceiveNotificationResponse`). The group PR should not be merged as routine, and not before `BVA-I316` lands.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` unchanged. `22P02` still unmapped.

### 3.3 Document changes this cycle

- **`api-rfc.md`:** §5.13 gets a 15 Oct update (client tap routing by `data.kind`, on the branch). §5.15 gets a 15 Oct update (Android contract aligned; caller name missing from `data`; VoIP registration unchanged; the visible `notification` block).
- `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin*.yaml`, `admin-api-rfc.md`, `suggestions.md`: unchanged. No route or schema changed on any `main`.

---

## 4. Risks

- **0902 ends today with no reviewer and no successor.** A bulk close would mark `I316`, `I324` (unmerged), `I325` (no code) and `I286` (partly done) as Done. Without 0903, the four open leaves have nowhere to go.
- **Merging `BVA-I316` unchanged would break pushes on iPhones** (§3.2). The branch now bundles four tickets, which raises the pressure to merge it whole.
- **A Dependabot group PR on mobile hides a three-major bump** of the notifications plugin under "minor-and-patch" (§3.2).
- **Wallet-failure notices are off by default** (14 Oct edition §3.1). Undecided.
- **Every backend repo still deploys or migrates production on push without a test gate.**
- **PII may be in production logs from before 12 Oct** (13 Oct edition §3.1). Not visible here.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1).
- **`BVA-I311` is blocked on server work nobody has been asked for.** 6 days, no comment.
- **Firebase keys tracked and in history**, unrestricted as far as can be seen. **Production SSH open to any address**, per the 1 Oct deploy commits. Both unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11). Dependabot's `local_auth` 3.x bump touches the same code.
- **The admin workstream is silent:** 22.9 days without a `beevia-admin` commit, 31.0 days without admin-board activity, no sprint.
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. Today's branch work is notifications and calling UX.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 8 Oct 14:05 → 15 Oct 14:05 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners.

### 6.1 Ayomikun Araoye: backend + admin API

**13 commits in 7 days, all in `beevia-api`** (#63–#71; the 8 Oct dependency refreshes in `beevia-admin-api` and `beevia-db-schema` fell out of the window). Nothing pushed and no board action since #71 merged on 13 Oct at 17:43 UTC, 1.8 days. All six of their 0902 leaves are in review. Their four 7-day submissions were all their own moves (`I308`, `I310`, `I315` on 8 Oct, `I325` on 12 Oct). Median cycle time **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 31.0 days. The two-line `call.incoming` change (§3.1) would be theirs, if the team wants the caller's name on the native call screen.

### 6.2 David Samuel: mobile

**No commit on `main` in 7 days** (the last, PR #44, was 8 Oct 10:38 UTC, just outside the window), **and 4 on `origin/BVA-I316`** (9, 12, 13 and 14 Oct). The newest, `d507fe4`, is substantial (§3.1). It implements `I307`'s routing and aligns `I309`'s Android contract with the server, but neither item has moved on the board. Their one board action in the window was `BVA-I286` to REVIEW/QA, after **14.0 days** in progress, against a 0.98-day median (n=34, which now includes it). Part of that ticket is not on any branch (§2). Of their eight 7-day submissions, two were their own (`I329`, `I286`), three Ayomikun's (`I308`, `I310`, `I324`) and three board administration's (`I306`, `I312`, `I316`). WIP: `I313` 7.9 d (its screen exists on `main`; the open question is design fit), `I309` 3.0 d, `I307` 2.2 d.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC. `BVA-I321` has been in REVIEW/QA since 7 Oct, moved there by David, and has now left the 7-day window, so their count is 0. Open WIP is zero. Whether `I286`'s message button and username now match the design, and whether the `I313` screen matches its design, are questions only design can answer.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **22.9 days** ago. The admin board has had no activity for 31.0 days, and `BVA-I9` has been In progress for all of it. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible here.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (from Mon 12 Oct, 4 days) | — | **6** | 2 | 1 | 3 |

Acceptance is still zero. Over 0902's sixteen days there were 16 transitions into review, and the review step took none. The bottleneck is not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more.
- **Work outside the board.** `d507fe4` advances two In progress items that have not moved. #71 had no item at all.
- **Who moved an item is not whether it is done.** `I316` and `I324` reached review unmerged, `I325` with no code, and `I286` with part of its fix missing.
- **Branch commits are not delivery,** so they are counted separately.
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 14 Oct | Status on 15 Oct |
|---|---|
| **1. Create 0903 and move the open leaves into it; do not close 0902 by sweep; set `ZOHO_SPRINT_FILTER` to `0903`** | ❌ **Not done.** No 0903. 0902 has not been swept yet either |
| **2. Review what is on `main` before the close; send `I316`/`I324` back; close `I319`/`I325`/`I328` with a note** | ❌ **Not done.** Nothing left review |
| **3. Rescope `BVA-I313` against what exists** | ❌ **Not done.** No comment on the item |
| **4. Decide the `walletActivity` default; add a board item for #71** | ❌ **Not done** |
| **5. Fix or remove the VoIP token registration before `BVA-I316` merges** | ◐ **Holding.** Not fixed (`d507fe4` left it in place), but the branch has not merged |
| **6. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done** |
| **7. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done** |
| **8. Check the production logs for pre-12 Oct PII** | ? **Not visible** |
| **9. Map `22P02` to `400`** | ❌ **Not done** |
| **10. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ❌ / ? Still tracked |
| **11. Make Flutter CI a required check** | ? **Not visible** |
| **12. Check the production host's SSH settings** | ? **Not visible** |
| **13. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **14. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **15. Open the admin board's next sprint, or say it is paused** | ❌ **Neither** |
| **16. Carried items** | ❌ **None moved** |

**None of sixteen done, one holding.** The work that did happen (`d507fe4`) advances sprint items but none of these recommendations.

---

## 8. What I would do this week

Re-ranked for the sprint boundary.

1. **Today, create 0903 and move the open leaves into it**: `I307`, `I309`, `I311`, `I313`. Do not close 0902 by sweep. Then set `ZOHO_SPRINT_FILTER` to `0903`, so the in-repo export stops reading 08-01.
2. **Review what is on `main` before the close**: `I306`, `I308`, `I310`, `I312`, `I315`, `I318`, `I321`, `I322`, `I327`, `I329`. Send `I316`, `I324` and `I286` back to In progress, the first two until their branch merges and `I286` until the label rename lands (or note on the item why it is out of scope). Close `I319`/`I325`/`I328` with a note, or open one backend item to extend `PATCH /users/me/settings`.
3. **Before `BVA-I316` merges, remove the VoIP token registration** or give the server a second token slot (`api-rfc.md` §5.15). Removing it is the smaller change and keeps Android's now-correct call path.
4. **Add `callerName` to `call.incoming`'s `data`** on the server, so the native call screen can show who is calling (`api-rfc.md` §5.15).
5. **Hold the Dependabot `pub-minor-and-patch` PR on mobile** until `BVA-I316` lands, and treat `flutter_local_notifications` 19 → 22 and `local_auth` 2 → 3 as code changes, not routine bumps.
6. **Rescope `BVA-I313` against what exists**, and decide the `walletActivity` default.
7. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
8. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4).
9. **Check the production logs for PII from before 12 Oct.**
10. **Map `22P02` to `400`** (`suggestions.md` §1.1).
11. **Restrict the Firebase API keys and untrack `ios/GoogleService-Info.plist`** (`suggestions.md` §5.13).
12. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
13. **Check the production host's SSH settings.**
14. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
15. **Bring `payments.dto.ts` onto `phone.util.ts`.**
16. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
17. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 31.0 days ago**. Today's sidecar is byte-identical to 14 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 31 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 22.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-four days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved.** No `main` changed in any repository. `d507fe4`'s calling work is on an unmerged branch, and line 2 does not move for CallKit until it is on `main` and the server can ring it on both platforms.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change on `main`. The duplicate-bubble fix is branch-only |
| 2 | Voice & video calling | 8 | 0.85 | 0 | CallKit on `origin/BVA-I316` only. Android payload now matches; iOS still cannot ring |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | No change; biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Why `BVA-I286` was moved to review** with the label rename undone, or whether the remaining design points were met. No comment records it.
- **Whether the Android background handler runs** for a `call.incoming` push that carries a visible `notification` block. That depends on device state, not code.
- **Whether #70 or #71 is deployed**, or whether FCM is configured in production (`FCM_SERVICE_ACCOUNT`).
- **Whether anyone but the author reviewed any PR**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0). The three ran in parallel from about 14:02 UTC.
2. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
3. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-15`: clean. The in-repo audit was run too, for the board section; its 23 drift lines are the known phantom, identical to 14 Oct. Both ran through `uv run --no-project --with pyyaml`.
5. Board comparison: `cmp` of every sidecar against 14 Oct's, a CSV diff past the preamble, and a listing of every audit entry after 14 Oct 14:00 UTC. Flow analysis (`flow15.py`): cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none).
6. Content checks. In `beevia-mobile`: every remote branch with dates, the full `d507fe4` diff, the VoIP registration on `BVA-I316`, the contact-profile screen and its l10n strings on four branches, the history of that screen since 24 Sep, and the Dependabot config and branch contents. In `beevia-api`: the `data` keys of every push kind in `notification.service.ts`, and `notifyIncomingCall()`'s callers. In all three backend repos: the `on:`/`needs:` lines of every release, sync and deploy workflow.
7. `api-rfc.md` updates (§3.3).
8. This report and its web edition.
9. End-of-run recheck at about 14:08 UTC: a fast re-export of 0902 (`--activity --no-descriptions`, exit 0) found no audit entry after 14 Oct 16:01 UTC, and `ls-remote` showed every `main` and `BVA-I316` at the commits read above. Nothing in this report changed as a result.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive`, `ls-remote` and read-only `log`/`show`/`diff`/`grep`/`ls-tree`/`rev-list`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-15.html`, `web-report/index.html`, `api-rfc.md`, plus new board exports for 15 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.** Dependabot's branches are visible, but not whether their PRs pass CI.
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 14 Oct 14:02 UTC → 15 Oct 14:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
