# Beevia — Project Status

**As of 2026-09-28** · Sprint **0901** (3 Sep → 22 Sep) — **closed six days ago, still the working board** · Sprint **0901-admin** (3 Sep → 22 Sep) — closed, static · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-28.csv` + `beevia-activity-2026-09-28.json` (64 items, sprint 08-01 — frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-28.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint 0901 (**77 items**) + sidecar in `/tmp/beevia-scratch/`; all five repos read at `origin/main` (`beevia-admin`, `beevia-mobile` in the working tree; `beevia-api`, `beevia-admin-api`, `beevia-db-schema` via a `git archive` shadow, since their working trees remain `diverged`), plus the unmerged `beevia-mobile` branch `origin/update-fixes`.

Scope: three boards, kept separate and never summed. **Window 25 Sep 12:58 UTC → 28 Sep 14:05 UTC — about 3.0 days, across a weekend.**

---

## Quick overview

> **The board is now 84% review queue — 57 of 68 leaves — and for the first time there is direct evidence that the queue is ahead of the code: the fixes behind at least two of this weekend's twenty QA submissions were written a day *after* the items were submitted, and are still not on `main`.** Nothing left REVIEW/QA; nothing was accepted; only five leaves are still open. Separately, the one backend merge of the window exposed something every previous edition missed: **no real payment on this product has ever used escrow**, because the client's in-chat Send calls the instant-transfer endpoint. The client fix exists — on the same unmerged branch — alongside a biometric PIN-bypass the server does not support and should not support as written. And `beevia-db-schema`'s `main` was **force-pushed** over the weekend.

**Corrections to previous editions — read these first.**

1. **Capability #7 was scored on a wrong premise, and the MVP estimate falls 1.2 points because of it.** The 25 September appendix (and several before it) justified 0.95 with: the client's send path posts `/payments/transfer`, and "the REST `/payments/send` … being unused by the client is expected — they are the HTTP mirror of the socket commands". That is false in both halves. Until 25 September **the socket had no send command at all** — only request/accept/decline/cancel — and `/payments/transfer` is, by its own spec, *"no escrow and no accept step"*. The PRD's *Transfer Acceptance & Escrow* (§10.2; Flow 5; §11 Phase 3) has been built on the server and bypassed by every client send. The backend's own commit message (#57) states the consequence: **all six payments on production went through `/payments/transfer`, none escrowed.** #7 is re-scored **0.95 → 0.85** (§Appendix). No weight changed.

2. **`api-rfc.md` §6.9 has understated the socket surface for weeks.** It listed 30 commands and a parity table saying payments were REST-only. Re-counted from `origin/main`: **38 commands**, including `payment.request`, `accept`, `decline`, `cancel` — and, since Friday, `step_up` and `send`. Corrected.

3. **"David holds 40 of 68 leaves" (25 Sep) was an arithmetic slip.** That edition's own breakdown (17 + 6 + 16 + 5 + 2 + 2) sums to **48**, and no assignment changed in this window. Today's figure is 48.

| Metric | 25 Sep | 28 Sep | Δ |
|---|---:|---:|---|
| Sprint 0901 items (leaves + parents) | 77 (68+9) | **77 (68+9)** | 0 — no items added for the first time in three editions |
| API surface (consumer / admin) | 137 / 49 | 137 / 49 | **0** |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | 0 |
| Spec drift vs `origin/main` (route level) | 0 | **0** | 0 |
| **Socket commands** (not covered by the route audit) | "30" | **38** | +2 real (`payment.step_up`, `payment.send`); +6 corrected |
| Sprint 0901 leaves To do | 17 | **2** | **−15** |
| Sprint 0901 leaves In progress | 5 | **1** | −4 |
| Sprint 0901 leaves BLOCKED | 2 | 2 | 0 |
| Sprint 0901 leaves REVIEW/QA | 38 | **57** | **+19** |
| Sprint 0901 leaves Done | 6 | 6 | **0 — eighth edition flat** |
| Review queue as a share of the board | 56% | **84%** | **+28 pts** |
| Review-queue median age (0901) | 2.3 d | **3.9 d** | +1.6 |
| Oldest item in the queue | 16.9 d | **19.9 d** | +3.0 |
| Items that left REVIEW/QA in the window | 0 | **0** | 0 |
| Items in REVIEW/QA whose fix is verifiably not on `main` | — | **≥2** (`BVA-I287`, `BVA-I303`) | new measure |
| `beevia-api` / `beevia-admin-api` days since a commit | 0.6 / 1.0 | **3.0 / 4.1** | |
| `beevia-db-schema` days since a commit | 0.6 | **3.7** — and `main` rewound by force-push | |
| `beevia-mobile` days since a commit on `main` / on any branch | 0.9 / — | **3.9 / 1.0** (`update-fixes`) | |
| `beevia-admin` days since a commit | 2.9 | **5.9** | +3.0 |
| Admin board: days since *any* activity | 10.9 | **14.0** | +3.1 |
| Ayomikun commits (7d, both identities, `origin/main`, non-merge) | 35 | **27** | rolling window |
| David commits (7d) — merged to `main` / on `update-fixes` | 3 / — | **3 / 2** | |
| Promise commits (7d, merged) | 2 | 2 | 0 |
| Unmerged `beevia-mobile` feature branches | 0 | **1** (`update-fixes`, 2 ahead, 68 files under `lib`/`test`/`api-docs`) | +1 |
| Estimation points set (0901 / 0901-admin / 08-01) | 0 / 77 · 0 / 12 · 0 / 64 | same | 0 |
| **Sprints open on either board** | 0 | **0** | 0 |
| MVP readiness (estimate) | ≈67% (66.72) | **≈66% (65.52)** | **−1.20 — correction, not regression** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **21 on 0901, all REVIEW/QA** (15 solely) · 3 on 0901-admin | 9 | 0.98 d (n=10) | **0** on 0901 · 1 on 0901-admin (`BVA-I8`, **14.0 d**) | **27** | His queue half has a median of **10.5 d** and holds the oldest item on the board (19.9 d). Shipped escrowed send over the socket (#57) — the most product-relevant backend change in a week |
| David Samuel | mobile | **48 on 0901** — 42 REVIEW/QA (34 solely), 2 BLOCKED, 1 In progress, 1 To do, 2 Done | **42** (10 moved by board administration) | 0.96 d (n=24) | 3 — `BVA-I277` In progress 3.9 d; `BVA-I260`, `BVA-I275` BLOCKED 5.1 d | **3 merged · 2 unmerged** | **The code for this weekend's QA moves is on `update-fixes`, not `main`**, and at least two fixes were committed a day after the items were submitted (§1.3) |
| Philip Chidera | design | 7 on 0901 — 4 Done, 2 REVIEW/QA, 1 To do (`BVA-I298`, 4.0 d) | 2 | 0.55 d (n=2) | 0 in progress | — | `BVA-I298` has sat in To do for four days — the only design-owned open item |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 In progress | 0 | — | 1 (`BVA-I9`, **14.0 d**) | 2 | `beevia-admin` **5.9 days** without a commit, the longest gap since the board went live; admin board silent for two weeks |

**The two questions for standup:** (1) **When does `update-fixes` merge — and until it does, what is QA testing?** Twenty items moved to REVIEW/QA since Friday; the code behind them is on a branch. (2) **Who force-pushed `beevia-db-schema` `main`, and was that meant to be possible?** It removed the `v0.0.38` release commit and left the `v0.0.38` tag pointing at a commit on no branch.

**The three things worth knowing:**

1. **REVIEW/QA has stopped meaning "ready for review".** The queue grew 38 → 57 in three days while the open set collapsed from 24 to 5 — every remaining To do item was emptied into it. Ten of the twenty moves were made by board administration on Friday in eight minutes (six straight from To do, never started); ten were David's on Saturday morning, eight of them also straight from To do. `beevia-mobile` `main` has had no commit since Thursday. The fixes live on `origin/update-fixes`, and content checks show at least two of them — `BVA-I287` (profile "Request money" button wired from `onTap: () {}` to a real handler) and `BVA-I303` (wallet title spacing) — **were committed on Sunday, 29 hours after the items were submitted**. Anyone testing a `main` build will find them unfixed. This is not a statement about anyone's diligence; it is what a board without a "fix on branch / awaiting merge" state does when there is no reviewer, and it makes the queue's size meaningless as a measure of finished work.

2. **Escrow has been built for weeks and bypassed by every real payment.** `beevia-api` #57 added `payment.step_up` and `payment.send`: the PIN gate moves from an HTTP header to the socket connection, armed only until the step-up token's own expiry, per socket. The commit's stated reason is the finding — the client's chat Send uses `/payments/transfer`, which credits instantly with no accept step and no 24-hour return, and all six production payments went that way. The client change to use escrow is written (`update-fixes`), unmerged. It also inherits the one unparsed phone field in the service: `payment.send` reuses `sendMoneySchema`, whose `recipientPhone` is still a bare `min(6).max(20)` string (`suggestions.md` §3.6, escalated a third time).

3. **The same client branch assumes a biometric step-up the server does not have.** `update-fixes` offers "use biometrics" next to the PIN on every money-moving sheet, and implements it by posting `{ "method": "biometric" }` to `POST /auth/step-up`. The server's schema is `{ pin }` only, so it will fail against the real API; the branch edits the vendored spec and the mock server to accept it, so the client's own tests pass. **This needs a design decision before a line of server code** — a step-up minted on the client's word that a prompt succeeded verifies nothing, and would reduce the PIN gate to "has a session". The standard shape is a device-bound key signing a server nonce (`suggestions.md` §5.11).

**If you read nothing else:** the queue swallowed the rest of the board over the weekend, the code behind it is on an unmerged branch, that branch both fixes the escrow bypass and introduces a biometric step-up the server cannot verify, and a backend `main` was force-pushed.

---

## 1. Sprint 0901 — closed 22 Sep, still the working board

**77 items: 68 leaves + 9 parent Stories.** All figures below are leaves unless stated. No item was added or removed in the window — the first window without a QA batch since 22 September.

### 1.1 Status distribution

| Status | 25 Sep | 28 Sep | Δ |
|---|---:|---:|---:|
| REVIEW/QA | 38 | **57** | **+19** |
| To do | 17 | **2** | **−15** |
| In progress | 5 | **1** | −4 |
| BLOCKED | 2 | 2 | 0 |
| Done | 6 | **6** | **0** |
| **Total leaves** | **68** | **68** | 0 |

The deterministic audit's `SINCE` section, run against the two 0901 scratch exports: **19 entered review, 0 left, 0 newly Done.** Its two problems — *57/68 in REVIEW/QA after the sprint's end* and *nothing left REVIEW/QA* — are both real.

### 1.2 Everything that moved

Twenty-two audit entries in the window, all status changes. No comments, no creations, no re-assignments.

| When (UTC) | Items | Move | Actor |
|---|---|---|---|
| Fri 25 Sep 12:58 | `BVA-I294` | To do → In progress | David Samuel |
| **Fri 25 Sep 16:04–16:08** | `BVA-I279`, `BVA-I295`, `BVA-I296`, `BVA-I294` | In progress → REVIEW/QA | board administration |
| **Fri 25 Sep 16:09–16:12** | `BVA-I264`, `BVA-I288`, `BVA-I291`, `BVA-I292`, `BVA-I299`, `BVA-I302` | **To do → REVIEW/QA** | board administration |
| Sat 26 Sep 08:35 | `BVA-I285`, `BVA-I287` | To do → In progress | David Samuel |
| **Sat 26 Sep 09:06–10:10** | `BVA-I285`, `BVA-I287` | In progress → REVIEW/QA | David Samuel |
| **Sat 26 Sep 09:06–10:10** | `BVA-I290`, `BVA-I293`, `BVA-I304`, `BVA-I303`, `BVA-I300`, `BVA-I265`, `BVA-I258` | **To do → REVIEW/QA** | David Samuel |

Two of Friday's moves are worth naming. `BVA-I295` (no ringback tone) and `BVA-I296` (no date grouping) are the two items the backend developer declined in writing on 24 September as mis-routed; both went to REVIEW/QA without any further comment on either. And `BVA-I294` was moved to QA three hours after its owner had started it.

### 1.3 The queue is ahead of the code

`beevia-mobile` `main`'s last commit is PR #36, 24 Sep 16:32 UTC — before every move in the table above. The only mobile code written since is on **`origin/update-fixes`**: two commits by `Davidtariq96` (24 Sep 14:31 UTC and **27 Sep 14:22 UTC**), 2 ahead of `main` and 2 behind, touching 68 files under `lib/`, `test/` and `api-docs/` (+2,634 / −946).

Checked by content, not commit message (the messages are "fixes and improvements" and "fixes"):

| Item | Submitted to QA | Where the fix is | Committed |
|---|---|---|---|
| `BVA-I287` Request Money button on profile not working | Sat 26 Sep 09:06 | `contact_profile.dart`: `onTap: () {}` → `onTap: _requestMoney` | **Sun 27 Sep 14:22** (`99c8909`), unmerged |
| `BVA-I303` Excessive spacing between wallet title and content | Sat 26 Sep 09:29 | `wallet_screen.dart`: `SizedBox(height: 42)` removed | **Sun 27 Sep 14:22** (`99c8909`), unmerged |

The branch's other files map plausibly onto more of the weekend's items (the attachment menu, card-benefit icons, chat widgets, money-request card labels), but only these two were verified line by line, so only these two are claimed.

**What this means for the queue.** A reviewer testing `main` on Saturday would have found both items unfixed; one testing it today still would. REVIEW/QA is being used for "I have this in hand" or "fix is on my machine" rather than "ready to verify", and with no reviewer there has been no pressure to tell those apart. The fix is a board convention, not a person: either a "fixed on branch" status, or a rule that an item enters REVIEW/QA when its code is on `main`.

### 1.4 The review queue — 57 items

Ages are the `actiontime` of each item's last transition into REVIEW/QA, from the activity sidecar.

| | Items | Median age | Oldest |
|---|---:|---:|---:|
| Ayomikun Araoye | 21 | **10.5 d** | **19.9 d** |
| David Samuel | 42 | 3.6 d | 13.9 d |
| Philip Chidera | 2 | 3.4 d | 3.9 d |
| **Whole queue** | **57** | **3.9 d** | **19.9 d** |

(65 owner-rows across 57 items — eight are co-assigned.) The seven-item Notification block submitted on 8 September is now **19.9 days old**. Ayomikun's half has not changed in composition since 24 September; it has simply aged three days. **One item in the project's history has made the REVIEW/QA → Done transition on sprint 0901** (`BVA-I268`, 16 Sep, closed by its own owner); none has been accepted by anyone other than its submitter.

### 1.5 What is open

Five leaves.

| Item | Status | Age | Owners |
|---|---|---:|---|
| `BVA-I260` Face verification shows static placeholder | BLOCKED | 5.1 d | David |
| `BVA-I275` Sender/receiver profile pictures swapped | BLOCKED | 5.1 d | David |
| `BVA-I277` New chat shows incorrect phone numbers for invites | In progress | 3.9 d | David |
| `BVA-I297` Inconsistent section divider styling | To do | 4.0 d | David |
| `BVA-I298` Message text / timestamp lack contrast | To do | 4.0 d | Philip |

`BVA-I260` and `BVA-I275` are **disputed, not blocked**: each carries a written argument from David (23 Sep) that the reported behaviour is intended. **No reply in five days, and no comment of any kind was added to the board in this window.** `BVA-I277` has exceeded David's 0.96-day median cycle four-fold; it is also the item on which he asked for a screenshot on 23 September, with no reply.

---

## 2. Admin dashboard board — `0901-admin`

**12 items: 8 leaves + 4 parent Stories. Unchanged in every respect.**

| Status | Leaves |
|---|---:|
| Done | 6 |
| In progress | 2 |

| Item | Status | Owner |
|---|---|---|
| `BVA-I5` · `BVA-I11` | Done | Ayomikun Araoye |
| `BVA-I6` · `BVA-I12` · `BVA-I15` | Done | Promise Udo |
| `BVA-I14` | Done | Unassigned |
| `BVA-I8` — Report Data Query | **In progress, 14.0 d** | Ayomikun Araoye |
| `BVA-I9` — Report Content Display | **In progress, 14.0 d** | Promise Udo |

**Last activity of any kind: 14 September 14:53 UTC — exactly two weeks ago.** `beevia-admin` has had no commit since 22 September (**5.9 days**) and `beevia-admin-api` none since 24 September (4.1 days). This is the first edition in which both the board and both repos of the admin workstream are silent at once. Its counts are never added to the main sprint's.

---

## 3. API surface and spec drift

**Audit: route level clean, spec health clean.** `beevia-api` code 137 / spec 137 · `beevia-admin-api` code 49 / spec 49 · proposed 38 / 18 · no `x-beevia-*`. Run against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-28`, and re-run clean after this cycle's edits. The in-repo audit reports 21 "in spec, not in code" lines (6 consumer + 15 admin); these are the known phantom drift from the three `diverged` working trees and were not acted on.

