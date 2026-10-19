"""Regenerate SCREENSHOTS.md from the screenshot slots in the pages.

Slots: `{/* screenshot-placeholder: <what it shows> Save as <path>.png */}` on
guide pages, and `{/* asset: <path>.png */}` followed by a pending
`<figure>` caption on getting-started pages. Run from the repo root:

    python3 scripts/screenshot_list.py
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

# Where to find the screen, and what state it needs, keyed by file name.
NOTES: dict[str, tuple[str, str]] = {
    "workspace-rule-draft.png": ("#/activity, after `/rule new <description>`", "Click \"Would it have blocked my recent proposals?\" and wait for the result."),
    "signals-fix-card.png": ("#/signals, a finding after Propose a fix", "Wait for the verdict; expand one file under The change."),
    "workshop-signals-upload.png": ("#/signals › SARIF upload › Upload", "Use public/samples/dockerfile-root.sarif with your repo name."),
    "workshop-signals-verdict.png": ("#/signals, the workshop finding", "After Propose a fix finishes (about two minutes)."),
    "workshop-policy-impact.png": ("#/activity, a finished rule draft", "After the impact check returns."),
    "01-register.png": ("auth.trustacks.com sign-in", "Signed out."),
    "02-team-profile.png": ("#/onboarding, step 1", ""),
    "03-enroll-runner.png": ("#/settings/runners, or onboarding step 2", "Redact the token, including inside the command."),
    "04-create-application.png": ("#/applications", "A name typed, before pressing Create."),
    "05-connect-repo.png": ("Applications › Connect a repo", ""),
    "06-declare-profile.png": ("#/onboarding, step 4", ""),
    "07-llm-provider.png": ("#/settings/llm", "Key masked (sk-ant…)."),
    "08-first-analysis.png": ("A service › Run a new analysis", "Capture while it streams."),
    "09-promote-proposal.png": ("Analysis › Promote to proposal", "Needs a proposal that reaches pr_opened."),
    "10-pr-and-ci.png": ("GitHub: the platform-repo PR", "Outside the app; crop to the PR body and checks."),
    "11-argocd-synced.png": ("Your ArgoCD UI", "Outside the app."),
    "gap-analyses.png": ("#/gaps", "BetaOrg1 has several runs; pick betaorg1-dogfood in the Application picker if shown."),
    "gap-analysis-detail.png": ("`#/gaps/<run id>`", "Open a completed run; the report is below the Activity log."),
    "01-overview.png": ("#/ (Overview)", "Needs at least one completed gap analysis for the maturity badge."),
    "02-stack.png": ("#/stack", "BetaOrg1's GitHub source is connected, so the Observed lines are real."),
    "03-application-detail.png": ("#/applications › Manage on betaorg1-dogfood", "Both member services and the platform repo bound."),
    "04-analysis.png": ("`#/services/<id>` › Run analysis, then the run at `#/analyses/<id>`", "Run on betaorg1-dogfood-service at main; capture after it reaches done."),
    "05-gap-analysis.png": ("#/gaps › Run new gap analysis, then `#/gaps/<run id>`", "Choose betaorg1-dogfood; capture after done so the report shows."),
    "06-maturity.png": ("#/maturity", "Reads the gap analysis from stop 5; bronze tier."),
    "07-proposal.png": ("`#/services/<id>` › Analyses › promote → › Promote to proposal; lands on `#/proposals/<id>`", "Needs a done analysis. If the run ends with nothing to change, no PR opens; use an earlier proposal that opened one."),
    "07-github-pr.png": ("GitHub: the PR in betaorg1-dogfood-platform", "Outside the app; crop to the PR body. Leave it open, do not merge for the shot."),
    "08-rules.png": ("#/rules/practice.workflow_has_test_step", "Source filter Constitution; hosted shows constitution rules only."),
    "09-signals.png": ("#/signals", "Needs at least one finding: upload a SARIF file first if the list is empty. Select an untriaged finding."),
    "10-compliance.png": ("#/compliance", "Needs recorded events in the last 90 days (any analysis, proposal or gap analysis)."),
    "10-audit-report.png": ("#/compliance › Download an audit report (PDF) → (#/audit)", "SOC2, PDF, default 7-day window; capture the confirmation after Generate report."),
    "signals.png": ("#/signals", "Needs at least one finding: upload a SARIF file first."),
    "signals-connect-choose.png": ("#/signals › Connect a source", ""),
    "signals-connect-runner.png": ("#/signals › Connect a source › GitHub", ""),
    "signals-connect-commands.png": ("… › Show the commands", "No token appears; nothing to redact."),
    "signals-connect-connected.png": ("… › I've run them", "BetaOrg1 is already connected, so this shows within seconds."),
    "signals-sarif-upload.png": ("#/signals › SARIF upload › Upload", "Upload a real scan, e.g. semgrep or trivy SARIF of a dogfood repo."),
    "stack.png": ("#/stack", "BetaOrg1's GitHub source is connected, so the Observed lines are real."),
    "workspace.png": ("#/activity", "Ask \"Why am I bronze, and what would get me to silver?\" and wait for the answer."),
    "team.png": ("#/settings/team", "Open the invite form; blur real emails."),
}

PLACEHOLDER = re.compile(r"screenshot-placeholder: (.*?) Save as (public/\S+?\.png)")
ASSET = re.compile(r"asset: (public/\S+?\.png)")
CAPTION = re.compile(r"<figcaption>(.*)</figcaption>")
WHERE = "**Where:** "


def first_clause(text: str) -> str:
    """Text up to the first sentence break (`. ` / `; ` / end) outside backticks.

    Routes such as `#/gaps/<id>` or `#/rules/<rule_id>` must survive whole, so
    a `.` or `;` inside a code span never ends the clause.
    """
    in_code = False
    for i, ch in enumerate(text):
        if ch == "`":
            in_code = not in_code
        elif not in_code and ch in ".;" and (i + 1 == len(text) or text[i + 1] == " "):
            return text[:i]
    return text


def where_line(lines: list[str]) -> str:
    """The page's **Where:** paragraph (joined across wrapped lines), first clause only."""
    for i, line in enumerate(lines):
        if line.startswith(WHERE):
            para = [line[len(WHERE) :]]
            for nxt in lines[i + 1 :]:
                if not nxt.strip():
                    break
                para.append(nxt.strip())
            return first_clause(" ".join(para)).replace("**", "").strip()
    return ""


