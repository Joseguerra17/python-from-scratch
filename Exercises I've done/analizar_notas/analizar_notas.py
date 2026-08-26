def analizar_notas(lista):
    nota_mas_alta = max(lista)
    nota_mas_baja = min(lista)
    promedio = sum(lista) / len(lista)
    return nota_mas_alta, nota_mas_baja, promedio

nota_mas_alta, nota_mas_baja, promedio = analizar_notas([7,2.5,4.6,3.1,6.8])

print(f"Tu nota más alta fue: {nota_mas_alta}")
print(f"Tu nota más baja fue: {nota_mas_baja}")
print(f"Tu promedio fue: {promedio}")