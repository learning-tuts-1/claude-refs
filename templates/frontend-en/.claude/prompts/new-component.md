# New Component

## Input
- Component name
- Type (ui, layout, feature)
- Props requirements

## Template

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

## Location
- UI: `components/ui/`
- Layout: `components/layout/`
- Feature: `components/[feature]/`

## Checklist
- [ ] forwardRef for UI components
- [ ] cn() for className merging
- [ ] Design tokens (no hardcoded colors)
- [ ] TypeScript strict (Props interface)
- [ ] Semicolons
