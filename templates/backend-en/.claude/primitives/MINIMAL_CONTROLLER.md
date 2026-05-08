# MINIMAL_CONTROLLER

## Controller Rules

### Core Principle

Controller contains **only** routing + ApiResponse wrapper. No business logic.

### Correct

```csharp
[HttpGet]
public async Task<ActionResult<ApiResponse<List<ProductResponse>>>> GetAll(
    [FromQuery] ProductFilterRequest filter)
{
    var products = await _productService.GetAllAsync(filter);
    return Ok(ApiResponse<List<ProductResponse>>.Ok(products));
}
```

### Wrong

```csharp
[HttpPost]
public async Task<ActionResult> Create(CreateProductRequest request)
{
    // Wrong - validation in Controller
    if (string.IsNullOrEmpty(request.Title))
        return BadRequest("Title required");

    // Wrong - business logic in Controller
    var exists = await _context.Products.AnyAsync(p => p.Title == request.Title);

    // Wrong - direct DB access in Controller
    _context.Products.Add(entity);
    await _context.SaveChangesAsync();
}
```

### Controller Template

```csharp
[ApiController]
[Route("api/[controller]")]
public class {{Entity}}Controller : ControllerBase
{
    private readonly I{{Entity}}Service _service;

    public {{Entity}}Controller(I{{Entity}}Service service)
        => _service = service;

    [HttpGet]
    public async Task<ActionResult<ApiResponse<PagedResult<{{Entity}}Response>>>> GetAll(
        [FromQuery] {{Entity}}FilterRequest filter)
    {
        var result = await _service.GetAllAsync(filter);
        return Ok(ApiResponse<PagedResult<{{Entity}}Response>>.Ok(result));
    }

    [HttpGet("{id:int}")]
    public async Task<ActionResult<ApiResponse<{{Entity}}Response>>> GetById(int id)
    {
        var item = await _service.GetByIdAsync(id);
        return Ok(ApiResponse<{{Entity}}Response>.Ok(item));
    }

    [HttpPost]
    public async Task<ActionResult<ApiResponse<{{Entity}}Response>>> Create(
        Create{{Entity}}Request request)
    {
        var item = await _service.CreateAsync(request);
        return Ok(ApiResponse<{{Entity}}Response>.Ok(item, "Created"));
    }

    [HttpPut("{id:int}")]
    public async Task<ActionResult<ApiResponse<{{Entity}}Response>>> Update(
        int id, Update{{Entity}}Request request)
    {
        var item = await _service.UpdateAsync(id, request);
        return Ok(ApiResponse<{{Entity}}Response>.Ok(item, "Updated"));
    }

    [HttpDelete("{id:int}")]
    public async Task<ActionResult<ApiResponse<bool>>> Delete(int id)
    {
        await _service.DeleteAsync(id);
        return Ok(ApiResponse<bool>.Ok(true, "Deleted"));
    }
}
```

### When to Use?

**Always** - for every Controller.