**Fourth consecutive cycle in which the most consequential change was invisible to the route audit** — this time because it is a socket command, which no OpenAPI route diff (including the CI one this report keeps recommending) will ever see.

### 3.1 `beevia-api` #57 — escrowed send over the socket

Merged Fri 25 Sep 14:57 UTC (`feat/ws-payment-send`, one commit by `Phoenixdadhev`). The only backend merge in the window.

- **`payment.step_up { stepUpToken }`** verifies the token `POST /auth/step-up` already mints and records `stepUpUntil` on *that socket*, equal to the token's own expiry. Never extended, never refreshed by activity; a second socket is not armed by the first.
- **`payment.send`** takes the `POST /payments/send` body and answers `step_up_required` until the socket is armed. It calls the unchanged `PaymentService.send` — hold, reserve, 24-hour auto-return, card in the thread.
- **Verification is now one implementation.** `TokenService.verifyStepUp` is shared by `StepUpGuard` (header) and the gateway (socket). A token without an `exp` is treated as already lapsed.

This is a well-shaped change. One property to keep in view: an armed socket can spend repeatedly until expiry (default 5 minutes), where the header path presents the token per request. Equivalent while the TTL stays short; worth re-checking if anyone lengthens it.

The commit also records that the five `beevia-api/docs/` files, including the WebSocket integration guide, were deleted from `main` by the 22–24 September package-update PR, so the new commands are documented in Postman only. `openapi.yaml` pointed readers at that deleted guide; corrected.

