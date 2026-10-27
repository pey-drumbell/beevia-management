# Beevia — Project Status

**As of 2026-10-27** · Sprint **1002** (21 Oct → 5 Nov, day 7 of 16): **new. 62 items, 43 leaves: 19 To do · 13 In progress · 10 REVIEW/QA · 0 BLOCKED · 1 Done** · Sprint **0902** (30 Sep → 15 Oct): swept on 21 Oct, 8 items left on it, all Done · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-27.csv` + `beevia-activity-2026-10-27.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-27.csv` + its activity sidecar (12 items, sprint 0901-admin); read-only scratch exports of sprint **1002 (62 items)** in `/tmp/beevia-scratch/1002/` and sprint **0902 (8 items)** in `/tmp/beevia-scratch/0902/`, the latter diffed against the 20 Oct file in the same folder; the 19 Oct scratch export of sprint **0901 (76 items, closed and static)** for cycle times. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 20 Oct 14:02 UTC → 27 Oct 15:55 UTC, 7.1 days (Tue → Tue).** No edition was written between 21 and 26 Oct, so this one covers a full week.

---

## Quick overview

> **The iOS call defect this report led with a week ago was fixed on the server within four days, and the board was reset. iPhones can now be rung over PushKit with their FCM token left alone, at least on a reading of the code. 0902 was closed without a review: 7 items were swept to Done and 15 leaves were taken off the sprint. A new sprint, 1002, holds 43 leaves of wallet, card and Help & Support work. After six days, 10 of its leaves are in REVIEW/QA. Only one of those 10 matches code written this week. Three are mobile screens with no code on any branch.** The board is describing work again, which it had stopped doing. But it is again counting a move to REVIEW/QA as delivery, and nothing on 1002 has been reviewed.

| Metric | 20 Oct | 27 Oct | Δ |
|---|---:|---:|---|
| Live sprint | 0902 (ended 15 Oct, not closed) | **1002 (21 Oct → 5 Nov)** | successor created 20–22 Oct by board administration; named `1002`, not `0903` |
| Sprint 1002 items (leaves + parents) | — | **62 (43+19)** | 15 Help & Support leaves, 28 wallet/card leaves |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | — | **19 / 13 / 10 / 0 / 1** | |
| Sprint 0902 items | 25 (21+4) | **8 (6+2), all Done** | 7 REVIEW/QA → Done in one sweep (21 Oct 14:50–14:52 UTC). **15 leaves + 2 parents left the sprint**, to a destination the export cannot see |
| Transitions into REVIEW/QA, last 7 days (leaves) | 3 | **10** | 4 by the leaf's owner (all Ayomikun), **6 moved by Ayomikun on David's and Philip's items**, 0 by board administration |
| Owners' last submission of their *own* leaf | 14 Oct (David, `I286`) | **27 Oct 13:11 UTC** (Ayomikun, `I358`) | David's last own submission is still 14 Oct, **13.0 days** ago |
| Items accepted by a reviewer | 0 | **0** | the 7 that left review went by sweep; none of 1002's 10 has left review |
| 1002 REVIEW/QA leaves with matching new code | — | **1 of 10** | `I366` (statements, merged today). 3 mobile screens have **no code on any branch**; 2 backend items map to endpoints shipped in August; 1 backend item has no identifiable change; 3 are design (not visible in git) |
| Call defects from 20 Oct still open | 3 | **1** | VoIP token clash: **fixed server-side** (#81 + db-schema #22). Light-mode mic: **fixed** (PR #52). `call.ended` push: **still unhandled** |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | 7 api merges and 2 db-schema releases went out that way |
| API surface (consumer / admin) | 139 / 49 | **141 / 49** | +2: `POST /statements`, `GET /statements` |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **2 found → 0** | statements added; 4 operations and 3 schemas updated in place (§3.5) |
| `beevia-mobile` days since a commit on `main` | 1.0 | **5.3** | PR #52, 22 Oct. Branch `BVA-I330` (Help & Support) was last pushed 0.3 days ago |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.9 / 12.3 / 11.1 | **0.1 / 19.3 / 0.1** | api: 7 merged PRs (#76–#84); db-schema v0.0.41, v0.0.42 |
| `beevia-admin` days since a commit | 27.9 | **35.0** | |
| Admin board: open sprint / days since any activity | none / 36.0 | **none / 43.0** | two admin-dashboard Stories now sit on the *main* board, unassigned (§2.3) |
| Estimation points set (1002 / 0902 / 0901 / 0901-admin / 08-01) | — · 0/25 · 0/76 · 0/12 · 0/64 | **0/62** · 0/8 · 0/76 · 0/12 · 0/64 | |
| MVP readiness (estimate) | ≈67% (66.76) | **≈67% (67.32)** | **+0.56**: line 2 (calling) 0.85 → 0.92, both platforms now ring a closed app (appendix) |

**Correction to 20 Oct.** That edition called the VoIP token registration on mobile `main` "the highest-priority item on the project" and said iPhones "probably lose push delivery", because the VoIP token would overwrite the FCM token in the device's one slot and then be pruned. Production evidence says otherwise. `beevia-api` #81's commit (24 Oct) reports **9 stored tokens, all `fcm`, not one `voip`**. The FCM sync was winning the race for the slot, so the token that got lost was the VoIP one, not the FCM one. iPhones most likely kept receiving ordinary pushes all along. The real defect was the inverse: the server never held a token it could ring iOS with. Both are fixed now (§3.1). The 20 Oct edition's reading was plausible from the code, but it got the direction of the failure wrong, and its first recommendation ("stop the VoIP registration today") would have been the wrong fix.

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (10 To do, 4 In progress, 4 REVIEW/QA) · 0901-admin: 1 In progress | **4 own** (+6 moves on teammates' items) | 0.99 d (n=17) | 4 Help & Support items: `I332` (5.2 d), `I335` (4.1 d), `I338`, `I347` (1.0 d) · `BVA-I8` on 0901-admin (**43.0 d**) | **10** (8 `beevia-api`, 2 `beevia-db-schema`) | Shipped the iOS ring path, statements and block state. **None of the four In-progress support endpoints has a branch on `beevia-api`** |
| David Samuel | mobile | **1002: 16** (6 To do, 7 In progress, 3 REVIEW/QA) · 0902: 3 Done by sweep | 3 (**0 own**, 3 moved by Ayomikun) | 0.99 d (n=37) | 7 items: `I331`, `I354` (**5.2 d**), `I334` (4.1 d), `I337`, `I346`, `I383`, `I386` (1.0 d) | **1 on `main`** (via PR #52) · **3 on `BVA-I330`** | **Their three REVIEW/QA items (`I365`, `I369`, `I376`) have no code on any branch.** Help & Support screens exist on `BVA-I330`, on placeholder data |
| Philip Chidera | design | **1002: 7** (2 To do, 1 In progress, 3 REVIEW/QA, 1 Done) | 3 (0 own, 3 moved by Ayomikun) | 0.94 d (n=4) | `I360` (1.0 d) | n/a | Back on the board on 22 Oct after 20 days. Completed `I356` themself (In progress → Done, 4.0 d) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**43.0 d**) | **0** | `beevia-admin` **35.0 days** without a commit. 1002 has two admin-dashboard Stories (Support Inbox, FAQ CMS), unassigned, with no dashboard task under either |

**The three questions for standup:** (1) **Where is the code for `I365`, `I369` and `I376`?** They are the statement, manage-card and delete-card screens, and they sit in REVIEW/QA. If they have not been started, move them back to To do, so the queue means what it says. (2) **What happened to 0902's 15 leaves?** They include `I309` (CallKit, In progress), `I311` (BLOCKED) and 13 items that were in review. They are not on 1002, not Done, and not on any listed sprint. Were they accepted, dropped, or parked in the backlog? (3) **Is there an agreed contract for Help & Support?** Mobile is building FAQ, dispute and support-chat screens against placeholder data (`TODO(support-api)`), and four backend support items have been In progress for 1–5 days with no server branch. The only support design on file is `openapi.proposed.yaml`'s `/support/tickets`, which does not match the board's FAQ and dispute model.

**The three things worth knowing:**

1. **Both platforms can now ring a closed app, on the code and on the author's word.** `beevia-db-schema` #22 (v0.0.41, 23 Oct) gave each device its own `voip_token`. `beevia-api` #79 (23 Oct) added an APNs VoIP transport that talks to Apple directly over HTTP/2, and #81 (24 Oct) routes iOS rings to it. The FCM token is left untouched. #81's message says the credentials were validated against Apple. #79 also fixed the silent pushes, which now go out as `background` at priority 5, so last week's recommendation 11 is done. #76 (ring expiry, 20 Oct), #77 (real caller and sender names, 21 Oct) and #78 (one live call per conversation, after one double-tap made five calls, 23 Oct) round out the server side. On the client, mobile PR #52 (22 Oct) renders `call_event` cards, subscribes the Activity screen to `activity.updated`, and fixes the light-mode mic. **One gap is left:** neither push handler consumes `call.ended`, so a ring on a device without a live socket ends only on the plugin's own timeout. No device was tested here.

2. **0902 was not reviewed. It was closed out in two moves, and 1002 is already repeating the pattern.** At 14:50 UTC on 21 Oct, board administration swept 0902's last 7 REVIEW/QA items to Done within two minutes. That includes `I286` with its "Transactions History" rename still not done ("Payment History" on `main`), and `I319`/`I328`, the backend preference-storage items, with no server code. The other 15 leaves, 13 of them in review, left the sprint. On 1002, 6 leaves went **To do → REVIEW/QA directly** in a 14-second batch on 23 Oct. On 27 Oct, 3 more went In progress → BLOCKED → REVIEW/QA in six seconds, and `I358` went straight from To do a minute later. Ayomikun made all 10 moves, on their own items and on David's and Philip's. Read against the code: the statements backend (`I366`) merged today. The card freeze and terminate endpoints (`I370`, `I377`) have existed since August. `I358` has no matching change. The three mobile screens have nothing. **The queue is being used as a planning column, not as "built, please verify".** That is a process question for the whole team, not a judgement on whoever moved the items.

3. **New server surface this week: statements and block state.** `POST /statements` (202, emailed PDF or CSV) and `GET /statements` shipped today. They are in `openapi.yaml` now. Two design points are open: the PDF's password is the user's phone number, and delivery is email-only (`suggestions.md` §4.8). Blocking now refuses calls (`403 blocked`) and is reported to the blocker as a directional `blocked` flag. Payments were left out on purpose, so a blocked user can still send a money request (`suggestions.md` §4.9). None of this moves the PRD's four structural gaps: FX, international KYC, consent and multi-currency are untouched.

**If you read nothing else:** the iOS call path went from broken to complete in a week, and the 20 Oct edition's worst fear did not happen. The board now has a sprint again. But its review column is being filled ahead of the code, and nothing has been reviewed since 30 Sep.

---

## 1. Board movement

### 1.1 Sprint 0902: swept and emptied

**25 items on 20 Oct, 8 today (6 leaves + 2 parents), all Done.**

| What happened | Items | When | By |
|---|---|---|---|
| REVIEW/QA → Done (`Item Completed`) | `I286`, `I317` (parent), `I318`, `I319`, `I326` (parent), `I327`, `I328` | 21 Oct 14:50:48–14:52:51 UTC | board administration |
| Already Done | `I314` | 2 Oct | Philip |
| **Left the sprint** | **15 leaves**: `I306`, `I307`, `I308`, `I310`, `I312`, `I313`, `I315`, `I316`, `I321`, `I322`, `I324`, `I325`, `I329` (REVIEW/QA), `I309` (In progress), `I311` (BLOCKED); **2 parents**: `I320`, `I323` | not visible | not visible |

The 17 that left are not on 1002 and not on any sprint Zoho lists for the project (`1002, 0902, 0901, 08-01, 0702, 0701`). 1002's own items were all "moved from Backlog", so the backlog is the likely destination. The export reads sprints only, though, so this cannot be confirmed here. **This is a close, not acceptance.** The sweep marked `I286` Done without its label rename, and `I319`/`I328` Done with no theme or text-size storage anywhere in `beevia-db-schema` or `beevia-api`. Whether the 13 review items that left were accepted, dropped or parked is the standup question.

### 1.2 Sprint 1002: new

**62 items: 43 leaves + 19 parents**, every one created by board administration between 20 Oct 11:32 and 22 Oct 14:11 UTC and moved in from the backlog on 21–22 Oct. Every leaf is a Task, no item has an epic or estimation points, and two leaves are `Unassigned` (`I348` *Triage Flow Configuration*, In progress; `I390` *Build Card Transactions Screen*, To do).

| Block | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Help & Support (`I330`–`I352`): home, FAQ, article feedback, report an issue, dispute history, support chat, admin support inbox, admin FAQ CMS | 15 | 6 | 9 | 0 | 0 |
| Wallet & card (`I353`–`I391`): more-options sheet, wallet details, limits & tier, statements, manage/freeze card, card spending from wallet, delete card, "verify it's you", card details, card limits, card transactions | 28 | 13 | 4 | 10 | 1 |
| **Total** | **43** | **19** | **13** | **10** | **1** |

**After the cut-off**, at 15:57 UTC, board administration added `BVA-I392` *Activity Screen – Verification Checklist* (To do, all three team members, with an attachment). It is outside this report's counts (appendix, step 9).

**Movement in the window (leaves):** 31 status transitions. Ayomikun made 15 (6 on their own items, 9 on teammates'), David 8 (3 on Ayomikun's items and 1 on the unassigned `I348`), Philip 5 plus one completion, and board administration 2 (`I383`, `I386` to In progress, 26 Oct). No comment, reopen or real block was recorded. The BLOCKED entries on 27 Oct (three leaves and their parent `I363`) each lasted six seconds, the routing pattern this board has used since 6 Oct.

### 1.3 Sprint 0901, 0901-admin and 08-01

All static. The 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep respectively. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01.

---

## 2. Sprint 1002: what is in review, and whether the code exists

### 2.1 The ten REVIEW/QA leaves, checked against the code

| Leaf | Owner | How it got to REVIEW/QA | Code |
|---|---|---|---|
| `I366` Statement generation & email delivery | Ayomikun | To do → In progress (Philip, 26 Oct) → BLOCKED → REVIEW/QA (Ayomikun, 27 Oct 13:10) | ✅ **`beevia-api` #84, merged 27 Oct 13:55 UTC**, with `beevia-db-schema` #23 (v0.0.42) |
| `I365` Build statement screen | David | same batch | ❌ **No statement code on any `beevia-mobile` branch** |
| `I364` Statement states & PDF layout | Philip | same batch | design; not visible in git |
| `I370` Card summary & freeze endpoints | Ayomikun | **To do → REVIEW/QA** (Ayomikun, 23 Oct 13:01) | `freeze`/`unfreeze`/`GET /cards/{id}` have existed since 27 Aug; **no card change this window** |
| `I369` Build manage card screen | David | **To do → REVIEW/QA** (Ayomikun, same second) | ❌ **No freeze/unfreeze call on any branch**; `main` only lists and issues cards (`wallet_service.dart:14`, `:139`) |
| `I368` Manage card layout & frozen state | Philip | **To do → REVIEW/QA** (Ayomikun) | design; not visible |
| `I377` Card termination endpoint | Ayomikun | **To do → REVIEW/QA** (Ayomikun, 23 Oct 13:00) | `POST /cards/{id}/terminate` has existed since 27 Aug; no change this window |
| `I376` Build delete card confirmation | David | **To do → REVIEW/QA** (Ayomikun) | ❌ **No terminate call on any branch** |
| `I375` Delete confirmation & wallet without a card | Philip | **To do → REVIEW/QA** (Ayomikun) | design; not visible |
| `I358` Wallet account details endpoint | Ayomikun | **To do → REVIEW/QA** (Ayomikun, 27 Oct 13:11) | no wallet change this window; the item may describe `GET /wallets/payin-details` (August), which cannot be confirmed from the title |

**One of ten matches new code.** Two more match endpoints that already existed, which is a legitimate "nothing to build" outcome if that is what the items meant, but the board does not say so. Three mobile items have nothing behind them. Seven of the ten never passed through In progress. None has a comment.

### 2.2 In progress

| Leaf | Owner | Age | Code |
|---|---|---:|---|
| `I331` Help & Support home screen | David | 5.2 d | `origin/BVA-I330`: `help_support_screen.dart` |
| `I334` FAQ screens | David | 4.1 d | `faq_screens.dart` on the branch |
| `I337` FAQ yes/no feedback | David | 1.0 d | on the branch |
| `I346` Support chat screen | David | 1.0 d | `support_chat_screen.dart` on the branch |
| `I354` Wallet "more options" sheet | David | 5.2 d | not found on any branch |
| `I383` Card details screen, `I386` card limits screen | David | 1.0 d | moved by board administration; not found |
| `I332` Open dispute count, `I335` FAQ content API, `I338` article feedback, `I347` support conversation endpoints | Ayomikun | 5.2 / 4.1 / 1.0 / 1.0 d | **no branch on `beevia-api` other than `main` and the merged `feat/expose-block-state`**; nothing support-related on `main` |
| `I348` Triage flow configuration | **Unassigned** | 1.0 d | — |
| `I360` Highest-tier state & upgrade entry | Philip | 1.0 d | design |

`origin/BVA-I330` (3 commits, 23–27 Oct, 38 files, +4,378/−73) holds the Help & Support screens, models, provider and service, plus l10n in four languages. **`SupportService` is entirely placeholder data**: its header says `TODO(support-api): the support endpoints aren't available yet, so every method here is served from in-memory placeholder data`. The branch also touches the call provider, `local_message_store.dart` and `conversation_provider.dart` (+147 lines) outside the support feature.

