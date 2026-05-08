# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## წესები

- **არაფერი წაშალო/დააკომიტო/დაფუშო** ჩემი ნებართვის გარეშე
- **შემეკამათე** - თუ რამე არ მოგწონს, თქვი
- **დოკუმენტაცია** ქართულად `docs/`-ში
- **Tailwind-first** - არა custom CSS, არა hardcoded ფერები
- **კომენტარები არ მჭირდება** კოდში (გამონაკლისი: TODO)
- **Semicolons** - ყველა statement უნდა დამთავრდეს `;` სიმბოლოთი
- **TypeScript strict** - არა `any`, არა `@ts-ignore`

## Tech Stack

| ტექნოლოგია | ვერსია | გამოყენება |
|------------|--------|------------|
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

## პროექტის სტრუქტურა

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
├── docs/                    # Documentation (ქართულად)
├── .claude/                 # Claude Code config
├── CLAUDE.md                # ეს ფაილი
└── biome.json               # Linter/Formatter config
```

## Design System

### ფერების გამოყენება

```tsx
// სწორი - Design tokens
<div className="bg-background text-foreground" />
<button className="bg-primary hover:bg-primary/90" />
<p className="text-muted-foreground" />

// არასწორი - Hardcoded values
<div style={{ background: '#f1f1f1' }} />
<div className="bg-[#F9A80C]" />
```

### Color Palette

| Token | გამოყენება |
|-------|------------|
| `background` | გვერდის ფონი |
| `foreground` | მთავარი ტექსტი |
| `primary` | ღილაკები, ლინკები |
| `muted` / `muted-foreground` | მეორეხარისხოვანი |
| `card` / `card-foreground` | ბარათები |
| `destructive` | შეცდომები, წაშლა |

## Code Quality (Biome)

**Biome** - all-in-one linter + formatter (Rust-based).

### Pre-commit Hook
კომიტზე ავტომატურად:
- Unused imports წაიშლება
- Imports დალაგდება
- Formatting გასწორდება

### კონფიგურაცია
- `biome.json` - წესები და settings
- `.husky/pre-commit` - git hook
- დეტალები: `.claude/primitives/BIOME_LINTING.md`

## API ინტეგრაცია

### Backend: `{{API_URL}}`

```typescript
import { apiClient } from '~/services/api';

// მაგალითები
apiClient.getItems({ page, pageSize, search });
apiClient.getItemById(id);
apiClient.createItem(data);
apiClient.updateItem(id, data);
apiClient.deleteItem(id);
```

### API Response ფორმატი

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
feat: ახალი ფუნქციონალი
fix: ბაგის გასწორება
refactor: კოდის რესტრუქტურიზაცია
style: სტილის ცვლილება
docs: დოკუმენტაცია
test: ტესტები
chore: სხვა
```

### წესები
- არასდროს force push main-ზე
- არასდროს Co-Authored-By: Claude კომიტებში
- კომიტი მხოლოდ ნებართვით

## Auto-Load Templates

**კომპონენტის შექმნამდე** - წაიკითხე `.claude/prompts/new-component.md`
**Page-ის შექმნამდე** - წაიკითხე `.claude/prompts/new-page.md`
**Hook-ის შექმნამდე** - წაიკითხე `.claude/prompts/new-hook.md`

## Compositions (Multi-File Tasks)

**ახალი Feature-სთვის** - წაიკითხე `.claude/compositions/new-feature.md`

```
User: "შექმენი Wishlist feature"
Claude: [კითხულობს compositions/new-feature.md]
        [ქმნის: Components + Context + Hook + Route]
```

## Primitives

| Primitive | აღწერა |
|-----------|--------|
| `GIT_RULES.md` | Git წესები, commit format |
| `TYPESCRIPT_STRICT.md` | TypeScript strict mode |
| `DESIGN_TOKENS.md` | ფერები, spacing, typography |
| `TAILWIND_FIRST.md` | Styling წესები |
| `BIOME_LINTING.md` | Linter + formatter |
| `SEMICOLONS.md` | Semicolon policy |
| `FORWARDREF_COMPONENT.md` | UI component template |

## .claude Agents

| Agent | Purpose |
|-------|---------|
| `ui-developer` | UI კომპონენტების შექმნა |
| `code-reviewer` | კოდის ხარისხის შემოწმება |
| `docs-explorer` | დოკუმენტაციის მოძიება |

## Skills

| Skill | აღწერა |
|-------|--------|
| `explain-code.md` | კოდის ახსნა ASCII დიაგრამებით |
| `tailwind-v4.md` | Tailwind CSS v4 პატერნები |

## Planning Rules

### Plan Mode
- Plan mode-ში **მხოლოდ დაგეგმე**, არ დაიწყო იმპლემენტაცია
- გეგმა ჩაწერე `plan/` ფოლდერში შესაბამის feature-ის PLAN.md-ში
- ყოველი feature-ისთვის: tasks list + dependencies

### Implementation
- ერთ დროს **ერთი task** - არა მთელი feature ერთხელ
- ყოველი task-ის შემდეგ: review + test + commit
- PLAN.md-ში მონიშნე [x] გაკეთებული tasks

### Context Recovery
როცა ახალ სესიას ვიწყებ, ჯერ წაიკითხე:
1. CLAUDE.md
2. plan/ - მიმდინარე feature-ის PLAN.md
3. dependencies.md

### Task Size
- ერთი task = ერთი commit
- მაქსიმუმ 2-3 ფაილის ცვლილება
- თუ task ძალიან დიდია, დაშალე

## შენიშვნები Claude-სთვის

1. **Design Tokens First** - ყოველთვის CSS variables
2. **TypeScript Strict** - არა any, არა type assertions
3. **Reuse Components** - არსებული UI კომპონენტების გამოყენება
4. **Documentation** - docs/ ფოლდერი, არა inline კომენტარები
