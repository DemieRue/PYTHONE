from tkinter import *

# Crear una ventana y un lienzo
window = Tk()
canvas = Canvas(window, width=500, height=200, bg="black")
canvas.pack()

# Crear un texto en el lienzo
text = canvas.create_text(250, 100, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white")

# Crear una función para iniciar el arrastre del texto
def drag_start(event):
    # Obtener el objeto que se ha clicado
    item = canvas.find_closest(event.x, event.y)
    # Guardar el objeto y las coordenadas iniciales del evento
    canvas.item = item
    canvas.startx = event.x
    canvas.starty = event.y

# Crear una función para mover el texto mientras se arrastra
def drag_move(event):
    # Obtener las coordenadas actuales del evento
    x = event.x
    y = event.y
    # Calcular el desplazamiento respecto a las coordenadas iniciales
    dx = x - canvas.startx
    dy = y - canvas.starty
    # Mover el objeto según el desplazamiento
    canvas.move(canvas.item, dx, dy)
    # Actualizar las coordenadas iniciales del evento
    canvas.startx = x
    canvas.starty = y

# Crear una función para soltar el texto al finalizar el arrastre
def drag_stop(event):
    # Borrar el objeto y las coordenadas iniciales del evento
    canvas.item = None
    canvas.startx = None
    canvas.starty = None

# Asociar el texto a los eventos del mouse
canvas.tag_bind(text, "<Button-1>", drag_start)
canvas.tag_bind(text, "<B1-Motion>", drag_move)
canvas.tag_bind(text, "<ButtonRelease-1>", drag_stop)

# Iniciar el bucle principal de la ventana
window.mainloop()