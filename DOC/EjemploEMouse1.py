#ejemplo de uso de evento mouse
from tkinter import *
vent1=Tk()
vent1.title("Ejemplo de evento Mouse")
def llamar(event):
    #print("Se clickeo en el punto:",event.x,event.y)
    aux="Click en: "+str(event.x)+","+str(event.y)
    lmensaje1.config(text=aux)   #para cambiar el texto en label es mediante el config

frame1=Frame(vent1,width=200,height=300)
frame1.bind("<Button-1>",llamar)
frame1.pack()
lmensaje1=Label(frame1,text="aqui ira el mensaje")
lmensaje1.place(x=100,y=100)
vent1.mainloop()
