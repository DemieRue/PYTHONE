import tkinter as tk

# Crea una ventana de tkinter
ventana = tk.Tk()
ventana.title("Calculadora de resistencias")

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

# Crea una función para calcular la resistencia
def calcular_resistencia():
    codigo = [color1.get(), color2.get(), color3.get()]
    valor = str(colores[codigo[0]]) + str(colores[codigo[1]])
    multiplicador = colores[codigo[2]]
    resistencia = int(valor) * 10**multiplicador
    if resistencia >= 1e6:
        resistencia_texto = str(resistencia/1e6) + "MΩ"
    elif resistencia >= 1e3:
        resistencia_texto = str(resistencia/1e3) + "kΩ"
    else:
        resistencia_texto = str(resistencia) + "Ω"
    resultado.config(text=resistencia_texto)

# Crea tres variables de tkinter para los tres colores de la resistencia
color1 = tk.StringVar()
color2 = tk.StringVar()
color3 = tk.StringVar()

# Crea tres menús desplegables para seleccionar los colores
menu_color1 = tk.OptionMenu(ventana, color1, *colores.keys())
menu_color1.pack(side=tk.LEFT, padx=10)
menu_color2 = tk.OptionMenu(ventana, color2, *colores.keys())
menu_color2.pack(side=tk.LEFT, padx=10)
menu_color3 = tk.OptionMenu(ventana, color3, *colores.keys())
menu_color3.pack(side=tk.LEFT, padx=10)

# Crea un botón para calcular la resistencia
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_resistencia)
boton_calcular.pack(pady=10)

# Crea un widget para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecuta la ventana de tkinter
ventana.mainloop()
