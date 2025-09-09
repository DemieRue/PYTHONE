import tkinter as tk

def dibujar_asterisco(event):
    if event.num == 1:  # Verificar si se hizo clic izquierdo
        #canvas.delete("asterisco")   Borrar el asterisco anterior

        x = event.x
        y = event.y

        # Dibujar las líneas del asterisco
        canvas.create_line(x, y - 15, x, y + 15, tags="asterisco")  # Línea vertical
        canvas.create_line(x - 25, y, x + 25, y, tags="asterisco")  # Línea horizontal
        canvas.create_line(x - 10, y - 10, x + 10, y + 10, tags="asterisco")  # Línea diagonal ascendente
        canvas.create_line(x - 10, y + 10, x + 10, y - 10, tags="asterisco")  # Línea diagonal descendente

# Crear la ventana
ventana = tk.Tk()

# Crear el lienzo (canvas) para dibujar
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()

# Configurar el evento de clic izquierdo
canvas.bind("<Button-1>", dibujar_asterisco)

# Mostrar la ventana
ventana.mainloop()