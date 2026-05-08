# FORWARDREF_COMPONENT

## UI Component Template

Every reusable UI component must use **forwardRef**.

### Template

```tsx
import * as React from 'react';
import { cn } from '@/lib/utils';

export interface {{ComponentName}}Props extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'elevated';
}

const {{ComponentName}} = React.forwardRef<HTMLDivElement, {{ComponentName}}Props>(
  ({ className, variant = 'default', ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'rounded-lg border bg-card text-card-foreground',
        variant === 'elevated' && 'shadow-md',
        className
      )}
      {...props}
    />
  )
);
{{ComponentName}}.displayName = '{{ComponentName}}';

export { {{ComponentName}} };
```

### Why forwardRef?

1. **Ref forwarding** - parent can access DOM
2. **Composition** - embeddable in other components
3. **3rd party** - compatible with animation libraries

### File Location

- UI components: `components/ui/`
- Layout: `components/layout/`
- Feature: `components/[feature]/`

### When to Use?

**Always** for reusable UI components.
Feature-only components don't require forwardRef.
