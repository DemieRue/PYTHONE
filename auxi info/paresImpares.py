#N NUMEROS DETERMINAR CUANTOS PARES E IMPARES
n=int(input("Intro n: "))
c=0
s=0

for i in range(n):
    x=int(input("Intro un numero: "))
    if(x%2==0):
        c=c+1
    else:
        s=s+1    

print("Pares: ",c)
print("Impraes: ",s)       
