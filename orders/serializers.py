import time

from rest_framework import serializers

from goods.models import Goods
from goods.serializers import GoodsSerializers
from orders.models import Orders, ShoppingCart, OrderGoods


class OrderManagement(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ShopCartSerializer(serializers.Serializer):
    # Get the currently logged in user
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label="number", min_value=1,
                                    error_messages={
                                        "min_value": "goods number cannot be less than one",
                                        "required": "Please choose purchase number"
                                    })
    # Here is the inheritance serializer. You must specify the queryset object.
    # If you inherit the model serializer, you do not need to specify it
    # Goods is a foreign key, which can be used to obtain all the values in the goods object
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    # The inherited serializer has no save function and must write a create method
    def create(self, validated_data):
        # validated_data is the Processed data
        # G et current user
        #  in view :self.request.user；in serializer:self.context["request"].user
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)
        # num + 1 if recorded in cart
        # If the shopping cart has no record, it is created
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            # add to shopCart
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        # modify good number
        instance.nums = validated_data["nums"]
        instance.save()
        return instance


# good in shopping cart
class ShopCartDetailSerializer(serializers.ModelSerializer):
    '''
    Shopping cart good detail information
    '''
    # one shopping cat mapping to one good
    goods = GoodsSerializers(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "nums")


# good in order
class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializers(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


# good in order
# goods need to use OrderGoodsSerializer
class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = Orders
        fields = "__all__"


class OrderInfoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # No post is required when generating orders
    order_id = serializers.CharField(read_only=True)
    order_status = serializers.IntegerField(read_only=True)
    order_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    pay_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    def generate_order_id(self):
        # Generate order number
        # Current time + userid + random number
        from random import Random
        random_ins = Random()
        order_id = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_id

    def validate(self, attrs):
        # Add order in validate_id, and then save in the view
        attrs["order_id"] = self.generate_order_id()
        return attrs

    class Meta:
        model = Orders
        fields = "__all__"
