#creando una función simple

#def saludar():
    #print("Hola José Guerra, ¿Como Estas?")
    
#ejecutando la funcion simple    
#saludar()

#crear una funcion que tenga parametros

#def saludar(nombre,sexo):
    #sexo = sexo.lower()
    #if (sexo == "mujer"):
        #adjetivo = "reina"
    #elif (sexo == "hombre"):
        #adjetivo = "titan"
    #else:
        #adjetivo = "crack"
    #print(f"Hola {nombre}, mi {adjetivo} ¿Como estas?")
    
#saludar("emilia","mujer")
#saludar("jose","hombre")
#saludar("lola","mujer")
        
#creando una funcion que tenga parametros con variables asignados por el usuario        
#def saludar(nombre):
    #print(f"Hola {nombre} ¿Como estas?")
    
#saludar(input("Cual es tu nombre? "))

#creando una funcion que devuelva valores
def crear_contraseña_random(num):
    chars = "akjfomiowfaoi"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

password,primer_numero = crear_contraseña_random(9)

print(f"Tu Contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")
    