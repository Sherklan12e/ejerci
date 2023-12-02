vector = []
for i in range(4):
    numero = int(input(f'numero {i + 1}: '))
    vector.append(numero)
mayor = numero
menor = numero
for i in vector:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i 
print(menor)
print(mayor)