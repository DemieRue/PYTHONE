# Escribir un programa que pidiendo un valor N seguido de N números, 
# calcule el máximo y mínimo de ese conjunto de N números.
lista=[]
minimo=0
maximo=0

num=int(input("¿Cuantos numeros desea ingresar? : "))
i=1
while i<=num:
    n=int(input("Ingrese un numero : "))
    lista.append(n)
    i+=1

for n in lista:
    if n<minimo:
        minimo=n
        
    if n>maximo:
        maximo=n
   
    
print("Lista : ",lista)
print("Mayor : ",maximo)
print("Menor : ",minimo)