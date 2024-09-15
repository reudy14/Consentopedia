from storeBase import StoreBase
from os import environ as env

class StorePGVector(StoreBase):
    def __init__(self):
        self.config = {
            "host": env.get("CHIN_PG_HOST"),
            "port": env.get("CHIN_PG_PORT"),
            "user": env.get("CHIN_PG_USER"),
            "password": env.get("CHIN_PG_PASSWORD"),
            "database": env.get("CHIN_PG_DATABASE")
        }
    
    def store(self):
        pass