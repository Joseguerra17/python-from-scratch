#abriendo el archivo con with open y agregando mas contenido con append (a)
with open("archivos\\texto_lola.txt","a",encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(3):
        archivo.write(f"Linea {i+1} agregada\n")
        
    #usando el bucle pero esta vez agregando mas contenido en la misma linea    
    archivo.write("\n")
    for i in range(3):
        archivo.writelines(f"Linea {i+1} agregada ")
        
        