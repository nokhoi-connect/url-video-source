import ipaddress
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from starlette.background import BackgroundTask
import yt_dlp

app = FastAPI(title="URL Video", docs_url=None, redoc_url=None)
MAX_FILE_BYTES = 1_000_000_000

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Descarga gratis contenido público autorizado en MP4 o MP3.">
<title>URL Video — Descarga gratuita de contenido autorizado</title>
<style>body{margin:0;background:#0b1020;color:#edf2ff;font:16px system-ui,sans-serif}.box{max-width:720px;margin:10vh auto;padding:38px;background:#121a30;border:1px solid #28365d;border-radius:20px}h1{margin:0 0 8px}.free{display:inline-block;margin:0 0 18px;padding:6px 10px;border-radius:999px;background:#153b31;color:#8cf3cd;font-size:13px;font-weight:700}p{color:#b9c4db;line-height:1.55}form{display:grid;gap:16px;margin-top:28px}input,select,button{font:inherit;border-radius:10px;padding:14px;border:1px solid #34436c;background:#0b1020;color:#fff}button{background:#765cff;border:0;font-weight:700;cursor:pointer}.note{font-size:13px;color:#94a3bd}label{display:grid;gap:7px}a{color:#a99bff}</style></head>
<body><main class="box"><span class="free">100 % GRATIS</span><h1>Descarga vídeos y audio</h1><p>Pega un enlace público y descarga gratis una copia en MP4 o MP3. El archivo se genera temporalmente y se elimina del servidor después de la descarga.</p>
<form method="post" action="/download"><label>URL pública<input name="url" type="url" required placeholder="https://ejemplo.com/video"></label><label>Formato<select name="format"><option value="mp4">Vídeo MP4</option><option value="mp3">Audio MP3</option></select></label><label class="note"><input type="checkbox" name="rights" value="yes" required> Confirmo que el contenido es mío, público o tengo permiso para descargarlo.</label><button type="submit">Descargar gratis</button></form><p class="note">No se admiten contenidos privados, de pago ni protegidos por DRM. Software de Nokhoi Connect.</p></main></body></html>"""

def validate_url(value: str) -> str:
    parsed = urlparse(value.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise HTTPException(400, "Introduce una URL pública válida que empiece por http:// o https://.")
    try:
        address = ipaddress.ip_address(parsed.hostname)
        if address.is_private or address.is_loopback or address.is_link_local or address.is_reserved:
            raise HTTPException(400, "Solo se permiten direcciones web públicas.")
    except ValueError:
        pass
    return parsed.geturl()

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return PAGE

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/download")
def download(url: str = Form(...), format: str = Form("mp4"), rights: str = Form(...)):
    if rights != "yes":
        raise HTTPException(400, "Debes confirmar que tienes derecho a descargar el contenido.")
    if format not in {"mp4", "mp3"}:
        raise HTTPException(400, "Formato no válido.")
    source_url = validate_url(url)
    workdir = Path(tempfile.mkdtemp(prefix="url-video-"))
    template = str(workdir / "%(title).120B.%(ext)s")
    options = {"outtmpl": template, "noplaylist": True, "max_filesize": MAX_FILE_BYTES, "quiet": True, "no_warnings": True, "restrictfilenames": True, "overwrites": True}
    if format == "mp3":
        options.update({"format": "bestaudio/best", "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]})
    else:
        options.update({"format": "bv*+ba/b[ext=mp4]/b", "merge_output_format": "mp4"})
    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.extract_info(source_url, download=True)
        files = [item for item in workdir.iterdir() if item.is_file()]
        if not files:
            raise RuntimeError("No se generó ningún archivo.")
        result = max(files, key=lambda item: item.stat().st_size)
        media_type = "audio/mpeg" if format == "mp3" else "video/mp4"
        return FileResponse(result, media_type=media_type, filename=result.name, background=BackgroundTask(shutil.rmtree, workdir, ignore_errors=True))
    except HTTPException:
        shutil.rmtree(workdir, ignore_errors=True)
        raise
    except Exception as exc:
        shutil.rmtree(workdir, ignore_errors=True)
        raise HTTPException(422, f"No se pudo preparar la descarga: {str(exc)[:250]}")
