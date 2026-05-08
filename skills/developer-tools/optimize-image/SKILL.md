---
name: optimize-image
description: Downloads an image from URL, resizes to exact dimensions, and converts to optimized WEBP format. Use when optimizing images for web.
argument-hint: "[url] [width] [height] [output-filename]"
---

# Image Optimization

Downloads, resizes, and converts images to optimized WEBP format.

## Usage

```
/optimize-image <url> <width> <height> [output-filename]
```

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `url` | Yes | URL of the image to download |
| `width` | Yes | Target width in pixels |
| `height` | Yes | Target height in pixels |
| `output-filename` | No | Output filename (defaults to `output.webp`) |

## Instructions

Run the optimization script:

```bash
python .claude/skills/optimize-image/scripts/optimize.py $0 $1 $2 $3
```

If dependencies are missing:

```bash
pip install Pillow requests
```

## Features

- Downloads images from any public URL
- Resizes to exact dimensions using LANCZOS resampling
- Converts to WEBP format with 85% quality
- Handles transparent images (PNG) by compositing on white background
- Reports original size, final dimensions, and file size
