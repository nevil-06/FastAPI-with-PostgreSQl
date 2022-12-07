"""First Revision

Revision ID: f18bd05f2020
Revises: 
Create Date: 2022-12-01 17:10:17.559350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f18bd05f2020'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("User",
    sa.Column("blood_group",)
    )


def downgrade() -> None:
    pass
