"""fixed users_in_role

Revision ID: 66d86fb2583f
Revises: 147ce8d245ad
Create Date: 2024-08-19 16:54:51.126435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66d86fb2583f'
down_revision: Union[str, None] = '147ce8d245ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_in_role', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('users_in_role', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users_in_role', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'users_in_role', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users_in_role', type_='foreignkey')
    op.drop_constraint(None, 'users_in_role', type_='foreignkey')
    op.drop_column('users_in_role', 'role_id')
    op.drop_column('users_in_role', 'user_id')
    # ### end Alembic commands ###
