import tkinter as tk

def draw_star(event):
    x, y = event.x, event.y
    canvas.create_line(x-10, y-10, x+10, y+10)
    canvas.create_line(x+10, y-10, x-10, y+10)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()
canvas.bind('<Button-1>', draw_star)
root.mainloop()