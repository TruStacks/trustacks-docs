import { ImageResponse } from 'next/og'

export const runtime = 'edge'
export const alt = 'TruStacks Docs · Software delivery generated for your stack'
export const size = { width: 1200, height: 630 }
export const contentType = 'image/png'

export default async function OpenGraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          background: '#0F172A',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          padding: '72px 88px',
          fontFamily: 'system-ui, -apple-system, "Segoe UI", sans-serif',
          color: '#E2E8F0'
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '20px',
            fontSize: '40px',
            fontWeight: 600,
            letterSpacing: '-0.01em',
            color: '#FFFFFF'
          }}
        >
          <div
            style={{
              width: '14px',
              height: '56px',
              background: '#10B981',
              borderRadius: '4px'
            }}
          />
          TruStacks <span style={{ opacity: 0.6, fontWeight: 500 }}>Docs</span>
        </div>

        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '24px'
          }}
        >
          <div
            style={{
              fontSize: '78px',
              fontWeight: 700,
              lineHeight: 1.05,
              letterSpacing: '-0.02em',
              color: '#FFFFFF',
              maxWidth: '900px'
            }}
          >
            Software delivery generated for your stack.
          </div>
          <div
            style={{
              fontSize: '32px',
              lineHeight: 1.3,
              color: '#94A3B8',
              maxWidth: '900px'
            }}
          >
            Agents propose. Policy decides. Humans approve.
          </div>
        </div>

        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-end',
            fontSize: '24px',
            color: '#94A3B8'
          }}
        >
          <div>docs.trustacks.com</div>
          <div style={{ color: '#10B981', fontWeight: 600 }}>
            Beta · 2026
          </div>
        </div>
      </div>
    ),
    { ...size }
  )
}
