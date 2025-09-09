# Realizar un programa que pida números hasta que se
# teclee uno negativo, y mostrar cuántos números pares
# e impares se han introducido.
# Inicializamos las variables para contar los números pares e impares
num_pares = 0
num_impares = 0

# Empezamos un bucle para pedir números al usuario
while True:
    num = int(input("Introduce un número: "))
    if num < 0:
        # Si se introduce un número negativo, salimos del bucle
        break
    elif num % 2 == 0:
        # Si el número introducido es par, lo contamos
        num_pares += 1
    else:
        # Si el número introducido es impar, lo contamos
        num_impares += 1

# Mostramos los resultados
print("Se han introducido", num_pares, "números pares y", num_impares, "números impares.")
