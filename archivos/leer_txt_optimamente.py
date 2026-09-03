#abriendo el archivo con with open
with open ("archivos\\texto_lola.txt",encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)    
    
#no es necesario cerrarlo al usar with open   
#esta es la forma optima de abrir un archivo