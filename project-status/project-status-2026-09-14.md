# Beevia — Project Status

**As of 2026-09-14** · Sprint **0901** (3 Sep → 22 Sep) — **day 12** · Sprint **0901-admin** (3 Sep → 22 Sep) — **day 12** · Sprint **08-01** (11 Aug → 28 Aug) — closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-09-14.csv` + `beevia-activity-2026-09-14.json` (64 items, sprint 08-01); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-09-14.csv` + its activity sidecar (12 items); a read-only scratch export of sprint 0901 (29 items); all five repos read at `origin/main`.

Scope: three boards, kept separate and never summed. Window **11 Sep 14:01 UTC → 14 Sep 14:03 UTC** (3.0 days, containing a weekend).

---

## Quick overview

> **The stall is over, and the first thing to say is that it was never quite real. Six items were marked Done and four new ones created on Friday 11 September — all of them between 19 and 103 minutes *after* the previous edition's cut-off, which is why that edition called the day "fully static". The window was genuinely empty; the day was not, and the headline claim built on it was wrong. Since then three things landed that this report has been asking for: Promise shipped the real Reports module, deleting the mock file and wiring all five endpoints; David pushed his first mobile commit in seven days, containing an actual on-device translation engine; and the org supply-chain guard went live in the three backend repositories. None of it is unqualified good news — the mobile work is on an unmerged branch that is now 39 days old, and four items were marked Done before the code for them existed anywhere.**

| | 11 Sep | 14 Sep | Δ |
|---|---:|---:|---:|
| Commits merged to `main`, all five repos, in window | 0 | **4** | **+4** |
| Commits on *any* ref, all five repos, in window | 0 | **6** | **+6** |
| Board transitions, all three boards, in window | 0 | **6** | **+6** |
| API surface (consumer / admin) | 137 / 47 | 137 / 47 | 0 |
| Proposed operations (consumer / admin) | 38 / 19 | 38 / 19 | 0 |
| Spec drift vs `origin/main`, both services | 0 | **0** | 0 |
| Sprint 0901 leaves, total | 17 | **20** | **+3** |
| Sprint 0901 leaves To do | 2 | **5** | **+3** |
| Sprint 0901 leaves In progress | 7 | **3** | **−4** |
| Sprint 0901 leaves REVIEW/QA | 8 | 8 | 0 |
| Sprint 0901 leaves Done | 0 | **4** | **+4** |
| Admin board leaves Done | 6 | 6 | 0 |
| Review-queue median age (0901) | 2.9 d | **5.9 d** | **+3.0** |
| Oldest open WIP (0901) | 6.9 d | **9.9 d** | **+3.0** |
| `beevia-mobile` `main` days since a commit | 16 | **18.4** | +2.4 |
| `beevia-admin` days since a commit | 3 | **0.1** | **−2.9** |
| Admin client modules on the live API | 8 / 10 | **9 / 10** | **+1** |
| Ayomikun commits (7d, 3 identities, merged) | 20 | **23** | **+3** |
| Promise commits (7d, merged) | 4 | **5** | **+1** |
| David commits (7d, merged to `main`) | 0 | **0** | 0 |
| Estimation points set (0901 / 0901-admin) | 0 / 25 · 0 / 12 | 0 / 29 · 0 / 12 | 0 |
| MVP readiness (estimate) | ≈58% (57.92) | **≈58% (58.10)** | **+0.18 pt** |

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | 10 on 0901 · 3 on 0901-admin | **8** (1 delivery + 7 reconciliation) | 3.0 d | 9: eight in REVIEW/QA (7 at **5.9 d**, 1 at 4.2 d), one In progress (4.2 d) | **23** (was 20) | The 20 → 23 rise is **exactly the three supply-chain-guard commits**, nothing else. His eight review items are now **5.9 d** old with 8 days left in the sprint. One new branch opened today, unmerged |
| David Samuel | mobile | 7 on 0901 — 3 To do, 2 In progress, **2 Done** | **0** — last was 3 Sep, **11.2 d ago** | 2.6 d | 2; ages **9.9 d**, 6.1 d | 0 to `main`; **1 on `origin/BVA-I242`** today | **First commit in 7 days**, and it is real work — an on-device ML Kit translation engine. But it sits on a branch now **15 commits and 39 days** deep, `main` is **18.4 days** cold, and `BVA-I233` is at **3.8× his own median**. Two of his items were marked Done on 11 Sep with no code anywhere |
| Philip Chidera | design | 3 on 0901 — **2 Done**, 1 To do | 0 — last was 28 Aug, **17.1 d ago** | 0.9 d | **0** | — | Closed all six of Friday's items in two bulk actions 7 seconds apart. Four were not his; two were David's. This is not new — he has moved the client-side rows all sprint (§6) |
| Promise Udo | admin dashboard | 4 on 0901-admin — 3 Done, 1 To do | — | — | 0 | **5** (was 4) | **Shipped the real Reports module today.** `mock-data.ts` deleted (462 lines), `api.ts` rewritten against all five endpoints, tests added. The two-edition-old "Done for code that does not exist" finding is **retired for Reports** (§5.1) |

**The two questions for standup:** (1) **When does `BVA-I242` merge?** It now carries 39 days and 15 commits of wallet, transfers and translation work, including the engine `BVA-I229` is blocked on — and none of it counts as delivered, or is visible to anyone, until it lands. (2) **What does Done mean when the code is on a branch?** Four items were marked Done on Friday; the mobile code for two of them was pushed three days *later*, to a branch, and is still unmerged. That is the same question the admin board raised, and Promise just answered his half of it by shipping.

**The three things worth knowing:**

1. **Friday was not a static day, and the previous edition's headline was an artifact of its own cut-off.** Four items were created at **14:20–14:23 UTC** and six were completed at **15:43 UTC** — 19 to 103 minutes after that report's 14:01 cut-off. Its §0.3 named this exact risk (*"what remains unobserved is Friday after 14:01 UTC only"*) and then built the report's headline on the assumption it had not happened. The corrected record has **one** static working day in the pipeline's history, not two (§0.1). The standing recommendation to move the cut-off to ~20:00 UTC has stopped being a tidiness argument: it produced a wrong front page.
2. **Two long-standing "Done but no code" findings moved in opposite directions on the same day.** Promise closed his — the Reports module is now genuinely wired, and the admin client goes from 8 of 10 modules on the live API to **9 of 10**. David's opened — `BVA-I236` and `BVA-I241` were marked Done on 11 Sep, and the mobile code for them was first pushed to `origin/BVA-I242` on **14 Sep**, three days afterwards, where it remains unmerged. The board says 4 of 20 leaves are Done; `beevia-mobile`'s `main` has not changed since 26 August.
3. **The translation architecture is now visible, and it is not the one the server was built for.** David's branch adds `OnDeviceTranslationService` on Google ML Kit — translation happens **on the device**. The only server endpoint the client references is `/translate/preferences`. So `POST /translate`, still bound unconditionally to `StubTranslateAdapter`, appears to have no intended client consumer at all. That is a question worth settling explicitly rather than leaving the stub live (§1.4).

