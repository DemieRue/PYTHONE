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
#creando 1er boton
boton=ttk.Button(ventana,text='Enter')
boton.pack()
#poner siempre al final
ventana.mainloop()