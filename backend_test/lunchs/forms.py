from django import forms
from .models import Dish, Menu, Order


class DishForm(forms.ModelForm):
    side_order = forms.CharField()

    class Meta:
        model = Dish
        fields = ["main", "side_order"]


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ["date"]


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["customization"]
