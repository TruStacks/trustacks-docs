import type { MetadataRoute } from 'next'

// The /contributing section is the internal, contributor-facing self-hosted
// and local-development docs. It is intentionally kept out of search: the
// public product docs are the hosted getting-started flow. Note this is a
// public static site, so /contributing is soft-hidden (out of nav + crawlers)
// rather than access-controlled.
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: ['/contributing', '/contributing/']
    }
  }
}
