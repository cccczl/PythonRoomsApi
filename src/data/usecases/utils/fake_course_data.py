from faker import Faker

from src.domain.models.course import CourseCreate, CoursePatch

fake = Faker()


def create_fake_course(user_id: int = 1):
    """Util to create a fake course"""

    return CourseCreate(
        title=fake.sentence(),
        description=fake.text(),
        url=fake.url(),
        user_id=user_id,
    )


def patch_fake_course(user_id: int = 1):
    """Util to patch a fake course"""

    return CoursePatch(
        title=fake.sentence(),
        description=fake.text(),
        url=fake.url(),
        user_id=user_id,
    )
