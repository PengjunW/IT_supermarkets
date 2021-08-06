import xadmin
# Register your models here.
from orders.models import Orders


class OrdersAdmin(object):
    pass


xadmin.site.register(Orders, OrdersAdmin)
