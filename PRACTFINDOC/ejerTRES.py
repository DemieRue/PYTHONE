#UNIV. RODRIGO SILVA MAMANI
import tkinter as tk
from tkinter import Canvas


def mostrar_linea():
    canvas.delete("all")
    canvas.create_line(50, 100, 200, 100 ,fill='red', width=5)


def mostrar_rectangulo():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 200, 150, fill='blue', outline='black')


def mostrar_circulo():
    canvas.delete("all")
    canvas.create_oval(100, 50, 300, 250, fill='green', outline='')


def mostrar_triangulo():
    canvas.delete("all")
    canvas.create_polygon(50, 150, 125, 50, 200, 150, fill='yellow', outline='black')


def mostrar_ovalo():
    canvas.delete("all")
    canvas.create_oval(100, 50, 250, 100, fill='purple', outline='')


ventana = tk.Tk()
ventana.title("Gráficas Básicas")
ventana.geometry("400x500")


canvas = Canvas(ventana, width=300, height=300, bg= 'white')
canvas.pack()


btn_linea = tk.Button(ventana, text="Línea", command=mostrar_linea)
btn_linea.pack()

btn_rectangulo = tk.Button(ventana, text="Rectángulo", command=mostrar_rectangulo)
btn_rectangulo.pack()

btn_circulo = tk.Button(ventana, text="Círculo", command=mostrar_circulo)
btn_circulo.pack()

btn_triangulo = tk.Button(ventana, text="Triángulo", command=mostrar_triangulo)
btn_triangulo.pack()

btn_ovalo = tk.Button(ventana, text="Óvalo", command=mostrar_ovalo)
btn_ovalo.pack()


ventana.mainloop()
