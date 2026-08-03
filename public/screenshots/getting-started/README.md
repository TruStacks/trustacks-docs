# Getting-started screenshots — capture guide

This folder holds the step screenshots for the getting-started walkthroughs.
Drop a PNG here with the exact filename below and it wires straight into the
page: each slot is already placed in the MDX as a labeled placeholder.

## How the slots work

In `app/getting-started/beta/page.mdx` every numbered step has:

```mdx
{/* asset: public/screenshots/getting-started/01-sign-in.png */}
<figure className="ts-shot ts-shot--pending">
  <figcaption>Step 1 · ...</figcaption>
</figure>
```

To ship a shot, drop the file here, then swap the placeholder for the image
and remove the `--pending` marker:

```mdx
<figure className="ts-shot">
  <img src="/screenshots/getting-started/01-sign-in.png" alt="Step 1 · ..." />
  <figcaption>Step 1 · ...</figcaption>
</figure>
```

(Leave the wiring to a maintainer if you like — just add the files with the
right names and say so on the PR; the MDX edit is mechanical.)

## Filenames and what each shows — `beta` (concierge) walkthrough

| File | Step | Shot |
|---|---|---|
| `01-sign-in.png` | 1 | Sign-in screen at `app.trustacks.com` after setting your password |
| `02-get-set-up.png` | 2 | The onboarding "Get set up" checklist |
| `03-llm-provider.png` | 3 | Settings → LLM Provider with a validated key |
| `04-connect-runner.png` | 4 | Runners → Connect a runner, the copyable one-line install |
| `05-connect-repo.png` | 5 | Services → Connect a repo, binding service + platform repos |
| `06-run-analysis.png` | 6 | The live event stream during Run analysis |
| `07-gap-report.png` | 7 | The Compliance gap report (tier, coverage %, SOC2 CC1–CC9) |
| `08-promote-proposal.png` | 8 | Promote to proposal, policy gate showing "allow" |
| `09-review-pr.png` | 9 | The pull request in GitHub with "Preservation notes" |
| `10-validated.png` | 10 | The item advancing shipping → validated after ArgoCD sync |
| `11-discord.png` | 11 | The "Join our Discord" link in the sidebar |

The self-serve `hosted-quickstart` page has no screenshot slots yet; add them
the same way if we want them, numbered `hq-01-...` to keep the two sets apart.

## Capture specs

- **Format:** PNG. Retina / `@2x` if your display supports it (sharper on
  high-DPI screens; the page scales them down to fit).
- **Width:** crop to the relevant UI panel, roughly 1200–1600px of content.
  Do not screenshot the whole desktop; frame the thing the caption names.
- **Theme:** pick one (light or dark) and use it for all 11 so the set reads
  as one sequence. The page adds a subtle border either way.
- **Redact before saving.** Blur or crop out: enrollment tokens, API keys
  (the runner one-liner is the big one), real customer emails, and any
  private org/repo names you would not want public. These ship to the public
  docs site.

## Getting them to Claude Code

The docs agent has **no browser or screenshot capability** and cannot reach
your logged-in `app.trustacks.com`, so capture is manual:

1. Grab each shot. macOS: `Cmd+Shift+4` (drag a region) or `Cmd+Shift+5`. For
   consistent framing a full-page browser extension works too (GoFullPage,
   Awesome Screenshot, Fireshot) — just crop to the panel.
2. Save into this folder with the exact filename above.
3. Say so on the PR (or in chat) and the agent verifies each file, wires it
   into the MDX, removes the `--pending` slot, and re-runs the build.
