"""Add Connection options column (JSON)

Revision ID: fa9cefccac47
Revises: 3f6e32040035
Create Date: 2024-08-15 13:02:24.137632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa9cefccac47"
down_revision: Union[str, None] = "3f6e32040035"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("connections", schema=None) as batch_op:
        batch_op.add_column(sa.Column("options", sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("connections", schema=None) as batch_op:
        batch_op.drop_column("options")

    # ### end Alembic commands ###
