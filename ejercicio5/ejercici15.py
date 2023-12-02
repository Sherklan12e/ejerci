def compara(uno,dos):
    if uno > dos:
        print('El primer añ0')
    elif uno < dos :
        print('El segundo año')
    else:
        print('son iguales')
    print(f'promedio del primer año {uno}')
    print(f'promedio del segundo año {dos}')
   

vector1 = []
suma1 = 0
vector2 = []
suma2 = 0
for i in range(1,12+1):
    nm = float(input(f'MES {i} del primer año: '))
    vector1.append(nm)
    suma1 = nm + suma1
    
for i in range(1,12+1):
    nmm = float(input(f'Mes {i} del segundo año: '))
    vector2.append(nmm)
    suma2 = nmm + suma2
    
promedio1 =  suma1 / len(vector1)
promedio2 = suma2 / len(vector2)
compara(promedio1,promedio2)
    
