# TAILWIND_FIRST

## Styling წესები

### მთავარი პრინციპი

**Tailwind utility classes ONLY** - არა custom CSS, არა inline styles.

### სწორი vs არასწორი

```tsx
// სწორი - Tailwind utilities
<div className="flex items-center gap-4 p-6 bg-card rounded-lg border" />
<button className="bg-primary text-primary-foreground px-4 py-2 rounded-full hover:bg-primary/90" />

// არასწორი - inline styles
<div style={{ display: 'flex', padding: '24px' }} />

// არასწორი - CSS modules
import styles from './Card.module.css'
<div className={styles.card} />

// არასწორი - hardcoded values
<div className="bg-[#13D9CC] text-[#333]" />

// არასწორი - arbitrary values (spacing)
<div className="p-[17px] mt-[23px]" />
```

### className Merge Pattern

```tsx
import { cn } from '@/lib/utils'

interface CardProps {
  className?: string
  children: React.ReactNode
}

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
// Mobile-first
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" />

// Responsive padding
<div className="px-4 md:px-8 lg:px-12" />

// Responsive text
<h1 className="text-2xl md:text-4xl lg:text-5xl" />
```

### Dark Mode

```tsx
// თუ dark mode გჭირდება
<div className="bg-white dark:bg-gray-900" />
<p className="text-gray-900 dark:text-gray-100" />

// უკეთესი - CSS variables (ავტომატური)
<div className="bg-background text-foreground" />
```

### Animation

```tsx
// Transition
<div className="transition-all duration-200 hover:shadow-lg" />

// Transform
<button className="hover:-translate-y-0.5 active:scale-95 transition-transform" />
```

### როდის გამოვიყენო?

**ყოველთვის** - ნებისმიერი styling-ისთვის. გამონაკლისი არ არსებობს.
