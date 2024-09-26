from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Query
from connection import listB, getByStudy, getQuery
import secrets

app = FastAPI(
    title="Backend List SB API",
    description="Standard Bulletin list and select by study",

)

app.secret_key = secrets.token_hex(16)

class QueryRequest(BaseModel):
    sql_query: str

@app.get('/list')
async def get_list():
    #items = listB()
    #return {"items": items}
    json=[{"TRIAL":"MK8510001",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NOT NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK0616015",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK0616015",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK0616013",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK0616017",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK0616019",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK5475013",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK8591A051",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK8591A052",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK8591A053",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"},{"TRIAL":"MK8591A054",
    "VALUE":"CASE WHEN (UP$#CODELISTCODE='CIGARETTE' AND TRTCIG IS NOT NULL AND STDTCCIG_DTS IS NULL) OR (UP$#CODELISTCODE='OTHER TOBACCO' AND TRTOTHTU IS NOT NULL AND STDTCOTBUSE_DTS IS NULL) OR (UP$#CODELISTCODE='ALCOHOL' AND OCCURAEUA IS NOT NULL AND ENDTCAU_DTS IS NOT NULL) OR (UP$#CODELISTCODE='CAFFEINE' AND OCCURCEUA IS NOT NULL AND ENDTC_DTS IS NOT NULL) OR (UP$#CODELISTCODE='E-LIQUID' AND OCCURELEUA IS NOT NULL AND STDTCELIQ_DTS IS NULL) THEN 'BEFORE' ELSE NULL END"}]
    return json

@app.get('/study')
async def get_study(study_name: str = Query(None)):
    if study_name:
        study_data = getByStudy(study_name)
        if study_data:
            return study_data
        else:
            raise HTTPException(status_code=404, detail="Study not found")
    else:
        raise HTTPException(status_code=400, detail="Missing study_name parameter")

@app.post('/query')
async def get_query(req: QueryRequest):
    res = getQuery(req.sql_query)  # Ejecutar la consulta en la base de datos

    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="No results found for the provided query")
    



'''
    hago una peticion a la api de project, y tal vez en otro hilo hago una consulta a la base de datos correspondiente a
    la libreria con la conexion correspondiente. cada hilo guarda su resultado en redis. El resultado de la bs de dato
    los convierto en diccionario (o hash table, no me quedo claro) y el json que devuelve la api, tambien lo convierto 
    a diccionario o la estructura necesaria, ambos los guardo en 2 hilos separados accediendo a los datos de redis. 
    accedo en el hilo principal a los 2 diccionarios de redis y comparo para hacer el join. de las 28 columnas de cada 
    fila necesito solo 2, asi que con el resultado del join armo un json para dar como respuesta con solo los 2 atributos 
    que necesito de cada objeto.

    hilo 1 => llama api, convierte a diccionario hash, guarda en cache. Puede quedar un rato para posible uso de otra libreria
    hilo 2 => consulta a la base, convierte a diccionario hash, guarda en cache => no se si es necesario cachear
    hilo principal recupara dic PC y dic compara variable. Arma respuesta json con lista trials (solo nombre?)


Petición a la API y consulta a la base de datos en paralelo:

Tu aplicación realiza una petición a la API de Project para obtener un conjunto de datos. 
Al mismo tiempo, en otro hilo, la aplicación realiza una consulta a la base de datos correspondiente 
a la librería utilizando la conexión correspondiente.

Almacenamiento de los resultados en Redis:

Ambos hilos guardan sus resultados en Redis como diccionarios (o en términos de Redis, 
estructuras de datos de tipo hash). Por ejemplo, podrías utilizar la función HSET para almacenar 
los resultados en Redis utilizando claves distintas para cada conjunto de datos.

Convertir los resultados en diccionarios (o estructuras hash):

Los resultados obtenidos de la base de datos y de la API se convierten en 
diccionarios (o en términos de Redis, estructuras de tipo hash) para que puedan ser 
fácilmente manipulados y comparados.

Comparación y join de los resultados:

En el hilo principal, se accede a los diccionarios almacenados en 
Redis que contienen los resultados de la base de datos y de la API. 
Se realiza la comparación y el join de los datos según sea necesario para 
obtener el conjunto de datos combinado.

Generación de la respuesta en formato JSON:

A partir del conjunto de datos resultante del join, se genera una respuesta en 
formato JSON que contiene solamente los dos atributos necesarios de cada objeto.


es necesario dejar los resultados de la respuesta de la api
(que ya me tome el trabajo de transformarlos a tabla hash) en cache por un 
tiempo mas que los resultados de la bd, que puedo deshechar en seguida despues de usarlos, 
porque la llamada a la api, es posible que me sirva para sucesivas comparaciones 
con los resultados de las distintas librerias (bases de datos)

esto se logra:
# Almacenar los resultados de la API en Redis con una expiración prolongada
redis.hset('api_results', 'api_key', 'api_value')
redis.expire('api_results', 3600)  # Configurar la expiración en 1 hora (en segundos)

# Almacenar los resultados de la base de datos en Redis con una expiración breve
redis.hset('db_results', 'db_key', 'db_value')
redis.expire('db_results', 300)  # Configurar la expiración en 5 minutos (en segundos)

'''