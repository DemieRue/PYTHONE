import tkinter as tk
from tkinter import ttk, scrolledtext
# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 500
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)        #(400x700)
# titulo
ventana.title(' ComboBox')
# combo box
datos = [x*1 for x in range(20)] #('amarillo','rojo','verde','azul')
combobox = ttk.Combobox(ventana, width=15, value=datos)
combobox.grid(row=5, column=1, padx=15, pady=15)
combobox.current(2)
print('Mostrando el valor del combo al iniciar ventana ',combobox.get())
# poner siempre al final
ventana.mainloop()