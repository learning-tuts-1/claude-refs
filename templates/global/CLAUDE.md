# Global Rules

## Auto-Dispatch: MUST Follow Project Conventions

BEFORE starting ANY task, you MUST:

1. Check if `.claude/` folder exists in the project root
2. If it does, read `CLAUDE.md` and scan `rules/`, `primitives/`, `agents/`, `skills/`
3. Identify which primitives are relevant to the current task and READ them
4. Use defined skills (e.g., `/check`, `/new-component`) instead of manual equivalents
5. Apply patterns from primitives in your implementation

AFTER completing code changes, you MUST:

1. Run the project's `/check` skill if it exists
2. For changes touching 3+ files, run the `code-reviewer` agent if it exists

NEVER skip these steps, even for "small" or "obvious" fixes.
