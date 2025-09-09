import tkinter as tk

def move_text():
    # Obtener las coordenadas actuales del texto
    x, y = canvas.coords(text_id)
    
    # Mover el texto en un ciclo for
    for i in range(1, 11):
        canvas.move(text_id, i, 0)
        canvas.update()  # Actualizar el lienzo para mostrar el movimiento
        canvas.after(100)  # Pausa de 100 milisegundos entre cada movimiento
    
    # Mover el texto de regreso a la posición original
    for i in range(1, 11):
        canvas.move(text_id, -i, 0)
        canvas.update()
        canvas.after(100)
    

# Crear la ventana principal
root = tk.Tk()
root.title("Mover texto con ciclo for")

# Crear el lienzo (canvas)
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Crear el texto inicial en el lienzo
text_id = canvas.create_text(200, 150, text="Rodrigo Silva", font=("Arial", 16))

# Crear un botón para iniciar el movimiento del texto
button = tk.Button(root, text="Mover", command=move_text)
button.pack()

# Ejecutar el bucle principal de la ventana
root.mainloop()
