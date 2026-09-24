# Active Work Order

Project: `FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY`
State source: `state/CURRENT_PROJECT.json`

## STATUS

**ACTIVE — ARRIVAL / INTEGRATION REPAIR / LIVE VERTICAL-SLICE PROOF**

## CURRENT VERIFIED TRUTH

- Harness learning ingestion defect was found and repaired on PR #9; PR guard executes the repaired learner and canonical skill-registry tests successfully.
- Foundry human-signal arrival contract + loopback service passed 171 tests and merged to `software-builder-v0` at `3bb8e0d073f4bdda2af414340633a95b0e182887`.
- Workshop loopback Foundry bridge + read-only local source-yard inventory passed Workshop CI and merged to `living-workshop-main-build` at `f083c699d0dbf1837a8f207a53bcb243abc06be2`.
- AIOS remains at `8a954439af2b15b00f7c961d83552772b382fd1f`.
- Digital Scrapyard / canonical salvage suite remains at `a059a27ef2bd662827a51da44dd8efb8863d634c`.
- Full natural-language-to-certified-result behavior is **not** yet proven live on the owner's Windows machine.

## ONE TARGET

Prove that the machine carries the integration burden from one natural-language owner request through the actual machine rather than requiring the owner to select repos, skills, modules, or internal categories.

## NEXT MOVE

1. On the owner's Windows Workshop, start the merged local companion and merged Foundry loopback service.
2. Send one human-signal request through Workshop -> Foundry and verify the returned `signal_id` / receipt.
3. Run the read-only source-yard inventory against one bounded local target and inspect the generated manifest.
4. Extend the same visible correlation identity into one bounded Foundry job -> AIOS -> Independent Proof -> Workshop result.

## DO NOT

- Do not build another OS, agent framework, proof engine, skill suite, or memory platform.
- Do not call source-yard inventory PROVEN_LIVE until it runs on the actual Windows machine.
- Do not call the whole machine PROVEN_LIVE because subsystem CI is green.
- Do not make the owner manually route a normal request through internal components.

## BLOCKERS

- `LOCAL_WINDOWS_FIELD_TRIAL_NOT_RUN`
- `FULL_JOB_CORRELATION_NOT_YET_WIRED`
- `OPEN_DOOR_UI_NOT_YET_EXPOSED`

## STOP CONDITION

One owner natural-language input traverses:

`Workshop -> Foundry -> bounded Foundry job -> AIOS -> Independent Proof -> Workshop`

under one visible correlation identity, and the read-only Windows inventory produces a real local manifest without executing or importing source files.
