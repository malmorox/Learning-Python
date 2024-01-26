from Vehiculo import Vehiculo

class Grua(Vehiculo):
    def __init__(self, matricula: str, n_ruedas: int, vehiculos_remolcados: list[Vehiculo] = None):
        super().__init__(matricula, n_ruedas)
        self.vehiculos_remolcados = vehiculos_remolcados or []

    def remolcar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos_remolcados.append(vehiculo)

    def imprimir_detalles(self):
        print(f"La grua con matrícula {self.matricula} hace: {self.tocar_bocina()}")

        if self.vehiculos_remolcados:
            print("Vehículos remolcados:")
            for vehiculo_remolcado in self.vehiculos_remolcados:
                print(f"- Matrícula: {vehiculo_remolcado.matricula} | Número de ruedas: {vehiculo_remolcado.n_ruedas}")

    def tocar_bocina(self):
        return "mooook!"