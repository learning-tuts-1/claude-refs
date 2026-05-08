# Project Plan

## V1 - MVP Features

| # | Feature | Priority | Status | Dependencies |
|---|---------|----------|--------|--------------|
| 01 | {{Feature 1}} | Critical | Not Started | - |
| 02 | {{Feature 2}} | Critical | Not Started | 01 |
| 03 | {{Feature 3}} | High | Not Started | 01, 02 |

## Build Order

```
Phase A (no dependencies):
  [01-{{feature1}}: backend]

Phase B (depends on Phase A):
  [01-{{feature1}}: frontend]
  [02-{{feature2}}: backend]

Phase C:
  [02-{{feature2}}: frontend]
  [03-{{feature3}}]
```

## Rules

- Plan mode = only planning, no implementation
- One task at a time
- Each task = one commit
- Mark [x] in PLAN.md after each task
- Read PLAN.md at the start of every new session
