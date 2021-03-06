"""Init db

Revision ID: 3b54c1808aa1
Revises: 
Create Date: 2021-07-01 00:46:16.578054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b54c1808aa1'
down_revision = None
branch_labels = None
depends_on = None


from enums import EsportesEnum, ModalidadeEnum
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('evento',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id_criador', sa.BigInteger(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('esporte', sa.Integer(), sa.CheckConstraint( f"esporte IN {EsportesEnum.to_sql_list()}" ), nullable=False),
    sa.Column('coord_x', sa.Integer(), nullable=False),
    sa.Column('coord_y', sa.Integer(), nullable=False),
    sa.Column('data_evento', sa.DateTime(), nullable=False),
    sa.Column('modalidade', sa.Integer(), sa.CheckConstraint( f"modalidade IN {ModalidadeEnum.to_sql_list()}" ), nullable=False),
    sa.Column('num_vagas', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_criador'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('evento')
    op.drop_table('usuario')
    # ### end Alembic commands ###
