class punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def muestra(self):
        print("Es una prueba")
#p1=punto()
p2=punto(3,7)
p3=punto(14,8)
print("El dato de atributo x es:",p2.x)
print("El dato de atributo x es:",p3.x)
print("El dato de atributo x es:",p3.muestra())
