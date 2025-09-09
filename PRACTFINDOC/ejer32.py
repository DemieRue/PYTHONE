import tkinter as tk

class Example (tk.Frame):
  def __init__ (self, parent):
    tk.Frame.__init__ (self, parent)
    # create a canvas
    canvas = tk.Canvas (self, width = 180, height = 500)
    canvas.pack ()
    # create a button for line
    button_line = tk.Button (self, text = "Line", command = self.draw_line)
    button_line_window = canvas.create_window (10, 10, anchor=tk.NW, window=button_line)
    # create a button for rectangle
    button_rect = tk.Button (self, text = "Rectangle", command = self.draw_rect)
    button_rect_window = canvas.create_window (10, 50, anchor=tk.NW, window=button_rect)
    # create a button for circle
    button_circle = tk.Button (self, text = "Circle", command = self.draw_circle)
    button_circle_window = canvas.create_window (10, 90, anchor=tk.NW, window=button_circle)
    # create a button for triangle
    button_triangle = tk.Button (self, text = "Triangle", command = self.draw_triangle)
    button_triangle_window = canvas.create_window (10, 130, anchor=tk.NW, window=button_triangle)
    # create a button for oval
    button_oval = tk.Button (self, text = "Oval", command = self.draw_oval)
    button_oval_window = canvas.create_window (10, 170, anchor=tk.NW, window=button_oval)

  def draw_line (self):
    # draw a line on the canvas
    pass

  def draw_rect (self):
    # draw a rectangle on the canvas
    pass

  def draw_circle (self):
    # draw a circle on the canvas
    pass

  def draw_triangle (self):
    # draw a triangle on the canvas
    pass

  def draw_oval (self):
    # draw an oval on the canvas
    pass


root = tk.Tk ()
Example (root).pack ()
root.mainloop ()