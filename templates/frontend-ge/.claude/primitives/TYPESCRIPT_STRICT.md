# TYPESCRIPT_STRICT

## TypeScript Strict Mode წესები

### აკრძალული პატერნები

```typescript
// არასდროს any
const data: any = response.data
// სწორი - კონკრეტული ტიპი
const data: ProductResponse = response.data

// არასდროს @ts-ignore
// @ts-ignore
someFunction()
// სწორი - გაასწორე ტიპი
someFunction() // with proper types

// არასდროს type assertion ტიპის გასაქცევად
const user = data as any as User
// სწორი
const user: User = parseUser(data)
```

### Interface წესები

```typescript
// Props interface კომპონენტისთვის
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

### Union Types (Enums-ის ნაცვლად)

```typescript
// სწორი
type Status = 'Pending' | 'Active' | 'Completed' | 'Cancelled'

// არასწორი
const status: string = 'Active'
```

### Import Types

```typescript
// ტიპები ცალკე იმპორტირდება
import type { Product, Order } from '@/types'
import { apiClient } from '@/services/api'
```

### Generic Types

```typescript
// Query hooks
function useQuery<TData, TError = Error>(
  queryKey: string[],
  queryFn: () => Promise<TData>
): UseQueryResult<TData, TError>

// API client
async function get<T>(url: string): Promise<ApiResponse<T>> {
  const response = await axios.get(url)
  return response.data
}
```

### Function Return Types

```typescript
// Explicit return types
function calculatePrice(basePrice: number, discount: number): number {
  return basePrice * (1 - discount)
}

// Async function types
async function fetchProducts(): Promise<Product[]> {
  const response = await apiClient.getProducts()
  return response.data
}
```
