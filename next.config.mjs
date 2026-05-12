import nextra from 'nextra'

const withNextra = nextra({
  contentDirBasePath: '/',
  search: {
    codeblocks: false
  }
})

export default withNextra({
  reactStrictMode: true,
  poweredByHeader: false
})
