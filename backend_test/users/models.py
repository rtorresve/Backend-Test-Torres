from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class User(AbstractUser):
    """Default user for project."""
    class Types(models.TextChoices):
        COOK = "COOK", "Cook"
        EMPLOYEE = "EMPLOYEE", "Employee"

    #: Ensures that creating new users through proxy models works
    base_type = Types.EMPLOYEE

    #: What type of user are we?
    type = models.CharField(max_length=50, choices=Types.choices, default=Types.EMPLOYEE)
    #: Where work the user?
    country = CountryField(blank_label='(select country)')

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class CookManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.COOK)


class Cook(User):
    base_type = User.Types.COOK
    objects = CookManager()

    class Meta:
        proxy = True


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)


class Employee(User):
    base_type = User.Types.EMPLOYEE
    objects = CookManager()

    class Meta:
        proxy = True
