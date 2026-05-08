# Stored Procedure გენერატორი

## ინსტრუქცია

შექმენი Stored Procedure შემდეგი პარამეტრებით:

**სახელი:** `{{schema}}.{{ProcedureName}}`
**ტიპი:** {{Modification | Query}}
**ცხრილი:** `{{schema}}.{{TableName}}`

## Modification SP-ის სტრუქტურა

1. Output parameters: `@ErrorCode INT`, `@ErrorMessage NVARCHAR(500)`
2. `SET NOCOUNT ON`
3. ვალიდაცია (50001-50099)
4. ბიზნეს წესების შემოწმება (50101-50199)
5. `BEGIN TRY / BEGIN TRANSACTION`
6. INSERT/UPDATE/DELETE
7. `COMMIT / END TRY / BEGIN CATCH / ROLLBACK`

## Query SP-ის სტრუქტურა

1. პარამეტრები: `@Page`, `@PageSize`, `@Search`, `@TotalCount OUTPUT`
2. `SET NOCOUNT ON`
3. COUNT query → `@TotalCount`
4. SELECT with `OFFSET / FETCH NEXT`
5. `ORDER BY` სავალდებულო

## Error Codes

| Range | Category |
|-------|----------|
| `50001-50099` | ველის ვალიდაცია |
| `50101-50199` | ბიზნეს წესი |
| `50201-50299` | ავტორიზაცია |
| `50301-50399` | ვერ მოიძებნა |

## ფაილის შენახვა

`docs/database/scripts/procedures/{{ProcedureName}}.sql`

## ჩეკლისტი

- [ ] `CREATE OR ALTER PROCEDURE`
- [ ] `SET NOCOUNT ON`
- [ ] Error output parameters (modification)
- [ ] ვალიდაცია სწორ error code-ებით
- [ ] TRY/CATCH + Transaction (modification)
- [ ] NVARCHAR ქართულისთვის
- [ ] Audit ველები (CreatedAt, UpdatedAt, CreatedBy)
