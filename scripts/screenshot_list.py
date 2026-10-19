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
    "signals.png": ("#/signals", "Needs at least one finding: upload a SARIF file first."),
    "signals-connect-choose.png": ("#/signals › Connect a source", ""),
    "signals-connect-runner.png": ("#/signals › Connect a source › GitHub", ""),
    "signals-connect-commands.png": ("… › Show the commands", "No token appears; nothing to redact."),
    "signals-connect-connected.png": ("… › I've run them", "BetaOrg1 is already connected, so this shows within seconds."),
    "signals-sarif-upload.png": ("#/signals › SARIF upload › Upload", "Upload a real scan, e.g. semgrep or trivy SARIF of a dogfood repo."),
    "stack.png": ("#/stack", "BetaOrg1's GitHub source is connected, so the Observed lines are real."),
    "workspace.png": ("#/workspace", "Needs a recent run."),
    "activity.png": ("#/activity", "Run /gaps and capture mid-run."),
    "team.png": ("#/settings/team", "Open the invite form; blur real emails."),
}

PLACEHOLDER = re.compile(r"screenshot-placeholder: (.*?) Save as (public/\S+?\.png)")
ASSET = re.compile(r"asset: (public/\S+?\.png)")
CAPTION = re.compile(r"<figcaption>(.*)</figcaption>")
WHERE = re.compile(r"^\*\*Where:\*\* (.*?)(?:\.|;|$)")


def where_line(lines: list[str]) -> str:
    for line in lines:
        m = WHERE.match(line)
        if m:
            return m.group(1).replace("**", "").strip()
    return ""


def main() -> None:
    files = subprocess.run(
        ["git", "ls-files", "app/**/page.mdx"], capture_output=True, text=True, check=True
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
        short = page.removeprefix("app/").removesuffix("/page.mdx")
        out.append(f"| {n} | `{path}` | `{short}` | {where} | {shows} | {note} |")
    out += [
        "",
        "## Wiring",
        "",
        "- **Getting-started** (`ts-shot--pending` figures): replace the pending figure with "
        '`<figure className="ts-shot"><img src="/screenshots/getting-started/NN-name.png" '
        'alt="…" /><figcaption>…</figcaption></figure>`.',
        "- **Guide pages** (comment slots): replace the comment with "
        '`<img src="/guide/name.png" alt="…" />` at the same spot.',
        "- Or drop the files at the paths above and say so on the PR; wiring them in is one commit.",
    ]
    Path("SCREENSHOTS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} slots")


if __name__ == "__main__":
    main()
