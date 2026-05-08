---
name: electron-vite
description: electron-vite build tool — project structure, HMR, IPC architecture, three-process setup. Use when working on Electron main/preload/renderer processes or build config.
---

# electron-vite

Fast builds, HMR, and three-process Electron architecture.

## Architecture

```
+-----------------------------------------------------------+
|                    Electron App                            |
|  +------------------+   contextBridge   +----------------+|
|  |   Main Process   |<--------------->|    Renderer     ||
|  |   (Node.js)      |   IPC channels    |   (React+Vite) ||
|  +------------------+                   +----------------+|
|           |              Preload                 |        |
|           +--------> contextBridge <-------------+        |
|                      window.api                           |
+-----------------------------------------------------------+
```

## Project Structure

```
src/
├── main/           # Main process (Node.js)
├── preload/        # contextBridge (window.api types)
└── renderer/       # React + Vite (UI)
```

## Commands

| Command | Description |
|---------|-------------|
| `electron-vite dev` | Dev mode with HMR |
| `electron-vite build` | Production build |

## IPC Pattern

```
Renderer                    Preload                     Main
window.api.doSomething() -> contextBridge -> ipcMain.handle()
         <-- Promise<result> <-- ipcRenderer.invoke() <--
```

## Key Concepts

- **externalizeDepsPlugin:** Node.js deps stay external in main/preload bundles
- **HMR:** Renderer gets hot reload; main process restarts on change
- **Security:** `contextIsolation: true`, `nodeIntegration: false`

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Module not found in main | Not externalized | Add to `externalizeDepsPlugin()` |
| `__dirname` undefined | ESM context | Use `import.meta.url` |
| HMR not working | Wrong process | HMR works in renderer only |
| Native module crash | Wrong Electron version | Run `npm run postinstall` |
