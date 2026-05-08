# GIT_RULES

## Git წესები

### აკრძალული მოქმედებები

1. **არასდროს დაფუშო** ჩემი ნებართვის გარეშე
   ```bash
   # არასწორი - ავტომატური push
   git push origin main

   # სწორი - ჯერ მკითხე
   git add . && git commit -m "message"
   # დაელოდე ნებართვას
   ```

2. **არასდროს გამოიყენო Co-Authored-By: Claude**
   ```bash
   # არასწორი
   git commit -m "Add feature

   Co-Authored-By: Claude..."

   # სწორი
   git commit -m "Add feature"
   ```

3. **არასდროს force push main/master-ზე**

### კომიტის მესიჯების ფორმატი

```
type: short description

type შეიძლება იყოს:
- feat: ახალი ფუნქციონალი
- fix: ბაგის გასწორება
- refactor: კოდის რესტრუქტურიზაცია
- style: სტილის ცვლილება
- docs: დოკუმენტაცია
- test: ტესტები
- chore: სხვა
```

### მაგალითები

```bash
git commit -m "feat: add product filtering by genre"
git commit -m "fix: resolve cart item count mismatch"
git commit -m "refactor: extract useProducts hook"
```
