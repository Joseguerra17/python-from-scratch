# 🔢 mayores_a

Recibe una lista de números y un límite, y devuelve solo los números **mayores** a ese límite.

## 💻 Código

```python
def mayores_a(lista, limite):
    mayores_al_limit = []
    for num in lista:
        if num > limite:
            mayores_al_limit.append(num)
    return mayores_al_limit

resultado = mayores_a([1,2,3,4,5,6,7,8,9,10], 3)
print(resultado)  # [4, 5, 6, 7, 8, 9, 10]
```

## 🧠 Patrón aplicado

```
lista vacía (antes del for) → if dentro del for → append dentro del if → return fuera del for
```

## 🐛 Errores en el camino

- **Primer intento:** llamé a la función pasando el límite como lista (`[3]`) en vez de como número suelto (`3`). Eso me obligó a agregar conversiones innecesarias (`str()`, `int()`, indexado `[0]`) dentro de la función solo para "desempacar" el número.

## ✅ Aprendizaje

Un parámetro solo debería ser una lista si representa **varios** valores a recorrer. Si representa un solo valor (como un límite de comparación), se pasa directo, sin corchetes.