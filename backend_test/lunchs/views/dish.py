from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from vanilla import CreateView, DeleteView, ListView, UpdateView

from ..forms import DishForm
from ..models import Dish


class DishMixin:
    model = Dish
    success_url = reverse_lazy('lunchs:list_dish')


@method_decorator(login_required, name='dispatch')
class ListDish(DishMixin, ListView):
    pass


@method_decorator(login_required, name='dispatch')
class CreateDish(DishMixin, CreateView):
    form_class = DishForm


@method_decorator(login_required, name='dispatch')
class EditDish(DishMixin, UpdateView):
    form_class = DishForm


@method_decorator(login_required, name='dispatch')
class DeleteDish(DishMixin, DeleteView):
    pass
