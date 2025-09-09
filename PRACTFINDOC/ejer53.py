#Univ. RODRIGO SILVA MAMANI
import tkinter as tk
from tkinter import *

ventana=tk.Tk()
ventana.title("Aumento y Disminucion")
ventana.geometry("600x600")

def dimension(valor):
    posicion=int(valor)+10
    canvas.delete("rectangulo")
    canvas.create_rectangle(posicion, posicion, posicion, posicion,tags="rectangulo", fill='blue', outline='black')

dimensionado=Scale(ventana,from_=0,to=500,orient=HORIZONTAL,command=dimension)
dimensionado.pack(side=BOTTOM,fill=X)

canvas=Canvas(ventana,bg="green")
canvas.pack(expand=YES,fill=BOTH)
ventana.mainloop()