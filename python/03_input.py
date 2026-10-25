print("Incluir Datos con Input")
nombre = input("¿Cual es tu nombre?: ")

print("Hola", nombre, "!")
print("Bienvenido a Springfield")
print("Hasta luego " + nombre)

Cantidad = int(input("¿cuantas rosquillas hay?: "))
total= Cantidad+2
print("Rosquillas totales: ", total)

print ("CONVERSIONES")
print("=== TIENDA DE APU ===")
nombre_cliente=input("Nombre del Cliente: ")
precio = float(input("Precio de Rosquilla: "))
cantidad = int(input("CANTIDAD:"))
total= cantidad * precio
print("total a pagar (round): ", round(total,2))
print(f"total a pagar (f): ${total:.2f}")