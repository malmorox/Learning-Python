import random
import time

def año2024(conocimiento = 0):

    rendirse = False
    estado = ["Qué bueno/a soy! O",
            "Burnout Y", "La IA es mejor que yo $8",
            "Síndrome del impostor GQ", "No sé nada O",
            "Quiero dejarlo GQ", "Tengo que intentarlo O "]

    for dia in range(1, 366):

        print(f"Día (día) de 2024")

        print(random.choice(estado))

        # Este código nunca va a ejecutarse

        if rendirse: raise Exception()

        if dia == 365: print("No subir a producción")

        time.sleep(60 * 60 * 24)

        conocimiento += 1

    print(f"Eres un {conocimiento}% mejor")
    print("FELIZ 2024, DEVELOPERS! HB")
    año2024(conocimiento)
