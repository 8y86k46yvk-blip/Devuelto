"""Copia los archivos de una semana a /redes/<semana>/ (los sirve devuelto.app) y escribe
plan.json con las publicaciones listas para programar en Metricool (createScheduledPost).

Uso: python3 publicar.py SEMANA.py
"""
import json, os, shutil, sys
import video

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
BASE_URL = "https://devuelto.app/redes"
BLOG_ID = "8136501"          # marca «Devuelto» en Metricool
TZ = "Atlantic/Canary"

COMUN = {"autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "",
         "hasNotReadNotes": False, "mediaAltText": [], "shortener": False, "smartLinkData": {"ids": []}}
TIKTOK = {"privacyOption": "PUBLIC_TO_EVERYONE", "disableComment": False, "disableDuet": False,
          "disableStitch": False, "commercialContentOwnBrand": True, "commercialContentThirdParty": False}


def main(semana):
    nombre = os.path.splitext(os.path.basename(semana))[0]
    origen = os.path.join(AQUI, "out", nombre)
    destino = os.path.join(REPO, "redes", nombre)
    os.makedirs(destino, exist_ok=True)
    meta = json.load(open(os.path.join(origen, "videos.json")))
    plan = []
    for p in video.cargar(semana):
        fecha = p["fecha"]
        base = {**COMUN, "publicationDate": {"dateTime": fecha, "timezone": TZ}, "text": p["texto"]}
        if p["tipo"] == "video":
            f = f'{p["id"]}.mp4'
            shutil.copy(os.path.join(origen, f), destino)
            info = {**base, "media": [f"{BASE_URL}/{nombre}/{f}"],
                    "videoCoverMilliseconds": meta[p["id"]]["portada_ms"],
                    "providers": [{"network": "instagram"}, {"network": "facebook"}, {"network": "tiktok"}],
                    "instagramData": {"type": "REEL", "showReelOnFeed": True},
                    "facebookData": {"type": "REEL"},
                    "tiktokData": {**TIKTOK, "autoAddMusic": False}}
            plan.append({"id": p["id"], "red": "ig+fb+tt", "date": fecha + "+00:00", "info": info})
        else:
            n = len(p["slides"])
            ig, tt = [], []
            for i in range(1, n + 1):
                for suf, lst in (("", ig), ("tt-", tt)):
                    f = f'{p["id"]}-{suf}{i}.jpg'
                    shutil.copy(os.path.join(origen, f), destino)
                    lst.append(f"{BASE_URL}/{nombre}/{f}")
            plan.append({"id": p["id"], "red": "ig+fb", "date": fecha + "+00:00",
                         "info": {**base, "media": ig, "providers": [{"network": "instagram"}, {"network": "facebook"}],
                                  "instagramData": {"type": "POST"}, "facebookData": {"type": "POST"}}})
            plan.append({"id": p["id"] + "-tt", "red": "tt", "date": fecha + "+00:00",
                         "info": {**base, "media": tt, "providers": [{"network": "tiktok"}],
                                  "tiktokData": {**TIKTOK, "title": p["titulo_tiktok"], "autoAddMusic": True,
                                                 "photoCoverIndex": 0}}})
    json.dump({"blogId": BLOG_ID, "publicaciones": plan}, open(os.path.join(origen, "plan.json"), "w"),
              ensure_ascii=False, indent=1)
    print(len(plan), "publicaciones en el plan")


if __name__ == "__main__":
    main(sys.argv[1])
