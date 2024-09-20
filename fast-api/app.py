from fastapi import FastAPI, HTTPException, Query
from connection import listB, getByStudy
import secrets

app = FastAPI(
    title="Backend List SB API",
    description="Standard Bulletin list and select by study",

)

app.secret_key = secrets.token_hex(16)

@app.get('/list')
async def get_list():
    items = listB()
    return {"items": items}

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