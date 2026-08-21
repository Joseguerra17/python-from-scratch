#forma no optima de sumar valores
#def suma(lista):
    #numeros_sumados = 0 
    #for numero in lista: 
        #numeros_sumados = numeros_sumados + numero
        #return numeros_sumados
    
#resultado = suma([5,3,9,10,20,3])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([5,10])

#utilizando el operador * como argumento (*args) solo funciona cuando el argumento va al final, en este caso suma(nombre,*numeros)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("José",5,5)
print(resultado1)


