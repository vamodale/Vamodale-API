import sqlalchemy as sa

from database import BaseModel, DatabaseConnector

class Usuario(BaseModel, DatabaseConnector.get_base_model()):
    __tablename__ = "usuario"
    
    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.String(255), nullable=False)
    apelido = sa.Column(sa.String(60), nullable=True)
    idade = sa.Column(sa.Integer, nullable=False)
    genero = sa.Column(sa.String(1), nullable=False)
    profile_picture = sa.Column(sa.String(255), nullable=True)
    cidade = sa.Column(sa.String(255), nullable=False)
