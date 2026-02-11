import pandas as pd
from pymongo import MongoClient
import os

class DataManager:
    def __init__(self):
        # En Docker, el hostname es el nombre del servicio en el docker-compose
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client["tu_base_de_datos"]
        self.amazon_df = None

    def load_market_data(self, path: str):
        """Carga el universo de Amazon desde Parquet"""
        self.amazon_df = pd.read_parquet(path)
        print(f"📊 Dataset de Amazon cargado: {len(self.amazon_df)} productos.")

    def get_my_product(self, request_id: str):
        """Busca tu producto en tu base de datos Mongo"""
        return self.db.productos.find({"request_id": request_id})