def mayores_a(lista, limite):
    mayores_al_limit = []
    for num in (lista):
        if num > limite:
            mayores_al_limit.append(num)
    return mayores_al_limit

resultado = mayores_a([1,2,3,4,5,6,7,8,9,10],3)
print(resultado)