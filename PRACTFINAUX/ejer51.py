from tkinter import Tk, Canvas

window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()

# initial coordinates of the oval
x0 = 100
y0 = 75
x1 = 200
y1 = 125

# draw the oval for the first time
oval = canvas.create_oval(x0, y0, x1, y1)

# define a function to update the oval
def update_oval():
    global x0, y0, x1, y1, oval
    # clear the previous oval
    canvas.delete(oval)
    # change the coordinates by a random amount
    x0 += random.randint(-10, 10)
    y0 += random.randint(-10, 10)
    x1 += random.randint(-10, 10)
    y1 += random.randint(-10, 10)
    # draw the new oval
    oval = canvas.create_oval(x0, y0, x1, y1)
    # schedule the next update after 100 milliseconds
    canvas.after(100, update_oval)

# start the animation
update_oval()

window.mainloop()