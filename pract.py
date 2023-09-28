print("""
  1: tarta:
  2: mostaza:
  3: cofe:
  """)

def tarta():
    print(""" 
          Tarta
    1: lorem
    2: lorem
    3: lorem      
    """)
    poner = int(input("Ingres lo que quiere: "))
    el = 0
    for i in poner:
        el = el + i 
    return i
def mostaza():
    print(""" 
          Tarta
    1: lorem
    2: lorem
    3: lorem      
           
        """)
def cofe():
    print(""" 
          Tarta
    1: lorem
    2: lorem
    3: lorem   """)
estado = True
while estado == True:
    poner = input("Ingrese lo que quiere: ")
    if poner == "tarta":
        tarta()
    elif poner == "mostaza":
        mostaza()
    elif poner == "cofe":
        cofe()
    else:
        estado == False
    