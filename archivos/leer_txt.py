#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos\\texto_lola.txt",encoding="UTF-8")

#leer archivo completo 
#archivo = archivo.read()

#leer linea por linea
#linea = archivo.readlines()

#leer una sola linea
linea = archivo.readline()

#leer una sola linea con la cantidad de letras que queremos mostrar, en este caso 5 letras
#linea = archivo.readline(5)

#cerrar el archivo
archivo.close()

#una vez cierras el archivo para volver a trabajar con el tienes que re-abrirlo con open, de lo contrario una vez cerrado y ya ejecutadas
#sus debidas acciones estas quedan guardadas.

print(linea)