from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="ACESS PORT IA API",
    version="0.1.0",
    description="API inicial da plataforma ACESS PORT IA.",
)

# Desenvolvimento local. Em produção, restringir aos domínios autorizados.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

CAMERAS = [
    {"id": f"camera-{channel}", "name": f"Câmera {channel:02d}", "channel": channel,
     "source": "DVR Intelbras", "status": "pending"}
    for channel in range(1, 5)
]


class EventIn(BaseModel):
    event_type: str
    camera_id: str | None = None
    occurred_at: datetime | None = None
    description: str | None = None
    metadata: dict[str, Any] = {}


class VehicleIn(BaseModel):
    plate: str
    vehicle_type: str | None = None
    color: str | None = None
    observed_at: datetime | None = None


@app.get("/api/v1/health")
def health():
    return {
        "status": "ok",
        "service": "acess-port-ia-api",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/v1/cameras")
def cameras():
    return {"items": CAMERAS, "count": len(CAMERAS)}


@app.get("/api/v1/events")
def events():
    return {"items": [], "count": 0, "message": "Nenhum evento recebido ainda."}


@app.get("/api/v1/vehicles")
def vehicles():
    return {"items": [], "count": 0, "message": "Nenhum veículo registrado ainda."}


@app.post("/api/v1/events", status_code=202)
def receive_event(event: EventIn):
    # Persistência será adicionada na etapa de banco de dados.
    return {
        "accepted": True,
        "persisted": False,
        "message": "Evento recebido pela API; armazenamento ainda não configurado.",
        "event": event.model_dump(mode="json"),
    }


@app.post("/api/v1/vehicles", status_code=202)
def receive_vehicle(vehicle: VehicleIn):
    # Persistência e OCR serão adicionados nas próximas etapas.
    return {
        "accepted": True,
        "persisted": False,
        "message": "Veículo recebido pela API; armazenamento ainda não configurado.",
        "vehicle": vehicle.model_dump(mode="json"),
    }
