def calcular_nota(n1, n2, n3):
    return (n1*0.3) + (n2*0.3) + (n3*0.4)


n1= float(input("Ingrese la primera nota: "))
n2= float(input("Ingrese la primera nota: "))
n3= float(input("Ingrese la primera nota: "))

notafinal= calcular_nota(n1,n2,n3)
print("Nota final: " , round(notafinal, 4))
