# ➖ diferencias

Recibe dos listas de números de igual tamaño y devuelve una nueva lista con la diferencia (resta) entre cada par de números en la misma posición.

## 💻 Código

```python
def diferencias(lista1, lista2):
    nueva_lista = []
    for indice, elemento_list in enumerate(lista1):
        elemento = lista2[indice]
        diferencia = elemento_list - elemento
        nueva_lista.append(diferencia)
    return nueva_lista

resultado = diferencias([10, 20, 30], [3, 5, 10])
print(resultado)  # [7, 15, 20]
```

## 🧠 Patrón aplicado

```
lista vacía (antes del for) → enumerate(lista1) para obtener índice + elemento
→ usar el índice para buscar el valor correspondiente en lista2 → restar → append → return fuera del for
```

## 🤔 Sobre el enunciado

"La diferencia entre cada **par** de números" se refería a un par de números emparejados por posición (uno de `lista1` y otro de `lista2`), **no** a números pares (múltiplos de 2) — ambigüedad razonable del enunciado, aclarada durante la práctica.

## ✅ Notas

Se usó `enumerate()` + indexado (`lista2[indice]`) a propósito, en vez de `zip()`, como decisión deliberada para practicar ambas formas de recorrer dos listas emparejadas — no por desconocer `zip()`, sino para reforzar el criterio de cuándo aplica cada una.

---

> 📌 Ejercicio propuesto por Claude (Anthropic) como práctica para reforzar el patrón `for + if + acumulador` con dos listas relacionadas.