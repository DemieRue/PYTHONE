#agregar un elemento al final de la lista
nombres_masculinos=["Alvaro","Jacinto","Miguel","Edgar","David"]
print(nombres_masculinos)
nombres_masculinos.append("Jose")
print(nombres_masculinos)

#agregar varios elementos al final de una lista
nombres_masculinos=["Alvaro","Jacinto","Miguel","Edgar","David"]
nombres_masculinos.extend(["Ivan","Jhennis"])
print(nombres_masculinos)

#agregar un elemento en una posicion determinada
nombres_masculinos=["Alvaro","Jacinto","Miguel","Edgar","David"]
nombres_masculinos.insert(5,"Ricky")
print(nombres_masculinos)

#ordenar una lista en reversa(invertir orden)
nombres_masculinos=["Alvaro","Jacinto","Miguel","Edgar","David"]
nombres_masculinos.reverse()
print(nombres_masculinos)

#ordenar una lista sde forma ascendente sort y descendente sort(reverse=true)
nombres_masculinos=["Alvaro","Jacinto","Miguel","Edgar","David"]
nombres_masculinos.sort(reverse=True)
print(nombres_masculinos)

#concatenacion simple
lista1=[1,2,3,4]
lista2=[3,4,5,6,7,8]
lista3=lista1+lista2
print(lista3)
