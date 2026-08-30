#Creando una lista con list()
lista = list(["Hola", 17, "Perro"])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#append agrega elementos a la lista
lista.append("Juanito")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "Jacinta")

#agregando varios elementos a la lista / basicamente agregar una lista detras de la otra
lista.extend(["Lola",2026])

#eliminando un elemento de la lista por su indice / con -1 eliminas el ultimo dato/elemento de la lista, con -2 eliminas el penultimo y asi sucesivamente
lista.pop(0)

#removiendo un elemento de la lista por su valor/dato/elemento
lista.remove("Jacinta")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True invierte los datos/elementos) No soporta str
#lista.sort()

#invirtiendo los elementos de una lista, funciona en cualquier lista
#lista.reverse()

print(lista[1])