# BIOME_LINTING

## What is Biome?

**Biome** - all-in-one linter + formatter (Rust-based, 10-20x faster than ESLint).

## Configuration

File: `biome.json`

```json
{
  "$schema": "https://biomejs.dev/schemas/2.0.0/schema.json",
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "correctness": {
        "noUnusedImports": "error",
        "noUnusedVariables": "warn"
      },
      "suspicious": {
        "noExplicitAny": "error"
      }
    }
  },
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2
  },
  "javascript": {
    "formatter": {
      "semicolons": "always",
      "quoteStyle": "single"
    }
  }
}
```

## Commands

```bash
npm run lint          # lint only
npm run check         # lint + format + fix
npx biome check --write ./app   # auto-fix
```

## Common Errors

### noUnusedImports
```tsx
// Wrong
import { useState, useEffect } from 'react';  // useEffect unused

// Correct
import { useState } from 'react';
```

### noExplicitAny
```tsx
// Wrong
const handleError = (error: any) => { ... }

// Correct
const handleError = (error: unknown) => { ... }
```

### useButtonType
```tsx
// Wrong
<button onClick={handleClick}>Click</button>

// Correct
<button type="button" onClick={handleClick}>Click</button>
```
