from tkinter import *

def move_left(event):
    canvas.move(text, -10, 0)

def move_right(event):
    canvas.move(text, 10, 0)

def move_center(event):
    canvas.coords(text, 200, 100)

root = Tk()
canvas = Canvas(root, width=400, height=200)
canvas.pack()

text = canvas.create_text(200, 100, text="Rodrigo Silva", font=("Arial", 20))

canvas.bind("<Button-1>", move_left)
canvas.bind("<Button-3>", move_right)
canvas.bind("<Button-2>", move_center)

root.mainloop()