# New API Endpoint Composition

Combines multiple primitives for creating a new API endpoint.

## Primitives Used

{{INCLUDE: ../primitives/MINIMAL_CONTROLLER.md}}
{{INCLUDE: ../primitives/HYBRID_REPOSITORY.md}}
{{INCLUDE: ../primitives/ERROR_TAXONOMY.md}}
{{INCLUDE: ../primitives/API_RESPONSE.md}}

## Instructions

### Input
- **Entity Name:** [ENTITY]
- **Operations:** [CRUD operations needed]
- **Special Business Rules:** [validation, business logic]

### Output Files

1. **Controller:** `Controllers/[Entity]Controller.cs`
2. **Service Interface:** `Interfaces/I[Entity]Service.cs`
3. **Service Implementation:** `Services/[Entity]Service.cs`
4. **Repository Interface:** `Interfaces/I[Entity]Repository.cs`
5. **Repository Implementation:** `Repositories/[Entity]Repository.cs`
6. **DTOs:** `DTOs/[Entity]/`
7. **Stored Procedure:** `docs/database/scripts/[Entity]/`

### Checklist

- [ ] Controller only calls service
- [ ] ApiResponse wrapper used everywhere
- [ ] Error codes in correct ranges
- [ ] Repository uses hybrid pattern
- [ ] DI registration added
