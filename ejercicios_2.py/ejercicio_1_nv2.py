def sin_profesor(cantidad):
    listado_alumnos = []
    for lista in range(cantidad):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        alumno = (nombre, edad)
        listado_alumnos.append(alumno)
        
    listado_alumnos.sort(key= lambda elements: elements[1])
    profesor = listado_alumnos[-1][0]
    asistente = listado_alumnos[0][0]
    return profesor, asistente

profesor, asistente = sin_profesor()

print(f"El profesor de esta clase sera: {profesor}")
print(f"El asistente de la clase sera: {asistente}")

#Forma mas corta de hacerlo
def sin_profesor(cantidad):
    listado_alumnos = []
    for lista in range(cantidad):
        alumno = (input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
        listado_alumnos.append(alumno)
        
    listado_alumnos.sort(key= lambda elements: elements[1])
    profesor = listado_alumnos[-1][0]
    asistente = listado_alumnos[0][0]
    return profesor, asistente

profesor, asistente = sin_profesor(3)

print(f"El profesor de esta clase sera: {profesor}")
print(f"El asistente de la clase sera: {asistente}")
        