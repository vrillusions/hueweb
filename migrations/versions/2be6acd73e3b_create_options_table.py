"""Create options table

Revision ID: 2be6acd73e3b
Revises: None
Create Date: 2014-08-06 21:05:47.375756

"""

# revision identifiers, used by Alembic.
revision = '2be6acd73e3b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('option', sa.String(length=50), nullable=False),
    sa.Column('value', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('option')
    )
    ### end Alembic commands ###
    op.execute('''\
    CREATE TRIGGER config_updated_at AFTER UPDATE ON config
        FOR EACH ROW
        BEGIN
            UPDATE config SET updated_at = CURRENT_TIMESTAMP
            WHERE option = old.option;
        END;''')



def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config')
    ### end Alembic commands ###
