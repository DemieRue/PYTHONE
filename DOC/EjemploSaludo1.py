class Saludo:
    mensaje="Bienvenido "   #atributo
    def saludar(self,nombre):
        print(self.mensaje + nombre)
        return
obj1=Saludo()

obj1.saludar("Juan")
