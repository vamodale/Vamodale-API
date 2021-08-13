import sqlalchemy as sa

from database import DatabaseConnector

usuario_evento = sa.Table( "usuario_evento", DatabaseConnector.get_base_model().metadata,
    sa.Column( 'id_usuario', sa.Integer, sa.ForeignKey( 'usuario.id' ) ),
    sa.Column( 'id_evento', sa.Integer, sa.ForeignKey( 'evento.id' ) )
)