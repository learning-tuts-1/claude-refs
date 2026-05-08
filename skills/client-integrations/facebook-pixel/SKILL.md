---
name: facebook-pixel
description: Facebook/Meta Pixel for conversion tracking, retargeting audiences, and e-commerce events. Use when implementing Facebook tracking or ad conversion.
---

# Facebook Pixel

Conversion tracking, retargeting, and lookalike audiences.

## Key Concepts

- **FacebookPixelService** — singleton, consent-gated (`marketing_consent`)
- **Standard events** — `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`, `Lead`, `Search`
- **Custom events** — app-specific events (e.g., `StudioOpen`, `AudioPreview`)
- **Page views** — tracked via router's location hook
- **E-commerce flow** — `ViewContent` -> `AddToCart` -> `InitiateCheckout` -> `Purchase`

## Retargeting Audiences

| Audience | Event | Window |
|----------|-------|--------|
| Site visitors | PageView | 180 days |
| Product viewers | ViewContent | 30 days |
| Cart abandoners | AddToCart (no Purchase) | 14 days |
| Purchasers | Purchase | 180 days |
