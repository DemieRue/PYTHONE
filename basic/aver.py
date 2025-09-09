import tkinter as tk


def suma():
    resultado.set(float(entrada1.get()) + float(entrada2.get()))

def resta():
    resultado.set(float(entrada1.get()) - float(entrada2.get()))

def multiplicacion():
    resultado.set(float(entrada1.get()) * float(entrada2.get()))

def division():
    resultado.set(float(entrada1.get()) / float(entrada2.get()))


root = tk.Tk()
root.title("Calculadora")


etiqueta1 = tk.Label(root, text="Número 1:")
entrada1 = tk.Entry(root)

etiqueta2 = tk.Label(root, text="Número 2:")
entrada2 = tk.Entry(root)

etiqueta_resultado = tk.Label(root, text="Resultado:")
resultado = tk.StringVar()
salida_resultado = tk.Label(root, textvariable=resultado)

boton_suma = tk.Button(root, text="Sumar", command=suma)
boton_resta = tk.Button(root, text="Restar", command=resta)
boton_multiplicacion = tk.Button(root, text="Multiplicar", command=multiplicacion)
boton_division = tk.Button(root, text="Dividir", command=division)


etiqueta1.grid(row=0, column=0)
entrada1.grid(row=0, column=1)

etiqueta2.grid(row=1, column=0)
entrada2.grid(row=1, column=1)

etiqueta_resultado.grid(row=2, column=0)
salida_resultado.grid(row=2, column=1)

boton_suma.grid(row=3, column=0)
boton_resta.grid(row=3, column=1)
boton_multiplicacion.grid(row=4, column=0)
boton_division.grid(row=4, column=1)


root.mainloop()

