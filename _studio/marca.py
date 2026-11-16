"""Piezas de marca compartidas por los vídeos y los carruseles de Devuelto."""
import html, re

NAVY = "#0E1A2B"
PAPER = "#F7F6F2"
GREEN = "#2FAF6E"        # verde sobre fondo oscuro
GREEN_DARK = "#187A4C"   # verde sobre fondo claro


def simbolo(color_trazo=PAPER, color_punto=GREEN, punto=True):
    p = (f'<g transform="translate(0 3)"><path d="M26.25 30.07 A31 31 0 1 0 50.00 19.00" fill="none" '
         f'stroke="{color_trazo}" stroke-width="10" stroke-linecap="round"/>'
         f'<path d="M41.60 19.00 L55.60 8.00 L55.60 30.00 Z" fill="{color_trazo}" stroke="{color_trazo}" '
         f'stroke-width="2" stroke-linejoin="round"/>')
    if punto:
        p += f'<circle cx="50" cy="50" r="10.5" fill="{color_punto}"/>'
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{p}</g></svg>'


def rich(texto):
    """Escapa el texto y convierte [[...]] en un tramo verde."""
    t = html.escape(texto, quote=False)
    return re.sub(r"\[\[(.+?)\]\]", r'<span class="g">\1</span>', t)


def palabras(texto, clase="w"):
    """Divide el texto en palabras (respetando los tramos verdes) para animarlas una a una."""
    out, i = [], 0
    for m in re.finditer(r"\[\[(.+?)\]\]|(\S+)", texto):
        if m.group(1):
            for w in m.group(1).split():
                out.append((w, True))
        else:
            out.append((m.group(2), False))
    return out


def plano(texto):
    return re.sub(r"\[\[(.+?)\]\]", r"\1", texto)


CTAS = {
    "fianza": ("¿No te han devuelto la fianza?", "Calcula cuánto te deben"),
    "agencia": ("¿Pagaste honorarios a la inmobiliaria?", "Calcula cuánto puedes recuperar"),
    "burofax": ("¿Te lo preparamos?", "Tu burofax de fianza, listo para enviar, por 19 €"),
    "guardar": ("Guárdalo para tu próximo piso", "Y si algún día no te devuelven la fianza, calcula cuánto te deben"),
}
