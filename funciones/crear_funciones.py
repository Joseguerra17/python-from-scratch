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
#def crear_contraseña_random(num):
    #chars = "akjfomiowfaoi"
    #num_entero = str(num)
    #num = int(num_entero[0])
    #c1 = num - 2
    #c2 = num
    #c3 = num - 5
    #contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #return contraseña,num

#password,primer_numero = crear_contraseña_random(9)

#print(f"Tu Contraseña nueva es: {password}")
#print(f"El numero utilizado para crearla fue: {primer_numero}")


#def clasificador_temperaturas(grados):
    #if grados < 10:
        #print(f"Hace demasiado Frío en tu ciudad: {grados}°C")
    #elif grados <= 24:
        #print(f"Actualmente hay un clima templado en tu ciudad: {grados}°C")
    #else:
        #print(f"Hace demasiada calor en tu ciudad: {grados}°C")
    #return grados

#grados = clasificador_temperaturas(19)


#def clasificador_temperaturas(grados):
   # if (grados < 10):
       # return f"Hace demasiado Frío en tu ciudad: {grados}°C"
    #elif (grados < 24):
        #return f"Actualmente hay un clima templado en tu ciudad: {grados}°C"
    #else:
        #return f"Hace demasiada calor en tu ciudad: {grados}°C"

#resultado = clasificador_temperaturas(9)

#if "templado" in resultado.lower():
    #print("¡Buen Dia para Salir!")
#if "frío" in resultado.lower():
    #print("¡Hace demasiado Frío el dia de Hoy!")
        
#print(resultado)

def filtrador_notas(lista): 
    lista_vacia = list([])
    for num in enumerate(lista):
        num1 = num[1]
        calculo1 = 1 + num1 / 100 * 6
        if num1 >= 60:
            lista_vacia.append(calculo1)
    return lista_vacia

resultado = filtrador_notas([67,34,22,16,86])
print(resultado)