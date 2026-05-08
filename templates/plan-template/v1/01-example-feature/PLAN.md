# Feature: {{Feature Name}}

## Overview
{{What is this feature and why do we need it}}

## Tasks

### Database
- [ ] Create {{table}} table + migration
- [ ] Create stored procedures (CRUD)
- [ ] Seed data (if needed)

### Backend API
- [ ] {{Entity}}Controller
- [ ] I{{Entity}}Service interface
- [ ] {{Entity}}Service implementation
- [ ] I{{Entity}}Repository interface
- [ ] {{Entity}}Repository implementation
- [ ] DTOs: Create/Update Request, Response, Filter
- [ ] Register in DI container
- [ ] Test: API endpoint tests

### Frontend
- [ ] Types: {{feature}} interfaces
- [ ] API: client methods for {{feature}}
- [ ] Hook: use{{Feature}} (query + mutations)
- [ ] Page: {{Feature}}Page
- [ ] Components: {{Feature}}List, {{Feature}}Card, {{Feature}}Form
- [ ] Route: add to router
- [ ] Test: component tests

### Integration
- [ ] Full flow test (Frontend → API → DB)

## Dependencies

### Depends On (Blocked By):
- {{other feature}} - {{what we need from it}}

### Blocks:
- {{downstream feature}} - {{what they need from us}}

## Notes
- {{Edge cases, design decisions, open questions}}
