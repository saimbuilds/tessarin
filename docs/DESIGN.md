# DESIGN.md: Tessarin Studio

This file is the source of truth for how tessarin.studio looks, moves and sounds. Any page, component or prototype follows it. If something isn't covered here, add it here first and then build it.

---

## 1. Concept: "Tessarin: The Film"

The site isn't a brochure. It plays like a **short film you scroll through**: an opening assembly, a title sequence, scenes, and end credits. The film language does real work:

| Film device | What it does on the site |
|---|---|
| Orb intro (preloader) | While the page loads, the logo's shards tessellate an orb around an ember core, laid from the bottom up. Each one lands hot and cools, so a molten edge rises with the build; a big odometer counter and a real piece count ("2,431 / 5,200 pieces") track it. On Enter the orb pulls in for a beat and bursts, and its pieces build the wordmark. The Enter click is the gesture browsers need before sound can play |
| Letterbox bars | Frame every screen at a 2.39:1 feel. The nav lives inside the bars |
| Scene numbers + timecode | Show where you are (SC.03 / WEB) and that the "film" is running |
| Closed captions | One line of copy per scene, written like subtitles: `[low strings swell] We build…` |
| Film-strip work reel | Projects shown as frames on a reel you scrub sideways |
| The finale (after Interstellar) | The DNA is pulled into a black hole that bends the copy and the stars around it. Then the camera dives into the glowing disk, the light swallows the frame, and the only thing left inside the glow is **Book a call**: the one point everything was bending toward |

**The hero object is the logo's own accent shard.** The slanted red-orange tile on the "r" is the atom of the brand. Thousands of these shards build the wordmark, fly apart into a tunnel the camera dives through, and re-form into each service. We never use generic particles, stock 3D or icons.

**Many pieces in, one point out.** The film opens with the shards assembling one orb and ends at one point (the Book a call button inside the light). Everything in between is built from those shards and, at the end, falls back in.

**Positioning in one line:** young, fast, unreasonably technical. We prove it by how the site itself is built, not by claiming it.

---

## 2. Anti-slop rules (non-negotiable)

1. No centered hero with a gradient blob and "We build digital experiences". No glassmorphism cards (the cursor ring is the only glass on the site). No icon grids. No emoji.
2. No purple or blue gradients and no neon green. The palette is black, bone-white and one accent. Nothing else.
3. Every animation has to *mean* something (assembly = building, tunnel = going deeper, credits = the ending). Nothing floats around just for decoration.
4. Type is huge and confident. The smallest display size is still bigger than you think.
5. Copy is clear, specific and confident, written to the client. No em dashes, no location line, and never "innovative solutions", "cutting-edge", "seamless" or "leverage". The full voice rules and every line on the site are in [`COPY.md`](COPY.md).
6. Sound is part of the design, not something added at the end. Every interaction has a voice.
7. The "Book a call" button is visible at every moment. Art never hides the conversion path.

---

## 3. Colour

| Token | Hex | Use |
|---|---|---|
| `--void` | `#000000` | Ground. Matches the logo's black exactly |
| `--bone` | `#EDEAE4` | Primary text, white shards. A warm off-white, never pure #FFF |
| `--ember` | `#E74A2A` | The accent, sampled from the logo. CTAs, the active scene, red shards, the REC dot. Under 5% of any screen |
| `--smoke` | `#7D7974` | Secondary text and metadata |
| `--hairline` | `rgba(237,234,228,.14)` | Rules and borders |
| `--ember-glow` | `rgba(231,74,42,.35)` | Bloom and focus rings only |

The ember always sits on void. Never put ember text on bone.

---

## 4. Typography

| Role | Face | Settings | Why |
|---|---|---|---|
| Display | **Unbounded** (variable 200–900) | 900 for titles, 200 for giant numerals, tracking −0.04em, line-height 0.86 | Wide, geometric, with cut terminals like the logo. It reads as a film title at huge sizes |
| Accent | **Bodoni Moda Italic** (400/600) | Used for 1–2 words per headline only | High-contrast editorial serif. The tension between the brutal wide sans and the fine italic is the type signature |
| Utility | **Martian Mono** (variable width + weight) | 400, uppercase, tracking +0.08em, 10–12px | Loading readout, timecode, captions, tags. Gives the "camera HUD" voice |

