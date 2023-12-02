vector = []
for i in range(2):
    edad = int(input(f'edad de la persona {1 + i}: '))
    vector.append(edad)
mayor = edad
igual = edad
    
if vector[0] > vector[1]:
    mayor = vector[0]
    print(' la edad mayor es: ', mayor)
    
elif vector[1] > vector[0]:
    mayor = vector[1]
    print(' la edad mayor es: ', mayor)
else:
    print('Los dos son iguales')
       
