# ⌨️ Velocidad al Escribir

Estima cuánto tardaría una persona en decir su nombre completo en voz alta, asumiendo que puede decir 2 palabras por segundo, y compara ese tiempo con un escenario "30% más rápido".

## 💻 Código

```python
# El usuario puede decir 2 palabras cada 1 segundo

palabras = input("Cual es tu nombre completo:")
cantidad_de_palabras = palabras.split(" ")
contar_palabras = len(cantidad_de_palabras)
dividir_palabras = contar_palabras / 2
entero_1 = int(dividir_palabras)

print("-----------------------------------A-----------------------------------")
print(f"Te demorarias {entero_1}s en decir la palabra: {palabras}")
print(f"y dijiste un total de {contar_palabras} palabra")
print("-----------------------------------------------------------------------")

if entero_1 > 120:
    print("-----------------------------------B-----------------------------------")
    print(f"Son demasiadas palabras loco, no terminas nunca. Cantidad de palabras: {contar_palabras}")
    print("-------------------------------------------------------------------------")

multiplicar_palabras = contar_palabras * 0.35
entero = int(multiplicar_palabras)

print("-----------------------------------C-----------------------------------")
print(f"Te demorarias {entero}s en decir la palabra un 30% mas rapido: {palabras}")
print(f"y dijiste un total de {contar_palabras} palabra")
print("-----------------------------------------------------------------------")
```

## 🧠 Conceptos aplicados

- `.split(" ")` para separar un texto en una lista de palabras.
- `len()` para contar cuántos elementos tiene esa lista (cuántas palabras hay).
- Operaciones matemáticas simples (división, multiplicación) para estimar tiempos.
- `if` para dar un mensaje especial en un caso extremo (más de 120 segundos).

## ✅ Notas

> 📌 Ejercicio resuelto antes de conocer funciones, aplicando solo lo aprendido hasta ese momento.