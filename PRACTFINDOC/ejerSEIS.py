#UNIV. RODRIGO SILVA MAMANI

import tkinter as tk

contador_click_izquierdo = 0
contador_click_derecho = 0

def contar_click(event):
    global contador_click_izquierdo, contador_click_derecho

    if event.num == 1: 
        contador_click_izquierdo += 1
    elif event.num == 3:  
        contador_click_derecho += 1

    actualizar_contadores()

def actualizar_contadores():
    lbl_click_izquierdo.config(text=f'Clic izquierdo: {contador_click_izquierdo}')
    lbl_click_derecho.config(text=f'Clic derecho: {contador_click_derecho}')

ventana = tk.Tk()
ventana.geometry("500x400")
ventana.title("Contador de Clics")

lbl_click_izquierdo = tk.Label(ventana, text="Clic izquierdo: 0")
lbl_click_izquierdo.pack()

lbl_click_derecho = tk.Label(ventana, text="Clic derecho: 0")
lbl_click_derecho.pack()

ventana.bind("<Button-1>", contar_click)  
ventana.bind("<Button-3>", contar_click)  

ventana.mainloop()
