def calculadora():
    print("-- CALCULADORA --")
    num1 = int(input("Escribe un Numero: "))
    num2 = int(input("Escribe tu Segundo Numero: "))
    operador = int(input("-- SELECCIONA TU OPERADOR -- \n(+) Suma -> 1\n(-) Resta -> 2\n(*) Multiplicación -> 3\n(/) División -> 4\n(**) Elevación -> 5\n-- ESCRIBE TU OPERADOR: "))
    if operador == 1:
        calculo = num1 + num2
        print(f"\nEL RESULTADO ES: {calculo}")
    elif operador == 2:
        calculo = num1 - num2
        print(f"\nEL RESULTADO ES: {calculo}")
    elif operador == 3:
        calculo = num1 * num2
        print(f"\nEL RESULTADO ES: {calculo}")
    elif operador == 4:
        calculo = num1 / num2
        print(f"\nEL RESULTADO ES: {calculo}")
    elif operador == 5:
        calculo = num1 ** num2
        print(f"\nEL RESULTADO ES: {calculo}")
    
calculadora()
    