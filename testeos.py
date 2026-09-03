#Practica de como llamar a indices dentro de variables
colores = ["azul","rojo","amarillo"]
indice = colores[1]

a = (5)
b = (5,)
print(type(a))  # devuelve un int
print(type(b))  # devuelve una tuple por la coma (,)

for i, c in enumerate(colores): print(f"El Color es: {c}\n El indice es: {i}\n----------")
 