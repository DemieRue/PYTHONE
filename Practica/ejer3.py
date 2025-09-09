# Realizar un programa que pida tres números y 
# mostrarlos ordenados de mayor a menor.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("El orden es : ",num1,",",num2,",", num3)
    else:
        print("El orden es : ",num1,",",num3,",", num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("El orden es : ",num2,",", num1,",", num3)
    else:
        print("El orden es : ",num2,",", num3,",", num1)
else:
    if num1 >= num2:
        print("El orden es : ",num3,",", num1,",", num2)
    else:
        print("El orden es : ",num3,",", num2,",", num1)
