import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")

#ordenando de forma descendente
df_ordenado_descendente = df.sort_values("edad", ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras filas con head(), siempre mostrara las filas anteriores al numero de fila que le estemos pidiendo en este caso head(3)
#con esto accedemos a las filas de arriba hacia abajo
primeras_filas = df.head(3)

#accediendo a las ultimas 3 filas con tail(), con esto accedemos a las filas de abajo hacia arriba
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accendiendo a un elemento especifico del dataframe (df) con loc, en este caso al apellido de la fila 1, accedemos por el nombre de la columna
elemento_especifico_loc = df.loc[1, "apellido"]

#accendiendo a un elemento especifico del dataframe (df) con iloc, esta vez por el indice
elemento_especifico_iloc = df.iloc[1,1]

#accediendo a todas las filas de una columna, en este caso el de los apellidos
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc

fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc

fila_3_iloc = df.iloc[2,:]

#accediendo a filas con edad mayor que 30, el primer dato que pide son las filas y el segundo las columnas
mayor_que_30 = df.loc[df["edad"]>20,:]

print(mayor_que_30)