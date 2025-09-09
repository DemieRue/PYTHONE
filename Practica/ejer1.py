# Realizar un programa que pida dos numeros y mostrar un
# mensaje )si uno es multiplo del otro.
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 % numero2 == 0:
    print(numero1, "es múltiplo de", numero2)
elif numero2 % numero1 == 0:
    print(numero2, "es múltiplo de", numero1)
else:
    print("Los números no son múltiplos entre sí.")
