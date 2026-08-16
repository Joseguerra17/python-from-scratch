diccionario = {
    'nombre' : "José Guerra",
    'edad' : 17,
    'altura' : 1.69
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_Perla = diccionario.get("Perla")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop("edad")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)