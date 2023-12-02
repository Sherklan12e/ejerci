vector = []
for i in range(1,8 +1):
    num = int(input(f'Ingresa el numero {i}: '))
    vector.append(num)
    
numero1 = int(input('ingresa el primer numero: '))
numero2 = int(input('Ingreas el segundo numero: '))

if numero1 in vector:
    print('Si perteneze!')
elif numero2 in vector:
    print('Si perteneze!')
else:
    print('No pertenecen!')