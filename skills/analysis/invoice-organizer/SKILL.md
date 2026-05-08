---
name: invoice-organizer
description: Organizes invoices and receipts for tax preparation — reads files, extracts key information, renames consistently, and sorts into folders. Use when preparing taxes or organizing financial documents.
---

# Invoice Organizer

Transforms chaotic invoice folders into clean, tax-ready filing systems.

## Process

1. **Scan folder** — identify all invoice files (PDF, JPG, PNG)
2. **Extract info** — vendor, date, invoice number, amount, description
3. **Rename consistently** — `YYYY-MM-DD Vendor - Invoice - Description.ext`
4. **Organize** — sort into logical folders (by vendor, category, date, or tax category)
5. **Generate CSV** — spreadsheet with all details for accountant
6. **Flag unclear files** — for manual review

## Organization Patterns

### By Year and Category (Tax-Friendly)
```
Invoices/
├── 2024/
│   ├── Software/
│   ├── Hardware/
│   └── Travel/
```

### By Vendor
```
Invoices/
├── Adobe/
├── Amazon/
└── Google/
```

### By Tax Category
```
Invoices/
├── Deductible/
├── Partially-Deductible/
└── Personal/
```

## Special Cases

- **Missing info** — use file modification date as fallback, flag for review
- **Duplicates** — compare hashes, keep highest quality version
- **Multi-page** — merge PDFs if needed

## Best Practices

1. Always copy (don't move) to preserve originals
2. Show plan before executing
3. Keep receipts 7 years (standard audit period)
4. Monthly routine beats annual chaos
