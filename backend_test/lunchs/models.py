from uuid import uuid4

from django.db import models
from django.urls.base import reverse

from ..users.models import Employee

APP_NAME = "lunchs"


class Dish(models.Model):
    main = models.CharField(max_length=100)
    side_order = models.TextField()

    class Meta:
        db_table = "dish"
        verbose_name = "dish"
        verbose_name_plural = "dishes"
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_absolute_url(self):
        return reverse(f"{APP_NAME}:detail_dish", kwargs={"pk": self.pk})


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateField()
    is_open = models.BooleanField(default=True)
    dishes = models.ManyToManyField("Dish", related_name="dishes_in_menu", through='MenuDish')

    class Meta:
        db_table = "menu"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}: {self.id}"

    def get_absolute_url(self):
        return reverse(f"{APP_NAME}:detail_menu", kwargs={"pk": self.pk})


class MenuDish(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


class Order(models.Model):
    customization = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "order"
        unique_together = (('employee', 'date'),)
        ordering = ["-date"]

    def __str__(self):
        return f"{self.pk}: {self.employee.username}"

    def get_absolute_url(self):
        return reverse(f"{APP_NAME}:detail_order", kwargs={"pk": self.pk})
