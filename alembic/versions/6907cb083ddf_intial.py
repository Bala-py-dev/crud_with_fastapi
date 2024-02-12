"""intial

Revision ID: 6907cb083ddf
Revises: 
Create Date: 2024-02-12 18:20:48.712528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6907cb083ddf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_id', sa.Integer),
        sa.Column('q', sa.String(200)),
    )

def downgrade():
    op.drop_table('items')
