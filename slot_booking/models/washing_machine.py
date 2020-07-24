from django.db import models


class WashingMachine(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    is_active = models.BooleanField(default=True)
