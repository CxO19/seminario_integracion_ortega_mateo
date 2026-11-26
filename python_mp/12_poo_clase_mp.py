class Vuelo:
    codigo: str
    destino: str

    def __init__(self, codigo: str, destino: str):
        self.codigo = codigo
        self.destino = destino

    def mostrar_info(self):
        print("Codigo", self.codigo)
        print("Destino", self.destino)

vuelo1 = Vuelo("AV204", "Quito")
vuelo2 = Vuelo("LA318", "Guayaquil")
vuelo3 = Vuelo("CM562", "Cuenca")
vuelo4 = Vuelo("MP001", "Madrid")

vuelo1.mostrar_info()
vuelo2.mostrar_info()
vuelo3.mostrar_info()
vuelo4.mostrar_info()