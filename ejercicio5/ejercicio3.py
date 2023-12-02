def entero(num):
    return num > 0
vector = []
for i in range(7):
    num = int(input(f'ingresa el numero {i+1}:' ))
    
    while not entero(num):
        print('Ingrese numeros enteros')
        num = int(input(f'ingresa el numero {i+1}:' ))
    vector.append(num)
    
mayor = num
for i in vector:
    if i > mayor:
        mayor = i
    
order = vector.index(mayor)

print('El numero mayor es, ', mayor)
print('Fue leido en ,', order +1)
print('el vector completo, ', vector)