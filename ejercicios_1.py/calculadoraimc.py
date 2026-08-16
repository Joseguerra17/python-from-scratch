#Calculadora de IMC

print("Calculadora IMC")
peso = float(input("Ingresa tu Peso (KG): "))
altura = float(input("Ingresa tu Altura (M): "))
imc = peso / altura**2

if imc:
    if imc >= 30:
        print(f"Tienes Obesidad | IMC:{imc}")
    elif imc >= 25 <= 29.9:
        print(f"Tienes Sobrepeso | IMC:{imc}") 
    elif imc >= 18.5 <= 24.9:
        print(f"Tienes Peso normal | IMC:{imc}")
    elif imc < 18.5:
        print(f"Tienes Bajo peso | IMC:{imc}")        