#!/usr/bin/env python3
"""
Image optimization script: downloads, resizes, and converts images to WEBP format.
"""

import sys
import os
from io import BytesIO

try:
    import requests
    from PIL import Image
except ImportError as e:
    print(f"Error: Missing required package. Please install with:")
    print("  pip install Pillow requests")
    sys.exit(1)


def download_image(url: str) -> Image.Image:
    """Download an image from a URL and return as PIL Image."""
    try:
        response = requests.get(url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to download image: {e}")
    except Exception as e:
        raise Exception(f"Failed to open image: {e}")


def resize_image(image: Image.Image, width: int, height: int) -> Image.Image:
    """Resize image to exact dimensions."""
    if image.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', image.size, (255, 255, 255))
        if image.mode == 'P':
            image = image.convert('RGBA')
        background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
        image = background
    elif image.mode != 'RGB':
        image = image.convert('RGB')

    return image.resize((width, height), Image.Resampling.LANCZOS)


def save_as_webp(image: Image.Image, output_path: str, quality: int = 85) -> int:
    """Save image as WEBP format and return file size in bytes."""
    image.save(output_path, 'WEBP', quality=quality, method=6)
    return os.path.getsize(output_path)


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"


def main():
    if len(sys.argv) < 4:
        print("Usage: python optimize.py <url> <width> <height> [output_filename]")
        print("Example: python optimize.py https://example.com/image.jpg 800 600 output.webp")
        sys.exit(1)

    url = sys.argv[1]

    try:
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    except ValueError:
        print("Error: Width and height must be integers")
        sys.exit(1)

    if width <= 0 or height <= 0:
        print("Error: Width and height must be positive integers")
        sys.exit(1)

    output_filename = sys.argv[4] if len(sys.argv) > 4 else "output.webp"

    if not output_filename.lower().endswith('.webp'):
        output_filename += '.webp'

    print(f"Downloading image from: {url}")
    image = download_image(url)
    original_size = image.size
    print(f"Original size: {original_size[0]}x{original_size[1]}")

    print(f"Resizing to: {width}x{height}")
    resized = resize_image(image, width, height)

    print(f"Saving as WEBP: {output_filename}")
    file_size = save_as_webp(resized, output_filename)

    print(f"\nSuccess! Image saved to: {output_filename}")
    print(f"Final dimensions: {width}x{height}")
    print(f"File size: {format_size(file_size)}")


if __name__ == "__main__":
    main()
