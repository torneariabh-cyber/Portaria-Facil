import os
import cv2
import time
import base64
import sqlite3
import threading
import re

from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from pydantic import BaseModel, Field

load_dotenv()

IP = os.getenv("DVR_IP", "200.3.196.212")
PORTA = os.getenv("DVR_PORT", "8016")
USUARIO = os.getenv("DVR_USER", "")
SENHA = os.getenv("DVR_PASSWORD", "")
CANAIS = [
    int(c.strip())
    for c in os.getenv("DVR_CHANNELS", "1,2,3,4").split(",")
]
SUBTYPE = os.getenv("DVR_SUBTYPE", "1")

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EVENT_IMAGE_DIR = DATA_DIR / "event_images"
DB_PATH = DATA_DIR / "acess_port_ia.db"
DATA_DIR.mkdir(exist_ok=True)
EVENT_IMAGE_DIR.mkdir(exist_ok=True)

# Regra definida para o condomínio:
# Canal 2 = entrada; canais 1, 3 e 4 = saída.
DIRECAO_POR_CANAL = {2: "ENTRADA", 1: "SAÍDA", 3: "SAÍDA", 4: "SAÍDA"}

app = FastAPI(
    title="ACESS PORT IA",
    description="Monitoramento e registro de eventos veiculares",
    version="1.1.0"
)

# Permite que o painel publicado no GitHub Pages consulte esta API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://torneariabh-cyber.github.io",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

cameras = {}
threads = {}
lock = threading.Lock()
db_lock = threading.Lock()


class VehicleEventIn(BaseModel):
    channel: int = Field(ge=1, le=4)
    plate: str | None = Field(default=None, max_length=12)
    vehicle_type: str | None = Field(default=None, max_length=40)
    color: str | None = Field(default=None, max_length=40)
    confidence: float | None = Field(default=None, ge=0, le=1)
    image_base64: str | None = None


def db_connect():
    connection = sqlite3.connect(DB_PATH, timeout=15)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    with db_lock:
        with db_connect() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS vehicle_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plate TEXT,
                    vehicle_type TEXT,
                    color TEXT,
                    channel INTEGER NOT NULL,
                    direction TEXT NOT NULL,
                    confidence REAL,
                    image_file TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            connection.commit()


def normalize_plate(value):
    if not value:
        return None
    plate = re.sub(r"[^A-Za-z0-9]", "", value).upper()
    return plate[:8] or None


def save_event_image(event_id, image_base64):
    if not image_base64:
        return None
    # Aceita data URL ou somente o conteúdo Base64.
    payload = image_base64.split(",", 1)[-1]
    try:
        raw = base64.b64decode(payload, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Imagem Base64 inválida")
    if len(raw) > 5 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Imagem excede 5 MB")
    filename = f"evento_{event_id}.jpg"
    target = EVENT_IMAGE_DIR / filename
    target.write_bytes(raw)
    return filename


@app.on_event("startup")
def startup():
    init_database()
    iniciar_cameras()


def endereco_rtsp(canal):
    usuario_seguro = quote(USUARIO, safe="")
    senha_segura = quote(SENHA, safe="")
    return (
        f"rtsp://{usuario_seguro}:{senha_segura}@{IP}:{PORTA}"
        f"/cam/realmonitor?channel={canal}&subtype={SUBTYPE}"
    )


def inicializar_camera(canal):
    with lock:
        cameras[canal] = {
            "online": False,
            "frame": None,
            "ultima_atualizacao": None,
            "erro": None
        }


def capturar_camera(canal):
    inicializar_camera(canal)
    while True:
        captura = None
        try:
            captura = cv2.VideoCapture(endereco_rtsp(canal), cv2.CAP_FFMPEG)
            captura.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 10000)
            captura.set(cv2.CAP_PROP_READ_TIMEOUT_MSEC, 10000)
            if not captura.isOpened():
                raise RuntimeError("Não foi possível abrir o fluxo RTSP")
            while True:
                sucesso, frame = captura.read()
                if not sucesso or frame is None:
                    raise RuntimeError("Falha ao receber imagem")
                with lock:
                    cameras[canal].update({
                        "online": True,
                        "frame": frame,
                        "ultima_atualizacao": datetime.now().isoformat(),
                        "erro": None
                    })
        except Exception as erro:
            with lock:
                cameras[canal].update({"online": False, "erro": str(erro)})
        finally:
            if captura is not None:
                captura.release()
        time.sleep(3)


