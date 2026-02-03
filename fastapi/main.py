from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "API de Pagamentos ativa"}
