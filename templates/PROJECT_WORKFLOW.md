# Project Workflow - Claude Code Expert Guide

როგორ წავიყვანო პროექტი იდეიდან პროდაქშენამდე Claude Code-ით.

---

## TL;DR - 4 ფაზა

```
IDEA → PLAN → BUILD → SHIP
 │       │       │       │
 │       │       │       └── Deploy, monitor
 │       │       └── ერთი feature → test → commit → next
 │       └── დეტალური დაგეგმვა: tasks, deps, files
 └── Vision, design system, architecture
```

---

## ფაზა 0: IDEA (პროექტის დაწყება)

### რა ვქნა პირველი?

1. **შექმენი პროექტის root ფოლდერი**
2. **დაწერე `docs/vision.md`** - რა არის პროექტი, ვისთვისაა, რა პრობლემას ჭრის
3. **შექმენი Design System** - `docs/design/` (ფერები, ტიპოგრაფია, კომპონენტები)
4. **დააკოპირე `.claude/` template** - claude-templates-დან
5. **დაწერე `CLAUDE.md`** - პროექტის წესები

### ფოლდერის სტრუქტურა (Day 1)

```
my-project/
├── CLAUDE.md                    # Claude-ს ინსტრუქციები
├── .claude/
│   ├── primitives/              # template-დან
│   ├── prompts/
│   ├── compositions/
│   └── agents/
├── docs/
│   ├── vision.md                # პროექტის ვიზია
│   ├── design/
│   │   ├── style-guide.md       # Design system
│   │   ├── design-tokens.json   # Color/spacing tokens
│   │   └── components/          # Component specs
│   └── architecture/
│       └── overview.md          # Tech decisions
└── plan/                        # <<<< ეს არის ახალი
    └── README.md                # Plan-ის overview
```

---

## ფაზა 1: PLAN (დაგეგმვა)

### plan/ ფოლდერის სტრუქტურა

```
plan/
├── README.md                    # Master plan - features list + priority
├── v1/                          # Version / Milestone
│   ├── 01-auth/                 # Feature #1
│   │   ├── PLAN.md              # Feature plan + tasks
│   │   ├── dependencies.md      # რაზეა დამოკიდებული
│   │   └── STATUS.md            # სტატუსი (optional)
│   ├── 02-products/             # Feature #2
│   │   ├── PLAN.md
│   │   └── dependencies.md
│   ├── 03-cart/                 # Feature #3
│   │   ├── PLAN.md
│   │   └── dependencies.md
│   └── DEPENDENCY_GRAPH.md      # რომელი feature რომელს ელოდება
└── backlog/                     # მომავალი იდეები
    └── ideas.md
```

### README.md (Master Plan)

```markdown
# Project Plan

## V1 - MVP Features

| # | Feature | Priority | Status | Dependencies |
|---|---------|----------|--------|--------------|
| 01 | Auth System | Critical | Not Started | - |
| 02 | Products CRUD | Critical | Not Started | 01-auth (partial) |
| 03 | Cart | High | Not Started | 01-auth, 02-products |
| 04 | Checkout | High | Not Started | 03-cart |
| 05 | Admin Panel | Medium | Not Started | 01-auth, 02-products |

## Build Order (Dependency-based)

```
Phase A (parallel-ში):
  [01-auth: backend]  ←── ეს პირველი
  [02-products: backend] ←── ეს პარალელურად

Phase B:
  [01-auth: frontend]  ←── auth backend-ის შემდეგ
  [02-products: frontend]

Phase C:
  [03-cart]  ←── auth + products ready

Phase D:
  [04-checkout]  ←── cart ready
```
```

### Feature PLAN.md შაბლონი

```markdown
# Feature: {{Feature Name}}

## Overview
რა არის ეს feature და რატომ გვჭირდება.

## Tasks

### Backend
- [ ] DB: Create {{table}} table + migration
- [ ] DB: Create stored procedures
- [ ] API: {{Entity}}Controller
- [ ] API: {{Entity}}Service
- [ ] API: {{Entity}}Repository
- [ ] API: DTOs (Request/Response)
- [ ] Test: API endpoint tests

### Frontend
- [ ] Types: {{feature}} interfaces
- [ ] API: client methods
- [ ] Hook: use{{Feature}}
- [ ] Page: {{Feature}}Page
- [ ] Components: {{Feature}}List, {{Feature}}Card
- [ ] Test: component tests

### Integration
- [ ] E2E: full flow test

## Dependencies

### Depends On (Blocked By):
- `01-auth` - JWT token for API calls

### Blocks:
- `03-cart` - needs product data

## Notes
- Edge cases
- Design decisions
- Open questions
```

