# BEEVIA

## Product Requirements Document

**MVP Scope — Secure Messaging & Multi-Currency Financial Platform**

| Attribute | Detail |
| --- | --- |
| Document | Beevia Product Requirements Document (PRD) |
| Scope | MVP only. |
| Supported currencies | NGN, USD, GBP, EUR |
| Audience | Founders, product, design, engineering leadership, investors, new hires |
| Infrastructure note | This document describes capabilities, not vendors. Specific financial and identity verification infrastructure partners are named only in the companion Technical & Compliance Architecture Specification. |

---

## 1. Product Overview

### 1.1 Introduction

Beevia is a secure communication platform that integrates encrypted messaging, real-time calling, and translation with licensed financial services. Users can message, call, and translate conversations with anyone, and can optionally hold and move money across multiple currencies inside the same conversation.

Financial services, wallets, transfers, and virtual cards are provided through licensed third-party financial infrastructure partners. Beevia does not hold user funds directly and is not itself a bank or financial institution. Identity verification is performed by independent, licensed identity verification providers.

### 1.2 Key Modules (MVP)

**Secure Messaging & Calling**

- End-to-end encrypted one-on-one chat for all users
- End-to-end encrypted audio and video calling
- Real-time, opt-in message translation, preserving end-to-end encryption

**Multi-Currency Wallets & Payments**

- Supported currencies at MVP: Nigerian Naira (NGN), US Dollar (USD), British Pound (GBP), and Euro (EUR)
- Users may hold wallets in multiple currencies simultaneously
- Send money to a conversation partner from any wallet the sender holds
- Funds convert automatically and settle into the recipient's corresponding currency wallet
- Request money from a conversation partner in a specified amount and currency
- Virtual card issuance for verified users, linked to a wallet

**Identity Verification**

- Two independent verification tiers: a local-market tier and an international tier, each unlocking the wallets relevant to that tier
- Verification is performed by independent, licensed identity verification providers, never built or stored by Beevia

### 1.3 Target Users

| User Type | What They Get |
| --- | --- |
| Individual adults (18+) | Messaging, calling, translation, multi-currency wallets, transfers, virtual cards |

MVP scope is limited to individual adult users. Business accounts and any form of dependent or guardian-managed account are explicitly out of scope for this document.

### 1.4 Supported Currencies & Markets

Beevia supports four currencies at MVP launch:

| Currency | Code | Primary Market | Verification Tier Required |
| --- | --- | --- | --- |
| Nigerian Naira | NGN | Nigeria | Local Tier |
| US Dollar | USD | United States and international users generally | International Tier |
| British Pound | GBP | United Kingdom | International Tier |
| Euro | EUR | Eurozone markets | International Tier |

NGN is treated as the local-market currency, tied to the Local Tier of identity verification described in the companion Technical & Compliance Architecture Specification. USD, GBP, and EUR are each tied to the International Tier. A user may hold any combination of these four wallets, subject to completing the relevant verification tier for each. See the companion document for the full verification tier model and the rules governing mandatory wallets by user location.

### 1.5 Why Beevia?

Most people use separate apps to talk and to move money. This creates friction: confirming a payment means leaving the conversation, switching apps, and returning to explain what happened. Beevia removes that friction by keeping conversation and payment in the same place, without taking on the risk or regulatory burden of becoming a bank.

Users get privacy-first communication and access to regulated financial services, with absolute clarity about which part of the experience is Beevia and which part is delivered by a licensed financial partner.

> **Assumptions and flags:** Beevia assumes licensed partner integrations for all financial services and is not itself licensed. Chat is genuinely end-to-end encrypted, which limits any form of message moderation. The product interface must always distinguish "Beevia as the interface" from "the licensed partner as the financial provider" — failing to do this risks misleading users and risks regulatory action.

---

## 2. Product Vision

### 2.1 Vision Statement

