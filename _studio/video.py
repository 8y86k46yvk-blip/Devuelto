"""Genera los vídeos verticales (1080×1920) de Devuelto: animación de texto + música propia.

Uso: python3 video.py SEMANA.py ID [ID...]   → escribe out/<semana>/<id>.mp4 y <id>-portada.jpg
"""
import json, math, os, re, subprocess, sys, wave, importlib.util
import numpy as np
from marca import NAVY, PAPER, GREEN, simbolo, rich, palabras, plano, CTAS

FPS = 30
W, H = 1080, 1920
AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0E1A2B}
#v{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif;color:#F7F6F2;
   background:radial-gradient(1300px 1000px at 50% 38%,#15263D 0%,#0E1A2B 72%)}
.deco{position:absolute;width:980px;height:980px;right:-380px;bottom:60px;opacity:.045}
.deco2{position:absolute;width:620px;height:620px;left:-300px;top:-230px;opacity:.035}
.bar{position:absolute;left:90px;right:90px;top:104px;height:6px;border-radius:3px;background:rgba(247,246,242,.12);overflow:hidden}
.bar i{display:block;height:100%;width:100%;background:#2FAF6E;transform-origin:0 50%;transform:scaleX(0)}
.top{position:absolute;left:90px;top:150px;display:flex;align-items:center;gap:18px}
.top svg{width:54px;height:54px}
.top span{font-weight:600;font-size:33px;color:rgba(247,246,242,.85)}
.scene{position:absolute;left:90px;right:90px;top:300px;height:1140px;display:flex;flex-direction:column;justify-content:center;opacity:0}
.kicker{font-weight:700;font-size:31px;letter-spacing:.16em;text-transform:uppercase;color:#2FAF6E;margin-bottom:40px}
.hook{font-family:Lora,serif;font-weight:600;font-size:100px;line-height:1.1;letter-spacing:-.012em}
.w{display:inline-block;white-space:pre}
.g{color:#2FAF6E}
.title{font-family:Lora,serif;font-weight:600;font-size:80px;line-height:1.14;letter-spacing:-.01em}
.body{font-weight:500;font-size:48px;line-height:1.4;color:#C9D2DE;margin-top:40px}
.num{font-family:Lora,serif;font-weight:600;font-size:200px;line-height:1;color:#2FAF6E;letter-spacing:-.02em;white-space:nowrap}
.sub{font-weight:500;font-size:52px;line-height:1.34;margin-top:46px}
.law{border-left:10px solid #2FAF6E;padding:8px 0 8px 52px}
.law .ref{font-weight:700;font-size:30px;letter-spacing:.12em;text-transform:uppercase;color:#2FAF6E;margin-bottom:36px;line-height:1.3}
.law .txt{font-family:Lora,serif;font-style:italic;font-weight:500;font-size:64px;line-height:1.26}
.tag{align-self:flex-start;font-weight:700;font-size:30px;letter-spacing:.16em;text-transform:uppercase;padding:12px 22px;border-radius:10px;margin-bottom:30px}
.tag.m{background:rgba(247,246,242,.1);color:rgba(247,246,242,.72)}
.tag.r{background:#2FAF6E;color:#0E1A2B}
.myth{font-family:Lora,serif;font-weight:500;font-size:62px;line-height:1.24;color:rgba(247,246,242,.62);margin-bottom:84px;
      text-decoration:line-through;text-decoration-thickness:5px;text-decoration-color:rgba(247,246,242,0)}
.real{font-family:Lora,serif;font-weight:600;font-size:72px;line-height:1.18}
.step{display:flex;gap:44px;align-items:flex-start}
.step .n{flex:none;width:136px;height:136px;border-radius:50%;background:#2FAF6E;color:#0E1A2B;font-family:Lora,serif;font-weight:700;font-size:80px;display:flex;align-items:center;justify-content:center}
.step .title{font-size:72px}
.list{margin-top:6px}
.list li{list-style:none;display:flex;gap:32px;align-items:flex-start;font-weight:500;font-size:54px;line-height:1.3;margin-top:44px}
.list li b{flex:none;width:64px;height:64px;border-radius:50%;background:#2FAF6E;display:flex;align-items:center;justify-content:center;margin-top:2px}
.list li b svg{width:34px;height:34px}
.quote{font-family:Lora,serif;font-style:italic;font-weight:500;font-size:78px;line-height:1.2}
.quote .q{color:#2FAF6E;font-style:normal}
.ans{margin-top:70px;border-left:10px solid #2FAF6E;padding-left:46px;font-weight:500;font-size:52px;line-height:1.38}
.cta{align-items:center;text-align:center}
.cta svg.s{width:210px;height:210px;margin-bottom:60px}
.cta .q1{font-family:Lora,serif;font-weight:600;font-size:76px;line-height:1.15}
.cta .q2{font-weight:500;font-size:46px;line-height:1.35;color:#C9D2DE;margin-top:34px}
.pill{margin-top:60px;background:#2FAF6E;color:#0E1A2B;font-weight:700;font-size:62px;padding:30px 66px;border-radius:999px}
.link{margin-top:34px;font-weight:500;font-size:36px;color:rgba(247,246,242,.6)}
"""

JS = r"""
const T = +document.body.dataset.total;
const E = 'cubic-bezier(.2,.75,.2,1)';
function kf(list){ return list.map(([o,p])=>Object.assign({offset:Math.min(1,Math.max(0,o/T))},p)); }
document.querySelectorAll('.scene').forEach(s=>{
  const st=+s.dataset.start, en=+s.dataset.end, last=s.dataset.last==='1';
  const a=[[0,{opacity:st===0?1:0,transform:'none'}],[st,{opacity:st===0?1:0,transform:'none'}],
           [st+(st===0?0:260),{opacity:1,transform:'none'}]];
  if(!last){ a.push([en-260,{opacity:1,transform:'none'}],[en,{opacity:0,transform:'translateY(-30px)'}],[T,{opacity:0,transform:'translateY(-30px)'}]); }
  else { a.push([T,{opacity:1,transform:'none'}]); }
  s.animate(kf(a),{duration:T,fill:'both'});
  s.querySelectorAll('[data-k]').forEach(el=>{
    const d=st+(+el.dataset.d||0), k=el.dataset.k;
    if(k==='up') el.animate([{opacity:0,transform:'translateY(50px)'},{opacity:1,transform:'none'}],{delay:d,duration:650,fill:'both',easing:E});
    if(k==='fade') el.animate([{opacity:0},{opacity:1}],{delay:d,duration:500,fill:'both',easing:E});
    if(k==='pop') el.animate([{opacity:0,transform:'scale(.8)'},{opacity:1,transform:'scale(1)'}],{delay:d,duration:750,fill:'both',easing:'cubic-bezier(.2,1.35,.4,1)'});
    if(k==='left') el.animate([{opacity:0,transform:'translateX(-60px)'},{opacity:1,transform:'none'}],{delay:d,duration:600,fill:'both',easing:E});
    if(k==='strike') el.animate([{textDecorationColor:'rgba(247,246,242,0)',color:'rgba(247,246,242,.62)'},{textDecorationColor:'rgba(247,246,242,.8)',color:'rgba(247,246,242,.42)'}],{delay:d,duration:450,fill:'both',easing:E});
  });
});
document.querySelector('.bar i').animate([{transform:'scaleX(0)'},{transform:'scaleX(1)'}],{duration:T,fill:'both'});
document.querySelector('.deco').animate([{transform:'rotate(0deg)'},{transform:'rotate(28deg)'}],{duration:T,fill:'both'});
document.querySelector('.deco2').animate([{transform:'rotate(0deg)'},{transform:'rotate(-20deg)'}],{duration:T,fill:'both'});
const anims=document.getAnimations(); anims.forEach(a=>a.pause());
const counts=[...document.querySelectorAll('[data-count]')];
function fmt(v,dec){ let s=v.toFixed(dec); let [i,f]=s.split('.'); i=i.replace(/\B(?=(\d{3})+(?!\d))/g,'.'); return f?i+','+f:i; }
window.setTime=function(t){
  anims.forEach(a=>a.currentTime=t);
  counts.forEach(el=>{ const s=+el.dataset.s, du=900, to=+el.dataset.count, dec=+el.dataset.dec;
    const p=Math.min(1,Math.max(0,(t-s)/du)), e=1-Math.pow(1-p,3);
    el.textContent=el.dataset.pre+fmt(to*e,dec)+el.dataset.suf; });
};
"""

CHECK = '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="#0E1A2B" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def contar(texto):
    return len(plano(texto).split())


def duracion(e):
    t = e["t"]
    if t == "hook":
        return min(4200, max(2900, 1400 + contar(e["texto"]) * 260))
    if t == "lista":
        return int(1500 + len(e["items"]) * 950 + contar(" ".join(e["items"])) * 120)
    if t == "cta":
        return 3600
    txt = " ".join(str(v) for k, v in e.items() if k not in ("t", "n"))
    return int(min(5800, max(3000, 1400 + contar(txt) * 225)))


def numero_partes(num):
    m = re.match(r"^([+]?)(\d{1,3}(?:\.\d{3})*|\d+)(?:,(\d+))?(.*)$", num)
    if not m:
        return None
    pre, ent, dec, suf = m.groups()
    valor = float(ent.replace(".", "") + ("." + dec if dec else ""))
    return pre, valor, len(dec) if dec else 0, suf


def escena_html(e, start, end, last, cta_tipo):
    t = e["t"]
    inner = ""
    if t == "hook":
        inner += f'<div class="kicker" data-k="fade" data-d="0">{e["kicker"]}</div>'
        ws = []
        dd = 120 if start > 0 else 60
        for i, (w, g) in enumerate(palabras(e["texto"])):
            cls = "w g" if g else "w"
            ws.append(f'<span class="{cls}" data-k="up" data-d="{dd + i * 85}">{rich(w)}</span>')
        inner += f'<div class="hook">{" ".join(ws)}</div>'
    elif t == "texto":
        inner += f'<div class="title" data-k="up" data-d="80">{rich(e["titulo"])}</div>'
        inner += f'<div class="body" data-k="up" data-d="420">{rich(e["cuerpo"])}</div>'
    elif t == "numero":
        p = numero_partes(e["num"])
        if p and p[1] >= 10:
            pre, val, dec, suf = p
            inner += (f'<div class="num" data-k="pop" data-d="60" data-count="{val}" data-dec="{dec}" '
                      f'data-pre="{pre}" data-suf="{suf}" data-s="{start + 60}">{e["num"]}</div>')
        else:
            inner += f'<div class="num" data-k="pop" data-d="60">{e["num"]}</div>'
        inner += f'<div class="sub" data-k="up" data-d="520">{rich(e["sub"])}</div>'
    elif t == "ley":
        inner += (f'<div class="law" data-k="left" data-d="60"><div class="ref">{e["ref"]}</div>'
                  f'<div class="txt" data-k="fade" data-d="420">«{rich(e["texto"])}»</div></div>')
    elif t == "mito":
        inner += f'<div class="tag m" data-k="fade" data-d="40">Mito</div>'
        inner += (f'<div data-k="up" data-d="120"><div class="myth" data-k="strike" data-d="1500">'
                  f'«{rich(e["mito"])}»</div></div>')
        inner += f'<div class="tag r" data-k="fade" data-d="1700">Realidad</div>'
        inner += f'<div class="real" data-k="up" data-d="1800">{rich(e["real"])}</div>'
    elif t == "paso":
        inner += (f'<div class="step"><div class="n" data-k="pop" data-d="40">{e["n"]}</div><div>'
                  f'<div class="title" data-k="up" data-d="200">{rich(e["titulo"])}</div>'
                  f'<div class="body" data-k="up" data-d="520">{rich(e["cuerpo"])}</div></div></div>')
    elif t == "lista":
        inner += f'<div class="title" data-k="up" data-d="60">{rich(e["titulo"])}</div><ul class="list">'
        for i, it in enumerate(e["items"]):
            inner += f'<li data-k="left" data-d="{500 + i * 800}"><b>{CHECK}</b><span>{rich(it)}</span></li>'
        inner += "</ul>"
    elif t == "dialogo":
        inner += f'<div class="quote" data-k="up" data-d="60"><span class="q">«</span>{rich(e["frase"])}<span class="q">»</span></div>'
        inner += f'<div class="ans" data-k="left" data-d="1300">{rich(e["respuesta"])}</div>'
    elif t == "cta":
        q1, q2 = CTAS[cta_tipo]
        inner += f'<div data-k="pop" data-d="40">{simbolo().replace("<svg", "<svg class=\"s\"", 1)}</div>'
        inner += f'<div class="q1" data-k="up" data-d="300">{q1}</div>'
        inner += f'<div class="q2" data-k="up" data-d="520">{q2}</div>'
        inner += f'<div class="pill" data-k="pop" data-d="800">devuelto.app</div>'
        inner += f'<div class="link" data-k="fade" data-d="1100">Enlace en el perfil</div>'
    cls = "scene cta" if t == "cta" else "scene"
    return f'<div class="{cls}" data-start="{start}" data-end="{end}" data-last="{1 if last else 0}">{inner}</div>'


def construir(post):
    escenas = list(post["escenas"]) + [{"t": "cta"}]
    t, partes, cortes = 0, [], []
    for i, e in enumerate(escenas):
        du = duracion(e)
        last = i == len(escenas) - 1
        partes.append(escena_html(e, t, t + du, last, post["cta"]))
        cortes.append(t)
        t += du
    total = t
    doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head>'
           f'<body data-total="{total}"><div id="v">'
           f'<div class="deco">{simbolo(punto=False)}</div><div class="deco2">{simbolo(punto=False)}</div>'
           f'<div class="bar"><i></i></div><div class="top">{simbolo()}<span>devuelto.app</span></div>'
           + "".join(partes) + f'</div><script>{JS}</script></body></html>')
    return doc, total, cortes


# ───────── música propia (sin derechos de terceros) ─────────
PROGS = [
    (90, [("A", [57, 60, 64]), ("F", [53, 57, 60]), ("C", [48, 52, 55, 60]), ("G", [55, 59, 62])]),
    (84, [("D", [50, 53, 57]), ("Bb", [46, 50, 53]), ("F", [53, 57, 60]), ("C", [48, 52, 55])]),
    (96, [("E", [52, 55, 59]), ("C", [48, 52, 55]), ("G", [55, 59, 62]), ("D", [50, 54, 57])]),
]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def musica(seg, variante, cortes_ms, ruta, sr=44100):
    bpm, prog = PROGS[variante % len(PROGS)]
    beat = 60 / bpm
    bar = beat * 4
    n = int(seg * sr)
    t = np.arange(n) / sr
    out = np.zeros(n)
    rng = np.random.default_rng(variante + 7)
    nbar = int(math.ceil(seg / bar)) + 1
    for b in range(nbar):
        _, notas = prog[b % len(prog)]
        t0 = b * bar
        i0, i1 = int(t0 * sr), min(n, int((t0 + bar * 1.15) * sr))
        if i0 >= n:
            break
        tt = t[i0:i1] - t0
        env = np.minimum(1, tt / 0.9) * np.exp(-np.maximum(0, tt - bar) * 4)
        for m in notas:
            f = hz(m)
            for det in (-0.35, 0.35):
                out[i0:i1] += 0.05 * env * (np.sin(2 * np.pi * (f + det) * tt) + 0.18 * np.sin(2 * np.pi * 2 * (f + det) * tt))
        # bajo suave en cada tiempo
        root = hz(notas[0] - 12)
        for k in range(4):
            s0 = int((t0 + k * beat) * sr)
            s1 = min(n, s0 + int(beat * sr))
            if s0 >= n:
                break
            tb = t[s0:s1] - (t0 + k * beat)
            out[s0:s1] += 0.10 * np.exp(-tb * 3.2) * np.minimum(1, tb / 0.01) * np.sin(2 * np.pi * root * tb)
        # arpegio en corcheas, muy bajo
        arp = [notas[j % len(notas)] + 12 for j in (0, 1, 2, 1, 0, 2, 1, 2)]
        for k, m in enumerate(arp):
            s0 = int((t0 + k * beat / 2) * sr)
            s1 = min(n, s0 + int(0.6 * sr))
            if s0 >= n:
                break
            ta = t[s0:s1] - (t0 + k * beat / 2)
            out[s0:s1] += 0.035 * np.exp(-ta * 6) * np.minimum(1, ta / 0.004) * np.sin(2 * np.pi * hz(m) * ta)
    # «whoosh» suave en cada cambio de escena
    for c in cortes_ms[1:]:
        s0 = int((c / 1000 - 0.18) * sr)
        s1 = min(n, s0 + int(0.42 * sr))
        if s0 < 0 or s0 >= n:
            continue
        ln = s1 - s0
        ruido = rng.standard_normal(ln)
        ruido = np.convolve(ruido, np.ones(24) / 24, mode="same")
        env = np.sin(np.linspace(0, np.pi, ln)) ** 2
        out[s0:s1] += 0.10 * ruido * env
    # paso bajo de un polo para suavizar
    try:
        from scipy.signal import lfilter
        y = lfilter([0.18], [1, -0.82], out)
    except ImportError:
        y = np.zeros_like(out)
        acc = 0.0
        for i in range(n):
            acc += 0.18 * (out[i] - acc)
            y[i] = acc
    y *= np.minimum(1, t / 0.6) * np.minimum(1, (seg - t) / 1.2)
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.5
    pcm = (y * 32767).astype(np.int16)
    with wave.open(ruta, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


def render(post, carpeta):
    from playwright.sync_api import sync_playwright
    doc, total, cortes = construir(post)
    os.makedirs(carpeta, exist_ok=True)
    html_path = os.path.join(carpeta, f'{post["id"]}.html')
    open(html_path, "w").write(doc)
    seg = total / 1000
    wav = os.path.join(carpeta, f'{post["id"]}.wav')
    musica(seg, post.get("musica", 0), cortes, wav)
    mp4 = os.path.join(carpeta, f'{post["id"]}.mp4')
    nframes = int(math.ceil(seg * FPS))
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg",
                           "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
                           "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", mp4],
                          stdin=subprocess.PIPE)
    portada_ms = min(cortes[1] - 300, 2600) if len(cortes) > 1 else 2000
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto("file://" + html_path)
        pg.wait_for_timeout(200)
        for i in range(nframes):
            pg.evaluate(f"setTime({i * 1000 / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        pg.evaluate(f"setTime({portada_ms})")
        pg.screenshot(path=os.path.join(carpeta, f'{post["id"]}-portada.jpg'), type="jpeg", quality=92)
        b.close()
    ff.stdin.close()
    ff.wait()
    os.remove(wav)
    return mp4, seg, portada_ms


def cargar(semana):
    spec = importlib.util.spec_from_file_location("semana", semana)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.POSTS


if __name__ == "__main__":
    semana, ids = sys.argv[1], sys.argv[2:]
    posts = {p["id"]: p for p in cargar(semana) if p["tipo"] == "video"}
    nombre = os.path.splitext(os.path.basename(semana))[0]
    carpeta = os.path.join(AQUI, "out", nombre)
    res = {}
    for i in ids or posts.keys():
        mp4, seg, pms = render(posts[i], carpeta)
        res[i] = {"seg": round(seg, 2), "portada_ms": pms}
        print(i, round(seg, 1), "s", flush=True)
    meta = os.path.join(carpeta, "videos.json")
    old = json.load(open(meta)) if os.path.exists(meta) else {}
    old.update(res)
    json.dump(old, open(meta, "w"), indent=1)
