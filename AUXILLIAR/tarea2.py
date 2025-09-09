#UNIV RODRIGO SILVA MAMANI TAREA 2
# INTRODUCIR POR TECLADO N NUMEROS Y MOSTRAR CUANTOS PARES E IMPARES

n=int(input("Cuantos numeros desea introducir : "))

contador_pares = 0
contador_de_impares = 0
c = 0

while c<n:
    x=int(input("Introduzca un numero : "))
    if x % 2 == 0:
        contador_pares += 1
    else:
        contador_de_impares += 1
    c += 1
print("Cantidad de numeros pares : ",contador_pares)
print("Cantidad de numeros impares : ",contador_de_impares)