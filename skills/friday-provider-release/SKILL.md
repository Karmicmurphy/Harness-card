# FRIDAY Provider Release — bounded existing-project skill

name: friday-provider-release
version: 0.1.0
status: CANDIDATE / PROVEN_IN_TEST_ONLY
canonical_repo: Karmicmurphy/Harness-card
canonical_path: skills/friday-provider-release/SKILL.md

## Trigger
Use when the owner says, in everyday language, to fix a deployed app, make a change live, repair GitHub-to-Cloudflare, or determine whether the latest code is actually running. This is a procedure for existing projects; do not invent another FRIDAY instance or deployment worker.

## Contract
1. Load Harness authority, owner approval and current work order. Project repos other than FOUNDATION remain separate; do not change canonical Foundation pins when repairing an application like COILSIDE.
2. Identify exact repository, branch, full commit SHA, existing provider target/environment and the minimum intended user action. Record what cannot change.
3. Inspect current GitHub CI and Cloudflare Pages/Workers settings and actual build/deploy logs. Examine source-side build scripts AND provider build commands before asking the owner to repair a token or permission.
4. Apply the smallest authorized and reversible source/configuration repair; use an isolated branch, verify tests, and merge only under the existing approval and CI gates. Never invent credentials, copy Production secrets to Preview, bypass Access, or create replacement infrastructure.
5. Confirm provider deployed SHA, existing target, environment, ID, traffic (for Workers), names of required bindings and live route separately. Generate a sanitized evidence packet for `scripts/provider_release_gate.py`; never supply secret values.
6. The script is a FAIL-CLOSED deterministic receipt checker, not a deploy tool or self-certification of live behavior. A reported `READY_FOR_INDEPENDENT_REVIEW` still needs independent provider, browser and owner-device confirmation.
7. To claim **PROVEN_LIVE**, independently check that the intended screen and primary real action work on the target phone. If blocked, name exactly one owner action and preserve safe state.
8. Record a durable release receipt, a reusable incident prevention rule when applicable, and the exact next unfinished gate.

### Multi-actor provider truth gate — field-proven correction

**Before** declaring GitHub-to-Cloudflare disconnected, requesting a Cloudflare token or telling the owner to manually reconnect an app:

1. Independently query the *existing* provider Worker/Pages build configuration (repository, branch, auto-build flag, stored token **metadata only**), provider build history keyed to exact Git commit, deployment history and production version/bindings.
2. Distinguish a **GitHub Actions release workflow** from **Cloudflare-native automatic Builds**. If one job lacks a repository secret, it may be redundant while provider-native Builds is already deploying. Lack of write scope on a connected Chat Cloudflare actor does not mean the account or native build trigger lacks the permission.
3. Compare the source SHA, green CI, successful provider build SHA, deployment timestamp/ID and deployed script or assets. A successful build from an older commit cannot prove a new commit was released; a deploy is still not a phone user-path proof.
4. For contradictory evidence, report `PARTIAL_UNKNOWN` and inspect the exact missing layer; never advertise an owner credential step on a negative inference from a single tool or actor. Preserve the known-good Worker, D1 and local phone records throughout.

This rule came from the existing Coilside/WTF field-app release on October 23: an unrelated GitHub release job lacked its `CLOUDFLARE_API_TOKEN`, while Cloudflare's separate authorized GitHub-triggered build successfully deployed the latest main branch. The right correction is **verify all active release paths before requesting credentials**, not install more credentials to fix an unused path.

## Reuse existing skills
Apply canonical `chat-software-harness`, `owner-interruption-minimizer` and `proof-gate` from the registered sources. Route `constraint-breaker-lab` only for actual cost/complexity bottlenecks. Do not load every unrelated skill.

## Evidence input example (non-secret)
```json
{
  "target": {"repo": "Karmicmurphy/coilside", "branch": "main", "sha": "2e07e429c9174d6ea99503e357476c37f8c5b241", "service": "coilside", "environment": "production", "required_bindings": ["COILSIDE_DB", "ASSETS"]},
  "authorization": {"production_approved": true},
  "ci": {"sha": "2e07e429c9174d6ea99503e357476c37f8c5b241", "conclusion": "success", "run_url": "https://github.com/Karmicmurphy/coilside/actions/runs/39082036540"},
  "deployment": {"sha": "2e07e429c9174d6ea99503e357476c37f8c5b241", "status": "success", "service": "coilside", "environment": "production", "id": "a5f1668f-41fc-4cda-b646-5c7a3b180242", "traffic_percent": 100, "bindings": ["COILSIDE_DB", "ASSETS"]}
}
```

Run: `python scripts/provider_release_gate.py sanitized-evidence.json`. Nonzero exit means evidence is not independently complete, not permission to force a deploy.

## Stop condition
A truthful, current, bounded release receipt gives the owner the real change, exact commit, deploy ID, verification level and zero or one necessary owner action. The separate Foundation Android Preview fixture remains behind its established owner/secret gates; this skill does not authorize fixture dispatch.
