from tkinter import *

# Crear una ventana y un lienzo
window = Tk()
canvas = Canvas(window, width=500, height=200, bg="black")
canvas.pack()

# Crear un texto en el lienzo
text = canvas.create_text(250, 100, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white")

# Crear una variable para la dirección del movimiento
direction = 1

# Crear una función para mover el texto automáticamente
def move_text():
    global direction
    # Obtener las coordenadas actuales del texto
    x1, y1, x2, y2 = canvas.bbox(text)
    # Si el texto llega al borde derecho, cambiar la dirección a izquierda
    if x2 >= 500:
        direction = -1
    # Si el texto llega al borde izquierdo, cambiar la dirección a derecha
    elif x1 <= 0:
        direction = 1
    # Mover el texto según la dirección
    canvas.move(text, direction * 5, 0)
    # Llamar a la función nuevamente después de 50 milisegundos
    canvas.after(50, move_text)

# Llamar a la función por primera vez
move_text()

# Iniciar el bucle principal de la ventana
window.mainloop()