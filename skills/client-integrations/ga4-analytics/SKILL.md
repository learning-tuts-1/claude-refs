---
name: ga4-analytics
description: Google Analytics 4 event tracking — page views, e-commerce events, custom events. Use when implementing analytics or tracking user actions.
---

# Google Analytics 4

GA4 event tracking — page views, e-commerce, custom events.

## Key Concepts

- **AnalyticsService** — singleton, consent-gated (`hasConsent()`)
- **Page views** — tracked via router location hook
- **E-commerce flow** — `view_item` -> `add_to_cart` -> `begin_checkout` -> `purchase`
- **Consent** — CookieConsent component sets `analytics_consent` in localStorage
- **Debug mode** — `debug_mode: true` in dev environment

## Event Naming

| Category | Events |
|----------|--------|
| E-commerce | `view_item`, `add_to_cart`, `purchase` |
| Navigation | `page_view` |
| Search | `search` |
| Custom | app-specific events |
