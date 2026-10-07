import nextra from 'nextra'

const withNextra = nextra({
  contentDirBasePath: '/',
  search: {
    codeblocks: false
  }
})

export default withNextra({
  reactStrictMode: true,
  poweredByHeader: false,
  async redirects() {
    return [
      {
        source: '/getting-started/quickstart',
        destination: '/getting-started/hosted-quickstart',
        permanent: true
      },
      {
        source: '/getting-started/beta',
        destination: '/getting-started/hosted-quickstart',
        permanent: true
      },
      {
        source: '/getting-started/ways-to-run',
        destination: '/getting-started/how-trustacks-runs',
        permanent: true
      },
      {
        source: '/installation/local-dev',
        destination: '/contributing/local-dev',
        permanent: true
      }
    ]
  }
})
