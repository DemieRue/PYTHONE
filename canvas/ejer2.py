from tkinter import *

# Crear una ventana y un lienzo
window = Tk()
canvas = Canvas(window, width=500, height=200, bg="black")
canvas.pack()

# Crear un texto en el lienzo
text = canvas.create_text(250, 100, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white")

# Crear una función para mover el texto
def move_text():
    # Crear una lista con los posibles valores del texto
    values = ["Rodrigo Silva", "Silva Rodrigo", "Silva", "Rodrigo"]
    # Usar un ciclo for para recorrer la lista
    for value in values:
        # Cambiar el texto del lienzo con el valor actual de la lista
        canvas.itemconfig(text, text=value)
        # Actualizar la ventana y esperar un segundo
        window.update()
        window.after(1000)

# Crear un botón para llamar a la función
button = Button(window, text="Mover texto", command=move_text)
button.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()