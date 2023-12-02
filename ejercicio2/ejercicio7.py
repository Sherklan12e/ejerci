vector = []
for i in range(3):
    numero = int(input('Ingresa un numero: '))
    vector.append(numero)
suma = 0
mu = 1
for o in vector:
    mu = o * mu
    suma = o + suma
if  vector[2]>0:       
    print(suma)
else:
    print(mu)