# FRIDAY private-repository read access — owner credential boundary

**Owner authorization, October 23, 2026:** FRIDAY may **read** the two private Foundation source repositories for governed monitoring, exact source comparisons and candidate assessment. This is **not** permission to modify, merge, deploy, or change their approved Harness SHAs.

## The two private repositories

- `Karmicmurphy/temporal-capability-foundry` — Factory / software builder
- `Karmicmurphy/digital-scrapyard-autopilot` — Salvage / warehouse

Both were verified private via GitHub repository metadata. The connected ChatGPT GitHub App can already access them, but its installation credential is **not** automatically available in the separate `Karmicmurphy/Harness-card` GitHub Actions runner. GitHub's built-in `GITHUB_TOKEN` for Harness cannot read other private repositories. This has been confirmed by the existing scheduled observation's two UNKNOWN access results.

## One-time owner identity step needed on GitHub

The available GitHub connector can read and edit repository code, but **cannot create a PAT, manage private keys, or set repository Actions secrets**. Neither a chat authorization nor GitHub App installation grants that runner credentials.

1. [Create a fine-grained GitHub access token](https://github.com/settings/personal-access-tokens/new) under resource owner **Karmicmurphy**. Token name `FRIDAY-FOUNDATION-READ`. Select **Only select repositories**, and exactly the **two private repositories above**. Under **Repository permissions**, set **Contents: Read-only** (Metadata: Read-only is automatically included). Do not grant Actions, Secrets, Administration, Contents Write, or repository-wide access. Set a suitable expiration/rotation schedule.
2. In [Harness Card repository Actions secrets](https://github.com/Karmicmurphy/Harness-card/settings/secrets/actions), choose **New repository secret**: name **`FOUNDATION_READ_TOKEN`**, value **the newly generated token**, then **Add secret**. Paste it **only into the GitHub secret field**, never a GitHub issue, chat, source code, commit, or output log.

**This is the only owner action required to make the existing reader functional.** Do not create any new GitHub App, service account or paid plan for this small read access; a GitHub App with managed installation-token rotation is a safer longer-term alternative to expiring PATs once needed.

## What the code does automatically once the secret is present

- Existing scheduled `.github/workflows/friday-control-plane.yml` runs daily (GitHub best-effort scheduling).
- On trusted non-PR runs, the GitHub observer and exact SHA-compare operator receive the named **read-only** token. The generated status/maintenance queue will identify both real observed heads, while approved/pinned SHAs remain unmodified.
- Existing self-improvement status refresh and safe generated-state collision recovery use the same named token only on trusted non-PR jobs.
- All `pull_request` checks fall back to the built-in repo-scoped `github.token`: the private credential is **not** injected into PR jobs.
- If a token is absent, expired, unauthorized or denied, the two private roles remain `UNKNOWN_READ_ACCESS`. This is not a reason to relax permissions, auto-repin or claim a successful comparison.
- Testable success: in a subsequent trusted scheduled/manual FRIDAY run, `foundation-observation.json` shows Factory and Salvage states `MATCH` or `RECONCILIATION_REQUIRED` with valid observed and canonical commits; queue no longer lists either as `UNKNOWN_READ_ACCESS`. **Do not mistake branch drift for an approved upgrade.**

## Scope, limits and follow-up

- A private-repo contents read token can read source code in **both repositories**, not merely metadata. Treat it as sensitive. Keeping Harness **public** means all authorized workflow authors must be trusted, even with PR-run secret withholding. GitHub Actions logs should never print the token or secret content.
- Expiration/revocation will return those roles to UNKNOWN until a rotated secret is installed. Do not automatically extend the scope to all private repositories or use a broad classic PAT.
- Do not alter current Harness `FRIDAY_BOUNDED_OPERATOR_LOOP` gate, approved SHA pins, public/private visibility, production, Android/phone or Cloudflare Preview. Those workstreams remain parked.
- The GitHub connected-app permission in **ChatGPT** and the FRIDAY **Actions runner** permission are separate; success in one does not prove the other.

## Proof debt

Code/CI changes can be merged without token access, but **live private-repo Actions access is NOT PROVEN** until the owner's actual secret is supplied and a trusted run confirms both repository reads. Do not record this as already granted.
