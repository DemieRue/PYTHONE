# Importar Tkinter
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de casa domótica")

# Crear una lista con los nombres de los dispositivos
dispositivos = ["sala", "comedor", "cocina", "baño", "cuarto1", "cuarto2", "cuarto3", "musica", "ventilador", "tv", "fiesta"]

# Crear una lista vacía para guardar los botones
botones = []

# Crear una lista vacía para guardar las variables booleanas
variables = []

# Crear una función que cambie el estado de un botón al pulsarlo
def cambiar_estado(i):
    # Obtener el valor actual de la variable booleana
    valor = variables[i].get()
    # Si es True, cambiarlo a False y cambiar el texto y el color del botón a "off" y "red"
    if valor:
        variables[i].set(False)
        botones[i].config(text="off", bg="red")
    # Si es False, cambiarlo a True y cambiar el texto y el color del botón a "on" y "green"
    else:
        variables[i].set(True)
        botones[i].config(text="on", bg="green")

# Crear una función que encienda todos los botones y cambie las variables a True
def encender_todos():
    for i in range(len(dispositivos)):
        variables[i].set(True)
        botones[i].config(text="on", bg="green")

# Crear una función que apague todos los botones y cambie las variables a False
def apagar_todos():
    for i in range(len(dispositivos)):
        variables[i].set(False)
        botones[i].config(text="off", bg="red")

# Crear una función que cierre la ventana
def cerrar_ventana():
    ventana.destroy()

# Crear un bucle para crear los botones y las variables de cada dispositivo
for i in range(len(dispositivos)):
    # Crear una variable booleana con el valor inicial False
    variable = tk.BooleanVar()
    variable.set(False)
    # Añadir la variable a la lista de variables
    variables.append(variable)
    # Crear un botón con el nombre del dispositivo y que llame a la función cambiar_estado al pulsarlo
    boton = tk.Button(ventana, text="off", command=lambda i=i: cambiar_estado(i))
    # Cambiar el color del botón a rojo
    boton.config(bg="red")
    # Añadir el botón a la lista de botones
    botones.append(boton)
    # Colocar el botón en la ventana usando grid
    boton.grid(row=i//4, column=i%4*2)

# Crear un botón para encender todos los dispositivos y colocarlo en la ventana
boton_encender = tk.Button(ventana, text="Encender todos", command=encender_todos)
boton_encender.grid(row=3, column=0, columnspan=2)

# Crear un botón para apagar todos los dispositivos y colocarlo en la ventana
boton_apagar = tk.Button(ventana, text="Apagar todos", command=apagar_todos)
boton_apagar.grid(row=3, column=2, columnspan=2)

# Crear un botón para cerrar la ventana y colocarlo en la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar ventana", command=cerrar_ventana)
boton_cerrar.grid(row=3, column=4, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()