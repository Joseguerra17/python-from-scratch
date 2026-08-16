cadena1 = "hola Soy José y tengo 17"
cadena2 = "estoy aprendiendo Python"
cadena3 = "2026"

#upper convierte a mayuscula
mayusc = cadena2.upper()

#lower convierte a minuscula
minusc = cadena2.lower()

#capitalize convierte todo a minuscula primero y luego deja la primera letra con mayuscula
primera_letra_mayusc = cadena2.capitalize()

#buscamos una cadena/valor sobre otra, si no hay coincidencias devuelve -1 
busqueda_find = cadena1.find("h")

#buscamos una cadena/valor sobre otra, si encuentra coincidencias arroja una excepción
busqueda_index = cadena1.index("o")

#si es un dato numerico devuelve True, de lo contrario devuelve False
es_numerico = cadena3.isnumeric()

#si es un alfanumerico devuelve True, si no devuelve False
es_alfanumerico = cadena1.isalpha()

#count cuenta la cantidad de coincidencias de una cadena dentro de otra cadena
contar_coincidencias = cadena1.count("o")

#len cuenta cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#startswith verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("h")

#endswith verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("17")

#si encuentra el valor/dato dado lo reemplaza ese valor por el valor/dato dado
cadena_nueva = cadena1.replace("José","Lolax")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)