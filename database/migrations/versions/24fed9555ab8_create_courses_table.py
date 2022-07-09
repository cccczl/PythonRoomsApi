"""create_courses_table

Revision ID: 24fed9555ab8
Revises: 415b6f64c099
Create Date: 2022-07-09 12:34:49.456745

"""
import os
import json
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = "24fed9555ab8"
down_revision = "415b6f64c099"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    courses = op.create_table(
        "courses",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("url", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    with open(os.path.join(os.path.dirname(__file__), "../data/courses.json")) as f:
        course_data = f.read()

    op.bulk_insert(courses, json.loads(course_data))

    op.create_index(op.f("ix_courses_id"), "courses", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_courses_id"), table_name="courses")
    op.drop_table("courses")
    # ### end Alembic commands ###
