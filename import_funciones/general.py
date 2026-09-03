from calculadora import suma,resta
import time

usuario = "Jose Guerra"
contraseña = "12345Jose"

if usuario == "Jose Guerra" and contraseña == "12345Jose":
    print("INICIANDO SESIÓN...")
    time.sleep(3)
    pregunta = input("Que Prefieres, SUMAR o RESTAR?\nTU RESPUESTA: ")
    pregunta = pregunta.lower()
    if pregunta == "sumar":
        suma()
    elif pregunta == "restar" or pregunta == "resta":
        resta()
    else:
        print("¡Opción no Valida!")
else:
    print("ACCESO DENEGADO -> TUS DATOS SON INCORRECTOS")
    