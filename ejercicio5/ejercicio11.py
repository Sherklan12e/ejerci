vector = []
positivos = []
negativos = []
def cero(n):
    return n !=0
for i in range(1,8+1):
    num = int(input(f'Ingrese el numero {i}: '))
    while not cero(num):
        print('INGRESE CUALQUIER NUMERO MENOS EL CERO')
        num = int(input(f'Ingrese el numero {i}: '))
    vector.append(num)
    
    
for i in vector:
    if i >=0:
        positivos.append(i)
    else:
        negativos.append(i)   
    
    
    
    
    
men = len(positivos)
ne = len(negativos)
for i in range(men-1):
    for j in range(men-1):
        if positivos[j] < positivos[j+1]:
            prueba = positivos[j]
            positivos[j] = positivos[j+1]
            positivos[j+1] = prueba
            
for i in range(ne-1):
    for j in range(ne-1):
        if negativos[j] > negativos[j+1]:
            pru = negativos[j]
            negativos[j]= negativos[j+1]
            negativos[j+1] = pru
            
print('Los numeros originales ', vector)
print(f"Los numero de positivos descrecientes {positivos}")
print(f'Los numero negativos crecientes { negativos}')