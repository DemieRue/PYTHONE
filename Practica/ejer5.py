# Realizar un programa que pida una cadena y un 
# carácter por teclado (valida que sea un carácter)
# y muestra cuantas veces aparece el carácter en la cadena.
"""cadena = input("Ingrese una cadena de caracteres: ")
caracter = input("Ingrese un caracter: ")

if len(caracter) != 1:
    print("Debe ingresar un solo caracter.")
else:
    contador = 0
    for letra in cadena:
        if letra == caracter:
            contador += 1

    print(f"El caracter '{caracter}' aparece {contador} veces en la cadena '{cadena}'.")"""

n=str(input("Ingrese una cadena : "))
r=str(input("Ingrese el caracter : "))
cad=n
c=0
for x in cad:
    if x==r:
        c=c+1
print("La cantidad de : ",r,"que hay en : ",cad,"es : ",c)

