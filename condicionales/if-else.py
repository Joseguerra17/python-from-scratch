edad = 17

#if en este caso esta preguntando si la (edad) es mayor o igual a (18) ejecuta la accion asignada, si la variable edad no cumple con que es mayor o igual a 18 entonces ejecuta el (else)

if edad >= 18: #todo lo que este aqui forma parte del if
    print("eres mayor de edad")
    
else: #todo lo que este aqui forma parte del else
    print("no eres mayor de edad")
    
#Ejemplo de la contraseña

contraseña_almacenada = "Lola123"
contraseña_escrita = "Lola123"

if contraseña_almacenada == contraseña_escrita: 
    print("INICIANDO SESIÓN...")
    
else:
    print("CONTRASEÑA INCORRECTA. INTENTA DE NUEVO")