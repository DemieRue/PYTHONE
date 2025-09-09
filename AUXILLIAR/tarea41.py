# Realizar un programa que permita ingresar por teclado una cadena 
# la misma que debe ser invertida, mostrar por pantalla ambas cadenas.

s=input("Ingresar Texto : ")
aux=""
i=len(s)-1
while i>=0:
    aux=aux+s[i]
    i=i-1

print(s)
print(aux)