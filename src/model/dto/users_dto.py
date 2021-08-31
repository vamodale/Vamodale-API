from typing import List

class UserDTO:
    id = int()
    nome = str()
    apelido = str()
    esportes = List[int]
    genero = str()
    idade = int()
    cidade = str()
    profile_picture = str()
    
    def __init__(self, user):
        self.id = user.id
        self.nome = user.nome
        self.apelido = user.apelido
        self.genero = user.genero
        self.idade = user.idade
        self.cidade = user.cidade
        self.profile_picture = user.profile_picture

    def to_dict(self):
        return self.__dict__
