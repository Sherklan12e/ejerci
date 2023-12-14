# Crear un arreglo de enteros de N elementos. Verificar si los elementos se
# encuentran en orden estrictamente creciente. Si los elementos no se encuentran
# en orden estrictamente creciente, imprimir por pantalla la cantidad de veces que
# se rompe ese orden.
# Ejemplo: {1, 3, 5, 2, 4, 6, 8, 8, 9, 10}, el n-umero de veces que se rompe el
# orden es 2.
def arreglo(N):
    vector = []
    for i in range(1,N+1):
        numero = int(input('Ingrese el numero: '))
        vector.append(numero)
    
    return vector



def verificar(arreglo):
    count = 0
    count2 = 0
    arreglo1 = list(arreglo)
    
    for i in range(len(arreglo) -1):
        for j in range(len(arreglo) -1):
            if arreglo[j] > arreglo[j+1]:
                prueba = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = prueba
                
    for i in arreglo1:
        if arreglo[i] == arreglo1[i]:
            count = count +1
        elif arreglo[i] != arreglo1[i]:
            count2 = arreglo1[i]
            if 
            
            
            
            
            



N =  n = int(input('Ingresa de cuanto va ser tu arreglo: '))
