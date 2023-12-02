def positivo(num):
    return num>0
vector = []
for i in range(1,7+1):
    num = int(input('Ingresa el numero: '))
    while not positivo(num):
        print('Por favor ingrese enteros positivos')
        num = int(input('Ingresa el numero: '))
    vector.append(num)
men = len(vector)
for i in range(men-1):
    for j in range(men-1):
        if vector[j] > vector[j+1]:
            prueba = vector[j]
            vector[j]= vector[j+1]
            vector[j+1] = prueba
print(vector)