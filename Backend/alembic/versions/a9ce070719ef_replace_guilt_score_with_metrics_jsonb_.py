"""Replace guilt_score with metrics JSONB in weekly_reports

Revision ID: a9ce070719ef
Revises: fa8aeec17f35
Create Date: 2025-06-18 00:19:16.249966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'a9ce070719ef'
down_revision: Union[str, None] = 'fa8aeec17f35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('weekly_reports', 'guilt_score')

    # Add the new metrics JSONB column
    op.add_column('weekly_reports', sa.Column('metrics', postgresql.JSONB(astext_type=sa.Text()), nullable=False))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('weekly_reports', 'metrics')

    # Re-add the guilt_score column
    op.add_column('weekly_reports', sa.Column('guilt_score', sa.Integer(), nullable=True))
