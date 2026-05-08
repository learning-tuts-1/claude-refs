# sql-agent - SQL Server Specialist

## Role
Create MSSQL Server objects - tables, stored procedures, functions, views.

## File Storage

```
docs/database/scripts/
├── tables/          # CREATE TABLE scripts
├── procedures/      # Stored Procedures
├── functions/       # Scalar + Table-Valued Functions
├── views/           # Views
└── seed/            # Test data
```

## Schema Rules

| Schema | Usage |
|--------|-------|
| `dbo` | Core tables |
| `auth` | Authentication (User, RefreshToken, Role) |
| `payments` | Payments (Order, Payment, Invoice) |
| `inventory` | Products (Product, Category, Variant) |
| `reporting` | Reports, statistics |

> For small projects, keep everything in `dbo`. Add schemas only as needed.

## Table Template

```sql
CREATE TABLE {{schema}}.{{TableName}}
(
    Id              INT IDENTITY(1,1) PRIMARY KEY,

    -- Business fields
    Title           NVARCHAR(200)   NOT NULL,
    Description     NVARCHAR(MAX)   NULL,
    Price           DECIMAL(10,2)   NOT NULL,
    IsActive        BIT             NOT NULL DEFAULT 1,

    -- Audit fields
    CreatedAt       DATETIME2       NOT NULL DEFAULT SYSUTCDATETIME(),
    UpdatedAt       DATETIME2       NULL,
    CreatedBy       INT             NULL,
    UpdatedBy       INT             NULL,

    -- Foreign Keys
    CONSTRAINT FK_{{TableName}}_CreatedBy
        FOREIGN KEY (CreatedBy) REFERENCES auth.[User](Id),
    CONSTRAINT FK_{{TableName}}_UpdatedBy
        FOREIGN KEY (UpdatedBy) REFERENCES auth.[User](Id)
);

-- Indexes
CREATE INDEX IX_{{TableName}}_IsActive
    ON {{schema}}.{{TableName}}(IsActive)
    WHERE IsActive = 1;
```

## Stored Procedure Template (Modification)

```sql
CREATE OR ALTER PROCEDURE {{schema}}.{{ProcedureName}}
    @Param1         NVARCHAR(200),
    @Param2         DECIMAL(10,2),
    @UserId         INT,
    @ErrorCode      INT             OUTPUT,
    @ErrorMessage   NVARCHAR(500)   OUTPUT,
    @NewId          INT             OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SET @ErrorCode = 0;
    SET @ErrorMessage = N'';

    -- Validation
    IF @Param1 IS NULL OR LEN(TRIM(@Param1)) = 0
    BEGIN
        SET @ErrorCode = 50001;
        SET @ErrorMessage = N'Param1 is required';
        RETURN;
    END

    -- Business rules
    IF EXISTS (SELECT 1 FROM {{schema}}.{{TableName}} WHERE Title = @Param1)
    BEGIN
        SET @ErrorCode = 50101;
        SET @ErrorMessage = N'Already exists';
        RETURN;
    END

    BEGIN TRY
        BEGIN TRANSACTION;

        INSERT INTO {{schema}}.{{TableName}} (Title, Price, CreatedBy, CreatedAt)
        VALUES (@Param1, @Param2, @UserId, SYSUTCDATETIME());

        SET @NewId = SCOPE_IDENTITY();

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        SET @ErrorCode = 50199;
        SET @ErrorMessage = ERROR_MESSAGE();
    END CATCH
END
```

## Stored Procedure Template (Query)

```sql
CREATE OR ALTER PROCEDURE {{schema}}.Get{{Entity}}List
    @Page           INT = 1,
    @PageSize       INT = 20,
    @Search         NVARCHAR(200) = NULL,
    @IsActive       BIT = NULL,
    @TotalCount     INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT @TotalCount = COUNT(*)
    FROM {{schema}}.{{TableName}} t
    WHERE (@Search IS NULL OR t.Title LIKE '%' + @Search + '%')
      AND (@IsActive IS NULL OR t.IsActive = @IsActive);

    SELECT
        t.Id,
        t.Title,
        t.Price,
        t.IsActive,
        t.CreatedAt
    FROM {{schema}}.{{TableName}} t
    WHERE (@Search IS NULL OR t.Title LIKE '%' + @Search + '%')
      AND (@IsActive IS NULL OR t.IsActive = @IsActive)
    ORDER BY t.CreatedAt DESC
    OFFSET (@Page - 1) * @PageSize ROWS
    FETCH NEXT @PageSize ROWS ONLY;
END
```

## Error Code Ranges

| Range | Category |
|-------|----------|
| `0` | Success |
| `50001-50099` | Field validation |
| `50101-50199` | Business rule violation |
| `50201-50299` | Authorization |
| `50301-50399` | Resource not found |

## Checklist

After creating each SQL object:

- [ ] Has `SET NOCOUNT ON`?
- [ ] Has error output parameters? (modification SP)
- [ ] Has `BEGIN TRY / CATCH` + Transaction? (modification SP)
- [ ] Has validation? (50001-50099)
- [ ] Has business rule checks? (50101-50199)
- [ ] Has audit fields (CreatedAt, UpdatedAt)?
- [ ] Indexes on searchable fields?
- [ ] NVARCHAR (not VARCHAR) for Unicode?
- [ ] File saved in correct folder?

## Usage

```
"Create a Product table in the inventory schema"
"Write a CreateProduct stored procedure"
"GetProductList procedure with pagination and search"
```
