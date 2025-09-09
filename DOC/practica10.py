# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:39:32 2023

@author: Latioskev
"""

import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x400")

canvas = tk.Canvas(ventana, width=400, height=400,bg="blue")
canvas.pack()

x = 0
y = 0
clic =False
aux=-1

def cambiaColor():
    global aux
    if aux > 5:
        aux=-1
    else:
        aux+=1
    return aux

lcolor=['yellow','orange','red','green','white','pink']

def cambiarColor(event):
    global clic
    clic=True
    canvas.itemconfig(text, fill="red")

def FinclicMouse(event):
    global clic
    clic = False
def ejecutar(event):
    global text
    global x,y
    text = canvas.create_text(x, y, text="Kevin Larrazabal", font=("arial", 20),fill=lcolor[cambiaColor()])
    canvas.tag_bind(text, "<Enter>", cambiarColor)
    canvas.bind("<Enter>",FinclicMouse)
    for i in range(1, 400):       
        x += 5 
        y += 6  
        canvas.coords(text, x, y)
        canvas.update()
        canvas.after(150)
canvas.bind("<Button-1>",ejecutar)
ventana.mainloop()


