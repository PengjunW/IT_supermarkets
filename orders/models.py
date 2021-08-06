from datetime import datetime

from django.db import models

# Create your models here.
from goods.models import Goods
from users.models import Users


# orders info
class Orders(models.Model):
    ORDER_STATUS = (
        (1, "Success"),
        (2, "Failed"),
        (3, "Paying"),
    )

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # good=models.ForeignKey(Goods,on_delete=models.CASCADE)

    order_id = models.CharField(max_length=30, null=True, blank=True, unique=True)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=3)
    order_time = models.DateTimeField(default=datetime.now)
    # nums=models.FloatField(default=0.0)
    charge = models.FloatField(default=0.0)

    class Meta:
        db_table = 'orders'


# Shopping cart
class ShoppingCart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # Quantity of goods purchased
    nums = models.IntegerField(default=0)

    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Shopping Cart'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


# Good detail in order
class OrderGoods(models.Model):
    # one order maps many goods
    # order information
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="goods")
    # two foreignKeys combine one map
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0)

    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Goods in order"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_id)
