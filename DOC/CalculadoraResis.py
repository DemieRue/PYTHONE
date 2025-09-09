#calladora de codigo de colores
from tkinter import*
from tkinter import ttk

ventana=Tk()
ventana.title("CODIGO DE COLORES")
ventana.geometry("700x400")

valor1=int(0)
valor2=int(0)
valor3=int(0)
valor4=int(0)
aux1=""
aux2=""
aux3=""
tol=""
tp=""
def seleccion1():
    global valor1      #estas variables deben ser globales
    global aux1
    aux1=lcolor1.get()
    if aux1=="Negro":
        valor1=0
    elif aux1=="Cafe":
        valor1=1
    elif aux1=="Rojo":
        valor1=2
    elif aux1=="Naranja":
        valor1=3
    elif aux1=="Amarillo":
        valor1=4
    elif aux1=="Verde":
        valor1=5
    elif aux1=="Azul":
        valor1=6
    elif aux1=="Morado":
        valor1=7
    elif aux1=="Gris":
        valor1=8
    elif aux1=="Blanco":
        valor1=9
def seleccion2():
    global valor2
    global aux2
    aux2=lcolor2.get()
    if aux2=="Negro":
        valor2=0
    elif aux2=="Cafe":
        valor2=1
    elif aux2=="Rojo":
        valor2=2
    elif aux2=="Naranja":
        valor2=3
    elif aux2=="Amarillo":
        valor2=4
    elif aux2=="Verde":
        valor2=5
    elif aux2=="Azul":
        valor2=6
    elif aux2=="Morado":
        valor2=7
    elif aux2=="Gris":
        valor2=8
    elif aux2=="Blanco":
        valor2=9
def seleccion3():
    global valor3
    global aux3
    aux3=lcolor3.get()
    if aux3=="Negro":
        valor3=1
    elif aux3=="Cafe":
        valor3=10
    elif aux3=="Rojo":
        valor3=100
    elif aux3=="Naranja":
        valor3=1000
        
def seleccion4():
    global tol
    global valor4
    tol=lcolort.get()
    if tol=="Ninguno":
        valor4=0
    elif tol=="Cafe":
        valor4=0.01
        tp="1%"
    elif tol=="Rojo":
        valor4=0.02
        tp="2%"
    elif tol=="Verde":
        valor4=0.005
        tp="0.05%"
def resultado():
    seleccion1()
    seleccion2()
    seleccion3()
    seleccion4()
    valorG=str(valor1)+str(valor2)
    x1=float(valor3)
    y1=float(valorG)
    valorT=float(x1*y1)
    Eresultado.delete(0,END)
    Eresultado.insert(0,valorT)

    #calculo para la tolerancia
    vmax=valorT+(valorT*(float(valor4)))
    vmin=valorT-(valorT*(float(valor4)))
    Etmax.delete(0,END)
    Etmax.insert(0,vmax)

    Etmin.delete(0,END)
    Etmin.insert(0,vmin)
    
#creacion de listas
color=["Negro","Cafe","Rojo","Naranja","Amarillo","Verde","Azul","Morado","Gris","Blanco"]
tolerancia=["Cafe","Rojo","Verde","Azul","Morado","Gris","Dorado","Plata"]

#listas
lcolor1=ttk.Combobox(ventana,width=10,state='readonly')
lcolor1.place(x=100,y=80)
lcolor1.set("Negro")
#cargar los valores a la lista
lcolor1['values']=color

lcolor2=ttk.Combobox(ventana,width=10,state='readonly')
lcolor2.place(x=200,y=80)
lcolor2.set("Negro")
lcolor2['values']=color

lcolor3=ttk.Combobox(ventana,width=10,state='readonly')
lcolor3.place(x=310,y=80)
lcolor3.set("Negro")
lcolor3['values']=color

lcolort=ttk.Combobox(ventana,width=10,state='readonly')
lcolort.place(x=410,y=80)
lcolort.set("Ninguno")
lcolort['values']=tolerancia

#boton resultado
botonr=Button(ventana,text="RESULTADO",bg='yellow',command=resultado)
botonr.place(x=10,y=140)

#caja de texto
Eresultado=Entry(ventana)
Eresultado.place(x=90,y=140)

#para la tolerancia
tole=Label(ventana,text="TOLERANCIA")
tole.place(x=380,y=180)

Etmax=Entry(ventana)
Etmax.place(x=460,y=180)
tma=Label(ventana,text="Max.")
tma.place(x=610,y=180)

Etmin=Entry(ventana)
Etmin.place(x=460,y=210)
tmi=Label(ventana,text="Min.")
tmi.place(x=610,y=210)

ventana.mainloop()
