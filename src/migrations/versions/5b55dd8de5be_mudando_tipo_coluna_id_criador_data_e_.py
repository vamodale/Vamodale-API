"""Mudando tipo coluna id_criador, data e created_by

Revision ID: 5b55dd8de5be
Revises: e2c2cec437af
Create Date: 2021-06-29 18:04:40.150140

"""
from alembic import op
from sqlalchemy import DateTime, func

# revision identifiers, used by Alembic.
revision = '5b55dd8de5be'
down_revision = 'e2c2cec437af'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name='evento',
        column_name='id_criador',
        nullable=False
    )
    op.alter_column(
        table_name='evento',
        column_name='created_at',
        server_default=func.now(),
        type_=DateTime
    )
    op.alter_column(
        table_name='evento',
        column_name='data_evento',
        type_=DateTime
    )

def downgrade():
    pass
