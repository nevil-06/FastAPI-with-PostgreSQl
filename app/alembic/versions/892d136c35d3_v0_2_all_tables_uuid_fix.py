"""v0.2 all tables uuid fix

Revision ID: 892d136c35d3
Revises: 7f9c1bf5c8b2
Create Date: 2022-12-10 16:17:40.366922

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '892d136c35d3'
down_revision = '7f9c1bf5c8b2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('competition',
    sa.Column('comp_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('comp_id')
    )
    op.create_table('entry',
    sa.Column('entry_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('comp_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comp_id'], ['competition.comp_id'], ),
    sa.PrimaryKeyConstraint('entry_id')
    )
    op.drop_table('Entry')
    op.drop_table('Competition')
    op.drop_table('User')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='User_pkey'),
    sa.UniqueConstraint('email', name='User_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Competition',
    sa.Column('comp_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.user_id'], name='Competition_user_id_fkey'),
    sa.PrimaryKeyConstraint('comp_id', name='Competition_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Entry',
    sa.Column('entry_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('comp_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['comp_id'], ['Competition.comp_id'], name='Entry_comp_id_fkey'),
    sa.PrimaryKeyConstraint('entry_id', name='Entry_pkey')
    )
    op.drop_table('entry')
    op.drop_table('competition')
    op.drop_table('user')
    # ### end Alembic commands ###