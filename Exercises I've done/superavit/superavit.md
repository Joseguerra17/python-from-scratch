# 💰 Estado Financiero

Recibe el ingreso mensual del usuario y sus gastos en distintas categorías, y calcula si tiene déficit, superávit o equilibrio financiero.

## 💻 Código

```python
print("Estado Financiero")
ingreso_mensual = input("¿Cuánto dinero recibes al mes?: ")
print("Gastos en Diferentes Categorias")
alimentacion = input("Alimentación: ")
transporte = input("Transporte: ")
entretenimiento = input("Entretenimiento: ")
servicios = input("Servicios Basicos (Agua, luz, internet): ")
otros = input("Otros gastos: ")

ingreso_mensual = int(ingreso_mensual)
alimentacion = int(alimentacion)
transporte = int(transporte)
entretenimiento = int(entretenimiento)
servicios = int(servicios)
otros = int(otros)

gasto_mensual = alimentacion + transporte + entretenimiento + servicios + otros
superavit = ingreso_mensual - gasto_mensual

if gasto_mensual > ingreso_mensual:
    print("Tienes un Déficit, estas gastando mas de lo que ganas.")
    print(f"Ingreso Mensual: {ingreso_mensual}")
    print(f"Gastos: {gasto_mensual}")
    print(f"Diferencia: {superavit}")
elif gasto_mensual < ingreso_mensual:
    print("Tienes Superávit, tus ingresos son mayores a los gastos.")
    print(f"Ingreso Mensual: {ingreso_mensual}")
    print(f"Gastos: {gasto_mensual}")
    print(f"Restante: {superavit}")
else:
    print("Tienes un Equilibrio, tus gastos son iguales a los ingresos.")
    print(f"Ingreso Mensual: {ingreso_mensual}")
    print(f"Gastos: {gasto_mensual}")
    print(f"Restante: {superavit}")
```

## 🧠 Conceptos aplicados

- Múltiples `input()` para recolectar varias categorías de gasto.
- Conversión de texto a número con `int()` en cada variable recolectada.
- Suma de varias variables para obtener un total (`gasto_mensual`).
- `if / elif / else` para comparar dos totales (ingreso vs. gasto) y clasificar el resultado en tres escenarios posibles.

## ✅ Notas

> 📌 Ejercicio resuelto antes de conocer funciones, aplicando solo lo aprendido hasta ese momento.