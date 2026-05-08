---
name: new-page-nextjs
description: Creates a new Next.js page with App Router pattern including loading skeleton. Use when creating new routes or pages in Next.js projects.
argument-hint: "[/path - description]"
---

შექმენი ახალი Next.js გვერდი App Router პატერნით.

## არგუმენტი

$ARGUMENTS — გვერდის path და აღწერა (მაგ: "/products/reviews - პროდუქტის შეფასებების გვერდი")

## შესაქმნელი ფაილები

1. `page.tsx` — გვერდის კომპონენტი
2. `loading.tsx` — Skeleton loading state

## პროცესი

1. წაიკითხე პროექტის primitives — თუ არსებობს
2. დაადგინე route group: (auth), (main), (dashboard)
3. შექმენი page.tsx
4. შექმენი loading.tsx შესაბამისი skeleton-ებით
5. გაუშვი linter შექმნილ ფაილებზე
6. აჩვენე checklist — რა დაკმაყოფილდა
