import tkinter as tk

# Create a window
root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Graphics Primitives')

# Create a canvas
canvas = tk.Canvas(root, width= 600, height= 400, bg= 'white')
canvas.pack(anchor=tk.CENTER, expand= True)

# Define the coordinates of the graphics primitives
line_coords = (100, 100, 500, 100)
rect_coords = (200, 150, 400, 250)
circle_coords = (300, 300, 400, 400)
triangle_coords = (100, 300, 200, 200, 300, 300)
oval_coords = (200, 350, 400, 450)

# Create buttons to display the graphics primitives
def show_line():
    canvas.create_line(*line_coords)

def show_rect():
    canvas.create_rectangle(*rect_coords)

def show_circle():
    canvas.create_oval(*circle_coords)

def show_triangle():
    canvas.create_polygon(*triangle_coords)

def show_oval():
    canvas.create_oval(*oval_coords)

button_line = tk.Button(root, text="Show Line", command=show_line)
button_rect = tk.Button(root, text="Show Rectangle", command=show_rect)
button_circle = tk.Button(root, text="Show Circle", command=show_circle)
button_triangle = tk.Button(root, text="Show Triangle", command=show_triangle)
button_oval = tk.Button(root, text="Show Oval", command=show_oval)

# Place the buttons at the bottom of the window
button_line.place(x=100, y=500)
button_rect.place(x=200, y=500)
button_circle.place(x=300, y=500)
button_triangle.place(x=400, y=500)
button_oval.place(x=500, y=500)

# Start the main loop
root.mainloop()