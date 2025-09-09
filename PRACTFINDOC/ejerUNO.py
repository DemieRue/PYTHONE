#UNIV. RODRIGO SILVA MAMANI

import tkinter as tk

def cambiar_estado_sala():
    if sala_button["text"] == "Encendido":
        sala_button["text"] = "Apagado"
        sala_button["bg"] = "red"
        
    else:
        sala_button["text"] = "Encendido"
        sala_button["bg"] = "lime"
        

def cambiar_estado_comedor():
    if comedor_button["text"] == "Encendido":
        comedor_button["text"] = "Apagado"
        comedor_button["bg"] = "red"
        
    else:
        comedor_button["text"] = "Encendido"
        comedor_button["bg"] = "lime"

def cambiar_estado_cuarto1():
    if cuarto1_button["text"] == "Encendido":
        cuarto1_button["text"] = "Apagado"
        cuarto1_button["bg"] = "red"
        
    else:
        cuarto1_button["text"] = "Encendido"
        cuarto1_button["bg"] = "lime"
        

def cambiar_estado_cuarto2():
    if cuarto2_button["text"] == "Encendido":
        cuarto2_button["text"] = "Apagado"
        cuarto2_button["bg"] = "red"
        
    else:
        cuarto2_button["text"] = "Encendido"
        cuarto2_button["bg"] = "lime"

def cambiar_estado_musica():
    if musica_button["text"] == "Encendido":
        musica_button["text"] = "Apagado"
        musica_button["bg"] = "red"
        
    else:
        musica_button["text"] = "Encendido"
        musica_button["bg"] = "lime"
        

def cambiar_estado_cocina():
    if cocina_button["text"] == "Encendido":
        cocina_button["text"] = "Apagado"
        cocina_button["bg"] = "red"
        
    else:
        cocina_button["text"] = "Encendido"
        cocina_button["bg"] = "lime"

def cambiar_estado_patio():
    if patio_button["text"] == "Encendido":
        patio_button["text"] = "Apagado"
        patio_button["bg"] = "red"
        
    else:
        patio_button["text"] = "Encendido"
        patio_button["bg"] = "lime"
        

def cambiar_estado_baño():
    if baño_button["text"] == "Encendido":
        baño_button["text"] = "Apagado"
        baño_button["bg"] = "red"
        
    else:
        baño_button["text"] = "Encendido"
        baño_button["bg"] = "lime"
        

def encender_todos():
    sala_button["text"] = "Encendido"
    sala_button["bg"] = "lime"

    comedor_button["text"] = "Encendido"
    comedor_button["bg"] = "lime"

    cuarto1_button["text"] = "Encendido"
    cuarto1_button["bg"] = "lime"

    cuarto2_button["text"] = "Encendido"
    cuarto2_button["bg"] = "lime"    

    musica_button["text"] = "Encendido"
    musica_button["bg"] = "lime"

    cocina_button["text"] = "Encendido"
    cocina_button["bg"] = "lime"

    patio_button["text"] = "Encendido"
    patio_button["bg"] = "lime"

    baño_button["text"] = "Encendido"
    baño_button["bg"] = "lime"        


def apagar_todos():
    sala_button["text"] = "Apagado"
    sala_button["bg"] = "red"
    
    comedor_button["text"] = "Apagado"
    comedor_button["bg"] = "red"

    cuarto1_button["text"] = "Apagado"
    cuarto1_button["bg"] = "red"    
    
    cuarto2_button["text"] = "Apagado"
    cuarto2_button["bg"] = "red"

    musica_button["text"] = "Apagado"
    musica_button["bg"] = "red"

    cocina_button["text"] = "Apagado"
    cocina_button["bg"] = "red"

    patio_button["text"] = "Apagado"
    patio_button["bg"] = "red"

    baño_button["text"] = "Apagado"
    baño_button["bg"] = "red"


ventana = tk.Tk()
ventana.title("Control de Casa Domótica")

departamento_label = tk.Label(ventana, text="CASA DOMOTICA")
departamento_label.grid(row=0, column=0)

sala_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_sala)
sala_button.grid(row=1, column=1, padx=10, pady=5)
sala_label = tk.Label(ventana, text="Sala")
sala_label.grid(row=1, column=0)

comedor_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_comedor)
comedor_button.grid(row=2, column=1, padx=10, pady=5)
comedor_label = tk.Label(ventana, text="Comedor")
comedor_label.grid(row=2, column=0)

cuarto1_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_cuarto1)
cuarto1_button.grid(row=3, column=1, padx=10, pady=5)
cuarto1_label = tk.Label(ventana, text="Cuarto 1")
cuarto1_label.grid(row=3, column=0)

cuarto2_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_cuarto2)
cuarto2_button.grid(row=4, column=1, padx=10, pady=5)
cuarto2_label = tk.Label(ventana, text="Cuarto 2")
cuarto2_label.grid(row=4, column=0)

musica_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_musica)
musica_button.grid(row=5, column=1, padx=10, pady=5)
musica_label = tk.Label(ventana, text="Musica")
musica_label.grid(row=5, column=0)

cocina_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_cocina)
cocina_button.grid(row=6, column=1, padx=10, pady=5)
cocina_label = tk.Label(ventana, text="Cocina")
cocina_label.grid(row=6, column=0)

patio_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_patio)
patio_button.grid(row=7, column=1, padx=10, pady=5)
patio_label = tk.Label(ventana, text="Patio")
patio_label.grid(row=7, column=0)

baño_button = tk.Button(ventana, text="Apagado", bg="red", command=cambiar_estado_baño)
baño_button.grid(row=8, column=1, padx=10, pady=5)
baño_label = tk.Label(ventana, text="Baño")
baño_label.grid(row=8, column=0)


encender_todos_button = tk.Button(ventana, text="Encender Todos", command=encender_todos)
encender_todos_button.grid(row=9, column=0, padx=10, pady=5)

apagar_todos_button = tk.Button(ventana, text="Apagar Todos", command=apagar_todos)
apagar_todos_button.grid(row=9, column=1, padx=10, pady=5)

cerrar_ventana_button = tk.Button(ventana, text="Cerrar Ventana", command=ventana.quit)
cerrar_ventana_button.grid(row=10, column=0, columnspan=2, padx=10, pady=5)


ventana.mainloop()
