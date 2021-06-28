from enum import IntEnum

class EsportesEnum(IntEnum):
    FUTEBOL = 1
    FUTSAL = 2
    VOLEI = 3
    BASQUETE = 4
    HANDEBOL = 5
    OUTROS = -1

    @classmethod
    def to_sql_list(cls):
        return f"({','.join( ( str(enum.value) for enum in cls ) )})"