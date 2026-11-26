from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

reservas_router = APIRouter()


class ReservaCreate(BaseModel):
    """Lo que el cliente envía para crear una reserva. Sin id: lo asigna el servidor."""
    pasajero: str = Field(min_length=3, max_length=100)
    observaciones: str | None = None
    clase: str = "economica"
    servicios: list[str] = Field(default_factory=list)


class ReservaRead(BaseModel):
    """Lo que el servidor expone al leer una reserva. Incluye campos calculados por el servidor."""
    id: int
    pasajero: str
    observaciones: str | None
    clase: str
    servicios: list[str]
    confirmada: bool


class ReservaUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    pasajero: str | None = Field(default=None, min_length=3, max_length=100)
    observaciones: str | None = None
    clase: str | None = None
    servicios: list[str] | None = None
    confirmada: bool | None = None


RESERVAS: list[dict] = [
    {
        "id": 1,
        "pasajero": "Maria Lopez",
        "observaciones": None,
        "clase": "economica",
        "servicios": [],
        "confirmada": False,
    },
    {
        "id": 2,
        "pasajero": "Mateo Ortega",
        "observaciones": None,
        "clase": "ejecutiva",
        "servicios": [],
        "confirmada": False,
    },
]
NEXT_ID = 3



@reservas_router.post("/reservas", response_model=ReservaRead, status_code=201)
def crear_reserva(reserva: ReservaCreate) -> dict:
    global NEXT_ID
    nueva_reserva = {
        "id": NEXT_ID,
        "confirmada": False,
        "notas_internas": "creado desde la API",
        **reserva.model_dump(),
    }
    RESERVAS.append(nueva_reserva)
    NEXT_ID += 1
    return nueva_reserva


@reservas_router.get("/reservas", response_model=list[ReservaRead])
def listar_reservas() -> list[dict]:
    return RESERVAS


@reservas_router.patch("/reservas/{reserva_id}", response_model=ReservaRead)
def actualizar_reserva(reserva_id: int, update: ReservaUpdate) -> dict:
    for reserva in RESERVAS:
        if reserva["id"] == reserva_id:
            cambios = update.model_dump(exclude_unset=True)
            reserva.update(cambios)
            return reserva
    raise HTTPException(status_code=404, detail="Reserva no encontrada")


@reservas_router.post("/reservas/from-model")
def crear_desde_modelo(reserva: ReservaCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = reserva.model_dump()
    nueva_reserva = {"id": len(RESERVAS) + 1, "confirmada": False, **data}
    RESERVAS.append(nueva_reserva)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validada = ReservaRead.model_validate(nueva_reserva)
    return validada.model_dump()


@reservas_router.get("/reservas/{reserva_id}/raw-vs-validated")
def comparar_raw_validado(reserva_id: int) -> dict:
    raw = next((r for r in RESERVAS if r["id"] == reserva_id), None)
    if raw is None:
        return {"error": "no encontrada"}

    # model_validate lanza una excepción si el dict no cumple el schema de ReservaRead
    validada = ReservaRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validada.model_dump(),
        "validated_model_dump_json": validada.model_dump_json(),
    }