from fastapi import FastAPI
from app.database import engine

app = FastAPI(title="DocuVault API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DocuVault backend running"}

@app.get("/health")
def health_check():
    try:
        engine.connect()
        return {"status": "healthy", "database": "connected"}
    except Exception:
        return {"status": "unhealthy", "database": "disconnected"}