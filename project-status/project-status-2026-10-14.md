# Beevia — Project Status

**As of 2026-10-14** · Sprint **0902** (30 Sep → 15 Oct): **day 15 of 16, 25 items, 0 leaves To do · 4 In progress · 15 REVIEW/QA · 1 BLOCKED · 1 Done** · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-14.csv` + `beevia-activity-2026-10-14.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-14.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **0902 (25 items)** in `/tmp/beevia-scratch/0902/`, diffed against the 13 Oct file in the same folder. Sprint 0901 was read from the 5 Oct scratch export (closed; nothing on it has moved since 30 Sep). All five repos were read at `origin/main`, and `beevia-mobile`'s unmerged `origin/BVA-I316` too. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: four boards, kept separate and never summed. **Window: 13 Oct 14:03 UTC → 14 Oct 14:02 UTC, 1.0 day.**

---

## Quick overview

> **Nothing moved on any board in the last 24 hours, and sprint 0902 ends tomorrow with 15 of its 21 leaves in REVIEW/QA, none reviewed, and no sprint after it.** The work went into code. `beevia-api` #71 (13 Oct, after the last edition's cut-off) makes the wallet-activity notification switch do something for the first time: nine pushes for top-ups, bank deposits, payouts and card loads. No board item tracks it, and the switch is off by default, so most users will receive none of them. This edition also corrects two things this pipeline had wrong for some time: the notification settings screen it said did not exist, and the preferences schema in `openapi.yaml`.

**Correction to the 8, 9 and 13 Oct editions.** They said `BVA-I313`'s notification settings screen did not exist ("no notification-settings screen on any branch", 13 Oct). **It does, and has since July.** `lib/features/settings/screens/notifications/notifications.dart` is on mobile `main`, with nine category toggles plus tones and feedback, wired to `GET`/`PATCH /notifications/preferences`. Its field names match the server's exactly. Those editions looked for new code on branches and never checked what was already on `main`. What `I313` still lacks is narrower (§2): the ticket's design groups the toggles into four categories, and one of them, *Account & Verification*, has no counterpart on the server.

**Correction to `openapi.yaml`, wrong since it was written on 5 Aug.** `NotificationPreferences` described five categories (`chat`, `calls`, `payments`, `security`, `system`) that the server replaced on 4 Aug. The route-level audit cannot see a wrong schema, so it reported clean for seventy days. Fixed in this edition (§3.2).

| Metric | 13 Oct | 14 Oct | Δ |
|---|---:|---:|---|
| Sprint 0902 items (leaves + parents) | 25 (21+4) | 25 (21+4) | 0 |
| Sprint 0902 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 0 / 4 / 15 / 1 / 1 | **0 / 4 / 15 / 1 / 1** | none |
| Board actions in the window (all boards) | 11 | **0** | first silent weekday since 6 Oct |
| Transitions into REVIEW/QA, last 7 days (leaves) | 15 | **10** | 5 by the leaf's owner, 2 by another team member, 3 by board administration. The 6 Oct batch left the window |
| Owners' last submission of their *own* leaf | 12 Oct 16:03 UTC (Ayomikun, `I325`) | **unchanged** | David's: 9 Oct 14:07 UTC |
| Items that left REVIEW/QA in the window | 0 | **0** | never, apart from the two bulk sweeps |
| 0902 leaves in REVIEW/QA whose code is not on `main` | 3 | **3** | `I316`, `I324` unmerged; `I325` nowhere |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | #71 went out the same way |
| API surface (consumer / admin) | 139 / 49 | 139 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | one *schema* error fixed by hand (§3.2) |
| `beevia-mobile` days since a commit on `main` | 5.1 | **6.1** | branch `origin/BVA-I316` unchanged since 13 Oct 14:02 UTC |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 5.3 / 4.1 | **0.8 / 6.3 / 5.1** | |
| `beevia-admin` days since a commit | 20.9 | **21.9** | |
| Admin board: open sprint / days since any activity | none / 29.0 | **none / 30.0** | |
| Successor sprint to 0902 in Zoho | none | **none** | 0902 ends tomorrow |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | 0/25 · 0/76 · 0/12 · 0/64 | **0/25** · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (66.76)** | 0: notifications are not a rubric capability |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **0902: 6, all in REVIEW/QA** · 0901-admin: 1 In progress | 4 (**all own**) | 0.99 d (n=16) | none on 0902 · `BVA-I8` on 0901-admin (**30.0 d**) | **17** (api 15, admin-api 1, db-schema 1) | Shipped #71 (wallet pushes), which no board item tracks |
| David Samuel | mobile | **0902: 15** (10 REVIEW/QA, 4 In progress, 1 BLOCKED) | 7 (**1 own**, 3 by Ayomikun, 3 by board administration) | 0.98 d (n=33) | `BVA-I286` (**13.9 d**) · `I313` (6.9 d) · `I309` (2.0 d) · `I307` (1.2 d) | **2 on `main`** (8 Oct) + **3 on `origin/BVA-I316`** | No push and no board action since 13 Oct 14:02 UTC. `I313`'s screen exists (correction above) |
| Philip Chidera | design | **0902: 2**: `BVA-I314` Done, `BVA-I321` REVIEW/QA | 1 (moved by David) | 0.99 d (n=3) | none | n/a | No board action since 2 Oct |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | `BVA-I9` (**30.0 d**) | **0** | `beevia-admin` **21.9 days** without a commit. No admin sprint |

