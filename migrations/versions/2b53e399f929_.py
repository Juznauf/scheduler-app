"""empty message

Revision ID: 2b53e399f929
Revises: 
Create Date: 2020-05-29 05:53:11.783116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b53e399f929'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('holidays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('leaves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.Column('note', sa.String(length=140), nullable=True),
    sa.Column('halfdaybegin', sa.Boolean(), nullable=True),
    sa.Column('halfdayend', sa.Boolean(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leaves')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('holidays')
    # ### end Alembic commands ###
