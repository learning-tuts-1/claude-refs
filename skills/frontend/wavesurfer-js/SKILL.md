---
name: wavesurfer-js
description: WaveSurfer.js v7 waveform visualization with regions plugin for trim functionality. Use when working on waveform display, audio visualization, or trim/region features.
---

# WaveSurfer.js v7

Waveform visualization with regions plugin for trim functionality.

## Basic Setup

```typescript
import WaveSurfer from "wavesurfer.js";

const ws = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#a3a3a3",
  progressColor: "#262626",
  height: 80,
  barWidth: 2,
  barGap: 1,
  barRadius: 2,
  normalize: true,
  backend: "WebAudio",
});

ws.load("/audio/track.mp3");
```

## Regions Plugin (Trim)

```typescript
import RegionsPlugin from "wavesurfer.js/dist/plugins/regions.js";

const regions = RegionsPlugin.create();
const ws = WaveSurfer.create({ container: "#waveform", plugins: [regions] });

ws.on("ready", () => {
  regions.addRegion({
    id: "trim",
    start: 0,
    end: ws.getDuration(),
    color: "rgba(38, 38, 38, 0.2)",
    drag: true,
    resize: true,
  });
});

regions.on("region-updated", (region) => {
  onTrimChange({ start: region.start, end: region.end });
});
```

## React Integration

```typescript
function Waveform({ url }: { url: string }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const wsRef = useRef<WaveSurfer | null>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const ws = WaveSurfer.create({ container: containerRef.current, height: 80 });
    ws.load(url);
    wsRef.current = ws;
    return () => { ws.destroy(); };
  }, [url]);

  return <div ref={containerRef} />;
}
```

## Performance Tips

1. Use `barWidth` — bars render faster than lines
2. Set `normalize: true` — consistent visual amplitude
3. Destroy on unmount — prevent memory leaks
4. Debounce region updates

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| No waveform | CORS | Configure audio server CORS |
| Memory leak | Not destroyed | Call `destroy()` on unmount |
| Region not visible | Wrong z-index | Check CSS stacking |
