def positivo(nukm):
    return nukm > 0

vector =  []
vecto2 = []
for i in range(1,8+1):
    num = int(input(f'Ingresa el numero {i}: '))
    while not positivo(num):
        print("Por favor ingresar numeros positivos")
        num = int(input(f'Ingresa el numero {i}: '))
    vector.append(num)
    vecto2.append(num)
    
men = len(vecto2)
for i in range(men-1):
    for j in range(men-1):
        if vecto2[j] < vecto2[j + 1]:
            prueba = vecto2[j]
            vecto2[j] = vecto2[j+1]
            vecto2[j+1] = prueba
            
print(f'El vector normal {vector}')
print(f'El vector de forma decresiente {vecto2} ')  
