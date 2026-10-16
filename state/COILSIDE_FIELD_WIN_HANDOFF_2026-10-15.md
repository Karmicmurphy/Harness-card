# COILSIDE field recovery — FRIDAY/Harness handoff and earned infrastructure win

**Recorded:** 2026-10-15 local / 2026-10-16 UTC  
**Lane:** LEARN → HANDOFF / CLOSEOUT of the *infrastructure repair*; do not start new architecture  
**Owner-reported outcome:** A genuine personal win after a frustrating field-app deployment/debugging cycle. The owner explicitly asked that FRIDAY preserve the problems, corrections, fixes and meaning of their language.  
**Evidence verdict:** **Infrastructure PROVEN_CURRENT; end-to-end Android use PARTIALLY_PROVEN / two-person note delivery PENDING.** These are separate claims.

## Canonical refs and resume path

- App source: [COILSIDE main](https://github.com/Karmicmurphy/coilside), confirmed commit `c33cde503b4565bc21193fd3d9f3b06b3c40b083` (PR [#5](https://github.com/Karmicmurphy/coilside/pull/5) feature upgrade + PR [#6](https://github.com/Karmicmurphy/coilside/pull/6) verified D1/Wrangler binding).
- Public app: `https://coilside.ollie-twis.workers.dev/`. Home publicly rendered with START WORK (three pay contexts) and TEAM NOTES. Do not infer that every inner feature has been exercised merely from the home.
- Cloudflare D1: dedicated `coilside-team-2026`, bound to existing Worker `coilside` as exactly `COILSIDE_DB`; existing static `ASSETS` binding preserved.
- Cloudflare evidence, read again this handoff: D1 exists, three tables, current binding present, current deployment timestamp `2026-10-16T04:05:11Z` (Wrangler). Provider/version state can advance; re-check before new actions.
- Initial incident and failed assumptions: [Harness issue #26](https://github.com/Karmicmurphy/Harness-card/issues/26).
- FRIDAY's read-only intake: [Workshop issue #27](https://github.com/Karmicmurphy/Ollie_Twis_Holo_workshop/issues/27).
- Harness authority: `AGENTS.md`, `OPERATING_CONTRACT.md`, `ROUTING.md`, `skills/chat-software-harness/SKILL.md`; current Foundation machine authority in `state/CURRENT_PROJECT.json` is **NOT** changed by this external app win.

## Exact owner intent / locked scope

One small, actually usable, public-facing field app for **two human participants**: owner + collaborator. The app's **work/pay contexts** are three independent timesheets: Tim Johnson's work, Sean's Farmhouse, and Jesse Johnson's projects. They are not three login accounts. A two-person Team Notes view exchanges notes between owner and Sean only. The unrelated personal Sean Factor archive is NOT the shared inbox.

- **Public app shell** remains public. **Private data** is not publicly readable merely because a URL is public.
- **No mandatory email, Cloudflare Access identity, or registration** in this phase.
- Passwordless device-held high-entropy owner/Sean *capability pairing* was implemented instead; owner shares Sean's private link. This is a persistent credential, **not literally single-use**, and possession confers role access; do not publicly paste, log or commit links.
- Priority: preserve existing Android hours, data recovery and field usability. Photos may remain local; R2 storage is not the current release requirement.
- **No new Worker/app/foundation stack.** Existing Cloudflare Access scoped app Bypass/Everyone stays intact; never edit the reusable account-wide All Workers policy on this app's behalf.

## What failed / why it cost owner time

1. **Cloudflare Access 403 and shared-policy trap.** A policy named like public access actually selected an application token and was reused across the app and All Workers. The assistant repeatedly routed the owner through confusing Android dashboard views and shared controls. **Correction:** separate COILSIDE-only Bypass + Everyone policy, save policy **and** parent Access app; API inspected attachment, external browser fetched homepage. The issue was provider policy, not necessarily Worker code.
2. **Wrong human architecture.** A candidate implementation assumed mandatory per-person email/Access identities; owner corrected this firmly. **Correction:** separate *pay entities* from *users*, preserve public home, use two-person capability tokens for private room access. Do not reintroduce sign-in without explicit new decision.
3. **Provider authorization confusion.** Chat-connected Cloudflare tool could list resources but its attempted D1 creation returned 10000; later an optional index write returned 7500. **Correction:** Cloudflare's own Agent Lee (owner-authorized write operations) successfully created D1, initialized core tables and bound it. Different actors have different permissions; never infer user/account lacks permission merely because one connector is read-only. Agent Lee's actions require the owner's explicit confirmation.
4. **GitHub merge ≠ Cloudflare deployment.** Repository CI validated source but did not auto-deploy. The Worker had been deployed using Wrangler. **Correction:** verify actual provider deployment, runtime bindings, real homepage and GitHub `wrangler.jsonc`, not just green GitHub actions. PR #6 recorded the real D1 ID in source; no fake UUID.
5. **Data integrity risk.** Editing work-entry start/stop could leave hours computed from *old* times. Legacy full-state cloud sync could silently overwrite newer records. **Correction:** recompute edited hours from patched timestamps (regression tests), use owner-paired cloud state with compare-and-set update returning 409 on stale writes; preserve JSON backup and local state.
6. **Excess UI complexity.** Duplicate Work Hours voice controls and multiple competing actions made the field UX harder. **Correction:** one voice capture, first home actions START WORK and TEAM NOTES, three clear work categories.
7. **False-finish risk.** A 200 homepage, passing tests or valid D1 binding was nearly described as completed phone-to-phone messaging. **Correction:** classify separately: infrastructure verified; two-device notes/send/read, real Android save/edit/reload/share, and backup restore are not yet user-path-proven.
8. **SQL source access / assistant limitation.** Agent Lee reported external GitHub fetch/tooling unavailable, so reconstructed runtime-embedded SQL; separate provider SQLite introspection confirmed 3 app tables and notes index match repository CREATE TABLE structures. `idx_coilside_state_updated_at` from migration 0001 is absent; **nonblocking performance index**, not a reason to restart setup or claim a failure of notes.

## What was verified / what remains

| Gate | Evidence | Verdict |
|---|---|---|
| COILSIDE feature source merged | PR #5; `main` checks passed for hours/pairing tests, TypeScript, lint and Cloudflare build | **PROVEN_IN_TEST** |
| Real D1 config versioned | PR #6 merged to `main` at `c33cde5` | **VERIFIED_CURRENT** |
| Public access / correct homepage | Saved app-specific Access Bypass and external public homepage response | **PROVEN_CURRENT** |
| Dedicated D1 and `COILSIDE_DB` | Cloudflare read API returned database, 3 expected tables and production Worker binding | **PROVEN_CURRENT** |
| Real Worker deployment exists | Provider GET returned active Worker deployment with D1 binding | **PROVEN_CURRENT**, not device proof |
| Sean message arrives, reads, replies | No owner/Sean two-phone round-trip observed | **PENDING_REAL_PATH** |
| Android hours, edited totals and recovery | Static/regression tests only; no complete on-phone evidence | **PENDING_REAL_PATH** |
| Auto-deploy from GitHub | No native Cloudflare Builds trigger observed for `coilside` | **NOT CONFIGURED / DEFER** |
| Optional state index and R2 photo backup | Index missing; photo cloud storage intentionally deferred | **NONBLOCKING / DEFER** |

### Smallest real-world closeout (do not expand)

1. On the owner's **existing Android installation**, **export JSON backup** and confirm it exists; never clear browser/PWA data as a troubleshooting reflex.
2. Open live COILSIDE, start TEAM NOTES, share the private Sean invitation via a trusted channel; Sean opens it on his own phone. Exchange two notes, refresh both, recognize sender and read status; unauthenticated/unknown browser cannot read.
3. On owner's phone, enter and correct time in each of three categories, verify separate Sunday–Saturday totals, shareable timesheet image, reload/offline survival, and cloud conflict denial when appropriate.
4. Once both humans actually confirm the path, add exact evidence and advance the **app's** outcome to PROVEN_LIVE. Do not alter Foundation's independent active gate.

## Owner-language translation contract — apply, do not make owner speak machine

| Owner wording / conversational pattern | Correct operator behavior |
|---|---|
| “WTF stupid fucking simple” | **Result and ease of use**, not a low-quality/unsafe app. Minimize screens, taps, jargon and repeated questions. |
| “Get it going”, “make it work”, “merge it” | Own the bounded execution chain: current source → checks → provider runtime → binding → actual action. Never collapse different gates or call merge a deployment. |
| “Check it”, “double-check”, “fucking check it” | **Actually query** the live repo/provider and report what the result proves; do not send user back to click if a connected read can answer. |
| “Use Harness Card”, “let FRIDAY/the machine know” | Load canonical authority, preserve decisions, receipts and provenance in linked repos; **do not** claim a saved note automatically trains or gets consumed by FRIDAY's running model. |
| “Everything is public”, “no sign-in” | Public *entry* and no formal account signup. Does **not** authorize public exposure of private two-person messages or personal hours. |
| “Sean, Tim, Jesse” in work context | Sean = collaborator; Tim/Sean's farmhouse/Jesse = timesheet/work-pay **labels** unless owner explicitly promotes them into app users. |
| “I don't know”, conversational course corrections, profanity, repeated emphasis | Recover intent from context, check assumptions, explain plainly. Strong emotion signals **urgency/friction** and a request for competent action, not permission to broaden scope or skip proof/safety. |
| “One thing at a time” / screenshots | Android touch-first: **one exact button at a time**, visually grounded, next screenshot; avoid speculative maze navigation. |
| “This is a win”, excitement | Acknowledge the **verified milestone** and the human cost, preserve success as a receipt, while still naming the remaining unproven behavior. |

### Distilled reusable FRIDAY/harness rules

- **R1 — Task-to-actor routing:** When connector writes fail, identify denied operation and ask whether owner-approved provider-native AI can execute that bounded task; verify through independent read afterward. Never try unrelated resources or broaden account-wide permissions.
- **R2 — Configuration truth ladder:** Repository SHA → passing CI → provider deployment/version → exact production bindings → public/private response → target Android user action. A lower rung cannot stand in for a higher one.
- **R3 — Scope hierarchy:** User correction **narrows** current work. Work category != person != access role. “Professional” must not invent a user-management system.
- **R4 — Touch/tap budget:** Owner's Android reality and repeated dashboard errors should route to visual one-step support or bounded automated provider writes; do not make the owner repeat known details.
- **R5 — Preservation:** Work hours are valuable data. Back up before destructive changes; reject stale sync writes; don't equate a green note API with successful data recovery.
- **R6 — Real-win accounting:** Preserve this **infrastructure win**, and leave actual message exchange + phone workflows awaiting proof. Celebrate without false completion language.
- **R7 — Machine memory limits:** GitHub issue and handoff are retrievable references, **not** a runtime ingestion guarantee. FRIDAY must be routed to read them in its next authorized owner-workflow.

## Failure accounting, provenance and stop

- User-facing failure cycles: **multiple** (Android Cloudflare Access navigation and repeated instructions); exact count **UNKNOWN** rather than invented.
- Internal failures caught: earlier CI Prisma/type-check and test declaration issues were corrected before source merge; exact run count **not reconstructed**.
- This incident is a **real infrastructure win**, not a claim that the entire owner/Sean phone workflow is proven. The owner explicitly recognized the milestone and requested that the machine preserve it.
- Source of truth is live provider and repo evidence at time of inspection, not only an AI's claims, this document, or old conversations.
- **STOP:** Preserve incident + lessons and scoped FRIDAY intake. Do not change production Foundation pins, Access policies, unrelated Cloudflare resources, or machine runtime. Next task if requested: *one bounded two-device acceptance test*.
