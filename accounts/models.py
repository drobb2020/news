from django.db import models  # type: ignore
from django.contrib.auth.models import AbstractUser  # type: ignore


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
