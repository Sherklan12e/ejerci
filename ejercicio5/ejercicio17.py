def arreglos(vector):
    men = len(vector)
    vector2 = []
    for i in vector:
        vector2.append(i)
    for i in range(men-1):
        for j in range(men-1):
            if vector[j] > vector[j+1]:
                prueba = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = prueba
    
    menor = vector2.index(vector[0]) 
    print(vector2)
    print(vector)
    print('El numero menor esta en el elemento: ', menor +1)
    
    
N = int(input('Ingresa cuantos elementos quieres: '))

def numero(n):
    vector = []
    for i in range(1,n+1):
        num = int(input(f'Ingresa el numero del elemento {i}: '))
        vector.append(num)
        
    return vector

vectorr = numero(N)
arreglos(vectorr)
   
    

    
                
    
    