def iniciar_cameras():
    for canal in CANAIS:
        if canal not in threads:
            thread = threading.Thread(
                target=capturar_camera, args=(canal,), daemon=True
            )
            threads[canal] = thread
            thread.start()


@app.get("/")
def inicio():
    return {
        "sistema": "ACESS PORT IA",
        "status": "online",
        "horario": datetime.now().isoformat()
    }


@app.get("/api/v1/health")
def health():
    return {
        "status": "operacional",
        "servidor": "local",
        "sistema": "ACESS PORT IA",
        "eventos": "habilitados"
    }


@app.get("/api/v1/cameras")
def listar_cameras():
    resultado = []
    with lock:
        for canal in CANAIS:
            dados = cameras.get(canal, {})
            resultado.append({
                "canal": canal,
                "status": "ONLINE" if dados.get("online") else "OFFLINE",
                "ultima_atualizacao": dados.get("ultima_atualizacao"),
                "erro": dados.get("erro")
            })
    return {"total": len(resultado), "cameras": resultado}


@app.get("/api/v1/events")
def listar_eventos(limit: int = 30):
    limit = max(1, min(limit, 200))
    with db_lock:
        with db_connect() as connection:
            rows = connection.execute(
                "SELECT * FROM vehicle_events ORDER BY id DESC LIMIT ?",
                (limit,)
            ).fetchall()
    return {
        "total": len(rows),
        "events": [
            {
                "id": row["id"],
                "plate": row["plate"],
                "vehicle_type": row["vehicle_type"],
                "color": row["color"],
                "channel": row["channel"],
                "direction": row["direction"],
                "confidence": row["confidence"],
                "created_at": row["created_at"],
                "image_url": (
                    f"/api/v1/events/{row['id']}/image"
                    if row["image_file"] else None
                ),
            }
            for row in rows
        ]
    }


@app.post("/api/v1/events", status_code=201)
def criar_evento(event: VehicleEventIn):
    if event.channel not in DIRECAO_POR_CANAL:
        raise HTTPException(status_code=400, detail="Canal sem direção configurada")

    plate = normalize_plate(event.plate)
    direction = DIRECAO_POR_CANAL[event.channel]
    created_at = datetime.now().astimezone().isoformat(timespec="seconds")

    with db_lock:
        with db_connect() as connection:
            cursor = connection.execute(
                """INSERT INTO vehicle_events
                   (plate, vehicle_type, color, channel, direction,
                    confidence, image_file, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, NULL, ?)""",
                (
                    plate,
                    event.vehicle_type.strip() if event.vehicle_type else None,
                    event.color.strip() if event.color else None,
                    event.channel,
                    direction,
                    event.confidence,
                    created_at,
                )
            )
            event_id = cursor.lastrowid
            image_file = save_event_image(event_id, event.image_base64)
            if image_file:
                connection.execute(
                    "UPDATE vehicle_events SET image_file = ? WHERE id = ?",
                    (image_file, event_id)
                )
            connection.commit()

    return {
        "id": event_id,
        "plate": plate,
        "channel": event.channel,
        "direction": direction,
        "created_at": created_at,
        "status": "registrado"
    }


@app.get("/api/v1/events/{event_id}/image")
def obter_imagem_evento(event_id: int):
    with db_lock:
        with db_connect() as connection:
            row = connection.execute(
                "SELECT image_file FROM vehicle_events WHERE id = ?",
                (event_id,)
            ).fetchone()
    if not row or not row["image_file"]:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    path = EVENT_IMAGE_DIR / row["image_file"]
    if not path.exists():
        raise HTTPException(status_code=404, detail="Arquivo de imagem não encontrado")
    return FileResponse(path, media_type="image/jpeg")


def gerar_video(canal):
    while True:
        with lock:
            dados = cameras.get(canal)
            frame = (
                dados["frame"].copy()
                if dados and dados.get("frame") is not None else None
            )
        if frame is None:
            time.sleep(0.2)
            continue
        sucesso, buffer = cv2.imencode(
            ".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 75]
        )
        if sucesso:
            yield (
                b"--frame\r\nContent-Type: image/jpeg\r\n\r\n"
                + buffer.tobytes() + b"\r\n"
            )


@app.get("/api/v1/cameras/{canal}/stream")
def transmitir_camera(canal: int):
    if canal not in CANAIS:
        raise HTTPException(status_code=404, detail="Câmera não encontrada")
    return StreamingResponse(
        gerar_video(canal),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
