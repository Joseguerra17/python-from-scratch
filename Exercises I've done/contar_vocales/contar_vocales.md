# 🔤 contar_vocales

Recibe un texto y devuelve **cuántas vocales** tiene.

## 💻 Código

### Versión con `.count()` (usando una herramienta ya hecha de Python)

```python
def contar_vocales(frase):
    frase = frase.lower()
    total = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
    return total
```

### Versión manual (recorriendo letra por letra, para practicar el patrón `for + if + acumulador`)

```python
def contar_vocales(frase):
    frase = frase.lower()
    contador = 0
    for letra in frase:
        if letra in "aeiou":
            contador += 1
    return contador

resultado = contar_vocales("Hola como estas gente estoy aprendiendo python")
print(resultado)
```

## 🧠 Patrón aplicado

```
contador = 0 (antes del for) → for letra por letra → if letra in "aeiou" → contador += 1 → return fuera del for
```

## 🐛 Errores en el camino

1. **Variable pisada:** en el primer intento, dentro de `for vocal in frase:`, sobreescribía la variable `vocal` con `vocal = str(frase)` (la frase completa), perdiendo el valor de la letra individual que el `for` ya entregaba. El resultado salía correcto **por casualidad**, porque `.count()` igual recorre la frase completa por dentro, sin depender del `for` externo — pero ese `for` en realidad no estaba aportando nada.
2. 🐞 **Bug real detectado en la versión manual:** sin convertir la frase a minúsculas primero (`frase.lower()`), las vocales en mayúscula (como la "E" de "Elsa") no se contaban, porque `"E" in "aeiou"` da `False` — mayúsculas y minúsculas son caracteres distintos para Python.

## ✅ Aprendizaje

Revisar casos límite antes de dar una solución por terminada: mayúsculas/minúsculas, listas o strings vacíos, el cero, etc. Una solución puede "funcionar" con el ejemplo de prueba usado, y aun así fallar con casos que no se probaron.

---

> 🤖 Ejercicio propuesto por Claude (Anthropic) como práctica para reforzar el patrón `for + if + acumulador`.