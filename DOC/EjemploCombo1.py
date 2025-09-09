from tkinter import *
from tkinter import ttk

def obtener_sel():
    #obtener elemento seleccionado de la lista
    print(lista_desplegable.current())

ventana=Tk()
ventana.title("Ejemplo de lista desplegable")
ventana.geometry('300x190')

#lista desplegable
lista_desplegable=ttk.Combobox(ventana,width=17,state='readonly')
lista_desplegable.place(x=30,y=77)
#opcion predeterminada
lista_desplegable.set("opcion 1")
#lista de opciones
opciones=["opcion 1","opcion 2","opcion 3"]

#ponemos valores en la lista
lista_desplegable['values']=opciones

#boton para permitir obtener informacion
boton1=Button(ventana,text="Obtiene",bg='gold',command=obtener_sel)
boton1.place(x=170,y=77)

ventana.mainloop()


