import tkinter as tk

# Variables para contabilizar los clics
contador_click_izquierdo = 0
contador_click_derecho = 0
contador_click_central = 0

def contar_click(event):
    global contador_click_izquierdo, contador_click_derecho, contador_click_central

    if event.num == 1:  # Clic izquierdo
        contador_click_izquierdo += 1
    elif event.num == 3:  # Clic derecho
        contador_click_derecho += 1
    elif event.num == 2:  # Clic central
        contador_click_central += 1

    actualizar_contadores()

def actualizar_contadores():
    lbl_click_izquierdo.config(text=f'Clic izquierdo: {contador_click_izquierdo}')
    lbl_click_derecho.config(text=f'Clic derecho: {contador_click_derecho}')
    lbl_click_central.config(text=f'Clic central: {contador_click_central}')

# Crear una ventana de tkinter
ventana = tk.Tk()
ventana.geometry("500x400")
ventana.title("Contador de Clics")

# Etiquetas para mostrar los contadores
lbl_click_izquierdo = tk.Label(ventana, text="Clic izquierdo: 0")
lbl_click_izquierdo.pack()

lbl_click_derecho = tk.Label(ventana, text="Clic derecho: 0")
lbl_click_derecho.pack()

lbl_click_central = tk.Label(ventana, text="Clic central: 0")
lbl_click_central.pack()

# Asociar la función de contar a los eventos de clic del mouse en la ventana
ventana.bind("<Button-1>", contar_click)  # Clic izquierdo
ventana.bind("<Button-3>", contar_click)  # Clic derecho
ventana.bind("<Button-2>", contar_click)  # Clic central

ventana.mainloop()
