#ejercioc de la practica nro 11
N=int(input("Introduzca un nro para N:"))
for f in range(N):
    for c in range(N):
        if f<c:
            print("+",end='  ')
        else:
            print("*",end='  ')
    print("")
