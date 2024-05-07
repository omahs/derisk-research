"""init database add notification data

Revision ID: 7d6aefb54f92
Revises: 
Create Date: 2024-05-07 22:31:34.699596

"""

from enum import Enum
from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7d6aefb54f92"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# credit by web_app/utils/values.py
class ProtocolIDs(Enum):
    HASHSTACK: str = "Hashstack"
    NOSTRA: str = "Nostra"
    ZKLEND: str = "zkLend"


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notification",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("wallet_id", sa.String(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column(
            "ip_address",
            sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
            nullable=False,
        ),
        sa.Column("health_ratio_level", sa.Float(), nullable=False),
        sa.Column(
            "protocol_id",
            sqlalchemy_utils.types.choice.ChoiceType(ProtocolIDs),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_index(
        op.f("ix_notification_email"), "notification", ["email"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_notification_email"), table_name="notification")
    op.drop_table("notification")
    # ### end Alembic commands ###
