import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref

from database import BaseModel, DatabaseConnector

class Usuario(BaseModel, DatabaseConnector.get_base_model()):
    __tablename__ = "usuario"
    
    nome = sa.Column(sa.String(255), nullable=False)
    apelido = sa.Column(sa.String(60), nullable=True)
    profile_picture = sa.Column(sa.String(255), nullable=True)
    cidade = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False, unique=True)
    openid = sa.Column(sa.String(), nullable=False, unique=True)


    def get_events( self ):
        with self.get_session() as session:
            try:    
                self.bound_session(session)
                return self.eventos
            except Exception as e:
                raise e
    @classmethod
    def login(cls, email, openid) -> object:
        try:
            with cls.get_session() as session:
                return session.query(cls).filter(cls.email == email and cls.openid == openid).first()
        except Exception as e:
            raise e
