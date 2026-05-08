# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Rules

- **Never delete/commit/push** without my permission
- **Push back** - if you disagree with something, say so
- **Documentation** in `docs/`
- **Tailwind-first** - no custom CSS, no hardcoded colors
- **No comments** in code (exception: TODO)
- **Semicolons** - every statement must end with `;`
- **TypeScript strict** - no `any`, no `@ts-ignore`

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| {{FRAMEWORK}} | {{VERSION}} | Framework |
| React | {{REACT_VERSION}} | UI Library |
| TypeScript | ^5 | Type Safety |
| Tailwind CSS | v4 | Styling |
| Biome | ^2 | Linting + Formatting |

## Commands

```bash
npm run dev         # Development
npm run build       # Production
npm run lint        # Biome lint
npm run check       # Biome lint + format + fix
```

## Project Structure

```
{{PROJECT_NAME}}/
├── {{APP_DIR}}/
│   ├── components/
│   │   ├── ui/              # Reusable UI (Button, Input, Card...)
│   │   ├── layout/          # Layout (Header, Footer, Sidebar)
│   │   └── [feature]/       # Feature-specific
│   ├── hooks/               # Custom React hooks
│   ├── contexts/            # React Context providers
│   ├── services/
│   │   └── api/
│   │       └── client.ts    # API client
│   ├── types/               # TypeScript interfaces
│   └── lib/
│       └── utils.ts         # Utility functions
├── docs/                    # Documentation
├── .claude/                 # Claude Code config
├── CLAUDE.md                # This file
└── biome.json               # Linter/Formatter config
```

## Design System

### Color Usage

```tsx
// Correct - Design tokens
<div className="bg-background text-foreground" />
<button className="bg-primary hover:bg-primary/90" />
<p className="text-muted-foreground" />

// Incorrect - Hardcoded values
<div style={{ background: '#f1f1f1' }} />
<div className="bg-[#F9A80C]" />
```

### Color Palette

| Token | Usage |
|-------|-------|
| `background` | Page background |
| `foreground` | Primary text |
| `primary` | Buttons, links |
| `muted` / `muted-foreground` | Secondary |
| `card` / `card-foreground` | Cards |
| `destructive` | Errors, delete |

## Code Quality (Biome)

**Biome** - all-in-one linter + formatter (Rust-based).

### Pre-commit Hook
On commit automatically:
- Unused imports removed
- Imports sorted
- Formatting fixed

Config: `biome.json` + `.husky/pre-commit`
Details: `.claude/primitives/BIOME_LINTING.md`

## API Integration

### Backend: `{{API_URL}}`

```typescript
import { apiClient } from '~/services/api';

apiClient.getItems({ page, pageSize, search });
apiClient.getItemById(id);
apiClient.createItem(data);
apiClient.updateItem(id, data);
apiClient.deleteItem(id);
```

### API Response Format

```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed"
}
```

## Git Workflow

### Commit Messages

```
feat: new feature
fix: bug fix
refactor: code restructuring
style: style changes
docs: documentation
test: tests
chore: other
```

### Rules
- Never force push to main
- Never Co-Authored-By: Claude in commits
- Commit only with permission

## Auto-Load Templates

**Before creating a component** - read `.claude/prompts/new-component.md`
**Before creating a page** - read `.claude/prompts/new-page.md`
**Before creating a hook** - read `.claude/prompts/new-hook.md`

## Compositions (Multi-File Tasks)

**For new features** - read `.claude/compositions/new-feature.md`

## Primitives

| Primitive | Description |
|-----------|-------------|
| `GIT_RULES.md` | Git rules, commit format |
| `TYPESCRIPT_STRICT.md` | TypeScript strict mode |
| `DESIGN_TOKENS.md` | Colors, spacing, typography |
| `TAILWIND_FIRST.md` | Styling rules |
| `BIOME_LINTING.md` | Linter + formatter |
| `SEMICOLONS.md` | Semicolon policy |
| `FORWARDREF_COMPONENT.md` | UI component template |

## .claude Agents

| Agent | Purpose |
|-------|---------|
| `ui-developer` | UI component creation |
| `code-reviewer` | Code quality review |
| `docs-explorer` | Documentation research |

## Skills

| Skill | Description |
|-------|-------------|
| `explain-code.md` | Code explanation with ASCII diagrams |
| `tailwind-v4.md` | Tailwind CSS v4 patterns |

## Planning Rules

### Plan Mode
- In plan mode **only plan**, do not start implementation
- Write plans in `plan/` folder in the feature's PLAN.md
- Every feature needs: tasks list + dependencies

### Implementation
- One task at a time - not the entire feature at once
- After each task: review + test + commit
- Mark [x] completed tasks in PLAN.md

### Context Recovery
At the start of a new session, first read:
1. CLAUDE.md
2. plan/ - current feature's PLAN.md
3. dependencies.md

### Task Size
- One task = one commit
- Maximum 2-3 file changes
- If a task is too big, break it down

## Notes for Claude

1. **Design Tokens First** - always CSS variables
2. **TypeScript Strict** - no any, no type assertions
3. **Reuse Components** - use existing UI components
4. **Documentation** - docs/ folder, not inline comments
