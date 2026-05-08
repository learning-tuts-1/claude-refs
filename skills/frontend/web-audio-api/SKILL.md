---
name: web-audio-api
description: Web Audio API patterns for audio playback, stem mixing, volume control, and waveform generation. Use when working on audio engines, playback, or mixing features.
---

# Web Audio API

Audio playback, stem mixing, real-time effects.

## Architecture

```
Sources (Drums, Bass, Melody)
         |
    Gain Nodes (Volume per track, Solo/Mute)
         |
    Master Gain
         |
    AudioContext.destination
```

## Key Concepts

- **AudioContext** — initialize on user interaction (autoplay policy)
- **AudioBufferSourceNode** — one-shot: create new source for each play()
- **GainNode** — per-track volume + master volume
- **Solo/Mute** — when any track is solo, mute all non-solo tracks
- **Time tracking** — use `requestAnimationFrame`, not `setInterval`
- **Memory** — disconnect and nullify sources on stop

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| No sound | Context suspended | Call `resume()` on user interaction |
| Playback glitches | Buffer underrun | Pre-load all audio before playing |
| Memory leak | Sources not cleaned | Disconnect and nullify on stop |
| Timing drift | Using setInterval | Use requestAnimationFrame |
| CORS error | Audio from different origin | Configure CORS on server |

## Performance Tips

1. Pre-load all stems before allowing playback
2. Use Web Workers for waveform generation
3. Cache decoded buffers
4. Limit concurrent tracks to 8-12 for smooth playback
