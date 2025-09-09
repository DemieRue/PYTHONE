# INGRESAR 3 NUMEROS DIFERENTES MOSTRAR EL MENOR DE ELLOS
# SINO SON VOLVER A PEDIR
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
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c
print(f"El numero menor es: {menor}") 