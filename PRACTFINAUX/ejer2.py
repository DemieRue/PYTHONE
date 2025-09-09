from tkinter import *
from tkinter import messagebox

def verificar_acceso():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    
    if usuario == "rodrigo" and contrasena == "informaticauno":
        messagebox.showinfo("Acceso Permitido", "¡Bienvenido!")
    else:
        messagebox.showerror("Acceso No Permitido", "Usuario o contraseña incorrectos")


ventana = Tk()
ventana.title("Acceso")
ventana.geometry("400x200")


label_usuario = Label(ventana, text="Usuario:")
label_usuario.pack()
entry_usuario = Entry(ventana)
entry_usuario.pack()

label_contrasena = Label(ventana, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = Entry(ventana, show="*")  
entry_contrasena.pack()

button_acceder = Button(ventana, text="Acceder", command=verificar_acceso)
button_acceder.pack()


ventana.mainloop()
