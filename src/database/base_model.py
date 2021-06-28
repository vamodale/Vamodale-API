from .db_connector import DatabaseConnector

class BaseModel(DatabaseConnector):
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
        try:
            with self.get_session() as session:
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

    def from_dict(self, dict):
        try:
            self.__dict__ = dict
        except Exception as e:
            raise e

