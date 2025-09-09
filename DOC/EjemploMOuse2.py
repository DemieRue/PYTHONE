#ejemplo de uso de evento mouse 2
from tkinter import *
vent1=Tk()
vent1.title("Ejemplo de evento Mouse")
vent1.geometry("400x250")
#metodos
def cambiarRojo(event):
    lcambia.config(bg="red")
def cambiarAzul(event):
    lcambia.config(bg="blue")

lcambia=Label(vent1,text="Hola",font="consola 40")
lcambia.place(x=100,y=100)
lcambia.bind("<Button-1>",cambiarRojo)
lcambia.bind("<Button-3>",cambiarAzul)
vent1.mainloop()
