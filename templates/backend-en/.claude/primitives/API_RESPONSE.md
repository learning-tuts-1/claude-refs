# API_RESPONSE

## API Response Wrapper Pattern

### Standard Format

Every API endpoint returns a unified format:

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

### When to Use?

**Always** - on every API endpoint.
