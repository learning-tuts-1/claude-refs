---
name: check
description: Runs Biome linting and TypeScript type-checking together. Use when verifying code quality, running lint checks, or checking types before committing.
---

Biome lint + TypeScript type-check ერთად.

## ნაბიჯები

1. გაუშვი `npx biome check src/`
2. გაუშვი `npx tsc --noEmit`
3. თუ შეცდომებია — დააჯგუფე კატეგორიებად (lint, format, type errors)
4. მოკლედ აჩვენე შედეგი: რამდენი ფაილი შემოწმდა, რამდენი error/warning

თუ $ARGUMENTS მითითებულია, მხოლოდ ის ფაილები შეამოწმე.
