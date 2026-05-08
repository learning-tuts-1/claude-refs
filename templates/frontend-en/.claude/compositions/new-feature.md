# New Feature Composition

Combines multiple primitives for creating a new feature.

## Primitives Used

{{INCLUDE: ../primitives/TAILWIND_FIRST.md}}
{{INCLUDE: ../primitives/TYPESCRIPT_STRICT.md}}
{{INCLUDE: ../primitives/DESIGN_TOKENS.md}}
{{INCLUDE: ../primitives/FORWARDREF_COMPONENT.md}}
{{INCLUDE: ../primitives/SEMICOLONS.md}}
{{INCLUDE: ../primitives/BIOME_LINTING.md}}

## Instructions

### Input
- **Feature Name:** [FEATURE]
- **Components Needed:** [list]
- **State Management:** Context | React Query | Local

### Output Files

1. **Components:** `components/[feature]/`
2. **Context (if needed):** `contexts/[Feature]Context.tsx`
3. **Hooks:** `hooks/use[Feature].ts`
4. **Types:** `types/[feature].ts`

### Checklist

- [ ] Tailwind-first (no custom CSS)
- [ ] Design tokens (no hardcoded colors)
- [ ] TypeScript strict (no any)
- [ ] Semicolons everywhere
- [ ] No unused imports
- [ ] forwardRef for UI components
- [ ] Error states handled
- [ ] Loading states handled
- [ ] `npm run check` passes (Biome)
