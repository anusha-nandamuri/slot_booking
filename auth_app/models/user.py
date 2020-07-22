from django.db import models
from django.contrib.auth.models import AbstractUser

from auth_app.constants.enums.enums import Gender


class User(AbstractUser):
    gender_choices = Gender.get_list_of_tuples()
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices, null=True)
    job_role = models.CharField(max_length=100, null=True)
    Department = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
