import tkinter as tk
from tkinter import ttk

# Crea una ventana de tkinter
ventana = tk.Tk()
ventana.title("Calculadora de resistencias")
ventana.geometry("400x300")

# Crea un diccionario que asocia cada color con su valor numérico
colores = {
    "negro": 0,
    "marrón": 1,
    "rojo": 2,
    "naranja": 3,
    "amarillo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "gris": 8,
    "blanco": 9
}

# Crea un diccionario que asocia cada valor de tolerancia con su símbolo
tolerancias = {
    "±1%": "F",
    "±2%": "G",
    "±5%": "J",
    "±10%": "K"
}
resultado = tk.Label(ventana, text="")
resultado.grid(row=3, column=4, padx=10,pady=10)
# Crea una función para calcular la resistencia
def calcular_resistencia():
    codigo = [color1.get(), color2.get(), color3.get(), color4.get()]
    valor = str(colores[codigo[0]]) + str(colores[codigo[1]])
    multiplicador = colores[codigo[2]]
    tolerancia = tolerancias[codigo[3]]
    resistencia = int(valor) * 10**multiplicador
    if resistencia >= 1e6:
        resistencia_texto = str(resistencia/1e6) + "MΩ"
    elif resistencia >= 1e3:
        resistencia_texto = str(resistencia/1e3) + "kΩ"
    else:
        resistencia_texto = str(resistencia) + "Ω"
    resultado.config(ventana,text=resistencia_texto + " " + tolerancia)

# Crea cuatro variables de tkinter para los cuatro colores de la resistencia
color1 = tk.StringVar()
color2 = tk.StringVar()
color3 = tk.StringVar()
color4 = tk.StringVar()

# Crea tres menús desplegables para seleccionar los colores
colores_opciones = list(colores.keys())
menu_color1 = ttk.Combobox(ventana, values=colores_opciones, textvariable=color1)
menu_color1.grid(row=0, column=1, padx=10, pady=10)
menu_color2 = ttk.Combobox(ventana, values=colores_opciones, textvariable=color2)
menu_color2.grid(row=0, column=2, padx=10, pady=10)
menu_color3 = ttk.Combobox(ventana, values=colores_opciones, textvariable=color3)
menu_color3.grid(row=0, column=3, padx=10, pady=10)

# Crea un menú desplegable para seleccionar la tolerancia
tolerancias_opciones = list(tolerancias.keys())
menu_color4 = ttk.Combobox(ventana, values=tolerancias_opciones, textvariable=color4)
menu_color4.grid(row=0, column=3, padx=10, pady=10)

# Crea un botón para calcular la resistencia
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_resistencia)
boton_calcular.grid(row=3, column=2, padx=10, pady=10)




ventana.mainloop()