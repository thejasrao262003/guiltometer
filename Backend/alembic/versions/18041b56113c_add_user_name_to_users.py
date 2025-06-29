"""add user_name to users

Revision ID: 18041b56113c
Revises: 04d634817735
Create Date: 2025-06-16 23:40:38.536694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18041b56113c'
down_revision: Union[str, None] = '04d634817735'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_name', sa.String(), nullable=False))
    op.add_column('users', sa.Column('encrypted_password', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'encrypted_password')
    op.drop_column('users', 'user_name')
    # ### end Alembic commands ###
