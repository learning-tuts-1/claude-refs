# Table გენერატორი

## ინსტრუქცია

შექმენი ცხრილი შემდეგი პარამეტრებით:

**სახელი:** `{{schema}}.{{TableName}}`
**აღწერა:** {{Description}}

## სტრუქტურა

```sql
CREATE TABLE {{schema}}.{{TableName}}
(
    -- Primary Key
    Id              INT IDENTITY(1,1) PRIMARY KEY,

    -- ბიზნეს ველები (შეავსე)
    ...

    -- სტატუსი
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

## წესები

- **IDENTITY(1,1)** Primary Key-სთვის
- **NVARCHAR** (არა VARCHAR) - ქართული სიმბოლოებისთვის
- **DATETIME2** (არა DATETIME) - მეტი precision
- **SYSUTCDATETIME()** - UTC დრო
- **Audit ველები** სავალდებულო: CreatedAt, UpdatedAt, CreatedBy, UpdatedBy
- **IsActive** soft delete-ისთვის
- **Index** ხშირად საძიებო ველებზე

## Naming

```sql
-- სწორი
dbo.Product, dbo.OrderItem, auth.User

-- არასწორი
dbo.tbl_Product, dbo.Products, dbo.TBL_ORDER_ITEM
```

## ფაილის შენახვა

`docs/database/scripts/tables/{{TableName}}.sql`

## ჩეკლისტი

- [ ] Primary Key (INT IDENTITY)
- [ ] NOT NULL / NULL სწორად
- [ ] Default values
- [ ] Foreign Key constraints
- [ ] Audit ველები (CreatedAt, UpdatedAt, CreatedBy, UpdatedBy)
- [ ] Index-ები საძიებო ველებზე
- [ ] NVARCHAR ტექსტისთვის
- [ ] Singular naming (Product, არა Products)
