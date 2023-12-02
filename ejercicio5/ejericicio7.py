vector = []
for i in range(1,10 +1):
    numero = int(input(f'Ingresa el numero {i}: '))
    vector.append(numero)

maximo = numero
minimo = numero
for i in vector:
    if i > maximo:
        maximo = i
    if i< minimo:
        minimo = i
ocurreciaminima = vector.index(minimo)
ocurrecimaxima = vector.index(maximo)
print(f'El numero maximo es {maximo}, y esta en la ocurrencia {ocurrecimaxima +1}.')
print(f'El numero minimo es {minimo}, y esta en la ocurrencia {ocurreciaminima+1}.')
