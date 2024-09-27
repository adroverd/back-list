import json
import pandas as pd
import os
import cx_Oracle

# PARA DEPLOY DEV
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

# PARA PRUEBAS LOCAL
'''def conDMW():
    dsn = cx_Oracle.makedsn(host='EXADB03PR-SCAN-ALSC.MERCK.COM', port=1521, service_name='PMCKCI')
    result = cx_Oracle.connect(user='adroverd_4938', password='Nanita!20245', dsn=dsn)
    return result'''
    
# TEMPORAL HASTA TENER LA API    
def conPC():
    with open('resources/PC_clean.json', 'r') as file:
        json_list = json.load(file)
        result = pd.DataFrame(json_list)
    return result