**Scale (clamp, fluid):** `--t-mega: clamp(4rem, 15vw, 15rem)` · `--t-xl: clamp(2.6rem, 7vw, 6.5rem)` · `--t-l: clamp(1.8rem, 3.6vw, 3.2rem)` · `--t-m: 1.15rem` · `--t-s: .95rem` · `--t-xs: .7rem` (mono)

**Rule:** one headline = Unbounded caps + one Bodoni italic word. For example: "FUTURE, *assembled.*"

Fonts are self-hosted (inlined as WOFF2 in prototypes, `next/font/local` in production).

---

## 5. Layout

- **Full-bleed scenes.** Each scene is at least one viewport tall. Scenes with scroll-driven animation are 200–300vh with a sticky stage inside.
- **Composition:** the 3D object sits centre stage. A giant outlined scene word (e.g. `WEB`) runs behind it with `mix-blend-mode: difference`. Copy sits on a small "scene card" bottom-left, and metadata (tags, scene number) sits bottom-right. **No left-text / right-image templates.**
- **Letterbox:** top and bottom bars are `max(56px, 7vh)` tall and pure void. Top bar: wordmark · scene label · sound · CTA. Bottom bar: timecode · scene ticks · REC.
- **Gutters:** `clamp(16px, 4vw, 56px)`. The grid is 12 columns on desktop and 4 on phones, but compositions break it on purpose for the giant type.

---

## 6. Motion

