# FORWARDREF_COMPONENT

## UI კომპონენტის შაბლონი

ყველა reusable UI კომპონენტი **forwardRef**-ით უნდა იყოს.

### შაბლონი

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

### რატომ forwardRef?

1. **Ref forwarding** - მშობელ კომპონენტს შეუძლია DOM-ზე წვდომა
2. **Composition** - სხვა კომპონენტებში ჩასმა
3. **3rd party** - animation ბიბლიოთეკებთან თავსებადობა

### Variant Pattern (cva)

```tsx
import { cva, type VariantProps } from 'class-variance-authority';

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:ring-2',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
      },
      size: {
        sm: 'h-9 px-3 text-sm',
        md: 'h-10 px-4',
        lg: 'h-11 px-8 text-lg',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'md',
    },
  }
);

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  isLoading?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, isLoading, children, ...props }, ref) => (
    <button
      ref={ref}
      className={cn(buttonVariants({ variant, size }), className)}
      disabled={isLoading}
      {...props}
    >
      {isLoading ? <Spinner /> : children}
    </button>
  )
);
Button.displayName = 'Button';
```

### ფაილის ადგილმდებარეობა

- UI კომპონენტები: `components/ui/`
- Layout: `components/layout/`
- Feature-specific: `components/[feature]/`

### როდის გამოვიყენო?

**ყოველთვის** - ყველა reusable UI კომპონენტისთვის.
Feature კომპონენტებისთვის (რომლებიც არ გამოიყენება სხვაგან) forwardRef არ არის სავალდებულო.
