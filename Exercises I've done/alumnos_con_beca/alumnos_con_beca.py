def alumnos_con_beca(nombres, promedios):
    promedios_mayor_o_igual = []
    for alumno, promedio in zip(nombres, promedios):
        if promedio >= 6:
            promedios_mayor_o_igual.append(alumno)
    return promedios_mayor_o_igual

resultado = alumnos_con_beca(["Pepito","Juanito","Lola"],[3.7,5,7,6.2])
print(f"Alumnos Becados: {resultado}") 