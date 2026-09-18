# Active Work Order

## TARGET
Prove the merged TWIS LOOP DECK simple performance shell on the target Android phone without restarting or redesigning the engine.

## CURRENT TRUTH
- VERIFIED_CURRENT: Authority repo is `Karmicmurphy/Ollie_Twis_Holo_workshop`, branch `main`, SHA `134540fc0abf6d64a82111eb5564dd604b57b2b3`.
- VERIFIED_CURRENT: Simple one-screen shell is merged into `app/loop-deck.html`.
- VERIFIED_CURRENT: Workshop CI and Static Contract passed on the merged change lineage.
- VERIFIED_CURRENT: Existing V2 engine remains intact behind Advanced.
- UNKNOWN: Actual Android microphone/audio timing, PWA cache refresh, and full phone interaction on Randy's device after this merge.
- VERIFIED_CURRENT: GitHub Pages deploy target is `https://karmicmurphy.github.io/Ollie_Twis_Holo_workshop/loop-deck.html`; deployment succeeded. Rendered Android behavior after the latest cache fix remains UNKNOWN.

## DO NOT
- Do not rebuild the Loop Deck engine.
- Do not replace the simple surface with another feature-heavy dashboard.
- Do not call the phone experience PROVEN_LIVE until the actual device path is exercised.
- Do not remove the Advanced V2 screens; they are the engine room.

## LANE
PROVE

## PROFESSIONAL FRAME
Mobile web audio release engineer + music performance workflow.

## ONE MOVE
Do not add features. Burn down the verified failure list first, then open the current main build on the target Android phone and exercise the simple path: landing screen -> KICK/BASS/HATS toggle -> bar-boundary behavior -> Energy -> first-use Ghost -> Fuck It/Undo -> custom sound + pack switching -> Save/Load -> reload.

## PROOF
Observed real-device behavior with sound output, toggles remaining phase-aligned, Ghost capturing prior audio, local custom sound surviving reload where OPFS is supported, and saved session restoring state.

## STOP
Stop when the Android path is either PROVEN_LIVE or BLOCKED/FAILED with a named failing layer and reproducible symptom.

## PARKING LOT
Pitch-preserving stretch, source separation, additional genre packs, richer waveform editing, and any new AI features.
