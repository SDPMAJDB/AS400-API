from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from src.db_request import DB400, DB400Error
from src.db_connect import ConnectionError
from src.secure import Secure

class Query(BaseModel):
    type: str
    query: str

app = FastAPI(
    title="DB400 API",
    description="API for executing queries on IBM i DB2 database",
    version="1.0.0",
)
db400 = DB400()

@app.post("/execute")
def execute_query(query: Query, authorization: str = Depends(Secure.verify_api_key)):
    try:
        result = db400.execute(query.type, query.query)
        return result
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail="Database connection error")
    except DB400Error as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")