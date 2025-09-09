# UNIV. RODRIGO SILVA MAMANI

import tkinter as tk

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=400, height=400)
ventana.title("Crecimiento y Decrecimiento Rectangulo")
canvas.pack()

rectangulo = canvas.create_rectangle(150, 150, 250, 250, fill="red")

def cre_y_decre(event):
    
    if event.keysym == "plus":
        escalar = 1.1
    elif event.keysym == "minus":
        escalar = 0.9
    else:
        return
   
    rx = canvas.winfo_width() / 2
    ry = canvas.winfo_height() / 2

    canvas.scale(rectangulo, rx, ry, escalar, escalar)

ventana.bind("<plus>", cre_y_decre)
ventana.bind("<minus>", cre_y_decre)

ventana.mainloop()