# Tessarin Studio: website prototype (v4)

The tessarin.studio site as a short film you scroll through: an intro where one shard fills as the page loads and then bursts into the wordmark, letterbox scenes, logo-shard 3D with bloom, a generative cinematic score, a simple shard cursor, and an Interstellar-style finale: everything from the journey (the wordmark, WEB, AI, the headset, the DNA) is pulled into a black hole that bends the copy, the camera dives into the glowing disk, and Book a call appears inside the light. The rules behind every design decision are in [`docs/DESIGN.md`](docs/DESIGN.md).

## Run it in VS Code

1. Open this folder in VS Code.
2. Install the **Live Server** extension (VS Code will suggest it, see `.vscode/extensions.json`).
3. Right-click `index.html` → **Open with Live Server**.
4. Click **Enter** (or **Enter without sound**). The sound button in the top bar turns the score on and off at any time.

Any other static server works too:

```bash
npx serve .            # or
python -m http.server 8000
```

> Don't open `index.html` by double-clicking. Browsers block fonts and the logo canvas on `file://`. If you need a single file that opens anywhere, use the standalone build below.

An internet connection is needed: three.js and Lenis load from the jsDelivr CDN.

## Standalone single-file build

```bash
python build.py
```

This writes `dist/tessarin-standalone.html`, with the fonts and logo inlined, so it opens with a double-click and can be sent as one file. A fresh copy is already included.

## What's where

| Path | What it is |
|---|---|
| `index.html` | The whole site: markup, CSS, and one `<script type="module">` |
| `brand/` | Logo (original JPG + transparent PNG) and self-hosted fonts (`fonts/fonts.css`) |
| `docs/DESIGN.md` | Design system: concept, colour, type, motion, sound, components |
| `docs/kode-teardown-and-site-plan.md` | Kode Immersive teardown and the original plan |
| `archive/v1-prototype.html` | The first prototype, kept for reference |
| `dist/` | Standalone build output |

### Inside `index.html` (search for these banners)

- **`SCORE`**: the generative soundtrack (Web Audio API). Key: D minor, 96 BPM. `PROG` holds the chord progressions, `MIX` the layer levels per scene, `ARP` the arpeggio patterns. `braam()`, `impact()`, `riser()` and `clack()` are the hits.
- **`GARGANTUA`**: the black hole. A post-processing pass that ray-traces bent light past a Schwarzschild black hole, draws the accretion disk, and bends the scene, the star field and the copy behind it.
- **Hole choreography**: the scroll timeline for the finale (`holeLens()` for the lens, the dive and the glow, `holeAim()` for the shards). The comment above it lists what happens at each point of the scroll.
- **`GARGANTUA`**: the black hole shader. `glow()` in it is the inside of the disk where Book a call appears.
- **`MEM` / `memAim()`**: where each piece of the journey sits around the black hole (wide and narrow screens) before it falls in. `GEAT` sets when each piece starts to fall.
- **`STAGE`**: three.js scene, bloom + film post-processing (chromatic aberration, grain, vignette), and the shard meshes.
- **Formations** (`F.logo`, `F.tunnel`, `F.helix`, the WEB/AI words, the VR headset, …): the shapes the shards build. `PLACE` sets their position, scale and motion.
- **Scroll model**: `measure()` and `readScroll()` map scroll position to "hold" and "transition" ranges for each `.scene`.
- **Scenes**: each `<section class="scene">` declares `data-form` (the shard shape), `data-mix` (the music mix) and `data-name`.
- **Bendable copy**: the black-hole headline is real HTML (`#holeText`) that is painted into the WebGL frame by `paintHoleText()`, so gravity can bend it. Edit the HTML and the painting follows.

## Things to replace before launch

- `https://cal.com/tessarin` → your real Cal.com link (3 places).
- The three sample projects in the reel (Vexilot, WebAudit, DriveFetch) → real case studies.

## Libraries and licences

three.js 0.170 (MIT), Lenis 1.1.13 (MIT), Unbounded / Bodoni Moda / Martian Mono (SIL OFL 1.1). The score is synthesised in code, so there are no audio files.

## Test hook

Adding `?test` to the URL speeds up the particle physics and exposes `window.__tessMeter()` (audio peak/RMS). It's only used for automated screenshots, and leaving it in is harmless.
