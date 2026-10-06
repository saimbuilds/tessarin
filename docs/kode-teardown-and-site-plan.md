# Tessarin.studio: Kode Immersive teardown + site plan

_Prepared 2026-10-05. Status: plan, waiting on answers to the questions at the bottom._

> **About the research.** This environment's network policy blocks direct browser access to kodeimmersive.com, so I couldn't take live screenshots or capture network traffic. The teardown below comes from the site's rendered content plus the builders' own write-up ([Awwwards case study](https://www.awwwards.com/case-study-kode-immersive.html), [Awwwards SOTD page](https://www.awwwards.com/sites/kode-immersive)). That write-up is more reliable than reverse-engineering minified JS would be, because it's the team explaining how they did it. If you want live captures later, add `kodeimmersive.com` to the allowed domains in the project's cloud environment settings.

---

## Part 1: How Kode Immersive is built

### Who made it
- **Malvah** (studio in Cape Town) did design and direction. **Francesco Michelini** did the WebGL. **Martin Leitner / Sounds Good** did the sound.
- Awwwards **Site of the Day, 13 May 2025**: 7.62 overall, 7.72 dev award. Design scored 7.84 and usability 7.25, so even the judges noticed that the "weird" navigation costs some clarity.

### The flow, top to bottom
1. **Preloader → "Enter" gate.** This does two jobs. It hides asset loading, and it gets a user click so the browser will allow audio to play. Without a gesture, autoplay rules keep the site silent. The gate is what makes the sound design possible at all.
2. **Chevron hero.** A big 3D chevron (their brand mark) is the first thing you see. "We see no limit to the potential of emerging technology."
3. **Narrative block with shifting text.** The text breaks apart and re-forms around the cursor, as a metaphor for "deconstruction and reformation."
4. **"Scratch around" easter egg.** You draw on the screen to reveal a hidden layer underneath. They added an **auto-trigger** so it fires by itself if you don't discover it, which means nobody misses the best moment.
5. **Services carousel.** Ideate / Create / Deliver, with prev/next. The sound shifts to feel like "entering a new realm" here.
6. **Mission line → leadership (2 people) → contact.**
7. **Menu that grows into the footer.** The nav starts small at the bottom and turns into the footer as you scroll.
8. A **sound on/off toggle** is always visible.

### The tech
| Layer | What they used | Why it matters |
|---|---|---|
| Rendering | **Three.js** (WebGL) | Industry standard |
| Threading | **OffscreenCanvas + Web Worker** | Rendering runs off the main thread, so scrolling and the UI never stutter |
| Physics | **Rapier** (WASM) | Gives objects real weight and collisions when you push them around |
| Draw calls | **BatchedMesh**: "40 or 50 draw calls down to just one" | The biggest single performance win, and why it runs on mid-range phones |
| 3D authoring | **Cinema 4D** for concepts, modeling and metacaps | |
| Visual glue | A subtle **pixel distortion + soft noise** post-process over everything | This is why 3D, flat orange, and type feel like one world instead of a 3D model pasted onto a webpage |
| Type | **Brut** by Off-Type (mono-ish) | |
| Colour | **#FF4C00 + #000000**, nothing else | Strict restraint is a big part of why it reads as premium |

### The sound philosophy (the part you liked most)
- An **80/20 rule**: just enough sound to amplify emotion, never wall-to-wall music.
- Sound comes in three layers: a **base ambience bed**, **transition swells** between sections, and **micro-sounds on hover and click** (they call it "cursor haptics").
- Everything is tied to an interaction or a scroll moment. Nothing is just background.

### Their process (worth copying)
Discover (strategy, style tiles) → Create (prototype design, 3D and code in parallel) → Craft (shaders, lighting, micro-interactions) → Deliver (cross-device QA, stress tests).

### What to take and what to leave
- **Take:** the gate plus sound, one strong 3D brand object, physics you can touch, a hidden interaction with an auto-trigger, a strict two-colour palette, a noise layer that unifies everything, and off-main-thread rendering.
- **Leave:** the orange/chevron look (that's their identity), and the usability cost. Your site has to **convert**, so the path to "talk to us" must never be hidden behind the art.

---

## Part 2: The plan for tessarin.studio

### The core idea: build the site out of tesserae
"Tessarin" sounds like **tessera**, the small tiles a mosaic is made of. That gives you a concept almost nobody else can copy, because it comes from your name:

> **Small pieces → one picture.** The agency is a set of sharp young builders who snap together into whatever a client needs. That honestly *is* your hiring model.

The whole site is made of thousands of small 3D tiles, rendered as one BatchedMesh/InstancedMesh, in one draw call just like Kode.

### The flow
1. **Gate.** A black screen with a scattered field of tiles slowly drifting, and a counter loading to 100. Two choices: **"Enter with sound"** / "Enter quietly". When you click, the tiles **snap together into the Tessarin mark**, with a crisp ceramic *click-click-click* cascade. That's the first "wow", and it's also the moment sound is unlocked.
2. **Hero.** The mark made of tiles. Your cursor is a force field: tiles scatter with **Rapier** physics and settle back with satisfying micro-clicks. One line of copy, something like _"We build what's next. Piece by piece."_ (copy to be workshopped).
3. **Manifesto with shifting text.** Your "young, fast, technical" story told honestly. Being in 3rd semester becomes a strength ("hungry, fast, unafraid of new tech") instead of something to hide.
4. **Services as tile formations.** As you scroll, the tiles re-form into a glyph for each service: **Web** (a browser frame), **AI** (a neural lattice that pulses), **Emerging tech** (a shape that keeps morphing). Each one gets its own sound texture.
5. **The Lab (this solves "we have few projects").** Instead of a thin portfolio, show **live experiments the visitor can play with on the page**: a shader toy, a small AI demo, a physics toy. A client sees proof of skill *working right in front of them*, which persuades better than a screenshot of a past project. You can keep adding experiments every week.
6. **"Scope it with Tessarin AI" (the conversion engine).** An on-brand AI chat (built on the Claude API) where a visitor describes their idea. It asks 3–4 smart questions, then produces a **one-page project brief** with a rough scope, which gets sent to your inbox and to them. This shows off your AI skill *and* collects qualified leads. This is the "talk to us instantly" moment you asked for.
7. **Easter egg.** Click/drag to **paint with tiles**, or type your name and the tiles spell it. It auto-triggers once if the visitor hasn't found it.
8. **Contact / footer.** The tiles collapse into the footer (our version of Kode's menu-to-footer trick). WhatsApp, email, Calendly, and the AI scoper.

**A non-negotiable for conversion:** a small persistent **"Start a project"** button is visible at every moment, above the art.

### Sound design
- **Palette:** ceramic/glass tile clicks (the signature sound), a soft low ambient bed, airy swells on section changes, plus a "data" texture for the AI section.
- **Rules:** 80/20 like Kode, every sound tied to an action, a global mute that's remembered, and sound off by default if the visitor picks "Enter quietly".
- **Tech:** Web Audio API (via Howler.js or Tone.js). Tile clicks are **pitched and panned by position** so they sound spatial, and the click rate is throttled so a big scatter doesn't turn into noise.
- **Source:** licensed SFX packs plus custom layering, or a freelance sound designer for 1–2 days if budget allows. I can prototype with free/CC0 sounds first.

### Recommended stack
| Concern | Pick | Why |
|---|---|---|
| Framework | **Next.js (App Router) + TypeScript** | SEO for the agency pages, easy API routes for the AI scoper, and your future hires will know it |
| 3D | **Three.js via React Three Fiber + drei** | Fast iteration in React, with full Three.js underneath when needed |
| Performance | **InstancedMesh/BatchedMesh**, OffscreenCanvas worker for the hero if needed, adaptive DPR, `drei/PerformanceMonitor` | Same tricks as Kode |
| Physics | **Rapier** (`@react-three/rapier`) | Same engine as Kode |
| Scroll & motion | **GSAP + ScrollTrigger + Lenis** smooth scroll | The standard for choreographed scroll |
| Shaders / post | Custom GLSL plus a noise/grain/pixel-distortion pass (`postprocessing`) | Gives us the "one world" glue |
| Audio | **Howler.js** (or Tone.js for generative layers) | |
| 3D authoring | **Blender** (free) → glTF, compressed with **Draco/Meshopt + KTX2** | C4D costs money, and most of our geometry is procedural tiles anyway |
| AI scoper | **Claude API** route plus **Resend** for email | |
| Hosting | **Vercel** + tessarin.studio domain | Free tier is enough to start |
| Fallbacks | `prefers-reduced-motion` and low-power detection → a lighter 2D version | Many mobile visitors are on mid-range Android over 4G, so this matters a lot |

**Performance budget:** under 2.5 MB for first load before the gate, 60 fps on desktop, 30+ fps on a mid-range Android, and the gate shows within about 1 s.

### Build phases (copying Kode's process)
1. **Discover:** answer the questions below, then I produce a moodboard/style tiles, copy draft, and 2–3 colour directions.
2. **Prototype:** I build the tile hero alone (gate → assemble → cursor physics → sound), deploy it to a preview URL, and you play with it on your phone. This is the riskiest and most important piece, so we prove it first.
3. **Build:** scroll choreography, service formations, Lab, AI scoper, contact.
4. **Craft:** sound mix, micro-interactions, the noise layer, the easter egg.
5. **Deliver:** device QA (low-end Android, iPhone Safari, desktop), SEO/OG images, analytics, launch, then submit to Awwwards.

---

## Part 3: Questions before we start
See the thread reply for the short version. Full list:

1. **Repo:** is there a GitHub repo I should build in, or should I create one (name, e.g. `tessarin-site`)? Connect it in Project settings → repositories.
2. **Brand assets:** do you have a logo, colours or fonts already, or should I design the identity too?
3. **Tessera concept:** does the "built from tiles" idea feel right, or do you have another metaphor in mind?
4. **Colours:** any colour you want to own? (Kode owns orange. Options: electric lime on black, deep emerald + gold, or cobalt + white.)
5. **Projects to show:** list whatever you *have* (even half-built, university or hackathon projects) with links. I'll decide what goes in the Lab.
6. **AI scoper:** OK to use the Claude API for it? Who pays for the API key, and which email should leads go to?
7. **Contact channels:** WhatsApp number, email, Calendly? Which one do you want clients to use first?
8. **Target clients:** local businesses, international startups, or both? (Answered: any location.) This changes the copy tone, pricing signals and timezone messaging.
9. **Team section:** show founders' faces and names, or keep it collective ("Tessarin is a crew")?
10. **Sound:** any budget for a sound designer or paid SFX pack, or free/CC0 only for now?
11. **Domain/hosting:** do you own tessarin.studio already? Is Vercel fine?
12. **Deadline:** is there a launch date or an event you're aiming for?

Sources: [Awwwards case study](https://www.awwwards.com/case-study-kode-immersive.html), [Awwwards SOTD](https://www.awwwards.com/sites/kode-immersive), [kodeimmersive.com](https://kodeimmersive.com/).

---

## Update 2026-10-05: decisions from Testlion
- **Brand:** the logo is in `brand/tessarin-logo.jpg`. Colours are black (dominant), white #F4F3F1, and the accent #E74A2A sampled from the slanted shard on the "r".
- **Concept:** the logo's accent is itself a slanted tile, so every particle on the site is that shard. They assemble into the wordmark, then re-form per section into a mosaic wall, a browser, a neural net, a knot, a lattice cube, a helix and a contact ring.
- **AI scoper chat: dropped.** Conversion now runs through a Cal.com "Book a call" button (always visible) plus a copyable email. Next step: add a short project form (name, email, budget range, message) sent through Resend or Formspree.
- **Projects:** the three placeholders (Atlas, Mehfil, Orbit) are marked as samples.
- **Clients:** everywhere, so the copy is in English and doesn't name a location.
- **Prototype v1:** `prototype/index.html`, published at https://claude.ai/artifact/QWZRCtJs7it2aQR5CqgLhh. All sound is generated live with the Web Audio API.
