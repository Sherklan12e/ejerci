# Leer un número entero desde el usuario
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es el doble de un número impar
if numero % 2 == 0 and (numero // 2) % 2 != 0:
    print(f"{numero} es el doble de un número impar.")
else:
    print(f"{numero} no es el doble de un número impar.")
