# Definir las variables
entero = 34
flotante = 34.12

# Función para sumar las dos variables
def suma(a, b):
    return a + b

# Función para restar la primera variable con la segunda
def resta(a, b):
    return a - b

# Función para multiplicar las dos variables
def multiplicacion(a, b):
    return a * b

# Función para dividir la primera variable por la segunda (manejando la división por cero)
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Llamar a las funciones y mostrar los resultados
print(f"Suma: {suma(entero, flotante)}")
print(f"Resta: {resta(entero, flotante)}")
print(f"Multiplicación: {multiplicacion(entero, flotante)}")
print(f"División: {division(entero, flotante)}")
