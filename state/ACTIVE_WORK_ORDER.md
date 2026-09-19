# Active Work Order

## TARGET
Close out the unified TWIS Loop Deck / Pro Rig as one browser workstation with one audio engine and one authoritative transport.

## CURRENT TRUTH
- AUTHORITY: `Karmicmurphy/Ollie_Twis_Holo_workshop` / `main` / `f39db751c41cfe9d909fa50efe5d19afa73b3d5d`.
- Pro Rig no longer owns a separate Tone.Transport runtime; `pro-rig.html` enters `loop-deck.html?mode=pro`.
- Loop Deck and Pro Rig now share `twis-loop-core.js`, `twis-loop-deck-v2.js`, the same AudioContext-backed transport, sound rack, loop state machines, OPFS/import path, and performance surface.
- Deterministic Loop Core tests pass.
- Static Contract passes.
- Workshop CI passes on merged main.
- Unified desktop/mobile Chromium browser proof passes.
- GitHub Pages deployment passes.
- DEPLOYED LIVE BROWSER proof passes: scenes, eight roles, BUILD/DROP/ECHO/WASH/VOCAL/FUCK IT, STOP, and ADVANCED all exercised successfully with no visible errors.
- Advanced-mode hidden-panel defect was fixed by routing ADVANCED to the actual `loop` page.

## DO NOT
- Do not reintroduce Tone.Transport or a second musical clock.
- Do not fork another Pro Rig engine.
- Do not replace working OPFS/import/recorder mechanisms solely for cleanliness.
- Do not call subjective sonic quality proven by automation.

## LANE
CLOSEOUT -> PHYSICAL/SONIC PROOF

## ONE MOVE
Only remaining material proof is physical target-device and subjective sonic acceptance. If that exposes a defect, fix only the failing layer and rerun the regression chain.

## PROOF COMPLETED
1. syntax/contracts/build;
2. deterministic master-clock and loop-state tests;
3. shared-engine desktop browser proof;
4. shared-engine phone-sized Chromium proof;
5. repeated start/stop and long-run browser proof;
6. advanced loop workstation visibility and controls;
7. Pages deployment;
8. deployed live-browser user-path proof.

## STOP
Do not call the sonic target fully DONE until the actual user accepts the sound on physical hardware. Functionally, the unified browser workstation path is PROVEN_LIVE_BROWSER.

## PARKING LOT
IndexedDB transactional project generations, bounded/preallocated recorder pages, workerized import analysis, multi-step semantic undo/redo, physical Android lifecycle proof, optional Signalsmith integration.
