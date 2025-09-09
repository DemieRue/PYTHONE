import tkinter as tk

def toggle_button(button):
    if button["text"] == "Encendido":
        button["text"] = "Apagado"
        button["bg"] = "red"
        status_label.config(text=f"{button['name']}: Apagado")
    else:
        button["text"] = "Encendido"
        button["bg"] = "green"
        status_label.config(text=f"{button['name']}: Encendido")

# Crear la ventana
window = tk.Tk()
window.title("Control de Casa Domótica")

# Crear los botones
buttons = []
for i in range(11):
    button = tk.Button(window, text="Apagado", width=10)
    button["command"] = lambda b=button: toggle_button(b)
    button.pack()
    buttons.append(button)

# Crear la etiqueta de estado
status_label = tk.Label(window, text="Estado de los botones:")
status_label.pack()

# Ejecutar la ventana
window.mainloop()
