# AS400-API
Just a simple Restfull API for AS400 DB with odbc connector

***ENVIRONEMENT_VARIABLE***
```
AS400_URL=ip AS/400
AS400_USER=login AS/400
AS400_PASSWORD=password AS/400
TZ=Indian/Reunion
```

***RUNNING COMMAND***  
```
uvicorn main:app --reload --port 45888 --host 0.0.0.0
```