---
name: ffmpeg-wasm
description: FFmpeg.wasm client-side audio/video processing — format conversion, trimming. Use when working on browser-based media processing or export.
---

# FFmpeg.wasm

Client-side audio/video processing in the browser.

## Architecture

```
AudioBlob (WAV) --> FFmpeg WASM (Browser) --> MP3 Blob (Download)
                         |
                    Virtual FS (in-memory)
```

## Setup

```typescript
import { FFmpeg } from "@ffmpeg/ffmpeg";
import { fetchFile, toBlobURL } from "@ffmpeg/util";

const ffmpeg = new FFmpeg();
const baseURL = "https://unpkg.com/@ffmpeg/core@0.12.6/dist/umd";

await ffmpeg.load({
  coreURL: await toBlobURL(`${baseURL}/ffmpeg-core.js`, "text/javascript"),
  wasmURL: await toBlobURL(`${baseURL}/ffmpeg-core.wasm`, "application/wasm"),
});
```

## Common Commands

```typescript
// WAV to MP3
await ffmpeg.exec(["-i", "input.wav", "-codec:a", "libmp3lame", "-b:a", "320k", "output.mp3"]);

// Trim audio
await ffmpeg.exec(["-i", "input.wav", "-ss", "10", "-t", "20", "-c", "copy", "output.wav"]);

// Normalize volume
await ffmpeg.exec(["-i", "input.wav", "-filter:a", "loudnorm", "output.wav"]);
```

## COOP/COEP Headers (required for SharedArrayBuffer)

```typescript
// vite.config.ts
server: {
  headers: {
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Embedder-Policy": "require-corp",
  },
}
```

## Performance Tips

1. Load FFmpeg once (~30MB WASM), lazy-load when needed
2. Show progress via callback
3. Clean up virtual FS files after use
4. Cache core files with service worker

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| SharedArrayBuffer error | Missing COOP/COEP headers | Set headers |
| Out of memory | Large files | Process in chunks |
