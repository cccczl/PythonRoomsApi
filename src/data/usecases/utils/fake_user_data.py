from faker import Faker

from src.domain.models.user import UserCreate, UserPatch

fake = Faker()


def create_fake_user():
    """Util to create a fake user"""

    return UserCreate(
        email="johndoe@test.com",
        role=1,
        first_name=fake.name(),
        last_name=fake.name(),
        bio=fake.text(),
        is_active=fake.boolean(),
    )


def patch_fake_user():
    """Util to patch a fake user"""

    return UserPatch(
        email="johndoepatch@test.com",
        role=1,
        first_name=fake.name(),
        last_name=fake.name(),
        bio=fake.text(),
    )
