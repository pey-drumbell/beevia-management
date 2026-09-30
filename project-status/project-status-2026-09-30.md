# Beevia — Project Status

**As of 2026-09-30** · Sprint **0902** (30 Sep → 15 Oct): **opened today, 11 items, all To do** · Sprint **0901** (3 Sep → 22 Sep): **closed today by a bulk sweep** · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-30.csv` + `beevia-activity-2026-09-30.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-30.csv` + its activity sidecar (12 items, sprint 0901-admin); read-only scratch exports of sprint 0901 (**76 items**) and sprint **0902 (11 items)**, each with its sidecar, in `/tmp/beevia-scratch/` and `/tmp/beevia-scratch/0902/`. All five repos were read at `origin/main`: `beevia-admin` and `beevia-mobile` in the working tree, and `beevia-api`, `beevia-admin-api` and `beevia-db-schema` through a `git archive` shadow because their working trees are still `diverged`. The unmerged branches `beevia-mobile` `origin/update-fixes` and `beevia-admin-api` `origin/ci/node-26-only` were read too.

Scope: four boards, kept separate and never summed. **Window: 29 Sep 14:05 UTC → 30 Sep 14:03 UTC, one working day.**

---

## Quick overview

> **Sprint 0901 was closed this morning by a bulk sweep, not by review.** At 07:56 UTC board administration moved every open item to Done: 68 transitions (61 leaves and 7 parents) in 35 seconds. The sweep took in 57 items from REVIEW/QA, the two disputed items, the one item In progress and the one item still To do. **It also closed the four QA items whose fixes are verifiably not on `main`**, so "Done" on this board does not mean "on `main`". Sprint **0902** opened at the same time, 30 Sep → 15 Oct, with 11 Stories. That ends six editions with no open sprint. The day's engineering changes were on the backend. **`beevia-api` #60 now rejects chat requests without `X-Device-Id`**, and the mobile client does not send that header when it starts a new chat, on `main` or on `update-fixes`. **`beevia-db-schema` #19 now publishes and migrates production on every push to `main`, without running CI first.**

**Correction to the previous edition: read this first.**

1. **The 29 Sep edition described `beevia-db-schema`'s pending branch `ci/pr-only-no-cron` as "also removes the schedule from its three standalone scan workflows" (§3.2, §4, `suggestions.md` §7.7). That missed its most consequential change.** The same commit (`de06516`, unchanged since it was read on 29 Sep) rewired **Release to trigger on every push to `main`**. It removed the gate that made Release wait for CI to pass, and it dropped CI's `paths-ignore` list. "Sync to server", which runs "Migrate the production database", still runs after every successful Release. The branch merged overnight as #19, so the chain on `main` is now **push → publish → migrate production, with no test or scan in between** (§3.2). Yesterday's recommendation, "keep a weekly scan and the `push` trigger", addressed the smaller half.
2. **The weekly submission trend (29 Sep §6.5: 9 / 15 / 44 / 1) counted parent Stories' transitions along with leaves.** On leaves only, the figures are **7 / 11 / 42 / 1** (W37–W40). Part of the difference in W37 is `BVA-I251`, which left the sprint today. The conclusion does not change.

| Metric | 29 Sep | 30 Sep | Δ |
|---|---:|---:|---|
| Sprint 0901 items (leaves + parents) | 77 (68+9) | **76 (67+9)** | −1 (`BVA-I251` left the sprint, §1.3) |
| Sprint 0901 leaves Done | 6 | **67 (all)** | **+61, all in one 35-second sweep** |
| Sprint 0901 leaves REVIEW/QA | 58 | **0** | −58 (57 → Done, 1 removed) |
| Sprint 0901 leaves To do / In progress / BLOCKED | 1 / 1 / 2 | **0 / 0 / 0** | all → Done in the sweep |
| Queue age at the sweep (57 items) | — | **median 5.7 d, oldest 21.7 d** | |
| **Sprints open on the main board** | 0 | **1 (0902, 30 Sep → 15 Oct)** | **first since 22 Sep** |
| Sprint 0902 items | — | **11 Stories, all To do** | 9 David · 1 Ayomikun · 1 Philip |
| Admin board: open sprint / days since any activity | none / 15.0 | **none / 16.0** | +1.0 |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | 0 |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | contract change on 6 routes, fixed in place (§3.1) |
| Chat routes that now **require** `X-Device-Id` | 0 | **6** | `beevia-api` #60 |
| Mobile calls to those routes that omit it (`main` / `update-fixes`) | — | **2 / 1** | inbox + new chat / new chat (§3.1) |
| `beevia-db-schema`: push to `main` → production migration without CI | no | **yes** | #19 (§3.2) |
| `update-fixes` vs `beevia-mobile` `main` | 3 ahead · 90 files | **4 ahead · 100 files, +5,339 / −1,417** | +1 commit (`edcadef`) |
| `beevia-mobile` days since a commit on `main` / any branch | 4.9 / 0.9 | **5.9 / 0.8** | |
| `beevia-api` days since a product (non-CI) commit | 4.0 | **0.5** | #60, #61 |
| `beevia-admin-api` days since a commit | 5.1 | **6.1** | CI branch still pending |
| `beevia-admin` days since a commit | 6.9 | **7.9** | |
| Ayomikun commits (7d, both identities, `origin/main`, non-merge) | 29 | **32** | 2 product, 0 CI new |
| David commits (7d): merged to `main` / on `update-fixes` | 1 / 3 | **0 / 4** | rolling window |
| Promise commits (7d, merged) | 1 | **0** | last 22 Sep |
| Estimation points set (0902 / 0901 / 0901-admin / 08-01) | — · 0/77 · 0/12 · 0/64 | **0/11** · 0/76 · 0/12 · 0/64 | 0902 opened unestimated |
| MVP readiness (estimate) | ≈66% (65.52) | **≈66% (65.52)** | 0 (a downgrade is pending on deploy, §5) |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 0901: 20, all swept to Done · **0902: 1** (`BVA-I315`, To do) · 0901-admin: 3 | 9 (4 own; 5 board administration) | 0.98 d (n=10) | 0 on 0901 · 1 on 0901-admin (`BVA-I8`, **16.0 d**) | **32** | Shipped #60 (strict `X-Device-Id`, the right fix) and #61 (observability). #19 made a push to `main` migrate production without CI (§3.2) |
| David Samuel | mobile | 0901: 48, all Done (46 by the sweep) · **0902: 9, all To do** | 38 (11 own; 23 board administration; 4 Ayomikun) | 0.96 d (n=24) | 0 on 0901 · 9 queued on 0902 | **0 merged · 4 unmerged** | `update-fixes` gained a fourth commit (44 files) and is now 100 files wide. Its QA items are marked Done but not on `main`. `createConversation` needs `X-Device-Id` (§3.1) |
| Philip Chidera | design | 0901: 7, all Done · **0902: 1** (`BVA-I314`, Activity tab design) | 3 (1 own; 2 board administration) | 0.55 d (n=2) | 0 | n/a | Their design item gates both the Activity backend and the Activity screen on 0902 |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) | 0 | n/a | 1 (`BVA-I9`, **16.0 d**) | **0** | `beevia-admin` **7.9 days** without a commit. The admin board got no new sprint today |

**The two questions for standup:** (1) **Is `beevia-api` #60 deployed, and who adds `X-Device-Id` to `createConversation`?** Once it is live, every mobile build, including `update-fixes`, gets `400` when starting a new chat, and a `main` build also gets `400` on the inbox. (2) **What does "Done" on 0901 mean for the four items whose fixes are only on `update-fixes`?** If the answer is "the fix exists somewhere", say so on 0902, and put merging that branch on it as an item.

**The three things worth knowing:**

1. **0901's Done column is a close, not an acceptance.** The sweep ran from 07:56:19 to 07:56:53 UTC and was done by board administration. It left no comment and no per-item note. It moved `BVA-I260` and `BVA-I275` to Done from BLOCKED. Both are the items where David argued on 23 Sep that the reported behaviour is intended, and nobody replied. If Done means "argument accepted", one line on each item would say so. It also closed `BVA-I277` from In progress. That item's request for a screenshot is still unanswered. It closed `BVA-I297` from To do, never started. And it closed `BVA-I287`, `BVA-I292`, `BVA-I294` and `BVA-I303`, whose fixes are verifiably **only** on `update-fixes`. This is the same kind of event as the 3 Sep close of sprint 08-01. It clears the board, but it tells a reader nothing about what was built. **Excluding the two bulk sweeps, no item on any board has ever been accepted by someone other than the person who submitted it.** Twelve editions have now said that no reviewing role is staffed.

2. **The backend fixed a silent failure, and the fix moves the failure to the client.** Without a device id, the six chat routes used to return rows nobody could decrypt, which looked like an empty chat. `beevia-api` #60 now rejects that request with `400 device_id_required`. That is correct, and the commit warns the client team explicitly. But the mobile client's `POST /conversations` sends no device header on either branch. `GET /conversations` sends it only on `update-fixes` (`edcadef`, 29 Sep 18:12 UTC, committed 8 h 40 min before #60). The client's mock server does not enforce the header, so no client test will catch this. `openapi.yaml` is updated (§3.1).

3. **Sprint 0902 is a real plan, and one item in it cannot be built as written.** It has 11 Stories: seven for push notifications, which is the client half of a server surface that exists (`/notifications/*`), plus a UI-audit fix and a three-part **Activity tab** (design, backend and screen). The backend item, `BVA-I315`, asks one endpoint for each row's *"last message text"* preview and for search across *"message/payment content"*. Under end-to-end encryption the server holds only ciphertext, so it can produce neither. Message previews and message-text search have to happen on the device, as the inbox already does. Fix the acceptance criteria before work starts, not in review. The Activity feed is also absent from the PRD and from both specs.

**If you read nothing else:** the board now shows 0901 fully Done, but that came from a 35-second close, not a review. Four of those items are still unfixed on `main`. Overnight, two backend changes shifted risk. #60 will make "start a chat" fail on every current mobile build once it deploys. #19 lets a push to `main` migrate production without a test. Both have one-line fixes.

---

## 1. Sprint 0901: closed today

**76 items: 67 leaves + 9 parent Stories**, all Done. All figures below are leaves unless stated.

### 1.1 Status distribution and movement

| Status | 29 Sep | 30 Sep | Δ |
|---|---:|---:|---:|
| REVIEW/QA | 58 | **0** | −58 |
| To do | 1 | **0** | −1 |
| In progress | 1 | **0** | −1 |
| BLOCKED | 2 | **0** | −2 |
| Done | 6 | **67** | +61 |
| **Total leaves** | **68** | **67** | −1 |

The audit's `SINCE` section, run against the 29 and 30 Sep scratch exports, reports **57 left review, 61 newly Done, 0 entered review, scope −1**.

### 1.2 The sweep

**Every board action in the window was part of it:** 68 `Item Completed` entries between **07:56:19 and 07:56:53 UTC**, all by board administration. There were no comments, re-assignments or other status moves on sprint 0901.

| From | Leaves | Owners (owner rows) |
|---|---:|---|
| REVIEW/QA | 57 | David 42 · Ayomikun 20 · Philip 3 (co-assignment counted for both) |
| BLOCKED | 2 | `BVA-I260`, `BVA-I275` (David): disputed, no reply since 23 Sep |
| In progress | 1 | `BVA-I277` (David): awaiting a screenshot since 23 Sep |
| To do | 1 | `BVA-I297` (David): never started |
| *Parents* | *7* | *REVIEW/QA → Done* |

The 57 queue items had waited a median **5.7 days**. The oldest were the Notification block submitted on 8 Sep (`BVA-I246`–`I249`), at **21.7 days**.

**What the sweep closed that is not on `main`:** `BVA-I287` (Request Money button), `BVA-I303` (wallet spacing), `BVA-I292` (E2EE notice) and `BVA-I294` (offline conversation list). All four were verified in the 28–29 Sep editions to be fixed only on `update-fixes`, and none of those fixes has reached `main` since. The other queued items were not checked line by line (appendix).

**Where 0901 stands in the project's history.** Sprint 0901's Done column now reads: 61 closed in the sweep, 5 closed by Philip on 11 and 16 Sep, and 1 (`BVA-I268`) moved REVIEW/QA → Done by its own owner on 16 Sep. This is the second bulk close. The first was sprint 08-01's 46-item sweep on 3 Sep.

### 1.3 The item that left: `BVA-I251`

`BVA-I251` *Account & Verification Status Notification Trigger* (Ayomikun, REVIEW/QA since 8 Sep) is no longer in sprint 0901, and it is not in 0902 either. Its destination cannot be seen from these exports: the backlog is not exported, and a deletion leaves no trace in the sprint sidecar. A client-side counterpart was created on 29 Sep as `BVA-I311` (*Account & Verification Status Notification Handling*, David, 0902). So the backend item was most likely set aside rather than lost, but that is inference.

---

## 2. Sprint 0902: opened today

**11 items, all Stories, no parents, all To do, 0 of 11 estimated, 0 with an epic.** The sprint runs 30 Sep → 15 Oct. Board administration created all of them, eight on 29 Sep 15:05–15:59 UTC and three today 13:12–13:25 UTC. At 07:52–07:53 UTC today it assigned them and moved them into the sprint from the backlog.

| Item | Owner | Theme |
|---|---|---|
| `BVA-I306` Push Notification Client Integration & Permission Flow | David | Push notifications (client) |
| `BVA-I307` Deep Link Routing & Badge Count | David | 〃 |
| `BVA-I308` New Message Notification Handling | David | 〃 |
| `BVA-I309` CallKit & ConnectionService Integration | David | 〃 |
| `BVA-I310` Money Notification Handling | David | 〃 |
| `BVA-I311` Account & Verification Status Notification Handling | David | 〃 |
| `BVA-I313` Build and Implement Notification Settings Screen | David | 〃 |
| `BVA-I286` Mismatched UI element on User Profile screen | David | UI audit §1.3 (created 24 Sep) |
| `BVA-I314` Complete the Activity Tab Design | Philip | Activity tab |
| `BVA-I315` Activity Feed Backend (Combined Chats, Calls & Payments) | Ayomikun | 〃 |
| `BVA-I316` Build the Activity Screen | David | 〃 |

Three things to read from it:

- **The notification work matches a server surface that already exists.** `/notifications/token`, `/notifications/preferences` and `/notifications/test` are implemented. The descriptions say "the backend api already stores multiple tokens per user", which is correct. This is client catch-up, not new API.
- **`BVA-I315` needs its acceptance criteria corrected before it starts.** It asks the server for *"a type-appropriate preview (last message text …)"* and search over *"message/payment content too"*. The server stores message bodies as per-device ciphertext and cannot read them. That is the product's E2EE guarantee, not a missing feature. The inbox already solves this: the server returns the ciphertext and the device decrypts it for the preview. A feed endpoint can return the same envelope, and name/payment search can stay server-side, while message-text search has to be local. Payments and calls are server-readable, so the rest of the item is buildable. The Activity feed appears in neither the PRD nor either spec, so it has no proposed contract to build against yet.
- **Nine of eleven items are David's**, on top of an unmerged 100-file branch. With no estimation points, the board cannot say whether that is a sprint's worth of work. The item count alone does not say it is too much.

---

## 3. API surface, spec drift and CI

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. The audit ran against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-30`, and again after today's spec edit. The in-repo audit reports its usual 21 phantom lines (6 consumer + 15 admin) from the three `diverged` working trees. They were not acted on.

### 3.1 What merged, and the contract change the route audit cannot see

| Repo | PR | Merged (UTC) | Change |
|---|---|---|---|
| `beevia-api` | **#60** `feat/require-device-id` (`f1d5a40`) | Wed 30 Sep 02:55 | `X-Device-Id` **required** on 6 routes; `400 device_id_required`; history returns `unresolved` |
| `beevia-api` | #61 `feat/nestjs-observe` (`9e4c811`) | Wed 30 Sep 03:21 | Adds `@nestjs/observe` ^0.3.3 APM alongside the Axiom/OTel pipeline; credentials via `OBSERVE_APP_KEY`/`SECRET` |
| `beevia-db-schema` | **#19** `ci/pr-only-no-cron` (`de06516`) | Wed 30 Sep 02:14 | CI and scans on PR only; **Release on every push to `main`, ungated** (§3.2) |
| `beevia-db-schema` | — `be14bc3` (bot) | Wed 30 Sep 02:15 | `chore(release): v0.0.38`, triggered by #19 |

**#60 is the day's consequential change, and it adds no route.** The six affected routes are `POST`/`GET /conversations`, `GET /conversations/{id}`, `GET`/`POST /conversations/{id}/messages` and `POST /messages/{id}/receipts`. They used to fall back to a message's own `ciphertext` when no device was named. That field is `null` for every 1:1 envelope send, so the response was an unreadable page that looked like an empty chat. A new `@DeviceId()` decorator now rejects a missing or blank header. It is the right call, and the commit message warns the client team plainly.

**The mobile client, checked at both heads:**

| Route | `main` | `update-fixes` |
|---|---|---|
| `GET /conversations/{id}/messages` | sends the header | sends the header |
| `GET /conversations` (inbox) | **omits it** | sends it when a device id is known |
| `POST /conversations` (start a chat) | **omits it** | **omits it** |

Messages and receipts go over the socket, whose handshake carries the header. Once #60 is deployed, starting a new direct chat fails on every current build. A `main` build's inbox fails too. `lib/mock` does not enforce the header, so the client's tests will not show it. Whether #60 is deployed yet cannot be seen from here.

**Spec updated in place** (`openapi.yaml`): `DeviceIdHeader` is now `required: true` and documents `device_id_required`. `listConversations`, `getConversation` and `getMessageHistory` gained their `400`. `MessageHistory` gained `unresolved`. `api-rfc.md` has a new §5.12 on the change and the client gap. This is the fifth consecutive cycle in which the most consequential change was invisible to a route-level diff (`suggestions.md` §5.4).

**#61** is additive. Both telemetry pipelines run, and the SDK is inert while its keys are unset. Two small points are worth keeping in view. It is a 0.x third-party SDK that instruments controllers and guards. And the server holds no message plaintext, so the spans it can export are metadata, but they include metadata about who messages whom. Neither point is a finding today.

### 3.2 `beevia-db-schema`: a push to `main` now migrates production without running CI

Before #19: push to `main` → **CI** (tests, filtered by `paths-ignore`) → **Release** only if CI succeeded → **Sync to server** (migrate production).
After #19: push to `main` → **Release** (publish) → **Sync to server**. CI runs on pull requests only.

The new comment in `release.yml` gives the premise: *"CI is a required check, so anything on main has already passed it."* That is branch protection (`suggestions.md` §7.1), which has never been verifiable from here. On 28 Sep this repository's `main` took a forced update, which shows a change *can* reach it without a pull request. Previously a push like that still had to pass CI before it could migrate anything. Now it does not. The effect is already visible in a harmless form: #19 changed only `.github/**`, which the old filter would have excluded, and it still produced a release 41 seconds later.

Recommendation (`suggestions.md` §7.7, updated today): **have Release run CI's verify job itself before publishing.** Alternatively, confirm in the GitHub UI that `main` requires a PR, requires the check and blocks force-push, and write the confirmation down. **`beevia-admin-api`'s pending branch makes the same change to its deploy chain** (`66737d7`: *"trigger the deploy chain from push"*), and it should get the same fix before it merges.

**Release state, resolved by accident.** `main`'s `package.json` is now 0.0.38, which matches the registry. The release step already skips a publish when the version exists. Tag `v0.0.38` still points at `e285f10`, which is on no branch, but its tree differs from `main`'s only under `.github/`. The 29 Sep question of what the tag should point at is now low-stakes.

**Reflog sweep:** no forced update in any of the five repos in this window.

### 3.3 Spec and document changes this cycle

| File | Change |
|---|---|
| `openapi.yaml` | `DeviceIdHeader` required and documented; `400` on `listConversations`, `getConversation`, `getMessageHistory`; `MessageHistory.unresolved` |
| `api-rfc.md` | **New §5.12:** `X-Device-Id` now required on six chat routes, with the client-coverage table |
| `suggestions.md` | **§7.7:** 2026-09-30 update on db-schema's ungated release → production migration, and the same change pending for `beevia-admin-api`. **§8 item 3b:** updated |

No route or proposed operation moved. `openapi.proposed.yaml`, `openapi.admin*.yaml` and `admin-api-rfc.md` are unchanged.

---

## 4. Risks

- **"Start a chat" breaks on deploy** (§3.1). This affects every mobile build, `main` and `update-fixes`, the moment #60 is live. The fix is one header in `createConversation`. **New today.**
- **A push to `beevia-db-schema` `main` migrates production with no CI** (§3.2). **New today.** The same change is pending for `beevia-admin-api`'s deploy chain.
- **The board says Done for work that is not on `main`** (§1.2). At least four items are affected. Any 0902 planning or release note built on 0901's Done column inherits this.
- **`update-fixes` keeps growing**: 4 ahead, 100 files, +5,339 / −1,417. The biometric step-up is still at `wallet_service.dart:78`, and the server still accepts `{ pin }` only (`auth.dto.ts:77`). `suggestions.md` §5.11.
- **`payments.dto.ts:5` phone field** is still `z.string().trim().min(6).max(20)`, the input to every escrowed chat send once `update-fixes` merges.
- **`BVA-I315` is specified against E2EE** (§2). It is cheap to fix now and expensive after build.
- **The admin workstream is silent:** 7.9 days with no repo commit, 16.0 days with no board activity, and no successor sprint.
- **Three diverged local working trees** (`beevia-api` behind 65, `beevia-admin-api` 34, `beevia-db-schema` 47, each 1 ahead).

---

## 5. PRD gap

No product code on any `main` moved a capability. The four structural gaps are where they were: the international KYC tier, multi-currency/FX settlement, virtual cards beyond what is wired, and consent management.

Re-verified at `origin/main`: `PaymentService.activeNgn()` at `payment.service.ts:506`, called from lines 70, 128 and 288. `StubTranslateAdapter` is still bound at `translate.module.ts:23`. The client's chat Send on `main` still posts `/payments/transfer`, which bypasses escrow.

**A downgrade is pending, conditional on deploy.** Capability #1 (E2EE messaging) is scored on screens that are *wired to the real API*. Once #60 is live, `main`'s inbox and new-chat calls are rejected by that API. The score is held at 0.90 today because whether #60 is deployed cannot be seen from here, and because `update-fixes` repairs the inbox. If #60 is live and neither fix has reached `main` by the next edition, #1 should come down.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of the relevant transition), never from `Last Modified`. Commit counts are non-merge commits on `origin/main` from 23 Sep 14:03 to 30 Sep 14:03 UTC, summing each person's git identities. Bot commits are excluded. David's unmerged branch commits are shown separately. **The 0901 sweep is not a submission and is not counted as anyone's output.**

### 6.1 Ayomikun Araoye: backend + admin API

**32 commits in 7 days**: `beevia-api` 17 (`Phoenixdadhev` 15, `Ayomikun Araoye` 2), `beevia-db-schema` 14 (13 + 1), `beevia-admin-api` 1. The two new commits are product work. #60 is a careful fix to a failure that looked like success, with tests (`device-id.decorator.spec.ts`, a new `sync` spec block). #61 is observability. Their CI change in `beevia-db-schema` (#19) is §3.2's risk. Its reasoning is sound for work that arrives by pull request. The gap is the unverified premise, not the engineering.

On the board, all 20 of their 0901 leaves were closed by the sweep. `BVA-I251` left the sprint. They have one 0902 item (`BVA-I315`), whose acceptance criteria need the E2EE correction in §2 before they start. `BVA-I8` has been In progress on the admin board for 16.0 days. Submissions in 7 days: 9 (4 own moves, 5 by board administration). Median cycle time: 0.98 d (n=10).

### 6.2 David Samuel: mobile

**38 submissions to REVIEW/QA in 7 days (owner rows): 11 own moves, 23 by board administration, 4 by Ayomikun on co-owned items.** Median cycle time 0.96 d (n=24). All 48 of their 0901 leaves are now Done, 46 of them by the sweep.

**Commits: 0 merged to `main` in the window, 4 on `update-fixes`.** The newest is `edcadef` (29 Sep 18:12 UTC, "all the fixes and improvements", 44 files, +1,488 / −404). It adds an outbox for messages sent offline, with tests. It also adds a minimised-call banner, wallet-provider changes, and the `X-Device-Id` header on the inbox fetch, written before the server began requiring it. None of it has been checked item by item against the board. The branch now holds real, board-requested work across chat, calls and wallet. The ask is unchanged, and it is about *where* the work is, not effort: merge it (without the biometric option), and add `X-Device-Id` to `createConversation` on the way.

They own 9 of 11 items on 0902.

### 6.3 Philip Chidera: design

Philip had no board action in the window. All 7 of their 0901 leaves are Done. They own `BVA-I314` (Activity tab design) on 0902, which both `BVA-I315` and `BVA-I316` depend on. That makes it the sprint's first dependency. No commits, because design work does not land in these repositories.

### 6.4 Promise Udo: admin dashboard

**No commit in the 7-day window.** The last was `0b41e35` on 22 Sep, **7.9 days** ago. The admin board has had no activity for 16.0 days, and `BVA-I9` has been In progress for all of it. The main board opened a new sprint today. The admin board did not. **Absence of data is not absence of work.** `beevia-admin` has no branch except `main`, so local work would be invisible here. The question from 28 Sep is still unanswered, and it now has a natural moment: whether the admin workstream gets a 0902 of its own.

### 6.5 Weekly submission trend (sprint 0901 leaves, transitions into REVIEW/QA)

| ISO week | Submissions |
|---|---:|
| 2026-W37 | 7 |
| 2026-W38 | 11 |
| 2026-W39 | **42** |
| 2026-W40 (from Mon 28 Sep) | 1 |

Across the sprint, acceptances by someone other than the submitter numbered **zero**, apart from today's bulk close. See correction 2 for the change of basis from the 29 Sep table.

### 6.6 What this does not measure

- **No estimation points on any item on any board**, including the 11 on the new sprint. Item counts say nothing about who is carrying more. This is the nineteenth edition to say so.
- **"Submitted" counts any transition into REVIEW/QA, by anyone**, and credits it to the item's owner. For David, 23 of 38 were board administration's moves.
- **The sweep is not throughput.** 61 items became Done in 35 seconds. Neither the "Done" count nor the jump from 6 to 67 measures delivery.
- **Commit counts reward small commits, and cycle times reward small items.** `edcadef` alone is 44 files.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository.

---

## 7. Previous recommendations: where they stand

| Recommendation from 29 Sep | Status on 30 Sep |
|---|---|
| **1. Merge `update-fixes` today, after taking out the biometric option** | ❌ **Not merged; grew again** (4 ahead, 100 files). The biometric option is still at `wallet_service.dart:78` |
| **2. Keep a weekly scan and the `push` trigger before the other CI branches merge** | ❌ **Went the other way.** `beevia-db-schema` #19 merged as written, and it did more than drop the scan (correction 1, §3.2). `beevia-admin-api`'s branch is still pending |
| **3. Write down what REVIEW/QA means** | ❌ **Not done, and now more urgent.** The queue was emptied by a sweep rather than a definition. 0902 starts with the same ambiguity |
| **4. Name a reviewer** | ❌ **Not done.** 0901 closed without review. Twelfth edition |
| **5. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done.** Line 5 unchanged |
| **6. Reply on `BVA-I260`, `BVA-I275` and `BVA-I277`** | ◐ **Closed without a reply.** All three are Done via the sweep, and none carries a comment. If Done means "argument accepted", one line on each item would say so |
| **7. Open sprint 0902 on both boards** | ◐ **Half done.** The main board's 0902 opened today (11 items). The admin board has no successor to `0901-admin` |
| **8. Ask about the admin workstream** | ❔ **No visible answer.** Repo silent 7.9 d, board 16.0 d |
| **9. Decide what `v0.0.38` should point at** | ◐ **Overtaken.** `main` re-bumped to 0.0.38 via #19's release run. The tag still points at `e285f10`, whose tree differs only under `.github/` |
| **10. Carried: OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; translation decision; stop vendoring the client spec; estimation points on 0902** | ❌ **None done.** 0902 opened with 0 of 11 estimated. `beevia-admin` still has no `.github/` |

**Two of ten moved, both partially, and both through board administration** (0902 opened; the tag question overtaken). No engineering recommendation was acted on.

---

## 8. What I would do this week

1. **Add `X-Device-Id` to `createConversation` in `beevia-mobile`**, on `update-fixes` or directly on `main`, before #60 is deployed. If it is already deployed, do it today. It is one header, and without it no build can start a chat. Also consider having the mock server enforce the header, so the client's tests see what the real API does.
2. **Merge `update-fixes`, without the biometric option.** It now fixes the inbox for #60 as well as the four items 0901 marked Done. Add it to 0902 as an item, so the board shows it.
3. **Gate `beevia-db-schema`'s Release on the verify job** (§3.2; `suggestions.md` §7.7). Make the same change to `beevia-admin-api`'s pending branch before it merges. Neither needs org access.
4. **Correct `BVA-I315`'s acceptance criteria for E2EE** before work starts. Return ciphertext previews for the device to decrypt, keep message-text search on the device, and write a proposed contract for the feed endpoint.
5. **Decide what REVIEW/QA and Done mean on 0902**, with someone named to move items out of review. 0901 ended with the whole board reviewed by nobody.
6. **Say what Done means for `BVA-I260`, `BVA-I275` and `BVA-I277`.** That is three one-line comments.
7. **Open the admin board's next sprint**, or say in one line that the admin workstream is paused.
8. **Estimate 0902.** It is 11 items and one sitting, while the sprint is one day old.
9. **Bring `payments.dto.ts` onto `phone.util.ts`** before item 2 lands.
10. **Carried, unchanged:** OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix; the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; stopping the vendored client spec.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 16.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 16 days. **Zoho lists no successor sprint for this project**, unlike the main board, which opened 0902 today. `beevia-admin` has gone 7.9 days without a commit and `beevia-admin-api`'s `main` 6.1 days. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈66% (estimate; 65.52, unchanged)

**Target 2026-09-01 (provisional). The target date passed twenty-nine days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build, not acceptance. Today's board sweep is exactly the kind of acceptance signal the rubric ignores.

**No score moved.** #60 changes how E2EE messaging fails, not what exists. The one score at risk is #1, and it is held pending deploy (§5).

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | #60 makes the device header mandatory. **`main`'s inbox and new-chat calls omit it**, so the score is held pending deploy (§5). The E2EE notice exists only on `update-fixes` |
| 2 | Voice & video calling | 8 | 0.80 | 0 | No `/calls` change. Call-audio routing and the minimised-call banner are on `update-fixes` only |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` at `payment.service.ts:506`, called from 70/128/288 |
| 7 | Send / request / receive in chat | 12 | 0.85 | 0 | Chat Send on `main` still posts `/payments/transfer` (no escrow). The escrowed `payment.send` path is on `update-fixes` only |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card change on `main` |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep. No `beevia-admin-api` `main` commit since 24 Sep |
| | **Weighted total** | **100** | **65.52** | **0** | **≈66%** |

### What this report cannot tell you

- **Whether `beevia-api` #60 is deployed.** Everything in §3.1 about client failures applies from the moment it is.
- **Whether a direct push to any backend `main` is possible.** Branch protection cannot be seen from a clone. §3.2 is a risk, not a finding of exposure.
- **Whether the 53 swept queue items not individually checked are fixed on `main`.** Four are verifiably not. The rest were not checked line by line, and no build ran.
- **Where `BVA-I251` went.** The backlog is not exported.
- **Whether any CI or release run passed**, or whether "Sync to server" ran after `be14bc3`.
- **Whether `update-fixes` builds or passes its tests.**
- **Velocity for any sprint.** Nothing on any board is estimated (0 of 11, 0 of 76, 0 of 12, 0 of 64).

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Sprint-name discovery on both projects (`--sprint __nonexistent__ --dry-run`). **Beevia now lists `0902`.** The admin project still lists only `0901-admin`.
2. Main board export: 64 items, sprint 08-01, exit 0.
3. Admin board export with `--sprint 0901-admin`: 12 items, exit 0.
4. Read-only scratch exports: sprint **0902** to `/tmp/beevia-scratch/0902/` (11 items, exit 0) and sprint 0901 to `/tmp/beevia-scratch/` (76 items, exit 0).
5. Fast-forward sync: 0 repos advanced, 2 already current, 3 refused as `diverged`. Then `git fetch` of all five, read-only.
6. Reflog sweep of all five repos for forced updates. None were found in the window.
7. Audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-30`: route level and spec health clean. It was re-run with the 29 and 30 Sep 0901 scratch exports copied in, for the `SINCE` delta, and again after the spec edit.
8. Activity-sidecar sweep of the window across 0901, 0902 and 0901-admin: status transitions, comments, and completions matched on all three Zoho action names (`Updated the status`, `Item Completed`, `Item Reopened`).
9. Content reads: `beevia-api` #60 and #61 diffs. Mobile `X-Device-Id` coverage via `git grep` at `origin/main` and `origin/update-fixes`. `update-fixes` `edcadef` (stat and the `chat_service.dart` diff). `beevia-db-schema` #19 and `sync.yml`. `beevia-admin-api`'s pending branch.
10. Edits to `openapi.yaml`, `api-rfc.md` and `suggestions.md`, then this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages at the sweep are measured from each item's last transition into `REVIEW/QA` to its `Item Completed` entry. Cycle times are `In progress` → `REVIEW/QA` pairs.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose transitions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync and `fetch`, the only git operations were `git archive` and read-only `log`/`diff`/`grep`/`show`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-30.html`, `web-report/index.html`, `openapi.yaml`, `api-rfc.md` and `suggestions.md`, plus new board exports for 30 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done). Sprint 0901 and 0902 figures come from the scratch exports. **Now that 0902 exists, moving the filter to `0902` would make the in-repo export useful again**, and it would give the next edition a day-over-day diff of the live sprint.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`, each 1 ahead. Every backend claim is made against `origin/main` through the shadow.
- **GitHub settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`** (and on `Parent Id` for 0902). This is the known sampling artefact. On 0901 the column resolves (`Language` 18, `Notification` 6, `security` 5; 47 blank). On 0902 all 11 are genuinely unassigned, and none has a parent.

**Window.** 29 Sep 14:05 UTC → 30 Sep 14:03 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
