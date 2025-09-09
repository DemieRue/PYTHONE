import tkinter as tk

# Variables para contabilizar los clics
contador_click_izquierdo = 0
contador_click_derecho = 0
contador_click_central = 0

def contar_click_izquierdo(event):
    global contador_click_izquierdo
    contador_click_izquierdo += 1
    print(f'Clic izquierdo: {contador_click_izquierdo}')

def contar_click_derecho(event):
    global contador_click_derecho
    contador_click_derecho += 1
    print(f'Clic derecho: {contador_click_derecho}')

def contar_click_central(event):
    global contador_click_central
    contador_click_central += 1
    print(f'Clic central: {contador_click_central}')

# Crear una ventana de tkinter
ventana = tk.Tk()

# Asociar las funciones de contar a los eventos de clic del mouse
ventana.bind('<Button-1>', contar_click_izquierdo)  # Clic izquierdo
ventana.bind('<Button-3>', contar_click_derecho)   # Clic derecho
ventana.bind('<Button-2>', contar_click_central)   # Clic central

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
