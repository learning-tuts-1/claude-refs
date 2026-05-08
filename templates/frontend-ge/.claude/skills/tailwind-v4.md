# Tailwind CSS v4 - სქილი

## CSS-First კონფიგურაცია

Tailwind v4-ში `tailwind.config.js` აღარ არის. ყველაფერი CSS-შია.

### Theme კონფიგურაცია

```css
/* app.css */
@import "tailwindcss";

@theme {
  /* ფერები */
  --color-primary: oklch(0.7 0.15 180);
  --color-secondary: oklch(0.6 0.12 30);
  --color-background: oklch(0.98 0 0);
  --color-foreground: oklch(0.15 0 0);
  --color-muted: oklch(0.93 0 0);
  --color-muted-foreground: oklch(0.55 0 0);
  --color-destructive: oklch(0.55 0.2 25);

  /* ფონტები */
  --font-heading: "{{HEADING_FONT}}", serif;
  --font-body: "{{BODY_FONT}}", sans-serif;

  /* სპეისინგი */
  --spacing-section: 5rem;

  /* ბორდერ რადიუსი */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;

  /* ანიმაცია */
  --animate-fade-in: fade-in 0.3s ease-out;
}

@keyframes fade-in {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Design Token-ების გამოყენება

```tsx
// სწორი - design tokens
<div className="bg-background text-foreground" />
<button className="bg-primary hover:bg-primary/90" />
<p className="text-muted-foreground text-sm" />

// არასწორი - hardcoded
<div style={{ background: '#f1f1f1' }} />
<div className="bg-[#FF0000]" />
```

## კომპონენტის პატერნები

### Button
```tsx
<button className="bg-primary text-primary-foreground px-4 py-2 rounded-md
  hover:bg-primary/90 transition-colors font-medium">
```

### Card
```tsx
<div className="bg-card text-card-foreground rounded-lg border p-6 shadow-sm">
```

### Input
```tsx
<input className="w-full rounded-md border border-input bg-background px-3 py-2
  text-sm placeholder:text-muted-foreground focus:outline-none focus:ring-2
  focus:ring-primary/20" />
```

## Responsive Design

```tsx
// Mobile-first
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

// Container
<div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
```

## Dark Mode

```css
@theme {
  --color-background: oklch(0.98 0 0);
  --color-foreground: oklch(0.15 0 0);
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-background: oklch(0.12 0 0);
    --color-foreground: oklch(0.95 0 0);
  }
}
```

## cn() Helper

```typescript
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]): string {
  return twMerge(clsx(inputs));
}
```

## წესები

- **@theme** - ყველა custom value @theme ბლოკში
- **oklch** - ფერებისთვის oklch ფორმატი (უკეთესი interpolation)
- **არა arbitrary values** - `bg-[#hex]` ნაცვლად @theme-ში დაამატე
- **არა @apply** - utility classes პირდაპირ JSX-ში
- **Design tokens** - ფერები, ფონტები, spacing ყოველთვის token-ებით
