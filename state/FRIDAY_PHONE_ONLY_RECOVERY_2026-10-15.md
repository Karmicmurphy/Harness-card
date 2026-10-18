# FRIDAY phone-only continuation — operational recovery checkpoint

**Observed / owner-reported:** 2026-10-15 local (2026-10-16 UTC).  
**Lane:** Recover verified state -> protect working artifacts -> resume one bounded phone path.  
**Owner interaction profile:** `config/owner_access_profile.json` (`PHONE_ONLY`, Android; no reliable PC access). This document intentionally excludes housing details and all private information.

## Current four-day continuation (load first on resume)

**Latest sanitized October 15–18 operational handoff:** [FRIDAY_RECENT_CONTINUITY_2026-10-18.md](FRIDAY_RECENT_CONTINUITY_2026-10-18.md). This carries the recent COILSIDE repair, FRIDAY Night Shift, provider-release gate, and verified Cloudflare/branch drift from the resumed work. **Read it for context, then establish fresh GitHub/Cloudflare truth; it cannot supersede `state/CURRENT_PROJECT.json`.** Private chats and actual time entries are not copied into public Harness.

## Outcome

The owner can keep working with FRIDAY, Harness and machine repositories from an **Android phone**, using ordinary language and Chat's connected GitHub/Cloudflare tools, without a Windows shell, local PC, pasting secrets, paid service or a new identity framework.

The machine should do the routine repository/provider work itself. If owner intervention is genuinely unavoidable, give **one exact tap** grounded in the actual phone screen; preserve the next step so the owner never needs to reconstruct the system.

This operating mode **does not** make a PC-only process/cloud service remotely runnable and does not claim private local files are in GitHub.

## Fresh inspection — verified current during this pass

| Component | Observed state / evidence | Safe conclusion |
|---|---|---|
| Harness authority | `Karmicmurphy/Harness-card` main; active gate `PAGES_BOUNDED_JOB_ROUND_TRIP` | No authority-promotion request; do not restart the completed READ path |
| Workshop cockpit | `Karmicmurphy/Ollie_Twis_Holo_workshop` has `living-workshop-main-build` observed `9822e988dd125f55b13be3891eb0a39975a26191` vs pinned `1785ed1405e769a17ec22066dc1e27a40dbf153b` | Reconciliation required, **not** permission to repin |
| Foundry | `Karmicmurphy/temporal-capability-foundry` branch `software-builder-v0` observed `319c4945c6b9bb180385cdf0935633e2f1915d61` vs pinned `e0e14e689b1d3a3bda1356276975b4b34f1b615e` | Divergence in branch ref; preserve gate/pin and inspect receipts before any promotion |
| AIOS | `Karmicmurphy/Untethered-AIOS` main observed `8a954439af2b15b00f7c961d83552772b382fd1f` | Matches pinned runtime |
| Digital Scrapyard | `Karmicmurphy/digital-scrapyard-autopilot` main observed `a904f29213b5a5bcf1b39f1392bca740c46a6093` vs pinned `a059a27ef2bd662827a51da44dd8efb8863d634c` | Observe only; not active machine improvement |
| Existing Pages | Cloudflare Pages project `ollie-twis-holo-workshop`; production branch `living-workshop-main-build`; approved Preview fixture deployment `48d4cbf1-3e74-4c99-a26b-af97cc986f14` still exists | Preview code deployed; no owner-path proof |
| Preview environment keys | Cloudflare API lists `FOUNDATION_ACCESS_AUD`, `FOUNDATION_ACCESS_DOMAIN`, `FOUNDATION_DISPATCH_SHA`, `FOUNDATION_PHONE_ENABLED`, `FOUNDATION_SOURCE_SHA`, `TWIS_ALLOW_AI`, `TWIS_ALLOW_REMOTE_WRITE`, `TWIS_REMOTE_HULL_MODE`. **Missing:** `FOUNDATION_GITHUB_TOKEN`, `FOUNDATION_OWNER_SUB`. These names are present in Production only | The live bounded phone-job path is still blocked by Preview's missing secrets and lack of fresh runtime/owner proof; never copy Production values automatically |
| Other previews | More recent `codex/local-machine-startup` Preview exists (Oct 3). | Not an authorized replacement for the exact reviewed fixture |
| Separate COILSIDE win | See `state/COILSIDE_FIELD_WIN_HANDOFF_2026-10-15.md`: app and Cloudflare D1/binding proven; Sean two-device note round trip not yet verified | Useful proof FRIDAY can learn, **not** a substitute for Foundation live proof |

Provider observations above are snapshots; read current provider again before any mutation. No private API tokens, actual secret values, identity subject, chats, personal files or sensitive personal circumstances are included.

## Do not make the owner conduct this workflow

When user says “FRIDAY, do this from my phone,” run the existing Chat Software Harness:

