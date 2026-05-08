# API_RESPONSE

## API Response Wrapper Pattern

### სტანდარტული ფორმატი

ყველა API endpoint აბრუნებს ერთიან ფორმატს:

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

### C# Implementation

```csharp
public class ApiResponse<T>
{
    public bool Success { get; set; }
    public T? Data { get; set; }
    public string? Message { get; set; }
    public ApiError? Error { get; set; }

    public static ApiResponse<T> Ok(T data, string? message = null)
        => new() { Success = true, Data = data, Message = message };

    public static ApiResponse<T> Fail(int code, string message)
        => new() { Success = false, Error = new ApiError(code, message) };
}

public record ApiError(int Code, string Message);
```

### Controller გამოყენება

```csharp
[HttpGet]
public async Task<ActionResult<ApiResponse<List<ProductResponse>>>> GetAll()
{
    var products = await _productService.GetAllAsync();
    return Ok(ApiResponse<List<ProductResponse>>.Ok(products));
}
```

### Paged Response

```csharp
public class PagedResult<T>
{
    public List<T> Items { get; set; } = new();
    public int TotalCount { get; set; }
    public int PageNumber { get; set; }
    public int PageSize { get; set; }
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
}
```

### როდის გამოვიყენო?

**ყოველთვის** - ყველა API endpoint-ზე.
