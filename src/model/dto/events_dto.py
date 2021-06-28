from typing import List, Tuple
from datetime import datetime

from enums import ModalidadeEnum, EsportesEnum

class EventsDTO:
    data = datetime()
    id_criador = int()
    esporte = EsportesEnum
    jogadores = List[int]
    modalidade = ModalidadeEnum.CASUAL
    num_vagas = int()
    coordenadas_local = Tuple[int]

    def __init__(self, event):

