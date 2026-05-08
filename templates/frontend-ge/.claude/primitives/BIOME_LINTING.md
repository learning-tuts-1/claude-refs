# BIOME_LINTING

## რა არის Biome?

**Biome** - all-in-one linter + formatter (Rust-based, 10-20x სწრაფი ESLint-ზე).

## კონფიგურაცია

ფაილი: `biome.json`

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

## ბრძანებები

```bash
npm run lint          # მხოლოდ lint
npm run check         # lint + format + fix
npx biome check --write ./app   # ავტო-fix
```

## Pre-commit Hook (Husky + lint-staged)

`package.json`:
```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "biome check --write --no-errors-on-unmatched"
    ]
  }
}
```

## ხშირი შეცდომები

### noUnusedImports
```tsx
// არასწორი
import { useState, useEffect } from 'react';  // useEffect არ გამოიყენება

// სწორი
import { useState } from 'react';
```

### noExplicitAny
```tsx
// არასწორი
const handleError = (error: any) => { ... }

// სწორი
const handleError = (error: Error) => { ... }
const handleError = (error: unknown) => { ... }
```

### useButtonType
```tsx
// არასწორი
<button onClick={handleClick}>Click</button>

// სწორი
<button type="button" onClick={handleClick}>Click</button>
```
