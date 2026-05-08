---
name: remix-framework
description: Remix full-stack React framework patterns — SSR, loaders, actions, file-based routing. Use when creating routes, handling forms, or working with server-side data loading.
---

# Remix Framework

Full-stack React framework with SSR, nested routing, loaders/actions.

## Architecture

```
Browser --> Route --> Loader (GET) --> Component
   |                                      |
   |         Action (POST) <--------------+
   |              |
   +------------- +--> Revalidate --> Re-render
```

## File-Based Routing

```
app/routes/
├── _index.tsx              -> /
├── products._index.tsx     -> /products
├── products.$handle.tsx    -> /products/:handle
├── api.auth.login.tsx      -> /api/auth/login
└── ($lang).about.tsx       -> /about or /ka/about
```

| Pattern | Example | URL |
|---------|---------|-----|
| `_index` | `_index.tsx` | `/` |
| `.` (dot) | `products.list.tsx` | `/products/list` |
| `$param` | `products.$id.tsx` | `/products/123` |
| `_` (escape) | `products.$id_.edit.tsx` | `/products/123/edit` |
| `($optional)` | `($lang).about.tsx` | `/about` or `/en/about` |

## Loader (Server-Side Data)

```typescript
import type { LoaderFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";

export async function loader({ params }: LoaderFunctionArgs) {
  const product = await getProduct(params.handle);
  if (!product) throw new Response("Not Found", { status: 404 });
  return json({ product });
}

export default function ProductPage() {
  const { product } = useLoaderData<typeof loader>();
  return <ProductDetails product={product} />;
}
```

## Action (Form Handling)

```typescript
import type { ActionFunctionArgs } from "@remix-run/node";
import { redirect } from "@remix-run/node";
import { Form, useActionData } from "@remix-run/react";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const errors = validate(formData);
  if (errors) return json({ errors }, { status: 400 });
  await processData(formData);
  return redirect("/success");
}
```

## Client vs Server Files

- `.server.ts` — server only (DB, secrets)
- `.client.ts` — client only (Firebase, localStorage)
- Regular `.ts` — both (be careful!)

## Fetcher (Non-Navigation)

```typescript
const fetcher = useFetcher();
<fetcher.Form method="post" action="/api/cart/add">
  <button disabled={fetcher.state === "submitting"}>Add to Cart</button>
</fetcher.Form>
```

## Error Handling

```typescript
export function ErrorBoundary() {
  const error = useRouteError();
  if (isRouteErrorResponse(error)) {
    return <div><h1>{error.status}</h1><p>{error.statusText}</p></div>;
  }
  return <div>Something went wrong</div>;
}
```
