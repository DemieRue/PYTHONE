#MOSTRAR EN LA LISTA SOLO LOS MULTIPLOS DE 4

lab= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
counter = [i for i in range(len(lab)) if i%4==0][1:]
la = []
for i in range(1,len(lab)):
    if i not in counter:
        la.append(lab[i-1])
print(f'{la}')
