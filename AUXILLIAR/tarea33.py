def funcion():
        abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in range(len(abc)):
            print(f'numero i: {i} tamano de la lista {len(abc)}')
            if i%3==0:
                print(i%3)
                abc.remove(abc[i])

funcion()