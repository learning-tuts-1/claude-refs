# ERROR_TAXONOMY

## Error Code System

### Ranges

| Range | Category | Description |
|-------|----------|-------------|
| `0` | Success | Successful operation |
| `50001-50099` | Validation | Field validation errors |
| `50101-50199` | Business Rules | Business logic violations |
| `50201-50299` | Authorization | Authorization errors |
| `50301-50399` | Not Found | Resource not found |

### Usage in Stored Procedures

```sql
CREATE PROCEDURE dbo.Create{{Entity}}
    @Title NVARCHAR(200),
    @ErrorCode INT OUTPUT,
    @ErrorMessage NVARCHAR(500) OUTPUT
AS
BEGIN
    -- Validation (50001-50099)
    IF @Title IS NULL OR LEN(@Title) = 0
    BEGIN
        SET @ErrorCode = 50001
        SET @ErrorMessage = N'Title is required'
        RETURN
    END

    -- Business Rule (50101-50199)
    IF EXISTS (SELECT 1 FROM {{Entity}} WHERE Title = @Title)
    BEGIN
        SET @ErrorCode = 50101
        SET @ErrorMessage = N'Already exists'
        RETURN
    END

    SET @ErrorCode = 0
    SET @ErrorMessage = N'Success'
END
```

### Usage in C#

```csharp
var errorCode = parameters.Get<int>("@ErrorCode");
if (errorCode != 0)
{
    var msg = parameters.Get<string>("@ErrorMessage");
    return errorCode switch
    {
        >= 50001 and <= 50099 => throw new ValidationException(msg),
        >= 50101 and <= 50199 => throw new BusinessRuleException(msg),
        >= 50201 and <= 50299 => throw new UnauthorizedException(msg),
        >= 50301 and <= 50399 => throw new NotFoundException(msg),
        _ => throw new Exception(msg)
    };
}
```

### When to Use?

Every Stored Procedure and Service where errors can occur.
