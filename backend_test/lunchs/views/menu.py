from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import MenuForm
from ..models import Menu


class MenuMixin(LoginRequiredMixin):
    model = Menu
    success_url = reverse_lazy('lunchs:list_menu')


class DetailMenu(DetailView):
    model = Menu


class ListMenu(MenuMixin, ListView):
    pass


class CreateMenu(MenuMixin, CreateView):
    form_class = MenuForm


class EditMenu(MenuMixin, UpdateView):
    form_class = MenuForm


class DeleteMenu(MenuMixin, DeleteView):
    pass
