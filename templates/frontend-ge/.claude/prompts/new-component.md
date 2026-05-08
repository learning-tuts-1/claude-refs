# ახალი კომპონენტის შექმნა

## Input
- კომპონენტის სახელი
- ტიპი (ui, layout, feature)
- Props-ის მოთხოვნები

## შაბლონი

```tsx
import * as React from 'react';
import { cn } from '@/lib/utils';

export interface {{ComponentName}}Props extends React.HTMLAttributes<HTMLDivElement> {
  // custom props
}

const {{ComponentName}} = React.forwardRef<HTMLDivElement, {{ComponentName}}Props>(
  ({ className, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          'rounded-md border bg-card text-card-foreground',
          className
        )}
        {...props}
      />
    );
  }
);
{{ComponentName}}.displayName = '{{ComponentName}}';

export { {{ComponentName}} };
```

## ადგილმდებარეობა
- UI: `components/ui/`
- Layout: `components/layout/`
- Feature: `components/[feature]/`

## Checklist
- [ ] forwardRef UI კომპონენტებისთვის
- [ ] cn() className merge-ისთვის
- [ ] Design tokens (არა hardcoded ფერები)
- [ ] TypeScript strict (Props interface)
- [ ] Semicolons
