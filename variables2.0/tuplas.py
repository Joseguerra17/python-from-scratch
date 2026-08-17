#Tuplas sirven mucho para almacenar datos solo de lectura, ya que gestionan mejor la memoria, en cambio las listas debido a que sirven para ir modificando datos no son tan optimas para ciertas situaciones

#creando tupla con tuple()
tupla = tuple(["dato1","dato2"])

#creando tupla con multiples datos y sin parentisis
tupla = "dato1","dato2"

#creando tupla con un solo dato y sin parentesis (lleva coma al final)
tupla = "dato",

print(type(tupla))