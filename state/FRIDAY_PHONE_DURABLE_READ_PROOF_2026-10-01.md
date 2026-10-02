# FRIDAY durable READ — phone proof

Date: 2026-10-01
Local time: approximately 22:56 America/Chicago
Authority: `RANDY_AND_HARNESS`
Governing recovery revision: `732378db1eb5a35558627695e1436c3760e7a4ab`

## Outcome

The refreshed FRIDAY MCP was exercised from Android through Codex Remote and the new durable READ operator was invoked successfully.

This closes the specific proof gap between local durable READ lifecycle tests and real phone-side invocation of the registered MCP tool.

## Phone-side invocation

Tool: `friday_run_read`

Observed result:

- status: `CERTIFIED`
- cached: `true`
- execution_performed: `false`
- authority_changed: `false`
- activation_performed: `false`
- work order: `friday-work:7fcc12e4d9057ab09819ff2a`
- canonical job: `job:4ea425916cc72eab71f134af`
- certificate: `cert:4b8681457665e0e0678d028e97eb2217`
- result: `PAGES_BOUNDED_JOB_ROUND_TRIP`
- scope: `IMMUTABLE_READ_FIXTURE_ONLY`
- source revision: `732378db1eb5a35558627695e1436c3760e7a4ab`

The existing certified receipt was recovered without rerunning the worker. No edits, new work, authority changes, or activation occurred.

## Evidence state

`PROVEN_REMOTE_PHONE_DURABLE_READ_RECOVERY`

What this proves:

1. Android phone -> Codex Remote -> refreshed registered FRIDAY MCP.
2. The updated MCP tool list is live remotely.
3. `friday_run_read` is callable from the phone path.
4. The durable READ lifecycle can recover an already certified result.
5. Duplicate/cached recovery returns the same preserved work-order/job/certificate correlation without executing again.
6. Recovery remains bounded to the existing immutable fixture and governing snapshot.

What this does **not** prove:

1. Fresh authority READ against current live Harness state.
2. Arbitrary natural-language READ capability.
3. Automatic/background queue consumption.
4. New Foundation execution for this cached call.
5. `PAGES_BOUNDED_JOB_ROUND_TRIP` itself.
6. Workshop/Cloudflare live phone dispatch.

## Durable learning

- A cached certified result is a first-class successful outcome when request identity and source snapshot are unchanged; do not rerun merely to demonstrate activity.
- Remote phone proof must exercise the specific MCP capability, not only inspect gateway status.
- Preserve the distinction between gateway status (`execution_performed: false`) and prior certified worker execution embodied in the stored certificate.
- Fixture-bounded proof must remain fixture-bounded until fresh authority capture and a broader capability contract are separately proven.

## Current next gate

The certified result continues to identify `PAGES_BOUNDED_JOB_ROUND_TRIP` as the next unproven gate in the immutable recovered snapshot. That finding is evidence from the stored snapshot, not proof that the gate is still the live-current blocker.

Before acting on it as current truth, either perform a fresh bounded authority read or explicitly operate against the pinned snapshot.
