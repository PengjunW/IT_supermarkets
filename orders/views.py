from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from orders.models import Orders, OrderGoods
from orders.serializers import OrderInfoSerializer, OrderDetailSerializer, ShopCartDetailSerializer, \
    ShopCartSerializer,OrderManagement
from .models import ShoppingCart
from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView


class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    Shopping Cart function
    list:
        get shopping cart detail information
    create：
        add to cart
    delete：
        delete shopping record
    """

    serializer_class = ShopCartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    #  good id
    lookup_field = "goods_id"

    # get shopping cart list
    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    # Inventory number- 1
    def perform_create(self, serializer):
        shop_cart = serializer.save()
        goods = shop_cart.goods
        goods.inventory_num -= shop_cart.nums
        goods.save()

    # Inventory number+1
    def perform_destroy(self, instance):
        goods = instance.goods
        goods.inventory_num += instance.nums
        goods.save()
        instance.delete()

    # update Inventory number,The modification may be to add pages or reduce pages
    def perform_update(self, serializer):
        # get the inventory quantity before modification
        existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
        existed_nums = existed_record.nums
        #  save existed_nums
        saved_record = serializer.save()
        # Number of changes
        nums = saved_record.nums - existed_nums
        goods = saved_record.goods
        goods.inventory_num -= nums
        goods.save()


class OrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OrderInfoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['order_id', 'order_status']
    ordering_fields = ['order_id']

    # config serializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderInfoSerializer

    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        order = serializer.save()
        temp = 0
        # Get all items in shopping cart
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()
            temp += shop_cart.goods.price * shop_cart.nums
            # empty cart
            shop_cart.delete()
        order.charge = temp
        order.save()
        return order

class OrderDelete(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = OrderManagement
    queryset = Orders.objects.all()

class MangageOrder(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = OrderManagement
    queryset = Orders.objects.all()