"""Create adress for users column

Revision ID: ce7985ecd793
Revises: 
Create Date: 2026-09-01 08:37:13.475990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce7985ecd793'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('users', sa.Column('adress', sa.String(), nullable = True))


def downgrade() -> None:
    op.drop_column('users', 'adress')
