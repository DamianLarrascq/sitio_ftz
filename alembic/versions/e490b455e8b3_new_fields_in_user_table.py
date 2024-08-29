"""new fields in User table

Revision ID: e490b455e8b3
Revises: 8a655eba07ea
Create Date: 2024-08-16 19:36:11.917542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e490b455e8b3'
down_revision: Union[str, None] = '8a655eba07ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dni', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('phone_number', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'dni')
    # ### end Alembic commands ###
