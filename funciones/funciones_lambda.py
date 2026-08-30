#lambda sirve para crear funciones anonimas, que despues podemos guardar en variables.
#sirve para hacer cosas sencillas y rapidas, y nos evitamos de hacer returns, ya que directamente esta guardada la informacion en la variable.
#no es apta cuando debemos dar mas de 1 instrucción.

numeros = [1,2,3,4,5,6,7,78,20,15,26]

#creando una funcion lambda para multiplicar por 2

multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga si es par o no
#def es_par(num):
    #if (num%2==0):
        #return True

#usando filter con una funcion comun
#numeros_pares = filter(es_par,numeros) #aqui la funcion filter, agarra la funcion es_par y luego los numeros de la lista (numeros).

#creando lo mismo que lo anterior pero con lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
#la funcion filter va revisando en este caso el iterable vuelta tras vuelta, en este caso revisa la lista, y comprueba uno por 1 si los numeros cumplen la division sea = 0

print(list(numeros_pares))