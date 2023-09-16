def ValidarNro(nro):
    estado = True
    if nro < -100:
        estado = False
    else:
        if nro > 100:
            estado = False
    return estado
sumar = 0
for x in range(1, 5, 1):

    finWhileNumero = False
    while finWhileNumero == False:
        numero = int(input("Ingrese un numero (entero): "))

        if ValidarNro(numero) == False:
            print("El numero ingresado esta por fuera del dominio (-100, +100)")
        else:
            finWhileNumero = True
    
    sumar = sumar + numero

    if x == 1:
        maximo = numero
        minimo = numero
    else:
        if numero > maximo:
            maximo = numero
        
        if numero < minimo:
            minimo = numero

print("El número mayor es: ", maximo)
print("El número menor es: ", minimo)

promedio = sumar / 4
print("El promedio es: ", promedio)

