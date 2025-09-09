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
####
ventana.rowconfigure(0,weight=2)
ventana.rowconfigure(1,weight=4)

#creando 1er boton
boton01=ttk.Button(ventana,text='boton1')
boton01.grid(row=0,column=0,sticky='S')
boton02=ttk.Button(ventana,text='boton2')
boton02.grid(row=0,column=1,sticky='S')
boton03=ttk.Button(ventana,text='boton3')
boton03.grid(row=0,column=2,sticky='W')
boton04=ttk.Button(ventana,text='boton4')
boton04.grid(row=0,column=4,sticky='NE')
#poner siempre al final
ventana.mainloop()