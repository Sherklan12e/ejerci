# Crear un arreglo de enteros de N elementos. Verificar si los elementos se
# encuentran en orden estrictamente creciente. Si los elementos no se encuentran
# en orden estrictamente creciente, imprimir por pantalla la cantidad de veces que
# se rompe ese orden.
# Ejemplo: {1, 3, 5, 2, 4, 6, 8, 8, 9, 10}, el n-umero de veces que se rompe el
# orden es 2.
while True:
        
    try:
        edad  = int(input('Ingrese su edad: '))
        print('Tu edad es : ', edad)
        break
        
    except:
        print('Ingresaste mal')
        
    finally:
        print('La ejecucion a finalizado')