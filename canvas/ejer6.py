from tkinter import *


window = Tk()
canvas = Canvas(window, width=500, height=200, bg="black")
canvas.pack()


text = canvas.create_text(250, 100, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white")


distance = 0


def move_text(event):
    global distance
    
    if event.num == 1:
        distance = -10
    
    elif event.num == 2:
        distance = 250 - canvas.coords(text)[0]
    
    elif event.num == 3:
        distance = 10
    
    canvas.move(text, distance, 0)


canvas.tag_bind(text, "<Button-1>", move_text)
canvas.tag_bind(text, "<Button-2>", move_text)
canvas.tag_bind(text, "<Button-3>", move_text)


window.mainloop()