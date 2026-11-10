
from fastapi import FastAPI

app = FastAPI(title="Curso FastAPI + uv")


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "Autor": "Mateo Ortega",
            "version": "0.1.0"}

@app.get("/mateo")
def endpoint_mateo() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno="Mateo Ortega")


@app.get("/ortega", response_model=Mensaje)
def endpoint_ortega():
    return {"texto": "Hola", "prioridad": 5, 
            "campo_interno": "imprime desde endpoint ortega"}


@app.get("/campo_extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola mateo", 
            "prioridad": 5, 
            "campo_interno": "si deberia salir incluido el moddelo", 
            "campo_extra": "no deberia salir"}