### dependencies.md შაბლონი

```markdown
# Dependencies: {{Feature Name}}

## Upstream (რაზე ვართ დამოკიდებული)

| Feature | რა გვჭირდება | Status |
|---------|-------------|--------|
| 01-auth | JWT middleware, User entity | Not Started |
| Database | MSSQL running | Ready |

## Downstream (ვინ არის ჩვენზე დამოკიდებული)

| Feature | რა უჭირდება ჩვენგან |
|---------|-------------------|
| 03-cart | Product entity, API endpoints |
| 05-admin | Product CRUD API |
```

### DEPENDENCY_GRAPH.md

```markdown
# Dependency Graph

```
                    ┌──────────┐
                    │ Database │
                    └────┬─────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          │
        ┌──────────┐ ┌──────────┐  │
        │ 01-Auth  │ │02-Products│  │
        │ Backend  │ │ Backend  │  │
        └────┬─────┘ └────┬─────┘  │
             │             │        │
        ┌────▼─────┐ ┌────▼─────┐  │
        │ 01-Auth  │ │02-Products│  │
        │ Frontend │ │ Frontend │  │
        └────┬─────┘ └────┬─────┘  │
             │             │        │
             └──────┬──────┘        │
                    │               │
               ┌────▼─────┐        │
               │ 03-Cart  │        │
               └────┬─────┘        │
                    │               │
               ┌────▼─────┐        │
               │04-Checkout│        │
               └───────────┘        │
                                    │
               ┌──────────┐        │
               │ 05-Admin │◄───────┘
               └──────────┘
```
```

---

## ფაზა 2: BUILD (იმპლემენტაცია)

### Claude Code-ით მუშაობის სწორი ფორმატი

**არასწორი approach:**
```
"შექმენი auth system" → Claude წერს ყველაფერს ერთხელ → 500 ხაზი → bugs
```

**სწორი approach:**
```
Step 1: "წაიკითხე plan/v1/01-auth/PLAN.md"
Step 2: "შექმენი მხოლოდ DB table migration" (1 task)
Step 3: review + commit
Step 4: "შექმენი CreateUser stored procedure" (1 task)
Step 5: review + commit
...
```

### ერთი სესიის workflow

```
1. გახსენი Claude Code
2. მიუთითე სად ხარ:
   "ვმუშაობ plan/v1/02-products/ feature-ზე.
    წაიკითხე PLAN.md და dependencies.md"

3. Claude კითხულობს plan-ს

4. მიუთითე კონკრეტული task:
   "შექმენი მხოლოდ ProductsController + ProductService.
    გამოიყენე compositions/new-api-endpoint.md"

5. Review → test → commit

6. PLAN.md-ში მონიშნე [x] გაკეთებული task

7. შემდეგი task...
```

### Plan Mode-ის სწორი გამოყენება

**Claude Code-ის plan mode** გამოიყენე **მხოლოდ** ერთი feature-ის ფარგლებში:

```
"plan mode-ში დავგეგმოთ როგორ გავაკეთო Products API.
 არ დაიწყო იმპლემენტაცია, მხოლოდ გეგმა დამიწერე.
 გეგმა ჩაწერე plan/v1/02-products/PLAN.md-ში."
```

### კონტექსტის გასუფთავების შემდეგ

როცა ახალ სესიას იწყებ:

```
"გავაგრძელოთ მუშაობა.
 წაიკითხე:
 1. CLAUDE.md
 2. plan/v1/02-products/PLAN.md
 3. plan/v1/02-products/dependencies.md

 სად ვარ: Backend tasks თითქმის მზადაა, Frontend-ზე გადავდივარ.
 შემდეგი task: 'Hook: useProducts'"
```

---

## ფაზა 3: docs/ ფოლდერი

### სტრუქტურა

```
docs/
├── vision.md                    # პროექტის ვიზია, მიზანი
├── design/
│   ├── README.md                # Design system overview
│   ├── style-guide.md           # ფერები, ტიპოგრაფია, spacing
│   ├── design-tokens.json       # Tokens JSON
│   └── components/              # Component specs (button.md, card.md...)
├── architecture/
│   ├── overview.md              # Tech stack decisions
│   ├── auth-system.md           # Auth flow diagram
│   ├── database-schema.md       # ERD, tables
│   └── api-design.md            # API endpoints, response format
├── api/
│   ├── auth.md                  # Auth endpoints documentation
│   ├── products.md              # Products API
│   └── orders.md                # Orders API
└── user-stories/
    ├── 01-registration.md       # User story: registration
    └── 02-purchase-flow.md      # User story: buying a product
```

### docs vs plan

