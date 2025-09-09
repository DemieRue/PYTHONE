# Realizar un programa que determine el menor
# de entre grupo de números enteros.
"""n=int(input("Ingrese la cantidad de numeros : "))
a=int(input("Ingrese un numero : "))
g=n

while n!=1:
    b=int(input("Ingrese un numero : "))
    if a>b:
        m=b
        a=m
    else:
        m=a
    n=n-1
print("El numero menor de los ",g,"numeros es el ",m)"""

cantidad = int(input("Ingrese la cantidad de números enteros que desea ingresar: "))

menor = float('inf')

for i in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    if numero < menor:
        menor = numero

print("El número entero menor es:", menor)
