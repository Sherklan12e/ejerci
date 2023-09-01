def calcular_Iva(p):
    IVA = p * 0.19
    return IVA  
precioCompra = float(input("Ingresa el valor de la compra: "))
IVA = calcular_Iva(precioCompra)
