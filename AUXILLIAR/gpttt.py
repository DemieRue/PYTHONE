# multiplicacion sin operador 
# ingresar numeros por teclado

def multiplicar(x,y):
    if y == 0:
        return 0
    else:
        return x + multiplicar(x, y-1)
    
x = int(input("Introduce el primer numero: "))
y = int(input("Introduce el segundo numero: "))
print("La multiplicación de los dos números es:",multiplicar(x,y))