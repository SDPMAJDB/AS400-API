import src.config
import os

class install:
    def __init__(self):
        cf = src.config.Configuration_serveurs()
        self.AS400_URL = cf.as400_url
        self.AS400_USER = cf.as400_user
        self.AS400_PASSWORD = cf.as400_password
        self.mapping = {"AS400_URL": self.AS400_URL, "AS400_USER": self.AS400_USER, "AS400_PASSWORD": self.AS400_PASSWORD}

    def install(self):
        print("Writing ODBC.ini credentials...")
        fr = open('/etc/odbc.ini', 'r+')
        content = fr.read()
        fr.close()
        f = open('/etc/odbc.ini', 'w+')
        f.write(content.format_map(self.mapping))
        f.close()
        print("Writing ODBC.ini credentials...OK")