**If you read nothing else:** Friday's "complete stop" was a measurement artifact and is corrected here; the project has genuinely moved since — a real Reports module, a real translation engine, and a supply-chain guard in three repos; but the single biggest risk has sharpened rather than eased, because **every one of the mobile gains is on a 39-day-old unmerged branch** while the board has started marking that work Done, and sprint 0901 has 8 days left with 13 of 20 leaves not finished.

---

## 0. Corrections

### 0.1 Correction — 11 September was not a fully static day, and the claim was the previous edition's headline

**Claim (2026-09-11, quick overview, §1.2 and the masthead): "the second fully static *working* day in the pipeline's thirty-eight-day record", with a table row reading `11 Sep · Fri · 0 commits · 0 board transitions`.**

The activity sidecars now show ten audited actions on 11 September, all after that report's 14:01 UTC cut-off:

| Time (UTC) | Board | Action | Items |
|---|---|---|---|
| 14:20:21 – 14:23:02 | 0901 | 4 items **created** | `BVA-I253` (Story) + `BVA-I254`, `BVA-I255`, `BVA-I256` |
| 15:43:43.414 – .417 | 0901 | 3 **Item Completed**, In progress → Done | `BVA-I241`, `BVA-I239`, `BVA-I240` |
| 15:43:50.132 – .134 | 0901 | 3 **Item Completed**, In progress → Done | `BVA-I236`, `BVA-I234`, `BVA-I235` |

So the corrected row is **11 Sep · Fri · 0 commits · 6 status transitions · 4 items created**, and the corrected count of fully static *working* days in the record is **one — Tuesday 25 August — not two.** Everything the previous edition built on the "second static day" framing (the precedent argument, the "one static working day is not a stall" reasoning, the masthead figure "2 of 38") should be read as describing a day that did not occur.

**What that edition got right, and why it was still wrong.** Its *window* claim was accurate and remains so: between 10 Sep 14:03 and 11 Sep 14:01 UTC nothing happened, and the report said so precisely. The error is the step from "nothing in this window" to "a fully static day" — a 24-hour window ending at 14:01 does not contain the working afternoon that follows it. The report even wrote the disclaimer (§0.3: *"What remains unobserved is Friday after 14:01 UTC only"*) and then published a headline that depended on nothing having happened there.

**Two things follow, and the second is the reusable one:**

- **The events are not lost — they are in this window** (11 Sep 14:01 → 14 Sep 14:03) and are counted once, here. No throughput has been double-counted or dropped.
- **A window figure must not be relabelled as a day figure.** This edition states the window in the headline and reserves calendar-day claims for the reconstruction in §1.2, which is measured to midnight. Where a day is still in progress at the cut-off, it is marked as partial rather than counted.

This is the fourth consecutive edition to open with a correction. The previous three were failures of re-derivation and transcription; this one is different in kind and more serious, because the mistake was **predicted in the same document that made it**. The instrument was understood; the conclusion ignored it.

### 0.2 The cut-off recommendation is no longer a process nicety

Risk #23 and recommendation 9 have asked for six editions that the daily export move from 14:00 UTC to ~20:00 UTC. The argument was hypothetical: *a zero is the one result a too-early cut-off makes hard to interpret.* It is no longer hypothetical — the hypothesis was tested on the next working day and confirmed. **A three-hour shift in the export time would have prevented the wrong headline entirely**, and would have cost nothing.

---

## 1. Sprint 0901 — the active sprint

### 1.1 State — the first completions of the sprint, and the first new scope

29 items — **20 leaves, 9 parent Stories** (was 25 items / 17 leaves). Day 12 of 20.

| Status | Leaves | 11 Sep | Δ |
|---|---:|---:|---:|
| To do | **5** | 2 | **+3** |
| In progress | **3** | 7 | **−4** |
| REVIEW/QA | 8 | 8 | 0 |
| Done | **4** | 0 | **+4** |
| BLOCKED | 0 | 0 | 0 |

| Owner | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Ayomikun Araoye | 10 | 1 | 1 | **8** | 0 |
| David Samuel | 7 | 3 | 2 | 0 | **2** |
| Philip Chidera | 3 | 1 | 0 | 0 | **2** |

Two distinct things happened, both on 11 September and both after the previous cut-off.

**Four leaves were completed, none of them through the review queue.** `BVA-I235`, `BVA-I236`, `BVA-I240` and `BVA-I241` all went **In progress → Done** directly, in two bulk actions seven seconds apart (15:43:43 and 15:43:50), along with their two parent Stories. This is the pattern the 12–31 August completions followed — owners' items closed outside the queue — and it means **the eight items in REVIEW/QA are still the only items this sprint has ever put through review, and none has come out.**

**Three leaves of new scope were added on day 9 of 20** (§1.6).

### 1.2 The static-day record, corrected and restated

Reconstructed to **calendar-day** boundaries — commits from `git log --all` across all five repositories with bot commits excluded, board transitions from the three activity sidecars:

| Date | Day | Commits | Board transitions |
|---|---|---:|---:|
| 8–9 Aug, 15–16 Aug, 22–23 Aug, 29–30 Aug, 5 Sep | Sat/Sun | 0 | 0 |
| **25 Aug** | **Tue** | **0** | **0** |
| ~~11 Sep~~ | ~~Fri~~ | 0 | **6** — see §0.1 |
| 12 Sep | Sat | **3** | 0 |
| 13 Sep | Sun | 0 | 0 |
| 14 Sep (to 14:03 UTC, **partial**) | Mon | **2** | 0 |

**One fully static working day on record: 25 August.** Note also that 12 September — a Saturday — carries three commits, so "weekend" is not a reliable predictor of zero on this project either.

### 1.3 The review queue is unchanged and is now the oldest it has been

| Item | Owner | Entered REVIEW/QA | Age |
|---|---|---|---:|
| `BVA-I246`–`BVA-I252` (7 items) | Ayomikun Araoye | 8 Sep 16:02–16:04 UTC | **5.9 d** |
| `BVA-I231` | Ayomikun Araoye | 10 Sep 10:25 UTC | **4.2 d** |

Nothing entered, nothing left, nothing was sent back — for the sixth consecutive edition. The seven notification items, all describing code merged in July and August, have now been queued **5.9 days**, which is longer than any of them took to build.

Eight days remain in the sprint. The project's only precedent for emptying this column is the 47-second sweep of 3 September that marked 46 queued items Done without a line of code changing — and §1.1 shows a second precedent forming beside it: closing items without using the queue at all.

