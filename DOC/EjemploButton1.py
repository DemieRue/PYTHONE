from tkinter import *
ventana2=Tk()
#creamos el metodo
def mensaje():
    Label(marco2,text="Hola a todos").grid(row=0,column=0)
#creamos el frame o marco
marco2=Frame()
marco2.grid(row=0, column=0)
marco2.config(width="150",height="250")
marco2.config(bg="black")
#creamos el boton
boton1=Button(marco2,text="Saluda",command=mensaje).grid(row=0,column=0)
ventana2.mainloop()
