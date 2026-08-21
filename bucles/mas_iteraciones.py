#creando las listas
frutas = ["platano","manzana","naranja","ciruela","durazno","pera"]
cadena = "Hola José"
numeros = [2,5,8,10]

#evitando que se coma una fruta en este caso una ciruela con la (setencia continue)
for fruta in frutas:
    if fruta == 'ciruela':
        continue
    print(f"Me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose (el else tampoco se ejecuta)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == 'naranja':
        break
else:
    print("Terminado")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (for recorre toda la lista y esos valores los asigna a la variable x, luego los * multiplica en 2)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
    