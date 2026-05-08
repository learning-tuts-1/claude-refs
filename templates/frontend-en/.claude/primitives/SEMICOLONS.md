# SEMICOLONS

## Rule

**Every statement must end with a semicolon (`;`)**

### Required

```typescript
const [isOpen, setIsOpen] = useState(false);
const ref = useRef<HTMLDivElement>(null);
import { useState } from 'react';
export const Component = () => { };
```

### Exceptions (no semicolon needed)

```typescript
function handleClick() { }
if (condition) { }
interface Props {
  name: string;
}
```

## Automatic Enforcement

Biome auto-fixes: `npm run check`
