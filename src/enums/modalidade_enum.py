from enum import IntEnum

class ModalidadeEnum(IntEnum):
    CASUAL = 1
    COMPETITIVO = 2
    
    @classmethod
    def to_sql_list(cls):
        return f"({','.join( ( str(enum.value) for enum in cls ) )})"
        