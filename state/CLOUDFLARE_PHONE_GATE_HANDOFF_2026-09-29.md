# Cloudflare phone gate handoff — 2026-09-29

Status: **NON-AUTHORITATIVE HANDOFF**

Canonical authority remains:
- `state/CURRENT_PROJECT.json`
- `state/ACTIVE_WORK_ORDER.md`
- `OPERATING_CONTRACT.md`
- `ROUTING.md`

This file exists only so the current Cloudflare/phone integration state is not lost between sessions.

## Current owner-visible state

The Workshop Pages preview is deployed and opens successfully at the current PR #26 preview deployment.

Candidate Workshop preview commit:
`0f2f6de0a1b9712592295c50eef4f609fc482baf`

Candidate preview deployment previously observed:
`b9f3cdab.ollie-twis-holo-workshop.pages.dev`

The Cloudflare Access application for the Workshop now exists after manual dashboard setup. The owner created/saved an Allow policy and confirmed One-Time PIN is available for the Workshop application. No private owner email, tokens, Access JWTs, or other private account values are recorded in this public repository.

The Access app was observed using the Pages preview wildcard form:
`*.ollie-twis-holo-workshop.pages.dev`

Production-host coverage still needs explicit verification for:
`ollie-twis-holo-workshop.pages.dev`

## What is already proven outside Cloudflare account configuration

The bounded GitHub execution path has already been proven on candidate code:

Workshop / bounded job identity
→ Foundry
→ AIOS
→ Builder
→ Independent Proof
→ correlated receipt

A real candidate dispatch preserved the same Foundation `job_id` through the execution and proof chain. Execution passed, Independent Proof certified, activation remained false, and human review remained required.

The retry implementation was corrected after a real failure mode was found: GitHub native reruns removed prior receipt artifacts. The candidate now uses linked child attempts with the same Foundation job identity, incremented attempt number, validated parent run, and preserved prior evidence. Native reruns must not be restored for this path.

Review candidates previously established:

- Foundry runner / correlation candidate — PR #32
  - `5b23c55e6c0c7d945adf15af882ed59244399f35`
- Foundry dispatcher / duplicate + retry candidate — PR #33
  - `9e8c81f3e1ece4ca3684d9d7503c46b1c5302ecf`
- Workshop Pages phone-return candidate — PR #26
  - `0f2f6de0a1b9712592295c50eef4f609fc482baf`

These remain candidate/review references unless canonical Harness authority explicitly promotes them.

## Cloudflare account state to verify next

The Pages project is:
`ollie-twis-holo-workshop`

Known earlier production commit:
`9822e988dd125f55b13be3891eb0a39975a26191`

Known candidate preview commit:
`0f2f6de0a1b9712592295c50eef4f609fc482baf`

Pages Functions were previously observed as enabled for production and preview.

The following Foundation account configuration was previously missing and still needs current-state verification before activation:

- `FOUNDATION_ACCESS_DOMAIN`
- `FOUNDATION_ACCESS_AUD`
- `FOUNDATION_OWNER_SUB`
- `FOUNDATION_GITHUB_TOKEN`
- `FOUNDATION_DISPATCH_SHA`
- `FOUNDATION_SOURCE_SHA`
- `FOUNDATION_PHONE_ENABLED`

Rules:

- `FOUNDATION_PHONE_ENABLED` stays absent/false until the complete field-test preconditions pass.
- `FOUNDATION_ACCESS_AUD` must come from the actual Workshop Access application; never guess it.
- `FOUNDATION_OWNER_SUB` must come from real authenticated Access identity evidence; never guess it.
- `FOUNDATION_GITHUB_TOKEN` must be a narrowly scoped encrypted server-side secret; never place it in source or browser code.
- Dispatcher/source SHAs must be explicitly reviewed pins, not simply the newest branch heads.
- Do not put any owner email, JWT, GitHub token, Cloudflare secret, or private account identifier in this public repo.

## Exact next gate

Do **not** reopen architecture.

Do **not** add another Worker, Pages project, D1, KV, Queue, AI Gateway, model router, database, or orchestration layer.

Do **not** move on to arbitrary natural-language coding.

The next gate is still the bounded phone round trip:

1. Verify Cloudflare Access protects the intended production and preview hostnames.
2. Read the real Access AUD from the Workshop application.
3. Configure only verified server-side Foundation values.
4. Derive the owner subject from a real authenticated Access session; do not guess.
5. Configure the narrowly scoped GitHub secret.
6. Verify the reviewed dispatcher/source pins.
7. Keep `FOUNDATION_PHONE_ENABLED` false until everything above is ready.
8. Enable only for the governed field test.
9. From the actual Android phone, run the fixed `aios-path-containment` job.
10. Preserve one Foundation `job_id` end-to-end.
11. Return the correlated Independent Proof receipt to the Workshop.
12. Verify reload recovery, forbidden-input rejection, controlled failure, duplicate rejection, and linked-child retry.
13. Only after that may Harness record the bounded phone path as proven live.

## Definition of success

For this gate, success is not “Cloudflare is configured.”

Success is:

**Android Workshop → authenticated Pages intake → bounded dispatch → Foundry / AIOS / Builder → Independent Proof → correlated receipt → result back on Android under the same `job_id`.**

Until that actual owner-path test passes, the machine remains **PARTIALLY_PROVEN** for this lane.
