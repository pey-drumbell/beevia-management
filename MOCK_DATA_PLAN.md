# Plan: mocking the backend for independent mobile development

*Branch: `Mock-data`. Analysis + plan only — nothing implemented yet.*

**Goal:** let the app run, be developed, be unit-tested and be screenshotted via
Maestro without a backend, while keeping production code paths honest.

---

## 1. What the app actually depends on

Six distinct external dependencies, with very different mockability:

| # | Dependency | Surface | Mockable? |
|---|---|---|---|
| 1 | **REST API** (Dio) | 23 endpoints, 25 call sites, 4 services | **Fully** |
| 2 | **Socket.IO** | 8 events (3 chat, 5 call), 10 call sites | **Fully** (needs a small seam) |
| 3 | **Signal E2EE** (`libsignal_protocol_dart`) | key bundles, session setup, encrypt/decrypt | **Fully, with real crypto** |
| 4 | **LiveKit** (WebRTC media) | `Room().connect()`, tracks, participants | **No** — see §5 |
| 5 | **Device capabilities** | contacts, camera, permissions, file picker | **Partly** — see §5 |
| 6 | **Local storage** | Hive, `flutter_secure_storage`, SharedPreferences | Real on device; **needs fakes in `flutter test`** |

### The seams that make this cheap

Two facts make this much easier than it looks:

```dart
// lib/core/network/network_service.dart — mutable global, every REST call goes through it
Dio networkService = NetworkService().dio;

// lib/core/socket/socket_manager.dart — mutable global
io.Socket? socketInstance;
```

Every one of the 25 HTTP call sites uses that single `Dio`. Swapping its
`httpClientAdapter` intercepts **all** REST traffic at the transport layer —
below the auth/refresh interceptor, so the 401→refresh logic still genuinely
runs and can be exercised. **Zero production changes needed for REST.**

`main.dart` is already a clean composition root (it wires socket listeners),
which gives a natural place to install mocks.

---

## 2. Recommended architecture: in-app mock, flag-driven

```
lib/mock/                      # only reachable when MOCK=true
  mock_config.dart             # flags, scenario selection, seeded clock
  mock_backend.dart            # install()/reset() entry point
  http/
    mock_http_adapter.dart     # Dio HttpClientAdapter -> router
    routes/                    # one handler per endpoint group
      auth_routes.dart  kyc_routes.dart  contacts_routes.dart
      conversations_routes.dart  keys_routes.dart  wallet_routes.dart
  socket/
    fake_socket_client.dart    # in-memory event bus + scripted inbound events
  crypto/
    mock_peer.dart             # a simulated *second device* with real Signal keys
  state/
    mock_server_state.dart     # mutable in-memory "database"
  fixtures/                    # deterministic JSON + scenario definitions
    scenarios/{fresh,onboarded,busy_chat,kyc_pending,error_states}.dart
```

### Entrypoint: separate `main_mock.dart` over a `--dart-define` flag

`main()` currently does six things inline — binding init, `Hive.initFlutter()`,
`LocalMessageStore.registerAdapters()`, `dotenv.load()`, two
`addSocketConnectedListener` calls, and `runApp` with a **5-provider
`MultiProvider`**. A second entrypoint that restated all of that would duplicate
~20 lines, and the dangerous part is the provider list: add a sixth provider to
`main.dart`, forget `main_mock.dart`, and the mock build diverges silently.

That duplication is an artifact of `main()` doing the work inline, not of having
two entrypoints. Extract the boot sequence and it disappears:

```dart
// lib/bootstrap.dart — single source of truth for boot + providers
Future<void> bootstrap({bool useMocks = false}) async {
  WidgetsFlutterBinding.ensureInitialized();
  ...
  if (useMocks) await MockBackend.install();
  runApp(MultiProvider(providers: [...], child: const MyApp()));
}

// lib/main.dart
void main() => bootstrap();

// lib/main_mock.dart
void main() => bootstrap(useMocks: true);
```

```bash
flutter run -t lib/main_mock.dart --dart-define=MOCK_SCENARIO=busy_chat
```

