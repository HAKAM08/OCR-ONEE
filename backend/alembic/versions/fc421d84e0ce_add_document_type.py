"""add document type

Revision ID: fc421d84e0ce
Revises: 6f9fefbb4efd
Create Date: 2026-07-25 19:34:42.620295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc421d84e0ce'
down_revision: Union[str, Sequence[str], None] = '6f9fefbb4efd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "documents",
        sa.Column(
            "document_type",
            sa.String(length=30),
            nullable=True
        )
    )

    op.execute(
        "UPDATE documents SET document_type = 'COMMON'"
    )

    op.alter_column(
        "documents",
        "document_type",
        nullable=False
    )

def downgrade() -> None:
    op.drop_column("documents", "document_type")