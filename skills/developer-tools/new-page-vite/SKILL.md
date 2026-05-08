---
name: new-page-vite
description: Creates a new page in Vite SPA with React Router. Use when creating new routes or pages in Vite + React Router projects.
argument-hint: "[/path - description]"
---

შექმენი ახალი გვერდი Vite + React Router პატერნით.

## არგუმენტი

$ARGUMENTS — გვერდის path და აღწერა (მაგ: "/appointments/new - ახალი ჯავშნის შექმნა")

## შესაქმნელი ფაილები

1. `src/pages/FeaturePage.tsx` — გვერდის კომპონენტი (named export)
2. `src/App.tsx` — Route registration

## პროცესი

1. წაიკითხე პროექტის primitives — თუ არსებობს
2. დაადგინე route path
3. შექმენი page component `src/pages/`-ში
4. დაამატე Route `src/App.tsx`-ში
5. გაუშვი linter შექმნილ ფაილებზე
6. აჩვენე checklist — რა დაკმაყოფილდა
