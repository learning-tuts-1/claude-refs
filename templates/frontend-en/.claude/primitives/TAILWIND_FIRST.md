# TAILWIND_FIRST

## Styling Rules

### Core Principle

**Tailwind utility classes ONLY** - no custom CSS, no inline styles.

### Correct vs Incorrect

```tsx
// Correct - Tailwind utilities
<div className="flex items-center gap-4 p-6 bg-card rounded-lg border" />

// Wrong - inline styles
<div style={{ display: 'flex', padding: '24px' }} />

// Wrong - CSS modules
import styles from './Card.module.css'

// Wrong - hardcoded hex values
<div className="bg-[#13D9CC] text-[#333]" />

// Wrong - arbitrary spacing
<div className="p-[17px] mt-[23px]" />
```

### className Merge Pattern

```tsx
import { cn } from '@/lib/utils'

function Card({ className, children }: CardProps) {
  return (
    <div className={cn(
      'rounded-lg border bg-card text-card-foreground p-6',
      className
    )}>
      {children}
    </div>
  )
}
```

### cn() Utility

```typescript
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### Responsive Design

```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" />
<div className="px-4 md:px-8 lg:px-12" />
<h1 className="text-2xl md:text-4xl lg:text-5xl" />
```

### When to Use?

**Always** - no exceptions for any styling.