**`FCM_SERVICE_ACCOUNT` is still blank in `beevia-api/.env.example`** (line 79) and still optional in `common/env.ts`, re-verified at `origin/main`. Accepting `BVA-I246` without checking the deployed value still accepts a `StubPushAdapter`.

### 1.4 Translation — the client engine exists, and it bypasses the server

This is the substantive technical news of the window, and it changes the shape of the question rather than closing it.

**Client.** `origin/BVA-I242` gained `b91d765` *"app localization"* today at 11:51 UTC. It adds, in `lib/core/language/`:

| File | What it is |
|---|---|
| `on_device_translation_service.dart` | Translation via `google_mlkit_translation` — **on-device**, with model download and a four-language switch (en, zh, es, fr) |
| `app_language.dart`, `language_provider.dart`, `language_settings_service.dart` | The preference layer |
| `l10n.yaml` + ARB resources, `ic_uk/ic_france/ic_spain/ic_china.svg` | Static interface copy, bundled — deliberately *not* passed through ML Kit |

`api_url.dart` gains exactly one translation constant: `languagePreferencesUrl = "/translate/preferences"`. **A grep of the branch for any other `/translate` API call returns nothing.**

**What that means for the server.** The six merged `/translate/preferences*` operations have a real consumer, and that is a genuine gain. But `POST /translate` — still bound unconditionally to `StubTranslateAdapter` at `translate.module.ts:23`, re-verified today — **appears to have no intended consumer at all**, because the client does the translating itself. The report has asked for four editions whether the server-side translate surface is being retired; the code now suggests the answer is yes, by default rather than by decision. Leaving a stub endpoint live in a shipped API is a worse outcome than either retiring it or implementing it.

**The board half is still ahead of the code half.** `BVA-I229` *Translation Engine Integration* — the item this engine *is* — is **still To do on day 12 of 20**, while `BVA-I236` *Build & Wire* and `BVA-I241` *Build the Toggle* are marked **Done**. None of it is on `main`.

### 1.5 `origin/BVA-I242` is `origin/BVA-I192` plus one commit

Worth stating plainly, because it looks like a new workstream and is not:

- `origin/BVA-I192` is unchanged at `295a7bd` (7 Sep), 14 commits ahead of `main`.
- `origin/BVA-I242` is `295a7bd` + `b91d765`, **15 commits ahead of `main`**, spanning **6 August → 14 September**.

So this is the same long-lived branch under a new name. It carries the wallet flow, p2p transfers, external transfers, transaction history, notifications and now localization — **39 days of mobile work, unmerged**, and by the rubric's rules (§ Appendix) worth zero. It also adds `/cards`, `/wallets/banks`, `/wallets/withdraw` and `/topups/initialize` to `api_url.dart`, none of which `main` references.

### 1.6 New scope arrived on day 9 — and it answers Module 4

Four items were created on 11 Sep at 14:20–14:23 UTC, under a new parent Story:

| Item | Type | Owner | Status | What |
|---|---|---|---|---|
| `BVA-I253` | Story | Philip, David, Ayomikun | To do | **Trust & Safety** |
| `BVA-I254` | Task | David Samuel | To do | Report sheet + message-count selector (1–20, default 5) + **decrypt-and-package logic** + confirmation state |
| `BVA-I255` | Task | Ayomikun Araoye | To do | Report submission endpoint, server-side count cap, storage, **Warn/Dismiss endpoints**, wire Suspend to the existing status-action endpoint |
| `BVA-I256` | Task | Philip Chidera | To do | Mobile sheet design update |

**This is the answer to two risks that have been open for six editions**, and it is a good one:

- **Risk #16** — *"Module 4 shipped as a queue with no way to work it off"*. `BVA-I255` is exactly the missing half: Warn, Dismiss, and Suspend wired to the existing endpoint.
- **Risk #17** — *"the product decision behind Module 4 is recorded nowhere but a controller docstring"*. It is now recorded on the board, and the decision is explicit: **the reporting user's own device decrypts and packages a user-chosen number of recent messages as evidence, with consent copy, and the reported party is not notified.** That is a coherent answer to the E2EE-versus-moderation problem in `admin-api-rfc.md` §5.1 — it keeps the server unable to read content and makes the reporter the disclosing party.

Both risks are **downgraded rather than retired**: nothing is built, all three items are To do, and they landed on **day 9 of a 20-day sprint whose existing scope is already behind**. Adding three leaves to a sprint that has completed four is a scheduling decision worth making deliberately rather than by default.

### 1.7 Still no estimates — ninth consecutive edition

**0 of 29 on 0901, 0 of 12 on 0901-admin, 0 of 64 on 08-01.** No tags. Velocity, burn-down and any normalisation of one person's load against another's remain underivable — and the sprint just grew by three items, which is precisely the event that estimation exists to price.

---

## 2. What shipped this cycle

Six commits on any ref across the five repositories; **four merged to `origin/main`**.

| Repo | Commit | When (UTC) | Author | What |
|---|---|---|---|---|
| `beevia-admin` | `f12135b` | 14 Sep 11:36 | Promise Udo | **Reports module implementation** — `mock-data.ts` (462 lines) and `csv.ts` deleted; `api.ts` +420 lines against the real endpoints; `presentation.ts`, `report-catalogue.ts`, `report-table`, `report-totals`, `report-status-badge`, `use-report-download` added, with tests |
| `beevia-api` | `8a0166c` | 12 Sep 20:09 | Phoenixdadhev | `ci:` org supply-chain guard |
| `beevia-admin-api` | `0219e60` | 12 Sep 20:09 | Phoenixdadhev | same |
| `beevia-db-schema` | `e3c48f0` | 12 Sep 20:09 | Phoenixdadhev | same |
| `beevia-api` | `a61b0a2` | 14 Sep 13:49 | Phoenixdadhev | *branch only* — `origin/fix/refresh-rejection-diagnostics`, "say why a token rotation was refused" |
| `beevia-mobile` | `b91d765` | 14 Sep 11:51 | Davidtariq96 | *branch only* — `origin/BVA-I242`, "app localization" (§1.4) |

**No commit added, removed or changed a route.** The audit against `origin/main` reports zero drift on both services (§4).

| Repo | `origin/main` tip | Dated (UTC) | Age at cut-off |
|---|---|---|---:|
| `beevia-admin` | `f12135b` | 14 Sep 11:36 | **0.1 d** |
| `beevia-api` | `8a0166c` | 12 Sep 20:09 | 1.7 d |
| `beevia-admin-api` | `0219e60` | 12 Sep 20:09 | 1.7 d |
| `beevia-db-schema` | `e3c48f0` | 12 Sep 20:09 | 1.7 d |
| `beevia-mobile` | `0ad0083` | 27 Aug 04:09 | **18.4 d** |

