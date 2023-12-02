vector = []
suma = 0

for i in range(1, 10 +1):
    compra = int(input(f'Compro {i} : '))
    vector.append(compra)
    suma = compra + suma
    
    
mayor = compra 
for i in vector:
    if i > mayor:
        mayor = i
        
print('mayor compra: ', mayor)
print('monto total a pagar: ', suma)
        