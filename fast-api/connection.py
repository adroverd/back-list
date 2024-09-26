import json
import pandas as pd
import os
import cx_Oracle


def con():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    service_name = os.getenv('DB_SERVICE_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    dsn = cx_Oracle.makedsn(host=host, port=port, service_name=service_name)
    connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    print("dsn ===>>>> " + dsn)
    return connection

# SIMIL ORM
def listB():
    connection = con()
    cursor = connection.cursor()
    
    query = "SELECT * FROM SB_TRACKER_INFO WHERE ROWNUM <= 20"
    cursor.execute(query)
    
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
 
    data_list = []

    for row in rows:
        data_list.append(dict(zip(columns, row)))

    cursor.close()
    connection.close()

    return data_list

def getByStudy(study_name):
    connection = con()
    cursor = connection.cursor()
    
    query = "SELECT * FROM SB_TRACKER_INFO WHERE STUDY_NAME = :study_name FETCH FIRST 1 ROW ONLY"
    cursor.execute(query, {'study_name': study_name})
    
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
 
    if row is not None:
        result = dict(zip(columns, row))
    else:
        result = None

    cursor.close()
    connection.close()

    return result


def getQuery(queryP):

    connection = con()
    cursor = connection.cursor()    
    query = queryP
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    df_from_db = pd.DataFrame(rows, columns=columns)

    with open('../resources/PC_clean.json', 'r') as file:
        json_list = json.load(file)
    df_from_json = pd.DataFrame(json_list)

    result_df = pd.merge(df_from_db, df_from_json, left_on='TRIAL', right_on='Project Name', how='inner')
    result_df = result_df[['TRIAL', 'VALUE']]

    # Convertir el DataFrame resultante a formato JSON
    result_json = result_df.to_json(orient='records')

    # Cerrar la conexión y liberar recursos
    cursor.close()
    connection.close()
    print(result_json)
    # Devolver el JSON como respuesta
    return result_json
