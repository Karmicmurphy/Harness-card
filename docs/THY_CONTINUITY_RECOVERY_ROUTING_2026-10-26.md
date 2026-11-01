# THY Recovery Routing — Machine-Side Continuity Handoff
Date: 2026-10-26 (America/Chicago)
Lane: NON-ACTIVE, USER-TRIGGERED CREATIVE CONTINUITY ROUTE
Status: REVIEW_PENDING / NOT A LIVE FRIDAY OPERATOR CAPABILITY

## User outcome
When the owner asks for the previously completed Thousand-Year Hangover episode, audio, or next continuation, **recover the verified existing work first** instead of suggesting that the user recreate, re-upload, or regenerate it. No extra accounts, duplicate creative projects, or unnecessary credits.

## Authority separation
The Thousand-Year Hangover is an independent creative saga, not CTOS/Foundation/FRIDAY governance or engineering. This public Harness repo owns only an optional **routing adapter**. The private source materials and the canonical full recovery package remain in the owner's ChatGPT Library folder:
`The Thousand Year Hangover! Never Ending Saga!`

Read the existing three Library artifacts through authorized Files access (never copy their contents here):
- `THY_Continuity_Recovery_SKILL.md`
- `THY_Complete_Thread_Handoff_2026-10-26.md`
- `THY_Asset_Manifest_2026-10-26.json`

The associated first-cut episode MP4 is named `THY_Episode_001_The_Noise_Inside_FIRST_CUT_v2.mp4`. Metadata was observed to exist in Library; audiovisual playback and last-frame identification remain UNVERIFIED. The original user-made Google Flow/CapCut footage is independent of this first cut, and the subsequently generated approved voice sample is independent of both. Do not assume audio has already been mixed in.

## Exact machine-side change
- Added a public-safe THY-only bridge: `skills/thy-continuity-recovery/SKILL.md`
- Added one conditional skill entry in `config/skill_registry.json`
- Added THY trigger and strict separate-project constraint in `ROUTING.md`
- Documented the adapter in `skills/SKILL_SOURCES.md`
- Added `tests/test_thy_continuity_recovery.py` to check resolution and the absence of private media, private URL, private file IDs or story data.

## The user path to prove after merge
1. Owner asks "Recover Thousand-Year Hangover".
2. A capable authorized client resolves the route, reads the private THY Library handoff and manifest, and surfaces the exact existing MP4 as an openable Library card.
3. Client checks actual playback and final frame, distinguishes later approved voice from older video, asks for no unnecessary regeneration, and checkpoints the next exact action privately.
4. If FRIDAY operator lacks ChatGPT Files access, return BLOCKED_BY_LIBRARY_ACCESS and no success claim.

## Live limits
A GitHub branch/PR and a passing code test DO NOT imply FRIDAY has loaded this skill, has ChatGPT Library access, can fetch the video's raw bytes, can execute creative editing, or can open the film on Android. Do not alter `state/CURRENT_PROJECT.json` Foundation active work order or five-repository authority to create this separate capability.

## Resume
Inspect the PR and its tests; request review/merge within existing authority. After merge, test the real THY recovery user path with an authorized Files-capable client. Do not merge, deploy, spend credits, grant provider scopes, or alter production in the course of this proposed routing change.
