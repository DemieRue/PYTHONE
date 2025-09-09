

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
# letras que ocupen 
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#En este lugar contengo todo el abecedario
abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#Puede ser en el for siguiente en donde me sale un error, list index out of range
for i in range(len(abc)):
    if i%3==0:
        #pongo el abc.remove para remover cada vez que el modulo de i%3 sea 0
        abc.remove(abc[i])
#En este apartado imprimo
print(abc)
#Y esto para activar la función
