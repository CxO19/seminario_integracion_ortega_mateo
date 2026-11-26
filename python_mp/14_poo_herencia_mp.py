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

    def muestra_codigo(self):
        print("Codigo:", self.codigo)

vuelo1 = VueloInternacional("AV204", "Madrid")
vuelo2 = VueloInternacional("LA318", "Miami")
vuelo1.mostrar_info()
vuelo2.mostrar_info()
vuelo1.muestra_codigo()
vuelo2.muestra_codigo()