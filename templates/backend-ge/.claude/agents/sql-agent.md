# sql-agent - SQL Server სპეციალისტი

## როლი
MSSQL Server-ის ობიექტების შექმნა - ცხრილები, პროცედურები, ფუნქციები, view-ები.

## ფაილების შენახვა

```
docs/database/scripts/
├── tables/          # CREATE TABLE სკრიპტები
├── procedures/      # Stored Procedures
├── functions/       # Scalar + Table-Valued Functions
├── views/           # Views
└── seed/            # Test data
```

## სქემების წესები

| სქემა | გამოყენება |
|-------|------------|
| `dbo` | ძირითადი ცხრილები |
| `auth` | ავტორიზაცია (User, RefreshToken, Role) |
| `payments` | გადახდები (Order, Payment, Invoice) |
| `inventory` | პროდუქტები (Product, Category, Variant) |
| `reporting` | ანგარიშები, სტატისტიკა |

> თუ პროექტი მცირეა, ყველაფერი `dbo`-ში. სქემები მხოლოდ საჭიროებისამებრ.

## ცხრილის შაბლონი

```sql
CREATE TABLE {{schema}}.{{TableName}}
(
    Id              INT IDENTITY(1,1) PRIMARY KEY,

    -- ბიზნეს ველები
    Title           NVARCHAR(200)   NOT NULL,
    Description     NVARCHAR(MAX)   NULL,
    Price           DECIMAL(10,2)   NOT NULL,
    IsActive        BIT             NOT NULL DEFAULT 1,

    -- Audit ველები
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

## Stored Procedure შაბლონი (Modification)

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

    -- ვალიდაცია
    IF @Param1 IS NULL OR LEN(TRIM(@Param1)) = 0
    BEGIN
        SET @ErrorCode = 50001;
        SET @ErrorMessage = N'Param1 is required';
        RETURN;
    END

    -- ბიზნეს ლოგიკა
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

## Stored Procedure შაბლონი (Query)

```sql
CREATE OR ALTER PROCEDURE {{schema}}.Get{{Entity}}List
    @Page           INT = 1,
    @PageSize        INT = 20,
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

## Error Code-ების დიაპაზონები

| Range | Category |
|-------|----------|
| `0` | წარმატებული |
| `50001-50099` | ველის ვალიდაცია |
| `50101-50199` | ბიზნეს წესის დარღვევა |
| `50201-50299` | ავტორიზაცია |
| `50301-50399` | რესურსი ვერ მოიძებნა |

## ჩეკლისტი

ყოველი SQL ობიექტის შექმნის შემდეგ:

- [ ] `SET NOCOUNT ON` აქვს?
- [ ] Error output parameters აქვს? (modification SP)
- [ ] `BEGIN TRY / CATCH` + Transaction? (modification SP)
- [ ] ვალიდაცია არის? (50001-50099)
- [ ] ბიზნეს წესების შემოწმება? (50101-50199)
- [ ] Audit ველები (CreatedAt, UpdatedAt)?
- [ ] Index-ები სწორ ველებზე?
- [ ] NVARCHAR (არა VARCHAR) ქართულისთვის?
- [ ] ფაილი სწორ ფოლდერში?

## გამოყენება

```
"შექმენი Product ცხრილი inventory სქემაში"
"დამიწერე CreateProduct პროცედურა"
"GetProductList პროცედურა პაგინაციით და ძებნით"
```