Beevia envisions a world where secure communication and financial access are no longer separated into different apps. Anyone should be able to message, call, and translate conversations securely, and handle financial tasks safely, without switching between tools or worrying about privacy.

We believe users should:

- Be in control of their privacy
- Know exactly where their money is and who is holding it
- Trust the tools they use every day

Beevia is not trying to become a bank. Beevia is the interface that helps people communicate and manage their financial lives, using trusted, licensed partners behind the scenes.

### 2.2 What Beevia Will Not Be

- Beevia is not a bank
- Beevia is not a content policing platform
- Beevia is not a cryptocurrency wallet or exchange

Beevia enables people to message and call securely, and to interact with money safely. The financial side always runs through licensed providers, never through Beevia's own systems.

---

## 3. Problem Statement

### 3.1 The Core Problem

Most people use separate tools for communicating and for managing money. This creates friction, confusion, and security risk. A user sends money in one app, confirms it happened in another, and explains the purpose of the payment in a third. There is no unified, secure place to message and move money while staying fully in control.

Existing options fall short:

- Messaging apps don't offer financial tools
- Banking apps are rigid, complex, and lack real-time communication
- Multi-currency money movement across borders is slow, expensive, or confusing

### 3.2 The Gaps Beevia Is Solving

**No integrated chat and finance**
Users jump between apps to send money and confirm it via chat. This slows things down and adds risk of error.

**Inconsistent user control across platforms**
Users want to set limits, get alerts, and control who they transact with. Most apps treat these as afterthoughts.

**Poor cross-border and cross-currency support**
Sending money across currencies is still slow, expensive, or confusing. Users want messaging and cross-currency payments in a single flow.

### 3.3 Impact of These Gaps

- Increased risk of fraud and payment mistakes
- Miscommunication around payments and their purpose
- High switching costs between communication and finance tools
- Growing user demand for transparency and simplicity

### 3.4 Beevia's Answer

We combine secure, encrypted messaging and calling with access to licensed financial services through trusted partners. Users can message, call, send or receive money across currencies, and manage controls in one app. Messaging and calling are universal. Financial features are partner-powered and permissioned by verification tier.

---

## 4. Our Solution

### 4.1 What Beevia Solves

Beevia gives users one app for secure communication and access to financial services, without holding user funds directly. Communication is built and secured by Beevia. Financial services are delivered through licensed partners. This creates a smooth user experience while keeping Beevia's regulatory exposure low.

### 4.2 Core Modules

**Secure Messaging & Calling for All Users**

- One-on-one chat with end-to-end encryption
- End-to-end encrypted audio and video calling
- Real-time, opt-in translation that preserves end-to-end encryption — translation happens on-device, after decryption, so the underlying communication infrastructure never has access to plaintext message content

**Multi-Currency Wallets & Payments via Licensed Partners**

- Licensed partners manage wallet accounts, balances, and money movement
- Users complete identity verification through partner-powered, embedded flows
- Beevia displays balances and transaction history using secure API access, never caching sensitive financial data unnecessarily
- Users may hold more than one currency wallet at a time

### 4.3 How This Works in Practice

- Messaging, calling, and translation are built and secured by Beevia
- Financial transactions are executed through regulated, licensed partners
- Controls and disclosures are layered into the interface so users always know which part of their experience is Beevia and which part is the licensed financial partner

Users get one platform to talk, call, and transact with clarity, without needing to trust Beevia as a bank.

---

## 5. Value Proposition

### 5.1 Why Beevia Exists

People want fewer apps, more control, and better security. Right now, they switch between apps to send money, talk about it, and track what happened. Beevia combines secure communication with access to financial services inside one interface, without taking on the risk of becoming a bank.

### 5.2 What Makes Beevia Different

**Communication Comes First**
Everyone can chat and call. Communication is encrypted, private, and available to every user. This creates context before, during, and after every transaction.

