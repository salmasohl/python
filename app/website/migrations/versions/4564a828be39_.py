"""empty message

Revision ID: 4564a828be39
Revises: 
Create Date: 2022-05-29 19:15:18.961102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4564a828be39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updated', sa.DateTime(), nullable=False))
    op.drop_index('ix_Users_email', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_Users_email', 'users', ['email'], unique=False)
    op.drop_column('users', 'updated')
    # ### end Alembic commands ###
