# Realizar un programa que lea números enteros hasta que se indique      por medio del
# mensaje ¿Continua S/N? que finaliza el ingreso de datos. Obtener la suma de los
# números ingresados.
# Por medio de una función se debe validar el ingreso de opciones definiendo a la
# función de la siguiente manera:
# boolean validaS_N ();
# A la función no le ingresan valores, se lee desde el teclado el carácter y si es
# uno de los correctos retorna un valor que será
# Verdadero si ingresó la letra S
# Falso si ingresó la letra N
# Caso contrario se pide el reingreso del dato hasta que el mismo sea válido.
def finwhille(numero):
    normal = False
    if numero == 'S' or numero == 's':
        normal = True
    if numero == 'N' or numero == 'n':
        normal == False
       
    return normal

def BoleanVS(numero):
    normal = True
    if numero == 'S' or numero == 's' :
        normal = False
    if numero == 'N' or numero == 'n':
        normal = False
    
    return normal   
count = 0
finwhile = True
while True == finwhile:
    num = int(input('Ingres un numero: '))
    confirmar = input('Desea continuar? S o N: ')
    
    while BoleanVS(confirmar)==True:
        print(BoleanVS(confirmar))
        print('ingrese S o N ')
        confirmar = input('Desea continuar? S o N: ')
    count = count+num
    if finwhille(confirmar):
        pass 
    else:
        finwhile = False
        print('Termino el programa ')
        print('La suma es ', count)
    