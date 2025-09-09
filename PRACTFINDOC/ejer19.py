import tkinter as tk

# Create the main ventana
ventana = tk.Tk()
ventana.title("GUI Example")

# Create a frame to hold the buttons
frame = tk.Frame(ventana)
frame.pack()

# Create a dictionary to store the boton states
estado_boton = {}

# Define a function to toggle the boton estado and color
def color_boton(boton):
    # Get the current estado of the boton
    estado = estado_boton[boton]
    # Toggle the estado
    estado = not estado
    # Update the dictionary
    estado_boton[boton] = estado
    # Change the color of the boton based on the estado
    if estado:
        boton.config(bg="lime")
    else:
        boton.config(bg="red")

# Define a function to turn on all the buttons
def encender_todo():
    # Loop through all the buttons
    for boton in estado_boton:
        # Set the estado to True
        estado_boton[boton] = True
        # Change the color to green
        boton.config(bg="lime")

# Define a function to turn off all the buttons
def apagar_todo():
    # Loop through all the buttons
    for boton in estado_boton:
        # Set the estado to False
        estado_boton[boton] = False
        # Change the color to red
        boton.config(bg="red")

# Define a list of boton names
botones = ["sala", "comedor", "cocina", "baño", "cuarto1", "cuarto2", "cuarto3", "musica", "ventilador", "tv", "fiesta"]

# Create and pack the buttons using a loop
for nombre in botones:
    # Create a boton with the nombre as text
    boton = tk.Button(frame, text=nombre)
    # Pack the boton in a grid layout
    boton.grid(row=0, column=botones.index(nombre))
    # Bind the boton to the toggle function
    boton.bind("<Button-1>", lambda event, b=boton: color_boton(b))
    # Initialize the boton estado to False
    estado_boton[boton] = False

# Create and pack the main buttons
encender = tk.Button(ventana, text="Encender todos", command=encender_todo)
encender.pack(side=tk.LEFT)

apagar = tk.Button(ventana, text="Apagar todos", command=apagar_todo)
apagar.pack(side=tk.RIGHT)

cerrar = tk.Button(ventana, text="Cerrar ventana", command=ventana.destroy)
cerrar.pack(side=tk.BOTTOM)

# Start the main loop
ventana.mainloop()