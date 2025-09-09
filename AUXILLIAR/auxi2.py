#**********WHILE**************+

#ejemplo1: 
i=1
while i<=10:
    print("Ejecucion"+str(i)) #str nos permite concatenar el mensaje con la variable
    i=i+1  #va incrementando cada vez que ingresa al while

print ("termino la ejecucion")#una vez que i es mayor a 10 sale del bucle e imprime este mensaje



#ejemplo2: 
edad=int(input("Introduce tu edad por favor: "))
while edad<0:
    print("has introducido uan edad negativa. Vuelva a intertarlo")
    edad=int(input("Introduce tu edad por favor: "))

print ("Gracias por colocar,puedes pasar")
print("edad del aspirante: "+str(edad))


#ejemplo3: 
edad=int(input("Introduce tu edad por favor: "))
while edad<5 or edad>100:
    print("has introducido uan edad negativa. Vuelva a intertarlo")
    edad=int(input("Introduce tu edad por favor: "))

print ("Gracias por colocar,puedes pasar")
print("edad del aspirante: "+str(edad))


#ejemplo4:calculamos la raiza cuadrada
import math 
numero=int(input("Introduce tu numero: "))
intentos=0

while numero<0:
    print("no se puede hallar la raiz cuadrada de un numero negativo")
    if intentos==2:
        print("has consumido demasiados intentos,el programa ha finalizado")
        break; #nos permite parar el bucle por completo
    
    numero=int(input("Introduce tu numero: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print ("la raiz cuadrada de "+str(numero)+" es "+ str(solucion))



#***********continue,pass y else**********
#ejemplo1:usamos continue 
nombre="juan perez"

contador=0
print(len(nombre))
for i in nombre:
    if i==" ":
        continue # obia el espacio
    contador+=1

print(contador)


#ejemplo2:usamos pass
while True:
    pass 

#para poder salir del bucle infinito presionamos crtl+c




#ejemplo3:usamos else
email=input("ingrese su correo : ")

for i in email:
    if i=="@":
        arroba=True
        break;

else:
    arroba=False
print(arroba)