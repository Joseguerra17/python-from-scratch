#creando un diccionario con dict()
diccionario = dict(nombre="Lola",apellido="China") #Forma alternativa de crear un dict() 

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["lola","china"]):"juan"}

#creando un diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","edad"])

print(diccionario)