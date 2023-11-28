count = 0

for i in range(5):
    numero = int(input(f'ingresa el numero {i + 1}: '))
    count = numero + count
    
    
count = count / 5

print(count)