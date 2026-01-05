from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI(title="DocuVault API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DocuVault backend running"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }