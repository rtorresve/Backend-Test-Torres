from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from vanilla import CreateView, DeleteView, ListView, UpdateView

from ..forms import MenuForm
from ..models import Menu


class MenuMixin:
    model = Menu
    success_url = reverse_lazy('lunchs:list_menu')


@method_decorator(login_required, name='dispatch')
class ListMenu(MenuMixin, ListView):
    pass


@method_decorator(login_required, name='dispatch')
class CreateMenu(MenuMixin, CreateView):
    form_class = MenuForm


@method_decorator(login_required, name='dispatch')
class EditMenu(MenuMixin, UpdateView):
    form_class = MenuForm


@method_decorator(login_required, name='dispatch')
class DeleteMenu(MenuMixin, DeleteView):
    pass