**Beevia Never Touches User Funds**
All financial services: wallets, payments, cards, and compliance are handled by licensed partners. Beevia acts as a secure front-end that connects users to these services while managing the user experience.

**Multi-Currency by Design**
Users can hold, send, receive, and request money across multiple currencies without leaving a conversation. Conversion happens automatically and transparently, with the exchange rate always confirmed before any money moves.

**One App That Respects Regulation**
Beevia does not try to own the financial stack. We let licensed providers handle custody, identity verification, and risk, while we focus on trust, clarity, and ease of use.

### 5.3 Bottom Line

Beevia gives users the ability to talk, call, and transact in one place, across currencies, without compromising security, compliance, or user control.

---

## 6. Goals and Objectives

Beevia is built around five goal areas: adoption, reliability, satisfaction, compliance, and financial operations. Each goal below reflects current MVP scope.

### 6.1 User Growth

- **Goal:** Reach 5,000 registered users in the first 12 months
- **How:** Targeted launch campaigns, partner-based trust, and referral incentives
- **Metric:** Monthly growth in new registrations and verified financial accounts

### 6.2 Product Reliability

- **Goal:** Keep app uptime above 99.9 percent and transaction latency under 2 seconds
- **How:** Scalable cloud architecture, message queuing, and continuous API monitoring
- **Metric:** Real-time uptime dashboards and transaction response logs

### 6.3 User Satisfaction

- **Goal:** Maintain at least a 4.5-star rating on app stores
- **How:** Prioritise clear onboarding, useful controls, and fast customer support
- **Metric:** Weekly review tracking and feedback loop integration

### 6.4 Legal and Security Compliance

- **Goal:** Stay fully compliant with data protection and financial regulations in all live markets
- **How:** Build on top of licensed partners and pass regular independent security audits
- **Metric:** Clean audit results, zero regulatory violations, up-to-date legal disclosures

### 6.5 Financial Operations

- **Goal:** Process at least 100,000 successful transactions in year one
- **How:** Launch with trusted partners, promote peer-to-peer and request-based payment use cases, and ensure low failure rates
- **Metric:** Monthly transaction volume and success/failure breakdowns

---

## 7. Key Performance Indicators

### 7.1 Product Adoption

| Metric | Goal |
| --- | --- |
| Monthly Active Users (MAU) | At least 10,000 MAU by Month 6 |
| New Verified Wallets | 3,000+ wallet activations within the first 3 months, counted only after successful verification |

### 7.2 Engagement

| Metric | Goal |
| --- | --- |
| Messages Sent per User per Week | Minimum of 15 messages per user per week |
| Median Time from First Chat to First Transaction | Under 5 days |
| Feature Retention | 50 percent of users who send one transaction do so again within 14 days |
| Call Adoption | At least 20 percent of active users complete one audio or video call per month |
| Translation Usage | At least 10 percent of active conversations have translation enabled |

### 7.3 System Reliability

| Metric | Goal |
| --- | --- |
| API Success Rate | 99.5 percent success on all partner API calls, including wallets, transactions, and identity verification |
| Message Delivery Latency | 90 percent of messages delivered in under 1.5 seconds |
| Call Connection Success Rate | 98 percent of initiated calls successfully connect |
| App Crash Rate | Fewer than 1 crash per 1,000 sessions |

### 7.4 Compliance and Trust

| Metric | Goal |
| --- | --- |
| User-Triggered Data Deletion Requests | 100 percent completed within 5 days |
| Financial Partner Escalations | Fewer than 0.5 percent of users escalated to partner support due to integration issues |
| Dispute Resolution Time | 90 percent of issues resolved within 72 hours |
| Unresolved Payment Requests | Fewer than 5 percent of requests expire without a response |

---

## 8. Core User Stories

Each story reflects what the user wants to do, not what we want to build. These stories validate scope, sequence, and edge cases for design and engineering.

### 8.1 Messaging & Calling

**As a user, I want to send secure messages so that my conversations stay private.**

