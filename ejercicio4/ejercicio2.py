def validar(s):
    return s > 0


nombres = []
vector = []

for i in range(1,3+1):
    nombre = input(f'Ingresa el nombre del Empleado {i}: ')
    sueldo = float(input(f'Ingresa el sueldo del empleado {i}: '))
    while not validar(sueldo):
        print('Ingrese el sueldo arriva de cero')
        sueldo = float(input(f'Ingresa el sueldo del empleado {i}: '))
    nombres.append(nombre)
    vector.append(sueldo)
    
mayor = sueldo
for i in vector:
    if i > mayor:
        mayor = i
    
empleado = vector.index(mayor)

print('El empleado con mayor sueldo es ', empleado + 1)

    