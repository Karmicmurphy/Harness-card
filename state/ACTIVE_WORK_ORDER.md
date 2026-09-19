# Active Work Order

## TARGET
Deliver one TWIS Pro Rig build that works from the same URL on Android phone and PC and sounds like an intentional professional melodic electronic performance, while preserving advanced Loop Deck import/loop capability.

## CURRENT TRUTH
- Android V3 interaction is USER_REPORTED_CURRENT and proven by screen recording.
- V3 sonic quality failed the user's professional-live-set target.
- V4 is implemented on `feature/pro-rig-v4-cross-device-sonic`.
- V4 uses CC0 sampled drums and CC0 voice texture when reachable, deterministic synth fallbacks, phrase-based harmony/melody, quantized scenes, build/drop transitions, sidechain-style ducking, master dynamics, and runtime diagnostics.
- The existing advanced Loop Deck remains available through LOOPS / IMPORT rather than being rebuilt.
- First V4 CI caught a stale V3 contract test; that test has been corrected.
- Live V4 phone and PC proof are still pending.

## DO NOT
- Do not add cosmetic UI work unless required by the target-device path.
- Do not claim cross-device success from responsive CSS alone.
- Do not call CI success sonic proof.
- Do not replace proven Loop Deck subsystems unnecessarily.
- Do not blame Android/PC before checking the actual runtime path.

## LANE
BUILD-FIX -> PROVE

## PROFESSIONAL FRAME
Electronic music producer + live-performance engineer + browser audio/reliability engineer.

## SKILLS / MECHANISMS
Artifact Compass, Artifact Salvage, Proof Gate, Environment Preflight, Rabbit-Hole Governor, Cost & Complexity Challenge.

## ONE MOVE
Finish V4 CI, merge/deploy only if clean, then exercise the identical live URL on Android and PC against the same sonic/human-path contract.

## PROOF
Required:
1. syntax/contracts/build pass;
2. rights-clean remote performance pack URLs reachable;
3. page opens silent;
4. PLAY produces coherent music;
5. stems/scenes/BUILD/DROP/VOCAL HIT have audible musical effects;
6. network sample failure leaves a usable fallback engine;
7. Android live path passes;
8. PC live path passes;
9. user accepts sonic result as materially closer to professional live-set target.

## STOP
DONE only after both device paths and sonic target are proven. Otherwise remain PARTIALLY_PROVEN/BLOCKED with exact failing layer.

## PARKING LOT
Offline vendoring of binary sample assets, Signalsmith pitch-lock integration, deeper stem separation, additional sound packs, visualizers.
