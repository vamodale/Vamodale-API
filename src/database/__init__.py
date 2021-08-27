from .db_connector import DatabaseConnector
from .base_model import BaseModel

def create_db():
    DatabaseConnector.get_base_model().metadata.create_all(DatabaseConnector.get_engine())
