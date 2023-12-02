numero = int(input('Ingresa el numero: '))

if numero <1:
    print('mayoores a  1 ')
else:
    for i in range(1,numero +1):
        cuadrado = i * i
        cubo =   i*i*i
        print(f"{i}    {cuadrado}      {cubo}" )