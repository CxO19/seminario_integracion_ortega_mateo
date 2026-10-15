print("Incluir Datos con Input")
nombre_usuario = input("¿Cual es tu nombre?: ")

print("Hola", nombre_usuario, "!")
print("Bienvenido al sistema de vuelos")
print("Hasta luego " + nombre_usuario)

numero_asientos = int(input("¿cuantos asientos deseas reservar?: "))
total_asientos = numero_asientos + 1
print("Asientos totales: ", total_asientos)

print("CONVERSIONES")
print("=== AEROLINEA UTE ===")
nombre_cliente = input("Nombre del Cliente: ")
precio_boleto = float(input("Precio del Boleto: "))
cantidad_boletos = int(input("CANTIDAD:"))
total_pago = cantidad_boletos * precio_boleto
print("total a pagar (round): ", round(total_pago, 2))
print(f"total a pagar (f): ${total_pago:.2f}")