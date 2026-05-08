# New Hook

## Input
- Hook name
- Purpose
- API endpoint (if applicable)

## Query Hook

```tsx
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/services/api/client';

interface {{DataType}} {}
interface {{HookName}}Params {}

export function {{hookName}}(params?: {{HookName}}Params) {
  return useQuery<{{DataType}}>({
    queryKey: ['{{queryKey}}', params],
    queryFn: () => apiClient.{{method}}(params),
    enabled: true,
  });
}
```

## Mutation Hook

```tsx
import { useMutation, useQueryClient } from '@tanstack/react-query';

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

## Location
`hooks/{{hookName}}.ts`