**The three questions for standup:** (1) **What happens to 0902 tomorrow?** Fifteen leaves are in review and five are open. If it closes by sweep, as 0901 did on 30 Sep, three leaves with no code on `main` will be marked Done. And with no 0903, the five open leaves have nowhere to go. (2) **Is `wallet_activity` meant to be off by default?** After #71 it decides whether a user hears that a payout failed and the money is back. (3) **What is left on `BVA-I313`?** The screen and its wiring exist. Is the outstanding work the design's four-group layout, and who owns the missing *Account & Verification* category on the server?

**The three things worth knowing:**

1. **The board went quiet on the sprint's second-to-last day.** No status change, comment, reopen or completion on any of the four boards between 13 Oct 14:03 and 14 Oct 14:02 UTC. The last 0902 action was `BVA-I307` going back to In progress on 13 Oct at 09:06 UTC. Since then, everything that happened is in git: #71 in `beevia-api` and the CallKit commit on `origin/BVA-I316`. Zoho still lists `0902, 0901, 08-01, 0702, 0701` for Beevia and only `0901-admin` for the admin project.

2. **`beevia-api` #71 gives the `walletActivity` switch its first sender, nine events.** Card top-ups (succeeded / failed), inbound bank deposits, bank payouts (completed / failed) and card loads and withdrawals (four outcomes) now push a `wallet.update` with an `event` and a `reference`. The hooks sit where the webhook, the client's status poll and the reconciliation sweep converge, behind each record's existing "already settled" guard. That guard, plus a `reference:event` dedupe key, keeps one movement to one push. A failure push says "the money is back in your wallet" and is sent only when the ledger reversal actually succeeded. When the reversal fails, the push is held back and the existing critical Slack alert stands. The care is visible in the code and in about 130 lines of new tests for top-ups, deposits and payouts. Card funding has none. Two things to know: **the switch defaults to off**, so a user who never opens settings hears none of this, failed payouts included. And no 0902 item asked for it, so the board under-counts the backend's week again.

3. **The settings screen behind `walletActivity` has existed on mobile `main` since July. The spec describing it was wrong.** The client sends and reads exactly the fourteen fields the server uses: camelCase on `PATCH`, either case on read. `openapi.yaml` described a five-field shape the server dropped on 4 Aug, the day before the spec was written. Anyone generating a client from the spec would have got a preferences model that matches nothing. The schema is now corrected (`NotificationPreferences` for the response, `UpdateNotificationPreferencesRequest` for the body), and `suggestions.md` §5.4 records it as the latest case for generating the spec from the running app.

