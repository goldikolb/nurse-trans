# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import whisper
import tempfile
import os

app = FastAPI()

@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Whisper-Modell laden (tiny für schnelleres Laden und weniger Speicherverbrauch)
model = whisper.load_model("tiny")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Temporäre Datei erstellen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        # Audio-Datei speichern
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()

        # Transkription durchführen
        result = model.transcribe(temp_file.name)

        # Temporäre Datei löschen
        os.unlink(temp_file.name)

        return JSONResponse(
            content={"text": result["text"]},
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "*"
            }
        )