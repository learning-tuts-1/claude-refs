---
name: tanstack-query
description: TanStack Query v5 server state management — caching, mutations, optimistic updates. Use when working with API data fetching, mutations, or cache management.
---

# TanStack Query v5

Server state management, caching, mutations.

## Architecture

```
Component --> useQuery/useMutation --> API Client
                    |
              QueryCache (in-memory)
```

## Key Concepts

- **staleTime:** 5 minutes default — data considered fresh, no refetch
- **retry:** 1 for queries, skip 4xx errors
- **refetchOnWindowFocus:** disabled for admin panels
- **placeholderData:** `keepPreviousData` for pagination
- **enabled:** conditional fetching (`enabled: !!id`)
- **Cache invalidation:** `queryClient.invalidateQueries()` after mutations

## Query Key Patterns

```typescript
queryKeys.products.all          // ['products']
queryKeys.products.list(filters) // ['products', 'list', filters]
queryKeys.products.detail(id)   // ['products', 'detail', id]
```

## Mutation Lifecycle

```
mutate() -> onMutate -> mutationFn -> onSuccess/onError -> onSettled
                |                        |
         optimistic update          invalidate cache
```

## Loading States

- `isLoading` = true only on initial load (no cached data)
- `isFetching` = true on any background fetch
- Use `isLoading` for full-page spinner, `isFetching && !isLoading` for subtle indicator

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Stale data after mutation | Missing invalidation | Add `invalidateQueries()` in `onSuccess` |
| Infinite refetch | Object in queryKey recreated each render | Stabilize with `useMemo` |
| Flash of old data | No `placeholderData` | Use `keepPreviousData` for pagination |
