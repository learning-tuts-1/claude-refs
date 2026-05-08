# {{PROJECT_NAME}} Backend

{{PROJECT_DESCRIPTION}}

## Rules

- **Never delete/commit/push** without my permission
- **Push back** - if you disagree, say so
- **Documentation** in `docs/`
- **No comments** in code

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| .NET | {{DOTNET_VERSION}} | Framework |
| C# | {{CSHARP_VERSION}} | Language |
| MSSQL Server | 2022 | Database |
| EF Core | {{EF_VERSION}} | ORM (reads) |
| Dapper | {{DAPPER_VERSION}} | Micro-ORM (SP calls) |

## Commands

```bash
dotnet run --project {{PROJECT_NAME}}.Api    # Development
dotnet build                                 # Build
dotnet test                                  # Tests
```

## Project Structure

```
{{PROJECT_NAME}}/
├── {{PROJECT_NAME}}.Api/
│   ├── Controllers/         # API Controllers
│   ├── Middleware/           # Custom middleware
│   └── Program.cs           # Entry point
│
├── {{PROJECT_NAME}}.Application/
│   ├── DTOs/                # Request/Response objects
│   ├── Interfaces/          # Service & Repository interfaces
│   ├── Services/            # Business logic
│   └── Exceptions/          # Custom exceptions
│
├── {{PROJECT_NAME}}.Domain/
│   ├── Entities/            # Domain entities
│   └── Enums/               # Domain enums
│
├── {{PROJECT_NAME}}.Persistence/
│   ├── Context/             # EF Core DbContext
│   ├── Repositories/        # Repository implementations
│   └── Migrations/          # EF Core migrations
│
└── docs/
    └── database/
        └── scripts/         # SQL scripts
```

## Architecture

```
Controller → Service → Repository → Database
    │            │
    │            └── Business Logic, Validation
    │
    └── Only route + ApiResponse wrapper
```

## API Response Format

### Success
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### Error
```json
{
  "success": false,
  "error": {
    "code": 50001,
    "message": "Title is required"
  }
}
```

### Error Code Ranges

| Range | Category | Description |
|-------|----------|-------------|
| `0` | Success | Successful operation |
| `50001-50099` | Validation | Field validation errors |
| `50101-50199` | Business Rules | Business logic violations |
| `50201-50299` | Authorization | Auth errors |
| `50301-50399` | Not Found | Resource not found |

## Controller Pattern

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;

    public ProductsController(IProductService productService)
        => _productService = productService;

    [HttpGet]
    public async Task<ActionResult<ApiResponse<List<ProductResponse>>>> GetAll()
    {
        var products = await _productService.GetAllAsync();
        return Ok(ApiResponse<List<ProductResponse>>.Ok(products));
    }
}
```

### Controller Rules
- Minimal logic (1-2 lines per method)
- Calls service, returns ApiResponse
- No business logic in Controller

## Repository Pattern (Hybrid)

- **EF Core** for reads (LINQ, Include, navigation properties)
- **Dapper** for writes (Stored Procedures, complex queries)

## Git Workflow

### Commit Messages

```
feat: new feature
fix: bug fix
refactor: code restructuring
docs: documentation
test: tests
chore: other
```

### Rules
- Never force push to main
- Never Co-Authored-By: Claude in commits

## Primitives

| Primitive | Description |
|-----------|-------------|
| `GIT_RULES.md` | Git rules |
| `API_RESPONSE.md` | Response wrapper |
| `ERROR_TAXONOMY.md` | Error code ranges |
| `MINIMAL_CONTROLLER.md` | Controller rules |
| `HYBRID_REPOSITORY.md` | EF Core + Dapper |

## Compositions

| Composition | Usage |
|-------------|-------|
| `new-api-endpoint.md` | New API endpoint |

## Agents

| Agent | Description |
|-------|-------------|
| `api-developer` | API endpoint creation |
| `code-reviewer` | Code quality review |
| `docs-explorer` | .NET documentation research |
| `sql-agent` | SQL Server object creation |

## Skills

| Skill | Description |
|-------|-------------|
| `explain-code.md` | Code explanation with ASCII diagrams |

## Auto-Load Templates

**Before creating a Stored Procedure** - read `.claude/prompts/generate-procedure.md`
**Before creating a Table** - read `.claude/prompts/generate-table.md`

## Planning Rules

### Plan Mode
- In plan mode **only plan**, do not start implementation
- Write plans in `plan/` folder in the feature's PLAN.md
- Every feature needs: tasks list + dependencies

### Implementation
- One task at a time - not the entire feature at once
- After each task: review + test + commit
- Mark [x] completed tasks in PLAN.md

### Task Size
- One task = one commit
- Maximum 2-3 file changes

## Notes for Claude

1. **Minimal Controller** - only routing + response
2. **Service Layer** - business logic here
3. **Hybrid Repository** - EF Core reads + Dapper writes
4. **Error codes** - always in correct ranges
5. **ApiResponse wrapper** - on every endpoint
