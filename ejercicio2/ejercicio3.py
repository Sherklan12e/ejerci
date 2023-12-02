count1 = 0
count2 = 0
for i in range(5):
    numero = int(input('Ingresa el numero: '))
    if numero >0:
        count1 = 1 + count1
    elif numero <0:
        count2 = 1 + count2
print(count1)
print(count2)