nombre = ["Lola","Juanito","Kratos","Esmeralda"]
apellido = ["Lolera","El constructor","El devorador","velera"]

with open("resolviendo_problemas_cortos\\problema1.txt","w",encoding="UTF-8") as archivo:
    for name, ape in zip(nombre,apellido):
        archivo.writelines(f"------------------- \nNombre: {name} \nApellido: {ape}\n")
    archivo.writelines("-------------------")