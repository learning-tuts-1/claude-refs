---
name: new-component
description: Creates a new React component following project conventions. Use when creating new UI or feature components.
argument-hint: "[ComponentName - description]"
---

შექმენი ახალი კომპონენტი პროექტის პატერნების მიხედვით.

## არგუმენტი

$ARGUMENTS — კომპონენტის სახელი და აღწერა (მაგ: "Tooltip - hover-ზე ინფორმაციის ჩვენება")

## პროცესი

1. წაიკითხე პროექტის primitives (COMPONENT_PATTERNS, TAILWIND_FIRST, DESIGN_TOKENS, TYPESCRIPT_STRICT, IMPORT_CONVENTIONS) — თუ არსებობს
2. დაადგინე კომპონენტის ტიპი: UI (`src/components/ui/`) თუ feature (`src/components/[feature]/`)
3. შექმენი ფაილი პროექტის არსებული პატერნებით
4. გაუშვი linter შექმნილ ფაილზე
5. აჩვენე checklist — რა დაკმაყოფილდა
