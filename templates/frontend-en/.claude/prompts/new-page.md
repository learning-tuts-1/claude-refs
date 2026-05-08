# New Page

## Input
- Page name
- Route path
- Data requirements

## Template

```tsx
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export function {{PageName}}Page() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">{{PageTitle}}</h1>
          <p className="text-muted-foreground">{{PageDescription}}</p>
        </div>
        <Button>Action</Button>
      </div>

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

## Location
`pages/{{PageName}}.tsx`

## Checklist
- [ ] Loading state
- [ ] Error state
- [ ] Empty state
- [ ] Design tokens
- [ ] TypeScript strict
