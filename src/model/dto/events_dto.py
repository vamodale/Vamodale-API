from typing import List, Tuple
from datetime import datetime

from enums import ModalidadeEnum, EsportesEnum

class EventDTO:
    data = datetime
    id_criador = int()
    esporte = EsportesEnum
    jogadores = List[int]
    modalidade = ModalidadeEnum.CASUAL
    num_vagas = int()
    coordenadas_local = Tuple[int]
    
    def __init__(self, event):
        self.nome = event.nome
        self.data = event.data_evento
        self.id_criador = event.id_criador
        self.esporte = EsportesEnum(event.esporte).name
        #TODO Relacionar jogadores ao evento
        self.jogadores = None
        self.modalidade = ModalidadeEnum(event.modalidade).name 
        self.num_vagas = event.num_vagas if event.num_vagas is not None else None 
        self.coordenadas_local = { 'x': event.coord_x, 'y': event.coord_y }

    def to_dict(self):
        return self.__dict__
