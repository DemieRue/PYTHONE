# INGRESAR UN NUMERO SI ES PAR ELEVAR AL CUADRADO
# SI ES IMPAR MOSTAR SU ESPONENCIAL
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es Par")
    y=numero**2
    print("Y al Cuadrado es: ",y)
else:
    print("El número es Impar")
    ex=2.718281828
    x=ex**numero
    print("Y el Exponencial es: ",x)

#ex=2.718281828
#x=int(input("ingrese el numero exponencial: "))
#r=ex**x
#print("resultado: ",r)

#numero = int(input("Ingresa un número: "))
#if numero & 1 == 0:
#    print("El número es par")
#else:
#    print("El número es impar")

