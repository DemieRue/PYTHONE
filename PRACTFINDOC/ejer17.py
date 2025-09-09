# Import tkinter module
import tkinter as tk

# Create a root window
root = tk.Tk()

# Create a frame to hold the buttons
frame = tk.Frame(root)

# Create a list of buttons
buttons = ["sala", "comedor", "cocina", "baño", "cuarto1", "cuarto2", "cuarto3", "musica", "ventilador", "tv", "fiesta"]

# Create a dictionary to store the button states
button_states = {}

# Define a function to toggle the button state and show it on the label
def toggle(button):
    # Get the current state of the button
    state = button_states[button]
    # Toggle the state
    state = not state
    # Update the dictionary
    button_states[button] = state
    # Update the label text
    if state:
        label.config(text=f"{button} is on")
    else:
        label.config(text=f"{button} is off")

# Define a function to turn on all the buttons and show it on the label
def turn_on_all():
    # Loop through all the buttons
    for button in buttons:
        # Set the state to True
        button_states[button] = True
    # Update the label text
    label.config(text="All are on")

# Define a function to turn off all the buttons and show it on the label
def turn_off_all():
    # Loop through all the buttons
    for button in buttons:
        # Set the state to False
        button_states[button] = False
    # Update the label text
    label.config(text="All are off")

# Define a function to close the window
def close_window():
    # Destroy the root window
    root.destroy()

# Create a label to show the button status
label = tk.Label(root, text="Welcome to home automation control")
label.pack()

# Loop through the buttons and create them on the frame
for button in buttons:
    # Initialize the button state to False
    button_states[button] = False
    # Create a tkinter button with the name and a command to toggle it
    b = tk.Button(frame, text=button, command=lambda x=button: toggle(x))
    # Pack the button on the frame
    b.pack(side=tk.LEFT)

# Create three main buttons on the root window
turn_on_button = tk.Button(root, text="Encender todos", command=turn_on_all)
turn_off_button = tk.Button(root, text="Apagar todos", command=turn_off_all)
close_button = tk.Button(root, text="Cerrar ventana", command=close_window)

# Pack the main buttons on the root window
turn_on_button.pack()
turn_off_button.pack()
close_button.pack()

# Pack the frame on the root window
frame.pack()

# Start the main loop of the root window
root.mainloop()