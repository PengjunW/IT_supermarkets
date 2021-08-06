import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_supermarket.settings')

import django

django.setup()
from goods.models import Goods
from orders.models import Orders
from users.models import Users


def populate():
    for i in range(1, 5):
        user = {'id': i, ' user_name': "a" + str(i), 'email': "12345@gmail.com",'password': 123456, }
        add_user(user['id'], user[' user_name'], user['email'],user['password'])

    goods = {'goods_id': 1, 'goods_name': 'huawei', 'price': 100, 'inventory_num': 1000}
    add_goods(goods['goods_id'], goods['goods_name'], goods['price'], goods['inventory_num'])
    goods = {'goods_id': 2, 'goods_name': 'huawei', 'price': 200, 'inventory_num': 1000}
    add_goods(goods['goods_id'], goods['goods_name'], goods['price'], goods['inventory_num'])
    goods = {'goods_id': 3, 'goods_name': 'apple', 'price': 300, 'inventory_num': 1000}
    add_goods(goods['goods_id'], goods['goods_name'], goods['price'], goods['inventory_num'])
    goods = {'goods_id': 4, 'goods_name': 'oppo', 'price': 400, 'inventory_num': 1000}
    add_goods(goods['goods_id'], goods['goods_name'], goods['price'], goods['inventory_num'])

    for i in range(1, 5):
        order = {'id': i,'user_id':i, 'order_status': 1, 'charge': 100}
        add_order(order['id'], order['user_id'],order['order_status'], order['charge'])


def add_order(id, userid, order_status=1, charge=100):
    o = Orders.objects.get_or_create(id=id,user_id = userid)[0]
    o.order_status = order_status

    o.charge = charge
    o.save()


def add_user(id, usename,email, password):
    u = Users.objects.get_or_create(id=id)[0]
    u.username = usename
    u.email =email
    u.password = password
    u.save()


def add_goods(goods_id, goods_name, price=100, inventory_num=100):
    g = Goods.objects.get_or_create(goods_id=goods_id)[0]
    g.goods_name = goods_name
    g.price = price
    g.inventory_num = inventory_num
    g.save()


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    print("finish")
