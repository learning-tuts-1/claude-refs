---
name: tailwind-v4
description: Tailwind CSS v4 patterns with CSS-first configuration and @theme design tokens. Use when styling components, working with colors/spacing/typography, or applying design system tokens.
---

# Tailwind CSS v4

CSS-first configuration, @theme design tokens, utility-first patterns.

## CSS-First Configuration

Tailwind v4 uses CSS instead of `tailwind.config.js`:

```css
@import "tailwindcss";

@theme {
  --color-background: hsl(220, 20%, 4%);
  --color-surface: hsl(220, 18%, 8%);
  --color-foreground: hsl(220, 10%, 94%);
  --color-muted: hsl(220, 10%, 55%);
  --color-brand: hsl(175, 85%, 46%);
  --color-destructive: hsl(0, 84%, 60%);
  --color-success: #10b981;
  --color-warning: #f59e0b;

  --font-sans: 'Inter', system-ui, sans-serif;
  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --duration-fast: 150ms;
  --duration-normal: 250ms;
}
```

## Rules

- Design tokens only, no hardcoded colors: `bg-brand` not `bg-[#13D9CC]`
- Spacing scale: `p-4` not `p-[15px]`
- No inline styles, no `!important`, no arbitrary values
- Use `cn()` helper for conditional classes
- Mobile-first responsive: `md:`, `lg:`, `xl:`
- No `@apply` in components — utility classes directly in JSX

## cn() Utility

```typescript
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

## Common Mistakes

```tsx
// Wrong — hardcoded colors
<div className="bg-[#0a0a0a] text-[#e5e5e5]" />

// Correct — design tokens
<div className="bg-background text-foreground" />

// Wrong — arbitrary spacing
<div className="p-[17px] gap-[7px]" />

// Correct — spacing scale
<div className="p-4 gap-2" />

// Wrong — inline styles
<div style={{ backgroundColor: '#141414' }} />

// Correct — Tailwind class
<div className="bg-surface" />
```

## Responsive Design

```tsx
<div className={cn(
  "p-4",          // Mobile
  "md:p-6",       // Tablet
  "lg:p-8"        // Desktop
)}>
  <div className="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
    {/* items */}
  </div>
</div>
```
