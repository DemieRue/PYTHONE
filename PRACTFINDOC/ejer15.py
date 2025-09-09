# Importar tkinter
import tkinter as tk

# Crear la ventana principal
window = tk.Tk()
window.title("Control de casa domótica")

# Crear una lista de botones con sus nombres y colores
buttons = [
    {"name": "Sala", "color": "green"},
    {"name": "Comedor", "color": "green"},
    {"name": "Cocina", "color": "green"},
    {"name": "Baño", "color": "green"},
    {"name": "Cuarto1", "color": "green"},
    {"name": "Cuarto2", "color": "green"},
    {"name": "Cuarto3", "color": "green"},
    {"name": "Música", "color": "green"},
    {"name": "Ventilador", "color": "green"},
    {"name": "TV", "color": "green"},
    {"name": "Fiesta", "color": "green"}
]

# Crear una función para cambiar el color y el estado de un botón al hacer clic
def toggle(button):
    # Obtener el color y el texto actuales del botón
    color = button.cget("bg")
    text = button.cget("text")
    # Si el color es verde, cambiarlo a rojo y añadir "(off)" al texto
    if color == "green":
        button.config(bg="red", text=text + "(off)")
    # Si el color es rojo, cambiarlo a verde y quitar "(off)" del texto
    elif color == "red":
        button.config(bg="green", text=text.replace("(off)", ""))

# Crear una función para encender todos los botones
def turn_on_all():
    # Recorrer todos los botones de la lista
    for button in buttons:
        # Obtener el widget del botón
        widget = button["widget"]
        # Cambiar el color a verde y quitar "(off)" del texto
        widget.config(bg="green", text=button["name"])

# Crear una función para apagar todos los botones
def turn_off_all():
    # Recorrer todos los botones de la lista
    for button in buttons:
        # Obtener el widget del botón
        widget = button["widget"]
        # Cambiar el color a rojo y añadir "(off)" al texto
        widget.config(bg="red", text=button["name"] + "(off)")

# Crear una función para cerrar la ventana
def close_window():
    window.destroy()

# Crear un marco para los botones de encendido y apagado
frame1 = tk.Frame(window)
frame1.pack()

# Crear un botón para encender todos los botones y añadirlo al marco
button_on = tk.Button(frame1, text="Encender todos", command=turn_on_all)
button_on.pack(side=tk.LEFT)

# Crear un botón para apagar todos los botones y añadirlo al marco
button_off = tk.Button(frame1, text="Apagar todos", command=turn_off_all)
button_off.pack(side=tk.LEFT)

# Crear un marco para los botones de la casa domótica
frame2 = tk.Frame(window)
frame2.pack()

# Recorrer los botones de la lista y crear un widget para cada uno
for button in buttons:
    # Crear un widget de botón con el nombre y el color del botón de la lista
    widget = tk.Button(frame2, text=button["name"], bg=button["color"], command=lambda b=button: toggle(b["widget"]))
    # Añadir el widget al marco con un diseño de cuadrícula
    widget.grid(row=buttons.index(button) // 4, column=buttons.index(button) % 4)
    # Guardar el widget en el diccionario del botón de la lista
    button["widget"] = widget

# Crear un botón para cerrar la ventana y añadirlo a la ventana principal
button_close = tk.Button(window, text="Cerrar ventana", command=close_window)
button_close.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()