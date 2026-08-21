#Sumar 2 Numeros con print()
def suma(num1,num2):
    resultado = num1 + num2
    print(f"La suma de los 2 numeros es: {resultado}") 
    
suma(20,20)

#Calcular Área de un Rectángulo con print()
def area(base,altura):
    resultado = base * altura
    print(f"El área del rectangulo es: {resultado}")
    
area(10,15)

#El número es PAR o IMPAR con print()
def numero(num):
    if num%2 == 0:
        print("El número es PAR")
    else:
        print("El número es IMPAR")

numero(1)

def calculo(number1,number2):
    resultado = number1 + number2
    return resultado,number1,number2

resultado_final,num1,num2 = calculo(15,10)
print(f"El resultado del calculo: {num1} + {num2} es {resultado_final}")