### 2.1 The supply-chain guard is the first incident control this report can actually verify

`.github/workflows/supply-chain-guard.yml` calls the shared reusable workflow in `Drumbell-Technologies/.github` **on push, on pull request, and daily at 06:19 UTC**. Critical and high findings fail the build; medium findings report without failing. The commit message states the repositories already scan clean and names the advisory findings it expects (unpinned actions, missing pnpm `minimumReleaseAge`).

This matters because risks #13–#15 have been open for editions with the standing caveat *"not verifiable from this workspace"*. A daily scheduled scan is verifiable from the workspace, and it closes the specific hole the September incident exposed: **a payload committed to a quiet repository now surfaces within a day rather than at the next pull request.**

**It covers three of five repositories.** `beevia-admin` and `beevia-mobile` have no such workflow — and `beevia-mobile` is the repository that has gone 18 days without a commit to `main`, which is exactly the "quiet repository" case the guard was written for. That gap is new risk #13a.

Still invisible from here: the workstation, credential rotation, and branch protection.

### 2.2 Repository integrity

Not re-swept by blob hash this cycle. Four refs moved since the 10 September sweep, so the previous editions' inference-from-immutability no longer fully holds; however, all four new `origin/main` commits were inspected by diff (three are a 22-line CI workflow; one is the Reports module) and none touches `eslint.config.mjs` or any build-time hook. A full hash sweep is warranted at the next edition that has budget for it, and is listed as a recommendation rather than claimed as done.

---

## 3. Where the sprint actually stands, at day 12 of 20

| Workstream | Board | Code |
|---|---|---|
| Notifications (7 items) | All in REVIEW/QA, **5.9 d** | **Merged in July/August.** Nothing this sprint |
| Translation — language preference (2 items) | 1 in REVIEW/QA 4.2 d, 1 In progress | **Merged 10 Sep**, matches the items |
| Translation — backend string bundles (1 item) | In progress, 4.2 d | No code yet |
| Translation — mobile engine + UI (7 items) | **2 Done**, 3 To do, 2 In progress | **On a branch, unmerged.** `main` untouched 18.4 days |
| Trust & Safety (3 items, **new**) | All To do | None |

**Eight days remain.** Of 20 leaves: 4 Done, 8 parked in a review queue nobody has emptied, 3 In progress, 5 To do. The backend half is merged or one item from it. The client half has real code for the first time this sprint — and it is on a branch that has not merged in 39 days, which is the difference between the board's "2 Done" and `origin/main`'s "nothing since 26 August".

The arithmetic of the sprint has not improved. It has changed shape: the question was *"has the mobile work started?"* and the answer is now yes. The new question is *"will it land?"*, and it has eight days to be answered.

---

## 4. Spec updates made this cycle

**None, and none were warranted.** No merged commit added, removed or altered a route. The deterministic audit run against a read-only `origin/main` shadow reports:

```
beevia-api         code=137  spec=137  proposed= 38  [OK]
beevia-admin-api   code= 47  spec= 47  proposed= 19  [OK]
```

**Drift: zero, both services, both directions.** All four files parse. No `x-beevia-*` markers, no broken `$ref`s, no orphaned components, no duplicate `operationId`s, no cross-file schema divergence outside the two whitelisted cases.

Per the audit skill's instruction for a clean run — *"say so and stop; do not rewrite documents that are already correct"* — `openapi.yaml`, `openapi.proposed.yaml`, `openapi.admin.yaml`, `openapi.admin.proposed.yaml`, `api-rfc.md`, `admin-api-rfc.md` and `suggestions.md` are unmodified today.

**The working-tree audit still reports 19 phantom drift lines** — 6 on `beevia-api`, 13 on `beevia-admin-api` — because three repositories are `diverged` and their working trees are 4 September code. **Sixth consecutive edition flagging it**, so that nobody "fixes" the spec by deleting nineteen operations that exist.

One item to note for the next spec cycle: `BVA-I255` (§1.6) will add a report-submission endpoint plus Warn and Dismiss endpoints to `beevia-admin-api`. When it is built, it moves the corresponding proposed operations rather than adding new ones — check `openapi.admin.proposed.yaml` before writing anything new.

### 4.1 The access-control gap is four days old and still open

Re-verified at `origin/main`: `GET /admin/reports/{id}` and `GET /admin/reports/{id}/download` are gated by `@RequirePermission('reports','view')` and `('reports','export')` and nothing else. `ReportsService` resolves the requesting admin's `viewableModules` at generation time (`reports.service.ts:133`) and passes them into the run; **that scoping is never re-applied at read.** A narrower admin can still open and download a report generated under a wider role.

**It got more expensive today.** Yesterday's argument for fixing it cheaply was that nothing consumed the module. As of `f12135b`, the client does: `api.ts` now polls `GET /admin/reports/{id}` and fetches `GET /admin/reports/{id}/download` through the authenticated client, and lists the team-wide run history that names each requester. The fix is the same two changes — persist `viewableModules` on the row, re-filter on read — but it is no longer free of consumer impact.

---

## 5. Admin dashboard board — `0901-admin`

**Sprint `0901-admin`, 3 Sep → 22 Sep, day 12.** 12 items — **8 leaves, 4 parent Stories**. **Zero transitions in the window**; the export is byte-identical to 11 September's apart from the timestamp.

| Status | Leaves | 11 Sep | Δ |
|---|---:|---:|---:|
| To do | 2 | 2 | 0 |
| In progress | 0 | 0 | 0 |
| Done | 6 | 6 | 0 |

| Owner | Leaves | To do | Done |
|---|---:|---:|---:|
| Promise Udo | 4 | 1 | **3** |
| Ayomikun Araoye | 3 | 1 | 2 |
| Unassigned | 1 | 0 | **1** |

The last transition remains `BVA-I13`/`BVA-I14`/`BVA-I15` → Done at 10 Sep 10:24 UTC, **4.2 days ago**. The board's whole history is still 21 transitions on two days.

### 5.1 The "Done with no code" finding is retired for Reports

This has been open for three editions. It is now closed by evidence:

| Item | Owner | Done? | Code at `origin/main` |
|---|---|---|---|
| `BVA-I5` | Ayomikun | ✅ | Merged — `434d5e6` |
| `BVA-I11` | Ayomikun | ✅ | Merged |
| `BVA-I14` | *Unassigned* | ✅ | Merged — `da01324` |
| `BVA-I6` *Report Picker, Parameter Form & History UI* | Promise | ✅ | **Merged today** — `report-type-gallery.tsx`, `parameter-form.tsx`, `recent-reports.tsx` |
| `BVA-I12` *Report Content Display* | Promise | ✅ | **Merged today** — `report-preview.tsx`, `report-table.tsx`, `report-totals.tsx`, `presentation.ts` |
| `BVA-I15` *Report Content Display* | Promise | ✅ | **Merged today** — same |

