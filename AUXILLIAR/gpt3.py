

class Marco:
    def __init__(self):
        self.coordenada_superior = 0
        self.coordenada_inferior = 0
        self.tipo_de_linea = None
        self.color_de_linea = None
        self.color_de_relleno = None

    def mostrarse(self):
        print("Coordenada superior: " + str(self.coordenada_superior))
        print("Coordenada inferior: " + str(self.coordenada_inferior))
        print("Tipo de linea: " + str(self.tipo_de_linea))
        print("Color de linea: " + str(self.color_de_linea))
        print("Color de relleno: " + str(self.color_de_relleno))

    def cambiarPosicion(self, coordenadaSuperior, coordenadaInferior):  # recibe dos parámetros para cambiar la posición del marco 
        self.coordenadaSuperior = coordenadaSuperior  # asignamos los parámetros a los atributos correspondientes 
        self.coordenadaInferior = coordenadaInferior

    def instanciarObjetos(self):  # instanciamos dos objetos de la clase Marco con diferentes atributos 

        marco1 = Marco()  # creamos el objeto marco1 con los valores por defecto que se han definido en el constructor 

        marco2 = Marco()  # creamos el objeto marco2 con los valores por defecto que se han definido en el constructor  

        marco2.tipoDeLinea = 'dashed'  # modificamos algunas propiedades del objeto marco2 para que sea diferente al objeto marco1  

        marco2.colorDeLinea = 'red'  

    return (marco1,marco2)


#############################################################################


class Estudiante:
  def __init__(self):
    self.nombre = None
    self.ci = None
    self.runiv = None
    self.fecha_ingreso = None

  def mostrar_estudiante(self):
    print("Nombre:", self.nombre)
    print("CI:", self.ci)
    print("RUNIV:", self.runiv)
    print("Fecha de ingreso:", self.fecha_ingreso)

    
estudiante1 = Estudiante() 
estudiante2 = Estudiante()


###################################################################


class Materia:
  def __init__(self, nombre_materia = None, codigo_mat = None, semestre = None, nro_inscritos = 0):
    self.nombre_materia = nombre_materia
    self.codigo_mat = codigo_mat
    self.semestre = semestre
    self.nro_inscritos = nro_inscritos

  def mostrarMateria(self):
    print("Nombre de la materia:", self.nombre_materia)
    print("Código de la materia:", self.codigo_mat)
    print("Semestre:", self.semestre)
    print("Número de inscritos:", self.nro_inscritos)

  
#instanciar 2 objetos 
materia1=Materia("Matematicas","MAT-001","Primer Semestre",20) 
materia2=Materia("Fisica","FIS-001","Segundo Semestre",30) 

 #mostrar los objetos creados 
print("Objeto 1") 
materia1.mostrarMateria() 
print() 
print("Objeto 2") 
materia2.mostrarMateria()