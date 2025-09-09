class Ciudad:
    def __init__(self,nc=None,h=0):
        self.NombreCiudad=nc
        self.nh=h
    def mostrar(self):
        pass
#creacion de 2 objetos
c1=Ciudad("La Paz",18000)
c2=Ciudad("Sucre",1000)
print("La ciudad:",c1.NombreCiudad,"el nro de habitantes es:",c1.nh)
print("La ciudad:",c2.NombreCiudad,"el nro de habitantes es:",c2.nh)
              
    
