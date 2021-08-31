"""Add user table

Revision ID: f01d13dee9ff
Revises: 3b54c1808aa1
Create Date: 2021-07-14 22:31:29.575658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f01d13dee9ff'
down_revision = '3b54c1808aa1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('usuario', sa.Column('nome', sa.String(length=255), nullable=False))
    op.add_column('usuario', sa.Column('apelido', sa.String(length=60), nullable=True))
    op.add_column('usuario', sa.Column('idade', sa.Integer(), nullable=False))
    op.add_column('usuario', sa.Column('genero', sa.String(length=1), nullable=False))
    op.add_column('usuario', sa.Column('profile_picture', sa.String(length=255), nullable=True))
    op.add_column('usuario', sa.Column('cidade', sa.String(length=255), nullable=False))


def downgrade():
    op.drop_column('usuario', 'cidade')
    op.drop_column('usuario', 'profile_picture')
    op.drop_column('usuario', 'genero')
    op.drop_column('usuario', 'idade')
    op.drop_column('usuario', 'apelido')
    op.drop_column('usuario', 'nome')
