from django.db import models


# Create your models here.


class Goods(models.Model):
    GOODS_STATUS = (
        (1, 'For sale'),
        (2, 'On sale'),
        (3, 'Out of stock'),
        (4, 'Prepare for sale')
    )

    goods_id = models.AutoField(primary_key=True)
    goods_name = models.TextField(default=0.0)
    price = models.FloatField(default=0.0)
    status = models.IntegerField(choices=GOODS_STATUS, default=1)
    inventory_num = models.IntegerField(default=0)
    goods_brief_description = models.TextField(max_length=500)

    # goods_images = models.ImageField(upload_to="goods/images/", null=True, blank=True)

    class Meta:
        db_table = 'goods'
