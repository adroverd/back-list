import pandas as pd

data = pd.read_excel("resources/IBFS_Lock studies_12Sep2024.xlsx", sheet_name="Export")

Project_JSON_data = data.to_json(orient='records')

with open('resources/PC.json', 'w') as file:
    file.write(Project_JSON_data)


# me hago un data frame
df = pd.read_json('resources/PC.json')
# limpio
registros_nulos = df[df.isnull().all(axis=1)]
print(registros_nulos)
# transformo el nombre
def transform_project_name(name):
        if pd.notnull(name):
            new_name = name.replace("-", "")
            return new_name[:-2]  # Truncate the last 2 characters
        else:
            return name
    
df['Project Name'] = df['Project Name'].apply(transform_project_name)   

# filtro (columna y valor, pueden ser mas de 1)
result = df[((df['CDM Dev Process'] == 'Integrated') 
             | (df['CDM Dev Process'] == 'PDAM NG') 
             | (df['CDM Dev Process'] == 'PDAM 2_0')) 
             & (df['Data Source'] == 'EDX3 Database')
             & (df["Analysis"] == "Interim DBL")
             & (df['DBL Complete'] == 'No')] # TODO preguntar las condiciones

print(result)


Project_JSON_data = result.to_json(orient='records')

with open('resources/PC_clean.json', 'w') as file:
    file.write(Project_JSON_data)


'''
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