
from tkinter import *
import tkinter as tk
ventana = tk.Tk()
ventana.geometry("500x400")
ventana.title("Lista en Tk")

def adicionar():
    an=Enombre.get()
    ap=Eapellido.get()
    ae=Eedad.get()
    aux=an+" "+ap+"  "+ ae
    listbox.insert(tk.END, aux)
    lnom1.config(text=an)
    lape1.config(text=ap)
    ledad1.config(text=ae)
    
def eliminar():
    n2=listbox.curselection()
    listbox.delete(n2)           
    Enombre.delete(0,END)
    Eapellido.delete(0,END)
    Eedad.delete(0,END)
    lnom1.config(text="aqui nombre")
    lape1.config(text="aqui apellido")
    ledad1.config(text="aqui edad")


ltitulo=Label(ventana,text="Agregar persona")
ltitulo.place(x=10,y=50)

nombre=Label(ventana,text="Nombre:")
nombre.place(x=10,y=100)
Enombre=Entry(ventana)
Enombre.place(x=80,y=100)

apellido=Label(ventana,text="Apellidos:")
apellido.place(x=10,y=130)
Eapellido=Entry(ventana)
Eapellido.place(x=80,y=130)

edad=Label(ventana,text="Edad:")
edad.place(x=10,y=160)
Eedad=Entry(ventana)
Eedad.place(x=80,y=160)

linfo=Label(ventana,text="Información:")
linfo.place(x=10,y=190)

lnom=Label(ventana,text="Nombre:")
lnom.place(x=10,y=220)
lnom1=Label(ventana,text="el nombre")
lnom1.place(x=80,y=220)

lape=Label(ventana,text="Apellidos:")
lape.place(x=10,y=250)
lape1=Label(ventana,text="el apellido")
lape1.place(x=80,y=250)

ledad=Label(ventana,text="Edad:")
ledad.place(x=10,y=280)
ledad1=Label(ventana,text=" la edad")
ledad1.place(x=80,y=280)

listbox = Listbox()
listbox.place(x=350,y=70)
listbox.insert(tk.END, "")


bad=Button(ventana,text="Añadir",command=adicionar)
bad.place(x=250,y=100)

bele=Button(ventana,text="Eliminar de lista",command=eliminar)
bele.place(x=250,y=150)

ventana.mainloop()