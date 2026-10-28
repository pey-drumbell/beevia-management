# Beevia — Project Status

**As of 2026-10-28** · Sprint **1002** (21 Oct → 5 Nov, day 8 of 16): **63 items, 44 leaves: 15 To do · 14 In progress · 14 REVIEW/QA · 0 BLOCKED · 1 Done** · Sprint **0902** (30 Sep → 15 Oct): swept 21 Oct, static · Sprint **0901** (3 Sep → 22 Sep): closed 30 Sep, static · Sprint **0901-admin** (3 Sep → 22 Sep): closed, static · Sprint **08-01** (11 Aug → 28 Aug): closed 3 Sep
Sources: `sprint-board-exports/beevia-sprint-board-2026-10-28.csv` + `beevia-activity-2026-10-28.json` (64 items, sprint 08-01, frozen); `sprint-board-exports/admin/beevia-admin-sprint-board-2026-10-28.csv` + its activity sidecar (12 items, sprint 0901-admin); a read-only scratch export of sprint **1002 (63 items)** in `/tmp/beevia-scratch/1002/`, diffed against the 27 Oct file in the same folder; the 27 Oct scratch export of **0902** and the 19 Oct export of **0901** (both closed, not re-exported) for cycle times. All five repos were read at `origin/main`, plus every remote branch and `refs/pull/*`. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were read through a `git archive` shadow, because their working trees are still `diverged`.

Scope: five boards, kept separate and never summed. **Window: 27 Oct 15:55 UTC → 28 Oct 14:05 UTC, 0.9 days (Tue → Wed).**

---

## Quick overview

> **The Help & Support FAQ shipped on the server today, end to end: a schema, five app routes and eleven admin routes, merged between 12:13 and 13:19 UTC. None of it was in the spec, and it is now (146 consumer and 60 admin operations). It is not yet usable. The migration grants the new `help_center` permission to no admin role, so nobody can write a FAQ entry, and the mobile FAQ screens still run on placeholder data. The three mobile screens that the 27 Oct edition said had "no code on any branch" do have code. It was committed on David's machine six hours before that edition's cut-off and pushed today, on `BVA-I353`. Five of its six card and statement calls do not match the server: three routes the server does not have, two with the wrong authentication.** The board moved 4 more leaves to REVIEW/QA. The two backend ones followed their merge by 21 minutes, which is what the column is for. The two mobile ones are placeholder screens on an unmerged branch.

