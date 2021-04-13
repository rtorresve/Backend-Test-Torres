from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from vanilla import CreateView, DeleteView, ListView, UpdateView

from ..forms import OrderForm
from ..models import Order


class OrderMixin:
    model = Order
    success_url = reverse_lazy('lunchs:list_order')


@method_decorator(login_required, name='dispatch')
class ListOrder(OrderMixin, ListView):
    pass


@method_decorator(login_required, name='dispatch')
class CreateOrder(OrderMixin, CreateView):
    form_class = OrderForm


@method_decorator(login_required, name='dispatch')
class EditOrder(OrderMixin, UpdateView):
    form_class = OrderForm


@method_decorator(login_required, name='dispatch')
class DeleteOrder(OrderMixin, DeleteView):
    pass
