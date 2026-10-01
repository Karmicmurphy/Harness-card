# Provider deployment debugging

Use this reference only when a software task has crossed into a hosted provider, CI, preview deployment, runtime binding, routing, or target-device mismatch.

## Truth ladder

Establish evidence in this order and do not skip levels:

1. repository branch/ref actually intended for the work;
2. provider deployment source SHA;
3. provider build configuration consumed for that deployment;
4. runtime configuration/bindings visible to the executing function or service;
5. route/hostname resolves to that deployment;
6. target-device request reaches that route;
7. primary user action succeeds;
8. user-visible result returns.

A green step never proves the next step.

## Configuration-authority collision check

Before asking the owner to re-enter provider settings, inspect every configuration authority that can override them:

- repository config files;
- provider dashboard environment settings;
- branch/environment overrides;
- deployment snapshots;
- build root/output/function-directory settings;
- routing/worker/service-worker/cache layers.

If two authorities disagree, stop retries and resolve the authority collision first.

## Fresh deployment rule

A retry of an old deployment is useful only when the inputs to that deployment are unchanged.

If source configuration authority changed, require a fresh deployment generated from the new source/ref. Then verify the provider reports that new ref.

## Zero-job CI rule

If a CI/workflow run is red but contains zero jobs, classify it as workflow/configuration validation first. Inspect workflow syntax, expressions, event filters, permissions, and provider integration before touching application code.

## Owner interruption rule

Do not ask the owner to perform a manual diagnostic action that the current session can answer from repository, CI, logs, provider tooling, or existing evidence.

When owner action is genuinely required, ask for one action that directly crosses the remaining unavailable boundary.

## Proof language

Use:

- IMPLEMENTED_UNPROVEN when source changed but checks are incomplete;
- PROVEN_IN_TEST when repository/CI checks pass;
- PROVEN_LIVE only when the target provider/runtime/device path is exercised successfully.

Never use "fixed" as a synonym for "patched".

## Failure-cycle sibling scan

After the first user-visible failure in a deployment layer, inspect sibling risks before another release attempt:

- stale configuration authority;
- stale tests/contracts;
- wrong branch/ref;
- wrong deployment alias;
- provider environment mismatch;
- stale cache/service worker;
- unrelated workflow noise;
- missing runtime binding;
- route interception;
- deployment snapshot reuse.
