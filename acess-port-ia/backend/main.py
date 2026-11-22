
import os
import cv2
import time
import threading

from datetime import datetime
from urllib.parse import quote

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

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

app = FastAPI(
    title="ACESS PORT IA",
    description="Sistema de inteligência artificial e monitoramento condominial",
    version="1.0.0"
)

cameras = {}
threads = {}
lock = threading.Lock()


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
            captura = cv2.VideoCapture(
                endereco_rtsp(canal),
                cv2.CAP_FFMPEG
            )

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
                cameras[canal].update({
                    "online": False,
                    "erro": str(erro)
                })

        finally:
            if captura is not None:
                captura.release()

        time.sleep(3)


@app.on_event("startup")
def iniciar_cameras():
    for canal in CANAIS:
        if canal not in threads:
            thread = threading.Thread(
                target=capturar_camera,
                args=(canal,),
                daemon=True
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
        "sistema": "ACESS PORT IA"
    }


@app.get("/api/v1/cameras")
def listar_cameras():
    resultado = []

    with lock:
        for canal in CANAIS:
            dados = cameras.get(canal, {})

            resultado.append({
                "canal": canal,
                "status": (
                    "ONLINE" if dados.get("online")
                    else "OFFLINE"
                ),
                "ultima_atualizacao": dados.get(
                    "ultima_atualizacao"
                ),
                "erro": dados.get("erro")
            })

    return {
        "total": len(resultado),
        "cameras": resultado
    }


def gerar_video(canal):
    while True:
        with lock:
            dados = cameras.get(canal)

            frame = (
                dados["frame"].copy()
                if dados and dados.get("frame") is not None
                else None
            )

        if frame is None:
            time.sleep(0.2)
            continue

        sucesso, buffer = cv2.imencode(
            ".jpg",
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 75]
        )

        if sucesso:
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + buffer.tobytes()
                + b"\r\n"
            )


@app.get("/api/v1/cameras/{canal}/stream")
def transmitir_camera(canal: int):
    if canal not in CANAIS:
        raise HTTPException(
            status_code=404,
            detail="Câmera não encontrada"
        )

    return StreamingResponse(
        gerar_video(canal),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
