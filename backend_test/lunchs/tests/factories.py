from factory import Faker
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory

from ..models import Dish, Menu, MenuDish, Order


user_factory = "backend_test.users.tests.factories.UserFactory"


class DishFactory(DjangoModelFactory):

    main = Faker("sentence", nb_words=2)
    side_order = Faker("sentence", nb_words=4)

    class Meta:
        model = Dish


class MenuFactory(DjangoModelFactory):

    date = Faker("date")
    is_open = Faker("boolean")

    class Meta:
        model = Menu


class GroupLevelFactory(DjangoModelFactory):

    menu = SubFactory(MenuFactory)
    dish = SubFactory(DishFactory)

    class Meta:
        model = MenuDish


class OrderFactory(DjangoModelFactory):

    customization = Faker("sentence", nb_words=2)
    employee = SubFactory(user_factory)
    dish = SubFactory(DishFactory)

    class Meta:
        model = Order
