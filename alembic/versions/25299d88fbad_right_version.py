"""Right version

Revision ID: 25299d88fbad
Revises: 84076ce67a7c
Create Date: 2023-04-27 23:01:06.096895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25299d88fbad'
down_revision = '84076ce67a7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('position', sa.String(), nullable=True))
    op.add_column('users', sa.Column('speciality', sa.String(), nullable=True))
    op.add_column('users', sa.Column('address', sa.String(), nullable=True))
    op.add_column('users', sa.Column('modified_date', sa.DateTime(), nullable=True))
    op.drop_column('users', 'about')
    op.drop_column('users', 'created_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_date', sa.DATETIME(), nullable=True))
    op.add_column('users', sa.Column('about', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'modified_date')
    op.drop_column('users', 'address')
    op.drop_column('users', 'speciality')
    op.drop_column('users', 'position')
    op.drop_column('users', 'age')
    # ### end Alembic commands ###
