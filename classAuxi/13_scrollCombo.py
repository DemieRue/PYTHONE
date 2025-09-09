import tkinter as tk
from tkinter import ttk, scrolledtext
# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 500
alto = 400
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Varios, scroll / combo')
# icono
#ventana.iconbitmap('icono.ico')
# scrolled text
texto = """Las listas desplegables son un elemento usado habitualmente en aplicaciones gráficas mediante la cual, se da al usuario, la capacidad de seleccionar una opción de entre las presentadas en dicha lista. En esta ocasión vamos, pues, a ver como crear dicho elemento, empezado por la creación de la ventana en la que vamos a incluirla y a importación tanto de «Tkinter» como del módulo «ScrolledText»
Tenemos ya creada nuestra lista desplegable, la cual, sin embargo, se encuentra vacía (por o que de momento nos serviría de poco). Es por ello, que lo que haremos a continuación será añadirle las opciones. Para ello, comenzaremos creando una lista (de nombre «opciones«) de tres opciones a incluir, que en un alarde de creatividad, llevarán por nombre, «opcion 1«, «opcion 2» y «opcion 3«.
Imposibilitando, de ese modo, la introducción de opciones adicionales a las previamente establecidas.

Por último, haremos referencia a la posibilidad de introducir alguna opción predeterminada, para que se muestre al abrir el programa. Esto lo haremos con el método «.set()» """
scroll = scrolledtext.ScrolledText(ventana, width=60, height=15)# ,wrap=tk.WORD
scroll.insert(tk.INSERT, texto)
scroll.grid(row=1, column=1)
# combo box
datos = [x*3 for x in range(20)]
combobox = ttk.Combobox(ventana, width=15, value=datos)
combobox.grid(row=5, column=1, padx=15, pady=15)
combobox.current(3)
print(f'Mostrando el valor del combo al iniciar ventana {combobox.get()}')
# imagen en el boton
#imagen = tk.PhotoImage(file='C:\\Users\\Personal\\Desktop\\Python_2022\\INF_SUP I\\CAP3\\tkinter-main\\logo.png')
#boton = ttk.Button(ventana, image=imagen)
#boton.grid(row=6, column=1)
#poner siempre al final
ventana.mainloop()
