# listas = ["Hola", "como", "Estas"]
# lista_distintas = ["esta" , 2, "caca", "volar"]
# esta = ("comer", "correr", 2)
def validar(charactere):
    estado = False
    vocales = ["a","e","i","o", "u"]
    if charactere in vocales:
        print("Si es una vocal")
        estado = True
    else:
        print("No es una vocal ")
        estado = False
    return estado
    print(vocales)
palabra = input("Escribe el caracter: ")
validar(palabra)