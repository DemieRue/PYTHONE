from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Cambiar Color Ventana")
ventana.geometry("500x300")

colores = ["pink", "lime", "purple", "yellow", "silver", "black", "orange"]
combo = ttk.Combobox(ventana, values=colores)
combo.pack()

def change_color():
    
    color = combo.get()
    
    if color in colores:
        ventana.configure(bg=color)
    
    else:
        color_name = color[1]
        ventana.configure(bg=color_name)

boton_color = Button(ventana, text="Cambiar Color", command=change_color)
boton_color.pack()

ventana.mainloop()