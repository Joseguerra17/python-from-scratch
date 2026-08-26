def combinar_productos(nombres, precios):
    productos_finales = []
    for elemento, precio in zip(nombres, precios):
        if precio < 10000:
            productos_finales.append((elemento, precio))
    return productos_finales

resultado = combinar_productos(["papas","zanahorias","porotos"],[2500,1500,10000,6700])
print(resultado)