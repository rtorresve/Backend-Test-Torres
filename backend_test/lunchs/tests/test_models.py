import pytest
from ..models import Dish, Menu, Order

APP_URL = "/lunchs"
pytestmark = pytest.mark.django_db


def test_dish_get_absolute_url(dish: Dish):
    assert dish.get_absolute_url() == f"{APP_URL}/dish/{dish.pk}/"


def test_menu_get_absolute_url(menu: Menu):
    assert menu.get_absolute_url() == f"{APP_URL}/menu/{menu.pk}/"


def test_user_get_absolute_url(order: Order):
    assert order.get_absolute_url() == f"{APP_URL}/order/{order.pk}/"
