# .claude/ კონცეფციები

## TL;DR

```
Primitive  = წესი          (შენი პროექტის კანონი)
Skill      = ცოდნა         (ტექნოლოგიის reference)
Prompt     = შაბლონი       (ფაილის scaffold)
Agent      = შემსრულებელი  (როლი, რომელიც იყენებს ზემოთ სამივეს)
Composition = workflow      (რამდენიმე primitive-ის კომბინაცია)
```

---

## 1. Primitive - წესი

**რა არის:** ერთი კონკრეტული წესი ან პატერნი შენს პროექტში.

**Project-specific?** დიახ, 100%. ეს შენი პროექტის კანონია.

**ზომა:** 20-50 ხაზი

**მაგალითი:**
```
TAILWIND_FIRST.md     → "არა custom CSS, არა hardcoded ფერები"
MINIMAL_CONTROLLER.md → "Controller-ში მხოლოდ routing + ApiResponse"
SEMICOLONS.md         → "ყოველი statement სემიკოლონით"
GIT_RULES.md          → "არასდროს დაფუშო ჩემი ნებართვის გარეშე"
```

**რატომ არის მნიშვნელოვანი:**
```
Claude შეცდომას უშვებს (hardcoded ფერი)
  → შენ ამატებ primitive-ს: DESIGN_TOKENS.md
    → Claude აღარასდროს გაიმეორებს
      → დროთა განმავლობაში: ნაკლები შეცდომა
```

ეს არის **compounding effect** - შენი .claude/ ფოლდერი ჭკვიანდება ყოველი პროექტით.

---

## 2. Skill - ცოდნა

**რა არის:** ტექნოლოგიის reference/ცნობარი. როგორ მუშაობს კონკრეტული ბიბლიოთეკა ან ტექნოლოგია.

**Project-specific?** არა. Skill გადატანადია პროექტებს შორის.

**ზომა:** 50-100 ხაზი

**მაგალითი:**
```
tailwind-v4.md      → "ასე მუშაობს @theme, oklch, design tokens"
explain-code.md     → "კოდი ახსენი ASCII დიაგრამით + Gotchas"
stripe-payments.md  → "ასე იქმნება Checkout Session, Webhook"
firebase-admin.md   → "ასე ვერიფიცირდება ID Token"
```

**განსხვავება Primitive-სგან:**

| | Primitive | Skill |
|---|-----------|-------|
| **რა** | წესი (რა არ უნდა გააკეთო) | ცოდნა (როგორ მუშაობს) |
| **Project-specific** | დიახ | არა |
| **მაგალითი** | "არა hardcoded ფერები" | "Tailwind v4-ში @theme ასე მუშაობს" |
| **იცვლება?** | იშვიათად | ვერსიასთან ერთად |

---

## 3. Prompt - შაბლონი

**რა არის:** კონკრეტული ტიპის ფაილის scaffold/template. რა სტრუქტურა უნდა ჰქონდეს ფაილს.

**Project-specific?** ნახევრად. სტრუქტურა უნივერსალურია, დეტალები პროექტის.

**ზომა:** 30-50 ხაზი

**მაგალითი:**
```
new-component.md        → "ასე შექმენი React კომპონენტი (forwardRef, cn(), props)"
new-page.md             → "ასე შექმენი route/page (loader, meta, layout)"
generate-procedure.md   → "ასე შექმენი Stored Procedure (validation, TRY/CATCH)"
generate-table.md       → "ასე შექმენი ცხრილი (audit fields, indexes)"
```

**როდის იხმარება:** Claude-ს ეუბნები "შექმენი კომპონენტი" → ის კითხულობს prompt-ს → იცის რა სტრუქტურა სჭირდება.

---

## 4. Agent - შემსრულებელი

**რა არის:** როლის განსაზღვრა. ვინ არის, რა იცის, რა ინსტრუმენტებს იყენებს.

**Project-specific?** ნახევრად. როლი უნივერსალურია, კონტექსტი პროექტის.

**ზომა:** 50+ ხაზი

**მაგალითი:**
```
ui-developer.md   → "შენ ხარ UI სპეციალისტი, იყენებ TAILWIND_FIRST + DESIGN_TOKENS"
sql-agent.md      → "შენ ხარ SQL სპეციალისტი, იყენებ ERROR_TAXONOMY + generate-procedure"
docs-explorer.md  → "შენ ხარ მკვლევარი, ეძებ Context7 → llms.txt → official docs"
code-reviewer.md  → "შენ ხარ რევიუერი, ამოწმებ TYPESCRIPT_STRICT + GIT_RULES"
```

