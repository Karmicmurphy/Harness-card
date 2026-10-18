# COILSIDE release incident — reusable FRIDAY prevention (2026-10-17)

**Evidence:** CI passed for COILSIDE source while an automatic Cloudflare Workers build failed on the same source. Cloudflare build output identified a missing generated Prisma client (`PrismaClient` export from `@prisma/client`), not a lost GitHub repository connection.

## Smallest proven repair
Updated `Karmicmurphy/coilside` `package.json` `cf:build` to run `prisma generate && opennextjs-cloudflare build`. GitHub CI passed. Cloudflare's existing `main` build trigger deployed revision `2e07e429c9174d6ea99503e357476c37f8c5b241` to existing Worker `coilside`, deployment `a5f1668f-41fc-4cda-b646-5c7a3b180242`, preserving existing D1 and assets bindings.

## Evidence boundary
The build and production deployment are provider-confirmed. Independent Android UI and primary-action confirmation was not obtained; **do not label this PROVEN_LIVE**. The Foundation Workshop Preview's different missing-secret problem remains open and separate.

## Reusable rule
Do not diagnose a deployment as credential failure just because an unrelated configuration API call returns 10000. First inspect the active repository integration, actual build trigger, exact build/deploy logs, source build scripts and current provider runtime settings. Match source SHA to deployment SHA. Test and deploy are not live-device proof.

## Permanent prevention
Use `friday-provider-release` with `scripts/provider_release_gate.py` and `tests/test_provider_release_gate.py` to produce a fail-closed, non-secret release evidence verdict. Keep owner approvals and secret operations at their existing gates.
