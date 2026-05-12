import type { Metadata } from 'next'
import Image from 'next/image'
import { Footer, Layout, Navbar } from 'nextra-theme-docs'
import { Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import 'nextra-theme-docs/style.css'
import './globals.css'

export const metadata: Metadata = {
  metadataBase: new URL('https://docs.trustacks.com'),
  title: {
    default: 'TruStacks Docs',
    template: '%s · TruStacks Docs'
  },
  description:
    'Technical documentation for TruStacks. Install the runner, connect a repository, author policy, and integrate with your existing stack.',
  openGraph: {
    title: 'TruStacks Docs',
    description:
      'Technical documentation for TruStacks. Install the runner, connect a repository, author policy, and integrate with your existing stack.',
    url: 'https://docs.trustacks.com',
    siteName: 'TruStacks Docs',
    type: 'website'
  },
  twitter: {
    card: 'summary_large_image',
    title: 'TruStacks Docs',
    description:
      'Technical documentation for TruStacks. Install the runner, connect a repository, author policy, and integrate with your existing stack.'
  },
  robots: { index: true, follow: true }
}

const logo = (
  <span className="flex items-center gap-2">
    <Image
      src="/brand/logo-icon.png"
      alt=""
      width={28}
      height={28}
      priority
    />
    <span style={{ fontWeight: 600, letterSpacing: '-0.01em' }}>
      TruStacks <span style={{ opacity: 0.6, fontWeight: 500 }}>Docs</span>
    </span>
  </span>
)

const navbar = (
  <Navbar
    logo={logo}
    logoLink="/"
    projectLink="https://github.com/TruStacks"
    chatLink="https://trustacks.com"
    chatIcon={
      <span style={{ fontSize: '0.875rem', fontWeight: 500 }}>trustacks.com</span>
    }
  />
)

const footer = (
  <Footer>
    <span style={{ fontSize: '0.875rem', opacity: 0.7 }}>
      © {new Date().getFullYear()} TruStacks. Software delivery generated for
      your stack.
    </span>
  </Footer>
)

export default async function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head />
      <body>
        <Layout
          navbar={navbar}
          pageMap={await getPageMap()}
          docsRepositoryBase="https://github.com/TruStacks/trustacks-docs/tree/main"
          footer={footer}
        >
          {children}
        </Layout>
      </body>
    </html>
  )
}
