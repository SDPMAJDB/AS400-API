import pyodbc
from src.config import Configuration_serveurs

class ConnectionError(Exception):
    pass

class CnxAS400:
    def connect(self):
        try:
            config = Configuration_serveurs()
            # conn_str = f'DSN={config.as400_url};UID={config.as400_user};PWD={config.as400_password}'
            conn_str = f'DSN=AS400'
            return pyodbc.connect(conn_str)
        except pyodbc.Error as e:
            raise ConnectionError("Failed to connect to the database") from e