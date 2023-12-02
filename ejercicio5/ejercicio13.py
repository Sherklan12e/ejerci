def validar(num):
    return num >= 0 and num<=9

vector =[]
for i in range(1,8+1):
    num = int(input(f'x {i}: '))
    while not validar(num):
        print('Por favor solo numeros de 0 a 9')
        num = int(input(f'x {i}: '))
    vector.append(num)

if vector == vector[::-1]:
    print('Es capicua')
else:
    print('No es capicua')