import os

import pytest

from .lunchs.models import Dish, Menu, Order
from .lunchs.tests.factories import DishFactory, MenuFactory, OrderFactory

from .users.models import User
from .users.tests.factories import UserFactory


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_test.settings")


@pytest.fixture(autouse=True)
def user() -> User:
    return UserFactory()


@pytest.fixture(autouse=True)
def dish() -> Dish:
    return DishFactory()


@pytest.fixture(autouse=True)
def menu() -> Menu:
    return MenuFactory()


@pytest.fixture(autouse=True)
def order() -> Order:
    return OrderFactory()