1. Recover `AGENTS.md`, `OPERATING_CONTRACT.md`, `ROUTING.md`, `state/CURRENT_PROJECT.json` and the relevant receipt. Query GitHub/provider current state rather than assuming it matches this file.
2. Clarify the **one desired result** without asking for a work history or PC access that is unavailable; use verified source first.
3. Run bounded, reversible inspection/build/tests via available connectors and CI. Use small PRs with receipts. Do not create another agent or front door.
4. If a required provider permission is absent, do not send owner on a dashboard scavenger hunt. Prefer one owner-approved native provider action when supported; verify via a separate independent read. No permission escalation.
5. If a step truly needs a secret or the exact verified owner subject, do not invent or pull from Production; stop at a precise owner gate and keep all existing work intact. Phone-only constraint is **not permission to weaken authentication**.
6. Give one link/action at a time when human taps are necessary; do not assume keyboard/mouse, browser devtools or desktop terminal.
7. Leave a current repo/CI/provider proof receipt with source SHA, deployment ID when known, remaining one gate, and clear DONE/BLOCKED state.
8. Do not treat an issue/Markdown file as proof that a running FRIDAY instance autonomously loaded it. This file is available for authorized agent retrieval.

## Smallest next executable proof (Foundation, distinct from COILSIDE)

**PAGES_BOUNDED_JOB_ROUND_TRIP remains the canonical active gate.** Approved exact Preview fixture has previously passed repository tests but the Preview still lacks two existing bindings, and a scripted read got a Cloudflare edge 403/1010 before reaching the Function. Do **not** trigger a live Foundry dispatch, change Production, rotate credentials or promote new refs as a workaround.

Phone-only continuation should first attempt all non-secret read-only inspection using Chat connectors, then stop at **the minimal explicit owner gate for missing Preview bindings**. Do not request/handle sensitive values in a public conversation or repo. Once a legitimate configuration path is available, re-deploy only reviewed source and obtain authenticated owner/path evidence before any separately authorized single fixture job.

## October 17 current provider check — minimum remaining owner gate

Read-only verified on 2026-10-17 (Cloudflare and GitHub, no secret values retrieved):
- Existing Pages project `ollie-twis-holo-workshop`, Preview environment, approved candidate deployment `48d4cbf1-3e74-4c99-a26b-af97cc986f14` remains successful at `256452bfc522af32260a6d78591acecf56379d52`; this does **not** verify live Function authentication or phone dispatch.
- Preview `FOUNDATION_DISPATCH_SHA=3787d3a468abea49d194a051364ce41f300f35d0` **matches** the actual `Karmicmurphy/temporal-capability-foundry` `main` head. `FOUNDATION_SOURCE_SHA=5b23c55e6c0c7d945adf15af882ed59244399f35`; `FOUNDATION_PHONE_ENABLED=true`. Preserve these pins.
- Preview **still lacks** the encrypted `FOUNDATION_GITHUB_TOKEN` and `FOUNDATION_OWNER_SUB`. Production has both names, but encrypted values cannot be read back, inferred from masked data, or safely copied by an API client. No account permissions, application authentication, production settings, or passwords were changed.
- FRIDAY Provider Release skill and fail-closed checker are now merged into Harness Card main (PR #31); this checker is not a live dispatch agent.

**One unavoidable owner-security setup, not a request to paste anything into Chat:**
1. In GitHub Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens, create a limited token for **only** `Karmicmurphy/temporal-capability-foundry`, with repository Actions **Read and write**; use an expiration and retain it securely. GitHub Actions workflow dispatch uses Actions write; artifact reads use Actions read.
2. In a browser with the owner's **actual Access sign-in**, open the protected Workshop application's `/cdn-cgi/access/get-identity` path and use the returned `user_uuid` as the signed-in Access subject (`sub`) after matching the intended account. Do not guess from account email or provider user identifiers.
3. In Cloudflare Dashboard -> Workers & Pages -> `ollie-twis-holo-workshop` -> Settings -> Variables and Secrets -> **Preview**, save encrypted `FOUNDATION_GITHUB_TOKEN` and encrypted `FOUNDATION_OWNER_SUB` using the two values above. Never publish values in GitHub, logs, Chat, plaintext env vars, or this public Harness.
4. After both values are stored, the machine must independently re-read **names only**, generate a **fresh deployment of the exact reviewed Preview source**, verify edge Access + Function runtime behavior, and only then consider an explicit scoped owner-authorized single fixture dispatch and correlated receipt. No automatic Production activation.

**Stop on unresolved credential setup.** No alternate secrets, bypass, new app/Worker or unrelated ref promotion is authorized. Do not retry deployments while missing the two secret bindings; it will not repair them.

## Proof and constraints

**Completed for this work order:** mobile constraint recovered, verified current repo branches and Pages binding presence, phone-first status machinery and sanitized recovery document prepared/tested.  
**Not completed:** live Foundation phone-to-Foundry receipt round-trip, recovery of inaccessible local-only Workshop files, or activation of an always-on personal agent.  
**Risk rules:** no spending, no account expansion, no backup destruction, no hidden copying of personal data, no fake completion, no private PC assumptions.

**STOP:** Phone-first recovery and an honest next gate are recorded. Await an actual authorized proof opportunity; do not broaden to unrelated user projects.
