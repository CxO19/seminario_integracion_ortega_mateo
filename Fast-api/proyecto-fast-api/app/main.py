# app/main.py
from fastapi import FastAPI

app = FastAPI(title="Curso FastAPI + uv")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "Autor": "Mateo Ortega",
            "version": "0.1.0"}