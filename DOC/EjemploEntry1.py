from tkinter import *
ventana2=Tk()
#creamos el frame o marco
marco2=Frame()
marco2.grid(row=0, column=0)
marco2.config(width="150",height="250")
marco2.config(bg="white")
titulo=Label(marco2,text="Introduzca su nombre:").grid(row=0,column=0)
#crear el objeto que permite introducir texto por teclado
tnombre=Entry(marco2)
tnombre.grid(row=0,column=1)
def borrar():
    tnombre.delete(0,END)
def saludo():
    n1=tnombre.get()
    tnombre.delete(0,END)
    tnombre.insert(0,"Hola "+n1) 
#boton
boton1=Button(marco2,text="Saluda",command=saludo)
boton1.grid(row=1,column=1)
botonb=Button(marco2,text="Borrar",command=borrar)
botonb.grid(row=1,column=2)
ventana2.mainloop()
