class Color:
    color = "Rojo"
    def __init__(self, nombre):
        self.nombre = nombre
        #Metodo counstructor
        
    def chagecolor(self):
        print("This color is " + self.color)
    
verde = Color()
rosado = Color()
verde.color = "Verde"
rosado.color = "Rosado"
verde.chagecolor()
rosado.chagecolor()