- One-on-one chat
- End-to-end encryption on every conversation
- Push notifications for new messages
- Message reactions and file attachments
- Visible indicator that a conversation is encrypted

**As a user, I want to call the person I am chatting with so that I can speak directly when text isn't enough.**

- Audio and video calling directly from a conversation
- End-to-end encrypted call sessions
- Missed call and call history shown in the conversation

**As a user, I want messages translated automatically so that I can talk to people who speak a different language.**

- Opt-in translation, set per conversation or globally
- Translation never breaks end-to-end encryption
- Original message always available alongside the translation

### 8.2 Multi-Currency Wallets

**As a user, I want to hold money in more than one currency so that I can manage funds the way I actually use them.**

- Add additional currency wallets after initial verification
- View balance and transaction history per wallet
- Each wallet clearly labelled by currency

**As a user, I want to send money to someone I'm chatting with, from whichever of my wallets I choose.**

- Select source wallet at the moment of sending
- See the converted amount and exchange rate before confirming
- Funds settle into the recipient's corresponding currency wallet
- Confirm with PIN or biometric authentication

**As a user, I want to request money from someone I'm chatting with, in a specific amount and currency.**

- Specify the amount and currency I want to receive
- See the request reflected clearly in the conversation, distinct from a regular message
- See a live, non-binding preview of what it may cost the other person to pay, in their currency
- Request automatically expires if not paid within the response window

**As a user, I want to confirm I want incoming money before it lands in my wallet.**

- Every incoming transfer requires my acceptance before funds settle, with one exception below
- If I requested an exact amount and that exact amount arrives, it settles automatically with no extra step
- If the amount differs from what I requested, I must actively accept or decline
- A visible countdown shows how long I have to respond before funds return to the sender

**As a user, I want a virtual card linked to my wallet so that I can spend online.**

- Card available once minimum verification tier is met
- Card number masked by default, revealed only after authentication
- Freeze and unfreeze the card at any time

### 8.3 Security & Account Control

**As a user, I want to protect my account from unauthorized access.**

- Biometric login
- Session expiration and re-authentication
- Authentication required for any financial action, regardless of session state

**As a user, I want to know when a financial service is unavailable so I don't get confused or blocked.**

- Display a clear status banner with the reason
- Offer retry or fallback options
- Never tell the user to contact the partner directly, Beevia handles escalation

---

## 9. Core User Flows

### Flow 1 — Messaging

**Flow:** Open conversation → send a message → receive a message → manage thread
**Who:** All verified users
**Partner involvement:** None — fully internal to Beevia

**Steps**

- Open chat tab
- Tap "New Chat"
- Select a contact
- Write and send message
- See sent / delivered / read status and encryption indicator
- React, forward, or delete message
- Mute or report conversation

**Edge cases**

- Blocked user → thread hidden, messaging disabled

### Flow 2 — Audio & Video Calling

**Flow:** Open conversation → initiate call → recipient accepts or declines → call session → end call
**Who:** All verified users
**Partner involvement:** Yes, a real-time communications infrastructure provider powers the encrypted call session

**Steps**

- Tap call icon inside a conversation
- Choose audio or video
- Recipient receives a call notification and accepts or declines
- Call session begins, end-to-end encrypted
- Either party ends the call
- Call duration and outcome logged in the conversation

**Edge cases**

- Recipient does not answer → missed call logged, notification sent
- Call drops mid-session → automatic reconnect attempt, graceful failure message if unsuccessful

### Flow 3 — Real-Time Translation

**Flow:** Enable translation → message received in another language → translated text displayed → original available on demand
**Who:** Any user who opts in, per conversation or globally
**Partner involvement:** Yes — a translation service provider, accessed via a secure proxy so the provider never has standing access to raw conversations

**Steps**

- User enables translation in settings or for a specific conversation
- Incoming message is decrypted on-device
- Decrypted text is sent to the translation provider for conversion only
- Translated text is displayed, with the original accessible on tap