def main() -> None:
    files = subprocess.run(
        ["git", "ls-files", "app/page.mdx", "app/**/page.mdx"], capture_output=True, text=True, check=True
    ).stdout.split()
    rows: list[tuple[str, str, str]] = []
    for f in files:
        lines = Path(f).read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if m := PLACEHOLDER.search(line):
                rows.append((m.group(2), f, m.group(1).strip()))
            elif m := ASSET.search(line):
                cap = next((c.group(1) for c in map(CAPTION.search, lines[i : i + 4]) if c), "")
                rows.append((m.group(1), f, cap))
    out = [
        "# Screenshot shot list",
        "",
        "Every screenshot slot on the site, generated from the slots in the pages by "
        "`scripts/screenshot_list.py` (rerun it after adding or moving a slot). Capture as "
        "**BetaOrg1** on app.trustacks.com unless noted, and save each PNG at the exact path.",
        "",
        "**Capture specs:** PNG, @2x if you can, cropped to the panel the caption names "
        "(about 1200–1600 px of content), one theme for the whole set. **Redact** enrollment "
        "tokens, API keys, real customer emails and private org/repo names: these ship to "
        "the public site.",
        "",
        "| # | Save as | Page | Where in the app | Shows | Setup / notes |",
        "|---|---|---|---|---|---|",
    ]
    for n, (path, page, shows) in enumerate(rows, 1):
        name = path.rsplit("/", 1)[-1]
        where, note = NOTES.get(name, ("", ""))
        if not where:
            where = where_line(Path(page).read_text(encoding="utf-8").splitlines())
        short = page.removeprefix("app/").removesuffix("page.mdx").rstrip("/") or "index"
        out.append(f"| {n} | `{path}` | `{short}` | {where} | {shows} | {note} |")
    out += [
        "",
        "## Wiring",
        "",
        "- Every slot is a visible `ts-shot--pending` box on its page (with a `Save as` line) "
        "under a comment the generator reads. To ship one, keep the comment, then replace the "
        "box with `<figure className=\"ts-shot\"><img src=\"/…/name.png\" alt=\"…\" />"
        "<figcaption>…</figcaption></figure>` (drop `ts-shot--pending` and the `Save as` line).",
        "- Or drop the files at the paths above and say so on the PR; wiring them in is one commit.",
    ]
    Path("SCREENSHOTS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} slots")


if __name__ == "__main__":
    main()
