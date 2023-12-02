# Inicializar variables para las comisiones de cada vendedor
comisiones = [0, 0, 0]

# Definir el porcentaje de comisión
porcentaje_comision = 0.05

while True:
    # Ingresar número de vendedor y monto de la boleta
    numero_vendedor = int(input("Ingrese el número de vendedor (0 para finalizar): "))
    
    # Verificar si se debe finalizar la entrada
    if numero_vendedor == 0:
        break
    
    # Validar el número de vendedor
    if 1 <= numero_vendedor <= 3:
        importe = float(input("Ingrese el importe de la boleta: "))
        
        # Calcular la comisión y acumularla en la lista
        comision = importe * porcentaje_comision
        comisiones[numero_vendedor - 1] += comision
    else:
        print("Número de vendedor no válido. Debe estar entre 1 y 3.")

# Mostrar las comisiones de cada vendedor
for i in range(3):
    print(f"El vendedor {i + 1} ganó en comisión: ${comisiones[i]:.2f}")