### 3.2 The finding behind it: escrow has never carried a real payment

The PRD makes transfer acceptance an MVP mechanic: funds reserved on the sender's ledger, an incoming card the recipient accepts or declines, automatic return after 24 hours (§10.2 *Transfer Acceptance & Escrow*; Flow 5; §11 Phase 3). The server has implemented that since the payments module shipped. **The client has never used it for a send.** `chat_send_money_flow.dart` → `WalletProvider.transferMoney` → `POST /payments/transfer` — which the spec describes as moving money "immediately — no escrow and no accept step". Per #57's commit, all six production payments went that way.

This report scored capability #7 at 0.95 for weeks on the reading that this was expected. It was not (correction #1).

The client change exists: `update-fixes` adds `PaymentEvents.armStepUp()` and `sendPayment()` and routes the chat send through them. Until it merges, `main` bypasses escrow.

### 3.3 The same branch: a biometric step-up the server does not implement

`update-fixes` also adds `WalletService.requestBiometricStepUpToken()` — `POST /auth/step-up` with `{ "method": "biometric" }` after a local `local_auth` prompt — and offers it next to the PIN on five confirmation sheets (both chat money flows, bank transfer, card request, a wallet sheet). The server's `stepUpSchema` is `z.object({ pin })`. On the real API every biometric confirmation will fail validation. The branch edits the vendored `api-docs/openapi.yaml` and the mock server to accept the body, so its contract test passes.

