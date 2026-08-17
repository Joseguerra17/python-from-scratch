
animales = ["perro","gato","loro","cocodrilo"]
numeros = [67,256,375,10]

#recorriendo la lista de animales
#for animal in animales:
    #print(animal)
    
#recorriendo la lista numeros y multiplicando cada valor por 10    
#for numero in numeros:
    #resultado = numero * 10
    #print(resultado)
    
#iterando dos listas del mismo tamaño al mismo tiempo    
#for animal,numero in zip(animales,numeros):
    #print(f"Mostrando lista 1: {animal}")
    #print(f"Mostrando lista 2: {numero}")
    
#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y su valor es {valor}")
    
#usando un for/else 
for numero in numeros:
    print(f"Ejecutando el ultimo bucle. Valor actual: {numero}")
else:
    print("El bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas, listas y conjuntos