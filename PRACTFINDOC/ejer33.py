import turtle
import tkinter as tk

def draw_line():
    turtle.pendown()
    turtle.forward(50)

def draw_rectangle():
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)

def draw_circle():
    turtle.pendown()
    turtle.circle(50)

def draw_triangle():
    turtle.pendown()
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)

def draw_oval():
    turtle.pendown()
    for i in range(2):
        turtle.circle(50, 90)
        turtle.circle(10, 90)

root = tk.Tk()

line_button = tk.Button(root, text="Línea", command=draw_line)
line_button.pack()

rectangle_button = tk.Button(root, text="Rectángulo", command=draw_rectangle)
rectangle_button.pack()

circle_button = tk.Button(root, text="Círculo", command=draw_circle)
circle_button.pack()

triangle_button = tk.Button(root, text="Triángulo", command=draw_triangle)
triangle_button.pack()

oval_button = tk.Button(root, text="Óvalo", command=draw_oval)
oval_button.pack()

root.mainloop()