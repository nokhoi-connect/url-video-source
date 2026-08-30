from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI(title="URL Video", docs_url=None, redoc_url=None)
PACKAGE = Path(__file__).with_name("URL-Video-para-Windows.zip")

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Aplicación gratuita para descargar contenido público autorizado en Windows.">
<title>URL Video — Aplicación gratuita para Windows</title>
<style>body{margin:0;background:#0b1020;color:#edf2ff;font:16px system-ui,sans-serif}.box{max-width:720px;margin:10vh auto;padding:38px;background:#121a30;border:1px solid #28365d;border-radius:20px}.free{display:inline-block;margin:0 0 18px;padding:6px 10px;border-radius:999px;background:#153b31;color:#8cf3cd;font-size:13px;font-weight:700}h1{margin:0 0 10px;font-size:clamp(28px,6vw,42px)}p{color:#b9c4db;line-height:1.6}.button{display:block;margin:28px 0 14px;padding:15px;text-align:center;border-radius:10px;background:#765cff;color:#fff;text-decoration:none;font-weight:700}.note{font-size:13px;color:#94a3bd}@media(max-width:480px){.box{margin:5vh 16px;padding:26px}}</style></head>
<body><main class="box"><span class="free">100 % GRATIS</span><h1>Descarga vídeos y audio en tu PC</h1><p>Instala URL Video en Windows y pega un enlace público para guardar una copia en MP4 o MP3 directamente en tu ordenador.</p><a class="button" href="/descargar-aplicacion">Descargar aplicación para Windows</a><p class="note">La descarga se procesa en tu propio ordenador: esta web no descarga vídeos online ni guarda enlaces. Úsala solo para contenido propio, público o con permiso. No funciona con contenido privado, de pago ni protegido por DRM.</p><p class="note">Software de Nokhoi Connect.</p></main></body></html>"""


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return PAGE


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/descargar-aplicacion")
def download_app() -> FileResponse:
    if not PACKAGE.is_file():
        raise HTTPException(503, "La aplicación se está publicando. Vuelve a intentarlo en unos minutos.")
    return FileResponse(PACKAGE, filename="URL-Video-para-Windows.zip", media_type="application/zip")
