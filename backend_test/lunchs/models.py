from uuid import uuid4

from django.db import models

from ..users.models import Employee


class Dish(models.Model):
    main = models.CharField(max_length=100)
    side_order = models.TextField()

    class Meta:
        db_table = "dish"
        verbose_name_plural = "dishes"
        ordering = ["-pk"]


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateField()
    is_open = models.BooleanField(default=True)
    dishes = models.ManyToManyField("Dish", related_name="dishes_in_menu")

    class Meta:
        db_table = "menu"
        ordering = ["-date"]


class Order(models.Model):
    customization = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "order"
        unique_together = (('employee', 'date'),)
        ordering = ["-date"]
