"""
Manejo de Cadena de Caracteres
"""

pasajero1 = "Carlos Ruiz"
print(f"Pasajero 1: {pasajero1}")
print(f"Tipo de datos: {type(pasajero1)}")

pasajero2 = "Maria Gomez"
print(f"Pasajero 2: {pasajero2}")
print(f"Tipo de datos: {type(pasajero2)}")

# Funciones comunes de las variables String

print("Funciones comunes de texto")

codigo_vuelo1 = "VUE-01"
codigo_vuelo2 = "VUE-02"
longitud_vuelo1 = len(codigo_vuelo1)
longitud_vuelo2 = len(codigo_vuelo2)

print("Codigo vuelo 1", codigo_vuelo1)
print("Longitud vuelo 1", longitud_vuelo1)

print("Codigo vuelo 2", codigo_vuelo2)
print("Longitud vuelo 2", longitud_vuelo2)

print("Convertir Mayusculas y Minusculas")
mensaje = "El vuelo se dirige a la ciudad de Quito"

mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()

print("Mensaje Original", mensaje)
print("Mensaje en Mayuscula", mensaje_mayusculas)
print("Mensaje en Minuscula", mensaje_minusculas)

print("Reemplazo de substring")
mensaje = "El avion viajara a Guayaquil"
nuevo_mensaje = mensaje.replace("Guayaquil", "Cuenca")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)

destinos = "Quito,Guayaquil,Cuenca"
print("destinos: ", destinos)
lista_destinos = destinos.split(",")
print(lista_destinos)
print("Primer destino : ", lista_destinos[0])

print("Extraer subcadenas")
mensaje = "Buen viaje y disfrute su vuelo siempre"
adjetivo = mensaje[5:10]
verbo = mensaje[14:22]
print("adjetivo es : ", adjetivo)
print("verbo es : ", verbo)

print("Comprobaciones utiles")
codigo = "VUE101"
numero = "2026"
nombre = "Aerolinea UTE"
identificador = "BOLETO1"

print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())