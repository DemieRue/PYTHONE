#OPERACIONES ARITMETICAS CON MENU
def suma(a,b):                                                                                                                                                                                        
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

while True:
    print("***MENU PRINCIPAL***")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opc = input("Ingrese una opcion:: ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    num1=int(input("Ingrese primer valor: "))
    num2=int(input("Ingrese segundo valor: "))
    
    if opc=="1":
        print("la suma es: ",suma(num1,num2))

    elif opc=="2":
        print("la resta es: ",resta(num1,num2))
    
    elif opc=="3":
        print("la multiplicacion es: ",multiplicacion(num1,num2))
    
    elif opc=="4":
        print("la divison es: ",division(num1,num2))

    else:
        print("Opcion Invalida!!!")
