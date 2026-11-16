"""Hoja de contactos de un vídeo: fotogramas en varios instantes (para revisar el diseño)."""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
import video
posts = {p["id"]: p for p in video.cargar(sys.argv[1])}
out = sys.argv[3]
p = posts[sys.argv[2]]
doc, total, cortes = video.construir(p)
open("/tmp/prev.html", "w").write(doc)
ts = []
for i, c in enumerate(cortes):
    end = cortes[i + 1] if i + 1 < len(cortes) else total
    ts.append(min(end - 300, c + 2400) if i < len(cortes) - 1 else total - 100)
ts = [100] + ts
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file:///tmp/prev.html"); pg.wait_for_timeout(200)
    ims = []
    for t in ts:
        pg.evaluate(f"setTime({t})"); pg.screenshot(path="/tmp/f.png"); ims.append(Image.open("/tmp/f.png").convert("RGB").resize((360, 640)))
    b.close()
sheet = Image.new("RGB", (360 * len(ims) + 10 * (len(ims) - 1), 640), "white")
for i, im in enumerate(ims): sheet.paste(im, (i * 370, 0))
sheet.save(out); print(total, cortes, ts)
