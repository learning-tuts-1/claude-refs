# SEMICOLONS

## წესი

**ყველა statement უნდა დამთავრდეს წერტილ-მძიმით (`;`)**

### აუცილებელია semicolon

```typescript
const [isOpen, setIsOpen] = useState(false);
const ref = useRef<HTMLDivElement>(null);
const value = useMemo(() => compute(), [deps]);
const handler = useCallback(() => { }, []);
import { useState } from 'react';
export const Component = () => { };
```

### გამონაკლისები (არ სჭირდება semicolon)

```typescript
// ფუნქციის დეკლარაცია
function handleClick() {
  // ...
}

// if/for/while blocks
if (condition) {
  // ...
}

// interface/type (მაგრამ property-ებს სჭირდება)
interface Props {
  name: string;
  onClick: () => void;
}
```

## ავტომატური enforcement

**Biome** ავტომატურად ამატებს:
```bash
npm run check   # გაასწორებს ავტომატურად
```
