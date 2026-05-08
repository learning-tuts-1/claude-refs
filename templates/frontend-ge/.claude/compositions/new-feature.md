# New Feature Composition

ეს არის composition ახალი feature-ის შესაქმნელად.

## გამოყენებული Primitives

{{INCLUDE: ../primitives/TAILWIND_FIRST.md}}
{{INCLUDE: ../primitives/TYPESCRIPT_STRICT.md}}
{{INCLUDE: ../primitives/DESIGN_TOKENS.md}}
{{INCLUDE: ../primitives/FORWARDREF_COMPONENT.md}}
{{INCLUDE: ../primitives/SEMICOLONS.md}}
{{INCLUDE: ../primitives/BIOME_LINTING.md}}

## Instructions

შექმენი ახალი feature შემდეგი სპეციფიკაციით:

### Input
- **Feature Name:** [FEATURE]
- **Components Needed:** [list]
- **State Management:** Context | React Query | Local

### Output Files

1. **Components:** `components/[feature]/`
   - FORWARDREF_COMPONENT pattern
   - TAILWIND_FIRST styling
   - DESIGN_TOKENS colors

2. **Context (თუ საჭიროა):** `contexts/[Feature]Context.tsx`
   - useCallback actions-ისთვის
   - სწორი cleanup

3. **Hooks:** `hooks/use[Feature].ts`
   - TypeScript strict
   - Export types

4. **Types:** `types/[feature].ts`
   - Interfaces ყველა მონაცემისთვის
   - Export types ცალკე

### Checklist

- [ ] Tailwind-first (no custom CSS)
- [ ] Design tokens (no hardcoded colors)
- [ ] TypeScript strict (no any)
- [ ] Semicolons everywhere
- [ ] No unused imports
- [ ] forwardRef for UI components
- [ ] useCallback for context actions
- [ ] Proper cleanup in useEffect
- [ ] Error states handled
- [ ] Loading states handled
- [ ] `npm run check` passes (Biome)
