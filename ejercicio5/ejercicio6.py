vector = []
num = 0
pares = []
impares = []
finwhile = False
while False == finwhile:
    num = 1 + num
    print('Solo puedes ingresar 20 numeros')
    numero = int(input(f'Ingrese el numero {num}: '))
    if numero ==0:
        finwhile = True
    if num ==20:
        finwhile = True
    vector.append(numero)
    
for i in vector:
    if i %2==0:
        pares.append(i)
    else:
        impares.append(i)

print('Los numeros pares son: ', pares)
print('Los numeros impares son: ', impares)