### 2.3 Off-scope signals on 1002

- **Admin-dashboard work is on the main board.** `I349` *Admin Dashboard: Support Inbox* and `I351` *Admin Dashboard: FAQ Content Management* are unassigned Stories whose only children are Ayomikun's API tasks (`I350`, `I352`). There is no dashboard UI task, and Promise has no 1002 item. The admin board itself has no sprint.
- **`I381` *PIN & Biometric Verification Endpoint*** (To do) is the server half of the biometric step-up that the client already offers and the server rejects (`suggestions.md` §5.11). It is the first board item that could close that gap.
- **`I372` *Card Payments Against the Wallet Balance*** (To do) would change how virtual cards are funded, which touches MVP line 9.

---

## 3. Code, API surface and spec drift

**Audit: two routes in code and not in the spec, now zero.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-27`), the first run found `GET /statements` and `POST /statements` undocumented (`beevia-api` 141 in code, 139 in spec). After this cycle's edits it is clean: 141/141, admin 49/49, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its known phantom lines from the three `diverged` working trees (8 consumer + 15 admin "in spec, not in code"). Those were not acted on.

**Three `main` branches moved.**

| Repo | From → to | What |
|---|---|---|
| `beevia-api` | `49c0683` → `9290c99` | 7 merged PRs (9 commits), 46 files, +2,880/−120: #76 ring expiry (20 Oct 14:14 UTC), #77 caller/sender names (21 Oct), #78 one live call per conversation, #79 APNs headers + VoIP transport (23 Oct), #81 route iOS rings to PushKit (24 Oct), #83 block state (27 Oct 13:01), #84 statements (27 Oct 13:55). All authored as `Phoenixdadhev`, merged as `Ayomikun Araoye`. #80's commit `314a71b` landed through #79; there is no #82 ref |
| `beevia-db-schema` | `40ecf69` → `21dbd73` | #22 `devices.voip_token` (v0.0.41, 23 Oct 16:51 UTC); #23 `statement_requests` + three enums (v0.0.42, 27 Oct 13:49 UTC). Migrations `0038`, `0039` |
| `beevia-mobile` | `31a77e8` → `ccb4f63` | PR #52 (22 Oct 09:34 UTC, a true merge of `BVA-I316` at `8039bd7`, "fixes and updated changes"): 32 files, +1,292/−494 |

`beevia-admin-api` (`c59460a`, 8 Oct) and `beevia-admin` (`0b41e35`, 22 Sep) did not move. **No PR is open on any backend repo.** Open mobile work: `origin/BVA-I330` (no PR ref yet), plus Dependabot PRs #45, #47, #50 and #51, all unchanged.

### 3.1 Calls: the server half of last week's fix list is done

Full detail in `api-rfc.md` §5.15 (2026-10-27 update).

| | Android | iOS |
|---|---|---|
| App backgrounded or killed | Native ring from the data-only FCM push, with the caller's name (unchanged since #74) | **VoIP push over APNs → PushKit → CallKit** (#79 + #81 server, `AppDelegate.swift` client). Falls back to the FCM push if the device has no VoIP token yet |
| Push token | FCM | **FCM and VoIP stored apart** (`devices.voip_token`, db-schema v0.0.41). Dead-token pruning clears only the token that died |
| Silent pushes (`call.ended`, FCM `call.incoming`) | — | `apns-push-type: background`, priority 5 (was 10 with no type, #79) |
| Ring dismissed when the call ends | Socket `call.update`; else the plugin's 30 s timeout. **`call.ended` push still ignored** | Same. Server ring expiry (#76) ends abandoned calls 60–75 s in |
| Call history in the thread | **`call_event` cards rendered** (PR #52) | same |

What makes this checkable is the commit messages: #79 cites a real-device test ("a visible alert push to a closed iOS app arrives, the silent call push does not"), #81 cites the production token table and an APNs credential check, and #78 cites a production incident (five calls in 23 s). None of it was tested here.

### 3.2 Mobile `main`: PR #52

| Landed | Note |
|---|---|
| `call_event` messages parsed (`call_event_data.dart`) and rendered as cards and previews (`conversation_provider.dart:426`, `:480`) | Closes 20 Oct's "server writes cards the client discards" |
| Activity screen subscribes to `activity.updated` (`activity_events.dart`) | Closes the open half of rec. 9 on the client |
| Caller name from the cached conversation list when a push has none (`call_kit_manager.dart`) | Defensive; #74/#77 already send `callerName` |
| Light-mode mic: the `colorFilter` now applies only in dark mode (`chat_widgets.dart:1108–1113`) | Closes rec. 5 |
| iOS `xcconfig`/`Podfile` changes, chat details refactor (710 lines), wallet and card-request widget edits | Off-board |

`main` has no conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`. The VoIP registration (`call_kit_manager.dart:84`, run from `bootstrap.dart:114`) is unchanged, and is now the correct behaviour. The biometric step-up is unchanged (`wallet_service.dart:78`).

