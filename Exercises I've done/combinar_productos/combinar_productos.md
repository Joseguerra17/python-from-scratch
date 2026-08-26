# 🛒 combinar_productos

Recibe dos listas (nombres de productos y precios) y devuelve una lista de tuplas `(nombre, precio)`, solo de los productos con precio menor a $10.000.

## 💻 Código

```python
def combinar_productos(nombres, precios):
    productos_finales = []
    for elemento, precio in zip(nombres, precios):
        if precio < 10000:
            productos_finales.append((elemento, precio))
    return productos_finales

resultado = combinar_productos(["papas","zanahorias","porotos"],[2500,1500,10000])
print(resultado)  # [('papas', 2500), ('zanahorias', 1500)]
```

## 🧠 Patrón aplicado

```
lista vacía (antes del for) → zip(nombres, precios) para recorrer ambas listas emparejadas
→ if precio < 10000 → append de la tupla (nombre, precio) → return fuera del for
```

## 🐛 Errores en el camino

- **Primer intento:** dentro de la función se reutilizaron los mismos nombres para los parámetros (`nombres`, `precios`, las listas completas) y para las variables del `for` (`nombres`, `precios`, un solo elemento por vuelta). Funcionaba porque `zip()` alcanza a leer las listas originales completas antes de que el `for` empezara a sobreescribirlas, pero era una situación confusa y arriesgada: si se necesitara usar las listas completas después de esa línea, ya no habría sido posible, porque el `for` las habría sobreescrito con valores individuales.

## ✅ Aprendizaje

Evitar usar el mismo nombre para un parámetro (la colección completa) y la variable de un `for` que lo recorre — aunque el código funcione por cómo está armado en ese momento, genera confusión y riesgo de perder acceso a la colección original más adelante.

---

> 📌 Ejercicio propuesto por Claude (Anthropic) como práctica para reforzar el patrón `for + if + acumulador` con dos listas relacionadas y tuplas.