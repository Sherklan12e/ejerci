vector = []
vector2 = []
suma = 0
for i in range(1,10+1):
    tiempo = int(input(f'Tiempo del corredor {i}: '))
    vector.append(tiempo)
    vector2.append(tiempo)
    suma = tiempo + suma
promedio = suma / len(vector)
meno = len(vector)
for i in range( meno-1):
    for j in range(meno-1):
        if vector[j] > vector[j+1]:
            prueba = vector[j]
            vector[j]= vector[j+1]
            vector[j+1] = prueba

print(f'El corredor que fue primero es: {vector2.index(vector[0])+ 1}')
print(f'El corredor que fue segundo es: {vector2.index(vector[1]) +1}')
print(f'El corredor que fue ultimo es: {vector2.index(vector[-1]) +1}')
print(f'El tiempor promedio de la carrera es: {promedio}')