| Metric | 27 Oct | 28 Oct | Δ |
|---|---:|---:|---|
| Sprint 1002 items (leaves + parents) | 62 (43+19) | **63 (44+19)** | +`I392` *Activity Screen – Verification Checklist*, added by board administration at 15:57 UTC on 27 Oct, just after that edition's cut-off |
| Sprint 1002 leaves To do / In progress / REVIEW/QA / BLOCKED / Done | 19 / 13 / 10 / 0 / 1 | **15 / 14 / 14 / 0 / 1** | 4 FAQ leaves → REVIEW/QA; 4 dispute leaves → In progress; `I392` → In progress |
| Transitions into REVIEW/QA, last 7 days (leaves) | 10 | **14** | 6 by the leaf's owner (all Ayomikun), **8 moved by Ayomikun on David's and Philip's items**, 0 by board administration |
| Owners' last submission of their *own* leaf | 27 Oct 13:11 UTC (Ayomikun, `I358`) | **28 Oct 13:02 UTC** (Ayomikun, `I338`) | David's last own submission is still 14 Oct, **13.9 days** ago |
| Items accepted by a reviewer | 0 | **0** | nothing has left 1002's review column |
| 1002 REVIEW/QA leaves with matching **merged** code | 1 of 10 | **3 of 14** | +`I335`, `I338` (FAQ API, #86). Five mobile items now have **branch** code, none merged and none working against the real API (§2.1) |
| Routes in code but not in the spec (consumer / admin) | 2 / 0 → 0 | **5 / 11 → 0** | `/help/*` and `/admin/help/*` documented today (§3.4) |
| API surface (consumer / admin) | 141 / 49 | **146 / 60** | admin-api's first new routes since 17 Sep |
| Proposed operations (consumer / admin) | 38 / 18 | 38 / 18 | none shipped; the FAQ was never proposed |
| Backend repos that deploy or migrate production on push with no test gate | 3 of 3 | **3 of 3** | 6 merges today (2 per repo) and 2 schema releases (v0.0.43, v0.0.44) went out that way |
| `beevia-mobile` days since a commit on `main` | 5.3 | **6.2** | branch `BVA-I353` pushed today: 5 commits, 69 files, +8,341 |
| `beevia-api` / `beevia-admin-api` / `beevia-db-schema` days since a commit | 0.1 / 19.3 / 0.1 | **0.1 / 0.0 / 0.1** | |
| `beevia-admin` days since a commit | 35.0 | **35.9** | |
| Admin board: open sprint / days since any activity | none / 43.0 | **none / 44.0** | the FAQ CMS API shipped, but its dashboard Story (`I351`) is unassigned and its API task (`I352`) still says To do |
| Estimation points set (1002) | 0/62 | **0/63** | |
| MVP readiness (estimate) | ≈67% (67.32) | **≈67% (67.32)** | **0**: Help & Support has no rubric line, and the card screens are on an unmerged branch (appendix) |

**Correction to 27 Oct.** That edition said `I365` (statement screen), `I369` (manage card) and `I376` (delete card) had "no code on any `beevia-mobile` branch". It made "Where is the code?" the first standup question and cited the three as the clearest case of the review column filling "ahead of the code". The code existed. Commit `9838d8e` *card implementation* is authored 27 Oct **09:57 UTC**, six hours before that edition's 15:55 cut-off. It adds `account_statement_screen.dart`, `manage_card_screen.dart`, `card_details_screen.dart` and the card service calls. It reached `origin` only after the 27 Oct recheck (16:06 UTC). This workspace first fetched it at 14:02 UTC today. What the 27 Oct edition saw was true of the remote, and it listed local branches under "cannot tell you". But the overview read absence on the remote as absence of work, which the framing rules warn against. **What stands:** `I369` and `I376` were moved to REVIEW/QA on 23 Oct, four days before that commit. Nothing is merged. And the calls the screens make mostly do not match the server (thing 2 below).

**Team, at a glance:**

| Person | Owns | Board leaves | Submissions (7d) | Median cycle | Open WIP | Commits (7d) | Flag |
|---|---|---|---:|---|---|---:|---|
| Ayomikun Araoye | backend + admin API | **1002: 18** (8 To do, 4 In progress, 6 REVIEW/QA) · `I392` shared · 0901-admin: 1 In progress | **6 own** (+8 moves on teammates' items) | 1.00 d (n=19) | `I332` (**6.2 d**), `I347` (1.9 d), `I341`, `I344` (0.0 d) · `BVA-I8` on 0901-admin (**44.0 d**) | **18** (12 `beevia-api`, 2 `beevia-admin-api`, 4 `beevia-db-schema`) | Shipped the FAQ on three repos in 90 minutes. **Grant `help_center` to a role**, or no one can write content. `I352` (FAQ CMS API) is still To do although #23 shipped it |
| David Samuel | mobile | **1002: 16** (4 To do, 7 In progress, 5 REVIEW/QA) · `I392` shared | 5 (**0 own**, 5 moved by Ayomikun) | 0.99 d (n=39) | 7: `I331`, `I354` (**6.2 d**), `I346`, `I383`, `I386` (1.9 d), `I340`, `I343` (0.0 d) | **1 on `main`** · **5 on `BVA-I353`** | Card, statement and block-state work pushed today. **5 of its 6 card/statement calls do not match the server** (§2.2). The FAQ screens are not wired to the FAQ API that shipped today |
| Philip Chidera | design | **1002: 7** (2 To do, 1 In progress, 3 REVIEW/QA, 1 Done) · `I392` shared | 3 (0 own, 3 moved by Ayomikun) | 0.94 d (n=4) | `I360` (1.9 d) · `I392` (0.0 d) | n/a | Started `I392`, the first acceptance checklist on any board (§1.2) |
| Promise Udo | admin dashboard | 0901-admin: 4 (3 Done, 1 In progress) · **1002: 0** | 0 | n/a | `BVA-I9` (**44.0 d**) | **0** | `beevia-admin` **35.9 days** without a commit. The FAQ content API they would build against now exists |

**The three questions for standup:** (1) **Who gets `help_center`?** Until a role holds it, every `/admin/help/*` call is `403`, so no FAQ content can be entered and the app's FAQ screen will be empty in production. (2) **Can `BVA-I353` be pointed at the real routes before it merges?** Statements go to `POST /statements`, card termination is `POST /cards/{id}/terminate`, and reveal, unfreeze and terminate take the **card PIN**, not an account step-up token. `GET /wallets/limits` does not exist yet. The branch's own contract-test comment says these routes are "specified only in openapi.proposed.yaml", which is not true. (3) **Is there a contract for disputes before both halves start?** `I340`/`I341`/`I343`/`I344` went to In progress today on both sides. The only design on file is the proposed `/support/tickets`, and `I341`'s description (a fixed reason-code enum, the transaction's type, attachments) does not match it.

**The three things worth knowing:**

1. **The FAQ is built and documented, but cannot be filled yet.** `beevia-db-schema` #25 (v0.0.44, 12:14 UTC) adds five tables, with a generated, weighted `tsvector` and a GIN index. `beevia-api` #86 (12:40 UTC) adds `GET /help/categories`, `/help/categories/{slug}`, `/help/search`, `/help/articles/{slug}` and `POST /help/articles/{slug}/feedback`. `beevia-admin-api` #23 (13:19 UTC) adds eleven content-management routes with drafts, ordering and a "category not empty" guard. The work is careful: real-Postgres integration tests, `websearch_to_tsquery` so a typed question cannot 500, and a fix the same hour when seeded content showed whole-question searches returning nothing. **Two gaps** (`suggestions.md` §4.10). The `help_center` permission is granted to no role, and `PermissionGuard` has no bypass, so no admin can call the routes. And search ignores the `en-US` fallback that every read honours, so while only English content exists, **search returns nothing on a Spanish, French or Chinese phone**. A third, smaller one: reorder does not enforce the "send every id" its own description promises.

2. **The mobile wallet and card screens exist, on an unmerged branch, wired mostly to routes the server does not have.** `origin/BVA-I353` (pushed today, 5 commits from 23 to 28 Oct) holds the Help & Support screens from `BVA-I330` plus statement, manage-card, card-details, limits and wallet-details screens, and the client half of block state. Against `beevia-api` `origin/main` (`suggestions.md` §5.14):

   | Client call | Server reality |
   |---|---|
   | `POST /wallets/statements`, `POST /cards/{id}/statements` | **404**: the route is `POST /statements`, body `type` + `walletId`/`cardId` + `startDate`/`endDate`, sent to the account email |
   | `DELETE /cards/{id}` | **404**: the route is `POST /cards/{id}/terminate`, with the card PIN |
   | `POST /cards/{id}/reveal`, `/unfreeze` with `X-Step-Up-Token` | **400**: both need the card PIN in the body |
   | `GET /wallets/limits` | **404**: proposed only |
   | `POST /cards/{id}/freeze` | ✅ |

   The mock server and the contract test were updated to accept all of these, so the branch's own tests pass. This is `suggestions.md` §5.10 (the vendored spec) causing a real defect for the first time since the biometric step-up. On the positive side, the block-state commit (`9e489f3`) reads the server's `blocked` flag, so the profile can offer Unblock. That closes the client half of last week's recommendation 7, once merged.

3. **Review is beginning to mean something, in one place.** Today's four REVIEW/QA moves were made at 13:01–13:02 UTC by Ayomikun, 21 minutes after #86 merged. The two backend items (`I335`, `I338`) are exactly what shipped. That is the first time on 1002 that a move to review followed merged code, and the cleanest since the board resumed. The two mobile items moved in the same batch (`I334` FAQ screens, `I337` "Wire up Yes/No feedback") are placeholder screens on an unmerged branch, and `I337`'s handler is still `// TODO(support-api): POST article feedback.` Separately, `I392` is a **verification checklist** for the Activity screen. It is a Figma-linked list of `[Design]`, `[Mobile]` and `[Backend]` acceptance checks, and Philip started it at 13:28 UTC. If it is filled in, it is the first acceptance artefact on any board.

**If you read nothing else:** the server side of Help & Support moved from nothing to a documented, tested FAQ in one morning. It needs one permission grant before anyone can use it. The mobile side has more code than the last edition knew. Most of it points at routes the server does not have, and the team's own test cannot see that.

---

## 1. Board movement

### 1.1 Sprints 0902, 0901, 0901-admin and 08-01

All static. 0902 was not re-exported, because it has had no entry since its 21 Oct sweep and none of its 15 removed leaves has reappeared on 1002. The 08-01 and 0901-admin sidecars have no entry after 3 Sep and 14 Sep. The audit's `SINCE` block compares two identical 08-01 exports and correctly reports no change. `ZOHO_SPRINT_FILTER` still points at 08-01.

### 1.2 Sprint 1002

**63 items: 44 leaves + 19 parents**, up one: `I392` *Activity Screen – Verification Checklist* (Story, no parent, co-assigned to all three team members, with an attachment), created and moved in by board administration at 15:57–15:58 UTC on 27 Oct. Its description links a Figma node and lists acceptance checks tagged `[Design]`, `[Mobile]` and `[Backend]`: "four filter chips (All, Chats, Calls, Payments)", "sorted newest activity first", "one endpoint returns…". Philip moved it to In progress at 13:28 UTC today. It is a review instrument, not a build task, and the Activity screen it checks shipped across 0902 without review.

| Block | Leaves | To do | In progress | REVIEW/QA | Done |
|---|---:|---:|---:|---:|---:|
| Help & Support (`I330`–`I352`) | 15 | 2 | 9 | 4 | 0 |
| Wallet & card (`I353`–`I391`) | 28 | 13 | 4 | 10 | 1 |
| Activity checklist (`I392`) | 1 | 0 | 1 | 0 | 0 |
| **Total** | **44** | **15** | **14** | **14** | **1** |

**Movement in the window (leaves): 9 status transitions.** Eight were made by Ayomikun between 13:01:58 and 13:02:19 UTC; the ninth is `I392` (Philip, 13:28):

| Leaf | Owner | Move | Code |
|---|---|---|---|
| `I335` FAQ content API | Ayomikun | In progress → REVIEW/QA (5.0 d) | ✅ `beevia-api` #86, merged 12:40 UTC |
| `I338` Article feedback endpoint | Ayomikun | In progress → REVIEW/QA (1.9 d) | ✅ #86 |
| `I334` FAQ home, category, article and search screens | David | In progress → REVIEW/QA (5.0 d), moved by Ayomikun | ◐ `faq_screens.dart` on `BVA-I330`/`BVA-I353`; placeholder data, no `/help` call |
| `I337` Wire up Yes/No feedback buttons | David | In progress → REVIEW/QA (1.9 d), moved by Ayomikun | ◐ buttons exist; `rateArticle()` is a `TODO(support-api)` |
| `I340` Report an issue screen, `I343` dispute history screen | David | To do → In progress, moved by Ayomikun | `report_issue_screen.dart`, `dispute_history_screen.dart` already on the branch, placeholder data |
| `I341` Dispute creation & attachment upload, `I344` dispute endpoints | Ayomikun | To do → In progress | no branch on `beevia-api` |

Their parents `I333` and `I336` (FAQ) went to REVIEW/QA and `I339` and `I342` (disputes) to In progress in the same batch. No comment, reopen, block or completion was recorded in the window.

---

## 2. Sprint 1002: what is in review, and whether the code exists

### 2.1 The fourteen REVIEW/QA leaves, checked against the code

| Leaf | Owner | Code on `main` | Code on a branch |
|---|---|---|---|
| `I366` Statement generation & email | Ayomikun | ✅ #84 (27 Oct) | — |
| `I335` FAQ content API | Ayomikun | ✅ **#86 (today)** | — |
| `I338` Article feedback endpoint | Ayomikun | ✅ **#86 (today)** | — |
| `I370` Card summary & freeze endpoints | Ayomikun | existing since 27 Aug, no change | — |
| `I377` Card termination endpoint | Ayomikun | existing since 27 Aug, no change | — |
| `I358` Wallet account details endpoint | Ayomikun | no change identifiable | — |
| `I365` Build statement screen | David | ❌ | ◐ `account_statement_screen.dart` (`BVA-I353`), **calls a route that does not exist** |
| `I369` Build manage card screen | David | ❌ | ◐ `manage_card_screen.dart`: freeze ✅, **unfreeze and reveal send the wrong credential** |
| `I376` Build delete card confirmation | David | ❌ | ◐ calls `DELETE /cards/{id}`, **which does not exist** |
| `I334` FAQ screens | David | ❌ | ◐ placeholder data |
| `I337` FAQ yes/no feedback | David | ❌ | ◐ placeholder handler |
| `I364`, `I368`, `I375` | Philip | design | not visible in git |

**Three of fourteen match merged code**, all backend. Two more match endpoints that already existed. Every mobile item in review has code on `BVA-I353`, which corrects the 27 Oct reading. None of it is merged, and none of it works end to end against the real API except freezing a card.

### 2.2 `origin/BVA-I353`: what it holds

5 commits by `Davidtariq96`, 23–28 Oct, 69 files, +8,341/−104. It contains `BVA-I330` whole (3 commits) plus:

- **`9838d8e` *card implementation*** (27 Oct 09:57 UTC): wallet details, transaction limits, account statement, manage card and card details screens. Also `WalletProvider` methods, `VirtualCard`/`WalletLimits` models, a 603-line options-sheet widget file, l10n in four languages, and **mock-server routes for all seven new calls**. `spec_contract_test.dart` allowlists the seven with a comment that the card sub-routes are "specified only in openapi.proposed.yaml so far" and the statement routes "have no spec at all yet". In fact `reveal`, `freeze` and `unfreeze` have been implemented since 27 Aug, and statements shipped on 27 Oct under `POST /statements`.
- **`9e489f3` *changes to blocking users*** (28 Oct 07:25 UTC): `PeerUserProfile.blocked` read from the server, and the profile action toggles Block/Unblock.

The Help & Support half (`SupportService`, 8 × `TODO(support-api)`) is unchanged. No branch ref has a PR yet. The highest PR is #53, a Dependabot PR.

### 2.3 In progress

| Leaf | Owner | Age | Note |
|---|---|---:|---|
| `I331` Help & Support home | David | 6.2 d | on the branch |
| `I354` Wallet "more options" sheet | David | 6.2 d | **now found**: `wallet_options_widgets.dart` on `BVA-I353` |
| `I383` Card details screen | David | 1.9 d | `card_details_screen.dart` on the branch |
| `I386` Card limits screen | David | 1.9 d | `transaction_limits_screen.dart`, against the unbuilt `GET /wallets/limits` |
| `I346` Support chat screen | David | 1.9 d | on the branch, placeholder |
| `I340`, `I343` Report-an-issue, dispute history | David | 0.0 d | on the branch, placeholder |
| `I332` Open dispute count endpoint | Ayomikun | **6.2 d** | no server branch |
| `I347` Support conversation endpoints | Ayomikun | 1.9 d | no server branch; #86's message says "there is no support-chat backend" |
| `I341`, `I344` Dispute endpoints | Ayomikun | 0.0 d | no server branch |
| `I348` Triage flow configuration | **Unassigned** | 1.9 d | — |
| `I360` Highest-tier state | Philip | 1.9 d | design |
| `I392` Activity verification checklist | all three | 0.0 d | review artefact |

---

## 3. Code, API surface and spec drift

**Audit: sixteen routes in code and not in the spec, now zero.** Against a `git archive` shadow of `origin/main` (`$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-28`), the first run found five consumer routes (`/help/*`) and eleven admin routes (`/admin/help/*`) undocumented. After this cycle's edits it is clean: 146/146 consumer, 60/60 admin, proposed 38/18, spec health clean, no `x-beevia-*`. The in-repo audit reports its phantom lines from the three `diverged` working trees (now 15 consumer + 26 admin "in spec, not in code", since the frozen trees fall further behind). Those were not acted on.

**Three `main` branches moved, all today.**

| Repo | From → to | What |
|---|---|---|
| `beevia-api` | `9290c99` → `1eba51c` | #85 package update (12:01 UTC; minor and patch bumps, e.g. NestJS 12.1 → 12.3, plus an upload-fixture lint fix for `@types/multer` 2.3); **#86 Help & Support** (12:40 UTC): `src/help/` (controller, service, DTO, 15 integration tests), Postman folder. 3 non-merge commits, all `Phoenixdadhev` |
| `beevia-admin-api` | `c59460a` → `d8ed60e` | #22 package update (12:00 UTC); **#23 Help & Support content management** (13:19 UTC): `src/help-center/`, 14 tests. First change since 8 Oct |
| `beevia-db-schema` | `21dbd73` → `b49e1be` | #24 package update → v0.0.43 (11:55 UTC); **#25 FAQ content** → **v0.0.44** (12:14 UTC): migration `0040`, `faq_categories`, `faq_articles`, `faq_category_translations`, `faq_article_translations` (generated `search` tsvector + GIN), `faq_feedback`; `admin_module` gains `help_center` |

`beevia-mobile` `main` (`ccb4f63`, 22 Oct) and `beevia-admin` (`0b41e35`, 22 Sep) did not move. **No PR is open on any backend repo.** Mobile: new branch `BVA-I353` (§2.2). Dependabot **#53** (`pub-minor-and-patch`, 28 Oct) replaces #51 and still bundles `flutter_local_notifications` ^19 → ^22. #45, #47 and #50 are still open.

### 3.1 Help & Support: what shipped

Full detail in `api-rfc.md` §5.17 and `admin-api-rfc.md` §3.15.

| | App (`beevia-api`) | Admin (`beevia-admin-api`) |
|---|---|---|
| Routes | 5: categories, category, search, article, vote | 11: category and article CRUD, two reorders, publish via `PATCH` |
| Language | Caller's language, else `en-US`, for every read. **Search: caller's language only** | `en-US` on every read; writes take `locale` |
| Drafts | Never visible | Default for new content |
| Who can call | Any signed-in user | **`help_center` permission, granted to no role** |
| Tests | 15 against real Postgres | 14 against real Postgres |
| Not covered | Disputes, support chat ("There is no support-chat backend to point it at", #86) | Support inbox (`I349`/`I350`) |

### 3.2 Mobile

`main` is unchanged since PR #52. It has no conflict markers in `pubspec.yaml`, `pubspec.lock` or `project.pbxproj`. **`call.ended` is still unhandled** on `main` and on `BVA-I353`. The biometric step-up (`wallet_service.dart:78`) is unchanged.

### 3.3 The standing checks

- **Pipelines:** no workflow change on any backend `main`. `beevia-api`'s `release.yml` still says "Deliberately not `needs: test`". db-schema's Release runs on push with no `needs:`, and v0.0.44 was cut 1 min after #25 merged, ahead of #86's deploy 26 min later. admin-api's Sync → Deploy chain is unchanged.
- `PaymentService.activeNgn()` (`payment.service.ts:79`, `:138`, `:323`) and `StubTranslateAdapter` (`translate.module.ts:23`) are unchanged. `22P02` is still unmapped. `messages.ref_id` still has no index.

### 3.4 Document changes this cycle

- **`openapi.yaml`** (141 → 146 operations): `listHelpCategories`, `getHelpCategory`, `searchHelp`, `getHelpArticle` and `rateHelpArticle` under a new `Help & Support` tag. Also the `HelpSlug` parameter and schemas `HelpCategory`, `HelpCategoryDetail`, `HelpArticleSummary`, `HelpArticle`, `HelpSearchHit`, `HelpFeedbackRequest`. The search operation documents the missing fallback.
- **`openapi.admin.yaml`** (49 → 60): eleven `/admin/help/*` operations, the `Help & Support` tag, `HelpCategoryId`/`HelpArticleId` parameters and nine schemas. `help_center` was added to `AdminModule`, the activity-event module enum and the module list in `info` (11 → 12 modules). The reorder operations document the unenforced completeness rule. `UpdateHelpArticleRequest` documents the real `categoryId` key.
- **`api-rfc.md`**: header and §3 totals (146), a Help & Support row, §6.8 rows, new §5.17.
- **`admin-api-rfc.md`**: header and summary totals (60), new §3.15, module count in §3.3.
- **`suggestions.md`**: new §4.10 (no role holds `help_center`; search fallback; reorder completeness; contract slips) and §5.14 (`BVA-I353`'s routes against the server).
- `openapi.proposed.yaml` and `openapi.admin.proposed.yaml`: no change. Nothing proposed shipped. `/support/tickets` remains the only dispute design on file.

---

## 4. Risks

- **The FAQ will be empty in production until someone grants `help_center`.** The app routes are live (deploy-on-push) and return empty lists until content exists. No admin can create content until a role holds the permission, and there is no dashboard screen for it either.
- **`BVA-I353` merges with five calls broken against the real API**, unless it is corrected first. The mock and contract test are set up to pass anyway. Statement, terminate, reveal, unfreeze and limits would all fail for real users, and three of those screens are in REVIEW/QA.
- **Non-English users get no FAQ search results** while content is English-only (`suggestions.md` §4.10).
- **Disputes are now being built from both ends with no shared contract.** Four dispute leaves went In progress today, and the only design on file (`/support/tickets`) does not match `I341`'s description.
- **The review column still mixes merged work with placeholder screens.** 3 of 14 items match merged code. If 1002 is closed by sweep the way 0902 was, the placeholder and mis-wired items will be recorded as delivered.
- **`call.ended` is still unconsumed** on any branch.
- **Every backend repo still deploys or migrates production on push without a test gate.** Today that was six merges and two schema releases, one 1 min after merge. Both feature PRs carry real integration tests that CI does not gate on.
- **The admin workstream:** 35.9 days without a `beevia-admin` commit and 44.0 without admin-board activity. The FAQ CMS has an API, but no dashboard owner or task.
- Carried, unchanged: statement PDF password (§4.8); blocks do not reach payments (§4.9); 0902's 15 removed leaves (not visible); wallet-failure notices off by default; possible pre-12 Oct PII in logs; malformed path ids return `500` (§1.1); production SSH (unverified); biometric step-up on `main` (§5.11); Firebase keys in history; three diverged local working trees.

---

## 5. PRD gap

Unchanged. The four structural gaps (international KYC, multi-currency/FX settlement, consent management, and virtual cards beyond what is wired) carry 32 of the rubric's 100 points. Help & Support is real product work that the PRD's support promises rely on, but it is not a rubric capability. Card management on `BVA-I353` touches line 9, but it is unmerged and mostly mis-wired, so it does not move the score.

---

## 6. Team performance: detail

All flow figures come from the activity sidecars (the `actiontime` of each transition), never from `Last Modified`. The 7-day window is 21 Oct 14:04 → 28 Oct 14:04 UTC. Commit counts are non-merge commits on `origin/main` in that window, summing each person's git identities (`Phoenixdadhev` + `Ayomikun Araoye`; `Davidtariq96` + `David Samuel`), with bots excluded. Branch commits are listed separately. WIP ages run from each item's last entry into In progress. **Submissions are split by who made the move.** Cycle times use 0901, 0902 and 1002.

### 6.1 Ayomikun Araoye: backend + admin API

**18 commits in 7 days**: 12 in `beevia-api` (iOS ring path, names, the one-call guard, block state, statements, package update, FAQ), 4 in `beevia-db-schema` and 2 in `beevia-admin-api`. Today's FAQ shipped across three repos in about 90 minutes, each commit explaining what it chose and which test fails without it. #86's follow-up fix came from seeding real content and noticing that the first test had passed by accident. **6 own submissions** (`I370`, `I377`, `I366`, `I358`, `I335`, `I338`), and 8 moves of David's and Philip's items. Median cycle **1.00 d (n=19)**. WIP: `I332` (6.2 d, past their median, with no server branch), `I347` (1.9 d) and the two dispute endpoints started today. `BVA-I8` has been In progress on the closed admin board for 44.0 days. `I352` (*FAQ Content Storage & Publish Endpoints*) is still To do although #23 delivered it. That is a board-hygiene note, not an output one.

### 6.2 David Samuel: mobile

**1 commit on `main`** (`8039bd7`, 21 Oct, via PR #52) and **5 on `origin/BVA-I353`**: Help & Support screens, sorting, card implementation and block state. **Zero own submissions**: the last was `I286` on 14 Oct, **13.9 days** ago. Their five 7-day "submissions" are Ayomikun's moves. Median cycle **0.99 d (n=39)**. WIP: **7 items**, still the most on the board. `I331` and `I354` are at 6.2 d, but both have visible branch work. The 27 Oct edition read the missing remote branch as missing work, and that was wrong (see the correction). The open question is one of contract: whether the branch's routes can be checked against the server spec before merge, not whether work is happening.

### 6.3 Philip Chidera: design

No submissions of their own in the window. Their three REVIEW/QA items were moved by Ayomikun on 23 and 27 Oct. Started `I392` today, the Activity screen's acceptance checklist. If it is used as written, with design, mobile and backend checks against a Figma node, it is the first review instrument the project has had. WIP: `I360` (1.9 d), `I392`. Design files are not in git, so the board is the only record.

### 6.4 Promise Udo: admin dashboard

**No commit in the window.** The last was `0b41e35` on 22 Sep, **35.9 days** ago. The admin board has had no activity for 44.0 days, and `BVA-I9` has been In progress for all of it. Today's admin FAQ API is the first new backend surface a dashboard screen could be built against since September. Its Story, `I351`, is unassigned. **Absence of data is not absence of work**: `beevia-admin` has only `main`, so local work would be invisible. But five weeks without a commit, a board item or a sprint is still worth one direct question.

### 6.5 Weekly submission trend (leaves, transitions into REVIEW/QA)

| ISO week | 0901 | 0902 | 1002 | by the leaf's owner | by another team member | by board administration |
|---|---:|---:|---:|---:|---:|---:|
| 2026-W39 | **42** | — | — | 15 | 0 | 27 |
| 2026-W40 (28 Sep → 4 Oct) | 1 | 0 | — | 1 | 0 | 0 |
| 2026-W41 (5 → 11 Oct) | — | **10** | — | 4 | 1 | 5 |
| 2026-W42 (12 → 18 Oct) | — | **8** | — | 2 | 1 | 5 |
| 2026-W43 (19 → 25 Oct) | — | 0 | **6** | 2 | 4 | 0 |
| 2026-W44 (from Mon 26 Oct, to 14:04 UTC Wed) | — | — | **8** | 4 | 4 | 0 |

**Acceptance is still zero.** Leaving aside the three bulk sweeps (3 Sep, 30 Sep, 21 Oct), no item has been accepted by someone other than its submitter since `BVA-I268` on 16 Sep. Ayomikun makes every move into review on 1002, on everyone's items. The bottleneck is still the review step, not the developers. `I392` is the first sign of a review step being designed.

### 6.6 What this does not measure

- **No estimation points on any item on any board.** Seven WIP items for David and four for Ayomikun are not comparable loads.
- **Unpushed work.** This edition is itself the example: a full day of card screens was invisible to the 27 Oct edition.
- **Who moved an item is not whether it is done.**
- **Nothing here measures correctness.** No build, test or lint ran in any repository. The route mismatches in §2.2 come from reading code on both sides, not from running the app.

---

## 7. Previous recommendations: where they stand

| Recommendation from 27 Oct | Status on 28 Oct |
|---|---|
| **1. Make REVIEW/QA mean "built, please verify"** | ◐ **Partly.** Today's two backend moves followed the merge by 21 min. `I365`/`I369`/`I376` were not moved back; their code exists on a branch but does not match the server. No notes on `I370`/`I377`/`I358` |
| **2. Account for 0902's 15 leaves** | ? **Not visible.** None has reappeared on 1002 |
| **3. Write the Help & Support contract first** | ◐ **FAQ half done in code**: shipped and documented today. Disputes and support chat started on both sides today with no contract. `I348` still unassigned |
| **4. Handle `call.ended` on the client** | ❌ **Not done**, on `main` or any branch |
| **5. Test the iOS ring on a real device** | ? **Not visible** |
| **6. Decide the statement password and delivery model** | ❌ **No change.** The client's statement sheet sends an `email` field the server does not accept, which suggests the client expects a user-chosen address |
| **7. Decide blocks vs payment requests; read `blocked` on the client** | ◐ **Client half on a branch** (`9e489f3`). Payments unchanged |
| **8. Set `ZOHO_SPRINT_FILTER` to `1002`** | ❌ **Not done** |
| **9. Give the admin dashboard a home** | ❌ **No.** The FAQ CMS API shipped, but its Story is unassigned and the admin board has no sprint |
| **10. Put `needs: test` back on `beevia-api`'s `sync`** | ❌ **Not done** |
| **11. Generate `openapi.yaml` from the app and diff it in CI** | ❌ **Not done.** Today 16 routes reached production undocumented |
| **12. Split `flutter_local_notifications` 19 → 22 out of Dependabot** | ❌ **Not done.** #51 was replaced by #53, which still bundles it |
| **13. Add the `messages.ref_id` index** | ❌ **Not done** |
| **14. Carried items** | ❌ **None moved** |

**Two partly done, none fully.** That is expected for a 0.9-day window, and most of today's work went to Help & Support.

---

## 8. What I would do this week

1. **Grant `help_center`** to the role that will own FAQ content, and to Super Admin, in a seed or migration so that a fresh environment does not depend on a manual click. Then enter the launch FAQ (`suggestions.md` §4.10.1).
2. **Correct `BVA-I353` before it merges.** Statements go to `POST /statements`. Reveal, unfreeze and terminate use the card-PIN sheet, and terminate is `POST /cards/{id}/terminate`. Hide the limits screen until `GET /wallets/limits` exists. Remove the seven allowlist entries from `spec_contract_test.dart` rather than editing them (`suggestions.md` §5.14).
3. **Stop vendoring the client spec** (`suggestions.md` §5.10). It has now caused a real defect: today's branch was written against a copy that lacks `/statements` and the card-PIN model.
4. **Wire the FAQ screens to `/help/*`.** The API exists and is documented. `I334`/`I337` are in REVIEW/QA on placeholder data.
5. **Add the `en-US` fallback to FAQ search** before any non-English user opens the help box (`suggestions.md` §4.10.2).
6. **Agree a dispute contract before the four dispute leaves go further.** Add it to `openapi.proposed.yaml` in place of, or reconciled with, `/support/tickets`, with `I341`'s reason-code enum and transaction type. Decide who owns `I348` (triage).
7. **Use `I392` as the pattern for review.** One checklist per feature, ticked by someone other than the builder, before Done.
8. **Handle `call.ended` on the client**, the last open call-path item.
9. **Make REVIEW/QA mean merged.** Move `I365`, `I369`, `I376`, `I334` and `I337` back to In progress until their code is on `main`. Mark `I352` Done or merge it into `I335`.
10. **Give the admin dashboard a home**: assign `I351`'s UI work (the FAQ CMS screen) to Promise on an admin-board sprint, or say the dashboard is paused.
11. **Put `needs: test` back on `beevia-api`'s `sync`**, and give db-schema's Release and admin-api's Sync a verify job. Today's PRs each carry real-Postgres tests that nothing gates on.
12. **Generate `openapi.yaml` from the running app and diff it in CI** (`suggestions.md` §5.4).
13. **Set `ZOHO_SPRINT_FILTER` to `1002`.**
14. **Carried:** decide the statement password and delivery model (§4.8); blocks vs payment requests (§4.9); account for 0902's 15 leaves; test the iOS ring on a device; split `flutter_local_notifications` out of #53; add the `messages.ref_id` index; restrict the Firebase API keys; decide the `walletActivity` default; check production logs for pre-12 Oct PII; map `22P02` to `400`; make Flutter CI a required check; check the production host's SSH settings; hide the biometric option outside mock mode until `I381` lands; and the longer tail listed on 27 Oct.

---

## Admin dashboard board

`0901-admin` still has 12 items (8 leaves + 4 parents: 6 leaves Done, 2 In progress). It is closed, and nothing on it has changed since **14 Sep 14:53 UTC, 44.0 days ago**. `BVA-I8` (*Report Data Query*, Ayomikun) and `BVA-I9` (*Report Content Display*, Promise) have both been In progress for all 44 days. **Zoho lists no successor sprint for this project.** Admin-dashboard work is instead on the consumer board's 1002, as two unassigned Stories (`I349` Support Inbox, `I351` FAQ CMS). The API under `I351` shipped today in `beevia-admin-api` #23, its first change in 20 days. `beevia-admin` has gone 35.9 days without a commit. These figures are never added to the main board's.

---

## Appendix: method and readiness rubric

### MVP readiness: ≈67% (estimate; 67.32, unchanged)

**Target 2026-09-01 (provisional). The target date passed fifty-seven days ago.** Weights are frozen, and **this edition makes no methodology change.** Scores measure build on `main`, not acceptance, and not correctness.

No line moves. Help & Support (FAQ) is not a rubric capability, and its admin half is content management outside the dashboard spec's eight modules, so line 11 is unaffected. The card-management screens touch line 9, but they are on an unmerged branch and mostly call routes the server does not have. The scoring rule is that a stub adds at most ~0.1, and branch code adds nothing until it is on `main`. Block state on the client is metadata. `call.ended` is still unhandled, so line 2 stays at 0.92.

| # | Capability | Weight | Score | Δ | Evidence |
|---|---|---:|---:|---:|---|
| 1 | E2EE messaging | 15 | 0.90 | 0 | No crypto, key or socket change |
| 2 | Voice & video calling | 8 | 0.92 | 0 | `call.ended` push still unhandled on any branch |
| 3 | Message translation | 7 | 0.60 | 0 | `translate.module.ts:23` still binds `StubTranslateAdapter` |
| 4 | Local KYC tier (BVN) | 8 | 0.90 | 0 | No `/kyc` or `/upgrade` change |
| 5 | International KYC tier | 6 | 0.00 | 0 | Proposed only |
| 6 | Multi-currency wallets | 12 | 0.85 | 0 | `activeNgn()` unchanged; `GET /wallets/limits` still proposed |
| 7 | Send / request / receive in chat | 12 | 0.92 | 0 | Biometric option still on `main` (`wallet_service.dart:78`) |
| 8 | Cross-currency FX settlement | 12 | 0.00 | 0 | `/fx/*` proposed only |
| 9 | Virtual cards | 10 | 0.80 | 0 | No server card change. Client manage, reveal and terminate on unmerged `BVA-I353`, 5 of 6 calls mismatched (§2.2) |
| 10 | Consent management | 4 | 0.00 | 0 | No endpoint, record or board item |
| 11 | Admin oversight | 6 | 0.97 | 0 | No `beevia-admin` commit since 22 Sep; FAQ CMS is outside the eight modules |
| | **Weighted total** | **100** | **67.32** | **0** | **≈67%** |

### What this report cannot tell you

- **Whether the FAQ routes are live in production**, beyond deploy-on-push implying they are. Also whether any content or role grant has been entered by hand since.
- **Whether `BVA-I353`'s screens are reachable** in the built app, or whether the author is already correcting the routes locally. This edition is itself evidence that local work can be a day ahead of the remote.
- **What the design items in review contain.** Design files are not in git.
- **Where 0902's 15 leaves went.** The export reads sprints, not the backlog.
- **Whether any PR was reviewed**, or whether branch protection requires CI on any `main`.
- **Velocity for any sprint.** Nothing on any board is estimated.

### Method

**Pipeline.** The `beevia-refresh` steps ran in this order:

1. Board exports, run in parallel and finished by about 14:00 UTC. Main board (step 1a): 64 items, sprint 08-01, exit 0. Admin board (step 1b) with `--sprint 0901-admin`: 12 items, exit 0. Read-only scratch export of **1002** with `--modified --activity` to `/tmp/beevia-scratch/1002/`: 63 items, exit 0. 0902 and 0901 were not re-exported; both are closed and static.
2. Fast-forward sync (step 2), exit 1. `beevia-admin` and `beevia-mobile` were already current, with no branch switch. `beevia-api`, `beevia-admin-api` and `beevia-db-schema` were refused as `diverged` (unchanged since 8 Sep).
3. Audit (step 3) against a `git archive` shadow of `origin/main` at `$BEEVIA_ROOT=/tmp/beevia-shadow-2026-10-28`: exit 1 (5 + 11 undocumented routes) before this cycle's spec edits, exit 0 after. The in-repo audit was run too, for the board section and the RFC-count check (exit 1, phantom lines only). Both ran through `uv run --no-project --with pyyaml`.
4. Board analysis (`q28.py`, `flow28.py`): 1002 day-over-day diff, every transition in the window by actor, cycle times, 7-day submissions split by actor, WIP ages, weekly trend, and a sweep for comments, reopens and completions (none in the window).
5. Content checks. `git fetch --all --prune`, `for-each-ref` and `ls-remote` (including `refs/pull/*`) on every repo, and the remote-tracking reflog for when `BVA-I353` first appeared. In `beevia-api`: all commit messages since `9290c99`, the help controller, DTO, service and module, the card controller's reveal, unfreeze and terminate contracts, the statements controller, `release.yml`, and the standing greps. In `beevia-admin-api`: the help-center controller, DTO and service, `PermissionGuard`, and how `ADMIN_MODULES` is derived. In `beevia-db-schema`: migration `0040`, the enum change, and whether any role is granted `help_center` (none). In `beevia-mobile`: `BVA-I353`'s diff, every new `wallet_service.dart` call against the server routes, the mock routes and contract-test allowlist, `SupportService`'s placeholders, `blocked` handling, `call.ended`, conflict markers, the biometric step-up, and Dependabot #53's `pubspec.yaml`.
6. Spec and RFC updates (§3.4).
7. This report and its web edition.
8. End-of-run recheck at 14:13 UTC. A fast re-export of 1002 (`--activity --no-descriptions`, exit 0) found no board action after 13:28 UTC. `ls-remote` showed every `main` at the commits read above, no new branch or PR on any repo, and no open backend PR.

**A note on who appears here.** Only people whose work is tracked have rows. Board administration is done by a non-contributor, whose actions are reported without naming the actor.

**Nothing was executed from any sub-repo.** No `npm`, `node`, `flutter` or build step ran. No repository was reset, rebased or cleaned, and no sub-repo file was edited. The sync's `--ff-only` limit was not overridden. Beyond the sync's own `fetch`, the only git operations were `fetch`, `ls-remote`, `reflog`, `git archive`, and read-only `log`/`show`/`diff`/`grep`/`for-each-ref`. Nothing was committed, pushed or deployed.

**Files changed this cycle:** this report, `web-report/2026-10-28.html`, `web-report/index.html`, `openapi.yaml`, `openapi.admin.yaml`, `api-rfc.md`, `admin-api-rfc.md`, `suggestions.md`, plus new board exports for 28 Oct in `sprint-board-exports/` and `sprint-board-exports/admin/`.

**Degraded inputs.**

- **`ZOHO_SPRINT_FILTER` is still `08-01`**, so the in-repo main export is a frozen closed sprint, and the audit's `SINCE` block compares two identical snapshots. All 1002 figures come from the scratch export.
- **0902 and 0901 were not re-exported.** Both are closed, and their 27 Oct and 19 Oct copies were reused for cycle times.
- **The default `python3` has no PyYAML**, so `audit.py` exits 2 when run exactly as the skill documents. Both audits ran through `uv run --no-project --with pyyaml`.
- **Three repositories remain unsynced.** `beevia-api`, `beevia-admin-api` and `beevia-db-schema` are `diverged`. Every backend claim is made against `origin/main` through the shadow.
- **Push times are not visible.** Commit dates show when work was written, not when it reached `origin`. `BVA-I353`'s arrival is bounded by the 27 Oct recheck (16:06 UTC) and this workspace's first fetch (28 Oct 14:02 UTC).
- **GitHub PR metadata, reviews, settings, CI results and deploy state cannot be seen from here.**
- **The export's "no source key" warning fired on `Epic`.** This is the known sampling artefact; 1002's items genuinely have no epic.

**Window.** 27 Oct 15:55 UTC → 28 Oct 14:05 UTC. All `actiontime` and board figures are in UTC. `git log` timestamps were converted from their local offsets.
