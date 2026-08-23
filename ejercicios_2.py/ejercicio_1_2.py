def contar_pares(num):
    lista_vacia = []
    for numero in (num):
        if numero%2==0:
            lista_vacia.append(numero)
            pares = len(lista_vacia)
        
    return lista_vacia, pares

lista_vacia,pares = contar_pares([2,5,23,1,6,7,10])
print(lista_vacia)
print(f"Hay {pares} pares.")