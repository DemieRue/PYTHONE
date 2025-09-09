# Realizar un programa que permita leer un número y 
# mostrar su cuadrado, repetir el proceso hasta 
# que se introduzca cero.
while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    print("El cuadrado de", numero, "es", numero**2)
