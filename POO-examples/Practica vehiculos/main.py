from Vehiculo import Vehiculo
from Coche import Coche
from Moto import Moto
from TipoMoto import TipoMoto
from Grua import Grua
from Camion import Camion

coche_remolcado = Coche("KOL556", 4, 2)
moto_remolcada = Moto("JPC456", 2, TipoMoto.Custom)

vehiculo = Vehiculo("ABC123", 4)
coche = Coche("DEF456", 2, 4)
moto = Moto("ZYX922", 2, TipoMoto.Scooter)
grua = Grua("GHI789", 6, [moto_remolcada, coche_remolcado])
camion = Camion("LNM417", 6, True)

vehiculo.imprimir_detalles()
coche.imprimir_detalles()
moto.imprimir_detalles()
grua.imprimir_detalles()
camion.imprimir_detalles()