**If you read nothing else:** 0902 ends tomorrow with no reviewer, no successor sprint and three review items not backed by code on `main`. The backend kept shipping: #71 adds wallet-movement pushes, but they are off by default and nothing on the board tracks them. This report had been wrong for three editions about `BVA-I313`, whose screen has existed all along.

---

## 1. Board movement

### 1.1 Sprint 0902

**25 items: 21 leaves + 4 parents.** All figures are leaves unless stated. Against the 13 Oct scratch export, the CSV differs only in its `Date` preamble line, and the activity sidecar is byte-identical. **No audit entry of any kind falls in the window**: no status change, comment, reopen, completion, re-assignment or edit.

| Status | 13 Oct | 14 Oct | Δ |
|---|---:|---:|---:|
| To do | 0 | 0 | 0 |
| In progress | 4 | 4 | 0 |
| REVIEW/QA | 15 | 15 | 0 |
| BLOCKED | 1 | 1 | 0 |
| Done | 1 | 1 | 0 |
| **Total leaves** | **21** | **21** | **0** |

The last 0902 action is still `BVA-I307` (BLOCKED → In progress, David, 13 Oct 09:06:47 UTC). The 13 Oct edition's end-of-run recheck found nothing after its cut-off, and today's export confirms it.

### 1.2 Sprint 0901, 0901-admin and 08-01

All three are static, and their sidecars are byte-identical to 13 Oct's. 0901's last entry is still the 30 Sep sweep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change.

---

## 2. Sprint 0902 at day 15

