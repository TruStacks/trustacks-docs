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
        destination: '/contributing/self-hosted-quickstart',
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
