#Calculadora de IMC

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