**Edge cases**

- Translation service unavailable → original message still shown, with a clear notice

### Flow 4 — View Wallet

**Flow:** Open wallet → select currency → view balance → browse transactions
**Who:** Verified users
**Partner involvement:** Yes, licensed banking infrastructure partners hold and report on wallet balances

**Steps**

- Tap Wallet
- Select which currency wallet to view — NGN, USD, GBP, or EUR — if more than one exists
- Fetch balance and transaction history via secure partner API
- Show partner attribution badge
- Tap any transaction to see full detail

**Edge cases**

- Unverified user → prompted to complete identity verification
- Partner API unavailable → fallback message shown, never a blank or broken screen

### Flow 5 — Send Money (Multi-Currency)

**Flow:** Open chat or wallet → tap Send → choose source wallet → enter amount → confirm → recipient accepts
**Who:** Verified users
**Partner involvement:** Yes, full custody, transfer execution, and transaction logging

**Steps**

- Open Send Money from chat or wallet
- Choose which of the sender's own wallets to send from
- Enter amount; see live exchange rate and fee if the recipient's wallet is in a different currency (for example, sending from a USD wallet to a recipient whose default wallet is NGN)
- Confirm with PIN or biometric — exchange rate locks at this moment
- Funds are reserved on the sender's ledger, pending recipient acceptance
- Recipient sees an incoming payment card in the conversation and accepts or declines
- On accept, funds settle into the recipient's corresponding currency wallet
- On decline, or if the recipient does not respond within 24 hours, funds return to the sender automatically

**Edge cases**

- Insufficient funds → blocked with clear message before confirmation
- Transaction above threshold → additional authentication required
- Partner API error → retry option, with reference number for support

### Flow 6 — Request Money (Multi-Currency)

**Flow:** Open chat → tap Request → enter amount and desired currency → request sent → recipient pays or declines
**Who:** Verified users
**Partner involvement:** Yes — same transfer execution infrastructure as a direct send

**Steps**

- Tap "Request" inside a conversation
- Enter the amount and select the currency to be received — for example, requesting 50 USD even if the payer's available wallets are in NGN or GBP — not tied to a specific wallet selection upfront
- Request appears in the conversation as a distinct card, visible to both parties, with a visible countdown
- Recipient taps to respond, selects which of their own wallets to pay from, and sees a live converted amount
- Recipient confirms with PIN or biometric — exchange rate locks at this moment
- Funds are reserved on the recipient-turned-payer's ledger
- If the amount paid exactly matches the original request, funds settle immediately into the requester's wallet with no further step
- If the amount paid differs from the original request in any way, the requester must actively accept or decline before funds settle
- If unpaid or unresolved within 24 hours, the request expires and no funds move

**Edge cases**

- Requester cancels before payment → request closes, nothing has moved
- Recipient pays a different amount than requested → requester sees both figures clearly and must accept or decline

### Flow 7 — Virtual Card

**Flow:** Meet minimum verification tier → request card → card issued → reveal, freeze, or view transactions
**Who:** Verified users meeting the minimum required verification tier
**Partner involvement:** Yes — card issuance and card network access are provided by a licensed card issuing partner

**Steps**

- User requests a virtual card linked to a specific wallet
- Card is issued by the partner and displayed masked by default
- Card details revealed only after biometric or PIN confirmation, then automatically re-masked
- User can freeze, unfreeze, and view card transaction history

**Edge cases**

- Card issuance unavailable → clear status message, retry option

### Flow 8 — User Deletes Account

**Flow:** Open settings → request deletion → confirm → data erased or flagged for partner-side deletion
**Who:** All users
**Partner involvement:** Yes, financial and identity data deletion requests are relayed to the relevant licensed partners

**Steps**

