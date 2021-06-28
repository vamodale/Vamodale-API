from sqlalchemy import Column, Date, BigInteger, String, ForeignKey, Integer, CheckConstraint

from src.database import BaseModel, DatabaseConnector
from src.model.schema import Usuario
from src.enums import ModalidadeEnum, EsportesEnum

class Event( BaseModel, DatabaseConnector.get_base_model() ):
    __tablename__ = "evento"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_criador = Column(BigInteger, ForeignKey(Usuario.id))
    created_at = Column(Date, nullable=False)
    nome = Column(String(100), nullable=False)
    esporte = Column(Integer, CheckConstraint( f"modalidade IN {EsportesEnum.to_sql_list()}" ), nullable=False )
    coord_x = Column(Integer, nullable=False)
    coord_y = Column(Integer, nullable=False)
    data_evento = Column(Date, nullable=False)
    modalidade = Column(Integer, CheckConstraint( f"modalidade IN {ModalidadeEnum.to_sql_list()}" ), nullable=False, default = 1 )
    num_vagas = Column(Integer, nullable=True)

