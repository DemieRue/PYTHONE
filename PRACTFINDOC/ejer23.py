import tkinter as tk
from tkinter import messagebox

def agregar_persona():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()

    if nombre and apellido and edad:
        persona = {"nombre": nombre, "apellido": apellido, "edad": edad}
        listbox_personas.insert(tk.END, persona)
    else:
        messagebox.showwarning("Error", "Por favor, complete todos los campos.")

def eliminar_persona():
    seleccion = listbox_personas.curselection()
    if seleccion:
        listbox_personas.delete(seleccion)
        mostrar_detalle("", "", "")
    else:
        messagebox.showwarning("Error", "Por favor, seleccione una persona.")

def mostrar_detalle(nombre, apellido, edad):
    label_nombre.config(text=f"Nombre: {nombre}")
    label_apellido.config(text=f"Apellido: {apellido}")
    label_edad.config(text=f"Edad: {edad}")

def seleccionar_persona(event):
    seleccion = listbox_personas.curselection()
    if seleccion:
        persona = listbox_personas.get(seleccion)
        mostrar_detalle(persona["nombre"], persona["apellido"], persona["edad"])
    else:
        mostrar_detalle("", "", "")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Agregar personas")
ventana.geometry("400x300")

# Crear los elementos de la interfaz
label_nombre = tk.Label(ventana, text="")
label_nombre.pack()

label_apellido = tk.Label(ventana, text="")
label_apellido.pack()

label_edad = tk.Label(ventana, text="")
label_edad.pack()

label_nombre_input = tk.Label(ventana, text="Nombre:")
label_nombre_input.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido_input = tk.Label(ventana, text="Apellido:")
label_apellido_input.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_edad_input = tk.Label(ventana, text="Edad:")
label_edad_input.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

button_agregar = tk.Button(ventana, text="Agregar", command=agregar_persona)
button_agregar.pack()

button_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_persona)
button_eliminar.pack()

listbox_personas = tk.Listbox(ventana)
listbox_personas.pack()

listbox_personas.bind("<<ListboxSelect>>", seleccionar_persona)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
