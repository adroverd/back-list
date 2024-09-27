import json
import pandas as pd
from connection import conDMW, conPC

def listB():
    con = conDMW()
    cursor = con.cursor()
    
    query = "SELECT * FROM SB_TRACKER_INFO WHERE ROWNUM <= 20"
    cursor.execute(query)
    
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
 
    data_list = []

    for row in rows:
        data_list.append(dict(zip(columns, row)))

    cursor.close()
    con.close()

    return data_list

def getByStudy(study_name):
    con = conDMW()
    cursor = con.cursor()
    
    query = "SELECT * FROM SB_TRACKER_INFO WHERE STUDY_NAME = :study_name FETCH FIRST 1 ROW ONLY"
    cursor.execute(query, {'study_name': study_name})
    
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
 
    if row is not None:
        result = dict(zip(columns, row))
    else:
        result = None

    cursor.close()
    con.close()

    return result


def getQuery(queryP):

    con = conDMW()
    cursor = con.cursor()    
    query = queryP
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    df_from_db = pd.DataFrame(rows, columns=columns)

    df_from_json=pd.DataFrame(conPC())

    result_df = pd.merge(df_from_db, df_from_json, left_on='TRIAL', right_on='Project Name', how='inner')
    result_df = result_df[['TRIAL', 'VALUE']]

    result_json = result_df.to_json(orient='records')

    cursor.close()
    con.close()

    return result_json