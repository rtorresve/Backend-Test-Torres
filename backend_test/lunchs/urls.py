from django.urls import path
from .views.dish import (
    ListDish, CreateDish, DetailDish, EditDish, DeleteDish)
from .views.menu import (
    ListMenu, CreateMenu, DetailMenu, EditMenu, DeleteMenu)
from .views.order import (
    ListOrder, CreateOrder, DetailOrder, EditOrder, DeleteOrder)

app_name = "lunchs"

urlpatterns = [
    path("dish/", ListDish.as_view(), name="list_dish"),
    path("dish/<pk>/", DetailDish.as_view(), name="detail_dish"),
    path("dish-create/", CreateDish.as_view(), name="create_dish"),
    path("dish-edit/<pk>/", EditDish.as_view(), name="edit_dish"),
    path("dish-delete/<pk>/", DeleteDish.as_view(), name="delete_dish"),
    path("menu/", ListMenu.as_view(), name="list_menu"),
    path("menu/<pk>/", DetailMenu.as_view(), name="detail_menu"),
    path("menu-create/", CreateMenu.as_view(), name="create_menu"),
    path("menu-edit/<pk>/", EditMenu.as_view(), name="edit_menu"),
    path("menu-delete/<pk>/", DeleteMenu.as_view(), name="delete_menu"),
    path("order/", ListOrder.as_view(), name="list_order"),
    path("order/<pk>/", DetailOrder.as_view(), name="detail_order"),
    path("order-create/", CreateOrder.as_view(), name="create_order"),
    path("order-edit/<pk>/", EditOrder.as_view(), name="edit_order"),
    path("order-delete/<pk>/", DeleteOrder.as_view(), name="delete_order"),
]
