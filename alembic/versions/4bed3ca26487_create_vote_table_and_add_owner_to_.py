"""create vote table and add owner to posts table

Revision ID: 4bed3ca26487
Revises: bbeafa40431b
Create Date: 2022-11-10 11:01:50.946376

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4bed3ca26487'
down_revision = 'bbeafa40431b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
