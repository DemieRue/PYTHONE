from tkinter import *
import tkinter as tk 
ventana1=Tk()
ventana1.title("Graficas primitivas")
canvas1=tk.Canvas(ventana1,width=400,height=450,bg="black")
canvas1.place(x=0,y=0)
#metodo presiona
def presiona(event):
    canvas1.create_oval(event.x-4,event.y-4,event.x+4,event.y+4,fill="blue")
def punto_mouse(event):
    ventana1.title(str(event.x)+","+str(event.y))
#vincular el evento de mouse con canvas
canvas1.bind("<Motion>",punto_mouse)
canvas1.bind("<Button-1>",presiona)

ventana1.mainloop()
