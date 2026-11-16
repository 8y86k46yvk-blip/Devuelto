# Estudio de contenido de Devuelto

Genera y programa las publicaciones de Instagram, Facebook y TikTok de Devuelto
(marca «Devuelto» en Metricool, blogId `8136501`, zona horaria `Atlantic/Canary`).

## Ritmo

3 publicaciones al día, todos los días:

| Hora (Canarias) | Formato | Redes |
|---|---|---|
| 10:00 | Vídeo vertical animado (Reel) | Instagram, Facebook y TikTok |
| 13:00 | Carrusel educativo | Instagram y Facebook (4:5) + TikTok en modo foto (9:16) |
| 18:00 | Vídeo vertical animado (Reel) | Instagram, Facebook y TikTok |

Las horas salen de las mejores franjas de TikTok en Metricool (picos a las 10, 12 y 18 h).

## Estilo

- Serio, limpio y profesional. Sin muñecos ni personajes. Azul tinta, blanco roto y verde.
- Nunca usar la palabra «IA». Devuelto no es un despacho de abogados: no prometer resultados.
- Cada dato legal se comprueba antes de publicarlo. Nada de inventar casos ni testimonios: los ejemplos
  van como «Imagina…» o «Ejemplo».
- Mezcla que mejor funciona en cuentas de derechos del inquilino: ganchos tipo pregunta, mito/realidad,
  «frases de casero», pasos y checklists, cifras clave y noticias contrastadas.
- Fianza (19 €) y honorarios de inmobiliaria (29 €). CTA siempre a devuelto.app.

## Proceso semanal

1. Lee `temas.md` para no repetir temas y, si hay datos, mira en Metricool qué publicaciones de la
   semana anterior funcionaron mejor para repetir su formato.
2. Comprueba con búsquedas cualquier dato que pueda haber cambiado (interés legal del dinero, leyes).
3. Escribe `semanas/AAAA-MM-DD.py` (lunes de la semana) con la misma estructura que las anteriores:
   14 vídeos (`v01`–`v14`) y 7 carruseles (`c01`–`c07`).
4. `python3 video.py semanas/X.py` y `python3 carrusel.py semanas/X.py` (salen en `out/X/`).
   Revisa algunos fotogramas con `preview.py` antes de seguir.
5. `python3 publicar.py semanas/X.py` → copia los archivos a `/redes/X/` y crea `out/X/plan.json`.
6. Commit y push a `main`. Espera a que GitHub Pages publique y comprueba que un archivo de
   `https://devuelto.app/redes/X/` responde.
7. Programa cada entrada de `plan.json` con `createScheduledPost` (blogId, date, info en JSON).
   TikTok exige `tiktokData.title` también en los vídeos (ya lo pone `publicar.py`).
8. Añade los temas nuevos a `temas.md`.

Dependencias: Python 3 con numpy, Playwright (Chromium), Pillow y ffmpeg; fuentes Lora e Inter.