- Tap "Delete My Account"
- Confirm identity with PIN or biometric
- Review consequences, including any data retained for legal or regulatory reasons
- All locally stored messages and media deleted
- Deletion request sent to relevant partners for wallet and identity data
- Confirmation email sent once complete

**Edge cases**

- Pending transaction or request exists → deletion blocked until resolved
- Partner deletion delay → "deletion in progress" status shown, not a silent failure

---

## 10. Detailed Feature Requirements

### 10.1 Messaging & Calling

**Feature: End-to-End Encrypted Messaging**

- **Users:** All
- **Function:** Send and receive one-on-one messages with end-to-end encryption
- **Notes:** Encryption indicator must always be visible. The communications infrastructure never has access to plaintext message content.

**Feature: End-to-End Encrypted Audio & Video Calling**

- **Users:** All
- **Function:** Real-time audio and video calls between two users, initiated from within a conversation
- **Notes:** Calls must be end-to-end encrypted to the same standard as messaging. Call history (duration, outcome) is logged in the conversation thread.

**Feature: Real-Time Translation**

- **Users:** All, opt-in per conversation or globally
- **Function:** Automatically translate incoming messages into the recipient's preferred language
- **Notes:** Translation occurs after on-device decryption. The translation provider receives only the text needed for conversion, never standing access to the conversation. Original text always remains accessible.

**Feature: File Sharing**

- **Users:** All
- **Function:** Send images, audio, and documents within a conversation
- **Notes:** Files are uploaded to encrypted storage with time-limited access tokens.

### 10.2 Multi-Currency Wallets

**Feature: Multi-Currency Wallet View**

- **Users:** Verified users
- **Function:** Show balance and recent transactions per currency wallet, across all four supported currencies (NGN, USD, GBP, EUR)
- **Partner:** A licensed banking infrastructure partner
- **Notes:** Wallet screen must clearly show partner attribution. Balance refreshes on pull-to-refresh; financial data is never cached longer than necessary.

**Feature: Add Additional Currency Wallet**

- **Users:** Verified users
- **Function:** Add a new currency wallet after initial verification
- **Notes:** Additional wallets may require meeting the relevant verification tier for that currency, if not already met.

**Feature: Send Money (Multi-Currency)**

- **Users:** Verified users
- **Function:** Send money from any wallet the sender holds, to a conversation partner, with automatic conversion into the recipient's corresponding wallet
- **Partner:** Provider executes the transfer, performs fraud checks, and applies limits
- **Notes:** Exchange rate locks at the sender's moment of confirmation. Funds are reserved, not settled, until the recipient accepts. Transfer result is shown inside the originating chat thread.

**Feature: Request Money (Multi-Currency)**

- **Users:** Verified users
- **Function:** Request a specific amount in a specific currency from a conversation partner
- **Notes:** The payer selects their own source wallet at the moment of payment; the exchange rate locks at the payer's confirmation, not at the moment the request was created. Exact-match payments settle automatically; any mismatch requires the requester's acceptance. Requests expire after 24 hours if unresolved.

**Feature: Transfer Acceptance & Escrow**

- **Users:** Verified users, on both sending and receiving ends
- **Function:** Hold funds in a reserved state on the payer's ledger until the receiving party actively accepts
- **Notes:** This applies uniformly to direct sends and to payments made in response to a request, with the single exact-match exception described above. A visible, human-readable countdown is always shown in the conversation, with escalating visual urgency in the final hour of the 24-hour window.

### 10.3 Virtual Cards

**Feature: Virtual Card Issuance**

- **Users:** Verified users meeting the minimum required verification tier
- **Function:** Generate a virtual debit card linked to a specific wallet, for online use
- **Partner:** A licensed card issuing partner; no full card data is ever stored by Beevia
- **Notes:** Card number, CVV, and expiry shown masked by default. Revealing full details requires biometric or PIN confirmation and automatically re-masks after a short, fixed display window. Card service must show the issuer's legal name and a compliance disclosure in-app. If the provider is unavailable, show a clear status message and retry option.

