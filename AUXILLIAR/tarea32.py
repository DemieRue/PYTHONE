
lab= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
la = []
for i in range(len(lab)):
    if (i%4)!=0:
        la += lab[i]

print(la)