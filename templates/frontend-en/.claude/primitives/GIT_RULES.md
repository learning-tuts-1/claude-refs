# GIT_RULES

## Git Rules

### Forbidden Actions

1. **Never push** without my explicit permission
   ```bash
   # Wrong - auto push
   git push origin main

   # Correct - ask first
   git add . && git commit -m "message"
   # Wait for permission
   ```

2. **Never use Co-Authored-By: Claude**

3. **Never force push to main/master**

### Commit Message Format

```
type: short description

Types:
- feat: new feature
- fix: bug fix
- refactor: code restructuring
- style: style changes
- docs: documentation
- test: tests
- chore: other
```

### Examples

```bash
git commit -m "feat: add product filtering by genre"
git commit -m "fix: resolve cart item count mismatch"
git commit -m "refactor: extract useProducts hook"
```
