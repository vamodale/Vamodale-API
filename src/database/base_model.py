from .db_connector import DatabaseConnector
from time import sleep
import datetime

from sqlalchemy import Column, BigInteger, DateTime

class BaseModel(DatabaseConnector):
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self):
        self.metadata.create_all(DatabaseConnector.get_engine())
        super().__init__()
    
    @classmethod
    def get_by_id(cls, id) -> object:
        try:
            with cls.get_session() as session:
                return session.query(cls).filter(cls.id == id).first()
        except Exception as e:
            raise e
        
    def save(self) -> None:
        with self.get_session() as session:
            try:
                session.add(self)
            except Exception as e:
                raise e

    def to_dict(self) -> dict:
        try:
            data = self.__dict__
            if '_sa_instance_state' in data:
                del data['_sa_instance_state']
            return data
        except Exception as e:
            raise e
    
    def bound_session( self, session ):
        self._sa_instance_state.session_id = session.hash_key

    @classmethod
    def from_dict(cls, dict):
        model = cls()
        try:
            model.__dict__.update( dict )
        except Exception as e:
            raise e
        finally:
            return model

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)
        
    @classmethod
    def search(cls, **kwargs):
        try:
            with DatabaseConnector.get_session() as session:
                query = session.query(cls)
                for key, value in kwargs.items():
                    query = query.filter( cls.__dict__[key] == value )
                return query.all()
        except Exception as e:
            raise e
