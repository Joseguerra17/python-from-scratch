def contar_vocales(frase):
    for vocal in (frase):
        vocal = frase.lower()
        vocal_total = vocal.count("a") + vocal.count("e") + vocal.count("i") + vocal.count("o") + vocal.count("u")
    return vocal_total

resultado = contar_vocales("Hola como estas gente estoy aprendiendo python")
print(resultado)

#Lo mismo pero mas corto y simple
def contar_vocales_2(frase):
    frase = frase.lower()
    contador = 0
    for letra in frase:
        if letra in "aeiou":
            contador += 1
    return contador

resultado2 = contar_vocales_2("Ola estoy aprendiendo python")
print(resultado2)

# contar_coincidencias = cadena1.count("o")