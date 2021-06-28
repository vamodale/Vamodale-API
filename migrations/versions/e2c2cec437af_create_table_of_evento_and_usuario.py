"""Create table of Evento and Usuario

Revision ID: e2c2cec437af
Revises: 
Create Date: 2021-06-28 00:00:36.773321

"""
from alembic import op

from sqlalchemy import Column, Date, BigInteger, String, ForeignKey, Integer, CheckConstraint

from src.database import BaseModel, DatabaseConnector
from src.model.schema import Usuario
from src.enums import ModalidadeEnum, EsportesEnum

# revision identifiers, used by Alembic.
revision = 'e2c2cec437af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "usuario",
        Column('id', BigInteger, primary_key=True, autoincrement=True)
    )
    op.create_table(
        'evento',
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('id_criador', BigInteger, ForeignKey(Usuario.id)),
        Column('created_at', Date, nullable=False),
        Column('nome', String(100), nullable=False),
        Column('esporte', Integer, CheckConstraint( f"modalidade IN {EsportesEnum.to_sql_list()}" ), nullable=False ),
        Column('coord_x', Integer, nullable=False),
        Column('coord_y', Integer, nullable=False),
        Column('data_evento', Date, nullable=False),
        Column('modalidade', Integer, CheckConstraint( f"modalidade IN {ModalidadeEnum.to_sql_list()}" ), nullable=False, default = 1 ),
        Column('num_vagas', Integer, nullable=True),
    )

def downgrade():
    op.drop_table('evento')
    op.drop_table('usuario')
