#Definiendo variable con numeros

a = 5
b = 5
c = a + b

print(c) #devuelve c, que es la suma de las 2 letras, a + b

#Definiendo variable con letras

nombre = "Jose Guerra"
edad = "17"

print(nombre, edad) #devuelve el nombre y la edad

#Definiendo variable con letras / Concatenar con +

nombre = "Jose Guerra"
edad = "17"
saludo = "Hola " + nombre + " tu edad actual es: " + edad + " Años!"

print(saludo)

#Definiendo variable con letras / f(strings)

nombre = "Jose Guerra"
edad = 17
saludo = f"Hola {nombre} Como Estas?"

print(saludo)

#Operadores de Pertenencia / (in y not in)
 
nombre = "Jose Guerra"
edad = 17
saludo = f"Hola {nombre} Como Estas?"

print("Hola" in saludo) #Aqui preguntamos si la palabra (Hola) esta en la variable (saludo). Lo que devuelve [True], ya que (Hola) si esta en la variable (saludo).
print("juanito" not in saludo ) #Aqui preguntamos si la palabra (juanito) NO esta en la variable (saludo). Lo que devuelve [True], ya que (juanito) no esta en la variable (saludo).

#Operadores de Pertenencia / Ahora con la Variable (nombre) / (in)

nombre = "Jose Guerra"
edad = 17
saludo = f"Hola {nombre} Como Estas?"

print("Juanito" in saludo) #False
print("Jose Guerra" in saludo) #True 

#Definiendo variable con camelCase

nombreCompleto = "José Guerra"

#Definiendo variable con snake_case

nombre_completo = "José Guerra" 
