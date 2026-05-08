---
name: sanity-cms
description: Sanity CMS patterns — schemas, GROQ queries, image pipeline, bilingual fields. Use when working with Sanity schemas, content queries, or image URL building.
---

# Sanity CMS

Schema patterns, GROQ queries, image pipeline.

## Bilingual Field Pattern

```typescript
defineField({
  name: 'title',
  type: 'object',
  fields: [
    { name: 'en', type: 'string', title: 'English' },
    { name: 'ka', type: 'string', title: 'Georgian' },
  ],
});
```

## GROQ Queries

```groq
// All documents with ordering
*[_type == "artwork"] | order(order asc) {
  _id, title, slug, year,
  "imageUrl": image.asset->url,
  "series": series->{ title, slug }
}

// By slug
*[_type == "artwork" && slug.current == $slug][0]

// By reference
*[_type == "artwork" && series->slug.current == $seriesSlug]

// All unique values
array::unique(*[_type == "product"].category)
```

## Image URL Builder

```typescript
import imageUrlBuilder from '@sanity/image-url';

const builder = imageUrlBuilder(client);
export function urlFor(source) { return builder.image(source); }

// Usage
urlFor(image).width(400).height(400).fit('crop').auto('format').url()  // Thumbnail
urlFor(image).width(1500).auto('format').url()                         // Detail (max protection)
urlFor(image).width(1200).height(630).fit('crop').auto('format').url() // OG Image
```

## Image Pipeline

```
Upload (full-res) -> Sanity CDN -> Auto-resize + WebP
                                    ├── thumbnail: 400px
                                    ├── grid: 800px
                                    ├── detail: 1500px max
                                    └── og: 1200x630
```

## Rules

- Bilingual fields: always `{ en: string, ka: string }` object
- Slug source: `'title.en'`
- Image hotspot: always `options: { hotspot: true }`
- Only GROQ queries, no REST API
- Max image width 1500px, never serve originals
