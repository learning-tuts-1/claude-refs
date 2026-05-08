# DESIGN_TOKENS

## Design System

### ფერები

| Token | გამოყენება |
|-------|------------|
| `background` | გვერდის ფონი |
| `foreground` | მთავარი ტექსტი |
| `primary` | ღილაკები, ლინკები, CTA |
| `secondary` | მეორეხარისხოვანი აქცენტი |
| `muted` | მეორეხარისხოვანი ზედაპირები |
| `muted-foreground` | მეორეხარისხოვანი ტექსტი |
| `card` / `card-foreground` | ბარათები |
| `destructive` | შეცდომები, წაშლა |
| `border` | ბორდერები |

### გამოყენების წესები

```tsx
// სწორი - Design tokens
<div className="bg-background text-foreground" />
<button className="bg-primary hover:bg-primary/90 text-primary-foreground" />
<p className="text-muted-foreground" />
<div className="border border-border rounded-lg" />

// არასწორი - Hardcoded values
<div style={{ background: '#f1f1f1' }} />
<div className="bg-[#F9A80C]" />
<div className="text-gray-500" />
```

### Spacing (4px base)

| Token | Value | გამოყენება |
|-------|-------|------------|
| `p-1` | 4px | Tight spacing |
| `p-2` | 8px | Small elements |
| `p-4` | 16px | Standard padding |
| `p-6` | 24px | Card padding |
| `p-8` | 32px | Section spacing |
| `gap-2` | 8px | Element gaps |
| `gap-4` | 16px | Standard gaps |

```tsx
// სწორი
<div className="p-4 gap-2" />

// არასწორი
<div className="p-[15px]" />
<div style={{ padding: '17px' }} />
```

### Typography

| Element | Classes |
|---------|---------|
| Headlines | `font-serif text-4xl font-bold` |
| Body | `font-sans text-base` |
| UI Labels | `font-sans text-sm font-medium` |
| Small/Caption | `text-xs text-muted-foreground` |

### Border Radius

| Token | Value |
|-------|-------|
| `rounded-sm` | 4-6px |
| `rounded` / `rounded-md` | 8px |
| `rounded-lg` | 12px |
| `rounded-xl` | 16px |
| `rounded-full` | 9999px |

### Shadows

```tsx
<div className="shadow-sm" />   // Subtle
<div className="shadow-md" />   // Cards
<div className="shadow-lg" />   // Modals
```

### WCAG AA Compliance

- **ტექსტის კონტრასტი:** 4.5:1 მინიმუმ
- **UI კონტრასტი:** 3:1 მინიმუმ
- **Touch targets:** 44x44px მინიმუმ
- **Focus states:** ყველა interactive ელემენტზე

```tsx
<button className="focus-visible:ring-2 focus-visible:ring-primary" />
```

### როდის გამოვიყენო?

**ყოველთვის** - ნებისმიერი სტილის გამოყენებისას, მხოლოდ design tokens.
