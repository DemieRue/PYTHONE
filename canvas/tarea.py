import tkinter as tk

root = tk.Tk()
root.title("Mover texto con eventos de ratón")
canvas = tk.Canvas(root, width=400, height=300, bg="black")
canvas.pack()

def move_text(event):
    if event.num == 1:  
        canvas.move(text_id, -10, 0)
    elif event.num == 3:  
        canvas.move(text_id, 10, 0)
    elif event.num == 2:  
        canvas.coords(text_id,200,150)

text_id = canvas.create_text(200, 150, text="Rodrigo Silva", font=("Arial Bold", 35), fill="white")

canvas.bind("<Button-1>", move_text)  
canvas.bind("<Button-3>", move_text)  
canvas.bind("<Button-2>", move_text)  

root.mainloop()
