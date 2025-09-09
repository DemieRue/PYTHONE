import tkinter as tk
#creamos objeto de la clase tk
ventana=tk.Tk()
#tamaño
ancho=900
alto=200
tamaño=str(ancho)+"x"+str(alto)
ventana.geometry(tamaño)
#titulo
ventana.title('Titulo de la ventana')
#icono
ventana.iconbitmap("C:\\Users\\alque\\Documents\\PYTHON\\classAuxi\\icono1.ico")
#poner siempre al final
ventana.mainloop()