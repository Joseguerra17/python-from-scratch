# ➕ suma_positivos

Recibe una lista de números (positivos y negativos mezclados) y devuelve la **suma** solo de los positivos.

## 💻 Código

```python
#Primera versión
def suma_positivos(lista):
    suma_positivos_list = []
    for num in (lista):
        if num > 0:
            suma_positivos_list.append(num)
    suma = sum(suma_positivos_list)
    return suma

resultado = suma_positivos([5,6,2,6,-5,-10,-15])
print(resultado)
```

```python
#Segunda Versión
def suma_positivos(lista):
    suma = 0
    for num in lista:
        if num > 0:
            suma = suma + num
    return suma

resultado = suma_positivos([5,6,2,6,-5,-10,-15])
print(resultado)  # 19
```

## 🧠 Patrón aplicado

```
acumulador numérico = 0 (antes del for) → if dentro del for → suma += num dentro del if → return fuera del for
```

## 🔁 Camino recorrido

1. **Primera versión:** armé una lista con `.append()` guardando todos los positivos, y al final usé `sum()` sobre esa lista para obtener el total.
2. **Segunda versión (más directa):** en vez de guardar los positivos en una lista intermedia, acumulo la suma directamente con `suma += num` dentro del `if`. Mismo resultado, un paso menos.

## ✅ Aprendizaje

- El acumulador de un patrón `for + if` no siempre tiene que ser una lista — puede ser un número que se va sumando (o contando) directamente. Mismo esqueleto, distinto tipo de acumulador.