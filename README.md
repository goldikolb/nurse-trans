# Nurse Trans

Eine Transkriptions-Anwendung mit Whisper AI

## Frontend

Das Frontend ist eine einfache HTML/JavaScript-Anwendung, die auf Netlify gehostet wird.

## Backend

Das Backend ist eine FastAPI-Anwendung, die auf Render gehostet wird und das Whisper AI-Modell für die Transkription verwendet.

### Lokale Entwicklung

1. Python-Abhängigkeiten installieren:
```bash
cd backend
pip install -r requirements.txt
```

2. Backend starten:
```bash
uvicorn main:app --reload
```

3. Frontend im Browser öffnen:
Öffnen Sie die `index.html` Datei in Ihrem Browser.

## Deployment

- Frontend: Netlify (https://nurse-trans.windsurf.build)
- Backend: Render (URL wird nach dem Deployment aktualisiert)