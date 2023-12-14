def mayor(year1 , year2):
    mayor = year1 
    if year2 > mayor:
        mayor = year2
        print('EL year two')
    elif mayor > year2:
        print('El year one')
    else:
        print('Los dos son iguales')
    
    return mayor

finwhile = True
ano = 1
count = 0
count2 = 0
suma = 0
suma2 = 0
suma3 = 0
while True == finwhile:
    count = count + 1
    count2 = count2 + 1
    mes = int(input(f'Ingresa la temperatura del mes {count} del año {ano}: '))
    
    suma = suma + mes
    if ano==2:
        suma3 = suma3 + mes
    if count==12:
        count = 0
        ano = ano + 1
        suma2 = suma
       
    if count2==24:
        finwhile = False
        
promedio1 = suma2 / 12
promedio2 = suma3 / 12
print(suma2)
print(suma3)
print('El promedio del year one: ', promedio1)
print('El promedio del year two: ', promedio2)
print('El year con mayor temperatura promedio es :', mayor(promedio1,promedio2))