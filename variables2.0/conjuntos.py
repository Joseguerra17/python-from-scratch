#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato 3"}

#Teoria de conjuntos

conjunto1 = {1,3,5,6,7}
conjunto2 = {1,5,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun (devuelve true solo si en los conjuntos no hay ningun numero/dato igual)
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)