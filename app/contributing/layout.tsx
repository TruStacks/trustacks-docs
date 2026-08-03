import type { ReactNode } from 'react'

// Keeps the contributor section out of site search. `app/robots.ts` hides
// /contributing from crawlers, but Pagefind indexes every built HTML page,
// so search would still surface it. `data-pagefind-ignore="all"` drops this
// subtree (content and metadata) from the index at postbuild time. Scoping
// it to a nested layout beats a Pagefind glob allowlist, which would
// silently drop any newly added public section from search.
export default function ContributingLayout({
  children
}: {
  children: ReactNode
}) {
  return <div data-pagefind-ignore="all">{children}</div>
}
