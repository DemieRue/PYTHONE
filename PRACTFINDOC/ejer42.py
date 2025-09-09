from tkinter import Tk, Canvas, mainloop
import math

def circle(canvas, x, y, r, width):
    id = canvas.create_oval(x-r, y-r, x+r, y+r, width=width)
    return id

def asterisk(canvas, x, y, r, width):
    # draw a circle
    circle(canvas, x, y, r, width)
    # draw eight lines
    for i in range(8):
        angle = i * math.pi / 4 # angle in radians
        x1 = x + r * math.cos(angle) # end point of line
        y1 = y + r * math.sin(angle)
        canvas.create_line(x, y, x1, y1, width=width)

w = Canvas(Tk(), width=500, height=500)
w.pack()
# draw an asterisk at (250, 250) with radius 100 and width 3
asterisk(w, 250, 250, 100, 3)
mainloop()