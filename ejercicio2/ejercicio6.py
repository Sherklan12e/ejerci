vector = []
for i in range(0,3):
    ingreso = float(input(f'el numero {i}'))
    vector.append(ingreso)
    
count = 0
for a in vector:
    if a > 100:
        print('este numero es mayor ', a)
        count = 1 + count
        
print('cantidad de numero mayores a 100 ', count)