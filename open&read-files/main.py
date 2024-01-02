filename = 'file.txt'

try:
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        print(line.rstrip())

except FileNotFoundError:
    print(f"El fichero '{filename}' no existe.")
except Exception as e:
    print(f"Ha surgido un error: {e}")