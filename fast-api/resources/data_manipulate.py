import pandas as pd


df = pd.read_json('resources/PC_clean.json')
result = df[df['Project Name'] == 'V94100102']

print(result)

'''
Project_JSON_data = result.to_json(orient='records')

with open('resources/PC_clean.json', 'w') as file:
    file.write(Project_JSON_data)



    Filtrado de datos:
Filtrar filas según una condición: df[df['columna'] > valor]
Filtrar filas que cumplan múltiples condiciones: df[(df['columna1'] > valor1) & (df['columna2'] == valor2)]
    Selección de datos:
Seleccionar solo ciertas columnas: df[['columna1', 'columna2']]
Seleccionar filas por posición: df.iloc[3:7]
    Agregación:
Calcular la media de una columna: df['columna'].mean()
Contar el número de ocurrencias de valores únicos: df['columna'].value_counts()
    Ordenamiento:
Ordenar el DataFrame por una columna: df.sort_values(by='columna')
Ordenar el DataFrame en orden descendente: df.sort_values(by='columna', ascending=False)
'''