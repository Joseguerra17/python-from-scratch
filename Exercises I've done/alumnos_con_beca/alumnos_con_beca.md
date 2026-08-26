# 🎓 alumnos_con_beca

Recibe dos listas (nombres y promedios) y devuelve solo los **nombres** de quienes tienen promedio mayor o igual a 6.0.

## 💻 Código

```python
def alumnos_con_beca(nombres, promedios):
    promedios_mayor_o_igual = []
    for alumno, promedio in zip(nombres, promedios):
        if promedio >= 6:
            promedios_mayor_o_igual.append(alumno)
    return promedios_mayor_o_igual

resultado = alumnos_con_beca(["Pepito","Juanito","Lola"],[3.7,5,6.2])
print(f"Alumnos Becados: {resultado}")  # ['Lola']
```

## 🧠 Patrón aplicado

```
lista vacía (antes del for) → zip(nombres, promedios) para recorrer ambas listas emparejadas
→ if promedio >= 6 → append solo del nombre (no del promedio) → return fuera del for
```

## 📝 Antes de escribir el código: trazado a mano

Con `nombres=["Pepito","Juanito","Lola"]` y `promedios=[3.7, 5, 6.2]`:

| Vuelta | alumno | promedio | ¿Entra al if? | ¿Qué se agrega? |
|---|---|---|---|---|
| 1 | Pepito | 3.7 | No | — |
| 2 | Juanito | 5 | No | — |
| 3 | Lola | 6.2 | Sí | "Lola" |

Resultado esperado: `["Lola"]` ✅ (coincide con lo que devolvió el código)

## ✅ Notas

- Se usó `zip()` en vez de `enumerate()` a propósito, como variación deliberada respecto al ejercicio anterior (`diferencias`), para practicar ambas formas de recorrer dos listas emparejadas y reforzar el criterio de cuándo usar una u otra.
- El `.append()` solo guarda `alumno` (el nombre), no una tupla — porque el enunciado pide únicamente los nombres, no el promedio.

---

> 📌 Ejercicio propuesto por Claude (Anthropic) como práctica para reforzar el patrón `for + if + acumulador` con dos listas relacionadas.