**Agent-ის ანატომია:**
```
Agent = როლი + კონტექსტი + ინსტრუმენტები

sql-agent:
  როლი:         SQL Server სპეციალისტი
  იყენებს:
    primitive:   ERROR_TAXONOMY.md (error code-ების წესი)
    prompt:      generate-procedure.md (SP შაბლონი)
    prompt:      generate-table.md (ცხრილის შაბლონი)
    skill:       — (არ სჭირდება external tech reference)
  აკეთებს:      ცხრილებს, პროცედურებს, view-ებს
```

---

## 5. Composition - Workflow

**რა არის:** რამდენიმე primitive-ის კომბინაცია ერთი დიდი task-ისთვის.

**Project-specific?** დიახ. შენი არქიტექტურის workflow.

**ზომა:** 50-100 ხაზი

**მაგალითი:**
```
new-api-endpoint.md → MINIMAL_CONTROLLER + HYBRID_REPOSITORY + ERROR_TAXONOMY + API_RESPONSE
new-feature.md      → TAILWIND_FIRST + TYPESCRIPT_STRICT + DESIGN_TOKENS + FORWARDREF_COMPONENT
```

**როდის:** როცა ერთი task რამდენიმე ფაილს ქმნის ერთდროულად.

---

## იერარქია

```
                    ┌─────────────┐
                    │    Agent    │  ← შემსრულებელი
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │Primitive │ │  Skill   │ │  Prompt  │
        │  (წესი)  │ │ (ცოდნა)  │ │(შაბლონი) │
        └──────────┘ └──────────┘ └──────────┘
              │
              ▼
        ┌─────────────┐
        │ Composition │  ← რამდენიმე primitive ერთად
        └─────────────┘
```

**Agent** იყენებს ყველაფერს:
- **Primitive** - რა წესები დაიცვას
- **Skill** - რა ტექნოლოგია იცოდეს
- **Prompt** - რა შაბლონით შექმნას ფაილი

---

## პრაქტიკული მაგალითი

```
შენ: "შექმენი CreateProduct stored procedure"

Claude-ის ტვინში:
  1. Agent: sql-agent.md → "მე ვარ SQL სპეციალისტი"
  2. Prompt: generate-procedure.md → "SP ასე უნდა გამოიყურებოდეს"
  3. Primitive: ERROR_TAXONOMY.md → "50001-50099 ვალიდაცია, 50101-50199 ბიზნეს წესი"
  4. შედეგი: სწორი SP სწორი error code-ებით
```

```
შენ: "შექმენი ProductCard კომპონენტი"

Claude-ის ტვინში:
  1. Agent: ui-developer.md → "მე ვარ UI სპეციალისტი"
  2. Prompt: new-component.md → "კომპონენტი forwardRef-ით, cn()-ით"
  3. Primitive: TAILWIND_FIRST.md → "არა custom CSS"
  4. Primitive: DESIGN_TOKENS.md → "ფერები token-ებით"
  5. Skill: tailwind-v4.md → "@theme ასე მუშაობს"
  6. შედეგი: სწორი კომპონენტი design system-ით
```

---

## რა არის Project-Specific და რა არა?

| კონცეფცია | Project-Specific | გადატანადი |
|-----------|:---:|:---:|
| **Primitive** | **დიახ** | ნაწილობრივ (GIT_RULES უნივერსალურია) |
| **Skill** | არა | **დიახ** (ტექნოლოგია არ იცვლება) |
| **Prompt** | ნახევრად | ნახევრად (სტრუქტურა იგივეა) |
| **Agent** | ნახევრად | ნახევრად (როლი იგივეა, კონტექსტი იცვლება) |
| **Composition** | **დიახ** | არა (შენი არქიტექტურის workflow) |

---

## როდის რას ვქმნი?

| სიტუაცია | რას ვქმნი |
|----------|-----------|
| Claude არასწორად აკეთებს რაღაცას | **Primitive** (წესი) |
| ახალი ტექნოლოგია/ბიბლიოთეკა გვჭირდება | **Skill** (ცოდნა) |
| ერთი ტიპის ფაილს ხშირად ვქმნი | **Prompt** (შაბლონი) |
| რამდენიმე ფაილს ერთდროულად ვქმნი | **Composition** (workflow) |
| სპეციალიზებული task-ი ხშირად მეორდება | **Agent** (შემსრულებელი) |
