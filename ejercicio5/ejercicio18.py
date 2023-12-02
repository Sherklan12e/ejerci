def positivos(vector):
    count= 0
    count2=0
    for i in vector:
        if i >=0:
            count = 1 +count
        else:
            count2= 1+ count2
        
    if count2==0:
        print('Todos son Positivos')
    else:
        print('NO Todos son Postivos')
            
            
N = int(input('Ingresa cuantos elementos quieres: '))
def arreglo(n):
    vector = []
    for i in range(1,n+1):
        num = int(input(f'Ingresa el valor del elemento {i}: '))
        vector.append(num)
        
    return vector


vector = arreglo(N)
positivos(vector)