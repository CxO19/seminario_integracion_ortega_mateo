class Vuelo:
    codigo: str
    destino: str

    def __init__(self, codigo: str, destino: str):
        self.codigo = codigo
        self.destino = destino

    def mostrar_info(self):
        print("Codigo", self.codigo)
        print("Destino", self.destino)

class VueloInternacional(Vuelo):
    def __init__(self, codigo: str, destino: str):
        super().__init__(codigo, destino)

    def mostrar_info(self):
        print("Vuelo internacional, codigo:", self.codigo, "Destino:", self.destino)

vuelo1 = VueloInternacional("AV204", "Madrid")
vuelo2 = VueloInternacional("LA318", "Miami")
vuelo1.mostrar_info()
vuelo2.mostrar_info()