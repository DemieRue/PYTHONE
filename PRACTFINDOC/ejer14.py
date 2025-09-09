import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control de Casa Domótica")

        # Crear botones
        self.buttons = {}
        for i, name in enumerate(["sala", "comedor", "cocina", "baño", "cuarto1", "cuarto2", "cuarto3", "música", "ventilador", "tv", "fiesta"]):
            button = tk.Button(self.root, text=name, command=lambda name=name: self.toggle(name))
            button.grid(row=i//2, column=i%2)
            self.buttons[name] = button

        # Crear etiqueta para mostrar estado de los botones
        self.status_label = tk.Label(self.root, text="")
        self.status_label.grid(row=6, column=0)

        # Crear botones principales
        tk.Button(self.root, text="Encender Todos", command=self.turn_on_all).grid(row=7, column=0)
        tk.Button(self.root, text="Apagar Todos", command=self.turn_off_all).grid(row=7, column=1)
        tk.Button(self.root, text="Cerrar Ventana", command=self.close).grid(row=8, column=0)

    def toggle(self, name):
        if self.buttons[name]["text"] == name:
            self.buttons[name]["text"] = name + " (ON)"
            self.status_label["text"] = f"{name} encendido"
        else:
            self.buttons[name]["text"] = name
            self.status_label["text"] = f"{name} apagado"

    def turn_on_all(self):
        for name in self.buttons:
            self.buttons[name]["text"] = name + " (ON)"
            self.status_label["text"] = "Todos encendidos"

    def turn_off_all(self):
        for name in self.buttons:
            self.buttons[name]["text"] = name
            self.status_label["text"] = "Todos apagados"

    def close(self):
        self.root.destroy()

app = App()
app.root.mainloop()