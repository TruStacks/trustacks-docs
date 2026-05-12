# trustacks-docs

Technical documentation for [TruStacks](https://trustacks.com), served at
[docs.trustacks.com](https://docs.trustacks.com).

Marketing and positioning live at `trustacks.com` (the `trustacks-www`
repository). The product itself lives in `trustacks-mvp`. This repository is
the technical reference: install, configure, integrate, author policy.

## Stack

- [Next.js 15](https://nextjs.org) (App Router) + TypeScript
- [Nextra v4](https://nextra.site) (`nextra-theme-docs`) for MDX-based docs
- [Pagefind](https://pagefind.app) for static search
- Vercel for hosting

## Local development

```bash
npm install
npm run dev
```

The dev server runs at <http://localhost:3000>.

## Repository layout

```
app/
  layout.tsx                Nextra Layout at root (owns html/body)
  page.mdx                  Overview / landing
  _meta.js                  Top-level sidebar order
  getting-started/          Install runner, first PR
  installation/             Local dev, cluster deploy, secrets, GitOps
  workshops/                Guided walkthroughs
  reference/                Architecture, constitution, Specialist Packs, CLI, MCP, linter
public/
  brand/                    Logos (mirrored from trustacks-www)
mdx-components.tsx          Nextra MDX components
next.config.mjs             withNextra wrap
```

## Contributing

PR-only on `main`. Conventional-commit messages with a path scope:

```
docs(getting-started): add prerequisites
feat(reference): document MCP server integration
fix(installation): correct ArgoCD command
chore(theme): bump nextra to 4.7
```

CodeRabbit reviews every PR. Triage each comment and reply inline with the
commit hash that addressed it before requesting merge.

Voice rules live in [`CLAUDE.md`](./CLAUDE.md) and the canonical
[`SITE_BRIEF.md`](../trustacks-www/SITE_BRIEF.md) in `trustacks-www`. The
load-bearing line: **coworker, not replacement.** Agents propose. Policy
decides. Humans approve.
