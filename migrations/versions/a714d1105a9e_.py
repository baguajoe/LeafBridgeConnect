"""empty message

Revision ID: a714d1105a9e
Revises: eae89d58fc8d
Create Date: 2025-02-20 19:52:14.517895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a714d1105a9e'
down_revision = 'eae89d58fc8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.add_column(sa.Column('industry', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('company_size', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('website', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('social_links', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('founded_year', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('verified', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('logo', sa.String(length=255), nullable=True))

    with op.batch_alter_table('job_application', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('resume_file_path', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('decision_notes', sa.Text(), nullable=True))
        batch_op.create_foreign_key(None, 'company', ['company_id'], ['id'])

    with op.batch_alter_table('job_comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('parent_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'job_comment', ['parent_id'], ['id'])
        batch_op.create_foreign_key(None, 'company', ['company_id'], ['id'])

    with op.batch_alter_table('job_posting', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'company', ['company_id'], ['id'])

    with op.batch_alter_table('user_media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'company', ['company_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('company_id')

    with op.batch_alter_table('job_posting', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('company_id')
        batch_op.drop_column('category')

    with op.batch_alter_table('job_comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('parent_id')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('company_id')

    with op.batch_alter_table('job_application', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('decision_notes')
        batch_op.drop_column('resume_file_path')
        batch_op.drop_column('company_id')

    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_column('logo')
        batch_op.drop_column('verified')
        batch_op.drop_column('founded_year')
        batch_op.drop_column('social_links')
        batch_op.drop_column('email')
        batch_op.drop_column('phone')
        batch_op.drop_column('website')
        batch_op.drop_column('company_size')
        batch_op.drop_column('industry')

    # ### end Alembic commands ###
