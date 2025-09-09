import tkinter as tk

ventana = tk.Tk()
ventana.title("Dibujando Cuadrado y Triangulo")

canvas = tk.Canvas(ventana, width = 400, height = 200)
canvas.create_rectangle(50, 50, 150, 150, fill = "blue")
canvas.create_polygon(300, 50, 350, 150, 250, 150, fill = "red")
canvas.pack()

ventana.mainloop()