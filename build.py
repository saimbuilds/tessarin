"""Builds dist/tessarin-standalone.html: index.html with the fonts and logo inlined,
so the page works as one file (double-click to open, or share as an attachment).

Usage:  python build.py
"""
import base64, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def b64(path):
    with open(os.path.join(ROOT, path), "rb") as f:
        return base64.b64encode(f.read()).decode()

html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

css = open(os.path.join(ROOT, "brand/fonts/fonts.css"), encoding="utf-8").read()
css = re.sub(r'url\("([^"]+\.woff2)"\)', lambda m: f'url(data:font/woff2;base64,{b64("brand/fonts/" + m.group(1))})', css)
html = html.replace('<link rel="stylesheet" href="brand/fonts/fonts.css">', f"<style>{css}</style>")
html = html.replace("brand/tessarin-logo.png", "data:image/png;base64," + b64("brand/tessarin-logo.png"))

os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
out = os.path.join(ROOT, "dist/tessarin-standalone.html")
open(out, "w", encoding="utf-8").write(html)
print(f"Wrote {out} ({len(html)//1024} KB)")
