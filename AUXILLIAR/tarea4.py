#Realizar un programa que permita leer n valores desde teclado mostrar el promedio
#de los pares mayores a 10 y menores a 98.

n=int(input("Ingrese la cantidad de numeros : "))
suma=0
li=[]
c=0
i=1
while(i<=n):
    print("Ingrese el numero : ",i)
    num=int(input())
    if num % 2 == 0:
        if num >= 10 and num <= 98:
            suma=suma+num
            li.append(num)
            c+=1
    i+=1
prom=round(suma/c,2)
print("Estos son los numeros pares mayores a 10 y menores a 98 : ",li)
print("Y el promedio entre ellos es : ",prom)