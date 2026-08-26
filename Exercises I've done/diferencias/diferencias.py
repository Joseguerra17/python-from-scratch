def diferencias(lista1, lista2):
    nueva_lista = []
    for indice, elemento_list in enumerate(lista1):
        elemento = lista2[indice]
        diferencia = elemento_list - elemento
        nueva_lista.append(diferencia)
    return nueva_lista

resultado = diferencias([10, 20, 30], [3, 5, 10])
print(resultado)