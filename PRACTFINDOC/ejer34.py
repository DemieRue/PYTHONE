import tkinter as tk

# create a root window
root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Graphics Primitives')

# create a canvas widget
canvas = tk.Canvas(root, width= 600, height= 400, bg= 'white')
canvas.pack(anchor=tk.CENTER, expand= True)

# define functions to draw shapes on canvas
def draw_line():
    # draw a line from (100, 100) to (500, 100) with red color and 5 pixels width
    canvas.create_line(100, 100, 500, 100, fill='red', width=5)

def draw_rectangle():
    # draw a rectangle with top-left corner at (200, 200) and bottom-right corner at (400, 300) with blue fill and black outline
    canvas.create_rectangle(200, 200, 400, 300, fill='blue', outline='black')

def draw_circle():
    # draw a circle with center at (300, 200) and radius of 100 pixels with green fill and no outline
    canvas.create_oval(200, 100, 400, 300, fill='green', outline='')

def draw_triangle():
    # draw a triangle with vertices at (100, 300), (200, 200), and (300, 300) with yellow fill and black outline
    canvas.create_polygon(100, 300, 200, 200, 300, 300, fill='yellow', outline='black')

def draw_oval():
    # draw an oval with bounding box at (400, 200), (600, 400) with purple fill and no outline
    canvas.create_oval(400, 200, 600, 400, fill='purple', outline='')

# create buttons for each shape and bind them to functions
line_button = tk.Button(root, text='Line', command=draw_line)
line_button.pack(side=tk.LEFT)

rectangle_button = tk.Button(root, text='Rectangle', command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT)

circle_button = tk.Button(root, text='Circle', command=draw_circle)
circle_button.pack(side=tk.LEFT)

triangle_button = tk.Button(root, text='Triangle', command=draw_triangle)
triangle_button.pack(side=tk.LEFT)

oval_button = tk.Button(root, text='Oval', command=draw_oval)
oval_button.pack(side=tk.LEFT)

# run the window
root.mainloop()