### 10.4 Privacy, Security & Compliance

**Feature: Biometric Login**

- **Users:** All
- **Function:** Authenticate using device-native face or fingerprint recognition
- **Notes:** Native device APIs only. Biometric data is never stored by Beevia.

**Feature: Delete My Account**

- **Users:** All
- **Function:** Wipe user data and request deletion from all relevant partners
- **Notes:** Clear confirmation with a deletion-in-progress state if any delay occurs.

**Feature: Consent Management**

- **Users:** All
- **Function:** Allow users to revoke consent for location, biometrics, and translation independently
- **Notes:** If a user revokes a consent required for a financial feature, that feature is disabled until consent is restored.

---

## 11. Product Roadmap

**Timeline:** 0–6 months to public launch.
**Model:** Communication and core wallet capability ship together as a single coherent MVP, since calling and translation are core to the MVP rather than later additions.

### Phase 1 — Foundation: Messaging, Calling & Translation

**Timeline:** Month 0 to 2
**Goal:** Launch core encrypted messaging, calling, and translation for all users

**Features**

- End-to-end encrypted one-on-one chat and calling
- Real-time translation
- User onboarding with phone verification
- Push notifications, file sharing
- Block / report controls

**Success metric**
500 weekly active users with a daily return rate over 20 percent

### Phase 2 — Identity Verification & Wallet View

**Timeline:** Month 2 to 3
**Goal:** Enable identity verification and read-only multi-currency wallet view

**Features**

- Local and international verification tiers
- Wallet balance and transaction history view, across all four MVP currencies: NGN, USD, GBP, and EUR
- Clear partner attribution throughout

**Success metric**
At least 1,000 users complete verification and view a wallet balance successfully

### Phase 3 — Send, Receive & Request Money

**Timeline:** Month 3 to 5
**Goal:** Enable multi-currency money movement between verified users

**Features**

- Send money from any held wallet, with automatic currency conversion
- Request money in a specified amount and currency
- Universal transfer acceptance and escrow mechanic
- Biometric or PIN confirmation on every financial action

**Success metric**
At least 2,000 successful transactions with a repeat rate over 40 percent

### Phase 4 — Virtual Cards & Compliance Hardening

**Timeline:** Month 5 to 6
**Goal:** Launch virtual cards and complete pre-launch compliance hardening

**Features**

- Virtual card issuance for verified users
- Consent logging, audit trails, and retention policies
- Independent security audit and penetration test
- Public launch readiness review

**Success metric**
Clean external compliance review with zero escalated support cases from partner-side issues

---

## 12. Launch Plan

### 12.1 Pre-Launch

- Finish Phase 1 through Phase 4 feature set
- Run internal alpha with full messaging, calling, and translation
- Finalise financial infrastructure and identity verification partner agreements
- Conduct internal security and compliance review

### 12.2 Alpha Launch

- **Audience:** Internal team, advisors, early design partners
- **Features:** Messaging, calling, translation, view-only wallet
- **Target outcome:** 100 users with 70 percent retention after 7 days

### 12.3 Beta Launch

- **Audience:** Invite-only waitlist
- **Features:** Live wallet view, identity verification, working multi-currency transfers
- **Target outcome:** 500 users, 250 active wallets, 100 completed transactions

### 12.4 Public Launch

- **Audience:** General public in initial launch markets
- **Features:** All MVP features live: messaging, calling, translation, multi-currency wallets, send, receive, request, virtual cards

**Compliance actions**

- Submit to all relevant app store data safety and privacy review requirements
- Make partner licenses visible and link to official regulatory registries

### 12.5 Post-Launch

- Drive adoption through trust-building content
- Launch referral program
- Monitor fraud, dispute, and chargeback behaviour closely

**Success benchmark**
1,000 verified wallets, 5,000 active users, and no compliance flags within 60 days of public launch
