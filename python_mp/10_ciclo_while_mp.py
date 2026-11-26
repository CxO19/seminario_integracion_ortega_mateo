carga = 2000
while carga < 10000:
    print("Cargando combustible del vuelo")
    carga += 2000

print("Combustible listo para el vuelo")

while carga > 0:
    print("El vuelo tiene", carga, "litros de combustible")
    carga -= 500

print("El tanque quedo vacio")

print("Continue y Break")
dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Dia 4: Mantenimiento de la aeronave")
        continue
    print("Dia", dia, "vuelo operando normalmente")
    if dia == 8:
        print("Fin del itinerario")
        break

# Ejercicio
puerta = 0
while puerta < 10:
    puerta += 1
    print("Se revisa el abordaje en la puerta normalmente")
    if puerta == 3:
        print("Puerta 3: Omitir puerta cerrada")
        continue
    if puerta == 7:
        print("Puerta 7: Detener busqueda")
        print("Se encontro al pasajero perdido en la puerta:", puerta)
        break