from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI(title="URL Video", docs_url=None, redoc_url=None)
PACKAGE = Path(__file__).with_name("URL-Video-para-Windows.zip")

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Aplicación gratuita para descargar contenido público autorizado en Windows.">
<title>URL Video — Aplicación gratuita para Windows</title>
<style>body{margin:0;background:#0b1020;color:#edf2ff;font:16px system-ui,sans-serif}.box{max-width:720px;margin:10vh auto;padding:38px;background:#121a30;border:1px solid #28365d;border-radius:20px}.logo{display:block;max-width:320px;width:100%;margin:0 auto 22px;border-radius:14px}.free{display:inline-block;margin:0 0 18px;padding:6px 10px;border-radius:999px;background:#153b31;color:#8cf3cd;font-size:13px;font-weight:700}h1{margin:0 0 10px;font-size:clamp(28px,6vw,42px)}p{color:#b9c4db;line-height:1.6}.button{display:block;margin:28px 0 14px;padding:15px;text-align:center;border-radius:10px;background:#765cff;color:#fff;text-decoration:none;font-weight:700}.note{font-size:13px;color:#94a3bd}.mobile-only{display:none}@media(max-width:480px){.box{margin:20vh 16px;padding:26px}.desktop-only{display:none}.mobile-only{display:block}}</style></head>
<body><main class="box"><div class="desktop-only"><img class="logo" src="/codex-clipboard-257a04c3-4734-4b04-9daa-a9edc1355c06.jpg" alt="Alien Downloader"><span class="free">100 % GRATIS</span><h1>Descarga vídeos y audio en tu PC</h1><p>Instala URL Video en Windows y pega un enlace público para guardar una copia en MP4 o MP3 directamente en tu ordenador.</p><a class="button" href="/descargar-aplicacion">Descargar aplicación para Windows</a><p class="note">La descarga se procesa en tu propio ordenador: esta web no descarga vídeos online ni guarda enlaces. Úsala solo para contenido propio, público o con permiso. No funciona con contenido privado, de pago ni protegido por DRM.</p><p class="note">Software de Nokhoi Connect.</p></div><div class="mobile-only"><h1>Disponible solo para PC</h1><p>URL Video es una aplicación para ordenadores con Windows. Visita esta página desde un PC para descargarla e instalarla.</p><p class="note">Software de Nokhoi Connect.</p></div></main></body></html>"""


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
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI(title="URL Video", docs_url=None, redoc_url=None)
PACKAGE = Path(__file__).with_name("URL-Video-para-Windows-v2.zip")

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="URL Video es una aplicación gratuita para Windows que guarda contenido público autorizado directamente en tu ordenador.">
<title>URL Video — Aplicación gratuita para Windows</title>
<style>
:root{color-scheme:dark}body{margin:0;background:#0b1020;color:#edf2ff;font:16px system-ui,-apple-system,"Segoe UI",sans-serif}.box{max-width:820px;margin:8vh auto;padding:42px;background:#121a30;border:1px solid #28365d;border-radius:20px;box-shadow:0 20px 60px #0005}.logo{display:block;width:min(100%,360px);margin:0 auto 24px;border-radius:14px}.free{display:inline-block;margin:0 0 18px;padding:6px 10px;border-radius:999px;background:#153b31;color:#8cf3cd;font-size:13px;font-weight:800;letter-spacing:.04em}h1{margin:0 0 12px;font-size:clamp(30px,6vw,46px);line-height:1.08}h2{margin:40px 0 16px;font-size:24px}p{color:#b9c4db;line-height:1.65}.lead{max-width:680px;font-size:18px}.button{display:block;margin:28px 0 14px;padding:16px;text-align:center;border-radius:11px;background:#765cff;color:#fff;text-decoration:none;font-weight:800;box-shadow:0 8px 24px #765cff55}.button:hover{background:#8b75ff}.benefits{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.benefit{padding:18px;border:1px solid #2b3961;border-radius:13px;background:#0e162a}.benefit strong{display:block;margin-bottom:6px;font-size:16px}.benefit span{color:#aebbd5;font-size:14px;line-height:1.5}.note{font-size:13px;color:#94a3bd}.footer{margin-top:28px}.mobile-only{display:none}@media(max-width:600px){.box{margin:20vh 16px;padding:26px}.desktop-only{display:none}.mobile-only{display:block}.benefits{grid-template-columns:1fr}}
</style></head>
<body><main class="box"><div class="desktop-only"><img class="logo" src="/codex-clipboard-257a04c3-4734-4b04-9daa-a9edc1355c06.jpg" alt="Alien Downloader"><span class="free">100 % GRATIS</span><h1>Descarga vídeos y audio en tu PC</h1><p class="lead">URL Video te permite guardar contenido público autorizado directamente en tu ordenador Windows, sin depender de una web que procese tus enlaces.</p><a class="button" href="/descargar-aplicacion">Descargar aplicación para Windows</a><p class="note">Compatible con Windows · Aplicación gratuita</p><h2>Todo lo que ganas con URL Video</h2><section class="benefits"><article class="benefit"><strong>Gratis y sencillo</strong><span>Descarga la aplicación, pega un enlace y elige el formato que necesitas.</span></article><article class="benefit"><strong>En tu propio PC</strong><span>El proceso se realiza en tu ordenador: esta página no recibe ni conserva tus enlaces.</span></article><article class="benefit"><strong>Vídeo y audio</strong><span>Guarda contenido autorizado como vídeo MP4 o extrae el audio en MP3.</span></article><article class="benefit"><strong>Sin depender del navegador</strong><span>Una aplicación de Windows preparada para usar cuando la necesites.</span></article><article class="benefit"><strong>Fácil de continuar</strong><span>Incluye instrucciones para instalar Python y ponerla en marcha desde el propio PC.</span></article><article class="benefit"><strong>Uso responsable</strong><span>Pensada para tus propios vídeos o para contenido público con autorización.</span></article></section><p class="note footer">La aplicación no funciona con contenido privado, de pago ni protegido por DRM. Úsala solo para contenido propio, público o con permiso.</p><p class="note">Software de Nokhoi Connect.</p></div><div class="mobile-only"><h1>Disponible solo para PC</h1><p>URL Video es una aplicación para ordenadores con Windows. Visita esta página desde un PC para conocer sus ventajas y descargarla.</p><p class="note">Software de Nokhoi Connect.</p></div></main></body></html>"""


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
    return FileResponse(PACKAGE, filename="URL-Video-para-Windows-v2.zip", media_type="application/zip", headers={"Cache-Control": "no-store"})
