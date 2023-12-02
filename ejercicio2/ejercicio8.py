# Ingresar por teclado 3 números naturales correspondientes a los lados de un triángulo
lado1 = int(input("Ingrese el primer lado del triángulo (número natural): "))
lado2 = int(input("Ingrese el segundo lado del triángulo (número natural): "))
lado3 = int(input("Ingrese el tercer lado del triángulo (número natural): "))

# Verificar si los números ingresados forman un triángulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Determinar el tipo de triángulo
    if lado1 == lado2 == lado3:
        print("Los lados forman un triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Los lados forman un triángulo isósceles.")
    else:
        print("Los lados forman un triángulo escaleno.")
else:
    print("Los lados ingresados no forman un triángulo.")
