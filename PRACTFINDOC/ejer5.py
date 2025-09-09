import tkinter as tk

def animate():
    global width, height, growing
    canvas.delete("rectangle")
    
    if growing:
        width += 5
        height += 5
        if width >= 200:
            growing = False
    else:
        width -= 5
        height -= 5
        if width <= 50:
            growing = True
    
    x1 = (canvas_width - width) / 2
    y1 = (canvas_height - height) / 2
    x2 = x1 + width
    y2 = y1 + height
    
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="rectangle")
    
    root.after(50, animate)

root = tk.Tk()
root.title("Simulación de crecimiento y decrecimiento de un rectángulo")

canvas_width = 400
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

width = 50
height = 50
growing = True

animate()

root.mainloop()