class Vuelo:
    codigo: str
    __pasajeros: int

    def __init__(self, codigo: str, pasajeros: int):
        self.codigo = codigo
        self.__pasajeros = pasajeros

    def mostrar_info(self):
        print("Codigo", self.codigo)
        print("Pasajeros", self.__pasajeros)

vuelo1 = Vuelo("AV204", 90)
vuelo2 = Vuelo("LA318", 60)
vuelo3 = Vuelo("CM562", 100)
vuelo4 = Vuelo("MP001", 50)

vuelo1.mostrar_info()
vuelo2.mostrar_info()
vuelo3.mostrar_info()
vuelo4.mostrar_info()