With `bootstrap()` extracted, the separate entrypoint costs one line per file
and is **strictly safer**: a `flutter build` of `lib/main.dart` never has
`lib/mock/` in its reachable graph at all. The `--dart-define` alternative
relies on tree-shaking to strip a `const bool.fromEnvironment` branch — which
does work in practice, but "not reachable" beats "we trust the compiler removed
it" for code that fabricates auth tokens and bypasses KYC.

`--dart-define` is still used for *scenario selection*, since that varies per
run rather than per build.

**Why in-app rather than a local mock server** (e.g. Dart `shelf` or Node):

- Works unchanged in `flutter test`, on emulator, on device, and in CI — no
  process lifecycle, no `10.0.2.2` host-networking special cases for Maestro.
- Deterministic: no ports, no races, no "did the server start yet".
- Cost: it doesn't exercise the real HTTP socket stack. Since we swap the
  *adapter* rather than stub the services, everything above the wire (Dio
  options, headers, interceptors, serialisation, error mapping) is still real,
  so this loses very little.

A local server remains a reasonable **later** addition for contract-testing
against the real API shape; it is not the right primary.

---

## 3. The interesting part: E2EE can be mocked *without* faking crypto

The naive approach is a `MOCK_SKIP_CRYPTO` flag that bypasses encryption. That
would hollow out the single most bug-prone path in the app.

Better: **the mock backend owns a simulated peer device that holds real Signal
keys.** Using `libsignal_protocol_dart` on the mock side, it can:

1. Serve a genuine, verifiable `PreKeyBundle` from `GET /keys/:userId`
   (the `KeyBundleResponse` shape already matches X3DH: `identity_key`,
   `signed_prekey`, `signed_prekey_sig`, `registration_id`, `one_time_prekey`).
2. **Decrypt** what the app emits on `message.send` — proving the app's
   `SessionBuilder.processPreKeyBundle` + `SessionCipher.encrypt` path is correct.
3. **Re-encrypt** a reply and push it back as a `message.created` socket event,
   which the app decrypts through the untouched real code in
   `chat_events._handleIncomingMessage`.

Result: the full E2EE round trip is exercised with real cryptography, no
production code changes, and mock "replies" that are actually readable. This
also makes the crypto path testable in CI for the first time.

Fallback if this proves fiddly: a `plaintext` passthrough mode behind a flag —
usable for pure UI work, but explicitly *not* the default.

---

## 4. Endpoint inventory (all 23 — all mockable)

| Group | Endpoints | Notes |
|---|---|---|
| Auth | `/auth/register`, `/auth/login`, `/auth/otp/request`, `/auth/otp/verify`, `/auth/pin`, `/auth/refresh`, `/auth/logout` | Fixed OTP (`123456`); wrong code returns a real error envelope. Short-lived tokens so the refresh interceptor can be exercised on demand. |
| Onboarding | `/onboarding/path`, `/onboarding/profile` | Drives the `chat_only` / `chat_banking` branch. |
| KYC | `/kyc/email`, `/kyc/email/verify`, `/kyc/bvn`, `/kyc/bvn/verify-ownership`, `/kyc/profile` | Canned BVN identities: one that verifies, one that mismatches, one that errors. |
| Wallet | `/wallets/payin-details?walletId` | Static account details. |
| Contacts | `/contacts/sync`, `/contacts`, `/users/lookup`, `/invites` | Split of on-Beevia vs invitable is fixture-controlled. |
| Chat | `/conversations` (GET + POST), `/conversations/:id/messages` | Paginated history with `afterSeq`/`beforeSeq` honoured. |
| Devices/Keys | `/devices` (POST + GET), `/keys/:userId` | Backed by the mock peer (§3). |

Each handler should support **latency and failure injection** so loading and
error states are reachable on demand — those states are currently almost
impossible to develop against.

---

## 5. What can NOT be fully mocked — and what to do instead

Answering the question directly:

### 5a. LiveKit / WebRTC calls — **not mockable in-process**

`CallProvider` constructs a concrete `Room()` and calls `room.connect(url,
token)`. There is no interface to substitute, and real media needs an SFU plus
platform WebRTC.

**Decided: signalling-only for now; a local LiveKit server comes later.**

Signalling-only means mocking the `call.*` socket events so the call **UI and
state machine** (incoming → ringing → active → ended/declined) are fully
drivable, while `room.connect()` is never reached. That covers every call
screen and every state transition, with no media. It is enough for development
and for Maestro screenshots.

