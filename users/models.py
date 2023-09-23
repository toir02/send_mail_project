from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    key = models.IntegerField(verbose_name='ключ', **NULLABLE)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
