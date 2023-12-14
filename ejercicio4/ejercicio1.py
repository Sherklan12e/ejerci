def validar(numero):
    return numero >= -100 and numero <= 100

vector=[]
for i in range(1,4+1):
    numero = int(input(f'Ingresa el numero {i}: '))
    while not validar(numero):
        print('Los numeros deben estar entre -100 y 100 ')
        numero = int(input(f'Ingresa el numero {i}: '))
    vector.append(numero)
count = 0
maximo = numero
minimo = numero    
for i in vector:
    count = count + i
    if i > maximo:
        maximo = i
    if i < minimo:
        minimo = i 

promedio = count / len(vector)

print(f'El minimo: {minimo}')
print(f'El maximo: {maximo}')
print(f'El promedio: {promedio}')   
        
        
        