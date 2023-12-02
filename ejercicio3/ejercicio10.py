# Realizar un algoritmo para ingresar la edad de las personas informando si la misma
# es menor a 15 (quince) es un niño, menor a 21 (veintiuno) es joven caso contrario
# es adulto. Repetir el proceso hasta que la edad sea menor o igual a 0 (cero).\
finwhile = True
while True == finwhile:
    edad = int(input('escribe la edad: '))
    if edad < 15:
        print('Eres un niño ')
        finwhile=False
    elif edad < 21:
        print('Eres un joven')
        finwhile = False
    elif edad > 21:
        print(' la edad sea menor o igual a 0 (cero)')