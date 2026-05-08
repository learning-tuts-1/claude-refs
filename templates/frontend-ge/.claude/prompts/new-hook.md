# ახალი Hook-ის შექმნა

## Input
- Hook-ის სახელი
- დანიშნულება
- API endpoint (თუ საჭიროა)

## Query Hook შაბლონი

```tsx
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/services/api/client';

interface {{DataType}} {
  // response type
}

interface {{HookName}}Params {
  // parameters
}

export function {{hookName}}(params?: {{HookName}}Params) {
  return useQuery<{{DataType}}>({
    queryKey: ['{{queryKey}}', params],
    queryFn: () => apiClient.{{method}}(params),
    enabled: true,
  });
}
```

## Mutation Hook შაბლონი

```tsx
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/services/api/client';

interface {{RequestType}} {
  // request type
}

export function {{hookName}}() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: {{RequestType}}) => apiClient.{{method}}(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['{{queryKey}}'] });
    },
  });
}
```

## ადგილმდებარეობა
`hooks/{{hookName}}.ts`

## Checklist
- [ ] TypeScript strict (return types, params)
- [ ] Error handling
- [ ] Loading states
- [ ] Semicolons
