import tkinter as tk
from tkinter import ttk, Frame, PhotoImage


# creamos objeto de la clase Tk
ventana = tk.Tk()
# tamaño
ancho = 600
alto = 500
tamaño = str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
# titulo
ventana.title('Imagen en Frame')
# icono
# creamos marco
frame = Frame(ventana)
# posicionamos
frame.pack(padx=10, pady=10)
frame.config(bg='orange',width=400,height=300,cursor="pirate",relief="ridge",bd=25) #lightblue
#frame.config(width=400, height=300)
#frame.config(cursor="pirate")  # arrow #pirate
#frame.config(relief="ridge")  # ridge #sunken
#frame.config(bd=25)

# imagen
#dentro de file,deben colocar la direccion de la imagen
#imagen = PhotoImage(file='C:\\Users\\Personal\\Desktop\\Python_2022\\INF_SUP I\\CAP3\\tkinter-main\\logo.png')
#lbl_imagen = ttk.Label(frame, image=imagen).pack()
# poner siempre al final
ventana.mainloop()
