def contador_pares(lista):
    lista_vacia = []
    for numero in (lista): #Bucle que revisa cada elemento de la lista
        if numero%2==0: #Condicion que revisa en este caso si el numero es PAR
            lista_vacia.append(numero) #Si la condicion se cumple entonces lo agrega a la nueva lista
    return lista_vacia #me devuelve la informacion de la lista
    

par_o_impar = contador_pares([1,2,3,4,5,6])
print(f"Los pares son: {par_o_impar}")

def alumnos_aprobados(nombres,notas):
    alumnos_lista = []
    for indice, nombre in enumerate(nombres):
        nota_actual = notas[indice]
        if nota_actual >= 60:
            alumnos_lista.append((nombre, nota_actual))
    return alumnos_lista

resultado = alumnos_aprobados(["Jose Guerra","Emiliano"],[67,78])
print(resultado)