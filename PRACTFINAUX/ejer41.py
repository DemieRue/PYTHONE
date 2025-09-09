# Import tkinter module
import tkinter as tk

# Create a root window
root = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(root, width = 300, height = 300)

# Draw a square
canvas.create_rectangle(50, 50, 150, 150)

# Draw a triangle
canvas.create_polygon(200, 50, 250, 150, 150, 150)

# Pack the canvas into the root window
canvas.pack()

# Start the main loop
root.mainloop()