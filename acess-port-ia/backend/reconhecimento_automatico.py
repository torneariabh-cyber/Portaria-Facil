import os
import re
import cv2
import time
import base64
import threading
import requests
import numpy as np
from urllib.parse import quote
from ultralytics import YOLO
import easyocr

BASE = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE, ".env")


def carregar_env():
    cfg = {}
    with open(ENV_FILE, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip().strip('"').strip("'")
    return cfg


CFG = carregar_env()
IP = CFG["DVR_IP"]
PORT = CFG.get("DVR_PORT", "8016")
USER = quote(CFG["DVR_USER"], safe="")
PASSWORD = quote(CFG["DVR_PASSWORD"], safe="")
CHANNELS = [int(x.strip()) for x in CFG.get("DVR_CHANNELS", "1,2,3,4").split(",")]
SUBTYPE = CFG.get("DVR_SUBTYPE", "0")
API_URL = CFG.get("API_URL", "http://127.0.0.1:8000/api/v1/events")
PLATE_MODEL = os.path.join(BASE, "detector_placas_br.pt")
VEHICLE_MODEL = os.path.join(BASE, "yolo26n.pt")

ANALYSIS_INTERVAL = 1.5
DUPLICATE_SECONDS = 60
MAX_IMAGE_WIDTH = 720

frames = {}
statuses = {}
lock = threading.Lock()
last_sent = {}
cv2.setNumThreads(1)


def rtsp_url(channel):
    return (f"rtsp://{USER}:{PASSWORD}@{IP}:{PORT}"
            f"/cam/realmonitor?channel={channel}&subtype={SUBTYPE}")


def capture_camera(channel):
    while True:
        cap = None
        try:
            cap = cv2.VideoCapture(rtsp_url(channel), cv2.CAP_FFMPEG)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            if not cap.isOpened():
                raise RuntimeError("Não foi possível abrir o RTSP")
            print(f"[CÂMERA {channel}] Conectada")
            while True:
                ok, frame = cap.read()
                if not ok or frame is None:
                    raise RuntimeError("Fluxo RTSP interrompido")
                with lock:
                    frames[channel] = (frame, time.time())
                    statuses[channel] = "ONLINE"
        except Exception as exc:
            with lock:
                statuses[channel] = "RECONECTANDO"
            print(f"[CÂMERA {channel}] {exc}")
        finally:
            if cap is not None:
                cap.release()
        time.sleep(3)


def class_name(model, class_id):
    names = model.names
    return str(names.get(class_id, class_id) if isinstance(names, dict) else names[class_id]).lower()


def vehicle_boxes(frame, model):
    result = model.predict(frame, imgsz=416, conf=0.30, device="cpu", verbose=False)[0]
    found = []
    if result.boxes is None:
        return found
    allowed = {"car", "motorcycle", "motorbike", "truck", "bus"}
    for box in result.boxes:
        cls = int(box.cls[0])
        name = class_name(model, cls)
        if name not in allowed:
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        found.append({"box": (x1, y1, x2, y2), "name": name,
                      "confidence": float(box.conf[0])})
    return found


def find_vehicle_for_plate(plate_box, vehicles):
    px1, py1, px2, py2 = plate_box
    cx, cy = (px1 + px2) / 2, (py1 + py2) / 2
    containing = []
    for item in vehicles:
        x1, y1, x2, y2 = item["box"]
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            area = max(1, (x2 - x1) * (y2 - y1))
            containing.append((area, item))
    if containing:
        return min(containing, key=lambda x: x[0])[1]
    return None


def vehicle_type(name):
    if name in ("motorcycle", "motorbike"):
        return "Motocicleta"
    if name == "car":
        return "Carro"
    if name in ("truck", "bus"):
        return "Outro veículo"
    return "Não identificado"


def estimate_color(image):
    if image is None or image.size == 0:
        return "Não identificada"
    h, w = image.shape[:2]
    # Usa a região central, evitando bordas e vidro quando possível.
    crop = image[int(h * 0.25):int(h * 0.85), int(w * 0.15):int(w * 0.85)]
    if crop.size == 0:
        crop = image
    small = cv2.resize(crop, (80, 80), interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    hue = hsv[:, :, 0].astype(np.float32)
    sat = hsv[:, :, 1].astype(np.float32)
    val = hsv[:, :, 2].astype(np.float32)
    # Ignora pixels muito escuros ou muito claros extremos para a cor dominante.
    valid = (val > 35) & (val < 245)
    if np.count_nonzero(valid) < 100:
        return "Preta" if float(np.mean(val)) < 75 else "Branca"
    mean_sat = float(np.mean(sat[valid]))
    mean_val = float(np.mean(val[valid]))
    if mean_sat < 35:
        if mean_val > 175:
            return "Branca"
        if mean_val < 75:
            return "Preta"
        return "Prata/Cinza"
    hh = float(np.median(hue[valid]))
    if hh < 10 or hh >= 170:
        return "Vermelha"
    if hh < 22:
        return "Laranja"
    if hh < 36:
        return "Amarela"
    if hh < 90:
        return "Verde"
    if hh < 130:
        return "Azul"
    if hh < 160:
        return "Roxa"
    return "Vermelha"


def encode_vehicle_image(frame, vehicle):
    h, w = frame.shape[:2]
    if vehicle:
        x1, y1, x2, y2 = vehicle["box"]
        pad_x = int((x2 - x1) * 0.06)
        pad_y = int((y2 - y1) * 0.06)
        x1, y1 = max(0, x1 - pad_x), max(0, y1 - pad_y)
        x2, y2 = min(w, x2 + pad_x), min(h, y2 + pad_y)
        crop = frame[y1:y2, x1:x2]
    else:
        crop = frame
    if crop is None or crop.size == 0:
        return None, None
    ch, cw = crop.shape[:2]
    if cw > MAX_IMAGE_WIDTH:
        nh = max(1, int(ch * MAX_IMAGE_WIDTH / cw))
        crop = cv2.resize(crop, (MAX_IMAGE_WIDTH, nh), interpolation=cv2.INTER_AREA)
    ok, encoded = cv2.imencode(".jpg", crop, [cv2.IMWRITE_JPEG_QUALITY, 78])
    if not ok:
        return None, crop
    return base64.b64encode(encoded.tobytes()).decode("ascii"), crop


def send_event(channel, plate, ocr_confidence, frame, vehicle):
    now = time.time()
    key = (channel, plate)
    if now - last_sent.get(key, 0) < DUPLICATE_SECONDS:
        return

    image_b64, vehicle_image = encode_vehicle_image(frame, vehicle)
    vtype = vehicle_type(vehicle["name"]) if vehicle else "Não identificado"
    color = estimate_color(vehicle_image) if vehicle_image is not None else "Não identificada"
    payload = {
        "channel": channel,
        "plate": plate,
        "vehicle_type": vtype,
        "color": color,
        "confidence": round(float(ocr_confidence), 4),
        "image_base64": image_b64,
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=15)
        response.raise_for_status()
        last_sent[key] = now
        data = response.json()
        print(f"[REGISTRADO] {plate} | CÂMERA {channel} | {data.get('direction')} | {vtype} | {color} | OCR {ocr_confidence:.0%}")
    except Exception as exc:
        print(f"[API] Falha ao registrar {plate}: {exc}")


def analyze_frame(channel, frame, plate_model, vehicle_model, reader):
    vehicles = vehicle_boxes(frame, vehicle_model)
    result = plate_model.predict(frame, imgsz=640, conf=0.20, device="cpu", verbose=False)[0]
    if result.boxes is None:
        return
    h, w = frame.shape[:2]
    boxes = sorted(result.boxes, key=lambda b: float(b.conf[0]), reverse=True)
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        mx, my = int((x2 - x1) * 0.10), int((y2 - y1) * 0.15)
        x1, y1 = max(0, x1 - mx), max(0, y1 - my)
        x2, y2 = min(w, x2 + mx), min(h, y2 + my)
        plate_crop = frame[y1:y2, x1:x2]
        if plate_crop.size == 0:
            continue
        readings = reader.readtext(plate_crop, detail=1,
                                   allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        if not readings:
            continue
        best = max(readings, key=lambda x: x[2])
        plate = re.sub(r"[^A-Z0-9]", "", best[1].upper())
        if len(plate) != 7:
            continue
        vehicle = find_vehicle_for_plate((x1, y1, x2, y2), vehicles)
        send_event(channel, plate, float(best[2]), frame, vehicle)


def main():
    print("=" * 58)
    print("ACESS PORT IA - RECONHECIMENTO MULTICÂMERA")
    print("Canais: " + ", ".join(map(str, CHANNELS)))
    print("Canal 2 = ENTRADA | Canais 1, 3 e 4 = SAÍDA")
    print("=" * 58)
    print("Carregando detector de placas...")
    plate_model = YOLO(PLATE_MODEL)
    print("Carregando detector de veículos...")
    vehicle_model = YOLO(VEHICLE_MODEL)
    print("Carregando OCR...")
    reader = easyocr.Reader(["pt", "en"], gpu=False)

    for channel in CHANNELS:
        threading.Thread(target=capture_camera, args=(channel,), daemon=True).start()
    print("IA iniciada. Análise compartilhada; CTRL+C encerra.")

    last_analysis = {c: 0 for c in CHANNELS}
    try:
        while True:
            for channel in CHANNELS:
                with lock:
                    item = frames.get(channel)
                if not item:
                    continue
                frame, received = item
                if time.time() - received > 5 or time.time() - last_analysis[channel] < ANALYSIS_INTERVAL:
                    continue
                last_analysis[channel] = time.time()
                try:
                    analyze_frame(channel, frame.copy(), plate_model, vehicle_model, reader)
                except Exception as exc:
                    print(f"[ANÁLISE CÂMERA {channel}] {exc}")
                time.sleep(0.05)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nReconhecimento encerrado.")


if __name__ == "__main__":
    main()
