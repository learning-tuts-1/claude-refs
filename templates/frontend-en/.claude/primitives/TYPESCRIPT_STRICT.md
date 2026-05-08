# TYPESCRIPT_STRICT

## TypeScript Strict Mode Rules

### Forbidden Patterns

```typescript
// Never use any
const data: any = response.data
// Correct
const data: ProductResponse = response.data

// Never use @ts-ignore
// @ts-ignore
someFunction()
// Correct - fix the type
someFunction() // with proper types

// Never chain type assertions
const user = data as any as User
// Correct
const user: User = parseUser(data)
```

### Interface Rules

```typescript
// Props interface
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  isLoading?: boolean
  children: React.ReactNode
  onClick?: () => void
}

// API Response types
interface ApiResponse<T> {
  success: boolean
  data: T
  error?: {
    code: number
    message: string
  }
}
```

### Union Types (instead of enums)

```typescript
// Correct
type Status = 'Pending' | 'Active' | 'Completed' | 'Cancelled'

// Wrong
const status: string = 'Active'
```

### Import Types

```typescript
import type { Product, Order } from '@/types'
import { apiClient } from '@/services/api'
```

### Generic Types

```typescript
function useQuery<TData, TError = Error>(
  queryKey: string[],
  queryFn: () => Promise<TData>
): UseQueryResult<TData, TError>

async function get<T>(url: string): Promise<ApiResponse<T>> {
  const response = await axios.get(url)
  return response.data
}
```

### When to Use?

**Always** - this is a project-wide standard.
