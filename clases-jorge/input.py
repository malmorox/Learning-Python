nombre = input("Introduce tu nombre: ")

if nombre is None or nombre.lstrip(""):
    print("Saludos anonimo!")
else:
    print(f"Hola {nombre}, ¿cómo estás?")