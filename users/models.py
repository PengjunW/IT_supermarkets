from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class Users(AbstractUser):
    """Customized model"""
    account_balance = models.FloatField(null=True, default=0.0)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.id
