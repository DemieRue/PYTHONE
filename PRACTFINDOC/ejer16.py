import tkinter as tk

class CasaDomoticaGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.estado_botones = {
            'sala': False,
            'comedor': False,
            'cocina': False,
            'baño': False,
            'cuarto1': False,
            'cuarto2': False,
            'cuarto3': False,
            'musica': False,
            'ventilador': False,
            'tv': False,
            'fiesta': False
        }

        self.crear_interfaz()

    def crear_interfaz(self):
        self.ventana.title("Casa Domótica")

        # Botones de encendido y apagado
        self.botones = {}
        fila = 0
        for nombre, estado in self.estado_botones.items():
            lbl_nombre = tk.Label(self.ventana, text=nombre.capitalize())
            lbl_nombre.grid(row=fila, column=0, padx=10, pady=5)
            
            btn_encender = tk.Button(self.ventana, text="Encender", command=lambda n=nombre: self.cambiar_estado(n, True))
            btn_encender.grid(row=fila, column=1, padx=5, pady=5)
            
            btn_apagar = tk.Button(self.ventana, text="Apagar", command=lambda n=nombre: self.cambiar_estado(n, False))
            btn_apagar.grid(row=fila, column=2, padx=5, pady=5)

            estado_lbl = tk.Label(self.ventana, text="Estado: {}".format("Encendido" if estado else "Apagado"))
            estado_lbl.grid(row=fila, column=3, padx=10, pady=5)

            self.botones[nombre] = {
                'encender': btn_encender,
                'apagar': btn_apagar,
                'estado': estado_lbl
            }

            fila += 1

        # Botones principales
        self.btn_encender_todos = tk.Button(self.ventana, text="Encender todos", command=self.encender_todos)
        self.btn_encender_todos.grid(row=fila, column=0, padx=10, pady=5)

        self.btn_apagar_todos = tk.Button(self.ventana, text="Apagar todos", command=self.apagar_todos)
        self.btn_apagar_todos.grid(row=fila, column=1, padx=10, pady=5)

        self.btn_cerrar_ventana = tk.Button(self.ventana, text="Cerrar ventana", command=self.ventana.quit)
        self.btn_cerrar_ventana.grid(row=fila, column=2, padx=10, pady=5)

    def cambiar_estado(self, nombre, encender):
        self.estado_botones[nombre] = encender
        estado_lbl = self.botones[nombre]['estado']
        estado_lbl.config(text="Estado: {}".format("Encendido" if encender else "Apagado"))

    def encender_todos(self):
        for nombre in self.estado_botones:
            self.cambiar_estado(nombre, True)

    def apagar_todos(self):
        for nombre in self.estado_botones:
            self.cambiar_estado(nombre, False)


ventana = tk.Tk()
app = CasaDomoticaGUI(ventana)
ventana.mainloop()
