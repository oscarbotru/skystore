from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    phone = models.CharField(max_length=50, **NULLABLE)
    email = models.EmailField(_('email address'), unique=True)
    country = models.CharField(max_length=150, **NULLABLE)

    verification_key = models.CharField(max_length=150, **NULLABLE)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
