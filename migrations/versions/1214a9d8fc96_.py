"""empty message

Revision ID: 1214a9d8fc96
Revises: 8be4f54153da
Create Date: 2023-07-08 17:59:53.767631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1214a9d8fc96'
down_revision = '8be4f54153da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ilustration', schema=None) as batch_op:
        batch_op.alter_column('url_image',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('alias', sa.String(length=30), nullable=True))
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
        batch_op.drop_column('alias')

    with op.batch_alter_table('ilustration', schema=None) as batch_op:
        batch_op.alter_column('url_image',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###
