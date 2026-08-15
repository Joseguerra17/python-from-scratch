#Lista (se puede modificiar)
lista = ["José Guerra","17 Años",1,69] 

#tupla (no se puede modificar) son inmutables, y siguen el orden ya establecido
tupla = ("José Guerra","17 Años",1,69)

#esto es valido, ya que la lista se puede modificar y se le pueden asignar nuevos datos
#lista[0] = "Juanito"

#esto no es valido, ya que las tuplas no se pueden modificar, solo respetan los datos ya establecidos
#tupla[0] = "Juanito"

#creando un conjunto (set)

#no almacena datos duplicados, tampoco se puede acceder a los datos/elementos del conjunto por el indice
conjunto = {"Juanito", 17, 1,69}

#print(conjunto[2]) > no puede acceder al dato/elemento

#creando un diccionario (dict) (la estructura del diccionario es key : value) y se va separando por coma, menos en el ultimo dato/elemento 

diccionario = {
    'nombre' : "José Guerra",
    'edad' : 17,
    'altura' : 1.69
}

print(diccionario['nombre']) #para imprimir los datos/elementos del diccionario se pide directamente el elemento, no como en las listas que pedimos el indice
