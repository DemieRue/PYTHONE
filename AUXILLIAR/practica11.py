#INGRESAR 3 NUMEROS DIFERENTES SINO SON VOLVER A PEDIR
print("Ingresa 3 Numeros diferentes")
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
while a==b or a==c or b==c:
    print("son numeros repetidos")
    print("Ingresa 3 Numeros diferentes")
    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))
print("son numeros diferentes")