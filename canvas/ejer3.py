from tkinter import *

# Crear una ventana y un lienzo
window = Tk()
canvas = Canvas(window, width=500, height=200, bg="black")
canvas.pack()

# Crear un texto en el lienzo con una etiqueta "texto"
text = canvas.create_text(250, 100, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white", tags="texto")

# Crear una función para mover el texto
def move_text():
    # Crear una lista con los posibles incrementos de x y y
    values = [(5, 0), (-5, 0), (0, 5), (0, -5)]
    # Usar un ciclo for para recorrer la lista
    for value in values:
        # Mover el texto con el incremento actual de x y y
        canvas.move("texto", value[0], value[1])
        # Actualizar la ventana y esperar un segundo
        window.update()
        window.after(1000)

# Crear un botón para llamar a la función
button = Button(window, text="Mover texto", command=move_text)
button.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()