# HYBRID_REPOSITORY

## EF Core + Dapper Hybrid Pattern

### პრინციპი

- **EF Core** - reads (LINQ, Include, navigation properties)
- **Dapper** - writes (Stored Procedures, complex queries)

### EF Core (Reads)

```csharp
public async Task<Product?> GetByIdAsync(int id)
{
    return await _context.Products
        .Include(p => p.Category)
        .Include(p => p.Tags)
        .FirstOrDefaultAsync(p => p.Id == id);
}

public async Task<PagedResult<Product>> GetPagedAsync(ProductFilter filter)
{
    var query = _context.Products.AsQueryable();

    if (!string.IsNullOrEmpty(filter.Search))
        query = query.Where(p => p.Title.Contains(filter.Search));

    if (filter.CategoryId.HasValue)
        query = query.Where(p => p.CategoryId == filter.CategoryId);

    var totalCount = await query.CountAsync();
    var items = await query
        .OrderByDescending(p => p.CreatedAt)
        .Skip((filter.Page - 1) * filter.PageSize)
        .Take(filter.PageSize)
        .ToListAsync();

    return new PagedResult<Product>
    {
        Items = items,
        TotalCount = totalCount,
        PageNumber = filter.Page,
        PageSize = filter.PageSize
    };
}
```

### Dapper (Writes - Stored Procedures)

```csharp
public async Task<int> CreateAsync(CreateProductRequest request)
{
    var parameters = new DynamicParameters();
    parameters.Add("@Title", request.Title);
    parameters.Add("@Price", request.Price);
    parameters.Add("@CategoryId", request.CategoryId);
    parameters.Add("@NewId", dbType: DbType.Int32, direction: ParameterDirection.Output);
    parameters.Add("@ErrorCode", dbType: DbType.Int32, direction: ParameterDirection.Output);
    parameters.Add("@ErrorMessage", dbType: DbType.String, size: 500, direction: ParameterDirection.Output);

    await _connection.ExecuteAsync(
        "dbo.CreateProduct",
        parameters,
        commandType: CommandType.StoredProcedure);

    var errorCode = parameters.Get<int>("@ErrorCode");
    if (errorCode != 0)
    {
        var errorMessage = parameters.Get<string>("@ErrorMessage");
        throw new BusinessException(errorCode, errorMessage);
    }

    return parameters.Get<int>("@NewId");
}
```

### Repository Interface

```csharp
public interface IProductRepository
{
    // EF Core - reads
    Task<Product?> GetByIdAsync(int id);
    Task<PagedResult<Product>> GetPagedAsync(ProductFilter filter);

    // Dapper - writes
    Task<int> CreateAsync(CreateProductRequest request);
    Task UpdateAsync(int id, UpdateProductRequest request);
    Task DeleteAsync(int id);
}
```

### როდის გამოვიყენო?

**ყოველთვის** - reads EF Core-ით, writes Stored Procedures-ით.
