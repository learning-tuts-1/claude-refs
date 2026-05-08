# explain-code - Code Explanation

## When to Use
When the user asks for code explanation, function breakdown, or logic walkthrough.

## Format

### 1. Brief Description (1-2 sentences)
What does this code do?

### 2. ASCII Diagram
```
Input → [Process A] → [Process B] → Output
            │
            ▼
       [Side Effect]
```

### 3. Step by Step
```
Step 1: What happens first
Step 2: What happens next
Step 3: What it returns
```

### 4. Gotchas (Potential Issues)
- What to watch out for?
- Edge cases
- Performance considerations

### 5. Analogy (Optional)
Real-world analogy to make it clearer.

## Rules

- **ASCII diagram** is mandatory for data flow
- **Don't oversimplify** - the user is a developer
- **Gotchas section** is mandatory - always point out potential issues
- **Be precise** - mention exact line numbers and variable names

## Example

```
User: "Explain this useEffect"

## What It Does
Fetches products from API on component mount and stores in state.

## Data Flow
```
Component Mount
      │
      ▼
  useEffect()
      │
      ▼
  fetch(/api/products)
      │
      ├─ Success → setProducts(data)
      │
      └─ Error → setError(err)
```

## Steps
1. Component mounts → useEffect fires
2. fetch requests /api/products endpoint
3. On success: products stored in state
4. On error: error stored in state

## Gotchas
- Empty dependency array [] - only runs on mount
- No cleanup - race condition possible on unmount
- No loading state - UI doesn't show loading indicator
```
