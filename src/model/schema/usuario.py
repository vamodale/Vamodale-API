import sqlalchemy as sa

from database import BaseModel, DatabaseConnector

class Usuario(BaseModel, DatabaseConnector.get_base_model()):
    __tablename__ = "usuario"
    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
