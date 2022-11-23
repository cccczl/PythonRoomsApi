from faker import Faker

from src.domain.models.sections import SectionCreate, SectionPatch

fake = Faker()


def create_fake_section(course_id: int = 1):
    """Util to create a fake section"""

    return SectionCreate(
        title=fake.sentence(),
        description=fake.text(),
        content_type=1,
        grade_media=fake.random_int(),
        course_id=course_id,
    )


def patch_fake_section(course_id: int = 1):
    """Util to patch a fake section"""

    return SectionPatch(
        title=fake.sentence(),
        description=fake.text(),
        content_type=1,
        grade_media=fake.random_int(),
        course_id=course_id,
    )