`src/features/reports/mock-data.ts` and `mock-data.test.ts` are **deleted**; `api.ts` now calls `GET /admin/reports/types`, `POST /admin/reports`, `GET /admin/reports`, `GET /admin/reports/{id}` (with a poll-until-ready `refetchInterval`) and `GET /admin/reports/{id}/download`. Tests accompany the new components.

**Across the client's ten feature modules, 9 are on the live API and 1 is mock** (`pending-transfers`) — up from 8 of 10. The five Reports endpoints that shipped on 9–10 September now have a consumer, four days later.

**What is *not* closed:** `BVA-I9` *Report Content Display* (Promise) and `BVA-I8` *Report Data Query* (Ayomikun) are still To do, and the board still records zero transitions by Promise on his own items — every one of the 21 was made by someone else. The "have Promise move his own items" recommendation stands; the "Done means nothing" concern does not, for Reports.

### 5.2 Never summed with the main board

12 items here and 29 on sprint 0901 are different projects and different backlogs; one person appears on both. A combined figure would be meaningless. The export stays in `sprint-board-exports/admin/` because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and would otherwise diff two unrelated boards.

---

## 6. Team performance — detail

All figures come from the activity sidecars and git, never from `Last Modified`. Commit counts are trailing-7-day, merged to the default branch except where stated, summing each person's git identities and excluding bots. Transition extraction matches `Updated the status`, `Item Completed` and `Item Reopened`. Method unchanged.

**Ayomikun Araoye — backend + admin API.** **23 commits** in the trailing 7 days (`beevia-admin-api` 14, `beevia-api` 5, `beevia-db-schema` 4, summing `Ayomikun Araoye`, `Phoenixdadhev` and `phoenixdahdev`). The rise from 20 is **exactly the three supply-chain-guard commits of 12 September** — verified by recomputing both windows, which return 23 identically, so nothing aged out and nothing else was added. **8 submissions** in the trailing 7 days (7 notification reconciliation items on 8 Sep, 1 delivery item on 10 Sep) — flat for the fourth consecutive edition, and all eight of those items are the ones still sitting in review. Median cycle 3.0 d over 12 passes. One open WIP, `BVA-I245`, 4.2 days, now 1.4× his median. He opened `origin/fix/refresh-rejection-diagnostics` today; it is unmerged and outside the sprint.

**David Samuel — mobile.** **Zero submissions for the eleventh consecutive day** — last was `BVA-I182` on 3 September, 11.2 days ago. Median cycle 2.6 d over 14 passes. **Zero commits to `main`; one commit to `origin/BVA-I242`** today, his first anywhere in 7 days, and substantively the most significant code in this window (§1.4). He holds two 0901 leaves In progress: `BVA-I233` at **9.9 days against a 2.6-day median — 3.8×**, the most overdue WIP on any board, and `BVA-I243` at 6.1 days (2.3×). Two further leaves, `BVA-I236` and `BVA-I241`, were marked Done on his behalf on 11 September; the code for them reached a branch on 14 September and `main` not at all.

The question this report has asked for four editions — *what is happening with the mobile client* — now has a partial answer: **work is happening, on a branch, and it is not landing.** That is a different problem from the one suspected, and a more tractable one.

**Philip Chidera — design.** No submissions; last was 28 August, **17.1 days ago**. Median cycle 0.9 d over 7 passes. **Zero open WIP** — both his items closed on Friday. He performed all six of Friday's completions in two bulk actions seven seconds apart, four of them on items he does not own.

**This is a process observation, not a personal one, and the sidecar makes that clear:** Philip has moved the client-side rows throughout the sprint, not only at completion — `BVA-I236` and `BVA-I241` were moved To do → In progress by him on 4 and 8 September as well. One person is maintaining the board state for two people's work. That is a reasonable division of labour if it is deliberate; it is a measurement problem regardless, because it means **board status on the client side reflects one person's view of progress rather than the owner's**, and §1.4 shows the two diverging by three days and one merge.

**Promise Udo — admin dashboard.** **5 commits** in the trailing window, including today's Reports module (§5.1). He made no board transitions, again — all 21 on that board were made by someone else. His three Done items now have code; his fourth, `BVA-I9`, is To do.

### 6.1 Weekly submission trend

Genuine submissions into REVIEW/QA by leaf items, counting **each pass**, across the main board and 0901:

| ISO week | Passes | Distinct items |
|---|---:|---:|
| W33 (11–17 Aug) | 1 | 1 |
| W34 (17–23 Aug) | 17 | 17 |
| W35 (24–30 Aug) | 31 | 19 |
| W36 (31 Aug – 6 Sep) | 3 | 3 |
| W37 (7–13 Sep) | **8** | 8 |
| W38 (14–20 Sep, day 1) | **0** | 0 |

W37 closed at eight, of which **one was delivery** and seven were the notification reconciliation. Note that Friday's four completions do **not** appear here: they never entered REVIEW/QA (§1.1).

### 6.2 Cycle times

| Person | n | Median |
|---|---:|---:|
| Philip Chidera | 7 | **0.9 d** |
| David Samuel | 14 | **2.6 d** |
| Ayomikun Araoye | 12 | **3.0 d** |

Unchanged — no item completed a REVIEW/QA pass in the window, so no sample grew. Friday's four completions bypassed the queue and therefore contribute no cycle-time sample at all, which is worth noticing: **the more the team closes items outside the queue, the less this metric can see.**

### 6.3 Completion, by route

| When | Completions | From | Character |
|---|---:|---|---|
| 12–31 Aug, over 6 days | 20 (12 leaves) | **Never REVIEW/QA** | Owners closing their own items |
| **3 Sep, one 47-second action** | **46** (30 leaves) | **REVIEW/QA, all 46** | Sprint close |
| **11 Sep, two actions 7 s apart** | **6** (4 leaves) | **In progress, all 6** | Bulk close, bypassing the queue |
| On `0901-admin` | 9 (6 leaves) | In progress / To do | By one person, on 2 days |

The main board still records **176** `Updated the status`, **66** `Item Completed` and **2** `Item Reopened` — 244 transitions, unchanged, as sprint 08-01 is closed. Sprint 0901 now records **39** transitions in total.

### 6.4 What these figures do not measure

