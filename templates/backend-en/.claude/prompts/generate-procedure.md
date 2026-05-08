# Stored Procedure Generator

## Instructions

Create a Stored Procedure with the following parameters:

**Name:** `{{schema}}.{{ProcedureName}}`
**Type:** {{Modification | Query}}
**Table:** `{{schema}}.{{TableName}}`

## Modification SP Structure

1. Output parameters: `@ErrorCode INT`, `@ErrorMessage NVARCHAR(500)`
2. `SET NOCOUNT ON`
3. Validation (50001-50099)
4. Business rule checks (50101-50199)
5. `BEGIN TRY / BEGIN TRANSACTION`
6. INSERT/UPDATE/DELETE
7. `COMMIT / END TRY / BEGIN CATCH / ROLLBACK`

## Query SP Structure

1. Parameters: `@Page`, `@PageSize`, `@Search`, `@TotalCount OUTPUT`
2. `SET NOCOUNT ON`
3. COUNT query → `@TotalCount`
4. SELECT with `OFFSET / FETCH NEXT`
5. `ORDER BY` is mandatory

## Error Codes

| Range | Category |
|-------|----------|
| `50001-50099` | Field validation |
| `50101-50199` | Business rule |
| `50201-50299` | Authorization |
| `50301-50399` | Not found |

## File Location

`docs/database/scripts/procedures/{{ProcedureName}}.sql`

## Checklist

- [ ] `CREATE OR ALTER PROCEDURE`
- [ ] `SET NOCOUNT ON`
- [ ] Error output parameters (modification)
- [ ] Validation with correct error codes
- [ ] TRY/CATCH + Transaction (modification)
- [ ] NVARCHAR for Unicode text
- [ ] Audit fields (CreatedAt, UpdatedAt, CreatedBy)
