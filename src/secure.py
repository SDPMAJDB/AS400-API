from fastapi import HTTPException, Header
from src.config import Configuration_serveurs

class Secure:
    @staticmethod
    def verify_api_key(x_api_key: str = Header(None)) -> None:
        config = Configuration_serveurs()
        if x_api_key != config.api_key:
            print(x_api_key)
            print(config.api_key)
            raise HTTPException(status_code=401, detail="Invalid API Key")