- **They cannot see a branch**, and this window is the clearest demonstration yet: David's single most substantial contribution to the sprint is invisible to every board metric in this report.
- **They cannot tell delivery from reconciliation.** Seven of W37's eight submissions describe code merged in July and August.
- **They say nothing about whether a completion was reviewed.** Of 72 completions this project has recorded, 26 bypassed the queue entirely and 46 came out of it in 47 seconds.
- **Cycle time is blind to items closed outside the queue** (§6.2), and that route is growing.
- **Board status on the client side is transcribed by one person for two people's work** (§6), so it records his reading of progress rather than each owner's.
- **They count merge commits.** Ayomikun's trailing figure includes merges.
- **They do not measure whether "Done" means merged.** Two 0901 leaves are Done for branch-only code.
- **No estimation points exist on any item, on any of the three boards** — 0/64, 0/29, 0/12.
- **Cycle time rewards small items; commit counts reward small commits.** Neither measures difficulty or quality.
- **Correctness and testing are out of scope for scoring**, per the owner's 2026-08-07 instruction — though it is worth recording that `f12135b` arrived with tests.

---

## 7. Risks

Ordered by what would cost most to leave alone. Two were downgraded and one retired this cycle; one is new.

1. **`origin/BVA-I242` carries 39 days and 15 commits of mobile work that has never merged** (§1.5), including the translation engine `BVA-I229` depends on and the code behind two items already marked Done. Eight days remain in the sprint. **Promoted to first** — every mobile gain in this report is contingent on this branch landing.
2. **Eight items sit in REVIEW/QA at 5.9 days and the project's only precedents for emptying that column are a 47-second bulk close and closing items without using it.** Sprint 0901 ends 22 September.
3. **Seven of those eight describe code merged in July and August** (§1.3), so accepting them would record a sprint's delivery that no sprint-0901 commit supports.
4. **Board Done and merged code have diverged on the client side** — `BVA-I236` and `BVA-I241` were Done three days before their code reached a branch, and it is still not on `main` (§1.4). This is distinct from #1, and worth separating from it: risk #1 is that the work may not land, whereas this one says the board would read the same either way.
5. **A generated report can be read by an admin whose role could not have generated it** (§4.1). Four days old, and **now consumed by a live client**, so no longer free to fix.
6. **Three new leaves of scope arrived on day 9 of 20** (§1.6) in a sprint that has completed four. The scope itself is well specified and closes two open risks; what deserves a decision is whether it belongs in this sprint or the next one.
7. **`beevia-mobile` `main` is 18.4 days stale** and is one of two repositories with no supply-chain guard.
8. **`POST /translate` has no consumer and never will**, on current evidence (§1.4) — the client translates on-device. A live stub endpoint in a shipped API.
9. **Translation shipped without its opt-in flag.** PRD §8.1 requires opt-in; the stored preference is a language only. The client now reads that surface, so the contract-change window is closing.
10. **Accepting `BVA-I246` may accept a stub.** `FCM_SERVICE_ACCOUNT` optional and blank in `.env.example` (line 79, re-verified).
11. **`GET /translate/languages` still does not constrain its `to` field.**
12. **Report CSVs are stored in Postgres with no retention policy** — up to 50,000 rows per run, forever. Now reachable from a live UI.
13. **The infected workstation's status is unknown**, and credential rotation and branch protection remain unverifiable from here.
    - **13a (new). The supply-chain guard covers 3 of 5 repositories.** `beevia-admin` and `beevia-mobile` have none — and `beevia-mobile` is the quiet repository the daily scan was written to protect (§2.1).
14. **Repository integrity was not hash-swept this cycle** and four refs moved since the last sweep (§2.2). Diff-inspected, not hash-verified.
15. **Three repositories remain unsynced locally**, so the working-tree audit reads 4 September code and reports 19 phantom drift lines. Sixth edition.
16. ~~**Module 4 shipped as a queue with no way to work it off**~~ — **downgraded.** `BVA-I255` specifies Warn, Dismiss and Suspend (§1.6). Not built; To do on day 12.
17. ~~**The product decision behind Module 4 is recorded nowhere**~~ — **retired.** `BVA-I253` records it explicitly: client-side decrypt-and-package with user-chosen message count and consent copy (§1.6).
18. **The per-user reconciliation check will report false discrepancies for every user the moment the treasury pool is enabled** — `ANCHOR_POOL_ACCOUNT_ID` still optional in `common/env.ts` and unset (`payout.service.ts:185`).
19. **Reconciliation is unbounded and silently capped** at 500 payouts / 1000 ledger rows — and the Reports module demonstrates the correct pattern in the same service.
20. **`treasury.solvent` is on the live landing screen and reads `false` for "unknown".**
21. **The money-oversight surface still has no second reviewer** — PRs #1–#10 self-merged.
22. **The Anchor webhook backfill is still unscoped** — 67 days of dropped events, unmeasured.
23. **The daily export still targets a closed sprint, and the cut-off is still 14:00 UTC** — seventh and sixth editions. §0.1 is the first time this pair produced a wrong published headline rather than a caveat.
24. **No estimation points on any of three boards** — ninth edition asking, and the sprint just grew.
25. **The same silent-200 is still live on `POST /kyc/profile`** — tenth consecutive edition.
26. **A hard-coded account number still reaches a money screen on `main`** — tenth consecutive edition. Unchanged by definition: `main` has not moved.
27. **The admin client's `wallet` module ignores the wallets endpoint built for it** — fourth edition. `api.ts:132` still carries the comment deriving balance from the most recent row's `balance_after`.
28. **This service now has three pagination conventions across seven endpoints.**

---

## 8. Previous recommendations — where they stand

| Recommendation from 11 Sep | Status on 14 Sep |
|---|---|
| Ask David what is happening — third time | ⚠️ **Partially answered by evidence, not by the room.** He is working, on a branch, and not merging (§1.4, §1.5). The conversation is still needed, but the question has changed |
| Confirm whether Friday was a day off | ✅ **Answered by the data — it was not.** Six transitions and four items created, after the cut-off (§0.1) |
| Scope the eight items in REVIEW/QA before 22 September | ❌ **Not done.** Unmoved, now 5.9 d and 4.2 d |
| Fix the report read-scoping (§4.1) | ❌ **Not done**, and now more expensive — the module has a live consumer |
| Add the `enabled` flag to the translation preference | ❌ **Not done**, and the window is closing — the client now reads that surface |
| Agree what Done means on the admin board | ⚠️ **Answered in practice for Reports** by shipping the code (§5.1); unanswered as a rule, and the same question has now appeared on the main board (§1.4) |
| Have Promise move his own board items | ❌ **Not done.** Zero transitions by him on that board, still |
| Wire the admin client to the five endpoints waiting for it | ✅ **DONE** — `f12135b`, all five, with tests (§5.1) |
| Write down that Option A is the answer to Module 4 | ✅ **DONE, better than asked.** `BVA-I253`/`BVA-I255` record the decision and specify the missing endpoints (§1.6) |
| Adopt the Reports truncation pattern in reconciliation | ❌ **Not done** |
| Add the route-collision check to CI, on push | ❌ **Not done** — though a supply-chain guard did land on push in three repos (§2.1), so the CI path is now proven |
| Move the daily export to sprint 0901 and the cut-off to ~20:00 UTC | ❌ **Not done** — and §0.1 is the cost |
| Put estimation points on all three boards | ❌ **Not done.** 0/29, 0/12 |
| Apply the BVN-ordering guard to `POST /kyc/profile` | ❌ **Not done.** Re-checked at `origin/main` |

