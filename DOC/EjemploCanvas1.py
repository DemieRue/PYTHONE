from tkinter import *
import tkinter as tk 
ventana1=Tk()
ventana1.title("Graficas primitivas")
canvas1=tk.Canvas(ventana1,width=400,height=450,bg="black")
canvas1.place(x=0,y=0)
#creacion de una linea
#canvas1.create_line(punto_inicial_x,punto_inicial_y,punto_final_x,punto_final_y,color)
canvas1.create_line(10,10,100,10,fill="red")
#creacion de un rectangulo
#canvas1.create_rectangle(punto_x,punto_y,ancho,alto,relleno)
canvas1.create_rectangle(150,200,250,110,fill="white")
#creacion del ovalo
#canvas1.create_oval(punto_x,punto_y,radio,??,outline="red")
canvas1.create_oval(300,200,400,350,outline="red",fill="red")
#
canvas1.create_arc(150,300,250,340,outline="red",start=180,extent=90)
#grafica de texto
canvas1.create_text(120,250,font=('arial',30),fill="blue",text="Hola")
ventana1.mainloop()