Because a real local LiveKit is planned, the implementation must **not**
hard-code "no media". Design for the swap now:

- Introduce a `CallTransport` seam with `LiveKitTransport` (real, today's code
  verbatim) and `NoopTransport` (connects nothing, reports connected). Select it
  in `bootstrap()` alongside the other mocks.
- Keep the mock backend's `call.*` handlers issuing **real-shaped** payloads
  including a `token` and room name, so that when a local LiveKit arrives only
  the token needs to become a genuinely signed one — no handler rewrites.
- Make the transport choice independent of the mock-backend choice, so
  `main_mock.dart` + real LiveKit is a valid combination later
  (`--dart-define=MOCK_CALL_TRANSPORT=livekit`).

Without that seam, the mock guard would be an `if` buried inside
`_connectToRoom`, and adding local LiveKit later would mean unpicking it.

### 5b. Device capabilities — **need seams, not mocks**

| Capability | Problem | Approach |
|---|---|---|
| `flutter_contacts` | Reads the real address book; `requestPermission()` is OS-level | Extract a `ContactsSource` interface; fake returns a fixed 30-contact list. Also removes the current inability to test contact sync. |
| `image_picker` (selfie/KYC) | Opens the real camera | `ImageSource` seam returning a bundled asset image. |
| `permission_handler` (calls) | OS dialogs | Fake returns granted. Maestro can also auto-grant at install time. |
| `file_picker` | OS picker | Same seam pattern; lowest priority (attachment flow is stubbed already). |

### 5c. Storage in `flutter test` — **needs fakes**

- `flutter_secure_storage` has **no implementation in the Dart VM test host** —
  any widget test touching `LocalStorageService` or `SignalKeyStore` throws
  today. Needs `setMockMethodCallHandler` or an in-memory implementation.
- `Hive` needs `Hive.init(tempDir)` in tests rather than `initFlutter()`.
- SharedPreferences needs `setMockInitialValues`.

These are prerequisites for *any* automated testing, mock backend or not.

### 5d. Also worth knowing

- `dotenv.load(fileName: ".env")` runs before anything; `SocketConstants`
  reads `LIVEKIT_URL` with a **non-null assertion**, so a missing key crashes at
  startup. The mock config must supply values (or a mock `.env`).
- `.env` is currently **tracked in git** with real URLs. Unrelated to this work,
  but it should probably be untracked and templated.

---

## 6. Designing the mock data for Maestro

Screenshot and E2E runs need more than "some data" — they need *determinism*:

- **Fixed seed, frozen clock.** All timestamps derive from one injected
  `MOCK_NOW`, so "9:41 AM" never drifts and screenshots are diffable.
- **Obviously-fake, self-labelling content.** *(Decided.)* Every fixture must be
  unmistakable as mock data at a glance, so a stray mock build can never be
  mistaken for real user data and a screenshot can never be mistaken for a
  production one:
  - Names from a fixed cast: `Ada Testerson`, `Mock Mockington`, `Sam Sample`.
  - Phone numbers in the reserved-for-fiction ranges (`+234 700 000 00xx`).
  - Emails on `@example.com` (RFC 2606, guaranteed unroutable).
  - BVNs / account numbers as visibly patterned digits (`00000000001`).
  - Money in a `MOCK` pseudo-currency or with an obvious sentinel amount, never
    a plausible NGN balance.
  - A persistent **`MOCK DATA` banner** in debug builds (a `Banner` widget in
    `bootstrap()` when `useMocks` is true).

  The content still has to exercise *layout* — long names that truncate, long
  messages that wrap, unread badges, empty states, an emoji message — but the
  strings themselves stay unambiguous. These screenshots are for regression
  diffing, not marketing.
- **Scenario per state**, selected by `--dart-define=MOCK_SCENARIO=`:
  `fresh` (nothing done) · `onboarding_mid` · `kyc_pending` · `onboarded_empty`
  · `busy_chat` (populated list, unread) · `incoming_call` · `error_states`.
- **State pre-seeding.** Scenarios write tokens/user/Hive directly so Maestro
  can deep-link to `/home` or `/settings` without replaying onboarding — the
  single biggest speed win for screenshot runs (the splash screen already
  branches on a stored token, so this works with no code change).
