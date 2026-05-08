---
name: indexeddb-cache
description: IndexedDB client-side file caching with expiration. Use when working on caching, offline support, or optimizing repeated file downloads.
---

# IndexedDB Cache

Client-side file caching with automatic expiration.

## Architecture

```
Request File -> Check Cache (IndexedDB) -> Hit -> Return
                       | Miss
                       v
                Fetch + Save to IndexedDB
```

## Key Concepts

- **Schema:** `{ key, data: ArrayBuffer, contentType, size, cachedAt, expiresAt }`
- **Expiration:** configurable (e.g., 30 days)
- **Indexes:** `expiresAt` (cleanup), `cachedAt` (ordering)
- **Cleanup:** `cleanExpired()` on startup

## Storage Limits

| Browser | Default Limit |
|---------|---------------|
| Chrome | 80% of disk (per origin) |
| Firefox | 50% of disk (per origin) |
| Safari | 1GB (prompts after) |

## Best Practices

1. Unique cache keys (full URL or hash)
2. Set expiration (30 days reasonable for media)
3. Clean expired entries on startup
4. Handle quota errors — clear old entries if full
