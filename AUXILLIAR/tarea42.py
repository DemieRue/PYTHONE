# Realizar la operación de multiplicación a×b de 
# dos valores enteros positivos con sumas.

a=int(input("Ingrese un numero positivo : "))
b=int(input("Ingrese un numero positivo : "))
multi=0
while a<0 or b<0:
    print("Son Numeros Negativos")
    print("Ingrese Dos Numeros Posistivos : ")
    a=int(input("Ingrese un numero positivo : "))
    b=int(input("Ingrese un numero positivo : "))

for c in range(1,b+1,1):
    multi=multi+a
print("La Multiplicacion es : ",multi)
