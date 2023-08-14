import os

class Configuration_serveurs:
    def __init__(self):
        self.as400_url = os.getenv('AS400_URL')
        self.as400_user = os.getenv('AS400_USER')
        self.as400_password = os.getenv('AS400_PASSWORD')
        self.api_key = os.getenv('API_KEY')