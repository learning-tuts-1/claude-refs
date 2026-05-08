# New API Endpoint Composition

ეს არის composition ახალი API endpoint-ის შესაქმნელად.

## გამოყენებული Primitives

{{INCLUDE: ../primitives/MINIMAL_CONTROLLER.md}}
{{INCLUDE: ../primitives/HYBRID_REPOSITORY.md}}
{{INCLUDE: ../primitives/ERROR_TAXONOMY.md}}
{{INCLUDE: ../primitives/API_RESPONSE.md}}

## Instructions

შექმენი ახალი API endpoint შემდეგი სპეციფიკაციით:

### Input
- **Entity Name:** [ENTITY]
- **Operations:** [CRUD operations needed]
- **Special Business Rules:** [validation, business logic]

### Output Files

1. **Controller:** `Controllers/[Entity]Controller.cs`
   - MINIMAL_CONTROLLER pattern
   - ApiResponse wrapper

2. **Service Interface:** `Interfaces/I[Entity]Service.cs`

3. **Service Implementation:** `Services/[Entity]Service.cs`

4. **Repository Interface:** `Interfaces/I[Entity]Repository.cs`

5. **Repository Implementation:** `Repositories/[Entity]Repository.cs`
   - HYBRID_REPOSITORY pattern

6. **DTOs:** `DTOs/[Entity]/`
   - Create[Entity]Request.cs
   - Update[Entity]Request.cs
   - [Entity]FilterRequest.cs
   - [Entity]Response.cs

7. **Stored Procedure:** `docs/database/scripts/[Entity]/`
   - ERROR_TAXONOMY codes

### Checklist

- [ ] Controller მხოლოდ service-ს იძახებს
- [ ] ApiResponse wrapper გამოყენებულია
- [ ] Error codes სწორი დიაპაზონებშია
- [ ] Repository hybrid pattern-ით
- [ ] DI registration-ში დამატებულია
