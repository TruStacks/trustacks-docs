# Contributing to trustacks-docs

This repository is the technical documentation hub for TruStacks, served
at [docs.trustacks.com](https://docs.trustacks.com). Marketing and
positioning live at `trustacks.com`; the product itself lives in
`trustacks-mvp`. This repository is the technical reference.

Pull requests are welcome. The conventions below keep the docs
consistent, accurate, and on-voice.

## How to file work

- **Found a bug or stale content?** Open an issue with the *Documentation
  bug* template.
- **Topic isn't covered?** Open an issue with the *Documentation gap*
  template.
- **Proposing a new section or page?** Open an issue with the *Feature
  request* template.

## Setting up locally

```bash
git clone https://github.com/TruStacks/trustacks-docs.git
cd trustacks-docs
npm install
npm run dev
```

The dev server runs at <http://localhost:3000>. Hot reload works for
both MDX content and theme overrides.

Before opening a PR:

```bash
npm run build       # full Next.js + Nextra build + Pagefind index
npm run typecheck   # tsc against the TypeScript config
```

## Conventions

### Branch and commit format

- **Branch off `main`, target `main`.** No stacked PRs. CodeRabbit's
  auto-review skips PRs targeting non-default branches.
- **One slice = one focused PR.** No bundling unrelated changes.
- **Conventional commits with a path scope**, matching what `main`'s
  history shows:
  ```
  docs(reference): expand architecture from skeleton to full reference
  docs(installation): correct GitOps repo layout
  fix(vercel): force framework preset to nextjs
  chore: gitignore .claude/ session state
  ```

### MDX style

- **Frontmatter is required.** Every `page.mdx` declares `title:` and
  `description:`.
- **Sentence-case headings.** No trailing periods on `H1` / `H2` /
  `H3`.
- **Tag fenced code blocks** with a language. `text` is acceptable
  for ASCII diagrams.
- **Use Nextra `<Callout>`** for Note / Tip / Warning / Error
  admonitions, not blockquote-driven workarounds.

### Voice rules (load-bearing)

These come from `SITE_BRIEF.md` in `trustacks-www`. They are
non-negotiable.

- **Coworker, not replacement.** The product replaces toil, not people.
  Reject phrasing that drifts toward autonomy-first language.
- **The canonical three-beat: *Agents propose. Policy decides. Humans
  approve.*** *"Decides"*, never *"disposes."*
- **Specialist Pack** is the canonical term. *"Practice Pack"* and
  *"compliance pack"* are retired.
- **No em-dashes** in customer-facing copy. Use periods, colons,
  commas, or parentheses. The interpunct (`·`) is the brand-rhythm
  separator and is preserved.
- **No emojis as decoration.** No fake-typing animations for agents.
- **Concrete numbers, not adjectives.** *"30-second analysis on a
  50-service repo"* beats *"fast."*

When in doubt, read `SITE_BRIEF.md` in `trustacks-www`.

### Anti-patterns

- *"Fully autonomous"*, *"set it and forget it"*, *"self-driving
  software delivery"* — autonomy-first framing.
- *"Replace your DevOps team"*, *"replace engineers"* — replacement
  framing.
- *"Practice Pack"*, *"Practice rules"*, *"compliance pack"* —
  retired terminology.

## Review process

Every PR gets reviewed by **CodeRabbit**. The auto-review fires on
PRs targeting `main`. After CodeRabbit posts:

- **Triage each comment.** Either fix the issue, or reply explaining
  why the comment doesn't apply.
- **Reply inline with the commit hash** that addressed the comment
  (e.g., *"Fixed in `abc1234`. Reworded the intro to ..."*).
- **Wait for CodeRabbit to acknowledge** the fix before requesting
  merge.

If CodeRabbit hits rate limits or credits are exhausted, surface that
to the user; merging without review is a per-PR judgment call.

## Repository layout

```text
app/
  layout.tsx                  Nextra Layout at root (owns html/body)
  page.mdx                    Overview / landing
  opengraph-image.tsx         OG share card generated at build time
  _meta.js                    Top-level sidebar order
  getting-started/            Install runner, first PR
  installation/               Local dev, cluster deploy, secrets, GitOps
  workshops/                  Guided walkthroughs
  reference/                  Architecture, constitution, Specialist Packs, CLI, MCP, linter
  concepts/                   Positioning and ecosystem fit
public/
  brand/                      Logos (mirrored from trustacks-www)
.github/
  ISSUE_TEMPLATE/             Bug, gap, feature request forms
mdx-components.tsx            Nextra MDX components
next.config.mjs               withNextra wrap
vercel.json                   Framework: nextjs (explicit; do not remove)
```

## Cross-repo boundaries

The docs site is one of three repositories in the TruStacks family:

- **`trustacks-docs`** (this repo) · technical reference, served at
  `docs.trustacks.com`
- **`trustacks-www`** · marketing site, served at `trustacks.com`
- **`trustacks-mvp`** · the product itself

When a positioning beat is needed, lift it from
`trustacks-www/SITE_BRIEF.md`, do not invent. When technical detail is
needed, lift from `trustacks-mvp/PROJECT_BRIEF.md`. If the two
disagree, the canon (PROJECT_BRIEF) wins for product behavior;
SITE_BRIEF wins for voice and naming.

## What this repo will never do

- **Sell anything.** Pricing lives at `trustacks.com/pricing`. Link
  there, do not replicate.
- **Substitute for marketing voice.** Positioning is owned by
  `trustacks-www`.
- **Host customer data.** No accounts, no logins, no personalization.
- **Link to internal or private resources.** All links public.

## Code of conduct

Be kind. Disagree with the work, not the person. Assume good intent.