| Moment | Spec |
|---|---|
| Smooth scroll | Lenis, `lerp 0.085` |
| Text reveal | Characters rise from a mask: `yPercent 110 → 0`, stagger 0.018s, `expo.out`, 1.1s |
| Word scrub (manifesto) | Each word goes from opacity 0.12 to 1, scrubbed to scroll |
| Shards → formation | Spring physics (stiffness 26, damping 6.5). Shards spin while moving and settle flat |
| Camera | A dolly through the shard tunnel in the manifesto (z 14 → −16, scrubbed) |
| Scroll velocity | Drives chromatic aberration and shard stretch, so fast scrolling *feels* fast |
| Cursor | A hollow ring of Liquid Glass (after Apple's 2025 material), 42px. The band is a lens: in Chromium browsers an SVG displacement map bends whatever is under it, with a slight red/green/blue split at the edges; Safari and Firefox get a frosted blur instead. Ember outline on both edges, a white specular highlight on the top-left rim, soft ember glow. It trails the pointer, stretches up to 14% along fast moves, swells 1.6x over anything clickable and squeezes on press. Hidden on touch screens. Nothing "space" about it |
| Magnetic CTA | Pulls up to 18px toward the cursor |
| Reduced motion | No tunnel, no CA, instant formations, no char reveals. Content still fully readable |

**Post-processing stack:** render → black hole lens (finale only) → UnrealBloom (threshold 0.6, strength 0.55) → film pass (radial chromatic aberration, animated grain 0.018, vignette) → output.

**Scroll length:** the whole film is about 13.5 screens on desktop (it was 21 in v4). The finale is 2.5 screens and ends exactly at the bottom of the page.

---

## 7. Sound and score

All of it is generated live with the Web Audio API, so there are no audio files and loading stays instant. A licensed track can replace it later.

- **Key and tempo:** D minor, 96 BPM. Chords change every 2 bars.
- **Progressions:** Opening `Dm – B♭ – F – C` · Services `Dm – Gm – B♭ – A` (tension) · Credits `B♭ – C – Dm – F` (resolve)
- **Layers:**
  - **Strings pad:** detuned saws with slow attack, plus a 4.5s convolution reverb
  - **Sub bass:** roots, swelling
  - **Ostinato:** 16th-note low strings, the Zimmer-style pulse
  - **Arp:** plucked chord tones through a ping-pong delay, with a different pattern for each service
  - **Clock ticks:** tension in the manifesto and process scenes
- **Hits:** a sharp "clack" on enter, then a **braam** (detuned brass-like saws with a filter sweep), taiko-style impacts between scenes, and a final braam in the credits.
- **Shard voice:** shards the cursor disturbs ring as glass notes **in the current chord**, so playing with the 3D is literally playing the score.
- **Mix per scene:** each scene sets target levels for the layers, crossfading over about 1.2s.
- **Rules:** the 80/20 rule (sound amplifies, never overwhelms). "Enter muted" is always offered. Mute state is remembered.

---

## 8. Components

- **Intro (preloader):** pure black over the live 3D stage. In the middle the orb builds: white shards stream in from all around and take slots on a sphere along a Fibonacci spiral (equal area per slot, so pieces placed = share loaded), landing hot and cooling to graphite, while ember shards churn in a core whose light glows through every seam. The orb turns slowly, leans toward the pointer, and shards under the pointer lift. Corners: the logo top-left (exactly where the top bar's logo will be), "Web · AI · Emerging tech" top-right. Bottom-left: a huge Unbounded counter 000–100 that rolls like a mechanical odometer, with a small ember Bodoni %. Bottom-right in mono: "Assembling" and the piece count, over an ember hairline progress bar. At 100% a seal of heat runs down the finished orb and the ember **Enter** pill (with a live sound-bars icon) and a quiet "Enter without sound" link appear under it. On Enter the orb pulls in, bursts (pressure wave, braam), its shards turn from graphite to bone as they fly, and they build the wordmark in the hero while the letterbox bars slide in.
- **Letterbox nav:** see §5. The scene label updates with a scramble effect.
- **Caption line:** mono, centred above the bottom bar, `[sound cue]` in smoke, then copy in bone. Types itself out.
- **Scene card:** mono eyebrow `SC.03 · WEB` → Unbounded headline → body (max 46ch) → tags.
- **Reel frame:** 4:5 poster with sprocket-hole edges, frame number, title in Bodoni italic, discipline in mono, and a "SAMPLE" flag until real work is in.
- **Black hole finale:** a ray-traced Schwarzschild black hole in the style of Interstellar's Gargantua. It has a black shadow, a thin ember-to-white accretion disk with its far side lensed over and under the shadow, a faint star field dragged around it, and an Einstein ring. Scroll timeline: the hole forms around the DNA → the DNA comes apart into the whole journey around the hole: the wordmark, WEB, AI and the headset, with the DNA in the middle → gravity takes them one by one in the order the visitor saw them, each spiralling through the disk and the horizon → the headline "Everything bends / toward *one point.*" appears, then bends, smears into a spiral and falls in → DNA shards orbit and cross the horizon → the camera dives toward the bright side of the disk (a riser builds) → the light swallows the frame in a short white-hot flash (braam and impact) → it settles into a slowly swirling ember glow, the inside of the disk → a black **Book a call** pill appears at the white-hot centre. Nothing else is on screen.
- **Buttons:** pill, mono uppercase. Primary is ember fill with void text; secondary has a hairline border.

---

## 9. References to study (Awwwards level)

- **kodeimmersive.com:** gate + sound, physics shards, restraint (our starting point, see the teardown)
- **lusion.co:** cinematic WebGL with physics and seamless transitions between scenes
- **igloo.inc:** a scroll-driven 3D journey where the camera *travels*
- **activetheory.net:** WebGL as the whole interface
- **Film title sequences** (Saul Bass, *Se7en*, *Blade Runner 2049*): this is where the type and caption ideas come from

---

## 10. Production stack

Next.js (App Router, TS) · React Three Fiber + drei · three postprocessing · Rapier · GSAP + ScrollTrigger · Lenis · Web Audio (custom score engine) · Cal.com embed · Vercel.

Performance budget: first paint of the intro in under 1s, 60fps desktop / 30fps mid-range Android, adaptive particle count and pixel ratio, bloom at half resolution on phones.
