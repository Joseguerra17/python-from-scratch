# ⚖️ Calculadora de IMC

Calcula el Índice de Masa Corporal a partir del peso y la altura ingresados por el usuario, y clasifica el resultado en una categoría.

## 💻 Código

```python
# Calculadora de IMC
print("Calculadora IMC: Índice de Masa Corporal")
peso = float(input("Ingresa tu Peso (KG): "))
altura = float(input("Ingresa tu Altura (M): "))
imc = peso / altura**2

if imc:
    if imc >= 30:
        print(f"Tienes Obesidad | IMC:{imc}")
    elif imc >= 25:
        print(f"Tienes Sobrepeso | IMC:{imc}")
    elif imc >= 18.5:
        print(f"Tienes Peso normal | IMC:{imc}")
    else:
        print(f"Tienes Bajo peso | IMC:{imc}")
```

## 🧠 Conceptos aplicados

- `input()` + `float()` para leer datos numéricos con decimales.
- Fórmula del IMC: `peso / altura²`.
- Cadena de `if / elif / else`, ordenada de la condición **más específica** (mayor valor) a la más general, para que ninguna condición "tape" a otra.

## ✅ Notas

> 📌 Ejercicio resuelto antes de conocer funciones, aplicando solo lo aprendido hasta ese momento.