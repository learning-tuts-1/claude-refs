# Dependency Graph

## V1 Features

```
                    ┌──────────┐
                    │ Database │
                    └────┬─────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ 01-{{f1}}│ │ 02-{{f2}}│ │ ...      │
        └────┬─────┘ └────┬─────┘ └──────────┘
             │             │
             └──────┬──────┘
                    │
               ┌────▼─────┐
               │ 03-{{f3}}│
               └──────────┘
```

## Legend

- `→` = depends on (must complete first)
- Features at the same level can be built in parallel
- Always start from the top (no dependencies)