**Three of fourteen actioned, plus one answered by data — after four consecutive editions of zero or one.** The pattern is worth naming, because it inverts the previous edition's conclusion. It observed that *"things that are code get done; things that are decisions do not."* This cycle, the two items cleared outright were **one code task and one decision** — and the decision (Module 4) was recorded more completely than the recommendation asked for. What remains unactioned is now dominated by **small edits nobody owns**: the `enabled` flag, the BVN guard, the truncation pattern, the export cut-off. These are hours of work, not days, and they have survived thirteen editions.

---

## 9. What I would do this week

Reordered by remaining time. Eight days left in sprint 0901.

1. **Merge `BVA-I242`, or say why it cannot merge.** Thirty-nine days, fifteen commits, the wallet flow, external transfers, transaction history and now the translation engine — all of it invisible to the board, the MVP estimate and every other developer. It is the single highest-value action available this week, and it gets harder every day the branch ages. If it is too large to merge safely, the answer is to split it, not to keep adding to it.
2. **Scope the eight items in REVIEW/QA before 22 September, not on it.** Seven describe July code and are now 5.9 days queued. If accepting them as-is is fine, say so on the board now; if not, name a reviewer. Friday's bulk close shows the alternative outcome forming.
3. **Decide whether Done requires merged.** Two items are Done for branch-only code and one board has just proved the opposite standard by shipping. One sentence agreed at standup fixes both boards, and without it the burn-down cannot be read.
4. **Fix the report read-scoping** (§4.1). Persist the generating admin's `viewableModules` on the row and re-filter on read. It was free last week; it now has a live consumer.
5. **Add the `enabled` flag to the translation preference.** PRD §8.1 asks for opt-in; the shipped surface stores a language only — and as of today a client reads it. One column and one field on two responses, while the client is still on a branch and the contract can still change cheaply.
6. **Settle what happens to `POST /translate`.** The client translates on-device (§1.4). Either retire the endpoint or implement it, but do not ship an API with a stub that returns its input unchanged and no consumer.
7. **Add the supply-chain guard to `beevia-admin` and `beevia-mobile`** (§2.1, risk #13a). The workflow file is 22 lines and already written; `beevia-mobile` is precisely the quiet repository the daily schedule exists for.
8. **Move the cut-off to ~20:00 UTC and the daily export to sprint 0901.** Sixth and seventh editions. This one is no longer a preference — §0.1 documents the wrong headline it caused, and the fix is a scheduler change.
9. **Price the Trust & Safety scope, or defer it.** Three leaves arrived on day 9 of a 20-day sprint that has completed four. The work is right and the decision behind it is good; the timing deserves a deliberate call rather than an implicit one.
10. **Have Promise move his own board items.** Fourth edition. He has now shipped the code for three of them and still has not touched the board.
11. **Adopt the Reports module's truncation pattern in reconciliation** (risk #19). Ten-line change; converts silently-wrong output into visibly-partial output.
12. **Add the route-collision check to CI, on push.** The supply-chain guard proves the pattern works in these repos; the audit already extracts routes and parses all four specs.
13. **Put estimation points on all three boards, or state that this project does not estimate.** Ninth edition — and the sprint grew by three items this week, which is the exact event estimation is for.
14. **Apply the BVN-ordering guard to `POST /kyc/profile`.** Tenth edition; five lines, already written.

---

## Appendix — method and readiness rubric

**Pipeline.** `beevia-refresh`: main board export (64 items, sprint 08-01, cut-off 14:03 UTC) → admin board export with `--sprint 0901-admin` (12 items) → fast-forward sync (**1 repo synced — `beevia-admin`, +3 commits; 1 already current; 3 refused as `diverged`**) → deterministic audit against the working tree → **a second audit run against a read-only `origin/main` shadow workspace** built with `git archive` into `/tmp` → `git log --all` sweep of every ref in all five repositories across the window → read-only scratch export of sprint 0901 (29 items) → re-verification at `origin/main` of every code fact this edition carries forward → this report. **No spec, RFC or suggestions file was modified, because the audit was clean** (§4).

**Nothing was executed from any sub-repo.** No `npm`, `node`, `eslint` or build step ran. The unsynced repositories were read with `git log`, `git archive` and `git show` into `/tmp`, outside the workspace. No repository was reset, rebased, reverted or cleaned, no file in any sub-repo was edited, and the sync step's `--ff-only` limit was not overridden. Nothing was committed, pushed or deployed.

**Degraded inputs.**

- **Three repositories could not be synced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` remain `diverged` because `origin/main` was rewritten during the 8 September remediation; `sync_repos.py` is `--ff-only` and correctly refuses. Their working trees are 4 September code, the sole cause of the working-tree audit's **19** phantom drift lines. Resolving it needs `git reset --hard origin/main` or equivalent, which is outside this pipeline's sanctioned exception and is a decision for whoever owns those clones. **Capture the local tips first** (`d9af17b`, `43abc3a`, `5b0592a`) — they are the only offline copy of the pre-incident history. Every code claim in this report was made against `origin/main`.
- **The `Epic` column is blank** on both in-repo boards — the OAuth refresh token lacks `ZohoSprints.epic.READ`. A known scope gap, not "no epic assigned"; the audit trail shows epics *are* set.
- **`Comments` bodies are unavailable** from the API.
- **`ZOHO_SPRINT_FILTER` is stale** — still `08-01`, so the in-repo main export covers a sprint that closed on 28 August and reads 41 leaves all `Done`. Sprint 0901 is exported to `/tmp/beevia-scratch/` for the eighth consecutive edition, because `beevia-audit` globs `sprint-board-exports/*.csv` non-recursively and diffs the two newest as snapshots of one board. **The deterministic audit's board section therefore describes the closed sprint**, and every 0901 figure in this report comes from the scratch export.
- **The window ends at 14:03 UTC**, so Monday afternoon UTC is unobserved. §0.1 is what that costs when it is not respected.
- **Repository integrity was not hash-swept.** Four refs moved since the 10 September sweep; the four new `origin/main` commits were diff-inspected and touch no build-time configuration, but this is weaker evidence than a hash check (§2.2).
- **Branch protection, credential rotation and workstation remediation are unverifiable** from this workspace. The supply-chain guard (§2.1) is the first control in this family that *is* verifiable, and it covers three of five repositories.
- **No estimation points on any item, on any of three boards**, so velocity is not derivable and no per-person figure is normalised for size.
- **The activity sidecars carry audit trails only for items currently on the three boards**, so a transition on an item since removed would not appear.

**Window.** 11 Sep 14:01 UTC → 14 Sep 14:03 UTC — **3.0 days, containing a weekend**, which is why the per-window counts are not comparable to a normal edition's 24 hours. All `actiontime` values and board times are UTC; the local export host runs UTC−6, so the 08:03 local run is a 14:03 UTC cut-off. Calendar-day figures in §1.2 are measured to midnight UTC and marked partial where the day is incomplete.

**Sources.** Boards: `beevia-sprint-board-2026-09-14.csv` (64 rows, 41 leaves, sprint 08-01) + activity sidecar; `admin/beevia-admin-sprint-board-2026-09-14.csv` (12 rows, 8 leaves, sprint 0901-admin) + activity sidecar; scratch export of `0901` (29 rows, 20 leaves) + activity sidecar. Code: all five repositories at `origin/main`; `beevia-admin` and `beevia-mobile` in the working tree, the other three extracted to a `/tmp` shadow. Specs: `openapi.yaml` (**137**), `openapi.proposed.yaml` (**38**), `openapi.admin.yaml` (**47**), `openapi.admin.proposed.yaml` (**19**) — all validated, no markers, no broken refs, no orphaned components, zero drift against `origin/main`.

**A note on who appears here.** Only people whose work is tracked have rows. Board actions performed by non-contributors are reported without attribution, per the standing instruction — this applies to the four items created on 11 September (§1.6), whose creation is reported without naming the actor.

<a id="mvp-method"></a>

### MVP readiness — ≈58% (estimate; 58.10, up from 57.92)

**Target 2026-09-01 (provisional) · the target date passed thirteen days ago.** On merged build evidence the product is roughly 58% of the way to the PRD's MVP. Three capabilities carrying 22 weighted points remain entirely unstarted.

**One score moved: Admin oversight, 0.87 → 0.90**, on the merged Reports client (§5.1). **Message translation did not move**, and that is the rubric working exactly as designed rather than an oversight — the on-device engine in §1.4 is real, substantial, and **on an unmerged branch**, which the rules score at zero. If `BVA-I242` merges, capability #3 moves materially in a single step.

| # | Capability | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.9 | Unchanged. Conversation/message/key/attachment paths live; client crypto, socket and attachment layers present. No merged commit touched `src/messaging/` |
| 2 | Voice & video calling | 8 | 0.8 | Unchanged. 4 call endpoints live; `audio_call_screen` / `video_call_screen` present at `origin/main`; incoming-call push wired — transport still falls back to a stub without `FCM_SERVICE_ACCOUNT` |
| 3 | Message translation | 7 | **0.30** | **Unchanged, and deliberately so.** Seven `/translate` operations implemented, one proposed. `translate.module.ts:23` still binds `TRANSLATE_PORT` unconditionally to `StubTranslateAdapter`; no opt-in flag. `beevia-mobile` `main` still returns **zero** `/translate` hits. The on-device ML Kit engine and the `/translate/preferences` call exist only on `origin/BVA-I242`, unmerged (§1.4) |
| 4 | Local KYC tier (BVN) | 8 | 0.9 | Unchanged. Ceiling unchanged: silent-200 on `/kyc/profile`, failed provisioning surfaces nowhere |
| 5 | International KYC tier | 6 | 0.0 | proposed only — 3 operations, none implemented |
| 6 | Multi-currency wallets | 12 | 0.70 | Unchanged. Pooled treasury merged but **disabled** (`ANCHOR_POOL_ACCOUNT_ID` optional in `common/env.ts` and unset, `payout.service.ts:185`), so not scored. Server NGN-only; `PaymentService.activeNgn()` re-verified at three call sites |
| 7 | Send / request / receive | 12 | 0.80 | Unchanged. Ceiling: request/receive still have no merged client flow; the wallet and transfer UI is on `BVA-I242` |
| 8 | Cross-currency FX | 12 | 0.0 | proposed only — 3 `/fx` operations, none implemented |
| 9 | Virtual cards | 10 | 0.55 | Unchanged. 13 `/cards` operations live server-side; `main` still has **zero** client `/cards` references — the branch adds `cardsUrl`, unmerged — and there is no issuer reveal flow |
| 10 | Consent management | 4 | 0.0 | No endpoint or record anywhere. `BVA-I253`'s consent copy is report-evidence consent, not the PRD's consent management, and is unbuilt |
| 11 | Admin oversight | 6 | **0.90** | **+0.03.** Admin API 47 operations; modules with something built 6 of 8; client **9 of 10** on the live API (was 8), `pending-transfers` the last mock. The five Reports endpoints now have a merged, tested consumer (§5.1). Ceiling held down by the open read-scoping gap in the same code (§4.1) and by Module 4's actions being specified but unbuilt |
| | **Weighted total** | **100** | | **58.10 → ≈58%** |

Weights frozen — no methodology change this edition. Scores measure **merged, reachable build evidence**: never board status, never items in review, never unmerged branches, never merged-but-disabled code, and never a design decision on its own.

**Three things that look like progress and are still worth zero by design:** the eight items in REVIEW/QA; the four leaves marked Done on 11 September, two of which have no merged code; and the **15 commits on `origin/BVA-I242`**, which are the most substantial client work of the sprint by any human measure and unmerged by this one. The gap between what this project has built and what this number credits is now almost entirely one branch wide.

### What this report cannot tell you

- **When, or whether, `BVA-I242` will merge.** It is the largest single uncertainty in the estimate and in the sprint.
- **Whether anything happened after 14:03 UTC today.** This is a limit of when the export runs rather than of what it captures, and §0.1 shows what that limit cost the last time it was ignored.
- **Whether the eight items in REVIEW/QA will be reviewed, swept, or bypassed.** There are now two precedents for not reviewing them.
- **Whether "Done" on the client side means the owner's judgement or the transcriber's** (§6).
- **Whether the Trust & Safety scope was priced before being added**, or added because it was ready.
- **Whether `FCM_SERVICE_ACCOUNT` is set in any deployed environment.** The fallback is silent by design.
- **Whether `POST /translate` is meant to survive.** The client's architecture implies not; nothing records a decision.
- **Whether the supply-chain guard has actually run, or passed.** The workflow is committed and scheduled; its run history is on GitHub, not in the clone.
- **Whether any of the 137 + 47 endpoints work.** Unit tests exist and no HTTP-level tests do; there is no second reviewer. Testing is out of scope for scoring per the owner's 2026-08-07 instruction.
- **Whether the infected workstation has been cleaned, or whether credentials were rotated.** Invisible from a git clone.
- **Whether branch protection is enabled.** The available GitHub token cannot see the org.
- **What the 67 days of dropped Anchor events cost.** Still unmeasured.
- **Velocity for any of the three sprints** — 0 of 64, 0 of 29 and 0 of 12 items estimated.
