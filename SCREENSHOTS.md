# Screenshot shot list

Every screenshot slot on the site, generated from the slots in the pages by `scripts/screenshot_list.py` (rerun it after adding or moving a slot). Capture as **BetaOrg1** on app.trustacks.com unless noted, and save each PNG at the exact path.

**Capture specs:** PNG, @2x if you can, cropped to the panel the caption names (about 1200–1600 px of content), one theme for the whole set. **Redact** enrollment tokens, API keys, real customer emails and private org/repo names: these ship to the public site.

| # | Save as | Page | Where in the app | Shows | Setup / notes |
|---|---|---|---|---|---|
| 1 | `public/screenshots/getting-started/01-register.png` | `getting-started/hosted-quickstart` | auth.trustacks.com sign-in | Step 1 · The auth.trustacks.com sign-in page with the Register option. | Signed out. |
| 2 | `public/screenshots/getting-started/02-team-profile.png` | `getting-started/hosted-quickstart` | #/onboarding, step 1 | Step 2 · Get set up, "Tell us about your team" with the optional company and team-size fields. |  |
| 3 | `public/screenshots/getting-started/03-enroll-runner.png` | `getting-started/hosted-quickstart` | #/settings/runners, or onboarding step 2 | Step 3 · Generate enrollment token, with the copyable helm install command. | Redact the token, including inside the command. |
| 4 | `public/screenshots/getting-started/04-create-application.png` | `getting-started/hosted-quickstart` | #/applications | Step 4 · Applications, "Create an Application" with a name typed and the Create button enabled. | A name typed, before pressing Create. |
| 5 | `public/screenshots/getting-started/05-connect-repo.png` | `getting-started/hosted-quickstart` | Applications › Connect a repo | Step 5 · + Connect repo: role picker, GitHub App install, then the repo and Application binding. |  |
| 6 | `public/screenshots/getting-started/06-declare-profile.png` | `getting-started/hosted-quickstart` | #/onboarding, step 4 | Step 6 · Get set up, "Declare what you run" with the 12 categories and the starter environment-profile.yaml. |  |
| 7 | `public/screenshots/getting-started/07-llm-provider.png` | `getting-started/hosted-quickstart` | #/settings/llm | Step 7 · Settings, LLM provider with Anthropic selected and the key saved (key masked). | Key masked (sk-ant…). |
| 8 | `public/screenshots/getting-started/08-first-analysis.png` | `getting-started/hosted-quickstart` | A service › Run a new analysis | Step 8 · A service's analysis running: the Coordinator and Code Reviewer turns streaming in. | Capture while it streams. |
| 9 | `public/screenshots/getting-started/09-promote-proposal.png` | `getting-started/hosted-quickstart` | Analysis › Promote to proposal | Step 9 · Proposal detail: the Constitution's "clean, no violations" turn and the "Pull request opened" banner. | Needs a proposal that reaches pr_opened. |
| 10 | `public/screenshots/getting-started/10-pr-and-ci.png` | `getting-started/hosted-quickstart` | GitHub: the platform-repo PR | Step 10 · The platform-repo pull request on GitHub with the Preservation notes section, and the green CI run. | Outside the app; crop to the PR body and checks. |
| 11 | `public/screenshots/getting-started/11-argocd-synced.png` | `getting-started/hosted-quickstart` | Your ArgoCD UI | Step 11 · Your ArgoCD showing the new Application Synced and Healthy. | Outside the app. |
| 12 | `public/guide/applications.png` | `guide/applications` | Applications in the sidebar (`#/applications`) | Applications list with one Application card, its services and target cluster, and a deploy-status chip. |  |
| 13 | `public/guide/application-detail.png` | `guide/applications` | Applications in the sidebar (`#/applications`) | Application detail with Renderer, GitOps root, Target clusters, Platform / GitOps repo and Member services cards. |  |
| 14 | `public/guide/connect-repo.png` | `guide/applications` | Applications in the sidebar (`#/applications`) | Connect a repo dialog, role picker with Service repo and Platform repo cards. |  |
| 15 | `public/guide/service-detail.png` | `guide/applications` | Applications in the sidebar (`#/applications`) | Service detail with the Run a new analysis bar and the Analyses tab showing one done analysis with "promote →". |  |
| 16 | `public/guide/proposal-detail.png` | `guide/applications` | Applications in the sidebar (`#/applications`) | Proposal detail timeline with Constitution "clean, no violations", an advisory gap row, the green "Pull request opened" banner and the Explanation card. |  |
| 17 | `public/guide/billing.png` | `guide/billing` | Billing in the sidebar (`#/settings/billing`) | Billing screen showing Plan (trial), Tier (developer), Trial ends and the Upgrade button. |  |
| 18 | `public/guide/compliance.png` | `guide/compliance` | Compliance in the sidebar (`#/compliance`) | Compliance screen with the SOC2 evidence card listing controls and event counts for the last 90 days. |  |
| 19 | `public/guide/audit-reports.png` | `guide/compliance` | Compliance in the sidebar (`#/compliance`) | Audit Reports form (control family SOC2, PDF, 7-day window) with the "Report download started" banner. |  |
| 20 | `public/guide/gap-analyses.png` | `guide/gap-analyses` | Gap analyses in the sidebar (`#/gaps`), a run's detail at | Gap analyses list with the Application picker, "Run new gap analysis" button and three runs. |  |
| 21 | `public/guide/gap-analysis-detail.png` | `guide/gap-analyses` | Gap analyses in the sidebar (`#/gaps`), a run's detail at | Gap analysis detail with the Activity log (Constitution, Coordinator, Baseline Security, SOC2 turns) and the report card with tier badge and category bars. |  |
| 22 | `public/guide/maturity.png` | `guide/maturity` | Maturity in the sidebar (`#/maturity`) | Maturity hero with the tier badge, the verified/credited/potential bar, the tooling and behavior bars, two open-gap cards and the Path to gold card. |  |
| 23 | `public/guide/onboarding.png` | `guide/onboarding` | Get set up in the sidebar (`#/onboarding`) | Get set up wizard, step list on the left with two steps ticked, "Enroll your runner" open on the right. |  |
| 24 | `public/guide/overview.png` | `guide/overview` | the first item in the sidebar (`#/`) | Overview with maturity header, two attention cards and the Policy in force card. |  |
| 25 | `public/guide/rules.png` | `guide/rules` | Rules in the sidebar (`#/rules`) | Rules screen with the gate strip, filters, a rule list on the left and practice.workflow_has_test_step selected on the right. |  |
| 26 | `public/guide/runners.png` | `guide/runners` | Runners in the sidebar (`#/settings/runners`) | Runners screen with the enrollment card (token + helm command), the upgrade card, and one connected runner row. |  |
| 27 | `public/guide/settings.png` | `guide/settings` | Settings in the sidebar (`#/settings/llm`) | Settings screen with the Anthropic provider selected, masked key fields and the green "configured" banner. |  |
| 28 | `public/guide/signals.png` | `guide/signals` | #/signals | Signals with the Sources panel (GitHub "Connected · read-only verified", ArgoCD "Reporting", SARIF upload) above the findings list, one finding selected showing the six-step governed loop. | Needs at least one finding: upload a SARIF file first. |
| 29 | `public/guide/signals-connect-choose.png` | `guide/signals` | #/signals › Connect a source | Connect a source dialog, first step: the three source cards (GitHub, read-only · ArgoCD deploy status · SARIF upload). |  |
| 30 | `public/guide/signals-connect-runner.png` | `guide/signals` | #/signals › Connect a source › GitHub | Connect a source, GitHub: the runner picker (runner id · version), Runner namespace and Helm release filled in. |  |
| 31 | `public/guide/signals-connect-commands.png` | `guide/signals` | … › Show the commands | Connect a source, GitHub: the commands step with the token scope (repo names, read-only permissions), the kubectl secret command and the version-pinned helm upgrade. | No token appears; nothing to redact. |
| 32 | `public/guide/signals-connect-connected.png` | `guide/signals` | … › I've run them | Connect a source, GitHub: the result "Connected · read-only verified · last sweep 0m ago · N observations". | BetaOrg1 is already connected, so this shows within seconds. |
| 33 | `public/guide/signals-sarif-upload.png` | `guide/signals` | #/signals › SARIF upload › Upload | Connect a source, SARIF upload: the file picker and the "Uploaded. N findings created." result. | Upload a real scan, e.g. semgrep or trivy SARIF of a dogfood repo. |
| 34 | `public/guide/stack.png` | `guide/stack` | #/stack | Stack with the Declared · Observed · Verified header, a connected GitHub source slot, the shadow banner, and the Security Plane cards with Observed and Verified lines. | BetaOrg1's GitHub source is connected, so the Observed lines are real. |
| 35 | `public/guide/team.png` | `guide/team` | #/settings/team | Team screen with the invite form open, two members and one pending invite. | Open the invite form; blur real emails. |
| 36 | `public/guide/workspace.png` | `guide/workspace` | #/workspace | Workspace with the gradient run header, the flow canvas (Coordinator connected to DevOps Engineer and Constitution), the chat stream and the tool-call drawer. | Needs a recent run. |
| 37 | `public/guide/activity.png` | `guide/workspace` | #/activity | Activity chat with a /gaps run in progress, Coordinator and Baseline Security turns, and the crew panel on the right. | Run /gaps and capture mid-run. |

## Wiring

- **Getting-started** (`ts-shot--pending` figures): replace the pending figure with `<figure className="ts-shot"><img src="/screenshots/getting-started/NN-name.png" alt="…" /><figcaption>…</figcaption></figure>`.
- **Guide pages** (comment slots): replace the comment with `<img src="/guide/name.png" alt="…" />` at the same spot.
- Or drop the files at the paths above and say so on the PR; wiring them in is one commit.
