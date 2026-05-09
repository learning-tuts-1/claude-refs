# claude-refs

დამხმარე რეპოზიტორია **Learning Tuts**-ის წიგნებისთვის: **„Claude Code — სრული სახელმძღვანელო"** და **„AI პრაქტიკული გზამკვლევი"**.

> 📘 ეს რეპოზიტორია შექმნილია წიგნის მკითხველებისთვის. ყველა skill, primitive, agent და template, რომელიც წიგნებშია განხილული, შეგიძლიათ პირდაპირ დააკოპიროთ და გამოიყენოთ თქვენს პროექტებში (copy-paste).

---

## 📂 რა არის აქ

### `skills/` — 31 skill

მრავალჯერადი გამოყენების (Reusable) Claude Code skill-ები 6 დომენისთვის:

| დომენი | რას ფარავს |
| --- | --- |
| [`developer-tools/`](https://www.google.com/search?q=skills/developer-tools) | Code quality, scaffolding (lint, type-check, new component, new page) |
| [`frontend/`]() | React, Tailwind, Electron, audio libraries |
| [`backend-dotnet/`]() | .NET ინტეგრაციები (Stripe, SignalR, Firebase, Cloudflare R2) |
| [`client-integrations/`]() | Browser SDK-ები (FB Pixel, GA4, Firebase Auth, FFmpeg-WASM) |
| [`cms/`]() | Sanity CMS workflow |
| [`writing/`]() | Prose, AI-ism detection, grill-me interviewing |
| [`analysis/`]() | Business analyst, deep-investigation, mermaid diagrams, invoice organizer |

თითოეულ skill-ს აქვს `SKILL.md` ფაილი შესაბამისი frontmatter-ით (`name`, `description`, `triggers`). უბრალოდ ჩააგდეთ ის თქვენი პროექტის `.claude/skills/` ფოლდერში და მზადაა გამოსაყენებლად.

### `templates/` — 5 საწყისი (Starter) პროექტი

სრული `.claude/` ფოლდერების ნიმუშები ახალი პროექტებისთვის:

| ნიმუში | აუდიტორია |
| --- | --- |
| [`frontend-ge/`]() | Frontend პროექტი — ქართული ინსტრუქციებით |
| [`frontend-en/`]() | Frontend პროექტი — ინგლისური ინსტრუქციებით |
| [`backend-ge/`]() | Backend პროექტი — ქართული ინსტრუქციებით |
| [`backend-en/`]() | Backend პროექტი — ინგლისური ინსტრუქციებით |
| [`global/`]() | Global Claude Code პარამეტრები (`~/.claude/`) |

თითოეული ნიმუში უკვე გამზადებულია და მოიცავს შემდეგ ფოლდერებს/ფაილებს: `CLAUDE.md` + `primitives/` + `prompts/` + `compositions/` + `agents/` + `skills/`.

**დამატებით:**

* [`templates/CONCEPTS.md`]() — Primitives, Skills, Prompts, Agents — რა განსხვავებაა მათ შორის?
* [`templates/PROJECT_WORKFLOW.md`]() — სრული სამუშაო პროცესი (Flow): idea → plan → build → ship
* [`templates/plan-template/`]() — ფაზური დაგეგმარების შაბლონი (Template)

---

## 🚀 გამოყენების ინსტრუქცია

### ახალი პროექტისთვის (Template-ის გამოყენება)

```bash
# დააკოპირეთ შესაფერისი template-ი
cp -r templates/frontend-ge/.claude my-project/.claude
cp templates/frontend-ge/CLAUDE.md my-project/CLAUDE.md

# გახსენით Claude Code
cd my-project
claude

```

### არსებულ პროექტში skill-ის დამატება

```bash
# მაგალითად: lint + typecheck skill-ის დამატება
cp -r skills/developer-tools/check .claude/skills/check

```

---

## 📚 წიგნების შესახებ

ეს რეპოზიტორია მხოლოდ პრაქტიკული დანამატია. იმისათვის, რომ კარგად გაიაზროთ ამ პრაქტიკული გადაწყვეტილებების მიღმა არსებული ლოგიკა, გაეცანით წიგნებს:

* **„Claude Code — სრული სახელმძღვანელო"** (110 გვერდი, ქართულად) — დეველოპერებისა და ანალიტიკოსებისთვის.
* **„AI პრაქტიკული გზამკვლევი"** (169 გვერდი, ქართულად) — ბიზნესის მფლობელებისთვის, მარკეტერებისა და ფრილანსერებისთვის.

წიგნების შეძენა შეგიძლიათ Facebook-ის მეშვეობით (თითოეულის ფასი — 29 ₾, ორივეს ერთად შეძენისას — 49 ₾).

---

## 🤝 კონტრიბუცია (Contribution)

ეს არის რჩეული (curated) კოლექცია — თითოეული skill და template რეალურ (Production) გარემოშია დატესტილი.

უკუკავშირისთვის (Feedback) ან კითხვებისთვის, გთხოვთ, გამოიყენოთ ამ რეპოზიტორიის GitHub Issues.

---

## ⚖️ ლიცენზია

MIT — გამოიყენეთ თავისუფლად, მათ შორის კომერციულ პროექტებშიც. ერთადერთი თხოვნა იქნება: თუ რამეს გააუმჯობესებთ, გამოგვიგზავნეთ PR (Pull Request).

---

**English short version:** Companion repo by **Learning Tuts** for two Georgian-language books on Claude Code and general AI productivity. Contains 31 reusable skills + 5 starter project templates with `.claude/` folders pre-configured. MIT licensed.
