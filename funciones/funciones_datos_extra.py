 #creando una funcion de 3 parametros
 
#def frase(nombre,apellido,adjetivo):
     #return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword arguments
#frase_resultante = frase(adjetivo="Inteligente",nombre="José",apellido="Guerra")
#print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "inteligente"):
     return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword arguments
frase_resultante = frase("José","Guerra","Megamente")
print(frase_resultante)

