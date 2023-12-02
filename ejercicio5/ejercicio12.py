vector = []
suma = 0
for i in range(1,25+1):
    num = int(input(f'Nota: {i}'))
    vector.append(num)
    suma = num + suma    

promedio = suma / len(vector)
count=0
count1=0
for i in vector:
    if i < promedio:
        count = 1 +count
    if i > promedio:
        count1 = 1+ count1
        
print(f'Los alumnos con mayor al promedio son: {count1}')
print(f'Los alumnos con menor  al promedio son: {count}')        