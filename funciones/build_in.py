numeros = [4,6,7,42,10,25,26]


#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#encontrando el numero mas bajo de una lista
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.346235,2)

#retorna False si le pasamos 0, vacio, False, None \ True devuelve cuando es distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(16)

#retorna True, si todos los valores son verdaderos
resultado_all = all([23,True])

#SUMA TODOS LOS VALORES DE UN ITERABLE
suma_total = sum(numeros)

print(suma_total)
