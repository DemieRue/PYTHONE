from tkinter import*
vent1=Tk()
def llamando(event):
    aux=str(event.x)+","+str(event.y)
    mensaje.config(text=aux)
    #print("se clickeo en el punto",event.x,event.y)

frame1=Frame(vent1,width=100,height=200)
frame1.bind("<Button-1>",llamando)
frame1.pack()
mensaje=Label(frame1,text=" ----")
mensaje.place(x=20,y=80)
vent1.mainloop()
