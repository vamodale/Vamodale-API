from typing import List, Tuple
from datetime import datetime

from controller import users_controller
from enums import ModalidadeEnum, EsportesEnum

class EventDTO:
    id = int()
    data = datetime
    id_criador = int()
    esporte = EsportesEnum
    jogadores = List[int]
    modalidade = ModalidadeEnum.CASUAL
    num_vagas = int()
    endereco = dict()
    criador = str()
    
    def __init__(self, event):
        self.id = event.id
        self.nome = event.nome
        self.data = event.data_evento
        self.id_criador = event.id_criador
        self.nome_criador = users_controller.get_user(event.id_criador).nome
        self.criador = f"/v1/users/{event.id_criador}"
        self.esporte = EsportesEnum(event.esporte).name
        self.jogadores = [ {
             'nome': user.nome,
             'apelido': user.apelido,
             'profile_picture': user.profile_picture, 
             'href': f"/v1/users/{user.id}" 
        } for user in event.get_jogadores() ]
        self.modalidade = ModalidadeEnum(event.modalidade).name 
        self.num_vagas = event.num_vagas if event.num_vagas is not None else None 
        self.endereco = {
            'cep': event.cep,
            'rua': event.rua,
            'bairro': event.bairro,
            'numero': event.numero,
            'complemento': event.complemento
        }

    def to_dict(self):
        return self.__dict__
