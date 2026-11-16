"""Genera los carruseles de Devuelto: 1080×1350 (Instagram y Facebook) y 1080×1920 (TikTok).

Uso: python3 carrusel.py SEMANA.py [ID...]   → out/<semana>/<id>-<n>.jpg y <id>-tt-<n>.jpg
"""
import os, sys
from playwright.sync_api import sync_playwright
from marca import simbolo, rich, CTAS
import video

AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:var(--h);overflow:hidden}
.s{position:relative;width:1080px;height:var(--h);overflow:hidden;background:#F7F6F2;color:#0E1A2B;font-family:Inter,sans-serif}
.s.dark{background:#0E1A2B;color:#F7F6F2}
.deco{position:absolute;width:900px;height:900px;right:-360px;bottom:-260px;opacity:.06}
.head{position:absolute;left:90px;right:90px;top:var(--top);display:flex;align-items:center;gap:16px}
.head svg{width:50px;height:50px}
.head span{font-weight:600;font-size:31px}
.head em{margin-left:auto;font-style:normal;font-weight:600;font-size:28px;opacity:.5}
.body{position:absolute;left:90px;right:90px;top:var(--bt);bottom:var(--bb);display:flex;flex-direction:column;justify-content:center}
.kicker{font-weight:700;font-size:31px;letter-spacing:.16em;text-transform:uppercase;color:#187A4C;margin-bottom:38px}
.g{color:#187A4C}
.dark .g{color:#2FAF6E}
.cover{font-family:Lora,serif;font-weight:600;font-size:100px;line-height:1.08;letter-spacing:-.015em}
.title{font-family:Lora,serif;font-weight:600;font-size:76px;line-height:1.12;letter-spacing:-.01em}
.txt{font-weight:500;font-size:46px;line-height:1.42;color:#33435A;margin-top:38px}
.tag{align-self:flex-start;font-weight:700;font-size:28px;letter-spacing:.15em;text-transform:uppercase;padding:12px 22px;border-radius:10px;margin-bottom:34px;background:#187A4C;color:#F7F6F2}
.tag.no{background:#0E1A2B}
.tag.m{background:rgba(14,26,43,.08);color:rgba(14,26,43,.6)}
.step{display:flex;gap:42px;align-items:flex-start}
.step .n{flex:none;width:128px;height:128px;border-radius:50%;background:#187A4C;color:#F7F6F2;font-family:Lora,serif;font-weight:700;font-size:74px;display:flex;align-items:center;justify-content:center}
.step .title{font-size:70px}
ul{margin-top:10px}
li{list-style:none;display:flex;gap:30px;align-items:flex-start;font-weight:500;font-size:48px;line-height:1.32;margin-top:40px}
li b{flex:none;width:58px;height:58px;border-radius:50%;background:#187A4C;display:flex;align-items:center;justify-content:center;margin-top:2px}
li b svg{width:32px;height:32px}
.num{font-family:Lora,serif;font-weight:600;font-size:220px;line-height:1;color:#187A4C;letter-spacing:-.02em;white-space:nowrap}
.sub{font-weight:500;font-size:54px;line-height:1.32;margin-top:44px}
.law{border-left:10px solid #187A4C;padding:6px 0 6px 50px}
.law .ref{font-weight:700;font-size:29px;letter-spacing:.12em;text-transform:uppercase;color:#187A4C;margin-bottom:34px;line-height:1.3}
.law .t{font-family:Lora,serif;font-style:italic;font-weight:500;font-size:64px;line-height:1.26}
.myth{font-family:Lora,serif;font-weight:500;font-size:58px;line-height:1.24;color:rgba(14,26,43,.45);text-decoration:line-through;text-decoration-thickness:4px;margin-bottom:70px}
.real{font-family:Lora,serif;font-weight:600;font-size:62px;line-height:1.2}
.swipe{position:absolute;right:90px;bottom:var(--sw);font-weight:600;font-size:30px;opacity:.55}
.cta{align-items:center;text-align:center}
.cta svg.big{width:190px;height:190px;margin-bottom:56px}
.cta .q1{font-family:Lora,serif;font-weight:600;font-size:80px;line-height:1.12}
.cta .q2{font-weight:500;font-size:46px;line-height:1.36;color:#C9D2DE;margin-top:32px}
.pill{margin-top:56px;background:#2FAF6E;color:#0E1A2B;font-weight:700;font-size:60px;padding:28px 64px;border-radius:999px}
.link{margin-top:30px;font-weight:500;font-size:34px;color:rgba(247,246,242,.62)}
.legal{position:absolute;left:90px;right:90px;bottom:var(--lg);text-align:center;font-size:26px;color:rgba(247,246,242,.45)}
"""

CHECK = '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="#F7F6F2" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

FORMATOS = {
    # alto, top cabecera, top cuerpo, bottom cuerpo, «desliza», aviso legal
    "ig": dict(h=1350, top=80, bt=190, bb=150, sw=70, lg=60),
    "tt": dict(h=1920, top=170, bt=300, bb=430, sw=330, lg=330),
}


def slide_html(sl, i, n, cta_post):
    t = sl["t"]
    dark = t == "cta"
    head_sym = simbolo() if dark else simbolo("#0E1A2B", "#187A4C")
    head = f'<div class="head">{head_sym}<span>devuelto.app</span><em>{i}/{n}</em></div>'
    b = ""
    if t == "portada":
        b = f'<div class="kicker">{sl["kicker"]}</div><div class="cover">{rich(sl["titulo"])}</div>'
    elif t == "texto":
        tag = ""
        if sl.get("etiqueta"):
            no = " no" if sl["etiqueta"].lower().startswith("no") else ""
            tag = f'<div class="tag{no}">{sl["etiqueta"]}</div>'
        b = f'{tag}<div class="title">{rich(sl["titulo"])}</div><div class="txt">{rich(sl["cuerpo"])}</div>'
    elif t == "lista":
        tag = f'<div class="tag">{sl["etiqueta"]}</div>' if sl.get("etiqueta") else ""
        items = "".join(f"<li><b>{CHECK}</b><span>{rich(x)}</span></li>" for x in sl["items"])
        b = f'{tag}<div class="title">{rich(sl["titulo"])}</div><ul>{items}</ul>'
    elif t == "paso":
        b = (f'<div class="step"><div class="n">{sl["n"]}</div><div><div class="title">{rich(sl["titulo"])}</div>'
             f'<div class="txt">{rich(sl["cuerpo"])}</div></div></div>')
    elif t == "numero":
        b = f'<div class="num">{sl["num"]}</div><div class="sub">{rich(sl["sub"])}</div>'
    elif t == "ley":
        b = f'<div class="law"><div class="ref">{sl["ref"]}</div><div class="t">«{rich(sl["texto"])}»</div></div>'
    elif t == "mito":
        b = (f'<div class="tag m">Mito</div><div class="myth">«{rich(sl["mito"])}»</div>'
             f'<div class="tag">Realidad</div><div class="real">{rich(sl["real"])}</div>')
    elif t == "cta":
        q1, q2 = CTAS[sl.get("variante", cta_post)]
        big = simbolo().replace("<svg", '<svg class="big"', 1)
        b = (f'{big}<div class="q1">{q1}</div><div class="q2">{q2}</div>'
             f'<div class="pill">devuelto.app</div><div class="link">Enlace en el perfil</div>')
    deco = f'<div class="deco">{simbolo("#0E1A2B" if not dark else "#F7F6F2", punto=False)}</div>' if t in ("portada", "cta") else ""
    swipe = '<div class="swipe">Desliza →</div>' if i < n else ""
    legal = '<div class="legal">Información general, no es asesoramiento jurídico. Devuelto no es un despacho de abogados.</div>' if dark else ""
    cls = "body cta" if dark else "body"
    return f'<div class="s{" dark" if dark else ""}">{deco}{head}<div class="{cls}">{b}</div>{swipe}{legal}</div>'


def render(post, carpeta, pg):
    n = len(post["slides"])
    rutas = {"ig": [], "tt": []}
    for fmt, f in FORMATOS.items():
        pg.set_viewport_size({"width": 1080, "height": f["h"]})
        for i, sl in enumerate(post["slides"], 1):
            vars_ = ";".join(f"--{k}:{v}px" for k, v in f.items())
            doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>:root{{{vars_}}}{CSS}</style></head>'
                   f'<body>{slide_html(sl, i, n, post["cta"])}</body></html>')
            pg.set_content(doc)
            suf = "" if fmt == "ig" else "tt-"
            ruta = os.path.join(carpeta, f'{post["id"]}-{suf}{i}.jpg')
            pg.screenshot(path=ruta, type="jpeg", quality=93)
            rutas[fmt].append(ruta)
    return rutas


if __name__ == "__main__":
    semana, ids = sys.argv[1], sys.argv[2:]
    posts = {p["id"]: p for p in video.cargar(semana) if p["tipo"] == "carrusel"}
    carpeta = os.path.join(AQUI, "out", os.path.splitext(os.path.basename(semana))[0])
    os.makedirs(carpeta, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i in ids or posts.keys():
            render(posts[i], carpeta, pg)
            print(i, flush=True)
        b.close()
