#el usuario puede decir 2 palabras cada 1 segundo

palabras = input("Cual es tu nombre completo:")
cantidad_de_palabras = palabras.split(" ")
contar_palabras = len(cantidad_de_palabras)
dividir_palabras = contar_palabras / 2
entero_1 = int(dividir_palabras)

print("----------------------------------A--------------------------------------")
print(f"Te demorarias {entero_1}s en decir la palabra: {palabras}") 
print(f"y dijiste un total de {contar_palabras} palabra")
print("-------------------------------------------------------------------------")

if entero_1 > 120:
    print("----------------------------------B--------------------------------------")
    print(f"Son demasiadas palabras loco, no terminas nunca. Cantidad de palabras: {contar_palabras}")
    print("-------------------------------------------------------------------------")


multiplicar_palabras = contar_palabras * 0.35
entero = int(multiplicar_palabras)

print("----------------------------------C--------------------------------------")
print(f"Te demorarias {entero}s en decir la palabra un 30% mas rapido: {palabras}") 
print(f"y dijiste un total de {contar_palabras} palabra")
print("-------------------------------------------------------------------------") 

