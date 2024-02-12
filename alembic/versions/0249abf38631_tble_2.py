"""tble_2

Revision ID: 0249abf38631
Revises: 6907cb083ddf
Create Date: 2024-02-12 18:33:34.899290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0249abf38631'
down_revision: Union[str, None] = '6907cb083ddf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'items_tbl',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_id', sa.Integer),
        sa.Column('q', sa.String(200)),
    )

def downgrade():
    op.drop_table('items_tbl')
