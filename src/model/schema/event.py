import datetime

from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer, CheckConstraint, DateTime

from database import BaseModel, DatabaseConnector
from model.schema import Usuario
from enums import ModalidadeEnum, EsportesEnum

class Event( BaseModel, DatabaseConnector.get_base_model() ):
    __tablename__ = "evento"

    id_criador = Column(BigInteger, ForeignKey(Usuario.id), nullable=False)
    nome = Column(String(100), nullable=False)
    esporte = Column(Integer, CheckConstraint( f"modalidade IN {EsportesEnum.to_sql_list()}" ), nullable=False )
    coord_x = Column(Integer, nullable=False)
    coord_y = Column(Integer, nullable=False)
    data_evento = Column(DateTime, nullable=False)
    modalidade = Column(Integer, CheckConstraint( f"modalidade IN {ModalidadeEnum.to_sql_list()}" ), nullable=False, default = 1 )
    num_vagas = Column(Integer, nullable=True)