- **Stable selectors.** Add `Key`/semantics labels to the widgets Maestro must
  tap. Currently absent; Maestro would rely on visible text, which is brittle.
- **Disable animations** and the 1.4s splash delay under mocks.

Suggested layout: `maestro/` with `flows/` (one YAML per journey),
`screenshots/` and a `runner.sh` that builds once and loops scenarios.

---

## 7. Suggested phasing

| Phase | Scope | Value |
|---|---|---|
| **0** | Extract `bootstrap()` + `main_mock.dart`; test-harness fakes (§5c); `MockConfig` | Unblocks all testing |
| **1** | Mock HTTP adapter + auth/onboarding/KYC routes + scenarios `fresh`/`onboarded` | **App runs end-to-end with no backend** — the main goal |
| **2** | Contacts + conversations + message history routes; `busy_chat` | Chat UI fully developable |
| **3** | `FakeSocketClient` seam + mock peer with real Signal crypto (§3) | Live message send/receive, E2EE exercised |
| **4** | `CallTransport` seam + call signalling scenarios (§5a) | Call UI developable |
| **5** | Maestro flows, stable keys, screenshot runner | Automated screenshots |
| **6** | *Later:* local LiveKit via `LiveKitTransport` (§5a) | Real call media testing |
| **7** | *Optional:* device-capability seams (§5b), contract tests | Completeness |

Phases 0–2 deliver most of the benefit; 3 is where it becomes genuinely
valuable for the hardest code in the app.

---

## 8. Production-code changes this requires

Deliberately kept minimal and listed up front — everything else is additive:

1. **Extract `bootstrap()`** from `main.dart` into `lib/bootstrap.dart`; `main.dart`
   becomes one line and `lib/main_mock.dart` is added (§2). Pure move.
2. **`socketInstance` gains an interface.** Introduce `SocketClient` with
   `RealSocketClient` (wrapping `io.Socket`) and `FakeSocketClient`. ~10 call
   sites across 3 files. *Unavoidable* — `io.Socket` is a concrete class.
3. **`CallProvider` gains a `CallTransport` seam** (§5a) — `LiveKitTransport`
   keeps today's code verbatim; `NoopTransport` is the mock. Chosen so local
   LiveKit can be dropped in later without unpicking a mock `if`.
4. **Device-capability seams** (§5b) — only if phase 6 is taken.
5. **Widget keys** for Maestro (§6) — additive, no behaviour change.

Items 1–4 are refactors worth doing on their own merit: they remove the last
untestable globals in the codebase and follow the same
promote-to-an-interface pattern the feature-first migration already used for
`addSocketConnectedListener`.

---

## 9. Decisions taken

1. **LiveKit — signalling-only for now**, with a `CallTransport` seam so a local
   LiveKit server can be added later without rework (§5a).
2. **Separate `main_mock.dart` entrypoint**, with `bootstrap()` extracted so the
   two entrypoints are one line each and the provider list has a single home
   (§2). Mock code is then never reachable from a release build.
3. **Obviously-fake fixture data** — reserved phone ranges, `@example.com`,
   patterned BVNs, a fixed fictional cast, and a `MOCK DATA` banner (§6).

## 10. Still open

**Is there an API spec (OpenAPI / Postman collection) to derive fixtures from?**

This is the one unanswered question and the biggest long-term risk. Without a
spec, every fixture encodes the response shape *as the current client code
guesses it* — inferred from `fromJson` methods, not from an authoritative
contract. Two consequences:

- If a guess is already wrong, the mock will faithfully reproduce the wrong
  shape and the bug stays hidden until integration.
- When the backend changes, nothing detects the drift; the mock keeps passing.

Mitigations, in order of preference:

1. Get the spec and generate fixtures from it. Best outcome by far.
2. Capture real responses once (proxy/charles/`dio` logging against staging) and
   freeze them as fixtures — evidence rather than inference.
3. Failing both: proceed on inferred shapes, but add a periodic contract test
   that replays fixtures against staging and diffs, so drift surfaces loudly.

Recommend deciding this before phase 1, since it determines where fixtures come
from rather than how they are wired in.
