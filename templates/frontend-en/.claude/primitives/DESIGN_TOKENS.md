# DESIGN_TOKENS

## Design System

### Colors

| Token | Usage |
|-------|-------|
| `background` | Page background |
| `foreground` | Primary text |
| `primary` | Buttons, links, CTA |
| `secondary` | Secondary accent |
| `muted` | Secondary surfaces |
| `muted-foreground` | Secondary text |
| `card` / `card-foreground` | Cards |
| `destructive` | Errors, delete actions |
| `border` | Borders |

### Usage Rules

```tsx
// Correct - Design tokens
<div className="bg-background text-foreground" />
<button className="bg-primary hover:bg-primary/90 text-primary-foreground" />
<p className="text-muted-foreground" />

// Wrong - Hardcoded values
<div style={{ background: '#f1f1f1' }} />
<div className="bg-[#F9A80C]" />
<div className="text-gray-500" />
```

### Spacing (4px base)

```tsx
// Correct
<div className="p-4 gap-2" />

// Wrong
<div className="p-[15px]" />
<div style={{ padding: '17px' }} />
```

### Typography

| Element | Classes |
|---------|---------|
| Headlines | `font-serif text-4xl font-bold` |
| Body | `font-sans text-base` |
| UI Labels | `font-sans text-sm font-medium` |
| Caption | `text-xs text-muted-foreground` |

### WCAG AA Compliance

- **Text contrast:** 4.5:1 minimum
- **UI contrast:** 3:1 minimum
- **Touch targets:** 44x44px minimum
- **Focus states:** visible ring on all interactive elements

```tsx
<button className="focus-visible:ring-2 focus-visible:ring-primary" />
```

### When to Use?

**Always** - every styling decision should use design tokens only.
