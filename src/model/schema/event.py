import datetime

from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer, CheckConstraint, DateTime, inspect
from sqlalchemy.orm import relationship, backref

from database import BaseModel, DatabaseConnector
from model.schema import Usuario
from model.dto import EventDTO
from enums import ModalidadeEnum, EsportesEnum

class Event( BaseModel, DatabaseConnector.get_base_model() ):
    __tablename__ = "evento"

    id_criador = Column(BigInteger, ForeignKey(Usuario.id), nullable=False)
    nome = Column(String(100), nullable=False)
    esporte = Column(Integer, CheckConstraint( f"esporte IN {EsportesEnum.to_sql_list()}" ), nullable=False )
    coord_x = Column(Integer, nullable=False)
    coord_y = Column(Integer, nullable=False)
    data_evento = Column(DateTime, nullable=False)
    modalidade = Column(Integer, CheckConstraint( f"modalidade IN {ModalidadeEnum.to_sql_list()}" ), nullable=False, default = 1 )
    num_vagas = Column(Integer, nullable=True)
    jogadores = relationship( "Usuario", secondary='usuario_evento', backref=backref( "eventos", lazy='subquery' ) )
 
    def add_jogador( self, user ):
        with self.get_session() as session:
            try:    
                self.bound_session(session)
                self.jogadores.append( user )
            except Exception as e:
                raise e
