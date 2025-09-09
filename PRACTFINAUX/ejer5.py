import tkinter as tk

class vcirculo:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=200)
        self.canvas.pack()
        
        self.x1 = 50
        self.y1 = 50
        self.x2 = 150
        self.y2 = 150
        
        self.ovalo = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill='blue')
        
        self.boton_crecer = tk.Button(master, text='Crecer', command=self.crecer_circulo)
        self.boton_crecer.pack(side=tk.LEFT)
        
        self.boton_decrecer = tk.Button(master, text='Decrecer', command=self.decrecer_circulo)
        self.boton_decrecer.pack(side=tk.LEFT)
        
    def crecer_circulo(self):
        
        self.x1 -= 5
        self.y1 -= 5
        self.x2 += 5
        self.y2 += 5
        
        self.canvas.coords(self.ovalo, self.x1, self.y1, self.x2, self.y2)
        
    def decrecer_circulo(self):
        
        self.x1 += 5
        self.y1 += 5
        self.x2 -= 5
        self.y2 -= 5
        
        self.canvas.coords(self.ovalo, self.x1, self.y1, self.x2, self.y2)

ventana = tk.Tk()
ventana.title("Crecimiento y Decrecimiento de Circulo")
simulador = vcirculo(ventana)

ventana.mainloop()