### 3.3 New server surface

- **Statements** (`beevia-api` #84 + db-schema #23). `POST /statements` takes `type` (`wallet`/`card`), the subject id, an inclusive UTC date range and `format` (`pdf`/`csv`). It returns `202` with `{id, status, delivered_to, transaction_count}` and builds and emails the file in a BullMQ job. Refusals come before queueing: `no_transactions`, `period_too_large` (> 5,000), `email_required`, `rate_limited` (3 per rolling day). `GET /statements` lists the last 50 requests. The PDF is AES-256 with the **phone number as password** (`suggestions.md` §4.8). The table is an audit record, and the file is not kept.
- **Block state** (#83). `ContactProfile.blocked` and `Conversation.peers[].blocked` are directional (true only when the viewer blocked). `POST /conversations/{id}/calls` refuses a blocked direct pair with `403 blocked`. **Payments deliberately do not check blocks** (`suggestions.md` §4.9). The client does not read `blocked` yet, so the contact profile still offers "Block" to someone already blocked.
- **One live call per conversation** (#78): a repeat tap returns your own call with a fresh token; the other side's live call gives `400 call_already_in_progress`.

### 3.4 The standing checks

- **Pipelines:** no workflow change on any backend `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`". `beevia-db-schema`'s Release runs on push with no `needs:`, and its Sync migrates production after Release (v0.0.41 and v0.0.42 went out that way, the latter 1 min after its merge). `beevia-admin-api` unchanged.
- `PaymentService.activeNgn()` (`payment.service.ts:79`, `:138`) and `StubTranslateAdapter` (`translate.module.ts:23`) are unchanged. `22P02` is still unmapped. `messages.ref_id` still has no index.
- **Dependabot (mobile):** #51 (`pub-minor-and-patch`, including `flutter_local_notifications` ^19 → ^22) is still open and unchanged.

### 3.5 Document changes this cycle

- **`openapi.yaml`** (139 → 141 operations): added `requestStatement` and `listStatements` under a new `Statements` tag, with schemas `RequestStatementRequest`, `StatementAccepted`, `StatementRequest`. Updated in place: `ContactProfile` (`blocked`), `Conversation.peers` (`blocked`), `startCall` (PushKit ring, one live call, `403 blocked`, APNs headers, name fallback), `endCall` (server ring expiry, idempotent end/decline), `registerPushToken` (two tokens per iOS device; **its `200` body was documented as a `Device` but has been `{device_id, registered}` since 11 Jul**, now corrected), `RegisterTokenRequest.pushProvider`. The `Cards` tag no longer says "Entirely proposed".
- **`api-rfc.md`**: header and §3 totals (141), a Statements row, §6.8 rows, a 2026-10-27 update to §5.15 (including the correction above), and a new §5.16 (statements and block state).
- **`suggestions.md`**: new §4.8 (statement PDF password) and §4.9 (blocks do not reach payments).
- `admin-api-rfc.md`, `openapi.proposed.yaml` and both admin specs: no change needed.

---

## 4. Risks

- **The review column no longer means "built".** Three of 1002's ten REVIEW/QA leaves have no code anywhere, and seven skipped In progress. If 1002 is closed the way 0902 was, by sweep, those three will be recorded as delivered.
- **0902's 13 un-reviewed REVIEW/QA leaves left the sprint with no visible decision**, along with `I309` (In progress) and `I311` (BLOCKED, never explained). Work that was waiting on review may now be invisible on every board.
- **Help & Support is being built from both ends with no shared contract.** Mobile uses placeholder data. The server has no support code on any branch. The only design on file (`/support/tickets`, proposed) does not match the board's FAQ and dispute model.
- **Statement PDFs are protected by a non-secret** (the phone number), and statements leave the app by email (`suggestions.md` §4.8).
- **A blocked user can still send money requests** (`suggestions.md` §4.9).
- **`call.ended` is still unconsumed**, so a ring on a device without a live socket ends only when the plugin times out. With VoIP rings now reaching closed iPhones, this is the remaining stale-ring path.
- **Every backend repo still deploys or migrates production on push without a test gate.** This week that was 7 api merges and two schema releases, one 1 min after merge.
- **The admin workstream is silent and now partly on the wrong board:** 35.0 days without a `beevia-admin` commit, 43.0 without admin-board activity, and two dashboard Stories unassigned on 1002.
- Carried, unchanged: wallet-failure notices off by default (undecided); possible pre-12 Oct PII in production logs (not visible); malformed path ids return `500` (`suggestions.md` §1.1); production SSH open to any address per the 1 Oct deploy commits (unverified); the biometric step-up on `main` fails against the real API (§5.11; `I381` may address it); Firebase keys in history; three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps carry 32 of the rubric's 100 points: international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired. None of 1002's 43 leaves touches FX, international KYC or consent. Statements, block state and Help & Support are real product work, but none is a PRD MVP capability on the rubric. `I372` (card spending from the wallet) and `I381` (biometric verification) are the two 1002 items nearest to scored lines.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 20 Oct 15:55 → 27 Oct 15:55 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Open-branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Cycle times use 0901, 0902 and 1002.

### 6.1 Ayomikun Araoye: backend + admin API

**10 commits in 7 days**: 8 in `beevia-api` (the whole iOS ring path, ring names, the one-call guard, block state, statements) and 2 in `beevia-db-schema` (`voip_token`, `statement_requests`). The commit messages remain the best evidence on the project: each states what production showed and which test fails if the change is reverted. **4 own submissions** (`I370`, `I377` on 23 Oct; `I366`, `I358` on 27 Oct). They also moved 6 of David's and Philip's items to REVIEW/QA. Median cycle **0.99 d (n=17)**. WIP: four Help & Support endpoints (`I332` 5.2 d, `I335` 4.1 d, `I338`, `I347` 1.0 d), with no support branch on `beevia-api`. Local work would not be visible here. `BVA-I8` has been In progress on the closed admin board for 43.0 days. Ayomikun also holds the API tasks under both admin-dashboard Stories (`I350`, `I352`). None of #76–#83 has a board item. That is unchanged from last week, and it is a process gap, not an individual one.

### 6.2 David Samuel: mobile

**1 commit on `main`** (`8039bd7`, 21 Oct, landed by PR #52 on 22 Oct) and **3 on `origin/BVA-I330`** (23–27 Oct, the Help & Support screens). **Zero own submissions**: their last was `I286` on 14 Oct, **13.0 days** ago. Their three 7-day "submissions" are Ayomikun's moves of `I365`, `I369` and `I376`, none of which has code. Median cycle **0.99 d (n=37)**. WIP: **7 items**, the most on the board. `I331` and `I354` are at 5.2 d, past their median, though `I331` has visible branch work. The board can't show whether seven parallel items is a plan or a backlog. Ask, don't assume. The REVIEW/QA items under their name that have no code are a board-hygiene question about who moves items. They are not evidence about David's output.

### 6.3 Philip Chidera: design

Back on the board on 22 Oct 15:07 UTC, their first action since 2 Oct (20.0 days). They moved `I356` to In progress that day, and `I360`, `I364`, `I365` and `I366` on 26 Oct. They completed `I356` (*Wallet Details Before the Account Exists*) themself on 26 Oct, In progress → Done in 4.0 days. That is the only 1002 completion. Three design items are in REVIEW/QA (`I364`, `I368`, `I375`), all moved by Ayomikun. WIP: `I360` (1.0 d). Design output is not visible in git, so the board is the only record. It now says more than it has in three weeks.

### 6.4 Promise Udo: admin dashboard

**No commit in the window.** The last was `0b41e35` on 22 Sep, **35.0 days** ago. The admin board has had no activity for 43.0 days, and `BVA-I9` has been In progress for all of it. 1002 adds two admin-dashboard Stories (`I349`, `I351`) but no dashboard task, and nothing assigned to Promise. **Absence of data is not absence of work.** `beevia-admin` has only `main`, so local work would be invisible here. But five weeks without a commit, a board item or a sprint is worth one direct question.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (from Mon 26 Oct, to 15:55 UTC Tue) | — | — | **4** | 2 | 2 | 0 |

**Acceptance is still zero.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted by someone other than its submitter since `BVA-I268` on 16 Sep. Board administration made no review moves this week. The team made all ten, but six of them were on someone else's item, and four of those six have no code. **The review step, not the developers, is still the bottleneck.** This week it also stopped working as a filter.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Item counts say nothing about who is carrying more. Seven WIP items for David and four for Ayomikun are not comparable loads.
- **Work outside the board.** #76–#83 (calls, names, the call guard, block state) and PR #52's call cards and mic fix have no items.
- **Who moved an item is not whether it is done**, and this week it is not even whether it was started (§2.1).
- **Local branches.** Server support work, admin dashboard work and design files would all be invisible here.
- **Nothing here measures correctness.** No build, test or lint ran in any repository. §3.1 rests on code reading and on the commit authors' own production claims.

---

## 7. Previous recommendations: where they stand

| Recommendation from 20 Oct | Status on 27 Oct |
|---|---|
| **1. Stop the VoIP token registration on mobile `main`** | ✅ **Overtaken, and it would have been the wrong fix.** The server now stores the VoIP token separately (#81 + db-schema #22), so the client's registration is correct as it stands. See the correction above |
| **2. Decide what a backgrounded iPhone gets for a call** | ✅ **Done.** APNs VoIP sender (#79) and routing (#81) |
| **3. Handle `call.ended` and `call_event` on the client** | ◐ **Half.** `call_event` cards render (PR #52). `call.ended` is still unhandled |
| **4. Merge #76; find out why `room_finished` is not arriving** | ◐ **#76 merged** (20 Oct 14:14 UTC). The webhook question is not visible from here |
| **5. Fix the light-mode mic; send `I322` back** | ◐ **Mic fixed** (PR #52). `I322` left 0902, destination unknown |
| **6. Create 0903, move `I309`/`I311` into it, do not sweep 0902, set `ZOHO_SPRINT_FILTER`** | ◐ **A successor exists (`1002`).** `I309`/`I311` are not in it, 0902 was swept, and the filter is still `08-01` |
| **7. Review 0902 against `main`** | ❌ **Not done.** 7 swept, 15 leaves removed, none reviewed |
| **8. Give off-board work a board item** | ◐ **Partly.** Statements (#84) has `I366`, and 1002 plans the next work in detail. #76–#83 still have none |
| **9. Subscribe Activity to `activity.updated`; add the `messages.ref_id` index** | ◐ **Subscribed** (PR #52). No index |
| **10. Split `flutter_local_notifications` 19 → 22 out of Dependabot #51** | ❌ **Not done.** #51 unchanged |
| **11. Send silent pushes at `apns-priority: 5`** | ✅ **Done** (#79, with `apns-push-type: background`) |
| **12. Restrict the Firebase API keys** | ? **Not visible** |
| **13. Put `needs: test` back on `beevia-api`'s `sync`; verify jobs elsewhere** | ❌ **Not done** |
| **14. Decide the `walletActivity` default** | ❌ **No change visible** |
| **15. Generate `openapi.yaml` from the running app and diff it in CI** | ❌ **Not done.** This week's spec gap (`registerPushToken`'s response, wrong for 3½ months) is the kind it would catch |
| **16. Check the production logs for pre-12 Oct PII** | ? **Not visible** |
| **17. Map `22P02` to `400`** | ❌ **Not done** |
| **18. Make Flutter CI a required check on mobile `main`** | ? **Not visible** |
| **19. Check the production host's SSH settings** | ? **Not visible** |
| **20. Hide the biometric option outside mock mode; bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** `I381` (To do) is the first item that could resolve the biometric half properly |
| **21. Open the admin board's next sprint, or say it is paused** | ❌ **Neither.** Admin-dashboard Stories appeared on the main board instead |
| **22. Carried items** | ❌ **None moved** |

**Four done or overtaken, six partly, the rest not done or not visible.** That is the best week for recommendations since the end of September, almost all of it in the call path.

---

## 8. What I would do this week

1. **Make REVIEW/QA mean "built, please verify".** Move `I365`, `I369` and `I376` back to To do (or In progress, if work exists locally). Put a one-line note on `I370`, `I377` and `I358` naming the endpoint that already satisfies them, and close them if that is the intent. Agree that only the person who built an item moves it to review.
2. **Account for 0902's 15 leaves.** For each one, record accepted, dropped, or moved to a sprint. `I309` (CallKit) is effectively done on `main` and can be reviewed. `I311` has been BLOCKED since 9 Oct with no explanation. `I325` has no server code.
3. **Write the Help & Support contract before more screens are built on placeholder data.** One short spec for FAQ, article feedback, disputes and the support conversation, added to `openapi.proposed.yaml`. It replaces or reconciles the current `/support/tickets` proposal and is agreed by both developers. Say whether `I348` (unassigned triage) is backend, ops or admin work.
4. **Handle `call.ended` on the client** (`CallKitManager.endNativeCall(callId)` from both push handlers). It is the last open item from the 20 Oct call list, and VoIP rings now reach closed iPhones.
5. **Test the iOS ring once on a real device** with a build from `main`, closed app, against production. The server and client halves were written separately, and only the author's own test is on record.
6. **Decide the statement password and delivery model** (`suggestions.md` §4.8) before users rely on it. At minimum, tell the user what the password is.
7. **Decide whether blocks apply to payment requests** (`suggestions.md` §4.9), and read `blocked` on the client so the profile can offer Unblock.
8. **Set `ZOHO_SPRINT_FILTER` to `1002`.** The in-repo export has read a closed sprint for eight weeks.
9. **Give the admin dashboard a home.** Either open an admin-board sprint with `I349`/`I351`'s UI work assigned to Promise, or say in one line that the dashboard is paused. Do not leave dashboard Stories unassigned on the consumer board.
10. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job (`suggestions.md` §7.7).
11. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4). It would have caught `registerPushToken`'s response.
12. **Split `flutter_local_notifications` 19 → 22 out of Dependabot #51**, and test it alone. The call path depends on it.
13. **Add the `messages.ref_id` index** in `beevia-db-schema`. The Activity feed and the call cards both query it.
14. **Carried:** restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode until `I381` lands; bring `payments.dto.ts` onto `phone.util.ts`; comments on `BVA-I260`/`I275`/`I277`; `code-scan.yml` into `beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring the five deleted `beevia-api` docs; writing the translation decision down; stopping the vendored client spec; untracking `android/app/.cxx/`.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 43.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 43 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work has instead appeared on the consumer board's 1002 as two unassigned Stories (§2.3). `beevia-admin` has gone 35.0 days without a commit, and `beevia-admin-api` 19.3. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, +0.56)

**Target 2026-09-01 (provisional). The target date passed fifty-six days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

**Line 2 moves 0.85 → 0.92.** The standing rule was not to move it for CallKit "until the server can ring it on both platforms". That condition is now met in code. `beevia-db-schema` v0.0.41 adds a separate VoIP token. `beevia-api` #79 adds an APNs VoIP transport and #81 routes iOS rings to it. Mobile `main` already had the PushKit receiver (`AppDelegate.swift`) and the registration (`bootstrap.dart:114`). Android has rung natively since #74. PR #52 renders call history cards, #78 stops duplicate calls, and #76 expires abandoned rings. It stops short of 0.95 because no client consumes the `call.ended` push, so a ring on a closed device is dismissed only by the plugin's timeout. Nothing else maps to a rubric line: statements and block state are not rubric capabilities, and Help & Support has no line.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change. Block state is metadata only |
| 2 | Voice & video calling | 8 | **0.92** | **+0.07** | iOS PushKit ring end to end (#79, #81, db-schema #22, `AppDelegate.swift`); Android unchanged; call cards (PR #52); `call.ended` push unhandled |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged. Wallet statements are NGN-ledger reporting, not multi-currency |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` (`wallet_service.dart:78`); payments ignore blocks (§4.9) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change on server or client; manage/freeze/delete screens have no code (§2.1) |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep |
| | **Weighted total** | **100** | **67.32** | **+0.56** | **≈67%** |

### What this report cannot tell you

- **Whether an iPhone actually rings.** §3.1 is a code reading plus the commit author's own device and credential checks. No device or production log was examined here.
- **Whether the APNs settings are in production**, beyond #81's statement that they are.
- **Where 0902's 15 leaves went**, or whether any was accepted before it left. The export reads sprints, not the backlog.
- **Whether `I354`, `I383`, `I386` or the four server support items exist on local branches.**
- **Whether PR #52 or any backend PR was reviewed**, or whether branch protection requires CI on any `main`.
- **What the design items in review contain.** Design files are not in git.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). Beevia now lists **`1002`**, `0902`, `0901`, `08-01`, `0702`, `0701`. The admin project lists only `0901-admin`.
2. Main board export (step 1a): 64 items, sprint 08-01, exit 0. Admin board export with `--sprint 0901-admin` (step 1b): 12 items, exit 0. Read-only scratch exports with `--modified --activity`: **1002** to `/tmp/beevia-scratch/1002/` (62 items, exit 0) and **0902** to `/tmp/beevia-scratch/0902/` (8 items, exit 0). All four ran in parallel and finished by about 15:54 UTC. 0901 was not re-exported; the 19 Oct copy of the closed sprint was reused.
3. Fast-forward sync (step 2), exit 1. **`beevia-mobile` fast-forwarded 2 commits on `main`** (`31a77e8` → `ccb4f63`, PR #52; no branch switch). `beevia-admin` was already current. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
4. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-27`: exit 1 (2 undocumented routes) before this cycle's spec edits, exit 0 after. The in-repo audit was run too, for the board section (exit 1, the known phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
5. Board analysis (`q27.py`, `flow27.py`): 1002 composition, 0902 before/after, every status transition in the window by actor, cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions. No comments, no reopens, 7 sweep completions on 0902, 1 owner completion on 1002.
6. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` (including `refs/pull/*`) on every repo. In `beevia-api`: all 8 commit messages since `49c0683`, the statements controller, DTO, service and constants, the call-service diff (block check, live-call guard, terminal no-op), the token-registration branch and its return shape, the conversation and contact-profile `blocked` fields, and the full `release.yml` at `origin/main`. In `beevia-db-schema`: migrations `0038`/`0039`, `devices.voip_token`, `clearPushToken`, the `statement_requests` schema and enums, and `messages` indexes. In `beevia-mobile`: PR #52's diff, the VoIP registration and its call site, both push handlers for `call.ended`, `call_event` handling, `activity.updated`, the mic widget, `AppDelegate.swift`'s PushKit wiring, conflict markers, the biometric step-up, card API usage on `main`, a search of **every remote branch** for statement, freeze and terminate code, and `origin/BVA-I330`'s diff and `SupportService`. Also checked: `I286`'s label in `app_en.arb`, and server storage for theme/text-size preferences (none).
7. Spec and RFC updates (§3.5).
8. This report and its web edition.
9. End-of-run recheck at 16:06 UTC. A fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found **one item added after the cut-off**: `BVA-I392` *Activity Screen – Verification Checklist*, a Story with an attachment, To do, co-assigned to all three team members, created and moved into 1002 by board administration at 15:57–15:58 UTC. It is not in this report's counts (1002 is 63 items as of the recheck). It may be the first review artefact for the Activity work that left 0902. `ls-remote` showed every `main` at the commits read above, no open backend PR, and no new mobile PR (highest PR ref still #52).

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch` and fast-forward, the only git operations were `fetch`, `ls-remote`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`/`rev-list`/`ls-tree`. Two read-only Zoho `--raw` calls looked for the project backlog: one returned `404`, the other carried no backlog id. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-27.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md`, `suggestions.md`, plus new board exports for 27 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 and 0902 figures come from the scratch exports.
- **The backlog is not exported**, so the destination of 0902's 17 removed items is unknown.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.** PR numbers come from `refs/pull/*` and merge-commit messages.
- **No edition between 21 and 26 Oct.** The window is 7.1 days, so day-level ordering inside it comes from `actiontime`s and commit times, not from intermediate snapshots.
- **The export's "no source key" warning fired on `Epic`** for all four exports. This is the known sampling artefact, not a scope gap; 1002's items genuinely have no epic.

**Window.** 20 Oct 14:02 UTC → 27 Oct 15:55 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
