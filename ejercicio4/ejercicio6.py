# Se ingresa pares de números enteros y la carga finaliza cuando los dos números de
# un par sean cero. Determinar el número de orden de ingreso del par donde la suma
# # de sus componentes sea la mayor, utilizar una función para realizar las sumas.



def suma(num1,num2):
    return num1 + num2
finwhile = True
mayor= 0
count = 0

while True == finwhile:
    count = count + 1
    print('=========================')
    print(f'El ingreso {count}')
    num1 = int(input('Ingresa el primer numero par: '))
    num2 = int(input('Ingresa el segundo numero par: '))
    print('========================')
    
    if suma(num1,num2) > mayor:
        mayor= suma(num1,num2)
        ingreso = count
    
    if num1 ==0 and num2 == 0:
        finwhile = False
        
print('El mayor de ingreso des en e;: ', ingreso)
print('Que la suma mayor es C: ', mayor)