from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import DishForm
from ..models import Dish


class DishMixin(LoginRequiredMixin):
    model = Dish
    success_url = reverse_lazy('lunchs:list_dish')


class DetailDish(DetailView):
    model = Dish


class ListDish(DishMixin, ListView):
    pass


class CreateDish(DishMixin, CreateView):
    form_class = DishForm


class EditDish(DishMixin, UpdateView):
    form_class = DishForm


class DeleteDish(DishMixin, DeleteView):
    pass
