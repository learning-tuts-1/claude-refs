# claude-refs

Companion repository for the books **„Claude Code — სრული სახელმძღვანელო"** and **„AI პრაქტიკული გზამკვლევი"** by **Learning Tuts**.

> 📘 ეს რეპო წიგნების მკითხველებისთვისაა. ყველა skill, primitive, agent და template, რომელიც წიგნებში ნახსენებია — აქვე copy-paste-ისთვის.

---

## 📂 რა არის აქ

### `skills/` — 31 skill
რიუზაბილური Claude Code skill-ები 6 დომენში:

| დომენი | რა ფარავს |
|---|---|
| [`developer-tools/`](skills/developer-tools) | code quality, scaffolding (lint, type-check, new component, new page) |
| [`frontend/`](skills/frontend) | React, Tailwind, Electron, audio libraries |
| [`backend-dotnet/`](skills/backend-dotnet) | .NET ინტეგრაციები (Stripe, SignalR, Firebase, Cloudflare R2) |
| [`client-integrations/`](skills/client-integrations) | Browser SDK-ები (FB Pixel, GA4, Firebase Auth, FFmpeg-WASM) |
| [`cms/`](skills/cms) | Sanity CMS workflow |
| [`writing/`](skills/writing) | Prose, AI-ism detection, grill-me interviewing |
| [`analysis/`](skills/analysis) | Business analyst, deep-investigation, mermaid diagrams, invoice organizer |

ყველა skill-ს აქვს `SKILL.md` ფაილი frontmatter-ით (`name`, `description`, `triggers`) — ჩასვი `.claude/skills/` ფოლდერში და მზადაა.

### `templates/` — 5 starter project ე
სრული `.claude/` ფოლდერების ნიმუშები ახალი პროექტებისთვის:

| ნიმუში | აუდიტორია |
|---|---|
| [`frontend-ge/`](templates/frontend-ge) | Frontend პროექტი — ქართული instructions |
| [`frontend-en/`](templates/frontend-en) | Frontend პროექტი — English instructions |
| [`backend-ge/`](templates/backend-ge) | Backend პროექტი — ქართული instructions |
| [`backend-en/`](templates/backend-en) | Backend პროექტი — English instructions |
| [`global/`](templates/global) | Global Claude Code settings (`~/.claude/`) |

თითოეული ნიმუში მოიცავს: `CLAUDE.md` + `primitives/` + `prompts/` + `compositions/` + `agents/` + `skills/` მზადყოფნად.

დამატებით:
- [`templates/CONCEPTS.md`](templates/CONCEPTS.md) — Primitives, Skills, Prompts, Agents — რა განსხვავებაა?
- [`templates/PROJECT_WORKFLOW.md`](templates/PROJECT_WORKFLOW.md) — სრული ფლოუ: idea → plan → build → ship
- [`templates/plan-template/`](templates/plan-template) — ფაზური დაგეგმვის template-ი

---

## 🚀 როგორ გამოვიყენო

### ახალი პროექტისთვის (template)
```bash
# დააკოპირე შესაფერისი template-ი
cp -r templates/frontend-ge/.claude my-project/.claude
cp templates/frontend-ge/CLAUDE.md my-project/CLAUDE.md

# გახსენი Claude Code
cd my-project
claude
```

### არსებულ პროექტში skill-ის დამატება
```bash
# მაგალითად: lint + typecheck skill
cp -r skills/developer-tools/check .claude/skills/check
```

---

## 📚 წიგნები

ეს რეპო companion-ია. პრაქტიკული გადაწყვეტილებების მიღმა აზრის გასაგებად — წიგნებში წაიკითხე:

- **„Claude Code — სრული სახელმძღვანელო"** (110 გვერდი, ქართული) — დეველოპერებისა და ანალიტიკოსებისთვის
- **„AI პრაქტიკული გზამკვლევი"** (169 გვერდი, ქართული) — ბიზნესის მფლობელებისთვის, მარკეტერებისთვის, ფრილანსერებისთვის

Facebook-ზე ხელმისაწვდომია (29 ₾ თითო ან 49 ₾ ორი ერთად).

---

## 🤝 Contribution

ეს არის curated კოლექცია — ყოველ skill-სა და template-ს Production-ში გავცადე.

დაბრუნებითი კავშირისთვის: GitHub Issues ამ რეპოზე.

---

## ⚖️ ლიცენზია

MIT — გამოიყენე თავისუფლად, კომერციულ პროექტებში ჩათვლით. ერთადერთი თხოვნა: თუ რამე გააუმჯობესე — გააქციე PR.

---

**English short version:** Companion repo by **Learning Tuts** for two Georgian-language books on Claude Code and general AI productivity. Contains 31 reusable skills + 5 starter project templates with `.claude/` folders pre-configured. MIT licensed.
