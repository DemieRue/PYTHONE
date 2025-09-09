import tkinter as tk

def scale_rect(value):
    global width, height
    width = int(value)
    height = int(value)
    
    canvas.delete("rectangle")
    x1 = (canvas_width - width) / 2
    y1 = (canvas_height - height) / 2
    x2 = x1 + width
    y2 = y1 + height
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="rectangle")

root = tk.Tk()
root.title("Simulación de crecimiento y decrecimiento de un rectángulo")

canvas_width = 400
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

width = 10
height = 10

x1 = (canvas_width - width) / 2
y1 = (canvas_height - height) / 2
x2 = x1 + width
y2 = y1 + height
canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="rectangle")

slider = tk.Scale(root, from_=10, to=250, orient="horizontal", command=scale_rect)
slider.pack()

root.mainloop()
