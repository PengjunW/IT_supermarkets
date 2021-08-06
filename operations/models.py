from datetime import datetime

from django.db import models

# Create your models here.
from goods.models import Goods
from users.models import Users


# User address
class UserAddress(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    province = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    signer_name = models.CharField(max_length=100, default="")
    signer_mobile = models.CharField(max_length=11, default="")
    add_time = models.DateTimeField(default=datetime.now)

    # class Meta:
    # verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
