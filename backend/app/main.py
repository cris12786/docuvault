from fastapi import FastAPI

app = FastAPI(title="DocuVault API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DocuVault backend running"}

