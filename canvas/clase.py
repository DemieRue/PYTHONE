from tkinter import *
import tkinter as tk 
ventana1=Tk()
ventana1.title("Graficas primitivas")
canvas1=tk.Canvas(ventana1,width=400,height=450,bg="blue")
canvas1.place(x=0,y=0)
presionado=False
px=0
py=0
#metodos
def bpresion(event):
    global presionado
    global px,py
    presionado=True
    px=event.x
    py=event.y
def punto_mouse(event):
    global presionado
    global px,py
    if presionado:
        canvas1.create_line(px,py,event.x,event.y,fill="white")
        px=event.x
        py=event.y

def boton_soltar(event):
    global presionado
    presionado=False
    
canvas1.bind("<ButtonPress-1>",bpresion)
canvas1.bind("<Motion>",punto_mouse)
canvas1.bind("<ButtonRelease-1>",boton_soltar)

ventana1.mainloop()