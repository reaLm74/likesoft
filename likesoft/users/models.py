from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )
    date_joined = models.DateTimeField(
        auto_now_add=timezone.now,
        verbose_name="Дата регистрации"
    )
