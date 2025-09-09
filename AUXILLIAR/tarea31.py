def funcion():

    abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    #Necesitamos saber cuál es la cantidad total de abecedario que será al final. Para eso divido 27/3 = 9. 
    # En esos 9 contamos inclusive el 0
    abcd= len(abc) - int(len(abc)/3)
    #Coloco la función de abcd en el for loop para que ahora si el index este dentro de rango:
    for i in range(0,abcd):
        if i%3==0:

            abc.remove(abc[i])

    print(abc)

funcion()