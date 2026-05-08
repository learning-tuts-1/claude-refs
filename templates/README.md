# Claude Code Project Templates

Reusable `.claude` folder templates + project planning system for Claude Code.

## Structure

```
claude-templates/
├── README.md                # This file
├── CONCEPTS.md              # Primitives, Skills, Prompts, Agents explained
├── PROJECT_WORKFLOW.md      # Full guide: idea → plan → build → ship
│
├── frontend-ge/             # Frontend template (Georgian)
│   ├── CLAUDE.md
│   └── .claude/
│       ├── primitives/      # 7 rules
│       ├── prompts/         # 3 templates
│       ├── compositions/    # 1 workflow
│       ├── agents/          # 3 agents
│       └── skills/          # 2 skills
│
├── frontend-en/             # Frontend template (English)
│   ├── CLAUDE.md
│   └── .claude/             # (same structure)
│
├── backend-ge/              # Backend template (Georgian)
│   ├── CLAUDE.md
│   └── .claude/
│       ├── primitives/      # 5 rules
│       ├── prompts/         # 2 templates
│       ├── compositions/    # 1 workflow
│       ├── agents/          # 4 agents
│       └── skills/          # 1 skill
│
├── backend-en/              # Backend template (English)
│   ├── CLAUDE.md
│   └── .claude/             # (same structure)
│
├── global/                  # Global Claude Code settings (~/.claude/)
│   ├── README.md            # Setup instructions
│   └── CLAUDE.md            # Auto-dispatch rule (applies to ALL projects)
│
└── plan-template/           # Project planning template
    ├── README.md            # Master plan (features + priority)
    └── v1/
        ├── DEPENDENCY_GRAPH.md
        └── 01-example-feature/
            ├── PLAN.md          # Tasks + checklist
            └── dependencies.md  # Up/downstream deps
```

## Quick Start

### 1. New Project Setup

```bash
mkdir my-project && cd my-project

# Copy template (pick language)
cp -r /path/to/claude-templates/frontend-ge/.claude .claude
cp /path/to/claude-templates/frontend-ge/CLAUDE.md CLAUDE.md

# Copy planning structure
cp -r /path/to/claude-templates/plan-template plan

# Create docs
mkdir -p docs/{design,architecture}
```

### 2. Replace Placeholders

Open CLAUDE.md and replace:
- `{{PROJECT_NAME}}` - your project name
- `{{PROJECT_DESCRIPTION}}` - description
- `{{FRAMEWORK}}` - React/Next.js/Remix
- `{{API_URL}}` - backend URL

### 3. Start Planning

Read `PROJECT_WORKFLOW.md` for the full guide.

## Template Contents

### Frontend (.claude/)

| Folder | Files | Purpose |
|--------|-------|---------|
| `primitives/` | GIT_RULES, TYPESCRIPT_STRICT, DESIGN_TOKENS, TAILWIND_FIRST, BIOME_LINTING, SEMICOLONS, FORWARDREF_COMPONENT | Coding rules |
| `prompts/` | new-component, new-page, new-hook | Single-file templates |
| `compositions/` | new-feature | Multi-file workflow |
| `agents/` | ui-developer, code-reviewer, docs-explorer | AI role definitions |
| `skills/` | explain-code, tailwind-v4 | Technology patterns |

### Backend (.claude/)

| Folder | Files | Purpose |
|--------|-------|---------|
| `primitives/` | GIT_RULES, API_RESPONSE, ERROR_TAXONOMY, MINIMAL_CONTROLLER, HYBRID_REPOSITORY | Coding rules |
| `prompts/` | generate-procedure, generate-table | SQL generation templates |
| `compositions/` | new-api-endpoint | Multi-file workflow |
| `agents/` | api-developer, code-reviewer, docs-explorer, sql-agent | AI role definitions |
| `skills/` | explain-code | Technology patterns |

## Concepts

| Concept | What | Size |
|---------|------|------|
| **Primitive** | One rule/pattern | 20-50 lines |
| **Composition** | Multiple primitives combined | 50-100 lines |
| **Agent** | AI role definition | 50+ lines |
| **Skill** | External technology reference | 50-100 lines |
| **Prompt** | Single-file code template | 30-50 lines |

## Compounding Effect

```
Claude makes a mistake
  → You add a rule to the primitive
    → Claude never repeats it
      → Over time: fewer mistakes, faster development
```

This is the core value - your `.claude/` folder gets smarter with every project.
