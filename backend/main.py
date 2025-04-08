# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile
import os

app = FastAPI()

# Einfache CORS-Einstellungen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Erlaubt alle Origins
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