| | docs/ | plan/ |
|---|------|-------|
| **რა** | HOW (როგორ მუშაობს) | WHAT/WHEN (რა გავაკეთოთ) |
| **ვისთვის** | Developer reference | Project management |
| **როდის** | იმპლემენტაციის შემდეგ | იმპლემენტაციის წინ |
| **მაგალითი** | "Auth API იყენებს JWT tokens" | "[ ] შექმენი Auth API" |

---

## ფაზა 4: Build Order - რა გააკეთო პირველი?

### Full-Stack პროექტის თანმიმდევრობა

```
1. PROJECT SETUP
   ├── Git repo init
   ├── CLAUDE.md + .claude/ setup
   ├── docs/vision.md
   └── plan/ structure

2. DESIGN
   ├── docs/design/style-guide.md
   ├── docs/design/design-tokens.json
   └── Reference images

3. DATABASE
   ├── Schema design (docs/architecture/database-schema.md)
   ├── Create tables
   └── Seed data

4. BACKEND (API)
   ├── Project setup (.NET/Node)
   ├── Auth system (JWT, middleware)
   ├── Core entities CRUD
   └── Test endpoints

5. FRONTEND
   ├── Project setup (React/Next/Remix)
   ├── Design system components (Button, Input, Card...)
   ├── Layout (Header, Footer, Sidebar)
   ├── Auth pages (Login, Register)
   ├── Core pages
   └── API integration

6. INTEGRATION
   ├── Frontend ↔ Backend connection
   ├── Auth flow E2E
   └── Core flows E2E

7. POLISH
   ├── Error handling
   ├── Loading states
   ├── Responsive design
   └── Accessibility
```

### თითოეული ნაბიჯის ზომა

**არასწორი:** "შექმენი მთელი Auth system" (ძალიან დიდი)
**სწორი:** ცალ-ცალკე tasks:

```
Auth System breakdown:
├── DB: Users table                    (15 min)
├── DB: CreateUser SP                  (10 min)
├── DB: ValidateUser SP                (10 min)
├── API: AuthController                (10 min)
├── API: AuthService                   (20 min)
├── API: JWT token generation          (15 min)
├── API: Auth middleware               (15 min)
├── Frontend: Auth types               (5 min)
├── Frontend: API client auth methods  (10 min)
├── Frontend: AuthContext              (15 min)
├── Frontend: Login page               (20 min)
├── Frontend: Register page            (15 min)
└── Integration test                   (15 min)
```

---

## CLAUDE.md-ში რა ჩავწერო Plan-ისთვის?

დაამატე ეს სექცია შენს CLAUDE.md-ში:

```markdown
## Planning Rules

### Plan Mode
- Plan mode-ში **მხოლოდ დაგეგმე**, არ დაიწყო იმპლემენტაცია
- გეგმა ჩაწერე `plan/` ფოლდერში შესაბამის feature-ის PLAN.md-ში
- ყოველი feature-ისთვის: tasks list + dependencies

### Implementation
- ერთ დროს **ერთი task** - არა მთელი feature ერთხელ
- ყოველი task-ის შემდეგ: review → test → commit
- PLAN.md-ში მონიშნე [x] გაკეთებული tasks

### Context Recovery
როცა ახალ სესიას ვიწყებ, ჯერ წაიკითხე:
1. CLAUDE.md
2. plan/ - მიმდინარე feature-ის PLAN.md
3. dependencies.md

### Task Size
- ერთი task = ერთი commit
- მაქსიმუმ 2-3 ფაილის ცვლილება
- თუ task ძალიან დიდია, დაშალე
```

---

## Quick Reference Card

```
ახალი პროექტი:
1. mkdir project && cd project
2. cp -r claude-templates/frontend-ge/.claude .claude
3. cp claude-templates/frontend-ge/CLAUDE.md CLAUDE.md
4. mkdir -p plan/v1 docs/{design,architecture}
5. დაწერე docs/vision.md
6. დაწერე plan/README.md (features list)

ახალი Feature:
1. mkdir plan/v1/XX-feature-name
2. Claude: "დაგეგმე ეს feature, ჩაწერე plan/v1/XX-feature-name/PLAN.md-ში"
3. Review plan
4. Claude: "დაიწყე პირველი task: [specific task]"

ახალი სესია (კონტექსტი გასუფთავებული):
1. Claude: "წაიკითხე CLAUDE.md და plan/v1/XX-feature/PLAN.md"
2. Claude: "სად ვარ: [last completed task]. შემდეგი: [next task]"

Feature-ის დასრულება:
1. ყველა task [x] in PLAN.md
2. plan/README.md-ში Status = "Done"
3. docs/-ში დაამატე documentation
4. შემდეგ feature-ზე გადავდივარ
```
