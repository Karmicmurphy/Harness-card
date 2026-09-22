# Active Work Order

Project: `FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY`
State source: `state/CURRENT_PROJECT.json`

## TARGET
Run the first real owner-device continuity field trial through PersonalJarvis -> FRIDAY -> Verified Continuation Capsule -> Foundation queue, and return a durable receipt.

## VERIFIED CURRENT
- Foundation core is operational in test.
- Verified Continuation Capsule V0 is proven in test.
- FRIDAY Gateway V0 is proven in test and remains queue-only / request-only.
- Candidate implementation remains on `Karmicmurphy/temporal-capability-foundry@verified-continuation-capsule-v0` PR #22.
- Owner-device execution is not yet proven.
- TWIS Loop Deck / Pro Rig is a separate creative project and is not the active Foundation work order.

## LANE
VERIFIED CONTINUITY + FRIDAY GATEWAY V0 / FOUNDATION CERTIFICATION / HUMAN REVIEW

## ONE MOVE
On Randy's owner device, connect PersonalJarvis to the `friday-foundry` MCP stdio gateway, recover one valid continuation capsule, queue one harmless bounded work order, read the durable receipt back, then stop.

## PROOF
1. PersonalJarvis can see the FRIDAY MCP tools.
2. `friday_recover` accepts and verifies a valid capsule.
3. Recovered project/revision/evidence/blockers/next-action match the capsule.
4. One READ, RESEARCH, or BUILD_CANDIDATE work order is queued.
5. The queued work order and receipt survive a gateway restart using the durable state directory.
6. `friday_status` reports `execution_performed: false`.
7. No merge, deploy, publish, spend, delete, permission change, or activation occurs.

## BLOCKER
`OWNER_DEVICE_REQUIRED`

This chat can inspect, prepare, test repository-side components, and repair stale authority. It cannot truthfully mark the field trial passed without the owner-device run.

## STOP
Stop at either:
- DONE: the owner-device field trial produces the durable receipt and all proof checks above pass; or
- BLOCKED: a concrete owner-device/runtime failure is captured with enough evidence for the next bounded repair.

## CURRENT NEXT ACTION
Connect a PersonalJarvis client to the proven friday-foundry MCP stdio gateway and run one owner-device field trial: verify a continuation capsule, recover current truth, queue one bounded work order, and return its receipt. Local Windows/phone execution remains BLOCKED_OWNER_DEVICE. Do not merge PR #22, deploy, activate, or broaden FRIDAY authority without Randy review.
