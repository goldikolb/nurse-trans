# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile
import os

app = FastAPI()

# CORS-Einstellungen
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://nurses-trans.netlify.app",  # Ihre aktuelle Netlify-Domain
        "http://localhost:5500",  # Für lokale Entwicklung
        "http://127.0.0.1:5500"   # Für lokale Entwicklung
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

        return {"text": result["text"]}