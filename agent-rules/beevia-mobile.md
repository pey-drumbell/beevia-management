# beevia-mobile — agent rules

The Beevia Flutter app. Dart SDK ^3.5.1, Provider for state, Dio for HTTP,
Socket.IO, libsignal for E2EE, Hive for local chat storage, LiveKit for calls.

Read `../agent-rules/shared-testing-principles.md` first.

---

## 1. Current state

Three test files exist (`test/mock/*_test.dart`), all exercising the mock
backend. CI runs `flutter test` but **not `flutter analyze`**, and collects
**no coverage**. Treat the suite as a seed, not a safety net, and grow it in
the priority order in §4.

## 2. Commands

```bash
flutter pub get
flutter analyze                 # must be clean — zero warnings, not just zero errors
flutter test
flutter test --coverage         # → coverage/lcov.info
flutter test test/path/to/file_test.dart
```

Before a PR: `flutter analyze && flutter test`. A new analyzer warning is a
failing build even if CI does not yet enforce it (see §7).

## 3. Conventions

- Tests live under `test/`, mirroring `lib/`'s structure, named `*_test.dart`.
  `test/support/` holds shared doubles — **reuse it, do not re-implement**:
  - `secure_storage_test_double.dart` → `fakeSecureStorage()` installs
    flutter_secure_storage's in-memory platform;
  - `mock_session.dart` for an authenticated session.
- Standard preamble for anything touching platform channels or the network
  (see `test/mock/wallet_mock_test.dart` — copy it):

  ```dart
  TestWidgetsFlutterBinding.ensureInitialized();

  setUpAll(() {
    dotenv.loadFromString(envString: 'BASE_URL=https://mock.local');
  });

  setUp(() {
    fakeSecureStorage();
    SharedPreferences.setMockInitialValues({...});
    MockBackend.install();
  });

  tearDown(() => MockBackend.reset());
  ```

- **`MockBackend.install()` in `setUp`, `MockBackend.reset()` in `tearDown`** —
  always both. A leaked adapter makes the *next* test file fail, which is the
  worst kind of flake to debug.
- Never load `.env` from disk in a test; `dotenv.loadFromString` keeps the test
  host free of assets.

## 4. What to test, in priority order

1. **`lib/core/crypto/**` and `lib/core/attachment_crypto/**` — highest value
   in the repo.** Mandatory cases: encrypt → decrypt round-trips to the
   original bytes; a **tampered ciphertext or MAC fails loudly** rather than
   returning garbage; wrong key fails; empty and large payloads; key
   serialisation survives a store/load cycle. Silent E2EE failure is the worst
   bug this app can ship.
2. **`lib/core/network/**` — request building and response mapping.** Headers
   and auth token attachment, error mapping (401 → session expiry, 4xx vs 5xx
   vs timeout vs offline), retry/refresh logic. Drive it through
   `MockBackend`, as the existing tests do.
3. **`lib/core/storage/**` and Hive models.** Round-trip persistence, schema/
   adapter compatibility with existing stored data (`local_message.g.dart` is
   committed — a field change that breaks reading old records is a data-loss
   bug), and behaviour when storage is empty or corrupt.
4. **`lib/core/socket/**`.** Connect/disconnect, reconnect with backoff, event
   dispatch to the right listener, and message handling while offline →
   queued → flushed on reconnect. Use a fake socket; never a real connection.
5. **`lib/features/*/services/**`.** Service-level tests against
   `MockBackend`, asserting the parsed domain result, not the raw map, once a
   typed model exists.
6. **State/providers (`ChangeNotifier`s).** Assert state transitions and that
   `notifyListeners` fires for the transitions the UI depends on; assert the
   error state is reachable and recoverable.
7. **Widget tests — only where there is logic**: conditional rendering,
   validation messages, disabled/loading buttons, list empty states. Use
   `pumpWidget` with the minimal provider scope, and `pumpAndSettle` for
   animations.
8. **Golden tests — do not add** unless a specific visual regression justifies
   one. They break on every font/renderer bump and cost more than they catch
   at this stage.

## 5. Determinism rules

- **No real network, ever.** `MockBackend` intercepts at Dio's
  `HttpClientAdapter`; anything that bypasses it is a bug in the test.
- No real secure storage, shared preferences, file system, or camera —
  use the doubles in `test/support/`.
- No `Future.delayed` as a synchronisation device. Use
  `tester.pumpAndSettle()`, `fakeAsync`, or await the actual future.
- Fix time and UUIDs by injection where output is asserted; do not assert on
  `DateTime.now()`.
- Every test must pass in isolation **and** in a full `flutter test` run.
  Global singletons (`networkService`, `MockBackend`) are the usual culprit —
  reset them in `tearDown`.

## 6. Widget test rules

- Find by semantics/text, not by widget-tree position or private type.
- Assert user-visible outcomes: text shown, button enabled, navigation
  occurred.
- Keep the widget under test small. If a widget needs half the app's providers
  to render, that is a design signal — extract the logic and unit-test it.
- Do not `pumpAndSettle` an infinite animation (loading spinners) — pump a
  fixed duration instead, or the test hangs until timeout.

## 7. Setup this repo is missing (proposed, not applied)

1. **Add `flutter analyze` to CI**, in `flutter-ci.yml`'s `test` job, before
   `flutter test`. It is the cheapest quality gate available and is currently
   absent.
2. **Collect coverage**: `flutter test --coverage`, then filter `lcov.info` to
   exclude `lib/gen/**`, `**/*.g.dart`, `lib/mock/**` (test infrastructure,
   not product code), and `lib/main.dart` / `lib/app.dart` (bootstrap).
   Publish the summary on the PR; set the threshold at the measured baseline
   and ratchet.
3. **Tighten `analysis_options.yaml`.** It currently includes
   `package:flutter_lints/flutter.yaml` with every optional rule commented
   out. Enable at least `avoid_print`, `prefer_single_quotes`,
   `always_declare_return_types`, and `unawaited_futures` — the last one
   catches a real class of async bug the analyzer is otherwise silent about.

## 8. Things not to do

- Do not add `hive_generator` back as a build dependency to regenerate an
  adapter — see the note in `pubspec.yaml`; the generated adapter is committed
  deliberately because the generator cannot resolve against this SDK.
- Do not commit changes to `lib/gen/**` or `*.g.dart` by hand.
- Do not write a test that only asserts a widget "renders without throwing".
  That is what `flutter analyze` plus the next real test already gives you.
- Do not put fixtures in `lib/mock/` that only tests use, or ship test-only
  code in the app bundle.
- Do not skip a test to land a PR without a linked ticket in the skip reason.
