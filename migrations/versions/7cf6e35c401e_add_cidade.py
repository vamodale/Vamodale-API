"""Add cidade

Revision ID: 7cf6e35c401e
Revises: e307f49bb08e
Create Date: 2021-08-31 12:04:47.928825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cf6e35c401e'
down_revision = 'e307f49bb08e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evento', sa.Column('cidade', sa.String(length=255), nullable=True))
    op.execute(f"UPDATE evento SET cidade = '""'")
    op.alter_column(f'evento', 'cidade', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuario_evento', type_='foreignkey')
    op.drop_constraint(None, 'usuario_evento', type_='foreignkey')
    op.create_foreign_key('usuario_evento_id_usuario_fkey', 'usuario_evento', 'usuario', ['id_usuario'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('usuario_evento_id_evento_fkey', 'usuario_evento', 'evento', ['id_evento'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'usuario', type_='unique')
    op.drop_constraint(None, 'usuario', type_='unique')
    op.create_unique_constraint('usuario_email_openid_key', 'usuario', ['email', 'openid'])
    op.drop_constraint(None, 'evento', type_='foreignkey')
    op.create_foreign_key('evento_id_criador_fkey', 'evento', 'usuario', ['id_criador'], ['id'], ondelete='CASCADE')
    op.drop_column('evento', 'cidade')
    # ### end Alembic commands ###