| Block | Leaves | State | Code |
|---|---:|---|---|
| Push notifications (`BVA-I306`–`I313`) | 8 | **4 REVIEW/QA** (`I306`, `I308`, `I310`, `I312`), 3 In progress (`I307`, `I309`, `I313`), **1 BLOCKED** (`I311`) | `I306` and `I312` on `main` (PR #44). `I308`/`I310` server halves on `main` (#64, #65). `I307`: every push tap still opens Home. `I309`: on `origin/BVA-I316`, contract mismatch (§3.3). **`I313`: screen and wiring on `main` since July** (correction, below). `I311`: the server sends neither push it displays |
| Activity tab (`BVA-I314`–`I316`) | 3 | design Done, backend `I315` REVIEW/QA, screen `I316` REVIEW/QA | Feed on `main` (#66). Screen on `origin/BVA-I316` only |
| Appearance (`BVA-I318`–`I329`) | 9 | all 9 REVIEW/QA | On `main` (PR #43) except `I324`'s chat-background application (branch only). `I319`, `I325`, `I328` have no server code |
| Carried bug `BVA-I286` | 1 | In progress, **13.9 d** | not identified on any branch |

**`BVA-I313`, re-read from the code.** The ticket asks for three things:

| Ticket asks | On `main` |
|---|---|
| Build the screen from design, with per-category toggles for *Messages*, *Calls*, *Money & Wallet* and *Account & Verification* | **A screen exists** with Messages, Voice calls, Video calls, Money received, Money sent, Money requests, Wallet activity, Security alerts and Product updates, plus notification sound, ringtone, message tone, vibration and keyboard sounds. Whether it matches Philip's design cannot be judged from code. **No *Account & Verification* category exists on the server.** `NOTIFICATION_CATEGORIES` (db-schema) has nine, and none covers account status or KYC results |
| Wire each toggle to the backend's preference endpoint | **Done.** `NotificationService.getPreferences`/`updatePreferences` call `GET`/`PATCH /notifications/preferences` with the server's exact camelCase keys |
| Reflect stored state on load, including defaults | **Done.** The client's fallbacks match the server's defaults, including `walletActivity` and `keyboardSounds` off |

So `I313` is not "no screen". At most it is a regrouping to the new design, plus a server category that `I311` also needs. That is the same gap: account-status and verification pushes that nothing sends.

**One day remains** (15 Oct). Four leaves are in progress and one is blocked, with no estimates to say what fits. **Zoho lists no sprint after 0902.**

---

## 3. Code, API surface and spec drift

**Audit: clean at route level.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-14`): `beevia-api` 139/139, `beevia-admin-api` 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. It was re-run clean after this edition's spec edit. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin). They were not acted on.

### 3.1 `beevia-api` #71: wallet-movement pushes

`origin/main` moved `b091cb3` → **`f836b91`**: PR #71, `feat/wallet-activity-notifications`. `Phoenixdadhev` committed it on 13 Oct, 17:15–17:33 UTC, and Ayomikun merged it at 17:43 UTC. Four commits: the feature, a lint fix in a test, and two dependency refreshes (patch-level only: Nest 12.1.3, drizzle-orm 0.45.4, socket.io 4.8.4, zod 4.6.7, pnpm 12.11.2). No route, controller or DTO changed.

| Event | Fired from | Guard |
|---|---|---|
| `topupSucceeded` / `topupFailed` | `TopupService.finalize` (webhook and client verify share it) | Non-pending intent returns early |
| `depositReceived` | `AnchorWebhookService`, after the ledger credit | Webhook event-id dedupe (`partnerWebhookEvents`) |
| `withdrawalCompleted` / `withdrawalFailed` | `BankTransferService.complete`/`fail` (webhook, poll and sweep converge here) | Non-pending transfer returns early. Failure push only if the reversal succeeded |
| `cardFunded` / `cardWithdrawn` / `cardFundingFailed` / `cardWithdrawalFailed` | `CardFundingService.complete`/`failTransfer` | As above. Copy depends on `direction` |

Every send is wrapped so that a push failure can never fail the money path. All nine go through `fanOut()` under the `walletActivity` category, whose default is **off** (`NOTIFICATION_CATEGORY_DEFAULTS`, db-schema). The server's DTO describes it as "Balance and statement activity. Off by default", which predates #71. Now that the category includes a failed-payout notice, the default deserves a deliberate decision. Minor: the `amount` string is `NGN 2500.00` (`toFixed(2)`), not the `NGN 2,500.00` the code comment shows.

**Client side.** The payload is a sixth `data.kind`, `wallet.update`, now added to the `api-rfc.md` §5.13 table. The client shows the visible `notification` block like any other push, and a tap opens Home, as for every kind until `I307` lands. No client change is required for the pushes to appear.

### 3.2 `openapi.yaml`: the preferences schema, corrected

| | Before (since 5 Aug) | Now |
|---|---|---|
| `NotificationPreferences` (response) | `chat`, `calls`, `payments`, `security`, `system` | 14 snake_case fields: nine categories (`messages` … `product_updates`), three tone strings, `vibration`, `keyboard_sounds`, with the defaults stated |
| `PATCH` request body | the same response schema | new `UpdateNotificationPreferencesRequest`: the 14 camelCase fields, `minProperties: 1`, tone strings 1–64 chars |

The five-field shape was the server's 11 Jul version. Commit `3710fdf` replaced it on 4 Aug, and the spec was written on 5 Aug from the older shape. No route changed, so no audit since has seen it. The `beevia-api` Swagger DTO (`UpdatePreferencesDto`) has been right throughout, which is the argument of `suggestions.md` §5.4 again.

### 3.3 Pipelines and the standing checks

- **No workflow file changed** in any backend repo. In `beevia-api`'s `release.yml`, `sync` still runs without `needs: test`, so #71 reached production, if it deployed, ungated, like #70 the day before. `beevia-db-schema`'s latest tag is still `v0.0.40` (9 Oct).
- **`beevia-mobile`**: `main` unchanged at `4f9c29f` (8 Oct). No conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`. `ios/GoogleService-Info.plist` still tracked. The biometric step-up is still on `main` (`wallet_service.dart:78`) and the server's `stepUpSchema` still takes `{ pin }` only.
- **`origin/BVA-I316`** is unchanged (`500cdc6`, 13 Oct 14:02 UTC; 3 ahead, 2 behind `main`), unmerged, and still registers `pushProvider: 'voip'` (`call_kit_manager.dart:78`). The server still keeps one push token per device and has no APNs sender. The risk recorded on 13 Oct (`api-rfc.md` §5.15) is unchanged and has not materialised.
- **`beevia-admin`**: no commit since `0b41e35` (22 Sep), 21.9 days. **`beevia-admin-api`**: last change the 8 Oct dependency refresh.
- `PaymentService.activeNgn()` and `StubTranslateAdapter` unchanged. `22P02` still unmapped, and `payments.dto.ts` still has its own loose phone rule.

### 3.4 Document changes this cycle

- **`openapi.yaml`:** `NotificationPreferences` rewritten; `UpdateNotificationPreferencesRequest` added; the `PATCH /notifications/preferences` body now references it (§3.2).
- **`api-rfc.md`:** §5.13 gets a 14 Oct update: the `wallet.update` row, the `walletActivity` default, and the schema correction.
- **`suggestions.md`:** §5.4 gets a 14 Oct update recording the schema miss as the latest contract-drift case.
- `openapi.proposed.yaml`, `openapi.admin*.yaml`, `admin-api-rfc.md`: unchanged.

---

## 4. Risks

- **0902 closes tomorrow with no reviewer and no successor.** A bulk close would mark `I316`, `I324` (unmerged) and `I325` (no code) Done. Without 0903, carry-over has nowhere to go. The last gap (0901 → 0902) lasted eight days.
- **Merging `BVA-I316` unchanged would break pushes on iPhones** (§3.3). Unchanged since 13 Oct.
- **Wallet-failure notices are off by default** (§3.1). A product decision, not a defect, but currently made by a column default.
- **Every backend repo still deploys or migrates production on push without a test gate.** #70 and #71 both went out that way.
- **PII may be in production logs from before 12 Oct** (13 Oct edition §3.1). Not visible here.
- **Malformed path ids still return `500`** (`suggestions.md` §1.1).
- **`BVA-I311` is blocked on server work nobody has been asked for.** Now 5 days, no comment.
- **Firebase keys tracked and in history**, unrestricted as far as can be seen. **Production SSH open to any address**, per the 1 Oct deploy commits. Both unverified.
- **The biometric step-up on `main` fails against the real API** (`suggestions.md` §5.11).
- **The admin workstream is silent:** 21.9 days without a `beevia-admin` commit, 30.0 days without admin-board activity, no sprint.
- **The spec can be wrong where the audit cannot see.** Today's fix was found by reading a diff, not by any check (`suggestions.md` §5.4).
- **Three diverged local working trees** (`beevia-api`, `beevia-admin-api`, `beevia-db-schema`).

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points, and no item on any open sprint touches them. #71's card and wallet pushes serve existing NGN flows. `activeNgn()` is untouched.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. The 7-day window is 7 Oct 14:06 → 14 Oct 14:06 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Co-assigned items count for both owners.

### 6.1 Ayomikun Araoye: backend + admin API

**17 commits in 7 days**: 15 in `beevia-api` (#63–#71), one each in `beevia-admin-api` and `beevia-db-schema` (dependency refreshes). In this window: #71 (§3.1), committed and merged three hours after the previous edition's cut-off. No 0902 item covers it. All six of their 0902 leaves are in review, and their four 7-day submissions were all their own moves (`I308`, `I310`, `I315` on 8 Oct, `I325` on 12 Oct). No board action in the window. Median cycle time **0.99 d (n=16)**. `BVA-I8` has been In progress on the closed admin board for 30.0 days.

### 6.2 David Samuel: mobile

**2 commits on `main` in 7 days** (8 Oct, PR #44) **and 3 on `origin/BVA-I316`** (9, 12 and 13 Oct). Nothing pushed, and no board action, since 13 Oct 14:02 UTC. Of their seven 7-day submissions, one was their own move (`I329`, 9 Oct). Three were Ayomikun's (`I308`, `I310`, `I324`) and three board administration's (`I306`, `I312`, `I316`). WIP: `BVA-I286` **13.9 d** against a 0.98-day median, with no identifiable code. `BVA-I313`, 6.9 d, has its screen and wiring on `main` already (§2). The open question there is design fit, not absence. `I309` (2.0 d) and `I307` (1.2 d) are recent.

### 6.3 Philip Chidera: design

No board action since 2 Oct 14:18 UTC. `BVA-I321` has been in REVIEW/QA since 7 Oct, moved there by David. Open WIP is zero. Whether the existing notifications screen matches the design `I313` refers to is a question only design can answer.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **21.9 days** ago. The admin board has had no activity for 30.0 days, and `BVA-I9` has been In progress for all of it. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible here.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|
| 2026-W38 | 11 | — | | | |
| 2026-W39 | **42** | — | (most by board administration; see 29 Sep edition) | | |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | 4 | 1 | 5 |
| 2026-W42 (from Mon 12 Oct, 3 days) | — | **5** | 1 | 1 | 3 |

Acceptance is still zero. Over two and a half weeks the team submitted 15 leaves on 0902 and the review step took none. The bottleneck is not the developers.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more.
- **Work outside the board.** #71 is real delivery with no item. Board totals understate the backend's week, and the admin dashboard's whole workstream is likewise off the main board.
- **Who moved an item is not who did the work, or whether it is done.** `I316` and `I324` reached review with their code unmerged, and `I325` with none.
- **Branch commits are not delivery,** so they are counted separately.
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 13 Oct | Status on 14 Oct |
|---|---|
| **1. Fix or remove the VoIP token registration before `BVA-I316` merges** | ◐ **Holding.** The branch has not merged and is unchanged, so the risk has not materialised. Nothing addresses it yet |
| **2. Review before Thursday, `main`-backed items first; send `I316`/`I324` back; close `I319`/`I325`/`I328`** | ❌ **Not done.** No board action at all |
| **3. Create 0903 and decide carry-over; write the blockers on `I311`/`I307`** | ❌ **Not done.** No 0903, no comments |
| **4. Check production logs for pre-12 Oct PII** | ? **Not visible** |
| **5. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done.** #71 deployed ungated |
| **6. Map `22P02` to `400`** | ❌ **Not done** |
| **7. Restrict the Firebase API keys; untrack `ios/GoogleService-Info.plist`** | ❌ / ? Still tracked |
| **8. Make Flutter CI a required check** | ? **Not visible** |
| **9. Check the production host's SSH settings** | ? **Not visible** |
| **10. Hide the biometric option outside mock mode** | ❌ **Not done** |
| **11. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done** |
| **12. Open the admin board's next sprint, or say it is paused** | ❌ **Neither** |
| **13. Carried items** | ❌ **None moved** |

**None of thirteen done, one holding.** One day is a short window, and the backend's day went to #71 rather than to any of these.

---

## 8. What I would do this week

Re-ranked for 0902's last day.

1. **Today or tomorrow, create 0903 and move the open leaves into it**: `I286`, `I307`, `I309`, `I311`, `I313`. Do not close 0902 by sweep. Then set `ZOHO_SPRINT_FILTER` to `0903`, so the in-repo export stops reading 08-01.
2. **Review what is on `main` before the close**: `I306`, `I308`, `I310`, `I312`, `I315`, `I318`, `I321`, `I322`, `I327`, `I329`. Send `I316` and `I324` back to In progress until their branch merges. Close `I319`/`I325`/`I328` with a note, or open one backend item to extend `PATCH /users/me/settings`.
3. **Rescope `BVA-I313` against what exists.** Compare the current screen to the design, and write what is left on the item. If *Account & Verification* is to be a category, open the server item, which `I311` needs too.
4. **Decide the `walletActivity` default**, now that it gates failed-payout notices. Add a board item for #71's work so the board reflects it.
5. **Before `BVA-I316` merges, fix or remove the VoIP token registration** (`api-rfc.md` §5.15).
6. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
7. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4). Today's schema fix is the case for it.
8. **Check the production logs for PII from before 12 Oct.**
9. **Map `22P02` to `400`** (`suggestions.md` §1.1).
10. **Restrict the Firebase API keys and untrack `ios/GoogleService-Info.plist`** (`suggestions.md` §5.13).
11. **Make Flutter CI a required check on mobile `main`**, and confirm the Firebase secrets.
12. **Check the production host's SSH settings.**
13. **Hide the biometric option outside mock mode** (`suggestions.md` §5.11).
14. **Bring `payments.dto.ts` onto `phone.util.ts`.**
15. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
16. **Carried, unchanged:** comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin` (after it has any CI); the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs, `encryption-model.md` first; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 30.0 days ago**. Today's sidecar is byte-identical to 13 Oct's. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 30 days. **Zoho lists no successor sprint for this project.** `beevia-admin` has gone 21.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 66.76, unchanged)

**Target 2026-09-01 (provisional). The target date passed forty-three days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**No score moved.** #71 adds notifications to existing wallet, top-up and card flows. Notifications are not one of the rubric's capabilities, and the flows themselves are unchanged. The correction about `I313` does not move a score either, for the same reason: notification settings are not a rubric line.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change |
| 2 | Voice & video calling | 8 | 0.85 | 0 | CallKit on `origin/BVA-I316` only, and cannot ring against the current server |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged. #71's wallet pushes are notifications, not wallets |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | No change; biometric option still on `main` |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | Card funding gains pushes (#71); no card capability change |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **66.76** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether #70 or #71 is deployed**, or whether FCM is configured in production (`FCM_SERVICE_ACCOUNT`). Without it, every push goes to the stub adapter.
- **Whether the notifications screen matches the design** `I313` refers to. Designs are not in these repositories.
- **What blocks `BVA-I311`, or why the board was silent today.** No comment records either.
- **Whether anyone but the author reviewed any PR**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch export of sprint **0902** to `/tmp/beevia-scratch/0902/` (25 items, `--modified --activity`, exit 0). The three ran in parallel from about 14:02 UTC.
2. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia lists `0902, 0901, 08-01, 0702, 0701`; the admin project lists only `0901-admin`.
3. Fast-forward sync (step 2), exit 1. `beevia-mobile` and `beevia-admin` were already current on `main` (no branch switch). `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep). `ls-remote` confirmed each `origin/main` matched the fetched ref.
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-14`: clean, and clean again after the spec edit. The in-repo audit was run too, for the board section; its 23 drift lines are the known phantom. Both ran through `uv run --no-project --with pyyaml`.
5. Board comparison: `cmp` of every sidecar against 13 Oct's, and a CSV diff past the preamble. Flow analysis (`flow14.py`): cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none).
6. Content checks. In `beevia-api`: the whole #71 diff, `fanOut()` and the push producer's job-id dedupe, the Anchor webhook's event-id dedupe, the ledger's idempotent fast path, `release.yml`, `stepUpSchema`, `22P02`, the payments phone rule, and the notification-preferences DTO, service view and its history (`cdd3809`, `3710fdf`, `54f754a`). In `beevia-db-schema`: `NOTIFICATION_CATEGORIES` and their defaults, tags. In `beevia-mobile`: remote branches with ahead/behind counts, conflict markers, tracked Firebase files, the biometric call, the VoIP registration on `BVA-I316`, push-kind handling, and the notifications settings screen, its service and its model.
7. `openapi.yaml`, `api-rfc.md` and `suggestions.md` updates (§3.4).
8. This report and its web edition.
9. End-of-run recheck from about 14:11 UTC. All three exports were re-run (exit 0 each), and every activity sidecar was byte-identical to the first run's. `origin/main` was unchanged in all five repos, and the sync again exited 1 on the same three `diverged` repos. The shadow audit was rebuilt from scratch (`/tmp/beevia-shadow-2026-10-14b`) and was clean. The `NotificationPreferences` edit was re-checked against `PreferencesView`, `UpdatePreferencesDto`, the db-schema column defaults and the snake_case response interceptor. Nothing in this report changed as a result.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `git archive`, `ls-remote` and read-only `log`/`show`/`diff`/`grep`/`ls-tree`/`rev-list`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-14.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 14 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 0902 figures come from the scratch export.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** for all three exports. This is the known sampling artefact, not a scope gap. All 25 0902 items are genuinely unassigned.
- **Sprint 0901 was not re-exported.** It is closed, and its 5 Oct scratch export shows no action since 30 Sep.

**Window.** 13 Oct 14:03 UTC → 14 Oct 14:02 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
