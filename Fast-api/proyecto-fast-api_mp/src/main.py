from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sistema de gestion de vuelos")


class Vuelo(BaseModel):
    destino: str
    asientos: int = 1
    campo_interno: str

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv - Sistema de gestion de vuelos",
            "Autor": "Mateo Ortega",
            "version": "0.1.0"}

@app.get("/mateo")
def endpoint_mateo() -> Vuelo:
    return Vuelo(destino="Quito", campo_interno="Mateo Ortega")


@app.get("/ortega", response_model=Vuelo)
def endpoint_ortega():
    return {"destino": "Guayaquil", "asientos": 5,
            "campo_interno": "imprime desde endpoint ortega"}


@app.get("/campo_extra", response_model=Vuelo)
def endpoint_campo_extra():
    return {"destino": "Cuenca",
            "asientos": 5,
            "campo_interno": "si deberia salir incluido el modelo",
            "campo_extra": "no deberia salir"}