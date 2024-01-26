from Vehiculo import Vehiculo
from TipoMoto import TipoMoto

class Moto(Vehiculo):
    def __init__(self, matricula: str, n_ruedas: int, tipo: TipoMoto):
        super().__init__(matricula, n_ruedas)
        self.tipo = tipo

    def imprimir_detalles(self):
        print(f"La moto con matrícula {self.matricula} y tipo '{self.tipo.value}' hace: {self.tocar_bocina()}")

    def tocar_bocina(self):
        return "pipiii!"