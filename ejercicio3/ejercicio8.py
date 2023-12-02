vector = []
for i in range(10):
    numero = int(input(f'Escribe un numero {i+1}: '))
    vector.append(numero)
negativo = 1
suma = 0
if 0 in vector:
    print('hay cero, termina')
else:
    for i in vector:
        if i >0:
            suma = i + suma
        elif i <0:
            negativo = negativo * i
            
    print(f'El producto de los negativos es, {negativo}')
    print(f'La suma de todos los positivos es, {suma}')