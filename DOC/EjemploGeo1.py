#USO DE metodo geometry
from tkinter import *
from tkinter import ttk
ventana=Tk()
ventana.title("Ejemplo lista desplegable")
ventana.geometry('400x200')
#lista desplegable
lista1=ttk.Combobox(ventana,width=17)
lista1.place(x=30,y=70)
#creamos la lista
paises=["Bolivia","Peru","Argentina","Brazil"]
#ponemos los valores a la lista esplegable
lista1['values']=paises

def obtener():
    print(lista1.get())
boton=Button(ventana,text="Obtener",command=obtener)
boton.place(x=50,y=100)

ventana.mainloop()
