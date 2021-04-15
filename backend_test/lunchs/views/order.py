from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from vanilla import CreateView, DetailView, DeleteView, ListView, UpdateView

from ..forms import OrderForm
from ..models import Order


class OrderMixin(LoginRequiredMixin):
    model = Order
    success_url = reverse_lazy('lunchs:list_order')


class DetailOrder(DetailView):
    model = Order


class ListOrder(OrderMixin, ListView):
    pass


class CreateOrder(OrderMixin, CreateView):
    form_class = OrderForm


class EditOrder(OrderMixin, UpdateView):
    form_class = OrderForm


class DeleteOrder(OrderMixin, DeleteView):
    pass
