#interfaz de calculo de operaciones basicas
from tkinter import *
ventana=Tk()
ventana.title("OPERACIONES BASICAS")
marco=Frame()
marco.grid(row=0, column=0)

label1=Label(marco,text="SUMA,RESTA, MULTIPLICAION Y DIVISION")
label1.grid(row=0,column=0)

label2=Label(marco,text="Digite un nro:")
label2.grid(row=1,column=0)
tnro1=Entry(marco)
tnro1.grid(row=1,column=1)

label3=Label(marco,text="Digite un nro:")
label3.grid(row=2,column=0)
tnro2=Entry(marco)
tnro2.grid(row=2,column=1)

labelr=Label(marco,text="Resultado:")
labelr.grid(row=3,column=0)
tres=Entry(marco)
tres.grid(row=3,column=1)
#funciones
def suma():
    n1=float(tnro1.get())
    n2=float(tnro2.get())
    s=str(n1+n2)
    tres.delete(0,END)
    tres.insert(0,s)
def resta():
    n1=float(tnro1.get())
    n2=float(tnro2.get())
    s=str(n1-n2)
    tres.delete(0,END)
    tres.insert(0,s)
    
marcob=Frame()
marcob.grid(row=1, column=0)

bsuma=Button(marcob,text="Suma",command=suma)
bsuma.grid(row=0,column=0)

bresta=Button(marcob,text="Resta",command=resta)
bresta.grid(row=0,column=1)

bresta=Button(marcob,text="Multiplicacion")
bresta.grid(row=0,column=2)

bresta=Button(marcob,text="División")
bresta.grid(row=0,column=3)

ventana.mainloop()
