print("CRUD DE LISTAS EN PYTHON")
reservas = [
    {"id": 1, "pasajero": "Carlos Ruiz", "destino": "Quito", "estado": "Confirmado"},
    {"id": 2, "pasajero": "Maria Gomez", "destino": "Guayaquil", "estado": "Confirmado"},
    {"id": 3, "pasajero": "Juan Perez", "destino": "Cuenca", "estado": "Confirmado"}
]
id_publico = 4
def create():
    global id_publico
    print("Registrar reserva")
    pasajero = input("Nombre pasajero: ")
    destino = input("Destino: ")
    estado = input("Estado (Confirmado, Pendiente, Cancelado): ")
    nueva_reserva = {
        "id": id_publico,
        "pasajero": pasajero,
        "destino": destino,
        "estado": estado
    }
    reservas.append(nueva_reserva)
    id_publico += 1

def read():
    print("Lista de reservas")
    for reserva in reservas:
        print(f"{reserva['id']} pasajero : {reserva['pasajero']}")

def update():
    print("Actualizar reserva")
    id_update = int(input("Id a modificar: "))
    for reserva in reservas:
        if (reserva["id"] == id_update):
            reserva["pasajero"] = input("Nuevo pasajero: ")
            reserva["destino"] = input("Nuevo destino: ")
            reserva["estado"] = input("Nuevo estado: ")
            print("actualizado")

def delete():
    print("Borrar reserva")
    id_update = int(input("Id a borrar: "))
    for reserva in reservas:
        if (reserva["id"] == id_update):
            reservas.remove(reserva)
            print("reserva eliminada")

def menu():
    while True:
        print("Reservas de Vuelos")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option=input("Seleccione 1 al 5: ")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("Ingrese una opcion valida")

menu()