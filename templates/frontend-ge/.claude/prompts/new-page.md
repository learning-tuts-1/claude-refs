# ახალი გვერდის შექმნა

## Input
- გვერდის სახელი
- Route path
- მონაცემების მოთხოვნები

## შაბლონი

```tsx
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export function {{PageName}}Page() {
  // Data fetching hook
  // const { data, isLoading } = useQuery(...)

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">{{PageTitle}}</h1>
          <p className="text-muted-foreground">
            {{PageDescription}}
          </p>
        </div>
        <Button>Action</Button>
      </div>

      {/* Content */}
      <Card>
        <CardHeader>
          <CardTitle>Content</CardTitle>
        </CardHeader>
        <CardContent>
          {/* Page content */}
        </CardContent>
      </Card>
    </div>
  );
}
```

## ადგილმდებარეობა
`pages/{{PageName}}.tsx` ან `routes/{{route}}.tsx`

## Checklist
- [ ] Loading state
- [ ] Error state
- [ ] Empty state
- [ ] Design tokens
- [ ] TypeScript strict
