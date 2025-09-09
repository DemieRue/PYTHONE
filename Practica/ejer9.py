# Realizar un programa que invierta un número introducido por 
# teclado. Debe solicitar un valor entero y mostrar el mismo 
# número con sus cifras invertidas. Si el
# número es negativo debe seguir siéndolo. 


n=int(input("Inegrese un numero : "))
r=0
if n>0:
    while n!=0:
        c=n%10
        r=r*10+c
        n=n//10
else:
    n=n*(-1)
    while n!=0:
        c=n%10
        r=r*10+c
        n=n//10
    r=r*(-1)
print("El numero invertido es : ",r)

