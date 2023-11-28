numeros = []
for i in range(4):
    numero = int(input(f'ingrese el numero {i +1}: '))
    numeros.append(numero)
    
for i in range(len(numeros)-1,-1,-1):
    print(numeros[i])