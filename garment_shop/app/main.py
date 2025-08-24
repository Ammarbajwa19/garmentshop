from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Garment Shop")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Garment Shop API</h1><p>Status: OK</p>"