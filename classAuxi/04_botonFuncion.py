import tkinter as tk
from tkinter import ttk

#creamos objeto de la clase tk
ventana=tk.Tk()
#tamaño
ancho=900
alto=200
tamaño=str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
#titulo
ventana.title('Titulo de la ventana')
#icono
ventana.iconbitmap("C:\\Users\\alque\\Documents\\PYTHON\\classAuxi\\icono1.ico")
#funcion click
def click():
    print("boton pulsado")
    boton01.config(text="has pulsado el boton 2")
#creando 1er boton
boton01=ttk.Button(ventana,text='Enter')
boton01.pack()
#otro boton
boton02=ttk.Button(ventana,text='click',command=click)
boton02.pack()
#poner siempre al final
ventana.mainloop()