"""create companies, devs

Revision ID: 5f72c58bf48c
Revises: 7a71dbf71c64
Create Date: 2023-03-15 15:06:20.944586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f72c58bf48c'
down_revision = '7a71dbf71c64'
branch_labels = None
depends_on = None


from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('freebies')