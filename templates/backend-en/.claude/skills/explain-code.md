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
User: "Explain this middleware"

## What It Does
Validates JWT Token on every request and adds User claims to HttpContext.

## Flow
```
HTTP Request
     │
     ▼
[Read Authorization Header]
     │
     ├─ No Token → 401 Unauthorized
     │
     ▼
[Validate JWT]
     │
     ├─ Invalid/Expired → 401
     │
     ▼
[Extract Claims]
     │
     ▼
[Set HttpContext.User]
     │
     ▼
next(context) → Controller
```

## Steps
1. Reads Authorization header from request
2. If no token, returns 401 immediately
3. Validates JWT signature and expiration
4. Extracts user claims (UserId, Role, etc.)
5. Sets HttpContext.User for downstream use
6. Calls next middleware/controller

## Gotchas
- Token expired → refresh token flow should trigger on client
- ClaimTypes.NameIdentifier → UserId, not UserName
- Middleware order matters - Auth must come after CORS
```
