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