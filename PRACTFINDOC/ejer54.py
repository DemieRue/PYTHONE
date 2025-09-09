import tkinter as tk
import math

# Create a window and a canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Define a function that draws a rectangle on the canvas
def draw_rectangle(x, y, size):
    # Calculate the coordinates of the top left and bottom right corners
    x1 = x - size / 2
    y1 = y - size / 2
    x2 = x + size / 2
    y2 = y + size / 2
    # Delete any previous rectangle on the canvas
    canvas.delete("rect")
    # Create a new rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", tag="rect")

# Define a function that animates the rectangle by changing its size and position
def animate_rectangle(x, y, size, angle):
    # Calculate the new size and position based on the angle
    new_size = size * math.sin(angle)
    new_x = x + size * math.cos(angle)
    new_y = y + size * math.sin(angle)
    # Draw the rectangle with the new parameters
    draw_rectangle(new_x, new_y, new_size)
    # Increase the angle by a small amount
    new_angle = angle + 0.05
    # Repeat the animation after 10 milliseconds with the new angle
    window.after(10, animate_rectangle, x, y, size, new_angle)

# Call the animation function with the initial parameters
animate_rectangle(250, 250, 100, 0)

# Start the main loop of the window
window.mainloop()