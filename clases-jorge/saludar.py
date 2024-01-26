def genUsuario(usuario:str):
    def queDice(palabra:str):
        return usuario + ' dice: ' + palabra
    return queDice

usuario = genUsuario('Jaime')
print(usuario('que te den'))