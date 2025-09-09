import tkinter as tk

def dibujar_cuadrado(canvas):
    canvas.create_rectangle(50, 50, 150, 150, fill="red")

def dibujar_triangulo(canvas):
    canvas.create_polygon(100, 200, 50, 300, 150, 300, fill="blue")

ventana = tk.Tk()
ventana.title("Dibujar Figuras")
canvas = tk.Canvas(ventana, width=300, height=400)
canvas.pack()

dibujar_cuadrado(canvas)
dibujar_triangulo(canvas)

ventana.mainloop()
