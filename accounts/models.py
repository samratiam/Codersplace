from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    USER_CHOICES = (
        ('Company', 'Company'),
        ('Coder', 'Coder'),
    )
    account_type = models.CharField(
        max_length=30, choices=USER_CHOICES, null=True, blank=True)
