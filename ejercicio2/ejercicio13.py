vercto = []
for i in range(5):
    ingreso = int(input(f'numero {i+1}: '))
    vercto.append(ingreso)
    
dime = len(vercto)
for i in range(dime-1):
    for j in range(dime-1):
        if vercto[j] > vercto[j +1]:
            prue = vercto[j]
            vercto[j] = vercto[j +1]
            vercto[j +1] =prue
            
print('el primero: ', vercto[0])
print('el segundo: ', vercto[1])
print('el ultimo: ', vercto[-1])