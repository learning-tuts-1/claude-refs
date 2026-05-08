# {{PROJECT_NAME}} Backend

{{PROJECT_DESCRIPTION}}

## წესები

- **არაფერი წაშალო/დააკომიტო/დაფუშო** ჩემი ნებართვის გარეშე
- **შემეკამათე** - თუ რამე არ მოგწონს, თქვი
- **დოკუმენტაცია** ქართულად `docs/`-ში
- **კომენტარები არ მჭირდება** კოდში

## Tech Stack

| ტექნოლოგია | ვერსია | გამოყენება |
|------------|--------|------------|
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

## პროექტის სტრუქტურა

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

## არქიტექტურა

```
Controller → Service → Repository → Database
    │            │
    │            └── Business Logic, Validation
    │
    └── მხოლოდ route + ApiResponse wrapper
```

## API Response ფორმატი

### წარმატება
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### შეცდომა
```json
{
  "success": false,
  "error": {
    "code": 50001,
    "message": "Title is required"
  }
}
```

### Error Code დიაპაზონები

| Range | Category | აღწერა |
|-------|----------|--------|
| `0` | Success | წარმატებული |
| `50001-50099` | Validation | ველის ვალიდაცია |
| `50101-50199` | Business Rules | ბიზნეს ლოგიკა |
| `50201-50299` | Authorization | ავტორიზაცია |
| `50301-50399` | Not Found | რესურსი ვერ მოიძებნა |

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

    [HttpPost]
    public async Task<ActionResult<ApiResponse<ProductResponse>>> Create(
        CreateProductRequest request)
    {
        var product = await _productService.CreateAsync(request);
        return Ok(ApiResponse<ProductResponse>.Ok(product, "Product created"));
    }
}
```

### Controller წესები
- მინიმალური ლოგიკა (1-2 ხაზი მეთოდში)
- Service-ს უძახებს, ApiResponse-ს აბრუნებს
- არანაირი ბიზნეს ლოგიკა Controller-ში

## Repository Pattern (Hybrid)

```csharp
// EF Core - reads (LINQ, includes)
public async Task<Product?> GetByIdAsync(int id)
{
    return await _context.Products
        .Include(p => p.Category)
        .FirstOrDefaultAsync(p => p.Id == id);
}

// Dapper - writes (Stored Procedures)
public async Task<int> CreateAsync(CreateProductRequest request)
{
    var parameters = new DynamicParameters();
    parameters.Add("@Title", request.Title);
    parameters.Add("@Price", request.Price);
    parameters.Add("@ErrorCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
    parameters.Add("@ErrorMessage", dbType: DbType.String, size: 500, direction: ParameterDirection.Output);

    await _connection.ExecuteAsync("dbo.CreateProduct", parameters,
        commandType: CommandType.StoredProcedure);

    var errorCode = parameters.Get<int>("@ErrorCode");
    if (errorCode != 0)
        throw new BusinessException(errorCode, parameters.Get<string>("@ErrorMessage"));

    return parameters.Get<int>("@NewId");
}
```

## Git Workflow

### Commit Messages

```
feat: ახალი ფუნქციონალი
fix: ბაგის გასწორება
refactor: კოდის რესტრუქტურიზაცია
docs: დოკუმენტაცია
test: ტესტები
chore: სხვა
```

### წესები
- არასდროს force push main-ზე
- არასდროს Co-Authored-By: Claude კომიტებში

## Primitives

| Primitive | აღწერა |
|-----------|--------|
| `GIT_RULES.md` | Git წესები |
| `API_RESPONSE.md` | Response wrapper |
| `ERROR_TAXONOMY.md` | Error code ranges |
| `MINIMAL_CONTROLLER.md` | Controller rules |
| `HYBRID_REPOSITORY.md` | EF Core + Dapper |

## Compositions

| Composition | გამოყენება |
|-------------|------------|
| `new-api-endpoint.md` | ახალი API endpoint |

## Agents

| Agent | აღწერა |
|-------|--------|
| `api-developer` | API endpoint-ების შექმნა |
| `code-reviewer` | კოდის ხარისხის შემოწმება |
| `docs-explorer` | .NET დოკუმენტაციის მოძიება |
| `sql-agent` | SQL Server ობიექტების შექმნა |

## Skills

| Skill | აღწერა |
|-------|--------|
| `explain-code.md` | კოდის ახსნა ASCII დიაგრამებით |

## Auto-Load Templates

**Stored Procedure-ის შექმნამდე** - წაიკითხე `.claude/prompts/generate-procedure.md`
**Table-ის შექმნამდე** - წაიკითხე `.claude/prompts/generate-table.md`

## Planning Rules

### Plan Mode
- Plan mode-ში **მხოლოდ დაგეგმე**, არ დაიწყო იმპლემენტაცია
- გეგმა ჩაწერე `plan/` ფოლდერში შესაბამის feature-ის PLAN.md-ში
- ყოველი feature-ისთვის: tasks list + dependencies

### Implementation
- ერთ დროს **ერთი task** - არა მთელი feature ერთხელ
- ყოველი task-ის შემდეგ: review + test + commit
- PLAN.md-ში მონიშნე [x] გაკეთებული tasks

### Task Size
- ერთი task = ერთი commit
- მაქსიმუმ 2-3 ფაილის ცვლილება

## შენიშვნები Claude-სთვის

1. **Controller მინიმალური** - მხოლოდ routing + response
2. **Service ფენა** - ბიზნეს ლოგიკა
3. **Repository hybrid** - EF Core reads + Dapper writes
4. **Error codes** - ყოველთვის სწორ დიაპაზონში
5. **ApiResponse wrapper** - ყველა endpoint-ზე
