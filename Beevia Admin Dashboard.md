**Beevia Admin Dashboard**

 

**Roles:**

| Role | General Access Level |
| :---- | :---- |
| Support | Search users, view standard profile info, add case notes, suspend/reactivate for account-safety requests, initiate assisted PIN reset. Cannot view KYC/verification detail or manage admin accounts. |
| Compliance | Everything Support can do, plus full KYC/verification detail (sensitive fields masked per policy), and policy-violation suspension actions. |
| Super Admin | Everything Compliance can do, plus creating/editing/deactivating admin accounts and assigning roles. |

 

## **Module Summary**

| Module |
| :---- |
| 1\. Authentication & Access Control |
| 2\. Admin Account Management |
| 3\. User Management & Support Tools |
| 4\. Trust & Safety / Content Moderation |
| 5\. Transaction & Wallet Oversight |
| 6\. Country & Feature Configuration |
| 7\. Analytics & Reporting Dashboard |
| 8\. Account Deletion Requests |

 

# **Module Detail**

**1\. Authentication & Access Control**

This is the entry point to the entire admin dashboard and the foundation every other module depends on. It establishes who is allowed into the system at all, confirms their identity with a second factor beyond just a password, and determines what they can see and do once inside based on their assigned role.

### **Key Capabilities**

●      Admin login, restricted to invited accounts only

●      Mandatory two-factor authentication (2FA) for every admin account

●      Three roles: Support, Compliance, Super Admin, each with a distinct permission set

●      Role-aware navigation: sections outside an admin's role don't render at all, not just disabled

 

**2\. Admin Account Management**

Before any Support agent or Compliance reviewer can use the dashboard, their account has to exist and be assigned the right role, this module is how that happens. It's restricted entirely to Super Admins, controlling who has privileged access to user data is a security-sensitive responsibility in its own right, separate from the day-to-day work those admins go on to do. This module also serves as the mechanism for correcting mistakes or responding to staffing changes. If someone leaves the team or changes function, their access needs to be revocable or adjustable immediately, not left active by default. Every action taken here (inviting, role changes, deactivation) should be treated as security-relevant and is a with its its own audit trail, similar to the account-level actions logged in User Management.

### **Key Capabilities**

●      Invite new admin accounts by email, with an assigned role

●      Change an existing admin's role

●      Deactivate/reactivate admin accounts, revoking access immediately

 

**3\. User Management & Support Tools**

It's where a Support agent finds a specific user's account when someone reaches out with a problem, and where Compliance reviews a user's verification status when something needs a closer look. It's built around a simple flow: search for a user, land on their full account detail, and take whatever action the situation calls for from there, adding a note, suspending the account, helping them regain access, or checking their KYC status. What each admin sees and can do on that account detail screen changes based on their role. Support sees standard profile and support-relevant information, while Compliance additionally sees verification detail that Support has no need to access.

### **Key Capabilities**

●      User search by phone number, name, username, or email

●      Full account detail view: profile, onboarding progress, wallet status, with role-based field visibility

●      Suspend/reactivate accounts, Support handles account-safety requests, Compliance/Super Admin handle policy-violation bans

●      Timestamped, attributed support case notes on a user's account, visible to all admins

●      KYC/verification status panel, visible to Compliance and Super Admin only

 

 

**4\. Trust & Safety / Content Moderation**

This module is where the admin gets to handle abuse, harassment, scams, or other behavior that violates the platform's rules. It's the direct counterpart to the Report feature already built into the consumer app's conversation screen: when a user reports someone, this is where that report actually gets reviewed and acted on.

### **Key Capabilities**

●      Queue of reported conversations awaiting review

●      Context needed to assess a report (reported messages, reporting user, reported user)

●      Actions: warn, suspend, or ban the reported user

 

**5\. Transaction & Wallet Oversight**

Once users are actually moving money through their Naira wallets, Beevia needs internal visibility into that activity, not to police every transaction, but to be able to answer basic operational and compliance questions: does this user's balance match what the banking partner's records say, does this pattern of activity look like normal usage or something that needs a closer look, and can the team investigate a specific user's transaction history if a dispute or regulatory inquiry comes in. This module is where that visibility lives. It's inherently tied to the banking partner relationship (Anchor) rather than something Beevia's backend can fully self-serve, since the wallet itself is a licensed banking product sitting behind Beevia's interface

### **Key Capabilities**

●      View user wallet balances and transaction history

●      Flag suspicious activity

●      Reconciliation against records from the banking partner (Anchor)

 

**6\. Country & Feature Configuration**

Expanding banking to a second country requires an engineering release. This module turns the banking and verification options into something an admin can actually manage: which countries have banking enabled, and by extension, which users see which onboarding paths. Beyond the country gating use case it starts with, this is a natural home for feature flags more broadly as Beevia's feature set grows, anywhere the team wants to turn something on for a subset of users (a new country, a beta feature, a gradual rollout) without shipping new code each time, this is where that control would live.

### **Key Capabilities**

●      Toggle which countries have Chat \+ Banking enabled, rather than requiring a code change to expand

●      Will be the general home for other feature flags as the product grows

 

**7\. Analytics & Reporting Dashboard**

It answers the questions that come up constantly once Beevia is live, how many people are signing up, where in onboarding they're giving up before finishing, how the split between Chat Only and Chat \+ Banking users is trending, and how actively people are actually using messaging and calling once they're in.

### **Key Capabilities**

●      Signups over time

●      Onboarding funnel drop-off (where users abandon the flow)

●      Chat Only vs. Chat \+ Banking split

●      Message and call volume

 

**8\. Account Deletion Requests**

Support may need to field questions from a user, Compliance needs to know that financial and KYC records are being retained appropriately even after a user's account is gone (since banking regulation typically requires retaining certain records regardless of what the user requests), and Super Admin needs some way to confirm deletions are actually completing correctly rather than silently failing.

### **Key Capabilities**

●  	a queue or list of pending account deletion requests

●  	visibility into what happens to a deleted user's data, messages left in other users' conversations, and any financial/KYC records retained for regulatory reasons even after deletion

●  	a way to confirm a deletion completed, for audit purposes

 

 

#  

