def validar(n):
    return n >= 1 and n<= 3
vector =[]
efectivo = 0
credito = 0
debito = 0
for i in range(1,30+1):
    
    venta = int(input(f'Ingresa el precio de la {i}: '))
    print("""
          1)efectivo
          2)targeta credito
          3)targeta debito
          
          """)
    metodo = int(input(f'Elije el metodo de pago de la venta {i}: '))
    while not validar(metodo):
        print('Introduzca solo 1 2 3 no mas numeros ')
        metodo = int(input(f'Elije el metodo de pago de la venta {i}: '))
    if metodo ==1:
        efectivo = venta + efectivo
    elif metodo ==2:
        credito = venta + credito
    elif metodo ==3:
        debito = venta + debito
   
        
total = efectivo + credito+ debito
print('monto total en efectivo: ', efectivo)
print('Monto total en credito ', credito)
print('Monto total en debito: ', debito)
print('Monto total total de todos: ', total)