The PRD does ask for "biometric or PIN confirmation on every financial action", so the requirement is legitimate. The server should **not** add it as the client currently frames it: a body saying "the prompt succeeded" is something any access-token holder can send, and minting a step-up token for it would reduce ADR-0003 to "has a session". Recorded as `suggestions.md` §5.11 with the standard device-bound-key design. `openapi.yaml` now states explicitly that the PIN is the only accepted factor.

### 3.4 Spec and document changes this cycle

| File | Change |
|---|---|
| `openapi.yaml` | *Transports* section: removed the pointer to the deleted `docs/chat-websocket-integration.md`; documented the connection-level step-up (`payment.step_up` → `payment.send`). `POST /auth/step-up`: socket arming; PIN is the only factor, no biometric body. `POST /payments/send`: its socket twin, and that send is the only path with an accept step. Prose only — no path, schema or operation added. |
| `api-rfc.md` | **§6.9 corrected** — 38 commands, not 30; parity table split so payments show on both transports (correction #2). §6.7 — escrow built but never used by a real payment. **New §5.11** — #57, the escrow bypass, the phone-field inheritance, and the biometric assumption. |
| `suggestions.md` | **§3.6 escalated a third time** — `payment.send` reuses the unparsed `recipientPhone`. **§5.10 updated** — the vendored client spec now declares server behaviour that does not exist, not merely stale behaviour. **New §5.11** — biometric step-up design; added as item **3e** in §8. |

`openapi.proposed.yaml`, `openapi.admin.yaml`, `openapi.admin.proposed.yaml` and `admin-api-rfc.md` needed no change: no proposed operation shipped, and `beevia-admin-api` has had no commit since the last edition.

---

## 4. Risks

### 4.1 `beevia-db-schema` `main` was force-pushed

Between the 25 Sep and 28 Sep fetches, `origin/main` moved from `e285f10` to `30651b3` as a **forced update** — the only one in any of the five repos' reflogs this window. Diffed:

- The rewrite **removed exactly one commit**, `e285f10 chore(release): v0.0.38 [skip ci]` by `github-actions[bot]` — a one-line `package.json` version bump. `30651b3` is its parent. **No content was added**; the new `main` is a strict ancestor of the old one.
- **Tag `v0.0.38` still points at `e285f10`, which is now on no branch.** `main`'s `package.json` says `0.0.37`; per `30651b3`'s own message, `0.0.38` is already on the registry.

The likeliest reading is someone repairing a half-finished release by hand; `30651b3` is itself a fix to let "a half-finished release be re-dispatched to completion". It is benign in content. **It is not benign as a signal.** After the 8 September incident, the standing recommendation (`suggestions.md` §7.1) was branch protection with force-push disabled on all five repos, and nine editions have reported that as unverifiable from here. It is now verified in the negative for this repo: **force-pushing `main` on `beevia-db-schema` was possible this weekend**, for whoever did it. Who pushed cannot be seen from a clone.

The next release run will find `main` at `0.0.37`, the registry at `0.0.38` and a `v0.0.38` tag already present. Whether it re-bumps to `0.0.38` on a new commit (leaving the tag pointing somewhere else) or skips is for the workflow owner to confirm.

### 4.2 Standing risks, updated

- **Review queue** — 84% of the board; see §1.3–1.4.
- **`payments.dto.ts` phone field** — now the input to every chat send once `update-fixes` merges (§3.2).
- **Vendored client spec** — now wrong in both directions (`suggestions.md` §5.10).
- **No sprint open** on either project; fifth edition.
- **Three diverged local working trees** (`beevia-api` behind 57, `beevia-admin-api` 34, `beevia-db-schema` 42 — the last *fell* by one because its `origin/main` was rewound, §4.1).

---

## 5. PRD gap

No capability *gap* closed, and one capability line was found to be less complete than reported (#7, correction #1). The four structural gaps — international KYC tier, multi-currency/FX settlement, virtual cards beyond what is wired, consent management — are where they were.

Re-verified at `origin/main`: `PaymentService.activeNgn()` at `payment.service.ts:506`, called from lines 70, 128 and 288. `StubTranslateAdapter` still bound at `translate.module.ts:23`.

---

## 6. Team performance — detail

All flow figures are from the activity sidecars (`actiontime` of the relevant transition), never from `Last Modified`. Commit counts are non-merge commits on `origin/main` since 21 Sep 14:05 UTC, summing each person's git identities; David's unmerged branch commits are shown separately.

### 6.1 Ayomikun Araoye — backend + admin API

**27 commits in 7 days**: `beevia-api` 13 (`Phoenixdadhev` 11, `Ayomikun Araoye` 2), `beevia-db-schema` 12 (11 + 1; two bot commits excluded), `beevia-admin-api` 2. Down from 35 in the last edition because the seven-day window rolled forward over a quiet weekend; his last commit is Friday's #57.

**All 21 of his 0901 items are in REVIEW/QA**, 15 solely his, median age 10.5 days, oldest 19.9. He has no open work on the main board and one admin-board item In progress for 14.0 days. Median cycle time In progress → REVIEW/QA 0.98 days (n=10); 9 submissions in seven days; he made no board action of his own in this window.

#57 is the most product-relevant backend change in a week, and its commit message is the clearest written statement anyone on the project has made of a PRD gap: it names the escrow bypass, quantifies it from production, and explains the design constraint that had kept send off the socket. **His queue profile remains a process finding, not a personal one** — nothing he does can move items out of a column nobody reviews.

### 6.2 David Samuel — mobile

**42 submissions to REVIEW/QA in 7 days** (owner-rows; 10 of them moved by board administration on Friday), median cycle 0.96 days (n=24). He owns 48 of 68 leaves, including 42 of the 57 queue entries (34 solely) and four of the five open items.

**Commits: 3 on `main` in seven days** (authored 21–22 Sep, landed with PR #35 on 23 Sep) **plus 2 on `update-fixes`**, the second on Sunday afternoon. The branch is substantial — 68 files, +2,634 / −946 — and contains real work the board is asking for: the escrowed send, the profile request-money button, spacing and icon fixes, call-audio routing, conversation-provider changes.

The pattern in §1.3 — items submitted before their code exists on `main`, some before it was committed at all — **is not a statement about effort**, and on this evidence the effort is visibly there. It is what a board with no reviewer and no "fixed on branch" state produces: submitting early costs nothing and nobody checks. The concrete asks are process ones: merge the branch, or agree that REVIEW/QA means "on `main`".

### 6.3 Philip Chidera — design

Two items in REVIEW/QA (`BVA-I274`, `BVA-I296` co-owned), one To do (`BVA-I298`, message/timestamp contrast, **4.0 days**, unstarted). No movement of his own in the window. No commits; design work does not land in these repositories.

### 6.4 Promise Udo — admin dashboard

2 commits in 7 days, both on 22 September. **`beevia-admin` has now gone 5.9 days without a commit**, and the admin board 14.0 days without activity; `BVA-I9` has been In progress for all fourteen. He has made no board action anywhere, ever — every transition on the admin board was made by someone else. **Absence of data is not absence of work**: the dashboard may be progressing on a local branch this pipeline cannot see (`beevia-admin` has no remote branch other than `main`). But there is now no signal in either direction, and it is worth one question.

### 6.5 Weekly submission trend (sprint 0901, transitions into REVIEW/QA)

| ISO week | Submissions |
|---|---:|
| 2026-W37 | 9 |
| 2026-W38 | 15 |
| 2026-W39 | **44** |
| 2026-W40 (from Mon 28 Sep) | 0 so far |

W39 nearly tripled W38 — and W39 includes the twenty weekend moves of §1.2, eight of which went straight from To do, so the rise measures status changes more than completed work. **Acceptances over the same three weeks: one** (`BVA-I268`, 16 September, closed by its own owner). When submissions triple and acceptance is one self-closure, the bottleneck is not the developers; no reviewing role is staffed, and this is the tenth consecutive edition saying so.

### 6.6 What this does not measure

- **No estimation points on any of 77 items** (nor on 12, nor on 64). Item counts say nothing about who is carrying more. Seventeenth edition.
- **Commit counts reward small commits; cycle times reward small items.** 27 backend commits against 3 + 2 mobile ones is not a comparison of output — David's second branch commit alone touches 36 files.
- **"Submitted" counts any transition into REVIEW/QA, by anyone**, attributed to the item's owner. Ten of David's 42 were moved by board administration.
- **Co-assignment is counted for both owners.**
- **Nothing here measures correctness.** No build, test or lint was run in any repository.

---

## 7. Previous recommendations — where they stand

| Recommendation from 25 Sep | Status on 28 Sep |
|---|---|
| **1. Stop the mobile repo reading a stale spec** | ❌ **Not done, and it moved the wrong way.** `main` is unchanged (still 27 operations short; `/wallets/banks`, `/wallets/resolve-account`, `/cards` still on `knownSpecDrift`). `update-fixes` edits the vendored copy to *add* a biometric step-up body the server does not accept (§3.3) |
| **2. Say out loud who reviews** | ❌ **Not done.** The queue went 38 → 57; nothing left it. Tenth edition |
| **3. Open sprint 0902 on both boards** | ❌ **Not done.** Zoho still lists `0901, 08-01, 0702, 0701` and `0901-admin`. Fifth edition |
| **4. Decide whether nineteen bugs to one person is the plan** | ❌ **No reassignment.** No item changed owner in the window; David holds 48 of 68 leaves (correction #3) |
| **5. Reply to the two disputed items** | ❌ **Not done.** `BVA-I260` and `BVA-I275` BLOCKED 5.1 days; no comment of any kind was added to the board in three days |
| **6. Bring `payments.dto.ts` onto `phone.util.ts`** | ❌ **Not done — and it now has a third caller** (`payment.send`, §3.1) |
| **7. Generate both OpenAPI documents in CI and diff them** | ❌ **Not done.** Honest caveat this cycle: it would *not* have caught #57, which is a socket change. It would have caught the previous three cycles' |
| **8. Copy `code-scan.yml` into `beevia-mobile` and `beevia-admin`; bring `beevia-db-schema` onto it** | ❌ **Not done.** `beevia-admin` still has no `.github/`; `beevia-mobile` still has `flutter-ci.yml`, `main.yml`, `pr.yml` and no security scan |
| **9. Estimation points on sprint 0902 as it is created** | ❌ Not done — no sprint 0902 |
| **10. Carried: `reports.service.ts` read-scoping; Module 4 decision record; `beevia-api/docs/`; the translation decision** | ❌ **None done.** #57's own commit message notes the `docs/` deletion; `beevia-admin-api` has had no commit, so §4.7 is unchanged by definition |
| *(24 Sep, carried in §6)* Confirm branch protection / force-push is disabled | 🔴 **Answered in the negative for `beevia-db-schema`** — `main` was force-pushed this weekend (§4.1) |

**None of ten resolved.** The window was a weekend; three of the ten are one-line or one-comment actions.

---

## 8. What I would do this week

1. **Merge `update-fixes` — or say why not — and agree what REVIEW/QA means.** Twenty items entered the queue on the strength of code on that branch; at least two were submitted before the code was committed. Pick one rule and write it on the board: an item enters REVIEW/QA when its fix is on `main`, or a "fixed on branch" status is added. Either makes the queue mean something again.
2. **Before it merges, take the biometric option out of the real-API build.** The server rejects `{ method: biometric }`, so the button fails on every money sheet. Then decide the design (`suggestions.md` §5.11: device-bound key, server nonce, signed response). This is a decision for the backend lead and the owner, not a patch.
3. **Bring `payments.dto.ts` onto `phone.util.ts` first.** One import, one deleted line. Once `update-fixes` merges, every chat send goes through `payment.send` and its unparsed `recipientPhone` (§3.1–3.2).
4. **Find out who force-pushed `beevia-db-schema` `main`, and turn force-push off.** The content was benign; the capability is the finding. While there, decide what the orphaned `v0.0.38` tag should point at before the next release run (§4.1).
5. **Name a reviewer.** 57 of 68 leaves. Tenth edition. One name against the word, or an explicit decision that REVIEW/QA means done.
6. **Open sprint 0902 on both boards**, carrying over the five open items and whatever of the 57 is genuinely unverified. Fifth edition.
7. **Reply on `BVA-I260`, `BVA-I275` and `BVA-I277`.** Two written disputes and one request for a screenshot, all five days old. Three comments.
8. **Stop vendoring the spec in `beevia-mobile`** (`suggestions.md` §5.10). It is now wrong in both directions.
9. **Ask about the admin workstream.** Two weeks of board silence, six days of repo silence, two items In progress for fourteen days. A one-line answer is enough.
10. **Carried, unchanged:** OpenAPI generation diffed in CI; `code-scan.yml` into `beevia-mobile`/`beevia-admin`; the `reports.service.ts` read-scoping fix (thirteenth edition); the Module 4 decision record; restoring or retiring `beevia-api/docs/`; writing the translation decision down; estimation points on 0902.

---

## Appendix — method and readiness rubric

### MVP readiness — ≈66% (estimate; 65.52, −1.20)

**Target 2026-09-01 (provisional) · the target date passed twenty-seven days ago.** Weights frozen — **no methodology change this edition.** Scores measure build, not acceptance.

**One score moved, down, on corrected evidence** (correction #1). Nothing was un-built; the line was over-scored.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No change to crypto, keys or sockets on `main`. `BVA-I292` (E2EE notice missing) is in REVIEW/QA; **board status does not score** |
| 2 | Voice & video calling | 8 | 0.80 | 0 | No `/calls` change. `update-fixes` touches `call_provider.dart` and `call_audio_route.dart` — unmerged, does not score |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter`; the client translates on-device. `/translate/batch` the only proposed `/translate` op |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` re-verified at `payment.service.ts:506`, called from 70/128/288 |
| 7 | Send / request / receive in chat | 12 | **0.85** | **−0.10** | **Corrected.** Request, accept, decline and cancel are wired over the socket (`payment_events.dart` ↔ `messaging.gateway.ts`). **Send is wired to the wrong mechanic:** the chat flow posts `/payments/transfer` (`wallet_service.dart:167`), which settles instantly with no accept step or 24-hour return, so the PRD's escrow for sends (§10.2, Flow 5, §11 Phase 3) is never exercised — per #57's commit, zero of six production payments were escrowed. The server-side escrow exists (REST since launch, socket since 25 Sep); the client change is on unmerged `update-fixes`. **Returns toward 0.95 when that merges**, on that named evidence. Still no REST read path for a single payment |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No card endpoint newly wired on `main`. `update-fixes` adds a biometric confirmation to card request that the real API rejects (§3.3) — unmerged, does not score either way |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | `beevia-admin` has had no commit since 22 Sep |
| | **Weighted total** | **100** | **65.52** | **−1.20** | **≈66%** |

Mobile screen inventory on `main` re-counted at **53** (51 under `lib/features/*/screens/` plus two call screens) — unchanged.

### What this report cannot tell you

- **Whether any of the 57 queued items is fixed on `main`.** Two are verifiably not; the rest were not checked line by line, and no build was run.
- **What the Friday To do → REVIEW/QA moves by board administration meant.** Six items went to the queue unstarted, with no comment. Re-test requests, a status convention, or a bulk tidy — the board does not say.
- **Who force-pushed `beevia-db-schema`**, or whether branch protection exists on the other four repos. A clone sees the rewrite, not the actor; the `gh` token here gets `404` on every repo's rules endpoint.
- **Whether `update-fixes` builds or passes its tests**, or when it will merge.
- **Whether `payment.step_up` / `payment.send` work end to end.** Nothing was executed; the commit reports a manual socket check.
- **What the admin dashboard work looks like this week.** No commit, no board activity.
- **Velocity for any of the three sprints** — 0 of 77, 0 of 12, 0 of 64 items estimated.

### Method

**Pipeline.** `beevia-refresh`: sprint-name discovery on both projects (no successor sprint on either) → main board export (64 items, sprint 08-01, exit 0) → admin board export with `--sprint 0901-admin` (12 items, exit 0) → read-only scratch export of sprint 0901 to `/tmp/beevia-scratch/` (77 items, exit 0) → fast-forward sync (**0 repos advanced; 2 already current; 3 refused as `diverged`**; exit 1) → `git fetch` and reflog sweep of all five repos for forced updates (**one found**, §4.1) → audit against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-09-28`, with the 25 and 28 Sep 0901 scratch exports copied in so the `SINCE` delta covers the active sprint → activity-sidecar sweep for the window (status transitions, comments, and completions matched on all three Zoho action names) → content reads of #57, the mobile send path on `main`, and `origin/update-fixes` (diffed against its merge-base, not by ancestry) → spec and document edits → audit re-run (clean) → this report and its web edition.

**Flow figures come from the activity sidecars, never from `Last Modified`.** Queue ages are the `actiontime` of each item's last transition into `REVIEW/QA`, measured to 28 Sep 14:05 UTC; cycle times are `In progress` → `REVIEW/QA` pairs; WIP ages are the entry into the current status.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is performed by a non-contributor whose transitions are reported without naming the actor; ten of this window's twenty-two audit entries are theirs.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran; no repository was reset, rebased or cleaned; no sub-repo file was edited; the sync's `--ff-only` limit was not overridden. `git fetch` and `git archive` were the only operations beyond the sync. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-09-28.html`, `web-report/index.html`, `openapi.yaml` (prose only), `api-rfc.md`, `suggestions.md`; new board exports for 28 Sep in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **No open sprint on either board.** Both closed 22 September with no successor. Fifth edition.
- **Three repositories remain unsynced** — `beevia-api`, `beevia-admin-api`, `beevia-db-schema` `diverged` (`ahead 1`, behind 57 / 34 / 42). Every backend claim is made against `origin/main` via the shadow. The in-repo audit's 21 drift lines are artefacts of this and were ignored.
- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint (41 leaves, all Done, last activity 3 Sep). All sprint-0901 figures come from the scratch export.
- **GitHub settings are unobservable** except where a forced update shows up in a reflog.
- **Whether any CI run passed is unknowable from a clone.**
- **The export's "no source key" warning fired on `Epic` again** — the known 50-row sampling artefact, not an OAuth scope gap.
- **Repository integrity: reflog sweep only.** A forced-update scan of all five repos ran; a full content hash sweep did not.

**Window.** 25 Sep 12:58 UTC → 28 Sep 14:05 UTC. All `actiontime` and board figures are UTC; `git log` timestamps were converted from their local offsets where quoted.
