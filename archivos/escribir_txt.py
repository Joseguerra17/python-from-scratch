#abriendo el archivo con with open y modificandolo con write (w)
with open("archivos\\texto_lola.txt","w",encoding="UTF-8") as archivo:
    
    #sobreescribiendo el archivo
    #archivo.write("Eres muy capo al estar aprendiendo")
    
    #agregando 2 lineas con writelines
    archivo.writelines(["Hola Capo\n","Como Estas?\n"])
    
    #agregando otras 2 lineas
    archivo.writelines(["Eres un Masteer\n","Brouttt"])
    