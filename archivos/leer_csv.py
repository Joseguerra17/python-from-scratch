import csv

with open("archivos\\datos.csv") as archivo:
    reader = (csv.reader(archivo))
    for filas in reader:
        print(filas)
    