from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, matricula: str, n_ruedas: int, n_puertas: int):
        super().__init__(matricula, n_ruedas)
        self.n_puertas = n_puertas

    def imprimir_detalles(self):
        print(f"El coche con matrícula {self.matricula} con {self.n_puertas} puertas hace: {self.tocar_bocina()}")

    def tocar_bocina(self):
        return "meeehh!"