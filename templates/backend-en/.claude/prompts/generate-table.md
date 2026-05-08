# Table Generator

## Instructions

Create a table with the following parameters:

**Name:** `{{schema}}.{{TableName}}`
**Description:** {{Description}}

## Structure

```sql
CREATE TABLE {{schema}}.{{TableName}}
(
    -- Primary Key
    Id              INT IDENTITY(1,1) PRIMARY KEY,

    -- Business fields (fill in)
    ...

    -- Status
    IsActive        BIT             NOT NULL DEFAULT 1,

    -- Audit
    CreatedAt       DATETIME2       NOT NULL DEFAULT SYSUTCDATETIME(),
    UpdatedAt       DATETIME2       NULL,
    CreatedBy       INT             NULL,
    UpdatedBy       INT             NULL,

    -- Foreign Keys
    CONSTRAINT FK_{{TableName}}_CreatedBy
        FOREIGN KEY (CreatedBy) REFERENCES auth.[User](Id)
);
```

## Rules

- **IDENTITY(1,1)** for Primary Key
- **NVARCHAR** (not VARCHAR) - for Unicode characters
- **DATETIME2** (not DATETIME) - better precision
- **SYSUTCDATETIME()** - UTC time
- **Audit fields** required: CreatedAt, UpdatedAt, CreatedBy, UpdatedBy
- **IsActive** for soft delete
- **Index** on frequently searched fields

## Naming

```sql
-- Correct
dbo.Product, dbo.OrderItem, auth.User

-- Incorrect
dbo.tbl_Product, dbo.Products, dbo.TBL_ORDER_ITEM
```

## File Location

`docs/database/scripts/tables/{{TableName}}.sql`

## Checklist

- [ ] Primary Key (INT IDENTITY)
- [ ] NOT NULL / NULL correctly set
- [ ] Default values
- [ ] Foreign Key constraints
- [ ] Audit fields (CreatedAt, UpdatedAt, CreatedBy, UpdatedBy)
- [ ] Indexes on searchable fields
- [ ] NVARCHAR for text
- [ ] Singular naming (Product, not Products)
