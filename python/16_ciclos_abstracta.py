from abc import ABC, abstractmethod

class Vuelo(ABC):
    @abstractmethod
    def despegar(self):
        pass


class VueloNacional(Vuelo):
    def despegar(self):
        return "Vuelo nacional despegando hacia Guayaquil"

vuelo = VueloNacional()
print(vuelo.despegar())