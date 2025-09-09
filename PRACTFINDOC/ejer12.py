# Importar Tkinter
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de casa domótica")

# Crear una lista con los nombres de los dispositivos
dispositivos = ["sala", "comedor", "cocina", "baño", "cuarto1", "cuarto2", "cuarto3", "musica", "ventilador", "tv", "fiesta"]

# Crear una lista vacía para guardar los botones
botones = []

# Crear una lista vacía para guardar las etiquetas
etiquetas = []

# Crear una función que cambie el estado de un botón y su etiqueta
def cambiar_estado(i):
    # Obtener el estado actual del botón
    estado = botones[i]["state"]
    # Si está encendido, apagarlo y cambiar el texto de la etiqueta a "off"
    if estado == "normal":
        botones[i]["state"] = "disabled"
        etiquetas[i]["text"] = "off"
    # Si está apagado, encenderlo y cambiar el texto de la etiqueta a "on"
    else:
        botones[i]["state"] = "normal"
        etiquetas[i]["text"] = "on"

# Crear una función que encienda todos los botones y cambie las etiquetas a "on"
def encender_todos():
    for i in range(len(dispositivos)):
        botones[i]["state"] = "normal"
        etiquetas[i]["text"] = "on"

# Crear una función que apague todos los botones y cambie las etiquetas a "off"
def apagar_todos():
    for i in range(len(dispositivos)):
        botones[i]["state"] = "disabled"
        etiquetas[i]["text"] = "off"

# Crear una función que cierre la ventana
def cerrar_ventana():
    ventana.destroy()

# Crear un bucle para crear los botones y las etiquetas de cada dispositivo
for i in range(len(dispositivos)):
    # Crear un botón con el nombre del dispositivo y que llame a la función cambiar_estado al pulsarlo
    boton = tk.Button(ventana, text=dispositivos[i], command=lambda i=i: cambiar_estado(i))
    # Añadir el botón a la lista de botones
    botones.append(boton)
    # Colocar el botón en la ventana usando grid
    boton.grid(row=i//4, column=i%4*2)
    # Crear una etiqueta con el texto "off" inicialmente
    etiqueta = tk.Label(ventana, text="off")
    # Añadir la etiqueta a la lista de etiquetas
    etiquetas.append(etiqueta)
    # Colocar la etiqueta en la ventana usando grid
    etiqueta.grid(row=i//4, column=i%4*2+1)

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
