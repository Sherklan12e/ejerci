def traidos(pares,impares):
    tercer = []
    for i in pares:
        if i %2==0:
            tercer.append(i)
    for i in impares:
        if i %2!=0:
            tercer.append(i)
            
            
    print('El tercer arreglo es : ' , tercer)
 
n1 = int(input('Ingresa el primer arreglo cuantos elementos quiere?: '))
arreglo1 = []
arreglo2 = []
for i in range(1,n1+1):
    num = int(input(f'Ingrese el valor {i}: '))
    arreglo1.append(num)

n2 = int(input('Ingresa el segundo arreglo cuantos elementos quiere? : '))

for i in range(1,n2 +1):
    num1 = int(input(f'Ingresa el valor {i}: '))
    arreglo2.append(num1)
    
traidos(arreglo2,arreglo1)
        
