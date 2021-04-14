import os
import pytest

from .users.models import User
from .users.tests.factories import UserFactory

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_test.settings")


@pytest.fixture(autouse=True)
def user() -> User:
    return UserFactory()
