print("Funciones")
print("Autor: Mateo Ortega")

def despegar():
    print("El piloto revisa los sistemas")
    print("¡Despegue autorizado!")

despegar()

def abordar(pasajero):
    print(pasajero, "realiza el abordaje")

abordar("Mateo")
abordar("Carlos")
abordar("Lucia")

def calcular_costo(precio, boletos):
    total = precio * boletos
    return total

resultado = calcular_costo(4, 26)
print("El costo total del grupo de Mateo Ortega es:", resultado)

resultado = calcular_costo(4, 5000)
print("El costo total del vuelo chárter es:", resultado)

def asignar_clase(nombre, millas):
    if millas >= 9000:
        print(f"Ascenso de {nombre} a clase ejecutiva exitoso")
    else:
        print(f"{nombre} necesita acumular mas millas")

asignar_clase("Mateo Ortega", 5000)
asignar_clase("Sofia", 15000)

nombre_vuelo: str = "AV204"
pasajeros: int = 33
distancia: float = 1.74
vuelo_activo: bool = True

def calcular_combustible(consumo: float, horas: int) -> float:
    return consumo * horas

combustible: float = calcular_combustible(15.5, 2)
print("Combustible calculado:", combustible)