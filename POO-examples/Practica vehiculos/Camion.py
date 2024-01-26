from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, matricula: str, n_ruedas: int, con_carga: bool):
        super().__init__(matricula, n_ruedas)
        self.con_carga = con_carga

    def imprimir_detalles(self):
        carga_estado = "CON" if self.con_carga else "SIN"
        print(f"El coche con matrícula {self.matricula} y {carga_estado} carga hace: {self.tocar_bocina()}")

    def tocar_bocina(self):
        return "turuuu!"