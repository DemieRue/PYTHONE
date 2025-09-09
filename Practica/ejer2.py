# Realizar un programa que permita pedir el día, 
# mes y año de una fecha correcta y mostrar la 
# fecha del día siguiente. suponer que todos 
# los meses tienen 30 días.
# Solicitar al usuario que ingrese la fecha
dia = int(input("Ingrese el día (en formato numérico): "))
mes = int(input("Ingrese el mes (en formato numérico): "))
anio = int(input("Ingrese el año (en formato numérico de cuatro dígitos): "))

# Verificar si la fecha es válida
fecha_valida = True

if mes < 1 or mes > 12:
    fecha_valida = False
elif dia < 1 or dia > 30:
    fecha_valida = False

# Si la fecha no es válida, mostrar un mensaje de error y terminar el programa
if not fecha_valida:
    print("La fecha ingresada no es válida.")
    exit()

# Calcular la fecha del día siguiente
dia_siguiente = dia + 1
mes_siguiente = mes
anio_siguiente = anio

if dia_siguiente > 30:
    dia_siguiente = 1
    mes_siguiente += 1

    if mes_siguiente > 12:
        mes_siguiente = 1
        anio_siguiente += 1

# Mostrar la fecha del día siguiente
print(f"La fecha del día siguiente es: {dia_siguiente}/{mes_siguiente}/{anio_siguiente}")
