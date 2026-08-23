def suma_positivos(lista):
    suma_positivos_list = []
    for num in (lista):
        if num >= 0:
            suma_positivos_list.append(num)
    suma = sum(suma_positivos_list)
    return suma

resultado = suma_positivos([5,6,2,6,-5,-10,-15])
print(resultado)

#Forma Alternativa de hacerlo mas Directo
def suma_positivos(lista):
    suma = 0
    for num in (lista):
        if num >= 0:
            suma = suma + num
    return suma

resultado = suma_positivos([5,22,35,15,125,124,-5,-1234,-14,-2,41])
print(resultado)