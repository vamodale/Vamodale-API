import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref

from database import BaseModel, DatabaseConnector

class Usuario(BaseModel, DatabaseConnector.get_base_model()):
    __tablename__ = "usuario"
    
    nome = sa.Column(sa.String(255), nullable=False)
    apelido = sa.Column(sa.String(60), nullable=True)
    idade = sa.Column(sa.Integer, nullable=False)
    genero = sa.Column(sa.String(1), nullable=False)
    profile_picture = sa.Column(sa.String(255), nullable=True)
    cidade = sa.Column(sa.String(255), nullable=False)
