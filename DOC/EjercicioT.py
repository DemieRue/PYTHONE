#ejercicio 2 de datagrama
N=int(input("Introduzca un nro para N:"))
M=(2*N)-1
t=1
for f in range(N):
    av=1
    for c in range(M):
        #if f+c==N-1 or f+c>=N-1 and av<=t:
        if f+c>=N-1 and av<=t:
            print("X",end='  ')
            av=av+1
        else:
            print(" ",end='  ')
    print("")
    t=t+2
